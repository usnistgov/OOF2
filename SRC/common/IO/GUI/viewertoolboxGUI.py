# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common.IO import reporter
from ooflib.common.IO import viewertoolbox
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.common.IO.mainmenu import OOF
from gi.repository import Gtk

ndigits = 10

class ViewerToolboxGUI(toolboxGUI.GfxToolbox, mousehandler.MouseHandler):
    def __init__(self, viewertoolbox):
        debug.mainthreadTest()

        toolboxGUI.GfxToolbox.__init__(self, "Viewer", viewertoolbox)
        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        infoframe = Gtk.Frame(label="Position Information", margin=2)
        infoframe.set_shadow_type(Gtk.ShadowType.NONE)
        mainbox.pack_start(infoframe, fill=False, expand=False, padding=0)

        infotable = Gtk.Grid()
        infoframe.add(infotable)
        pixellabel = Gtk.Label("Pixel: ",
                               halign=Gtk.Align.END, hexpand=False)
        self.pixel_x = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.pixel_x, "PixelX")
        self.pixel_x.set_width_chars(ndigits)
        self.pixel_y = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.pixel_y, "PixelY")
        self.pixel_y.set_width_chars(ndigits)
        physicallabel = Gtk.Label("Physical: ",
                                  halign=Gtk.Align.END, hexpand=False)
        self.physical_x = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.physical_x, "PhysicalX")
        self.physical_x.set_width_chars(ndigits)
        self.physical_y = Gtk.Entry(editable=False)
        gtklogger.setWidgetName(self.physical_y, "PhysicalY")
        self.physical_y.set_width_chars(ndigits)

        infotable.attach(pixellabel,      0,0, 1,1)
        infotable.attach(self.pixel_x,    1,0, 1,1)
        infotable.attach(self.pixel_y,    2,0, 1,1)
        infotable.attach(physicallabel,   0,1, 1,1)
        infotable.attach(self.physical_x, 1,1, 1,1)
        infotable.attach(self.physical_y, 2,1, 1,1)

        zoomframe = Gtk.Frame(label="Zoom", margin=2)
        gtklogger.setWidgetName(zoomframe, "Zoom")
        zoomframe.set_shadow_type(Gtk.ShadowType.NONE)
        mainbox.pack_start(zoomframe, fill=False, expand=False, padding=0)
        zoombox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                          margin=2)
        zoomframe.add(zoombox)

        buttonrow = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            homogeneous=True, spacing=2, margin=2)
        zoombox.pack_start(buttonrow, expand=False, fill=True, padding=0)
        inbutton = gtkutils.StockButton("zoom-in-symbolic", 'In')
        buttonrow.pack_start(inbutton, expand=False, fill=True, padding=0)
        gtklogger.setWidgetName(inbutton, "In")
        gtklogger.connect(inbutton, 'clicked', self.inCB)
        outbutton = gtkutils.StockButton("zoom-out-symbolic", 'Out')
        buttonrow.pack_start(outbutton, expand=False, fill=True, padding=0)
        gtklogger.setWidgetName(outbutton, "Out")
        gtklogger.connect(outbutton, 'clicked', self.outCB)
        fillbutton = gtkutils.StockButton("zoom-fit-best-symbolic", 'Fill')
        buttonrow.pack_start(fillbutton, expand=False, fill=True, padding=0)
        gtklogger.setWidgetName(fillbutton, "Fill")
        gtklogger.connect(fillbutton, 'clicked', self.fillCB)

        factorrow = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                            margin=2)
        zoombox.pack_start(factorrow, expand=False, fill=False, padding=0)
        factorrow.pack_start(Gtk.Label("Zoom Factor: "),
                             expand=False, fill=False, padding=0)
        self.zoomfactor = Gtk.Entry(editable=True)
        self.zoomfactor.set_width_chars(ndigits)
        gtklogger.setWidgetName(self.zoomfactor, "Factor")
        self.zfactorsignal = gtklogger.connect_passive(
            self.zoomfactor,"changed")
        factorrow.pack_start(self.zoomfactor, expand=True, fill=True, padding=0)

        zoombox.pack_start(
            Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL, margin=2),
            fill=False, expand=False, padding=2)

        label0 = Gtk.Label("Shift+Click: Zoom in\nCtrl+Click: Zoom out",
                           halign=Gtk.Align.CENTER,
                           margin_bottom=2)
        label0.set_pattern("             _______\n            ________\n")
        label0.set_justify(Gtk.Justification.LEFT)
        zoombox.pack_start(label0, fill=False, expand=False, padding=0)

        canvas_info = gtkutils.StockButton("dialog-information-symbolic",
                                           "Canvas Info",
                                           halign=Gtk.Align.CENTER,
                                           margin=2)
        gtklogger.setWidgetName(canvas_info, "Info")
        gtklogger.connect(canvas_info, "clicked", self.canvas_infoCB)
        canvas_info.set_tooltip_text(
            "Display canvas information in the message window.")
        mainbox.pack_end(canvas_info, expand=False, fill=False, padding=0)

        self.currentZFactor = self.gfxwindow().zoomFactor()

        switchboard.requestCallbackMain("zoom factor changed",
                                        self.zfactorCB)

        # Make sure that the Zoom commands in the graphics windows
        # Settings menu use an up-to-date zoom factor.
        self.gfxwindow().menu.Settings.Zoom.In.add_gui_callback(
            self.wrapMenuZoom)
        self.gfxwindow().menu.Settings.Zoom.Out.add_gui_callback(
            self.wrapMenuZoom)


    def activate(self):
        toolboxGUI.GfxToolbox.activate(self)
        self.gfxwindow().setMouseHandler(self)
        self.updateZFactor()

    def zfactorCB(self, *args):         # switchboard "zoom factor changed"
        self.updateZFactor()
        
    def updateZFactor(self):
        debug.mainthreadTest()
        self.currentZFactor = self.gfxwindow().zoomFactor()
        self.zfactorsignal.block()
        self.zoomfactor.set_text("%g"% self.currentZFactor)
        self.zfactorsignal.unblock()

    def zoomfactorChanged(self, *args):  # gtk callback
        self.getNewZoomFactor()

    def wrapMenuZoom(self, menuitem):
        # gui callback for Zoom commands in the Settings menu.
        self.getNewZoomFactor()
        menuitem()
        
    def findMicrostructure(self):
        who = self.toolbox.gfxwindow().topwho('Microstructure', 'Image',
                                              'Skeleton', 'Mesh')
        if who is not None:
            return who.getMicrostructure()

    def acceptEvent(self, eventtype):
        ## If we were allowing the canvas to be dragged to a new
        ## position, we'd have to accept 'down' and 'move' as well.
        return eventtype == 'up'
