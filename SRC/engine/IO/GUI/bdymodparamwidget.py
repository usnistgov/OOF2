# -*- python -*-
# $RCSfile: bdymodparamwidget.py,v $
# $Revision: 1.11 $
# $Author: langer $
# $Date: 2014/09/27 21:41:00 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Special widget for boundary modifier parameters -- has some
# intelligence to know whether its result should be a
# PointBoundaryModifier or an EdgeBoundaryModifier.

from ooflib.common.IO.GUI import regclassfactory
from ooflib.engine import boundarymodifier



class BoundaryModParamWidget(regclassfactory.RegisteredClassFactory):
    def __init__(self, registry, obj=None, title=None,
                 callback=None, fill=0, expand=0, scope=None, name=None,
                 *args, **kwargs):
        # scope.parent is the ParameterDialog box in which we live.
        self.modifiertype = scope.parent.modifiertype
        regclassfactory.RegisteredClassFactory.__init__(
            self, registry, obj=obj, title=title, callback=callback,
            fill=fill, expand=expand, scope=scope, name=name,
            *args, **kwargs)


    def includeRegistration(self, registration):
        return registration.modifiertype == self.modifiertype


def _makeBMPWidget(self, scope):
    return BoundaryModParamWidget(self.registry,
                                  obj=self.value, scope=scope, name=self.name)

boundarymodifier.BoundaryModifierParameter.makeWidget = _makeBMPWidget
