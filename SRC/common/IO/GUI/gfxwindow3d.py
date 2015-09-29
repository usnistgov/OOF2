# -*- python -*-
# $RCSfile: gfxwindow3d.py,v $
# $Revision: 1.11 $
# $Author: vrc $
# $Date: 2010/08/05 21:23:33 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import gobject
import gtk
from types import *
import math, time, sys

from ooflib.SWIG.common import coord
from ooflib.SWIG.common import geometry
from ooflib.SWIG.common.guitop import top
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import config
from ooflib.common.IO.GUI import oofcanvas3d    
#from ooflib.common.IO.GUI import fakecanvas
from ooflib.SWIG.common import threadstate
from ooflib.common.IO.GUI import rubberband3d as rubberband
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common import subthread
from ooflib.common import toolbox
from ooflib.common import utils
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import layereditor
from ooflib.common.IO import mainmenu
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gfxmenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import quit
from ooflib.common.IO.GUI import subWindow
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.common.IO.GUI import toolbarGUI
from ooflib.common.IO.GUI import gfxwindowbase

# during_callback() is called (by CanvasOutput.show()) only in
# non-threaded mode, so we don't worry about the thread-safety of a
# global variable here.
_during_callback = 0
def during_callback():
    return _during_callback

_pi_over_2 = math.pi/2.0