##        return eventtype in ('down', 'move', 'up')

    # World coord from world_coord() needs to be recalibrated.
    def recalibrate(self, point):
        return primitives.Point(point.x, -point.y)

    def get_proper_world_coord(self, i, j):
        temp = self.gfxwindow().oofcanvas.world_coord(i, j)
        return self.recalibrate(temp)

    def canvas_infoCB(self, *args):
        debug.mainthreadTest()
        # Visible canvas size in pixel units
        xmax = self.gfxwindow().oofcanvas.get_width_in_pixels()-1
        ymax = self.gfxwindow().oofcanvas.get_height_in_pixels()-1
        # Visible MS in physical units
        ll = self.get_proper_world_coord(0, ymax)
        ur = self.get_proper_world_coord(xmax, 0)
        reporter.report("### Canvas Information ###")
        reporter.report("Width (pixels)    : ", xmax)
        reporter.report("Height (pixels)   : ", ymax)
        reporter.report("Lower-left corner : ", ll)
        reporter.report("Upper-right corner: ", ur)
        reporter.report("H-scroll position : ",
                        self.gfxwindow().hScrollPosition())
        reporter.report("V-scroll position : ",
                        self.gfxwindow().vScrollPosition())
        reporter.report("Pixels per unit   : ",
                        self.gfxwindow().oofcanvas.get_pixels_per_unit())
        reporter.report("Canvas allocation : ",
                        self.gfxwindow().oofcanvas.get_allocation())
        reporter.report("Scroll region     : ",
                        self.gfxwindow().oofcanvas.get_scrollregion())

    def inCB(self, *args):              # gtk callback
        self.getNewZoomFactor()
        self.gfxwindow().menu.Settings.Zoom.In()
    def outCB(self, *args):             # gtk callback
        self.getNewZoomFactor()
        self.gfxwindow().menu.Settings.Zoom.Out()
    def fillCB(self, *args):            # gtk callback
        self.gfxwindow().menu.Settings.Zoom.Fill_Window()

    def getNewZoomFactor(self):
        debug.mainthreadTest()
        # The zoomfactor widget doesn't have any gtk callbacks because
        # all of the signals generate either too few or too many
        # events.  getNewZoomFactor must be called before the zoom
        # factor is used in case the user has changed the zoomfactor
        # widget.
        txt = self.zoomfactor.get_text()
        if not txt:
            # Nothing's been entered yet, just use the default value
            return
        try:
            factor = float(txt)
        except ValueError:
            raise ooferror.ErrUserError("Bad zoom factor! %s" % txt)
        if factor != self.currentZFactor:
            # Use runBlock to ensure that the new zoom factor is set
            # before being used.
            mainthread.runBlock(
                self.gfxwindow().menu.Settings.Zoom.Zoom_Factor,
                kwargs={'factor':factor})
        
    def up(self, x, y, button, shift, ctrl, data):
        debug.mainthreadTest()
        ms = self.findMicrostructure()
        if ms:
            pixel = ms.pixelFromPoint(primitives.Point(x,y))
            if ms.pixelInBounds(pixel):
                self.pixel_x.set_text("%d" % pixel.x)
                self.pixel_y.set_text("%d" % pixel.y)
                self.physical_x.set_text("%-11.4g" % x)
                self.physical_y.set_text("%-11.4g" % y)

        if shift and not ctrl:
            self.getNewZoomFactor()
            self.gfxwindow().menu.Settings.Zoom.InFocussed(
                focus=primitives.Point(x,y))
        elif not shift and ctrl:
            self.getNewZoomFactor()
            self.gfxwindow().menu.Settings.Zoom.OutFocussed(
                focus=primitives.Point(x,y))

##    def move(self, x, y, shift, ctrl):
##        debug.mainthreadTest()

def _makeGUI(self):
    return ViewerToolboxGUI(self)

viewertoolbox.ViewerToolbox.makeGUI = _makeGUI
    
