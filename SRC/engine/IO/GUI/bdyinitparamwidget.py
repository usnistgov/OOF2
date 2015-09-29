# -*- python -*-
# $RCSfile: bdyinitparamwidget.py,v $
# $Revision: 1.1 $
# $Author: langer $
# $Date: 2011/06/08 14:44:39 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import bdycondition
from ooflib.engine import mesh
from ooflib.engine.IO import boundaryconditionmenu

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class BCNameWidget(parameterwidgets.StringWidget):
    pass

def _bcNameParameter_makeWidget(self, scope=None):
    return BCNameWidget(self, scope=scope, name=self.name)

boundaryconditionmenu.BCNameParameter.makeWidget = _bcNameParameter_makeWidget

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class FloatBCInitWidget(regclassfactory.RegisteredClassFactory):
    def __init__(self, obj=None, title=None, callback=None,
                 fill=0, expand=0, scope=None, name=None,
                 *args, **kwargs):
        meshwidget = scope.findWidget(
            lambda x: isinstance(x, whowidget.WhoWidget)
            and x.whoclass is mesh.meshes)
        meshctxt = mesh.meshes[meshwidget.get_value()]
        bcwidget = scope.findWidget(
            lambda x: isinstance(x, BCNameWidget))
        bc = meshctxt.getBdyCondition(bcwidget.get_value())
        self.time_derivs = (bc.field.time_derivative()
                            in meshctxt.all_initializable_fields())
        debug.fmsg("time_derivs=", self.time_derivs)
        regclassfactory.RegisteredClassFactory.__init__(
            self, bdycondition.FloatBCInitMethod.registry, obj=obj,
            title=title, callback=callback, fill=fill, expand=expand,
            scope=scope, name=name, *args, **kwargs)
    def includeRegistration(self, reg):
        return self.time_derivs == reg.time_derivative

def _floatBCInitParam_makeWidget(self, scope=None):
    return FloatBCInitWidget(self, scope=scope, name=self.name)

bdycondition.FloatBCInitParameter.makeWidget = _floatBCInitParam_makeWidget

