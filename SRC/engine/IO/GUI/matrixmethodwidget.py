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
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import matrixmethod
from ooflib.engine import preconditioner
from ooflib.engine import subproblemcontext
from ooflib.engine import symstate
from ooflib.engine import timestepper


class AsymmetricMatrixMethodFactory(regclassfactory.RegisteredClassFactory):
    def includeRegistration(self, reg):
        return not reg.symmetricOnly and not reg.no_gui

def _makeAsymMtxMethodWidget(self, scope=None, **kwargs):
    return AsymmetricMatrixMethodFactory(self.registry, obj=self.value,
                                         scope=scope, name=self.name,
                                         **kwargs)

matrixmethod.AsymmetricMatrixMethodParam.makeWidget = _makeAsymMtxMethodWidget

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class PreconditionerWidget(regclassfactory.RegisteredClassFactory):
    def __init__(self, value, scope, name, **kwargs):
        matrixmethodwidget = scope.findWidget(
            lambda w: (isinstance(w, regclassfactory.RegisteredClassFactory)
                       and w.registry is matrixmethod.MatrixMethod.registry))
        self.matrixmethod = matrixmethodwidget.getRegistration().subclass
        regclassfactory.RegisteredClassFactory.__init__(
            self, preconditioner.Preconditioner.registry, scope=scope,
            name=name, **kwargs)

    def includeRegistration(self, reg):
        # A preconditioner should be listed if it's in the solver_map
        # for the currently selected matrix method.
        return (not reg.no_gui and
                reg.subclass in self.matrixmethod.solver_map)

def _makePreconditionerWidget(self, scope=None, **kwargs):
    return PreconditionerWidget(self.registry, obj=self.value,
                                scope=scope, name=self.name,
                                **kwargs)

preconditioner.PreconditionerParameter.makeWidget = _makePreconditionerWidget

