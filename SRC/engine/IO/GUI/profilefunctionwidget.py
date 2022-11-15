# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.engine import profile
from ooflib.engine import profilefunction
from ooflib.engine.IO.GUI import meshparamwidgets

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ProfileFunctionXWidget(parameterwidgets.XYStrFunctionWidget):
    def get_value(self):
        debug.mainthreadTest()
        return profilefunction.ProfileFunctionX(self.gtk.get_text().lstrip())
    def validValue(self, value):
        if isinstance(value, (str, bytes)):
            try:
                fn = profilefunction.ProfileFunctionX(value)
                return True
            except:
                return False
        return isinstance(value, profilefunction.ProfileFunctionX)

def PFPX_makeWidget(self, scope=None, **kwargs):
    return ProfileFunctionXWidget(self, scope, name=self.name, **kwargs)

profilefunction.ProfileFunctionXParameter.makeWidget = PFPX_makeWidget

class ProfileFunctionXTWidget(parameterwidgets.XYTStrFunctionWidget):
    def get_value(self):
        debug.mainthreadTest()
        return profilefunction.ProfileFunctionXT(self.gtk.get_text().lstrip())
    def validValue(self, value):
        if isinstance(value, (str, bytes)):
            try:
                fn = profilefunction.ProfileFunctionXT(value)
                return True
            except:
                return False
        return isinstance(value, profilefunction.ProfileFunctionXT)

def PFPXT_makeWidget(self, scope=None, **kwargs):
    return ProfileFunctionXTWidget(self, scope, name=self.name, **kwargs)

profilefunction.ProfileFunctionXTParameter.makeWidget = PFPXT_makeWidget
    

# Local utility class -- keeps track of a Gtk.Box, and the contained
# Gtk.Label and Registered Class Factory.  Allows the label to be
# dynamically reset.  Exposes a small part of the enclosed Registered
# Class Factory interface.
class LabelledProfileRCF:
    def __init__(self, fpsw, scope=None, label=""):
        debug.mainthreadTest()
        self.fpsw = fpsw                # parent FluxProfileSetWidget
        self.gtk = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.label = Gtk.Label(label=label+" = ")
        self.widget = regclassfactory.RegisteredClassFactory(
            profile.ProfileXT.registry, scope=scope, name=label)
        self.sbcb = switchboard.requestCallbackMain(self.widget, self.rcfCB)
        self.gtk.pack_start(self.label, expand=False, fill=False, padding=0)
        self.gtk.pack_start(self.widget.gtk, expand=True, fill=True, padding=0)
        self.show()
    def rcfCB(self, interactive):
        self.fpsw.rcfChanged(interactive)
    def show(self):
        debug.mainthreadTest()
        self.label.show()
        self.widget.show()
        self.gtk.show()
    def set_label(self, label):
        debug.mainthreadTest()
        self.label.set_text(label)
        self.show()
    def get_value(self):
        return self.widget.get_value()
    def set(self, value, interactive):
        self.widget.set(value, interactive)
    def cleanUp(self):
        switchboard.removeCallback(self.sbcb)
        
    
# Widget for FluxProfileSet objects -- this widget goes with the
# FluxProfileSetParameter, and consequently only comes up in contexts
# where a flux can be retrieved -- it is a container for that number
# of profile widgets.
class FluxProfileSetWidget(parameterwidgets.ParameterWidget):
    def __init__(self, param, scope=None, name=None, **kwargs):
        if scope is None:
            raise ooferror.PyErrPyProgrammingError(
                "FluxProfileSetWidget instanced with no scope.")
        self.scope=scope
        self.fluxwidget = scope.findWidget(
            lambda x: x.__class__==meshparamwidgets.FluxParameterWidget)
        self.sbcb = switchboard.requestCallbackMain(self.fluxwidget,
                                                    self.checkFlux)
        quargs = kwargs.copy()
        quargs.setdefault('spacing', 2)
        gtk_obj = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, **quargs)
        parameterwidgets.ParameterWidget.__init__(self, gtk_obj, scope, name)
        self.profileset = [] # Profiles themselves.
        self.widgetset = []  # LabelledProfileRCF objects
        self.set_value(param.value)
        # TODO LATER: The real right way to handle validity is to behave
        # as a proper container, and catch the validity changes of the
        # enclosed RCFs.  However, we happen to know that we are always
        # valid, so we do it the simple way.
        self.widgetChanged(1, interactive=0)

    # Changes the length of the list of profile sets, padding with
    # ConstantProfile(0.0) as required to get the length.
    def checkFlux(self, interactive):
        flux = self.fluxwidget.get_value()
        self.nslots = flux.divergence_dim()
        if len(self.profileset) > self.nslots:
            self.profileset = self.profileset[:self.nslots]
        elif len(self.profileset) < self.nslots:
            self.profileset += [profile.ConstantProfile(0.0)]*\
                               (self.nslots-len(self.profileset))
        self.show()
        self.widgetChanged(True, interactive)
            
    # Parses the funcstr.
    def set_value(self, newvalue):
        if newvalue:
            self.profileset = newvalue.get_profiles()
        self.checkFlux(interactive=False)

    def get_value(self):
        return profile.FluxProfileSet([w.get_value() for w in self.widgetset])
            

    # Draw the right number of slots with the right widgets in them.
    # The widgets are LabelledProfileRCF objects, see above.
    def show(self):
        if len(self.widgetset) > self.nslots:
            for w in self.widgetset[self.nslots:]:
                self.gtk.remove(w.gtk)
                w.cleanUp()
            self.widgetset = self.widgetset[:self.nslots]
        elif len(self.widgetset) < self.nslots:
            for i in range(len(self.widgetset), self.nslots):
                new_widget = LabelledProfileRCF(self, scope=self.scope,
                                                label="p%d" % i)
                # new_widget = regclassfactory.RegisteredClassFactory(
                #     profile.Profile.registry, scope=self.scope)
                self.widgetset.append(new_widget)
                self.gtk.pack_start(new_widget.gtk,
                                    expand=False, fill=False, padding=0)
        # Widget list and profile set are now the same length. 
        for i in range(len(self.widgetset)):
            self.widgetset[i].set(self.profileset[i], 0)
            self.widgetset[i].show()
        self.gtk.show()

    def rcfChanged(self, interactive):  # called by LabelledProfileRCFs.
        self.widgetChanged(True, interactive)

    def cleanUp(self):
        switchboard.removeCallback(self.sbcb)
        for widget in self.widgetset:
            widget.cleanUp()
        parameterwidgets.ParameterWidget.cleanUp(self)

def FPSP_makeWidget(self, scope, **kwargs):
    return FluxProfileSetWidget(self, scope, name=self.name, **kwargs)

profile.FluxProfileSetParameter.makeWidget = FPSP_makeWidget
