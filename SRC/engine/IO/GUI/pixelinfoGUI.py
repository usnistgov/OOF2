# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import material
from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import pixelinfoGUIplugin

from gi.repository import Gtk

class MaterialPlugIn(pixelinfoGUIplugin.PixelInfoGUIPlugIn):
    ordering = 3
    nrows = 1
    def __init__(self, toolbox, table, row):
        debug.mainthreadTest()
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.__init__(self, toolbox)

        label = Gtk.Label('material=', halign=Gtk.Align.END, hexpand=False)
        table.attach(label, 0,row, 1,1)
        self.materialtext = gtk.Entry(editable=False,
                                      halign=Gtk.Align.FILL, hexpand=True)
        gtklogger.setWidgetName(self.materialtext, 'material')
        self.materialtext.set_width_chars(12)
        table.attach(self.materialtext, 1,row, 1,1)
        self.sbcb = switchboard.requestCallbackMain(
            'materials changed in microstructure', self.matchanged)

    def close(self):
        switchboard.removeCallback(self.sbcb)
        pixelinfoGUIplugin.PixelInfoGUIPlugIn.close(self)

    def update(self, where):
        debug.mainthreadTest()
        microstructure = self.toolbox.findMicrostructure()
        if microstructure and where is not None:
            mat = material.getMaterialFromPoint(microstructure, where)
            if mat:
                self.materialtext.set_text(mat.name())
                return
        self.materialtext.set_text('<No material>')

    def clear(self):
        debug.mainthreadTest()
        self.materialtext.set_text("")

    def nonsense(self):
        debug.mainthreadTest()
        self.materialtext.set_text('???')

    def matchanged(self, ms):
        if ms is self.toolbox.findMicrostructure():
            self.update(self.toolbox.currentPixel())

pixelinfoGUIplugin.registerPlugInClass(MaterialPlugIn)
