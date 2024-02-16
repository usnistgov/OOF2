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
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import errorestimator
from ooflib.engine import skeletoncontext
from ooflib.engine import subproblemcontext
from ooflib.engine.IO.GUI import meshparamwidgets
import ooflib.engine.mesh

skeletonContexts = skeletoncontext.skeletonContexts

class AMRWhoParameterWidget(whowidget.WhoParameterWidget):
    def __init__(self, whoclass, value=None, scope=None, name=None, **kwargs):
        self.skelwidget = scope.findWidget(
            lambda x: isinstance(x, whowidget.WhoWidget)
            and x.whoclass is skeletonContexts)
        whowidget.WhoParameterWidgetBase.__init__(self, whoclass,
                                                  value=value, scope=scope,
                                                  name=name, **kwargs)

        # switchboard callbacks
        self.sbcallbacks = [
            switchboard.requestCallbackMain(self.skelwidget,
                                            self.skelwidgetChanged),
            switchboard.requestCallbackMain(('who changed', 'Skeleton'),
                                            self.skelModified),
            switchboard.requestCallbackMain('mesh status changed',
                                            self.meshStatusChanged)]
        
    def widgetCB(self, interactive):
        # Gives an "OK" sign only when the current skeleton object is
        # the base skeleton of the to-be-refined mesh.
        try:
            # Supplying skelwidget.get_value seems enough. If the
            # whoclass is a subproblem, the mesh and subproblem names
            # also get filled in the choosers.
            self.set_value(self.skelwidget.get_value())
            # If the following throws an exception, the skeleton
            # cannot be modified. Even if it does not throw an
            # exception, there may still be insufficient information
            # to do AMR.
            subproblem = subproblemcontext.subproblems[self.get_value()]
            # Already sure that the current skeleton object is the
            # base skeleton of the to-be-refined mesh.  
            meshctxt = subproblem.getParent()
            self.widgetChanged(not meshctxt.outOfSync(), interactive)
        except KeyError:
            self.widgetChanged(0, interactive)

    # Callback for "skelwidget" change in Skeleton Page.
    def skelwidgetChanged(self, *args, **kwargs):
        self.widgetCB(False)

    # Callback for skeleton modification (modify, undo, redo).
    def skelModified(self, *args, **kwargs):
        self.widgetCB(False)

    def meshStatusChanged(self, meshctxt):
        self.widgetCB(False)

    def cleanUp(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        whowidget.WhoParameterWidgetBase.cleanUp(self)
                        
def _AMRWhoParameter_makeWidget(self, scope=None, **kwargs):
    return AMRWhoParameterWidget(self.whoclass, self.value, scope=scope,
                                 **kwargs)

errorestimator.AMRWhoParameter.makeWidget = _AMRWhoParameter_makeWidget

#########################################

class ZZFluxParameterWidget(meshparamwidgets.SubProblemFluxParameterWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        meshparamwidgets.SubProblemFluxParameterWidget.__init__(self, param,
                                                                scope, name,
                                                                **kwargs)

        self.meshChangedCB()
        self.sbcallbacks += [switchboard.requestCallbackMain(
            ('new who', 'Mesh'), self.meshChangedCB)]

    def meshChangedCB(self, *args):
        mesh = self.getSource()           # really SubProblem
        if mesh:
            self.widgetChanged(mesh.has_solution(), interactive=1)
        
def _ZZFluxParameter_makeWidget(param, scope, **kwargs):
    return ZZFluxParameterWidget(param, scope=scope, name=param.name, **kwargs)

errorestimator.ZZFluxParameter.makeWidget = _ZZFluxParameter_makeWidget
