# -*- python -*-
# $RCSfile: invariantwidget.py,v $
# $Revision: 1.12 $
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
from ooflib.SWIG.engine import invariant
from ooflib.common import debug
from ooflib.common.IO.GUI import regclassfactory
from ooflib.engine.IO.GUI import meshparamwidgets

class InvariantParameterWidget(regclassfactory.RegisteredClassFactory):
    def __init__(self, value, scope, name):
        self.invariandwidget = scope.findWidget(
            lambda w: isinstance(w, meshparamwidgets.InvariandWidget))
        self.findInvariand()
        regclassfactory.RegisteredClassFactory.__init__(
            self, invariant.InvariantPtr.registry, scope=scope, name=name)
        if value is not None:
            self.set(value, interactive=0)
        self.sbcallback = switchboard.requestCallbackMain(
            self.invariandwidget, self.invWidgetChanged)
    def findInvariand(self):
        invariand = self.invariandwidget.get_value()
        if invariand is not None:
            self.invariandclass = \
                                invariand.newOutputValue().valuePtr().__class__
        else:
            self.invariandclass = None
    # This function can get an "interactive" argument -- discard it.
    def invWidgetChanged(self, *args):
        self.findInvariand()
        self.update(self.registry)
    def cleanUp(self):
        switchboard.removeCallback(self.sbcallback)
        regclassfactory.RegisteredClassFactory.cleanUp(self)
    def includeRegistration(self, registration):
        return invariant.okInvariant(registration, self.invariandclass)

def _InvariantParameter_makeWidget(self, scope):
    return InvariantParameterWidget(self.value, scope=scope, name=self.name)

invariant.InvariantParameter.makeWidget = _InvariantParameter_makeWidget
