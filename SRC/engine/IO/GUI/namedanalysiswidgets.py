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
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.engine import namedanalysis

class AllAnalyses:
    def getNames(self):
        return (namedanalysis.bulkAnalysisNames() + 
                namedanalysis.bdyAnalysisNames())
    def signals(self):
        return [
            switchboard.requestCallbackMain("named analyses changed",
                                            self.update),
            switchboard.requestCallbackMain("named boundary analyses changed",
                                            self.update)
            ]

class BulkAnalyses:
    def getNames(self):
        return namedanalysis.bulkAnalysisNames()
    def signals(self):
        return [
            switchboard.requestCallbackMain("named analyses changed",
                                            self.update)
            ]

class BdyAnalyses:
    def getNames(self):
        return namedanalysis.bdyAnalysisNames()
    def signals(self):
        return [
            switchboard.requestCallbackMain("named boundary analyses changed",
                                            self.update)
            ]


class AnalysisNamesWidgetBase(parameterwidgets.ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        names = sorted(self.getNames())
        self.widget = chooser.ScrolledMultiListWidget(names,
                                                      callback=self.widgetCB,
                                                      **kwargs)
        parameterwidgets.ParameterWidget.__init__(self, self.widget.gtk,
                                                  scope, name=name,
                                                  expandable=True)
        self.widget.set_selection(param.value)
        self.widgetChanged(param.value is not None, interactive=False)
        self.sbcallbacks = self.signals()
        self.widgetChanged(len(self.get_value()) > 0, interactive=False)
    def cleanUp(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        parameterwidgets.ParameterWidget.cleanUp(self)
    def get_value(self):
        return self.widget.get_value()
    def set_value(self, value):
        self.widget.set_selection(value)
    def widgetCB(self, list, interactive):
        self.widgetChanged(len(list) > 0, interactive=True)
    def update(self, *args):
        names = sorted(self.getNames())
        self.widget.update(names)
        self.widgetChanged(len(self.get_value()) > 0, interactive=False)


class AnalysisNamesWidget(AnalysisNamesWidgetBase, AllAnalyses):
    pass

def _AnalysisNamesParam_makeWidget(self, scope=None, **kwargs):
    return AnalysisNamesWidget(self, scope, name=self.name, **kwargs)

namedanalysis.AnalysisNamesParameter.makeWidget = _AnalysisNamesParam_makeWidget


class BulkAnalysisNamesWidget(AnalysisNamesWidgetBase, BulkAnalyses):
    pass

def _BulkAnalysisNamesParam_makeWidget(self, scope=None, **kwargs):
    return BulkAnalysisNamesWidget(self, scope, name=self.name, **kwargs)

namedanalysis.BulkAnalysisNamesParameter.makeWidget = \
    _BulkAnalysisNamesParam_makeWidget


class BdyAnalysisNamesWidget(AnalysisNamesWidgetBase, BdyAnalyses):
    pass

def _BdyAnalysisNamesParam_makeWidget(self, scope=None, **kwargs):
    return BdyAnalysisNamesWidget(self, scope, name=self.name, **kwargs)

namedanalysis.BdyAnalysisNamesParameter.makeWidget = \
    _BdyAnalysisNamesParam_makeWidget

################

class AnalysisNameWidgetBase(parameterwidgets.ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        self.chooser = chooser.ChooserWidget([], name=name, **kwargs)
        parameterwidgets.ParameterWidget.__init__(self, self.chooser.gtk, scope)
        self.update()
        if param.value is not None:
            self.set_value(param.value)
        self.sbcallbacks = [
            switchboard.requestCallbackMain("named analyses changed",
                                            self.update)
            ]
    def cleanUp(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        parameterwidgets.ParameterWidget.cleanUp(self)
    def set_value(self, name):
        self.chooser.set_state(name)
        self.widgetChanged(name is not None, interactive=False)
    def get_value(self):
        return self.chooser.get_value()
    def update(self, *args):
        names = sorted(self.getNames())
        self.chooser.update(names)
        self.widgetChanged(len(names) > 0, interactive=False)


class AnalysisNameWidget(AnalysisNameWidgetBase, AllAnalyses):
    pass

def _AnalysisNameParam_makeWidget(self, scope=None, **kwargs):
    return AnalysisNameWidget(self, scope, name=self.name, **kwargs)

namedanalysis.AnalysisNameParameter.makeWidget = _AnalysisNameParam_makeWidget


class BulkAnalysisNameWidget(AnalysisNameWidgetBase, BulkAnalyses):
    pass

def _BulkAnalysisNameParam_makeWidget(self, scope=None, **kwargs):
    return BulkAnalysisNameWidget(self, scope, name=self.name, **kwargs)

namedanalysis.BulkAnalysisNameParameter.makeWidget = \
    _BulkAnalysisNameParam_makeWidget


class BdyAnalysisNameWidget(AnalysisNameWidgetBase, BdyAnalyses):
    pass

def _BdyAnalysisNameParam_makeWidget(self, scope=None, **kwargs):
    return BdyAnalysisNameWidget(self, scope, name=self.name, **kwargs)

namedanalysis.BdyAnalysisNameParameter.makeWidget = \
    _BdyAnalysisNameParam_makeWidget
