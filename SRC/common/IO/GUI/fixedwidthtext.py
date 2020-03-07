# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

OBSOLETE

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common.IO.GUI import mainmenuGUI
from gi.repository import Gtk

class FixedWidthTextView(Gtk.TextView):
    def __init__(self, *args, **kwargs):
        Gtk.TextView.__init__(self, *args, **kwargs)
        self.sbcb = switchboard.requestCallbackMain('change fixed font',
                                                    self.changeFontSize)
        self.connect('destroy', self.destroyCB)
        self.changeFont(mainmenuGUI.getFixedFontSize())
        self.styleProvider = None

    def changeFontSize(self, size):
        debug.mainthreadTest()
        styleContext = self.get_style_context()
        if self.styleProvider:
            styleContext.remove_provider(self.styleProvider)
        self.styleProvider = Gtk.CssProvider()
        self.styleProvider.load_from_data(
            "textview { font: %dpx monospace; }" % size)
        styleContext.add_provider(self.styleProvider,
                                  Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
    def destroyCB(self, *args):
        switchboard.removeCallback(self.sbcb)
