OBSOLETE

# -*- python -*-
# $RCSfile: timestepperwidget.py,v $
# $Revision: 1.8 $
# $Author: langer $
# $Date: 2014/09/27 21:41:02 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Custom widget for the TimeStepperParameter, that checks the
# NonlinearSolverBase object, and only lists the appropriate TimeSteppers.

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import ooferror2
from ooflib.common import debug
from ooflib.common.IO.GUI import regclassfactory
from ooflib.engine import timestepper
from ooflib.engine import nonlinearsolver

OBSOLETE

class TimeStepperParamWidget(regclassfactory.RegisteredClassFactory):

    def __init__(self, registry, obj=None, scope=None, name=None):
        self.nonlinSolverWidget = scope.findWidget(
            lambda w: (isinstance(w, regclassfactory.RegisteredClassFactory)
                       and w.registry is nonlinearsolver.NonlinearSolverBase.registry))
        regclassfactory.RegisteredClassFactory.__init__(
            self, registry, obj=obj, scope=scope, name=name)
        self.sbcb = switchboard.requestCallbackMain(self.nonlinSolverWidget,
                                                    self.linchanged)

    def linchanged(self, interactive):
        self.update(self.registry)

    def cleanUp(self):
        switchboard.removeCallback(self.sbcb)
        regclassfactory.RegisteredClassFactory.cleanUp(self)

    def includeRegistration(self, registration):
        if(self.nonlinSolverWidget.isValid()):
            nonlinear_solver_registration = self.nonlinSolverWidget.getRegistration()
            if nonlinear_solver_registration is nonlinearsolver.NonlinearSolver:
                return issubclass(registration.subclass,
                                  timestepper.NonLinearStepper)
            else:
                return issubclass(registration.subclass,
                                  timestepper.LinearStepper)

def _makeTSWidget(self, scope):
    return TimeStepperParamWidget(self.registry, self.value, scope=scope,
                                  name=self.name)


#timestepper.TimeStepperParameter.makeWidget = _makeTSWidget
