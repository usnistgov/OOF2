# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# ParameterWidgets for things that depend on a Mesh, such as Fields,
# Fluxes, and Equations defined on the Mesh.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import equation
from ooflib.SWIG.engine import field
from ooflib.SWIG.engine import flux
from ooflib.SWIG.engine import planarity
from ooflib.common import debug
from ooflib.common.IO import placeholder
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import mesh
from ooflib.engine import skeletoncontext
from ooflib.engine import subproblemcontext
from ooflib.engine.IO import meshparameters

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

## Blocks of code preceded by "if TESTINGPAPER:" are an attempt to
## reproduce the bug that motivated gui test 00176.
TESTINGPAPER = False

class MeshParamWidgetBase(parameterwidgets.ParameterWidget):
    # Base class for a widget that displays and allows choices from a
    # list of things from a Mesh (eg, defined Fields or active
    # Equations).  The meshfunc constructor argument is a function
    # that returns the list of things to display.  It's called with
    # the mesh as its first argument, so it can be a Mesh member
    # function.  self.chooser is the ChooserWidget that displays the
    # items returned by meshfunc.

    def __init__(self, param, whoclass, meshfunc, scope, name=None,
                 separator_func=None, **kwargs):
        self.meshfunc = meshfunc
        self.whoclass = whoclass
        self.chooser = chooser.ChooserWidget([], callback=self.chooserCB,
                                             name=name,
                                             separator_func=separator_func,
                                             **kwargs)
        parameterwidgets.ParameterWidget.__init__(self, self.chooser.gtk, scope)
        self.meshwidget = scope.findWidget(
            lambda w: isinstance(w, whowidget.WhoWidget)
            and w.whoclass is whoclass)
        assert self.meshwidget is not None
        if self.meshwidget is None:
            raise ooferror.PyErrPyProgrammingError("Can't find WhoWidget for %s"
                                                   % repr(whoclass))
        self.sbcallbacks = [
            switchboard.requestCallbackMain(self.meshwidget, self.update),
            switchboard.requestCallbackMain("mesh changed", self.meshChangeCB),
            switchboard.requestCallbackMain("subproblem changed",
                                            self.meshChangeCB)
            ]

        self.update(interactive=0)
        
        if TESTINGPAPER:
            if param.value is not None:
                self.set_value(param.value)
        else:
            self.set_value(param.value)
        
    def update(self, interactive):
        msh = self.getSource()
        self.vals = {None:None}
        if msh is not None:
            namelist = []
            for obj in self.meshfunc(msh):
                self.vals[obj.name()] = obj
                namelist.append(obj.name())
            self.chooser.update(namelist)
            self.widgetChanged(len(namelist) > 0, interactive)
        else:
            self.chooser.update([])
            self.widgetChanged(0, interactive)
    def chooserCB(self, *args):
        self.widgetChanged(1, interactive=1)
    def meshChangeCB(self, meshcontext):
        if self.meshwidget:             # we haven't been cleaned up
            src = self.getSource()
            # 'meshcontext' might be a subproblem, actually.
            if meshcontext is src or meshcontext.getParent() is src:
                self.update(interactive=0)
    def getSource(self):
        if self.meshwidget is not None:
            meshname = self.meshwidget.get_value()
            try:
                return self.whoclass[meshname]
            except KeyError:
                pass
    def get_value(self):
        return self.vals.get(self.chooser.get_value(), None)
    def set_value(self, obj):
        if TESTINGPAPER:
            if obj is not None and obj.name() in self.chooser.choices():
                self.chooser.set_state(obj.name())
                self.widgetChanged(1, interactive=0)
        else:
            if obj is not None and obj.name() in self.chooser.choices():
                self.chooser.set_state(obj.name())
                self.widgetChanged(1, interactive=0)
        
    def cleanUp(self):
        debug.mainthreadTest()
        self.meshwidget = None
        switchboard.removeCallbacks(self.sbcallbacks)
        parameterwidgets.ParameterWidget.cleanUp(self)

class MeshParamWidget(MeshParamWidgetBase):
    def __init__(self, param, meshfunc, scope, name=None, separator_func=None,
                 **kwargs):
        MeshParamWidgetBase.__init__(self, param,
                                     mesh.meshes,
                                     meshfunc, scope, name, separator_func,
                                     **kwargs)

