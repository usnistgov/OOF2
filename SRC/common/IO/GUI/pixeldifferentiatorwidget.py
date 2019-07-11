# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import burn
from ooflib.SWIG.common import switchboard
from ooflib.common.IO import pixelgroupmenu
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory

# A widget for choosing PixelDifferentiators.  Different ones are
# displayed depending on the current Contiguity.  For example, if
# choosing discontiguous pixels, the differentiator doesn't need to
# consider neighboring pixels, but if doing something like a Burn
# algorithm, it needs to consider both local and global differences.

class PixelDifferentiatorWidget(regclassfactory.RegisteredClassFactory):
    def __init__(self, value, scope, name):
        self.contiguity = None  # current value of contiguityWidget
        self.contiguityWidget = scope.findWidget(
            lambda w: isinstance(w, parameterwidgets.EnumWidget) and
            w.enumclass is pixelgroupmenu.Contiguity)
        assert self.contiguityWidget is not None
        self.contiguity = self.contiguityWidget.get_value()
        self.sbcb = switchboard.requestCallbackMain(
            self.contiguityWidget, self.contiguityWidgetChanged)

        regclassfactory.RegisteredClassFactory.__init__(
            self, burn.PixelDifferentiator.registry, scope=scope, name=name)

    def cleanUp(self):
        switchboard.removeCallback(self.sbcb)
        regclassfactory.RegisteredClassFactory.cleanUp(self)

    def contiguityWidgetChanged(self, *args):
        self.contiguity = self.contiguityWidget.get_value()
        self.refresh()

    def includeRegistration(self, registration):
        return self.contiguity in registration.contiguities
    
def _makeWidget(self, scope):
    return PixelDifferentiatorWidget(self.value, scope=scope, name=self.name)

burn.PixelDifferentiatorParameter.makeWidget = _makeWidget

