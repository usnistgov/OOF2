# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import equation
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import microstructure
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import fieldinit
from ooflib.engine import skeletoncontext
from ooflib.engine.IO import subproblemmenu
import ooflib.SWIG.engine.field
import ooflib.engine.IO.meshmenu
import ooflib.engine.mesh

from gi.repository import GObject
from gi.repository import Gtk
import string

allCompoundFields = ooflib.SWIG.engine.field.allCompoundFields

subpmenu = subproblemmenu.subproblemMenu
meshmenu = ooflib.engine.IO.meshmenu.meshmenu

class ButtonSignal:
    def __init__(self, button, signal):
        self.button = button
        self.signal = signal
    def set(self, active):
        debug.mainthreadTest()
        self.signal.block()
        self.button.set_active(active)
        self.signal.unblock()
    def set_sensitive(self, sensitivity):
        debug.mainthreadTest()
        self.button.set_sensitive(sensitivity)


class FieldPage(oofGUI.MainPage):
    def __init__(self):
        oofGUI.MainPage.__init__(self, name="Fields & Equations", ordering=210,
                                 tip="Define fields on a finite element mesh.")
        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=3,
                            halign=Gtk.Align.CENTER, margin_top=2)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)

        self.subpwidget = whowidget.WhoWidget(
            ooflib.engine.subproblemcontext.subproblems, scope=self)
        switchboard.requestCallbackMain(self.subpwidget, self.subpwidgetCB)
        label = Gtk.Label("Microstructure=", halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.subpwidget.gtk[0],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label("Skeleton=", halign=Gtk.Align.END, margin_start=5)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.subpwidget.gtk[1],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label("Mesh=", halign=Gtk.Align.END, margin_start=5)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.subpwidget.gtk[2],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label("SubProblem=", halign=Gtk.Align.END, margin_start=5)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.subpwidget.gtk[3],
                             expand=False, fill=False, padding=0)

        hpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                          wide_handle=True)
        gtklogger.setWidgetName(hpane, 'HPane')
        mainbox.pack_start(hpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(hpane, 'notify::position')

        ## Field Pane
        fieldframe = Gtk.Frame(
            label="Fields", shadow_type=Gtk.ShadowType.IN,
            margin_start=2, margin_end=gtkutils.handle_padding,
            margin_top=2, margin_bottom=2)
        hpane.pack1(fieldframe, resize=True, shrink=False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin=2)
        fieldframe.add(vbox)
        scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(scroll, "Fields")
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        vbox.pack_start(scroll, expand=True, fill=True, padding=0)
        self.fieldtable = Gtk.Grid(border_width=2)
        scroll.add(self.fieldtable)
        self.build_fieldTable()

        self.copyfieldbutton = Gtk.Button("Copy Field State...",
                                          halign=Gtk.Align.CENTER,
                                          hexpand=False)
        vbox.pack_start(self.copyfieldbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.setWidgetName(self.copyfieldbutton, 'CopyField')
        gtklogger.connect(self.copyfieldbutton, 'clicked', self.copyfstateCB)
        self.copyfieldbutton.set_tooltip_text(
            "Copy all field status variables from the current subproblem"
            " to another subproblem.")

        ## Equation Pane
        eqnframe = Gtk.Frame(
            label="Equations", shadow_type=Gtk.ShadowType.IN,
            margin_start=gtkutils.handle_padding, margin_end=2,
            margin_top=2, margin_bottom=2)
        hpane.pack2(eqnframe, resize=True, shrink=False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin=2)
        eqnframe.add(vbox)
        scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(scroll, "Equations")
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        vbox.pack_start(scroll, expand=True, fill=True, padding=0)
        self.eqntable = Gtk.Grid(border_width=2)
        scroll.add(self.eqntable)
        self.eqnbuttons = {}
        self.build_eqnTable()

        self.copyeqnbutton = Gtk.Button("Copy Equation State...",
                                        halign=Gtk.Align.CENTER,
                                        hexpand=False)
        vbox.pack_start(self.copyeqnbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.setWidgetName(self.copyeqnbutton, "CopyEquation")
        gtklogger.connect(self.copyeqnbutton, "clicked", self.copyeqstateCB)
        self.copyeqnbutton.set_tooltip_text(
            "Copy the status of all equations from the current mesh"
            " to another mesh.")

        switchboard.requestCallbackMain(("new who", "Microstructure"),
                                         self.newMSorSkeletonOrMesh)
        switchboard.requestCallbackMain(("new who", "Skeleton"),
                                        self.newMSorSkeletonOrMesh)
        switchboard.requestCallbackMain(("new who", "Mesh"),
                                        self.newMSorSkeletonOrMesh)
        switchboard.requestCallbackMain("made reservation",
                                        self.reservationChanged)
        switchboard.requestCallbackMain("cancelled reservation",
                                        self.reservationChanged)
        switchboard.requestCallbackMain("new field", self.newFieldCB)
        switchboard.requestCallbackMain("field defined", self.defineFldCB)
        switchboard.requestCallbackMain("field activated", self.activateFldCB)
        if config.dimension() == 2:
            switchboard.requestCallbackMain("field inplane", self.inplaneFldCB)
        switchboard.requestCallbackMain("new equation",self.newEquationCB)
        switchboard.requestCallbackMain("equation activated",
                                        self.activateEqnCB)
        switchboard.requestCallbackMain("mesh status changed",
                                        self.meshStatusCB)
#         switchboard.requestCallbackMain("field initialized", self.initFldCB)

    def installed(self):
        self.sensitize()
        self.update()

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    def build_fieldTable(self):
        debug.mainthreadTest()
        self.fieldtable.foreach(Gtk.Widget.destroy) # clear the table
        self.fieldbuttons = {}
        self.fieldtable.attach(
            Gtk.VSeparator(orientation=Gtk.Orientation.VERTICAL),
            1,0, 1,len(allCompoundFields))
        # self.fieldtable.set_col_spacing(0, 3)
        row = 0
        for fname, fld in allCompoundFields.items():
            label = Gtk.Label(fname, halign=Gtk.Align.END, hexpand=False)
            self.fieldtable.attach(label, 0,row, 1,1)

            button = Gtk.CheckButton('defined', hexpand=False)
            gtklogger.setWidgetName(button, fname+" defined")
            signal = gtklogger.connect(button, 'clicked',
                                       self.fieldDefineCB, fld)
            self.fieldbuttons[(fname, "defined")] = ButtonSignal(button, signal)
            self.fieldtable.attach(button, 2,row, 1,1)
            self.setFieldDefineTip(button, fld)

            button = Gtk.CheckButton('active', hexpand=False)
            gtklogger.setWidgetName(button, fname+" active")
            signal = gtklogger.connect(button, 'clicked',
                                       self.fieldActiveCB, fld)
            self.fieldbuttons[(fname, "active")] = ButtonSignal(button, signal)
            self.fieldtable.attach(button, 3,row, 1,1)
            self.setFieldActiveTip(button, fld)

            button = Gtk.CheckButton('in-plane')
            gtklogger.setWidgetName(button, fname + " in-plane")
            signal = gtklogger.connect(button, 'clicked',
                                       self.fieldInPlaneCB, fld)
            self.fieldbuttons[(fname, "inplane")] = ButtonSignal(button, signal)
            self.fieldtable.attach(button, 4,row, 1,1)
            self.setFieldInPlaneTip(button, fld)

            row += 1

    def newFieldCB(self):               # switchboard "new field"
        self.build_fieldTable()
        self.show()

    def fieldDefineCB(self, button, field): # gtk callback
        if button.get_active():
            subpmenu.Field.Define(subproblem=self.currentFullSubProblemName(),
                                  field=field)
        else:
            subpmenu.Field.Undefine(subproblem=self.currentFullSubProblemName(),
                                    field=field)
        self.setFieldDefineTip(button, field)

    def setFieldDefineTip(self, button, field):
        if button.get_active():
            verb = "Undefine"
        else:
            verb = "Define"
        button.set_tooltip_text(
            "%s the %s field on the mesh.  Only defined fields have values."
            % (verb, field.name()))

    def fieldActiveCB(self, button, field): # gtk callback
        if button.get_active():
            subpmenu.Field.Activate(
                subproblem=self.currentFullSubProblemName(), field=field)
        else:
            subpmenu.Field.Deactivate(
                subproblem=self.currentFullSubProblemName(), field=field)
        self.setFieldActiveTip(button, field)
        
    def setFieldActiveTip(self, button, field):
        if button.get_active():
            verb = "Deactivate"
        else:
            verb = "Activate"
        button.set_tooltip_text(
            "%s the %s field on the subproblem. The solver finds the values"
            " of the active fields by solving the active equations."
            % (verb, field.name()))

    def fieldInPlaneCB(self, button, field): # gtk callback
        debug.mainthreadTest()
        if button.get_active():
            meshmenu.Field.In_Plane(
                mesh=self.currentFullMeshName(),
                field = field)
        else:
            meshmenu.Field.Out_of_Plane(
                mesh=self.currentFullMeshName(),
                field = field)
        self.setFieldInPlaneTip(button, field)

    def setFieldInPlaneTip(self, button, field):
        debug.mainthreadTest()
        if button.get_active():
            verb = "Do not constrain"
        else:
            verb = "Constrain"
        button.set_tooltip_text(
            "%s the derivatives of the %s field to lie in the x-y plane."
            % (verb, field.name()))

    def defineFldCB(self, subpname, fieldname, defined): # sb "field defined"
        if subpname == self.currentFullSubProblemName():
            # TODO PLASTICITY: For testing purposes, we sometimes
            # define fields for which there are no widgets -- these
            # cause a key error here.  Ignore it.
            try:
                self.fieldbuttons[(fieldname, "defined")].set(defined)
            except KeyError:
                pass
            self.update()

    def activateFldCB(self, subpname, fieldname, active): # sb "field activated"
        if subpname == self.currentFullSubProblemName():
            self.fieldbuttons[(fieldname, "active")].set(active)

    def inplaneFldCB(self, meshname, fieldname, inplane): # sb "field inplane"
        if meshname == self.currentFullMeshName():
            self.fieldbuttons[(fieldname, "inplane")].set(inplane)

    def activateEqnCB(self, subpname, eqname, active): # "equation activated"
        if subpname == self.currentFullSubProblemName():
            self.eqnbuttons[(eqname, "active")].set(active)

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    def build_eqnTable(self):
        debug.mainthreadTest()
        self.eqntable.foreach(Gtk.Widget.destroy) # clear the table
        self.eqnbuttons = {}
        eqlist = equation.allEquations
        row=0
        for eqn in eqlist:
            label = Gtk.Label(utils.underscore2space(eqn.name()),
                              halign=Gtk.Align.END)
            self.eqntable.attach(label, 0,row, 1,1)
            button = Gtk.CheckButton('active')
            gtklogger.setWidgetName(button, eqn.name() + " active")
            signal = gtklogger.connect(button, 'clicked', self.eqnButtonCB, eqn)
            self.eqnbuttons[(eqn.name(), "active")] = ButtonSignal(button,
                                                                   signal)
            button.set_tooltip_text('Active equations will be solved.')
            self.eqntable.attach(button, 2,row, 1,1)
            row += 1
        self.eqntable.attach(
            Gtk.Separator(orientation=Gtk.Orientation.VERTICAL),
            1,0, 1,len(eqlist))

    def newEquationCB(self):  # Switchboard, "new equation".
        self.build_eqnTable()
        self.show()

    def activateEqnCB(self, subproblem, eqn, active): # sb "equation activated"
         if subproblem == self.currentFullSubProblemName():
             self.eqnbuttons[(eqn, "active")].set(active)

    def eqnButtonCB(self, button, eqn): # gtk callback
        if button.get_active():
            subpmenu.Equation.Activate(
                subproblem=self.currentFullSubProblemName(), equation=eqn)
        else:
            subpmenu.Equation.Deactivate(
                subproblem=self.currentFullSubProblemName(), equation=eqn)


    ########################

    def currentFullMeshName(self):
        return self.subpwidget.get_value(depth=3)
    def currentMeshContext(self):
        try:
            return ooflib.engine.mesh.meshes[self.currentFullMeshName()]
        except KeyError:
            return None
    def currentMesh(self):
        meshctxt = self.currentMeshContext()
        if meshctxt:
            return meshctxt.getObject()
            
    def currentFullSubProblemName(self):
        return self.subpwidget.get_value()
    def currentSubProblemContext(self):
        try:
            return ooflib.engine.subproblemcontext.subproblems[
                self.currentFullSubProblemName()]
        except KeyError:
            return None
    def currentSubProblem(self):
        subpc = self.currentSubProblemContext()
        if subpc:
            return subpc.getObject()

    def sensitize(self):
        # This is called a lot, from reservationChanged() amd
        # meshStatusCB().  There's not much to do about it, short of a
        # system for aggregating switchboard calls. Extra calls to
        # this function aren't really a problem, although they do
        # result in a lot of checkpoint lines in the gui log file.
        debug.mainthreadTest()
        subpctxt = self.currentSubProblemContext()
        subpok = subpctxt is not None and not subpctxt.query_reservation()
        meshctxt = self.currentMeshContext()
        meshok = meshctxt and not meshctxt.outOfSync()
        self.fieldtable.set_sensitive(subpok and meshok)
        self.eqntable.set_sensitive(subpok and meshok)
        self.copyfieldbutton.set_sensitive(subpok and meshok)
        self.copyeqnbutton.set_sensitive(subpok and meshok)
        gtklogger.checkpoint("Field page sensitized")
        
    def update(self):
        self.set_state(self.currentFullSubProblemName())

    def set_state(self, subppath):
        debug.mainthreadTest()
        path = labeltree.makePath(subppath)
        self.subpwidget.set_value(path)
        # Retrieve the subproblem from the widget, just in case
        # subppath wasn't a complete subproblem path.
        subpctxt = self.currentSubProblemContext()
        if subpctxt:           # ie, path was complete
            subp = subpctxt.getObject() # CSubProblem object
            mesh = self.currentMesh()
            for fname,fld in allCompoundFields.items():
                fdef = subp.is_defined_field(fld)
                self.fieldbuttons[(fname, "defined")].set(fdef)
                self.fieldbuttons[(fname, "active")].set_sensitive(fdef)
                if config.dimension() == 2:
                    self.fieldbuttons[(fname, "inplane")].set_sensitive(fdef)
                if fdef:
                    self.fieldbuttons[(fname, "active")].set(
                        subp.is_active_field(fld))
                    if config.dimension() == 2:
                        self.fieldbuttons[(fname, "inplane")].set(
                            mesh.in_plane(fld))
                else:                   # field not defined
                    self.fieldbuttons[(fname, "active")].set(0)
                    if config.dimension() == 2:
                        self.fieldbuttons[(fname, "inplane")].set(0)
            for eqn in equation.allEquations:
                active = subp.is_active_equation(eqn)
                self.eqnbuttons[(eqn.name(),"active")].set(active)
        else:                           # no current subproblem
            for button in self.fieldbuttons.values():
                button.set(False)
            for button in self.eqnbuttons.values():
                button.set(False)
        self.sensitize()

    def copyfstateCB(self, gtkobj):     # Button callback.
        menuitem = subpmenu.Copy_Field_State
        targetparam = menuitem.get_arg("target")
        
        targetparam.set(self.currentFullSubProblemName())
        if parameterwidgets.getParameters(targetparam,
                                          parentwindow=self.gtk.get_toplevel(),
                                          title="Select a target Subproblem"):
            menuitem.callWithDefaults(source=self.currentFullSubProblemName())

    def copyeqstateCB(self, gtkobj): # Button callback
        menuitem = subpmenu.Copy_Equation_State
        targetparam = menuitem.get_arg("target")
        targetparam.set(self.currentFullSubProblemName())
        if parameterwidgets.getParameters(targetparam,
                                          parentwindow=self.gtk.get_toplevel(),
                                          title="Select a target subproblem"):
            menuitem.callWithDefaults(source=self.currentFullSubProblemName())

    # switchboard ("new who", "Skeleton") or ("new who", "Mesh")
    def newMSorSkeletonOrMesh(self, skeletonname):
        if not self.currentSubProblemContext():
            self.subpwidget.set_value(skeletonname)

    def subpwidgetCB(self, interactive):      # switchboard callback
        self.update()

    def reservationChanged(self, whoobj):
        # switchboard "made reservation", "cancelled reservation"
        if self.currentFullSubProblemName() == whoobj.path():
            self.sensitize()

    def meshStatusCB(self, meshctxt):
        if meshctxt is self.currentMeshContext():
            self.sensitize()

#############

fp = FieldPage()