class GfxWindow3D(gfxwindowbase.GfxWindowBase):
    initial_height = 800
    initial_width = 1000

    def preinitialize(self, name, gfxmanager, clone):
        debug.mainthreadTest()
        self.gtk = None
        self.closed = None # State data used at window-close time.
        self.name = name
        self.oofcanvas = None
        self.realized = 0
        self.zoomed = 0
        self.settings = ghostgfxwindow.GfxSettings()
        self.mouseHandler = mousehandler.nullHandler # doesn't do anything
        self.rubberband = rubberband.NoRubberBand()
        #self.contourmapdata = None 

        # Build all the GTK objects for the interior of the box.  These
        # actually get added to the window itself after the SubWindow
        # __init__ call.  They need to be created first so the
        # GhostGfxWindow can operate on them, and then create the menus
        # which are handed off to the SubWindow.
        self.mainpane = gtk.VPaned()
        gtklogger.setWidgetName(self.mainpane, 'Pane0')

        # Panes dividing upper pane horizontally into 3 parts.
        # paned1's left half contains paned2.
        self.paned1 = gtk.HPaned()
        gtklogger.setWidgetName(self.paned1, "Pane1")
        self.mainpane.pack1(self.paned1, resize=True)
        gtklogger.connect_passive(self.paned1, 'size-allocate')

        # paned2 is in left half of paned1
        self.paned2 = gtk.HPaned()
        gtklogger.setWidgetName(self.paned2, "Pane2")
        self.paned1.pack1(self.paned2, resize=True)
        gtklogger.connect_passive(self.paned2, 'size-allocate')

        # The toolbox is in the left half of paned2 (ie the left frame of 3)
        toolboxframe = gtk.Frame()
        toolboxframe.set_shadow_type(gtk.SHADOW_IN)
        self.paned2.pack1(toolboxframe, resize=True)
        gtklogger.connect_passive(toolboxframe, 'size-allocate')

        # Box containing the toolbox label and the scroll window for
        # the toolbox itself.
        toolboxbox1 = gtk.VBox()
        toolboxframe.add(toolboxbox1)
        hbox = gtk.HBox()
        toolboxbox1.pack_start(hbox, expand=0, fill=0, padding=2)
        hbox.pack_start(gtk.Label("Toolbox:"), expand=0, fill=0, padding=3)
        
        self.toolboxchooser = chooser.ChooserWidget([],
                                                    callback=self.switchToolbox,
                                                    name="TBChooser")
        hbox.pack_start(self.toolboxchooser.gtk, expand=1, fill=1, padding=3)

        # Scroll window for the toolbox itself.
        toolboxbox2 = gtk.ScrolledWindow()
        gtklogger.logScrollBars(toolboxbox2, 'TBScroll')
        
        toolboxbox2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        toolboxbox1.pack_start(toolboxbox2, expand=1, fill=1)

        # Actually, the tool box goes inside yet another box, so that
        # we have a gtk.VBox that we can refer to later.
        self.toolboxbody = gtk.VBox()
        toolboxbox2.add_with_viewport(self.toolboxbody)

        self.toolboxGUIs = []           # GUI wrappers for toolboxes.
        self.current_toolbox = None

        # The canvas is in the right half of paned2 (ie the middle
        # pane of 3).
        # TODO: make this a table with compact, view control buttons,
        # for now, just a frame with the gtkglext window.

        self.canvasBox = gtk.VBox()
        self.toolbarFrame = gtk.Frame()
        self.toolbarFrame.set_shadow_type(gtk.SHADOW_IN)
        self.canvasBox.pack_start(self.toolbarFrame, expand=0, fill=0, padding=0)

        self.toolbar = toolbarGUI.ToolBar(self)
        self.toolbarFrame.add(self.toolbar.gtk)
        self.toolbar.gtk.show()

        self.canvasFrame = gtk.Frame()
        self.canvasFrame.set_shadow_type(gtk.SHADOW_IN)
        gtklogger.setWidgetName(self.canvasFrame, "Canvas")
        self.canvasBox.pack_start(self.canvasFrame, expand=1, fill=1, padding=0)

        self.paned2.pack2(self.canvasBox, resize=True)

        # HACK.  Set the position of the toolbox/canvas divider.  This
        # prevents the toolbox pane from coming up minimized.
        self.paned2.set_position(300)


        # Bottom part of main pane is a list of layers.  The actual
        # DisplayLayer objects are stored in self.display.

        layerFrame = gtk.Frame(label='Layers')
        
        self.mainpane.pack2(layerFrame, resize=False)
        self.layerScroll = gtk.ScrolledWindow()
        gtklogger.logScrollBars(self.layerScroll, "LayerScroll")
        self.layerScroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        layerFrame.add(self.layerScroll)

        self.layerList = gtk.ListStore(gobject.TYPE_PYOBJECT)
        self.layerListView = gtk.TreeView(self.layerList)
        gtklogger.setWidgetName(self.layerListView, "LayerList")
        self.layerListView.set_row_separator_func(self.layerRowSepFunc)
        self.layerListView.set_reorderable(True)
        self.layerListView.set_fixed_height_mode(False)
        self.layerScroll.add(self.layerListView)

        gtklogger.adoptGObject(self.layerList, self.layerListView,
                              access_method=self.layerListView.get_model)

        # The row-deleted and row-inserted signals are used to detect
        # when the user has reordered rows manually.  When the program
        # does anything that might cause these signals to be emitted,
        # it must first call suppressRowOpSignals.
        self.rowOpSignals = [
            gtklogger.connect(self.layerList, "row-deleted",
                             self.listRowDeletedCB),
            gtklogger.connect(self.layerList, "row-inserted",
                             self.listRowInsertedCB)
            ]
        self.destination_path = None

        showcell = gtk.CellRendererToggle()
        showcol = gtk.TreeViewColumn("Show")
        showcol.pack_start(showcell, expand=False)
        showcol.set_cell_data_func(showcell, self.renderShowCell)
        self.layerListView.append_column(showcol)
        gtklogger.adoptGObject(showcell, self.layerListView,
                               access_function=gtklogger.findCellRenderer,
                               access_kwargs={'col':0, 'rend':0})
        gtklogger.connect(showcell, 'toggled', self.showcellCB)        

