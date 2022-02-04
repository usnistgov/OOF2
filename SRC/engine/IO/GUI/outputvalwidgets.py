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

from gi.repository import Gtk

# The generic output value widget just prints the value.

## TODO: Widgets should have labels that display the Output's
## shortrepr().  The problem is that the widget is created by the
## OutputVal, not the Output.

## TODO PYTHON3: Check that 2to3 was correct in changing
## iterator.next() to next(iterator) a bunch of places in this file.

class GenericOVWidget:
    def __init__(self, val, **kwargs):
        debug.mainthreadTest()
        if val is not None:
            self.gtk = Gtk.Entry(editable=False, **kwargs)
            gtklogger.setWidgetName(self.gtk, 'generic')
            self.gtk.set_text(repr(val))
        else:
            self.gtk = Gtk.Label("No data")
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
        iterator = val.getIterator()
        if iterator.size() != 0:
            self.gtk = Gtk.Grid(row_spacing=2, column_spacing=2,**kwargs)
            row = 0
            while not iterator.end():
                label = Gtk.Label(iterator.shortrepr()+':',
                                  halign=Gtk.Align.END)
                self.gtk.attach(label, 0,row, 1,1)
                entry = Gtk.Entry(editable=False, halign=Gtk.Align.FILL,
                                  hexpand=True)
                gtklogger.setWidgetName(entry, iterator.shortrepr())
                entry.set_text("%-13.6g" % val[iterator])
                self.gtk.attach(entry, 1,row, 1,1)
                row += 1
                next(iterator)
        else:
            self.gtk = Gtk.Label("No data", **kwargs)
            self.gtk.set_sensitive(False)
    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

def _VectorOutputVal_makeWidget(self, **kwargs):
    return VectorWidget(self, **kwargs)

outputval.VectorOutputValPtr.makeWidget = _VectorOutputVal_makeWidget

outputval.ListOutputValPtr.makeWidget = _VectorOutputVal_makeWidget
corientation.COrientationPtr.makeWidget = _VectorOutputVal_makeWidget

####################

# There is another SymmMatrix3Widget object in tensorwidgets.py, but
# it's primarily used for the input of tensor-valued parameters in
# properties.  It's sufficiently different that combining the two is
# probably not useful.

class SymmMatrix3Widget:
    def __init__(self, val, **kwargs):
        debug.mainthreadTest()
        self.gtk = Gtk.Grid(**kwargs)
        iterator = val.getIterator()
        rowlabels = [None]*3
        collabels = [None]*3
        while not iterator.end():
            comps = iterator.components()
            row = comps[0]
            col = comps[1]
            ijstr = iterator.shortrepr()
            if not rowlabels[row]:
                rowlabels[row] = ijstr[0]
                label = Gtk.Label(rowlabels[row]+': ', halign=Gtk.Align.END,
                                  hexpand=False)
                self.gtk.attach(label, 0,row+1, 1,1)
            if not collabels[col]:
                collabels[col] = ijstr[1]
                label = Gtk.Label(collabels[col], hexpand=True,
                                  halign=Gtk.Align.FILL)
                self.gtk.attach(label, col+1,0, 1,1)
            entry = Gtk.Entry(editable=False, halign=Gtk.Align.FILL,
                              hexpand=True)
            gtklogger.setWidgetName(entry, rowlabels[row]+collabels[col])
            self.gtk.attach(entry, col+1,row+1, 1,1)
            entry.set_text("%-13.6g" % val[iterator])
            next(iterator)
            
    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

def _SymmMatrix_makeWidget(self, **kwargs):
    return SymmMatrix3Widget(self, **kwargs)

symmmatrix.SymmMatrix3Ptr.makeWidget = _SymmMatrix_makeWidget
                

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

