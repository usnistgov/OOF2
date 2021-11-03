# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import pixelgroup
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common import subthread
from ooflib.common.IO import pixelinfo
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import pixelinfoGUIplugin
from ooflib.common.IO.GUI import toolboxGUI
from gi.repository import Gtk
import ooflib.common.microstructure


class PixelInfoToolboxGUI(toolboxGUI.GfxToolbox, mousehandler.MouseHandler):
    def __init__(self, pixelinfotoolbox):
        debug.mainthreadTest()
        toolboxGUI.GfxToolbox.__init__(self, "Pixel Info", pixelinfotoolbox)
        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                          margin_start=2, margin_end=2)
        self.gtk.add(mainbox)

        self.grid = Gtk.Grid(column_spacing=2, row_spacing=2)
        mainbox.pack_start(self.grid, expand=False, fill=False, padding=0)
        
        label = Gtk.Label('x=', halign=Gtk.Align.END, hexpand=False)
        self.grid.attach(label, 0,0,1,1)
        self.xtext = Gtk.Entry(halign=Gtk.Align.FILL, hexpand=True)
        gtklogger.setWidgetName(self.xtext, "X")
        self.xtext.set_width_chars(10)
        self.grid.attach(self.xtext, 1,0,1,1)

        label = Gtk.Label('y=', halign=Gtk.Align.END, hexpand=False)
        self.grid.attach(label, 0,1,1,1)
        self.ytext = Gtk.Entry(halign=Gtk.Align.FILL, hexpand=True)
        gtklogger.setWidgetName(self.ytext, "Y")
        self.ytext.set_width_chars(10)
        self.grid.attach(self.ytext, 1,1,1,1)

        self.xtsignal = gtklogger.connect(self.xtext, 'changed',
                                          self.pointChanged)
        self.ytsignal = gtklogger.connect(self.ytext, 'changed',
                                          self.pointChanged)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                      homogeneous=True, spacing=2)
        self.grid.attach(box, 0,2, 2,1) # box spans both grid columns
        self.updatebutton = gtkutils.StockButton("view-refresh-symbolic",
                                                 'Update',
                                                 halign=Gtk.Align.FILL,
                                                 hexpand=True)
        box.pack_start(self.updatebutton, expand=True, fill=True, padding=0)
        gtklogger.setWidgetName(self.updatebutton, "Update")
        gtklogger.connect(self.updatebutton, 'clicked', self.updateButtonCB)
        self.clearbutton = gtkutils.StockButton("edit-clear-symbolic", 'Clear',
                                                halign=Gtk.Align.FILL,
                                                hexpand=True)
        box.pack_start(self.clearbutton, expand=True, fill=True, padding=0)
        gtklogger.setWidgetName(self.clearbutton, "Clear")
        gtklogger.connect(self.clearbutton, 'clicked', self.clearButtonCB)

        self.updatebutton.set_sensitive(0)
        self.clearbutton.set_sensitive(0)
        self.buildGUI()
        
        self.sbcallbacks = [
            switchboard.requestCallbackMain(pixelinfotoolbox,
                                            self.update),
            switchboard.requestCallbackMain('new pixelinfo GUI plugin',
                                            self.buildGUI),
            switchboard.requestCallbackMain((self.gfxwindow(),
                                             'layers changed'), self.update)
            ]

    def buildGUI(self):
        debug.mainthreadTest()
        row = 4
        self.plugins = []
        for pluginclass in pixelinfoGUIplugin.plugInClasses:
            hsep = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
            self.grid.attach(hsep, 0,row, 2,1)
            self.plugins.append(pluginclass(self, self.grid, row+1))
            row += pluginclass.nrows + 1

    def activate(self):
        toolboxGUI.GfxToolbox.activate(self)
        self.gfxwindow().setMouseHandler(self)

    def deactivate(self):
        toolboxGUI.GfxToolbox.deactivate(self)
        self.gfxwindow().removeMouseHandler()

    def close(self):
        map(switchboard.removeCallback, self.sbcallbacks)
        for plugin in self.plugins:
            plugin.close()
        self.plugins = []

    def findGUIPlugIn(self, plugInClass):
        for plugin in self.plugins:
            if isinstance(plugin, plugInClass):
                return plugin

    def acceptEvent(self, eventtype):
        return eventtype == 'up'

    # It's possible to click on the background of the canvas, but
    # outside the image/microstructure.  In this case, do nothing --
    # the behavior is then the same as if you click outside the drawn
    # area.
    def up(self, x, y, button, shift, ctrl, data):
        msOrImage = self.gfxwindow().topmost('Microstructure', 'Image')
        if msOrImage:
            where = msOrImage.pixelFromPoint(primitives.Point(x,y))
            if msOrImage.pixelInBounds(where):
                self.toolbox.menu.Query(x=where.x, y=where.y)
        else:
            for plugin in self.plugins:
                plugin.nonsense();
            

    def currentPixel(self):
        return self.toolbox.currentPixel()
    
    def update(self):
        debug.mainthreadTest()
        self.xtsignal.block()
        self.ytsignal.block()
        try:
            where = self.currentPixel()

            if where is not None:
                self.clearbutton.set_sensitive(1)
            else:
                self.xtext.set_text('')
                self.ytext.set_text('')
                self.clearbutton.set_sensitive(0)
                for plugin in self.plugins:
                    plugin.clear()

            msOrImage = self.gfxwindow().topmost('Microstructure', 'Image')
            if where is not None and msOrImage is not None:
                self.xtext.set_text(`where.x`)
                self.ytext.set_text(`where.y`)
                size = msOrImage.sizeInPixels() # might be ICoord or iPoint
                if 0 <= where.x < size[0] and 0 <= where.y < size[1]:
                    for plugin in self.plugins:
                        plugin.update(where)
                else:
                    for plugin in self.plugins:
                        plugin.nonsense()
            else:
                for plugin in self.plugins:
                    plugin.nonsense()

                self.updatebutton.set_sensitive(0)
        finally:
            self.xtsignal.unblock()
            self.ytsignal.unblock()

        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " updated")

    def updateButtonCB(self, button):
        debug.mainthreadTest()
        self.updatebutton.set_sensitive(0)
        x = int(self.xtext.get_text())
        y = int(self.ytext.get_text())
        msOrImage = self.gfxwindow().topmost('Microstructure', 'Image')
        size = msOrImage.sizeInPixels() # might be ICoord or iPoint
        if x < 0 or x >= size[0] or y < 0 or y >= size[1]: # illegal size
            self.update()               # restore original values
            return
        self.toolbox.menu.Query(x=x, y=y)

    def clearButtonCB(self, button):
        self.toolbox.menu.Clear()

    def pointChanged(self, *args):
        debug.mainthreadTest()
        self.updatebutton.set_sensitive(1)

    def findMicrostructure(self):
        return self.toolbox.findMicrostructure()

def _makeGUI(self):
    return PixelInfoToolboxGUI(self)

pixelinfo.PixelInfoToolbox.makeGUI = _makeGUI