##         cmapcell = gtk.CellRendererToggle()
##         cmapcell.set_radio(True)
##         cmapcol = gtk.TreeViewColumn("Map")
##         cmapcol.pack_start(cmapcell, expand=False)
##         cmapcol.set_cell_data_func(cmapcell, self.renderCMapCell)
##         self.layerListView.append_column(cmapcol)
##         gtklogger.adoptGObject(cmapcell, self.layerListView,
##                                access_function='findCellRenderer',
##                                access_kwargs={'col':1, 'rend':0})
##         gtklogger.connect(cmapcell, 'toggled', self.cmapcellCB)        

        layercell = gtk.CellRendererText()
        layercol = gtk.TreeViewColumn("What")
        layercol.set_resizable(True)
        layercol.pack_start(layercell, expand=True)
        layercol.set_cell_data_func(layercell, self.renderLayerCell)
        self.layerListView.append_column(layercol)

        methodcell = gtk.CellRendererText()
        methodcol = gtk.TreeViewColumn("How")
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
        






    def postinitialize(self, name, gfxmanager, clone):
        debug.mainthreadTest() 
        # Add gui callbacks to the non-gui menu created by the GhostGfxWindow.
        filemenu = self.menu.File
        filemenu.Quit.add_gui_callback(quit.queryQuit)
        layermenu = self.menu.Layer
        layermenu.New.add_gui_callback(self.newLayer_gui)
        layermenu.Edit.add_gui_callback(self.editLayer_gui)
        layermenu.Delete.add_gui_callback(self.deleteLayer_gui)
        layermenu.Hide.add_gui_callback(self.hideLayer_gui)
        layermenu.Show.add_gui_callback(self.showLayer_gui)
##         layermenu.Hide_Contour_Map.add_gui_callback(
##             self.hideLayerContourmap_gui)
##         layermenu.Show_Contour_Map.add_gui_callback(
##             self.showLayerContourmap_gui)
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

        # SubWindow initializer makes the menu bar, and sets up the
        # .gtk and .mainbox members.  ".gtk" is the window itself,
        # and .mainbox is a gtk.VBox that holds the menu bar.
        windowname = utils.underscore2space("OOF3D " + name)
        subWindow.SubWindow.__init__(
            self, windowname, menu=self.menu)



        self.gtk.connect('destroy', self.destroyCB)
        self.gtk.connect_after('realize', self.realizeCB)
        self.gtk.set_default_size(GfxWindow3D.initial_width,
                                  GfxWindow3D.initial_height)

        self.mainbox.set_spacing(3)

        self.mainbox.pack_start(self.mainpane, fill=1, expand=1)

        self.gtk.show_all()

        self.updateToolboxChooser()


    def __repr__(self):
        return 'GfxWindow("%s")' % self.name

    ################################################

    def newCanvas(self):
        # Recreate the canvas object.
        # It's important to acquire and release the lock in the
        # subthread, before calling mainthread.runBlock, to avoid
        # deadlocks.
        debug.subthreadTest()
        self.acquireGfxLock()
        try:
            mainthread.runBlock(self.newCanvas_thread)
        finally:
            self.releaseGfxLock()

    def newCanvas_thread(self):
        debug.mainthreadTest()

        view = None
        if self.oofcanvas:
            view = self.oofcanvas.get_view()
            self.oofcanvas.widget.destroy()

        self.oofcanvas = oofcanvas3d.OOFCanvas3D(self.settings)
        self.canvasFrame.add(self.oofcanvas)
        self.oofcanvas.set_mouse_callback(self.mouseCB)
        self.oofcanvas.set_rubberband(self.rubberband)
        if view is not None:
            self.oofcanvas.set_view(view)

        # delayed import to avoid import loops
        from ooflib.common.IO.GUI import canvasoutput
        from ooflib.common.IO import outputdevice

        #set self.device 
        rawdevice = canvasoutput.CanvasOutput(self.oofcanvas)
        self.device = outputdevice.BufferedOutputDevice(rawdevice)
       
        self.oofcanvas.show()



        

    ################################################

    def draw(self, zoom=False):
        if self.closed:
            return

        if self.oofcanvas.is_empty():
            # *Always* zoom to fill the window on the first non-trivial draw
            zoom = True
        self.acquireGfxLock()
