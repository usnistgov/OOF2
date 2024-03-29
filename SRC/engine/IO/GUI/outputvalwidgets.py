# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Widgets for displaying OutputVals.

# These are used in the MeshDataGUI.  They just display the value, not
# the name of the Output. TODO: They probably should display the name
# too, so that the Concatenate output is less confusing.

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import corientation
from ooflib.SWIG.engine import fieldindex
from ooflib.SWIG.engine import outputval
from ooflib.SWIG.engine import symmmatrix
from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from ooflib.engine.IO import outputClones

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# The generic output value widget just prints the value.

## TODO: Widgets should have labels that display the Output's
## shortrepr().  The problem is that the widget is created by the
## OutputVal, not the Output.

class GenericOVWidget:
    def __init__(self, val, **kwargs):
        debug.mainthreadTest()
        if val is not None:
            self.gtk = Gtk.Entry(editable=False, **kwargs)
            gtklogger.setWidgetName(self.gtk, 'generic')
            self.gtk.set_text(repr(val))
        else:
            self.gtk = Gtk.Label(label="No data")
            self.gtk.set_sensitive(False)
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()
    def show(self):
        debug.mainthreadTest()
        self.gtk.show()

####################
        
class VectorWidget:
    def __init__(self, val, **kwargs):
        debug.mainthreadTest()
        components = list(val.components())
        if components:
            self.gtk = Gtk.Grid(row_spacing=2, column_spacing=2,**kwargs)
            row = 0
            for comp in components:
                label = Gtk.Label(label=comp.shortrepr()+':',
                                  halign=Gtk.Align.END)
                self.gtk.attach(label, 0,row, 1,1)
                entry = Gtk.Entry(editable=False, halign=Gtk.Align.FILL,
                                  hexpand=True)
                gtklogger.setWidgetName(entry, comp.shortrepr())
                entry.set_text("%-13.6g" % val[comp])
                self.gtk.attach(entry, 1,row, 1,1)
                row += 1
        else:
            self.gtk = Gtk.Label(label="No data", **kwargs)
            self.gtk.set_sensitive(False)
    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

def _VectorOutputVal_makeWidget(self, **kwargs):
    return VectorWidget(self, **kwargs)

outputval.VectorOutputVal.makeWidget = _VectorOutputVal_makeWidget

outputval.ListOutputVal.makeWidget = _VectorOutputVal_makeWidget
corientation.COrientation.makeWidget = _VectorOutputVal_makeWidget

####################

# There is another SymmMatrix3Widget object in tensorwidgets.py, but
# it's primarily used for the input of tensor-valued parameters in
# properties.  It's sufficiently different that combining the two is
# probably not useful.

class SymmMatrix3Widget:
    def __init__(self, val, **kwargs):
        debug.mainthreadTest()
        self.gtk = Gtk.Grid(**kwargs)
        rowlabels = [None]*3
        collabels = [None]*3
        for ijcomp in fieldindex.symTensorIJComponents:
            row = ijcomp.row()
            col = ijcomp.col()
            ijstr = ijcomp.shortrepr()
            if not rowlabels[row]:
                rowlabels[row] = ijstr[0]
                label = Gtk.Label(label=rowlabels[row]+': ',
                                  halign=Gtk.Align.END, hexpand=False)
                self.gtk.attach(label, 0,row+1, 1,1)
            if not collabels[col]:
                collabels[col] = ijstr[1]
                label = Gtk.Label(label=collabels[col], hexpand=True,
                                  halign=Gtk.Align.FILL)
                self.gtk.attach(label, col+1,0, 1,1)
            entry = Gtk.Entry(editable=False, halign=Gtk.Align.FILL,
                              hexpand=True)
            gtklogger.setWidgetName(entry, rowlabels[row]+collabels[col])
            self.gtk.attach(entry, col+1,row+1, 1,1)
            entry.set_text("%-13.6g" % val[ijcomp])
            
    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

def _SymmMatrix_makeWidget(self, **kwargs):
    return SymmMatrix3Widget(self, **kwargs)

symmmatrix.SymmMatrix3.makeWidget = _SymmMatrix_makeWidget
                

####################

class ConcatenatedOutputsWidget:
    def __init__(self, val, **kwargs):
        quargs = kwargs.copy()
        quargs.setdefault('spacing', 2)
        self.gtk = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, **quargs)
        # Use makeWidget(v) instead of v.makeWidget() so that
        # GenericOVWidget will be used if needed for subwidgets.
        self.widgets = [makeWidget(v) for v in val.args]
        first = True
        self.sbcallbacks = []
        for w in self.widgets:
            if not first:
                self.gtk.pack_start(
                    Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL),
                    expand=False, fill=False, padding=0)
            first = False
            self.gtk.pack_start(w.gtk, expand=0, fill=1, padding=0)
            self.sbcallbacks.append(
                switchboard.requestCallbackMain(w.gtk, self.subWidgetChanged))
    def cleanUp(self):
        switchboard.removeCallbacks(self.sbcallbacks)
    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()
    def subWidgetChanged(self, interactive):
        switchboard.notify(self)

def _ConcatenatedOutputs_makeWidget(self):
    return ConcatenatedOutputsWidget(self)
        
outputClones.ConcatenatedOutputVal.makeWidget = _ConcatenatedOutputs_makeWidget


####################

def makeWidget(val, **kwargs):
    try:
        wfunc = val.makeWidget
    except AttributeError:
        return GenericOVWidget(val, **kwargs)
    return wfunc(**kwargs)

