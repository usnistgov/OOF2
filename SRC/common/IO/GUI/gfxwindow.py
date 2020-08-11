# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import coord
from ooflib.SWIG.common import geometry
from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import progress
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common.IO.GUI.OOFCANVAS import oofcanvasgui
from ooflib.SWIG.common.IO.OOFCANVAS import oofcanvas
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common import subthread
from ooflib.common import utils
from ooflib.common.IO import display
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gfxmenu
from ooflib.common.IO.GUI import gfxwindowbase
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import labelledslider
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import quit
from ooflib.common.IO.GUI import subWindow

from gi.repository import GObject
from gi.repository import Gtk
import threading

# during_callback() is called (by CanvasOutput.show()) only in
# non-threaded mode, so we don't worry about the thread-safety of a
# global variable here.
_during_callback = 0
def during_callback():
    return _during_callback


# TODO: Merge GfxWindow and GfxWindowBase.  There's no need for two
# classes if OOF2 and OOF3D don't share code.

# TODO: Document and simplify the call chains and signals.  Some
# routines (eg, show_contourmap_info) are being called too often.
# What has to be done when the gfxlock is acquired?  What can't be
# done?

class GfxWindow(gfxwindowbase.GfxWindowBase):
    # This whole initialization sequence is complicated. See note in
    # gfxwindowbase.py.  preinitialize() is run from
    # GfxWindowBase.__init__ before the canvas is created, and
    # postinitialize() is run after the canvas is created.  Both are
    # run on the main thread.

    def preinitialize(self, name, gfxmgr, clone):
        debug.mainthreadTest()
        self.gtk = None
        self.closed = None # State data used at window-close time.
        self.name = name
        self.oofcanvas = None
        self.realized = 0
        self.zoomed = 0
        self.settings = ghostgfxwindow.GfxSettings()
        self.mouseHandler = mousehandler.nullHandler # doesn't do anything
        self.rubberband = None

        # Build all the GTK objects for the interior of the box.  These
        # actually get added to the window itself after the SubWindow
        # __init__ call.  They need to be created first so the
        # GhostGfxWindow can operate on them, and then create the menus
        # which are handed off to the SubWindow.

        # The bottom of mainpane contains the layer list.  The top
        # contains everything else.
        self.mainpane = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL,
                                  wide_handle=True)
        gtklogger.setWidgetName(self.mainpane, 'Pane0')
        gtklogger.connect_passive(self.mainpane, 'notify::position')

        # Panes dividing upper pane horizontally into 3 parts.
        # paned1's left half contains paned2.
        self.paned1 = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                                wide_handle=True,
                                margin_bottom=gtkutils.handle_padding)
        gtklogger.setWidgetName(self.paned1, "Pane1")

        self.mainpane.pack1(self.paned1, resize=True, shrink=False)
        gtklogger.connect_passive(self.paned1, 'notify::position')

        # paned2 is in left half of paned1
        self.paned2 = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                                wide_handle=True,
                                margin_right=gtkutils.handle_padding)
        gtklogger.setWidgetName(self.paned2, "Pane2")
        self.paned1.pack1(self.paned2, resize=True, shrink=True)
        gtklogger.connect_passive(self.paned2, 'notify::position')

        # The toolbox is in the left half of paned2 (ie the left frame of 3)
        toolboxframe = Gtk.Frame(margin_end=gtkutils.handle_padding,
                                 margin_start=2)
        toolboxframe.set_shadow_type(Gtk.ShadowType.IN)
        self.paned2.pack1(toolboxframe, resize=True, shrink=True)

        # Box containing the toolbox chooser and the scroll window for
        # the toolbox itself.
        toolboxbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        toolboxframe.add(toolboxbox1)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       spacing=2, margin=2)
        toolboxbox1.pack_start(hbox, expand=False, fill=False, padding=2)
        hbox.pack_start(Gtk.Label("Toolbox:"),
                        expand=False, fill=False, padding=3)
        
        self.toolboxchooser = chooser.ChooserWidget(
            [], callback=self.switchToolbox, name="TBChooser")
        hbox.pack_start(self.toolboxchooser.gtk,
                        expand=True, fill=True, padding=3)

        # Scroll window for the toolbox itself.
        tbscroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(tbscroll, 'TBScroll')

        tbscroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        toolboxbox1.pack_start(tbscroll, expand=True, fill=True, padding=0)

        self.toolboxstack = Gtk.Stack(homogeneous=False)
        tbscroll.add(self.toolboxstack)

        self.toolboxGUIs = []           # GUI wrappers for toolboxes.
        self.current_toolbox = None

        # canvasbox contains the time slider and the canvas
        canvasbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                            margin_start=gtkutils.handle_padding,
                            #margin_end=gtkutils.handle_padding
                            )
        # Setting shrink=False here is necessary so that the canvas'
        # scroll bars are always visible.
        self.paned2.pack2(canvasbox, resize=True, shrink=False)

        # timebox contains widgets for displaying and setting the time
        # for all AnimationLayers in the window.
        self.timebox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                               spacing=2, margin=2)
        gtklogger.setWidgetName(self.timebox, 'time')
        canvasbox.pack_start(self.timebox, expand=False, fill=False, padding=0)
        self.timebox.pack_start(Gtk.Label("time:"), expand=False, fill=False,
                                padding=0)
        self.prevtimeButton = gtkutils.StockButton("go-previous-symbolic")
        gtklogger.setWidgetName(self.prevtimeButton, "prev")
        gtklogger.connect(self.prevtimeButton, 'clicked', self.prevtimeCB)
        self.timebox.pack_start(self.prevtimeButton, expand=False, fill=False,
                                padding=0)
        self.prevtimeButton.set_tooltip_text("Go to the previous stored time.")
        self.nexttimeButton = gtkutils.StockButton("go-next-symbolic")
        gtklogger.setWidgetName(self.nexttimeButton, "next")
        gtklogger.connect(self.nexttimeButton, 'clicked', self.nexttimeCB)
        self.timebox.pack_start(self.nexttimeButton, expand=False, fill=False,
                                padding=0)
        self.nexttimeButton.set_tooltip_text("Go to the next stored time.")

        # The slider/entry combo has immediate==False because we don't
        # want to update until the user is done typing a time.
        self.timeslider = labelledslider.FloatLabelledSlider(
            value=0.0, vmin=0, vmax=0, step=0.01,
            callback=self.timeSliderCB,
            name='timeslider',
            immediate=False)

        # self.timeslider.set_policy(gtk.UPDATE_DISCONTINUOUS)
        self.timebox.pack_start(self.timeslider.gtk, expand=True, fill=True,
                                padding=0)
        self.timeslider.set_tooltips(
            slider="Select an interpolation time.",
            entry="Enter an interpolation time.")

        canvasbox.pack_start(self.makeCanvasWidgets(),
                             expand=True, fill=True, padding=0)

        # HACK.  Set the position of the toolbox/canvas divider.  This
        # prevents the toolbox pane from coming up minimized.
        ##self.paned2.set_position(250)

        # Bottom part of main pane is a list of layers.  The actual
        # DisplayLayer objects are stored in self.layers.

        layerFrame = Gtk.Frame(label='Layers',
                               margin_top=gtkutils.handle_padding)

        self.mainpane.pack2(layerFrame, resize=False, shrink=False)
        self.layerScroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(self.layerScroll, "LayerScroll")
        self.layerScroll.set_policy(Gtk.PolicyType.AUTOMATIC,
                                    Gtk.PolicyType.AUTOMATIC)
        layerFrame.add(self.layerScroll)

        self.layerList = Gtk.ListStore(GObject.TYPE_PYOBJECT)
        self.layerListView = Gtk.TreeView(self.layerList)
        gtklogger.setWidgetName(self.layerListView, "LayerList")
        self.layerListView.set_row_separator_func(self.layerRowSepFunc)
        self.layerListView.set_fixed_height_mode(False)
        self.layerScroll.add(self.layerListView)

        gtklogger.adoptGObject(self.layerList, self.layerListView,
                              access_method=self.layerListView.get_model)

        # Handle right-clicks on the layer list.  They pop up the Layer
        # menu.
        gtklogger.connect(self.layerListView, 'button-press-event',
                          self.layerlistbuttonCB)

        ## TODO: Reordering by drag and drop is disabled because I
        ## can't figure out how it's supposed to work.  It didn't work
        ## properly in gtk+2 either.
        # # The row-deleted and row-inserted signals are used to detect
        # # when the user has reordered rows manually.  When the program
        # # does anything that might cause these signals to be emitted,
        # # it must first call suppressRowOpSignals.
        # self.layerListView.set_reorderable(True)
        # self.rowOpSignals = [
        #     gtklogger.connect(self.layerList, "row-deleted",
        #                      self.listRowDeletedCB),
        #     gtklogger.connect(self.layerList, "row-inserted",
        #                      self.listRowInsertedCB)
        #     ]
        # self.destination_path = None

        showcell = Gtk.CellRendererToggle()
        showcol = Gtk.TreeViewColumn("Show")
        showcol.pack_start(showcell, expand=False)
        showcol.set_cell_data_func(showcell, self.renderShowCell)
        self.layerListView.append_column(showcol)
        gtklogger.adoptGObject(showcell, self.layerListView,
                               access_function=gtklogger.findCellRenderer,
                               access_kwargs={'col':0, 'rend':0})
        gtklogger.connect(showcell, 'toggled', self.showcellCB)

        freezecell = Gtk.CellRendererToggle()
        freezecol = Gtk.TreeViewColumn("Freeze")
        freezecol.pack_start(freezecell, expand=False)
        freezecol.set_cell_data_func(freezecell, self.renderFreezeCell)
        self.layerListView.append_column(freezecol)
        gtklogger.adoptGObject(freezecell, self.layerListView,
                               access_function=gtklogger.findCellRenderer,
                               access_kwargs={'col':2, 'rend':0})
        gtklogger.connect(freezecell, 'toggled', self.freezeCellCB)

        layercell = Gtk.CellRendererText()
        layercol = Gtk.TreeViewColumn("What")
        layercol.set_resizable(True)
        layercol.pack_start(layercell, expand=True)
        layercol.set_cell_data_func(layercell, self.renderLayerCell)
        self.layerListView.append_column(layercol)

        methodcell = Gtk.CellRendererText()
        methodcol = Gtk.TreeViewColumn("How")
        methodcol.set_resizable(True)
        methodcol.pack_start(methodcell, expand=True)
        methodcol.set_cell_data_func(methodcell, self.renderMethodCell)
        self.layerListView.append_column(methodcol)

        gtklogger.adoptGObject(self.layerListView.get_selection(),
                              self.layerListView,
                              access_method=self.layerListView.get_selection)
        self.selsignal = gtklogger.connect(self.layerListView.get_selection(), 
                                          'changed', self.selectionChangedCB)
        gtklogger.connect(self.layerListView, 'row-activated',
                         self.layerDoubleClickCB)

    def makeCanvasWidgets(self):
        # The canvas is in the right half of paned2 (ie the middle
        # pane of 3).  We *don't* use a ScrolledWindow for it, because
        # we need direct access to the Scrollbars.  Instead, we make
        # the Scrollbars ourselves and put them in a Table with the
        # canvas.
        self.canvasTable = Gtk.Grid()
        gtklogger.setWidgetName(self.canvasTable, "Canvas")
        self.canvasTable.set_column_spacing(1)
        self.canvasTable.set_row_spacing(1)
        self.hScrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.HORIZONTAL)
        self.vScrollbar = Gtk.Scrollbar(orientation=Gtk.Orientation.VERTICAL)
        gtklogger.setWidgetName(self.hScrollbar, "hscroll")
        gtklogger.setWidgetName(self.vScrollbar, "vscroll")
        # # Catch button release events on the Scrollbars, so that their
        # # changes can be logged.  *Don't* catch the "changed" signals
        # # from their Adjustments, because they occur too often.
        # gtklogger.connect(self.hScrollbar, "button-release-event",
        #                   self.scrlReleaseCB, 'h')
        # gtklogger.connect(self.vScrollbar, "button-release-event",
        #                   self.scrlReleaseCB, 'v')
        self.canvasTable.attach(self.hScrollbar, 0,1, 1,1)
        self.canvasTable.attach(self.vScrollbar, 1,0, 1,1)
        self.canvasFrame = Gtk.Frame()
        self.canvasTable.attach(self.canvasFrame, 0,0, 1,1)
        return self.canvasTable

    def makeContourMapWidgets(self):
        # the contourmap is in the right half of paned1 (the right pane of 3)
        contourmapframe = Gtk.Frame(shadow_type=Gtk.ShadowType.IN,
                                    margin_start=gtkutils.handle_padding,
                                    margin_end=2)
        contourmapbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                                margin=2)
        self.paned1.pack2(contourmapframe, resize=False, shrink=True)
        gtklogger.setWidgetName(contourmapframe, "ContourMap")
        contourmapframe.add(contourmapbox)
        self.contourmap_max = Gtk.Label("max", halign=Gtk.Align.CENTER)
        gtklogger.setWidgetName(self.contourmap_max, "MapMax")
        self.new_contourmap_canvas()    # Sets self.contourmapdata.canvas.
        self.contourmap_min = Gtk.Label("min", halign=Gtk.Align.CENTER)
        gtklogger.setWidgetName(self.contourmap_min, "MapMin")
        contourmaplevelbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                     spacing=1)
        self.contourlevel_min = Gtk.Label()
        contourmaplevelbox.pack_start(self.contourlevel_min,
                                      expand=True, fill=True, padding=0)
        contourmaplevelbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.VERTICAL),
            expand=False, fill=False, padding=0)
        contourmaplevelbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.VERTICAL),
            expand=False, fill=False, padding=0)
        self.contourlevel_max = Gtk.Label()
        contourmaplevelbox.pack_end(self.contourlevel_max,
                                    expand=True, fill=True, padding=0)
        contourmapclearbutton = Gtk.Button("Clear Mark")
        gtklogger.setWidgetName(contourmapclearbutton, "Clear")
        gtklogger.connect(contourmapclearbutton, "clicked",
                         self.contourmap_clear_marker)
        contourmapbox.pack_start(self.contourmap_max, expand=False, fill=False,
                                 padding=0)
        contourmapbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
            expand=False, fill=False, padding=0)
        contourmapbox.pack_start(self.contourmapdata.canvas.layout,
                                 expand=True, fill=True, padding=0)
        contourmapbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
            expand=False, fill=False, padding=0)
        contourmapbox.pack_start(self.contourmap_min, expand=False, fill=False,
                                 padding=0)
        contourmapbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
            expand=False, fill=False, padding=0)
        contourmapbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
            expand=False, fill=False, padding=0)
        contourmapbox.pack_start(contourmaplevelbox, expand=False, fill=False,
                                 padding=0)
        contourmapbox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
            expand=False, fill=False, padding=0)
        contourmapbox.pack_end(contourmapclearbutton, expand=False, fill=False,
                               padding=0)
        contourmapframe.show_all() # Is this needed?


    def postinitialize(self, name, gfxmgr, clone):
        debug.mainthreadTest()
        # SubWindow initializer makes the menu bar, and sets up the
        # .gtk and .mainbox members.  ".gtk" is the window itself,
        # and .mainbox is a gtk.VBox that holds the menu bar.
        windowname = utils.underscore2space("OOF2 " + name)
        subWindow.SubWindow.__init__(self, windowname, menu=self.menu)

        # The ContourMapData structure is created in the
        # GhostGfxWindow constructor, and the widgets can't be made
        # until after the contructor is called.
        self.makeContourMapWidgets()
        # Add gui callbacks to the non-gui menu created by the GhostGfxWindow.
        filemenu = self.menu.File
        filemenu.Save_Canvas_Region.add_gui_callback(self.saveCanvasRegion_gui)
        # The generic Quit callback uses Quit.data to know which
        # window it's being called from, so that the dialog can appear
        # in the right place.
        filemenu.Quit.add_gui_callback(quit.queryQuit)
        filemenu.Quit.data = self.gtk.get_toplevel()

        layermenu = self.menu.Layer
        # layermenu.New doesn't need a GUI callback.
        layermenu.Edit.add_gui_callback(self.editLayer_gui)
        layermenu.Delete.add_gui_callback(self.deleteLayer_gui)
        layermenu.Hide.add_gui_callback(self.hideLayer_gui)
        layermenu.Show.add_gui_callback(self.showLayer_gui)
        layermenu.Freeze.add_gui_callback(self.freezeLayer_gui)
        layermenu.Unfreeze.add_gui_callback(self.unfreezeLayer_gui)
        layermenu.Raise.One_Level.add_gui_callback(self.raiseLayer_gui)
        layermenu.Raise.To_Top.add_gui_callback(self.raiseToTop_gui)
        layermenu.Lower.One_Level.add_gui_callback(self.lowerLayer_gui)
        layermenu.Lower.To_Bottom.add_gui_callback(self.lowerToBottom_gui)
        settingmenu = self.menu.Settings
        toolboxmenu = self.menu.Toolbox

        # Construct gui's for toolboxes.  This must be done after the
        # base class is constructed so that all non-gui toolboxes are
        # created before any of their gui versions.  Some gui
        # toolboxes need to know about more than one non-gui toolbox.
        
        map(self.makeToolboxGUI, self.toolboxes)
        if self.toolboxGUIs:
            self.selectToolbox(self.toolboxGUIs[0].name())
            self.toolboxchooser.set_state(self.toolboxGUIs[0].name())

        # raise_window routine is in SubWindow class.
        getattr(mainmenu.OOF.Windows.Graphics, name).add_gui_callback(
            self.raise_window)

        self.gtk.connect('destroy', self.destroyCB)
        self.gtk.connect_after('realize', self.realizeCB)
        self.gtk.set_default_size(ghostgfxwindow.GhostGfxWindow.initial_width,
                                  ghostgfxwindow.GhostGfxWindow.initial_height)

        self.mainbox.set_spacing(3)

        self.mainbox.pack_start(self.mainpane,
                                fill=True, expand=True, padding=0)

        self.gtk.show_all()

        self.updateToolboxChooser()
        self.switchboardCallbacks.append(
            switchboard.requestCallback("shutdown", self.shutdownCB))

    def __repr__(self):
        return 'GfxWindow("%s")' % self.name

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    def newCanvas(self):
        debug.mainthreadTest()
        canvas = oofcanvasgui.Canvas(width=300, height=300, ppu=1.0,
                                     vexpand=True, hexpand=True)
        self.canvasFrame.add(canvas.layout)
        self.hScrollbar.set_adjustment(canvas.get_hadjustment())
        self.vScrollbar.set_adjustment(canvas.get_vadjustment())
        # Changes to the adjustments need to go into the gui log.
        gtklogger.adoptGObject(self.hScrollbar.get_adjustment(),
                               self.hScrollbar,
                               access_method=self.hScrollbar.get_adjustment)
        gtklogger.adoptGObject(self.vScrollbar.get_adjustment(),
                               self.vScrollbar,
                               access_method=self.vScrollbar.get_adjustment)
        gtklogger.connect_passive(self.hScrollbar.get_adjustment(),
                                  'value-changed')
        gtklogger.connect_passive(self.vScrollbar.get_adjustment(),
                                  'value-changed')
        canvas.setMouseCallback(self.mouseCB, None)

        gtklogger.setWidgetName(canvas.layout, "OOFCanvas")
        gtklogger.connect_passive(canvas.layout, "button-press-event")
        gtklogger.connect_passive(canvas.layout, "button-release-event")
        gtklogger.connect_passive(canvas.layout, "motion-notify-event")
        gtklogger.log_motion_events(canvas.layout)

        ## TODO GTK3: Do we need to log scroll-event if we're already
        ## logging the scrollbars?
        # gtklogger.connect_passive(canvas.layout, "scroll-event")
        
        if self.rubberband:
            canvas.setRubberBand(self.rubberband)
        return canvas
        
    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Contour map stuff.

    def newContourmapCanvas(self):
        # Arguments are width, height, and ppu. They don't matter.
        # Just call zoomToFill after drawing.
        return oofcanvasgui.Canvas(100, 100, 1)

    # Create object and assign to self.contourmap_canvas.
    def new_contourmap_canvas(self):
        ghostgfxwindow.GhostGfxWindow.new_contourmap_canvas(self)
        self.contourmapdata.canvas.setResizeCallback(
            self.contourmap_resize, None)
        self.contourmapdata.canvas.setMouseCallback(self.contourmap_mouse, None)

    