##        debug.fmsg("Got gfx lock.")
        try:
##            debug.fmsg("Calling display.draw on ", self.display)
            self.display.draw(self, self.device)
##            debug.fmsg("Back from display.draw.")
            if zoom and self.realized:
                # We're using buffered output, the canvas may not have
                # received the data yet.  We have to force the data to
                # the canvas, and we have to wait until it's done
                # before zooming.
##                debug.fmsg("Flushing device.")
                self.device.flush_wait()
##                debug.fmsg("Flushed, zooming.")
                self.zoomFillWindow(lock=False)
##                debug.fmsg("Zoomed.")
        finally:
##            debug.fmsg("Releasing gfxlock.")
            self.releaseGfxLock()
##        debug.fmsg("Exiting.")

    def show_contourmap_info(self):
        if not self.gtk:
            return

        current_contourmethod = self.current_contourmap_method

        if current_contourmethod:
            current_contourmethod.draw_contourmap(
                self, self.device)


    def zoomFillWindow_thread(self):
        if self.closed:
            return
        if self.oofcanvas and not self.oofcanvas.is_empty():
            self.oofcanvas.reset()
            self.current_toolbox.updateview()


    def bgColor(self, menuitem, color):
        self.acquireGfxLock()
        try:
            ghostgfxwindow.GhostGfxWindow.bgColor(self, menuitem, color)
            mainthread.runBlock(self.oofcanvas.set_bgColor, (color,))
            self.oofcanvas.render()
        finally:
            self.releaseGfxLock()

    def contourmapBGColor(self, menuitem, color):
        self.acquireGfxLock()
        try:
            ghostgfxwindow.GhostGfxWindow.contourmapBGColor(self, menuitem, color)
            mainthread.runBlock(self.oofcanvas.set_contourmap_bgColor, (color,))
            self.oofcanvas.render()
        finally:
            self.releaseGfxLock()

    def contourmapTextColor(self, menuitem, color):
        self.acquireGfxLock()
        try:
            ghostgfxwindow.GhostGfxWindow.contourmapTextColor(self, menuitem, color)
            mainthread.runBlock(self.oofcanvas.set_contourmap_textcolor, (color,))
            self.oofcanvas.render()
        finally:
            self.releaseGfxLock()


    def setRubberband(self, rubberband):
        self.rubberband = rubberband
        self.oofcanvas.set_rubberband(rubberband)
       
    # menu callback
    def toggleAntialias(self, menuitem, antialias):
        ghostgfxwindow.GhostGfxWindow.toggleAntialias(
            self, menuitem, antialias)
        self.newCanvas()
        # Draw is subthread-safe, devices are all buffered.
        self.draw()

    def toggleContourpane(self, menuitem, contourpane):
        ghostgfxwindow.GhostGfxWindow.toggleContourpane(
            self, menuitem, contourpane)
        self.newCanvas()
        # Draw is subthread-safe, devices are all buffered.
        self.draw()

    def contourpanewidthCB(self, menuitem, fraction):
        ghostgfxwindow.GhostGfxWindow.contourpanewidthCB(
            self, menuitem, fraction)
        self.newCanvas()
        # Draw is subthread-safe, devices are all buffered.
        self.draw()





    def saveImage(self, menuitem, filename, overwrite):
        mainthread.runBlock(self.oofcanvas.saveImageThreaded, (filename,))


    def marginCB(self, menuitem, fraction):
        self.oofcanvas.set_margin(fraction)

##############################################

# This function redefines the one in GfxWindowManager when the GUI
# code is loaded.

def _newWindow(self, name, **kwargs):
    if top(): # if in GUI mode
        return GfxWindow3D(name, self, **kwargs)
    return ghostgfxwindow.GhostGfxWindow(name, self, **kwargs)

gfxmanager.GfxWindowManager._newWindow = _newWindow



