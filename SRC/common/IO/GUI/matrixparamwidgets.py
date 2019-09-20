# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This file contains the definitions of input widgets used for
# the input of matrix data.  These are usable as parameterwidgets.

from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import widgetscope
import gtk
import math
import types


# An array of input things.  Exactly which kind of input thing is
# determined by the paramtype argument, which must be a Parameter
# subclass.  An array of that subclass's widgets will be
# built. paramargs is a dictionary containing the default arguments
# for the Parameter's constructor.

# MatrixInputBase does not create a working ParameterWidget all by
# itself, since it doesn't set and display a single Parameter
# containing all of the matrix entries. See cijklparamwidgets.py
# for examples of subclasses that do work as ParameterWidgets.

class MatrixInputBase(parameterwidgets.ParameterWidget,
                  widgetscope.WidgetScope):
    def __init__(self, label, rows, cols, paramtype, paramargs={},
                 value=None, scope=None, name=None):
        debug.mainthreadTest()
        frame = gtk.Frame()
        self.table = gtk.Table(rows=rows+2, columns=cols+2)
        frame.add(self.table)
        parameterwidgets.ParameterWidget.__init__(self, frame, scope, name)
        widgetscope.WidgetScope.__init__(self, scope)
        self.rows = rows
        self.cols = cols
        self.widgets = {}
        self.sbcallbacks = []

        # Labels.
        for r in range(self.rows):
            lbl = gtk.Label(' %d ' % (r+1))
            lbl.set_alignment(1.0, 0.5)
            self.table.attach(lbl,0,1,r+1,r+2)
        for c in range(self.cols):
            lbl = gtk.Label(`c+1`)
            self.table.attach(lbl,c+1,c+2,0,1)

        digitsize = guitop.top().digitsize
        
        for r in range(self.rows):
            for c in range(self.cols):
                # Parameters are quite lightweight, no harm in providing
                # a dummy to the FloatWidget.
                dummyparam = paramtype(name="%d,%d"%(r,c), **paramargs)
                newfloat = dummyparam.makeWidget(scope=self)
                self.sbcallbacks.append(
                    switchboard.requestCallbackMain(newfloat,
                                                    self.floatChangeCB))
                # Also, set the size -- otherwise, the matrix
                # array gets to be too big.
                newfloat.gtk.set_size_request(8*digitsize, -1)

                self.widgets[(r,c)] = newfloat
                self.table.attach(newfloat.gtk, c+1,c+2, r+1,r+2,
                                  xoptions=gtk.FILL)

        self.widgetChanged(1, interactive=0) # always valid
    def floatChangeCB(self, interactive):
        self.widgetChanged(1, interactive)
    def cleanUp(self):
        map(switchboard.removeCallback, self.sbcallbacks)
        parameterwidgets.ParameterWidget.cleanUp(self)

    # Turn the gtk.Entry 'changed' signal on and off.  Used to
    # suppress signalling loops when widgets' values depend on one
    # another.
    def block_signals(self):
        debug.mainthreadTest()
        for floatwidget in self.widgets.values():
            floatwidget.block_signal()
    def unblock_signals(self):
        debug.mainthreadTest()
        for floatwidget in self.widgets.values():
            floatwidget.unblock_signal()


# This class does different things on init than its parent,
# but is otherwise similar.
class SymmetricMatrixInputBase(MatrixInputBase):
    def __init__(self, label, rows, cols, paramtype, paramargs={},
                 value=None, scope=None, name=None):
        debug.mainthreadTest()
        frame = gtk.Frame()
        self.table = gtk.Table(rows=rows+1, columns=cols+1)
        frame.add(self.table)
        parameterwidgets.ParameterWidget.__init__(self, frame, scope, name)
        widgetscope.WidgetScope.__init__(self, scope)
        #scope.addWidget(self)
        self.rows = rows
        self.cols = cols
        self.widgets = {}
        self.sbcallbacks = []

        # Do labels first.
        for r in range(self.rows):
            lbl = gtk.Label(' %d ' % (r+1))
            lbl.set_alignment(1.0, 0.5)
            self.table.attach(lbl,0,1,r+1,r+2)
        for c in range(self.cols):
            lbl = gtk.Label(`c+1`)
            self.table.attach(lbl,c+1,c+2,0,1)

        digitsize = guitop.top().digitsize

        # Now put the actual widgets in.
        for r in range(self.rows):
            for c in range(r,self.cols):
                dummyparam = paramtype(name="%d,%d"%(r,c), **paramargs)
                newfloat = dummyparam.makeWidget(scope=self)
                self.sbcallbacks.append(
                    switchboard.requestCallbackMain(newfloat,
                                                    self.floatChangeCB))
                # Also, set the size -- otherwise, the matrix
                # array gets to be too big.
                newfloat.gtk.set_size_request(8*digitsize,-1)
                
                self.widgets[(r,c)] = newfloat
                try:
                    self.widgets[(r,c)].set_value(value[(r,c)])
                except:
                    pass
                self.table.attach(newfloat.gtk,c+1,c+2,r+1,r+2,
                                  xoptions=gtk.FILL)
        self.widgetChanged(1, interactive=0)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# MatrixInput and SymmetricMatrixInput display an array of floats.

class MatrixInput(MatrixInputBase):
    def __init__(self, label, rows, cols, value=None, scope=None, name=None):
        MatrixInputBase.__init__(self, label=label,
                                 rows=rows, cols=cols,
                                 paramtype=parameter.FloatParameter,
                                 paramargs=dict(value=0.0),
                                 value=value, scope=scope, name=name)

class SymmetricMatrixInput(SymmetricMatrixInputBase):
    def __init__(self, label, rows, cols, value=None, scope=None, name=None):
        SymmetricMatrixInputBase.__init__(self, label=label,
                                          rows=rows, cols=cols,
                                          paramtype=parameter.FloatParameter,
                                          paramargs=dict(value=0.0),
                                          value=value, scope=scope, name=name)


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# MatrixBoolInput and SymmetricMatrixBoolInput display an array of bools.

class MatrixBoolInput(SymmetricMatrixInputBase):
    def __init__(self, label, rows, cols, value=None, scope=None, name=None):
        MatrixInputBase.__init__(self, label=label,
                                 rows=rows, cols=cols,
                                 paramtype=parameter.BooleanParameter,
                                 paramargs=dict(value=False),
                                 value=value, scope=scope, name=name)

class SymmetricMatrixBoolInput(SymmetricMatrixInputBase):
    def __init__(self, label, rows, cols, value=None, scope=None, name=None):
        SymmetricMatrixInputBase.__init__(self, label=label,
                                          rows=rows, cols=cols,
                                          paramtype=parameter.BooleanParameter,
                                          paramargs=dict(value=False),
                                          value=value, scope=scope, name=name)
        