##    # Function called after layers have been arranged.  Does not
##    # draw the actual contourmap, just records the layers.
##    def contourmap_newlayers(self):
##        ghostgfxwindow.GhostGfxWindow.contourmap_newlayers(self)
##        for ell in self.display:
##            if ell==self.current_contourmap_method:
##                mainthread.runBlock(
##                    self.layerwidgets[ell].setContourmapButton,(1,))
##            else:
##                mainthread.runBlock(
##                    self.layerwidgets[ell].setContourmapButton,(0,))

    # def set_contourmap_layer(self, method):
    #     ghostgfxwindow.GhostGfxWindow.set_contourmap_layer(self, method)
        
            
    # Draw the contourmap onto the canvas, and update the numbers on the
    # display.  Called after all the layers have been drawn in the
    # main pane.  Also called from the menu callback which resets the
    # aspect ratio.

    # TODO LATER: There is some clunkiness in this routine, associated
    # particularly with the "discrete" displays, most particularly
    # with the CenterFill display.  The problem is that, in the
    # center-fill display and the skeleton quality display, the colors
    # drawn on the main canvas are broad swaths painted with the color
    # corresponding to a particular level, which behaves as a "contour
    # level" -- when there are few of these, this looks dumb, some
    # colors which may occur over a wide area of the main canvas will
    # be invisible on the contourmap.  This problem occurs for regular
    # contours also, but isn't as noticeable, partially because you
    # have more of them, and partially because the maximum of a real
    # contour plot occupies a small fraction of the main-canvas area.
    
    # A possible answer is to make the colormap be drawn continuously,
    # no matter how many levels there actually are.  Alternatively,
    # one could figure out how to do something sensible with the fact
    # that contour lines in general occur at particular levels, but if
    # you want to see something on the map, it has to be drawn over an
    # interval.

    def show_contourmap_info(self):
        if not self.gtk:
            return
        wasempty = self.contourmapdata.canvas.empty()
        self.contourmapdata.canvas_mainlayer.clear()
        self.contourmapdata.canvas_mainlayer.removeAllItems()
        
        # Copy self.current_contourmap_method to a local variable to
        # prevent interference from other threads. (TODO: Really?
        # Shouldn't this be done while the gfxlock is acquired?)
        current_contourmethod = self.current_contourmap_method
        if current_contourmethod:
            current_contourmethod.draw_contourmap(
                self, self.contourmapdata.canvas_mainlayer)
            self.contourmapdata.canvas.zoomToFill()
            (c_min, c_max, lvls) = current_contourmethod.get_contourmap_info()
        else:
            # A newly empty contourmap canvas has to be drawn to erase
            # its old contents.
            if not wasempty:
                self.contourmapdata.canvas.draw()
            c_min = c_max = None
        
        if c_min is None:
            mainthread.runBlock(self.contourmap_min.set_text, ('min',))
        else:
            mainthread.runBlock(self.contourmap_min.set_text,
                                (("%.3g" % c_min).rstrip(),) )
            
        if c_max is None:
            mainthread.runBlock(self.contourmap_max.set_text, ('max',) )
        else:
            mainthread.runBlock(self.contourmap_max.set_text,
                                (("%.3g" % c_max).rstrip(),) )

        self.show_contourmap_ticks(self.contourmapdata.mark_value)
        gtklogger.checkpoint("contourmap info updated for " + self.name)


    # Draw the marks on it.  Argument is the new value for the ticks.

    def show_contourmap_ticks(self, y):
        if not self.gtk:
            return
        c_min = None
        c_max = None

        self.contourmapdata.canvas_ticklayer.removeAllItems()
        
        if self.current_contourmap_method:
            (c_min, c_max, lvls) = \
                    self.current_contourmap_method.get_contourmap_info()

        if ((c_max is not None) and (c_min is not None)):
            if y is not None:
                real_y = y + c_min
                # need to know which level am I in.
                level = None
                for i in range(len(lvls)):
                    if real_y <= lvls[i]:
                        level = i-1
                        if i==len(lvls):
                            i -= 1
                        break
                if level is not None:
                    width=(c_max-c_min)/self.settings.aspectratio
                    polygon = oofcanvas.CanvasRectangle(
                        0, lvls[level]-c_min,
                        width, lvls[level+1]-c_min)
                    clr = self.settings.contourmap_markercolor
                    polygon.setLineColor(color.canvasColor(
                        self.settings.contourmap_markercolor))
                    polygon.setLineWidth(self.settings.contourmap_markersize)
                    polygon.setLineWidthInPixels()
                    self.contourmapdata.canvas_ticklayer.addItem(polygon)

                    self.contourmapdata.mark_value = y
                    minimum = lvls[level]
                    maximum = lvls[level] + (lvls[1]-lvls[0])
                    mainthread.runBlock(
                        self.contourlevel_min.set_text,
                        ("%.2e" % minimum,) )
                    mainthread.runBlock(
                        self.contourlevel_max.set_text,
                        ("%.2e" % maximum,) )

        # If any of the above conditions were not met, clear the
        # tick layer.
        if (c_max is None) or (c_min is None) or \
               (y is None) or (level is None):
            mainthread.runBlock(
                self.contourlevel_min.set_text, ('',) )
            mainthread.runBlock(
                self.contourlevel_max.set_text, ('',) )

        self.contourmapdata.canvas.show()

    # Callback for size changes of the pane containing the contourmap.
    def contourmap_resize(self, data):
        self.contourmapdata.canvas.zoomToFill()

    def contourmap_mouse(self, event, x, y, button, shift, ctrl, data):
        debug.mainthreadTest()
        if event=="down":
            self.contourmapdata.mouse_down = 1
        elif (event=="move") and self.contourmapdata.mouse_down==1:
            subthread.execute(self.show_contourmap_ticks, (y,))
        elif event=="up":
            self.contourmapdata.mouse_down = None
            subthread.execute(self.show_contourmap_ticks, (y,))

    # Button callback.
    def contourmap_clear_marker(self, gtk):
        self.contourmapdata.mark_value = None
        self.contourlevel_min.set_text('')
        self.contourlevel_max.set_text('')
        subthread.execute(self.show_contourmap_info)

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Called on a subthread, not on the main thread.
    # Argument is actually used at gfxwindow-open-time by the menu command.
    def draw(self, zoom=False): # switchboard "redraw" callback
        debug.subthreadTest()
        if self.closed:
            return
        if self.oofcanvas.empty():
            # *Always* zoom to fill the window on the first non-trivial draw
            zoom = True

        self.updateTimeControls()
        self.drawLayers()
        if zoom and self.realized:
            self.zoomFillWindow()

        # Copy the OOFCanvas::CanvasLayers to the OOFCanvas::Canvas
        # (actually just tells gtk to queue up a draw event).
        self.oofcanvas.draw()
        
        # Update the contourmap info, now that the appropriate layer
        # has completed its draw.
        self.show_contourmap_info()
            
    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    def animate(self, menuitem, start, finish, times, frame_rate, style):
        menuitem.disable()
        prog = progress.getProgress("Animation", style.getProgressStyle())

        # Construct a generator that produces the times of the
        # animation frames.  Python generators aren't thread safe in
        # some mysterious way, so the generator has to be constructed
        # on the main thread.  If this isn't done, then interrupting
        # an animation can lead to an internal python error or seg
        # fault. (TODO: Check that this is still true.)
        timegen = mainthread.runBlock(self._timegenerator,
                                      (style, times, start, finish))
        # Get the full list of times from the animation layers so we
        # can find the start and finish times.  This is just to
        # calibrate the progress bar.  timegen is what actually
        # produces the frame times.
        times = self.findAnimationTimes()
        
        if times and times[-1] > times[0]:
            time0 = times[0]
            time1 = times[-1]
            # Animation timing is controlled by a timeout callback
            # which periodically sets an "escapement" Event.  Every
            # time the Event is set, it allows one frame to be drawn.
            self._escapement = threading.Event()

            # This menuitem shouldn't finish until the escapement
            # timeout callback has been cleared, which is indicated by
            # another event.
            escapementDone = threading.Event()

            # _stopAnimation indicates that the animation is complete,
            # either because it ran to the end, the user interrupted
            # it, or the program is quitting.
            self._stopAnimation = False

            # Start the escapement.
            GObject.timeout_add(
                int(1000./frame_rate), # time between frames, in milliseconds
                self._escapementCB,
                prog,
                escapementDone)

            # Draw frames, after waiting for an escapement event.
            while not self._stopAnimation:
                self._escapement.wait()
                if prog.stopped() or self._stopAnimation:
                    self._stopAnimation = True
                    break
                # Clear the event, so that we have to wait for the
                # escapement to set it again before drawing the
                # next frame. This is done *before* drawing the
                # current frame, because if drawing a frame takes
                # longer than the time between escapement events,
                # we'll want to start on the next frame as soon as
                # possible.
                self._escapement.clear()

                try:
                    time = timegen.next()
                except StopIteration:
                    self._stopAnimation = True
                else:
                    # Update the progress bar and actually do the drawing.
                    prog.setMessage(`time`)
                    prog.setFraction((time-time0)/(time1-time0))
                    self.drawAtTime(time)

            ## TODO: Use some other scheme for unthreaded mode.

            escapementDone.wait()
            prog.finish()
            menuitem.enable()

    def _escapementCB(self, prog, escapementDone):
        # Timeout callback that calls self._escapement.set()
        # periodically.  This is called on the main thread.
        self._escapement.set()
        if prog.stopped() or self._stopAnimation:
            self._stopAnimation = True
            escapementDone.set()
            return False        # don't reinstall time out callback
        return True             # do reinstall timeout callback

    def _timegenerator(self, style, times, start, finish):
        return iter(style.getTimes(times.times(start, finish, self)))

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    def shutdownCB(self):
        self._stopAnimation = True
        # self._escapement might not exist if the window hasn't
        # been animated, so we need to use try/except.
        try:  
            self._escapement.set()
        except:
            pass

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#        

    # TODO: clean up the rest of this file!

    # menu callback
    def toggleAntialias(self, menuitem, antialias):
        ghostgfxwindow.GhostGfxWindow.toggleAntialias(
            self, menuitem, antialias)
        mainthread.runBlock(self.oofcanvas.setAntialias, (antialias,))

    # used by viewertoolbox zoom functions -- only 2D!
    def zoomFactor(self):
        return self.settings.zoomfactor

    def zoomIn(self, *args):
        self.acquireGfxLock()
        try:
            if self.oofcanvas and not self.oofcanvas.empty():
                mainthread.runBlock(self.oofcanvas.zoom,
                                    (self.settings.zoomfactor,))
                self.zoomed = 1
        finally:
            self.releaseGfxLock()

    def zoomInFocussed(self, menuitem, focus):
        self.acquireGfxLock()
        try:
            if self.oofcanvas and not self.oofcanvas.empty():
                mainthread.runBlock(self.oofcanvas.zoomAbout,
                                    (focus.x, focus.y,
                                     self.settings.zoomfactor))
                self.zoomed = 1
        finally:
            self.releaseGfxLock()

    def zoomOut(self, *args):
        self.acquireGfxLock()
        try:
            if self.oofcanvas and not self.oofcanvas.empty():
                mainthread.runBlock(self.oofcanvas.zoom,
                                    (1./self.settings.zoomfactor,))
                self.zoomed = 1
        finally:
            self.releaseGfxLock()
        hadj = self.hScrollbar.get_adjustment()

    def zoomOutFocussed(self, menuitem, focus):
        self.acquireGfxLock()
        try:
            if self.oofcanvas and not self.oofcanvas.empty():
                mainthread.runBlock(self.oofcanvas.zoomAbout,
                                    (focus.x, focus.y,
                                     1./self.settings.zoomfactor))
                self.zoomed = 1
        finally:
            self.releaseGfxLock()


    def zoomFillWindow_thread(self):
        debug.mainthreadTest()
        if self.closed:
            return
        if self.oofcanvas and not self.oofcanvas.empty():
            self.zoom_bbox()


    def zoom_bbox(self):
        debug.mainthreadTest()
        self.oofcanvas.zoomToFill()

    def saveCanvasRegion_gui(self, menuitem):
        if self.oofcanvas.empty():
            reporter.warn("Canvas is empty! Not saving anything.")
            return
        visrect = self.oofcanvas.visibleRegion() # an OOFCanvas::Rectangle
        ll = menuitem.get_arg('lowerleft')
        ll.value = primitives.Point(visrect.xmin(), visrect.ymin());
        ur = menuitem.get_arg('upperright')
        ur.value = primitives.Point(visrect.xmax(), visrect.ymax());
        if parameterwidgets.getParameters(*menuitem.params,
                                          parentwindow=self.gtk,
                                          title="Save Region"):
            menuitem.callWithDefaults()

    # GUI override of menu callback for new contourmap aspect ratio.
    # GUI callbacks are required because, when the settings change,
    # you have to redraw the window.
    def aspectRatio(self, menuitem, ratio):
        self.acquireGfxLock()
        try:
            self.settings.aspectratio = ratio
        finally:
            self.releaseGfxLock()
        self.show_contourmap_info()

    # Overridden menu callbacks for these settings.
    def contourmapMarkSize(self, menuitem, width):
        self.acquireGfxLock()
        try:
            self.settings.contourmap_markersize = width
            v = self.contourmapdata.mark_value
            self.contourmapdata.mark_value = None
        finally:
            self.releaseGfxLock()
        self.show_contourmap_ticks(v)

    def contourmapMarkColor(self, menuitem, color):
        self.acquireGfxLock()
        try:
            self.settings.contourmap_markercolor = color
            v = self.contourmapdata.mark_value
            self.contourmapdata.mark_value = None
        finally:
            self.releaseGfxLock()
        self.show_contourmap_ticks(v)

    def toggleLongLayerNames(self, menuitem, longlayernames):
        self.acquireGfxLock()
        try:
            self.settings.longlayernames = longlayernames
            self.fillLayerList()
        finally:
            self.releaseGfxLock()
        
    # Sets background color for both canvases.
    def bgColor(self, menuitem, color):          # OOFMenu callback
        self.acquireGfxLock()
        try:
            ghostgfxwindow.GhostGfxWindow.bgColor(self, menuitem, color)
            self.oofcanvas.setBackgroundColor(
                color.getRed(), color.getGreen(), color.getBlue())
            self.contourmapdata.canvas.setBackgroundColor(
                color.getRed(), color.getGreen(), color.getBlue())
            mainthread.runBlock(self.oofcanvas.draw)
            mainthread.runBlock(self.contourmapdata.canvas.draw)
        finally:
            self.releaseGfxLock()

    def marginCB(self, menuitem, fraction):
        self.acquireGfxLock()
        try:
            self.settings.margin = fraction
            self.oofcanvas.setMargin(fraction)
        finally:
            self.releaseGfxLock()

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Scrolling 

    def hScrollPosition(self):
        return self.hScrollbar.get_adjustment().value

    def vScrollPosition(self):
        return self.vScrollbar.get_adjustment().value

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Rubber Band

    def setRubberBand(self, rubberband):
        self.rubberband = rubberband
        if self.oofcanvas is not None:
            if rubberband is not None:
                self.oofcanvas.setRubberBand(rubberband)
            else:
                self.oofcanvas.removeRubberBand()

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Right click on layer list
    
    def layerlistbuttonCB(self, gtkobj, event):
        if event.button == 3:
            popupMenu = Gtk.Menu()
            gtklogger.newTopLevelWidget(popupMenu, 'PopUp-'+self.name)
            for item in self.menu.Layer:
                item.construct_gui(self.menu.Layer, popupMenu, None)
            popupMenu.show_all()
            popupMenu.popup_at_pointer(event)

        # It's important to return False here, since doing so allows
        # other handlers to see the event.  In particular, it allows a
        # right-click to select the treeview line, so that the popup
        # menu can act on it.  Most of the menu items act on the
        # current selection.
        return False         
        
    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#    

    # Time Controls. 

    ## TODO: What happens if the user types in a time that's outside
    ## of the range?

    def timeSliderCB(self, slider, val):
        self.menu.Settings.Time.callWithDefaults(time=val)
        
    def prevtimeCB(self, gtkbutton):
        times = self.findAnimationTimes()
        for i,t in enumerate(times[1:]):
            if t >= self.displayTime:
                # i indexes times[1:] so the previous time is
                # times[i], not times[i-1].
                self.menu.Settings.Time.callWithDefaults(time=times[i])
                return

    def nexttimeCB(self, gtkbutton):
        times = self.findAnimationTimes()
        for t in times:
            if t > self.displayTime:
                self.menu.Settings.Time.callWithDefaults(time=t)
                return

    def updateTimeControls(self):
        mainthread.runBlock(self._updateTimeControls)
    def _updateTimeControls(self):
        debug.mainthreadTest()
        times = self.findAnimationTimes()
        if times:
            self.timeslider.set_sensitive(True)
            mintime = min(times)
            maxtime = max(times)
            self.timeslider.setBounds(mintime, maxtime)
        else:
            self.timeslider.set_sensitive(False)
        self.sensitizeTimeButtons(times)

    def sensitizeTimeButtons(self, times=None):
        debug.mainthreadTest()
        if times is None:       # distinguish from []!
            times = self.findAnimationTimes()
        notlast = bool(times and self.displayTime != times[-1])
        notfirst = bool(times and self.displayTime != times[0])
        self.nexttimeButton.set_sensitive(notlast)
        self.prevtimeButton.set_sensitive(notfirst)

    def setTimeCB(self, menuitem, time):
        self.drawAtTime(time)

    def drawAtTime(self, time, zoom=False):
        debug.subthreadTest()
        if time is not None:
            self.setDisplayTime(time)
            mainthread.runBlock(self.timeslider.set_value, (self.displayTime,))
            # Ensure that animatable layers will be redrawn by backdating
            # them, and then calling "draw".  All time-dependent layers
            # are animatable, and they get their time from the GfxWindow's
            # displayTime.

            # Don't backdate layers that have already been drawn at the
            # given time.  Layers that have been drawn already return
            # outOfTime==True.
            for layer in self.layers:
                if layer.animatable(self) and layer.outOfTime(self):
                    layer.backdate()
        self.draw(zoom=zoom)

        mainthread.runBlock(self.sensitizeTimeButtons)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# This function redefines the one in GfxWindowManager when the GUI
# code is loaded.

def _newWindow(self, name, **kwargs):
    if guitop.top(): # if in GUI mode
        return GfxWindow(name, self, **kwargs)
    return ghostgfxwindow.GhostGfxWindow(name, self, **kwargs)

gfxmanager.GfxWindowManager._newWindow = _newWindow

