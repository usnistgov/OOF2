# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common import toolbox
from ooflib.common import primitives
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import widgetscope
from gi.repository import Gtk

class GfxToolbox(widgetscope.WidgetScope):
    def __init__(self, name, toolbox):
        debug.mainthreadTest()
        self.toolbox = toolbox          # non-GUI toolbox
        # root of toolbox's gtk widget tree:        
        self.gtk = Gtk.Frame(shadow_type=Gtk.ShadowType.NONE)
        gtklogger.setWidgetName(self.gtk, name)
        self.active = 0
        self._name = name
        widgetscope.WidgetScope.__init__(self, parent=None)
    def name(self):
        return self._name
    def close(self):
        pass
    def activate(self):
        self.active = 1
    def deactivate(self):
        self.active = 0
    def gfxwindow(self):
        return self.toolbox.gfxwindow()
    def __cmp__(self, other):           # for sorting in gfxwindow's list
        return cmp(self.toolbox.ordering, other.toolbox.ordering)
    # convenience function to get a point object from mouseclick coordinates
    def getPoint(self, x, y):
        return primitives.Point(x,y)

# The base Toolbox class doesn't make a GUI, but it provides a trivial
# makeGUI function so that derived toolboxes that don't create a GUI
# don't have to define makeGUI themselves.

def _makeGUI(self):
    pass

toolbox.Toolbox.makeGUI = _makeGUI
