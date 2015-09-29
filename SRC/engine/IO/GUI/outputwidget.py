# -*- python -*-
# $RCSfile: outputwidget.py,v $
# $Revision: 1.3 $
# $Author: langer $
# $Date: 2014/09/27 21:41:01 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import utils
from ooflib.engine.IO import output
from ooflib.common.IO.GUI import gfxLabelTree
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import widgetscope
import gtk

class OutputParameterWidget(parameterwidgets.ParameterWidget,
                            widgetscope.WidgetScope):
    def __init__(self, value, outputtree, scope=None, name=None):
        debug.mainthreadTest()
        frame = gtk.Frame()
        self.vbox = gtk.VBox()
        frame.add(self.vbox)
        # top part is a bunch of chooser widgets representing the
        # LabelTree of outputs.
        self.treewidget = \
                     gfxLabelTree.LabelTreeChooserWidget(outputtree,
                                                         callback=self.treeCB,
                                                         name=name)
        self.vbox.pack_start(self.treewidget.gtk, expand=0, fill=0)
        # bottom part is a ParameterTable
        self.parambox = gtk.VBox()
        gtklogger.setWidgetName(self.parambox, "Parameters")
        self.paramtable = None
        self.params = []
        self.paramhier = []
        self.vbox.pack_start(self.parambox, expand=0, fill=0)
        
        parameterwidgets.ParameterWidget.__init__(self, frame, scope, name)
        widgetscope.WidgetScope.__init__(self, scope)
        if value is not None:
            self.set_value(value)
        else:
            self.set_value(outputtree.numberOneChild())
    def show(self):
        debug.mainthreadTest()
        self.gtk.show()                 # self.gtk is the GtkFrame
        self.vbox.show()
        self.treewidget.show()
        self.parambox.show()
        if self.paramtable:
            self.paramtable.show()
    def set_value(self, value):
        if value is not None:
            self.treewidget.set_value(value.getPrototype())
            self.makeParameterTable(value, interactive=0)
    def makeParameterTable(self, value, interactive):
        debug.mainthreadTest()
        self.destroyParameterTable()
        # get the hierarchical list of clones of the settable parameters
        self.paramhier = value.listAllParametersHierarchically(onlySettable=1)
        self.params = utils.flatten_all(self.paramhier)
        if self.params:
            self.paramtable = \
                            parameterwidgets.HierParameterTable(self.paramhier,
                                                                scope=self)
            self.parambox.pack_start(self.paramtable.gtk, expand=0, fill=0)
            self.widgetChanged(self.paramtable.isValid(), interactive)
            self.paramtable.show()
            self.sbcallback = switchboard.requestCallbackMain(
                self.paramtable, self.tableChangedCB)
        else:
            self.paramtable = None
            self.widgetChanged(1, interactive)
    def get_value(self):
        if self.paramtable is not None:
            self.paramtable.get_values()
        outputprototype = self.treewidget.get_value()
        if outputprototype:
            # Because we're working with clones of the Parameters in
            # the prototype, paramtable.get_values() hasn't set the
            # prototype Parameters.  Therefore we need to set the
            # parameters in the prototype's clone here.
            pdict = {}
            for param in self.params:
                pdict[param.name] = param.value
            bozo = outputprototype.clone(params=pdict)
            return bozo
    def destroyParameterTable(self):
        debug.mainthreadTest()
        if self.paramtable is not None:
            table = self.paramtable
            self.paramtable = None
            table.destroy()
            switchboard.removeCallback(self.sbcallback)
    def treeCB(self):
        self.makeParameterTable(self.treewidget.get_value(), interactive=1)
    def tableChangedCB(self, arg):      # switchboard callback
        self.widgetChanged(self.paramtable.isValid(), interactive=1)

######################
        
class ScalarOutputParameterWidget(OutputParameterWidget):
    def __init__(self, value, scope=None, name=None):
        OutputParameterWidget.__init__(self, value, output.scalarOutputs,
                                       scope=scope, name=name)

