# -*- python -*-
# $RCSfile: toolboxGUI.py,v $
# $Revision: 1.19 $
# $Author: langer $
# $Date: 2014/09/27 21:40:36 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.common import debug
from ooflib.common import toolbox
from ooflib.common import primitives
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import widgetscope
import gtk
import sys

class GfxToolbox(widgetscope.WidgetScope):
    def __init__(self, name, toolbox):
        debug.mainthreadTest()
        self.toolbox = toolbox          # non-GUI toolbox
        self.gtk = gtk.Frame()          # root of toolbox's gtk widget tree
        gtklogger.setWidgetName(self.gtk, name)
        self.gtk.set_shadow_type(gtk.SHADOW_NONE)
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
    # needed for 3D only
    def updateview(self):
        camera = self.gfxwindow().oofcanvas.getCamera()
        camera.OrthogonalizeViewUp()
        self.gfxwindow().oofcanvas.calculateclipping(clippingadj.get_value())
        self.gfxwindow().oofcanvas.render()
    # convenience function to get a point object from mouseclick coordinates
    def getPoint(self, x, y):
        if config.dimension() == 2:
            return primitives.Point(x,y)
        elif config.dimension() == 3:
            return self.gfxwindow().oofcanvas.screenCoordsTo3DCoords(x,y)        

#static variable for all toolboxes, does this belong here?
clippingadj = gtk.Adjustment(value=100, lower=0, upper=100, step_incr=-1, page_incr=-5, page_size=0)

# The base Toolbox class doesn't make a GUI, but it provides a trivial
# makeGUI function so that derived toolboxes that don't create a GUI
# don't have to define makeGUI themselves.

def _makeGUI(self):
    pass

toolbox.Toolbox.makeGUI = _makeGUI
