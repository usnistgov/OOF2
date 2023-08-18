# -*- python -*-

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

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Widgets for Parameters whose value is an Output (not the value of an
# Output, but the Output object itself).

class OutputParameterWidget(parameterwidgets.ParameterWidget,
                            widgetscope.WidgetScope):
    def __init__(self, value, outputtree, scope=None, name=None, **kwargs):
        debug.mainthreadTest()
        frame = Gtk.Frame(**kwargs)
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                            margin=2)
        frame.add(self.vbox)
        # top part is a bunch of chooser widgets representing the
        # LabelTree of outputs.
        self.treewidget = \
                     gfxLabelTree.LabelTreeChooserWidget(outputtree,
                                                         callback=self.treeCB,
                                                         name=name)
        self.vbox.pack_start(self.treewidget.gtk,
                             expand=False, fill=False, padding=0)
        # bottom part is a ParameterTable
        self.parambox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        gtklogger.setWidgetName(self.parambox, "Parameters")
        self.paramtable = None
        self.params = []
        self.paramhier = []
        self.vbox.pack_start(self.parambox, expand=False, fill=False, padding=0)
        
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
            self.makeParameterTable(value, interactive=False)
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
            self.parambox.pack_start(self.paramtable.gtk,
                                     expand=False, fill=False, padding=0)
            self.widgetChanged(self.paramtable.isValid(), interactive)
            self.paramtable.show()
            self.sbcallback = switchboard.requestCallbackMain(
                self.paramtable, self.tableChangedCB)
        else:
            self.paramtable = None
            self.widgetChanged(True, interactive)
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
    def get_proto(self):
        return self.treewidget.get_value()

    def destroyParameterTable(self):
        debug.mainthreadTest()
        if self.paramtable is not None:
            table = self.paramtable
            self.paramtable = None
            table.destroy()
            switchboard.removeCallback(self.sbcallback)
    def treeCB(self):
        self.makeParameterTable(self.treewidget.get_value(), interactive=True)
    def tableChangedCB(self, arg):      # switchboard callback
        self.widgetChanged(self.paramtable.isValid(), interactive=True)

######################
        
class ScalarOutputParameterWidget(OutputParameterWidget):
    def __init__(self, value, scope=None, name=None, **kwargs):
        OutputParameterWidget.__init__(self, value, output.scalarOutputs,
                                       scope=scope, name=name, **kwargs)

def _ScalarOutputParameter_makeWidget(self, scope=None, **kwargs):
    return ScalarOutputParameterWidget(
        self.value, scope=scope, name=self.name, **kwargs)

output.ScalarOutputParameter.makeWidget = _ScalarOutputParameter_makeWidget



class PositionOutputParameterWidget(OutputParameterWidget):
    def __init__(self, value, scope=None, name=None, **kwargs):
        OutputParameterWidget.__init__(self, value, output.positionOutputs,
                                       scope=scope, name=name, **kwargs)

def _PositionOutputParameter_makeWidget(self, scope=None, **kwargs):
    return PositionOutputParameterWidget(self.value, scope=scope,
                                         name=self.name, **kwargs)

output.PositionOutputParameter.makeWidget = _PositionOutputParameter_makeWidget

class AggregateOutputParameterWidget(OutputParameterWidget):
    def __init__(self, value, scope=None, name=None, **kwargs):
        OutputParameterWidget.__init__(self, value, output.aggregateOutputs,
                                       scope=scope, name=name, **kwargs)

def _AggregateOutputParameter_makeWidget(self, scope=None, **kwargs):
    return AggregateOutputParameterWidget(self.value, scope=scope,
                                          name=self.name, **kwargs)

output.AggregateOutputParameter.makeWidget = \
                                           _AggregateOutputParameter_makeWidget

#####################

# The widget for a ValueOutputParameter displays either the
# ScalarOutputs or the AggregateOutputs, depending on the setting of
# an EnumWidget for the OutputType.

class ValueOutputWidget(parameterwidgets.ParameterWidget, 
                        widgetscope.WidgetScope):
    def __init__(self, value, scope=None, name=None, **kwargs):
        debug.mainthreadTest()
        widgetscope.WidgetScope.__init__(self, scope)

        self.scalar_output_obj = ScalarOutputParameterWidget(
            None, scope=self, name="Scalar")
        self.aggregate_output_obj = AggregateOutputParameterWidget(
            None, scope=self, name="Aggregate")
        quargs = kwargs.copy()
        quargs.setdefault('spacing', 2)
        parameterwidgets.ParameterWidget.__init__(
            self,
            Gtk.Box(orientation=Gtk.Orientation.VERTICAL, **quargs),
            scope, name)
        self.stack = Gtk.Stack()
        self.gtk.pack_start(self.stack, expand=False, fill=False, padding=0)
        self.stack.add_named(self.scalar_output_obj.gtk, "Scalar")
        self.stack.add_named(self.aggregate_output_obj.gtk, "Aggregate")
        self.scalar_output_obj.show()
        self.aggregate_output_obj.show()
        self.output_obj = self.scalar_output_obj

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
        self.stack.show()
    def isValid(self):
        return self.output_obj.isValid()
    def cleanUp(self):
        switchboard.removeCallback(self.sbcallback)
        parameterwidgets.ParameterWidget.cleanUp(self)
    def typeWidgetCB(self, interactive):
        debug.mainthreadTest()
        self.setType(self.typewidget.get_value().string())
    def setType(self, outtype):
        debug.mainthreadTest()
        if outtype == "Scalar":
            self.output_obj = self.scalar_output_obj
        else:                   # outtype == "Aggregate"
            self.output_obj = self.aggregate_output_obj
        self.stack.set_visible_child_name(outtype)
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

def _ValueOutputParameter_makeWidget(self, scope=None, **kwargs):
    return ValueOutputWidget(self.value, scope=scope, name=self.name, **kwargs)

output.ValueOutputParameter.makeWidget = _ValueOutputParameter_makeWidget