def _ScalarOutputParameter_makeWidget(self, scope=None):
    return ScalarOutputParameterWidget(self.value, scope=scope, name=self.name)

output.ScalarOutputParameter.makeWidget = _ScalarOutputParameter_makeWidget



class PositionOutputParameterWidget(OutputParameterWidget):
    def __init__(self, value, scope=None, name=None):
        OutputParameterWidget.__init__(self, value, output.positionOutputs,
                                       scope=scope, name=name)

def _PositionOutputParameter_makeWidget(self, scope=None):
    return PositionOutputParameterWidget(self.value, scope=scope,
                                         name=self.name)

output.PositionOutputParameter.makeWidget = _PositionOutputParameter_makeWidget

class AggregateOutputParameterWidget(OutputParameterWidget):
    def __init__(self, value, scope=None, name=None):
        OutputParameterWidget.__init__(self, value, output.aggregateOutputs,
                                       scope=scope, name=name)

def _AggregateOutputParameter_makeWidget(self, scope=None):
    return AggregateOutputParameterWidget(self.value, scope=scope,
                                          name=self.name)

output.AggregateOutputParameter.makeWidget = \
                                           _AggregateOutputParameter_makeWidget

#####################

# The widget for a ValueOutputParameter displays either the
# ScalarOutputs or the AggregateOutputs, depending on the setting of
# an EnumWidget for the OutputType.

class ValueOutputWidget(parameterwidgets.ParameterWidget, 
                        widgetscope.WidgetScope):
    def __init__(self, value, scope=None, name=None):
        debug.mainthreadTest()
        widgetscope.WidgetScope.__init__(self, scope)
        self.scalar_output_obj = ScalarOutputParameterWidget(
            None, scope=self, name="Scalar")
        self.aggregate_output_obj = AggregateOutputParameterWidget(
            None, scope=self, name="Aggregate")
        parameterwidgets.ParameterWidget.__init__(self, gtk.VBox(), scope, name)
        self.gtk.pack_start(self.scalar_output_obj.gtk,
                            expand=False, fill=False)
        self.gtk.pack_start(self.aggregate_output_obj.gtk,
                            expand=False, fill=False)
        self.output_obj = self.scalar_output_obj
        self.aggregate_output_obj.gtk.hide()
        self.typewidget = scope.findWidget(
            lambda x: (isinstance(x, parameterwidgets.EnumWidget)
                       and x.enumclass is output.OutputType))
        assert self.typewidget is not None
        self.setType("Scalar")
        self.sbcallback = switchboard.requestCallbackMain(
            self.typewidget, self.typeWidgetCB)
        self.set_value(value)
    def show(self):
        debug.mainthreadTest()
        self.gtk.show()
        self.output_obj.show()
    def isValid(self):
        return self.output_obj.isValid()
    def cleanUp(self):
        switchboard.removeCallback(self.sbcallback)
        parameterwidgets.ParameterWidget.cleanUp(self)
    def typeWidgetCB(self, interactive):
        debug.mainthreadTest()
        self.setType(self.typewidget.get_value())
    def setType(self, outtype):
        debug.mainthreadTest()
        self.output_obj.gtk.hide()
        if outtype == "Scalar":
            self.output_obj = self.scalar_output_obj
        else:                   # outtype == "Aggregate"
            self.output_obj = self.aggregate_output_obj
        self.output_obj.show()
        self.widgetChanged(self.isValid(), interactive=False)
    def get_value(self):
        return self.output_obj.get_value()
    def set_value(self, val):
        if val is not None:
            if val.isScalarOutput():
                self.setType('Scalar')
            else:
                self.setType('Aggregate')
            self.output_obj.set_value(val)
        self.widgetChanged(self.isValid(), interactive=False)

def _ValueOutputParameter_makeWidget(self, scope=None):
    return ValueOutputWidget(self.value, scope=scope, name=self.name)

output.ValueOutputParameter.makeWidget = _ValueOutputParameter_makeWidget