class SubProblemParamWidget(MeshParamWidgetBase):
    def __init__(self, param, meshfunc, scope, name=None, separator_func=None,
                 **kwargs):
        MeshParamWidgetBase.__init__(self, param,
                                     subproblemcontext.subproblems,
                                     meshfunc, scope, name, separator_func,
                                     **kwargs)
    

# Widgets for quantities to which Invariants can be calculated should
# be subclasses of InvariandWidget.

class InvariandWidget: pass

# Widgets for quantities for which components can be extracted should
# be subclasses of IndexableWidget.

class IndexableWidget: pass

#############################

def meshfieldlister(meshctxt):          # meshfunc for FieldParameterWidgets
    # list fields and out-of-plane fields, if defined.
    try:
        compoundfields = meshctxt.all_compound_subproblem_fields()
        flds = []
        for fld in compoundfields:
            flds.append(fld)
            if config.dimension() == 2:
                if not meshctxt.getObject().in_plane(fld): 
                    flds.append(fld.out_of_plane())
        return flds
    except:
        # This might be called with an unresolvable proxy if there
        # are no meshes.
        return []


class FieldParameterWidget(MeshParamWidget, InvariandWidget, IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        if param.outofplane:
            flist = meshfieldlister
        else:
            flist = mesh.Mesh.all_compound_subproblem_fields
        MeshParamWidget.__init__(self, param, flist, scope, name, **kwargs)
##        self.sbcallbacks.append(
##            switchboard.requestCallbackMain("field defined", self.fieldDefCB))
    def fieldDefCB(self, *args):
        self.update(interactive=False)

def _makeFieldWidget(param, scope, **kwargs):
    return FieldParameterWidget(param, scope, name=param.name, **kwargs)

meshparameters.FieldParameter.makeWidget = _makeFieldWidget

def subpfieldlister(subp):     # meshfunc for SubProblemFieldParameterWidgets
    # list fields and out-of-plane fields, if defined.
    try:
        compoundfields = subp.all_compound_fields()
        flds = []
        for fld in compoundfields:
            flds.append(fld)
            if not subp.getParent().getObject().in_plane(fld):
                flds.append(fld.out_of_plane())
        return flds
    except:
        # This might be called with an unresolvable proxy if there
        # are no meshes.
        return []
        
class SubProblemFieldParameterWidget(SubProblemParamWidget, InvariandWidget,
                                     IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        if param.outofplane:
            flist = subpfieldlister
        else:
            flist = subproblemcontext.SubProblemContext.all_compound_fields
        SubProblemParamWidget.__init__(self, param, flist, scope, name,
                                       **kwargs)

def _makeSubPFieldWidget(param, scope, **kwargs):
    return FieldParameterWidget(param, scope, name=param.name, **kwargs)

meshparameters.SubProblemFieldParameter.makeWidget = _makeSubPFieldWidget

#############################

class FluxParameterWidget(MeshParamWidget, InvariandWidget, IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param,
                                 mesh.Mesh.all_subproblem_fluxes,
                                 scope, name=name, **kwargs)
            
def _makeFluxWidget(param, scope, **kwargs):
    return FluxParameterWidget(param, scope, name=param.name, **kwargs)

meshparameters.FluxParameter.makeWidget = _makeFluxWidget

class SubProblemFluxParameterWidget(SubProblemParamWidget, InvariandWidget,
                                    IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        SubProblemParamWidget.__init__(
            self, param,
            subproblemcontext.SubProblemContext.all_fluxes,
            scope, name=name, **kwargs)
            
def _makeSubPFluxWidget(param, scope, **kwargs):
    return SubProblemParamWidget(param, scope, name=param.name, **kwargs)

meshparameters.SubProblemFluxParameter.makeWidget = _makeSubPFluxWidget

#############################

class EquationParameterWidget(MeshParamWidget, IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        eqfunc = mesh.Mesh.all_subproblem_equations
        MeshParamWidget.__init__(self, param, eqfunc, scope, name=name,
                                 **kwargs)

def _makeEquationWidget(param, scope, **kwargs):
    return EquationParameterWidget(param, scope, name=param.name, **kwargs)

meshparameters.EquationParameter.makeWidget = _makeEquationWidget

class SubProblemEquationParameterWidget(SubProblemParamWidget, IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        eqfunc = subproblemcontext.SubProblemContext.all_equations
        SubProblemParamWidget.__init__(self, param, eqfunc, scope, name=name,
                                       **kwargs)

def _makeSubPEquationWidget(param, scope, **kwargs):
    return SubProblemEquationParameterWidget(param, scope, name=param.name,
                                             **kwargs)

meshparameters.SubProblemEquationParameter.makeWidget = _makeSubPEquationWidget

class EquationBCParameterWidget(MeshParamWidget, IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        eqfunc = mesh.Mesh.all_subproblem_equations_bc
        MeshParamWidget.__init__(self, param, eqfunc, scope, name, **kwargs)

def _makeEquationBCWidget(param, scope, **kwargs):
    return EquationBCParameterWidget(param, scope, name=param.name, **kwargs)

meshparameters.EquationBCParameter.makeWidget = _makeEquationBCWidget

class SubProblemEquationBCParameterWidget(SubProblemParamWidget,
                                          IndexableWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        eqfunc = subproblemcontext.SubProblemContext.all_equations_bc
        SubProblemParamWidget.__init__(self, param, eqfunc, scope, name,
                                       **kwargs)

def _makeSubPEquationBCWidget(param, scope, **kwargs):
    return SubProblemEquationBCParameterWidget(param, scope, name=param.name,
                                               **kwargs)

meshparameters.SubProblemEquationBCParameter.makeWidget = \
                                                     _makeSubPEquationBCWidget

#############################################
#############################################

class FieldIndexParameterWidget(parameterwidgets.ParameterWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        debug.mainthreadTest()
        self.chooser = chooser.ChooserWidget([], callback=self.chooserCB,
                                             name=name,
                                             hexpand=True,
                                             halign=Gtk.Align.FILL)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                           **kwargs)
        parameterwidgets.ParameterWidget.__init__(self, self.box, scope)
        self.fieldwidget = scope.findWidget(
            lambda w: isinstance(w, IndexableWidget))
        self.sbcallback = switchboard.requestCallbackMain(self.fieldwidget,
                                                          self.fieldCB)
        self.notapplicable = Gtk.Label(label='(Not Applicable)',
                                       halign=Gtk.Align.START)
        self.nIndices = 0
        self.update()
        if TESTINGPAPER:
            if param.value is not None and param.value != '':
                self.chooser.set_state(param.value)
        else:
            if param.value in self.chooser.choices():
                self.chooser.set_state(param.value)
        self.widgetChanged(True, interactive=False)
    def chooserCB(self, *args):
        self.widgetChanged(True, interactive=True)
    def fieldCB(self, interactive):
        self.update()
        self.widgetChanged(True, interactive)
    def update(self):                   # field has changed
        complist = []
        self.nIndices = 0
        field = self.fieldwidget.get_value()
        if field is not None:
            for fcomp in field.components(planarity.ALL_INDICES):
                self.nIndices += 1
                comprepr = fcomp.shortrepr()
                complist.append(comprepr)
        self.chooser.update(complist)

        # The __init__ used to put both the chooser and the "Not
        # Applicable" label in the Box, and the show() method showed
        # or hid them as appropriate.  That doesn't work in Gtk3
        # because ParameterDialog.run() calls show_all().  There's a
        # TODO in ParameterDialog explaining why.  So now update() has
        # to explicitly add and remove the chooser and label from the
        # box, and this widget doesn't need a customized show() method.
        currentWidgets = self.box.get_children()
        if len(currentWidgets) == 1:
            currentWidget = currentWidgets[0]
            if self.nIndices > 1 and currentWidget is self.notapplicable:
                self.box.remove(self.notapplicable)
                self.box.pack_start(self.chooser.gtk,
                                    expand=False, fill=False, padding=0)
            elif self.nIndices <= 1 and currentWidget is self.chooser.gtk:
                self.box.remove(self.chooser.gtk)
                self.box.pack_start(self.notapplicable,
                                    expand=False, fill=False, padding=0)
        else:                   # no current widget
            if self.nIndices > 1:
                self.box.pack_start(self.chooser.gtk,
                                    expand=False, fill=False, padding=0)
            else:
                self.box.pack_start(self.notapplicable,
                                    expand=False, fill=False, padding=0)
        self.show()
    def get_value(self):
        val = self.chooser.get_value()
        if val is None:
            return ''
        return val
    def cleanUp(self):
        parameterwidgets.ParameterWidget.cleanUp(self)
        switchboard.removeCallback(self.sbcallback)

def _makeFieldIndexParameterWidget(param, scope, **kwargs):
    return FieldIndexParameterWidget(param, scope, name=param.name, **kwargs)

meshparameters.FieldIndexParameter.makeWidget = _makeFieldIndexParameterWidget


############################################################

# Not a widget for listing things in a SubProblem, but for listing the
# SubProblems in a Mesh.  This is only a bit of a hack, since it's
# different than the other widgets in the class.  The value of a
# SubProblemParameter is the SubProblem's path (similar to a
# WhoWidget), whereas the value of the other types of MeshParamWidget
# is a real object.

class SubProblemWidget(MeshParamWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param, mesh.Mesh.subproblems,
                                 scope, name, **kwargs)
        self.sbcallbacks.append(
            switchboard.requestCallbackMain(("new who", "SubProblem"),
                                            self.newSubProblemCB))
    def newSubProblemCB(self, subppath):
        self.update(interactive=False)
    def get_value(self):
        subp = MeshParamWidget.get_value(self)
        if subp:
            return subp.path()
    def set_value(self, path):
        try:
            MeshParamWidget.set_value(self, subproblemcontext.subproblems[path])
        except KeyError:
            pass

def _makeSubProblemWidget(param, scope, **kwargs):
    return SubProblemWidget(param, scope, name=param.name, **kwargs)

subproblemcontext.SubProblemParameter.makeWidget = _makeSubProblemWidget

############################################################

# Special widget for mesh boundary parameters.  As it turns out, these
# params take strings, not boundary objects, so we override a
# significant fraction of the foregoing machinery, which is really
# designed for parameters which take the actual object.

class MeshBoundaryParamWidget(MeshParamWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param, _getSortedBdyNames,
                                 scope, name=name, separator_func=_bdysepfunc,
                                 **kwargs)
        self.sbcallbacks.append(
            switchboard.requestCallbackMain('mesh boundaries changed',
                                            self.newBdys) )
    def newBdys(self, msh):
        if msh is self.getSource():
            self.update(interactive=0)
    def update(self, interactive):
        msh = self.getSource()
        if msh is not None:
            namelist = self.meshfunc(msh)
            self.chooser.update(namelist)
##             # remove from namelist the boundaries with visible=False
##             for name in namelist:
##                 try: # ignore the separator which will cause a key error
##                     print name, msh.getObject().boundaries[name].visible
##                     if not msh.getObject().boundaries[name].visible:
##                         namelist.remove(name)
##                 except:
##                     pass
            if namelist: # If list has nonzero length, widget is valid.
                self.widgetChanged(1, interactive)
        else:
            self.chooser.update([])
            self.widgetChanged(False, interactive)
    def set_value(self, value):
        if TESTINGPAPER:
            self.chooser.set_state(value)
            self.widgetChanged(True, interactive=0)
        else:
            if value in self.chooser.choices():
                self.chooser.set_state(value)
                self.widgetChanged(True, interactive=0)
    def get_value(self):
        return self.chooser.get_value()

def _makeBoundaryWidget(param, scope, **kwargs):
    return MeshBoundaryParamWidget(param, scope, name=param.name, **kwargs)

meshparameters.MeshBoundaryParameter.makeWidget = _makeBoundaryWidget

# The MeshBoundaryParamWidget puts _separator_proxy in the list of
# boundaries to divide the edge boundaries from the point boundaries.
# The ChooserWidget replaces it with a real separator, using
# _bdysepfunc as the predicate.

_separator_proxy = "----------"

def _getSortedBdyNames(msh):
    return msh.edgeBoundaryNames() + [_separator_proxy] + \
           msh.visiblePointBoundaryNames()

def _bdysepfunc(bdyname):
    return bdyname == _separator_proxy





# Special cases for nontrivial edge and point boundaries.


class MeshEdgeBdyParamWidget(MeshBoundaryParamWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param,
                                  mesh.Mesh.edgeBoundaryNames,
                                  scope, name=name, **kwargs)
        self.sbcallbacks.append(
            switchboard.requestCallbackMain('mesh boundaries changed',
                                            self.newBdys) )

def _makeEdgeBdyWidget(param, scope, **kwargs):
    return MeshEdgeBdyParamWidget(param, scope, name=param.name, **kwargs)

meshparameters.MeshEdgeBdyParameter.makeWidget = _makeEdgeBdyWidget



class MeshPeriodicEdgeBdyParamWidget(MeshBoundaryParamWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param,
                                  mesh.Mesh.periodicEdgeBoundaryNames,
                                  scope, name=name, **kwargs)
        self.sbcallbacks.append(
            switchboard.requestCallbackMain('mesh boundaries changed',
                                            self.newBdys) )

def _makePeriodicEdgeBdyWidget(param, scope, **kwargs):
    return MeshPeriodicEdgeBdyParamWidget(param, scope, name=param.name,
                                          **kwargs)

meshparameters.MeshPeriodicEdgeBdyParameter.makeWidget \
    = _makePeriodicEdgeBdyWidget



class MeshPointBdyParamWidget(MeshBoundaryParamWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param,
                                  mesh.Mesh.visiblePointBoundaryNames,
                                  scope, name=name, **kwargs)
        self.sbcallbacks.append(
            switchboard.requestCallbackMain('mesh boundaries changed',
                                        self.newBdys) )


def _makePointBdyWidget(param, scope, **kwargs):
    return MeshPointBdyParamWidget(param, scope, name=param.name, **kwargs)

meshparameters.MeshPointBdyParameter.makeWidget = _makePointBdyWidget

#Interface branch
def _getSortedBdyInterfaceNames(msh):
    interfacemsplugin=msh.getMicrostructure().getPlugIn("Interfaces")
    return msh.edgeBoundaryNames() + [_separator_proxy] + \
           interfacemsplugin.getInterfaceNames()

#This one includes the string "<every>"
def _getMeshEdgeBdyNamesExtra(msh):
    return [placeholder.every.IDstring] + msh.edgeBoundaryNames()

#This one lists mesh boundary names and interface names together.
#It is no longer used, as new mesh boundaries are also
#created from interfaces (originally, mesh boundaries are
#created only based on a skeleton boundary template).
class MeshEdgeBdyInterfaceParamWidget(MeshBoundaryParamWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param, _getSortedBdyInterfaceNames,
                                 scope, name=name, separator_func=_bdysepfunc,
                                 **kwargs)
        self.sbcallbacks.append(
            switchboard.requestCallbackMain('mesh boundaries changed',
                                            self.newBdys) )

def _makeEdgeBdyInterfaceWidget(param, scope, **kwargs):
    return MeshEdgeBdyInterfaceParamWidget(param, scope, name=param.name,
                                           **kwargs)

meshparameters.MeshEdgeBdyInterfaceParameter.makeWidget \
    = _makeEdgeBdyInterfaceWidget

class MeshEdgeBdyParamWidgetExtra(MeshBoundaryParamWidget):
    def __init__(self, param, scope, name=None, **kwargs):
        MeshParamWidget.__init__(self, param, _getMeshEdgeBdyNamesExtra,
                                 scope, name=name, separator_func=_bdysepfunc,
                                 **kwargs)
        self.sbcallbacks.append(
            switchboard.requestCallbackMain('mesh boundaries changed',
                                            self.newBdys) )

def _makeEdgeBdyWidgetExtra(param, scope, **kwargs):
    return MeshEdgeBdyParamWidgetExtra(param, scope, name=param.name, **kwargs)

meshparameters.MeshEdgeBdyParameterExtra.makeWidget = _makeEdgeBdyWidgetExtra
