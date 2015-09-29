# -*- python -*-
# $RCSfile: equationPage.py,v $
# $Revision: 1.57 $
# $Author: langer $
# $Date: 2010/06/02 20:25:31 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

OBSOLETE

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import equation
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import microstructure
from ooflib.common import utils
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import tooltips
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import subproblemcontext
from ooflib.engine.IO import subproblemmenu
import gtk

subpmenu = subproblemmenu.subproblemMenu

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

class EquationPage(oofGUI.MainPage):
    def __init__(self):
        oofGUI.MainPage.__init__(self, name="Equations", ordering=220,
                                 tip="Define equations for the mesh to solve.")
        mainbox = gtk.VBox()
        self.gtk.add(mainbox)
        
        align = gtk.Alignment(xalign=0.5)
        mainbox.pack_start(align, expand=0, fill=0)
        centerbox = gtk.HBox(spacing=3)
        align.add(centerbox)
        self.subpwidget = whowidget.WhoWidget(
            whoville.getClass('SubProblem'), scope=self)
        switchboard.requestCallbackMain(self.subpwidget, self.subpwidgetCB)
        label = gtk.Label("Microstructure=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.subpwidget.gtk[0], expand=0, fill=0)
        label = gtk.Label("Skeleton=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.subpwidget.gtk[1], expand=0, fill=0)
        label = gtk.Label("Mesh=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.subpwidget.gtk[2], expand=0, fill=0)
        label = gtk.Label("SubProblem=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.subpwidget.gtk[3], expand=0, fill=0)

        eqnframe = gtk.Frame("Equations")
        eqnframe.set_shadow_type(gtk.SHADOW_IN)
        scroll = gtk.ScrolledWindow()
        gtklogger.logScrollBars(scroll, "Equations")
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        eqnframe.add(scroll)
        bbox = gtk.VBox() # extra layer keeps table from expanding inside scroll
        scroll.add_with_viewport(bbox)
        self.eqntable = gtk.Table()
        bbox.pack_start(self.eqntable, expand=0, fill=0)
        self.eqnbuttons = {}
        self.build_eqnTable()
        switchboard.requestCallbackMain("new equation",
                                        self.newEquationCB)
        switchboard.requestCallbackMain("equation activated",
                                        self.activateEqnCB)
#         switchboard.requestCallbackMain("kinetics activated",
#                                         self.activateKinCB)
#         switchboard.requestCallbackMain("dynamics activated",
#                                         self.activateDynCB)
        mainbox.pack_start(eqnframe, expand=1, fill=1)

        copybox = gtk.HBox(spacing=3)
        self.copybutton = gtk.Button("Copy Equation State")
        gtklogger.setWidgetName(self.copybutton, "Copy")
        gtklogger.connect(self.copybutton, "clicked", self.copyeqstateCB)
        copybox.pack_start(self.copybutton, expand=1,fill=0)
        mainbox.pack_start(copybox, expand=0, fill=0)
        tooltips.set_tooltip_text(self.copybutton,
            "Copy the status of all equations from the current mesh to another mesh.")
        
        switchboard.requestCallbackMain(("new who", "Microstructure"),
                                        self.newSkeletonOrMesh)
        switchboard.requestCallbackMain(("new who", "Skeleton"),
                                        self.newSkeletonOrMesh)
        switchboard.requestCallbackMain(("new who", "Mesh"),
                                        self.newSkeletonOrMesh)
##        switchboard.requestCallbackMain(("new who", "SubProblem"),
##                                        self.newSubProblem)
##        switchboard.requestCallbackMain(("remove who", "SubProblem"),
##                                        self.removeSubProblem)
        switchboard.requestCallbackMain("made reservation",
                                        self.reservationChanged)
        switchboard.requestCallbackMain("cancelled reservation",
                                        self.reservationChanged)

    def installed(self):
        self.sensitize()
        self.update()

    #######################

    def build_eqnTable(self):
        debug.mainthreadTest()
        self.eqntable.foreach(gtk.Object.destroy) # clear the table
        self.eqnbuttons = {}
        eqlist = equation.allEquations
        self.eqntable.resize(len(eqlist), 3)
        row=0
        for eqn in eqlist:
            label = gtk.Label(utils.underscore2space(eqn.name()))
            label.set_alignment(1.0, 0.5)
            self.eqntable.attach(label, 0,1, row, row+1,
                                 xoptions=gtk.FILL, yoptions=0)
            button = gtk.CheckButton('active')
            gtklogger.setWidgetName(button, eqn.name() + " active")
            signal = gtklogger.connect(button, 'clicked', self.eqnButtonCB, eqn)
            self.eqnbuttons[(eqn.name(), "active")] = ButtonSignal(button,
                                                                   signal)
            tooltips.set_tooltip_text(button,'Active equations will be solved.')
            self.eqntable.attach(button, 2,3, row,row+1, xoptions=0,
                                 yoptions=0)
## Moved to time dependence page
#             if eqn.get_kinetic()>0 and config.devel()>=1:
#                 button = gtk.CheckButton('kinetic')
#                 gtklogger.setWidgetName(button, eqn.name() + " kinetic")
#                 signal = gtklogger.connect(button, 'clicked', self.eqnKineticCB,
#                                            eqn)
#                 self.eqnbuttons[(eqn.name(), "kinetic")] = ButtonSignal(button,
#                                                                         signal)
#                 self.eqntable.attach(button, 3,4, row, row+1,
#                                    xoptions=0, yoptions=0)
#             if eqn.get_dynamics()>0 and config.devel()>=1:
#                 button = gtk.CheckButton('dynamic')
#                 gtklogger.setWidgetName(button, eqn.name() + " dynamic")
#                 signal = gtklogger.connect(button, 'clicked',
#                                            self.eqnDynamicCB, eqn)
#                 self.eqnbuttons[(eqn.name(), "dynamic")] = ButtonSignal(button,
#                                                                         signal)
#                 self.eqntable.attach(button, 4,5, row, row+1,
#                                    xoptions=0, yoptions=0)
            row += 1
        self.eqntable.attach(gtk.VSeparator(), 1,2, 0,len(eqlist),
                             xoptions=0, yoptions=gtk.EXPAND|gtk.FILL)
        self.eqntable.set_col_spacing(0, 3)

    def newEquationCB(self):  # Switchboard, "new equation".
        self.build_eqnTable()
        self.show()

#     def eqnKineticCB(self, button, eqn): # gtk callback
#         if button.get_active():
#             subpmenu.Equation.ActivateKinetics(
#                 subproblem=self.currentFullSubProblemName(), equation=eqn)
#         else:
#             subpmenu.Equation.DeactivateKinetics(
#                 subproblem=self.currentFullSubProblemName(), equation=eqn)


#     def eqnDynamicCB(self, button, eqn): # gtk callback
#         if button.get_active():
#             subpmenu.Equation.ActivateDynamics(
#                 subproblem=self.currentFullSubProblemName(), equation=eqn)
#         else:
#             subpmenu.Equation.DeactivateDynamics(
#                 subproblem=self.currentFullSubProblemName(), equation=eqn)


    def eqnButtonCB(self, button, eqn): # gtk callback
        if button.get_active():
            subpmenu.Equation.Activate(
                subproblem=self.currentFullSubProblemName(), equation=eqn)
        else:
            subpmenu.Equation.Deactivate(
                subproblem=self.currentFullSubProblemName(), equation=eqn)


    def activateEqnCB(self, subproblem, eqn, active): # sb "equation activated"
         if subproblem == self.currentFullSubProblemName():
             self.eqnbuttons[(eqn, "active")].set(active)
            
#     def activateKinCB(self, subproblem, eqn, active): # sb "kinetics activated"
#         if subproblem == self.currentFullSubProblemName():
#             self.eqnbuttons[(eqn, "kinetic")].set(active)

#     def activateDynCB(self, subproblem, eqn, active): # sb "dynamics activated"
#         if subproblem == self.currentFullSubProblemName():
#             self.eqnbuttons[(eqn, "dynamic")].set(active)

    ########################

    def currentFullSubProblemName(self):
        return self.subpwidget.get_value()
    def currentSubProblemContext(self):
        try:
            return subproblemcontext.subproblems[
                self.currentFullSubProblemName()]
        except KeyError:
            return None
    def currentSubProblem(self):
        subpc = self.currentSubProblemContext()
        if subpc:
            return subpc.getObject()
            
    def sensitize(self):
        debug.mainthreadTest()
        subpctxt = self.currentSubProblemContext()
        subpok = subpctxt is not None and not subpctxt.query_reservation()
        self.eqntable.set_sensitive(subpok)
        self.copybutton.set_sensitive(subpok)
        self.update()
    def update(self):
        self.set_state(self.currentFullSubProblemName())
    def set_state(self, subppath):
        debug.mainthreadTest()
        path = labeltree.makePath(subppath)
        self.subpwidget.set_value(path)
        # Retrieve widget value in case path wasn't a complete SubProblem path.
        subproblem = self.currentSubProblemContext()
        if subproblem:
            subp = subproblem.getObject()
            for eqn in equation.allEquations:
                active = subp.is_active_equation(eqn)
                self.eqnbuttons[(eqn.name(),"active")].set(active)
#                 if config.devel():
#                     kinstate = eqn.name() in subproblem.active_kinetics
#                     self.eqnbuttons[(eqn.name(),"kinetic")].set(kinstate)
#                     self.eqnbuttons[(eqn.name(),"kinetic")].set_sensitive(
#                         active and eqn.get_kinetic)
                
#                     dynstate = eqn.name() in subproblem.active_dynamics
#                     self.eqnbuttons[(eqn.name(),"dynamic")].set(dynstate)
#                     self.eqnbuttons[(eqn.name(),"dynamic")].set_sensitive(
#                         active and eqn.get_dynamics())
        else:                           # no current subproblem
            for button in self.eqnbuttons.values():
                button.set(0)

    def copyeqstateCB(self, gtkobj):
        menuitem = subpmenu.Copy_Equation_State
        targetparam = menuitem.get_arg("target")
        targetparam.set(self.currentFullSubProblemName())
        if parameterwidgets.getParameters(targetparam,
                                          title="Select a target subproblem"):
            menuitem.callWithDefaults(source=self.currentFullSubProblemName())
    
    # switchboard ("new who", "Skeleton") or ("new who", "Mesh")
    def newSkeletonOrMesh(self, skeletonname):
        if not self.currentSubProblem():
            self.subpwidget.set_value(skeletonname)

##    def newSubProblem(self, subpname):  # switchboard ("new who", "SubProblem")
##        self.set_state(subpname)
##        self.sensitize()
        
    def subpwidgetCB(self, interactive): # sb widget signal
        self.update()
        self.sensitize()

##    def removeSubProblem(self, path):   # sb ("remove who", "SubProblem")
##        self.update()
##        self.sensitize()

    def reservationChanged(self, whoobj):
        # switchboard "made reservation", "cancelled reservation"
        if self.currentFullSubProblemName() == whoobj.path():
            self.sensitize()


#############

ep = EquationPage()
