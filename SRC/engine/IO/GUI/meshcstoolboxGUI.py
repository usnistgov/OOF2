# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# GUI part of the Mesh cross-section toolbox.  Collects mouse
# clicks, draws paths, etc.

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import utils
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import mousehandler
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import toolboxGUI
from ooflib.engine import analysisdomain
from ooflib.engine import analysissample
from ooflib.engine import mesh
from ooflib.engine.IO import analyze
from ooflib.engine.IO import analyzemenu
from ooflib.engine.IO import meshcstoolbox
from ooflib.engine.IO import meshmenu
from ooflib.engine.IO import outputdestination
from ooflib.engine.IO.GUI import outputdestinationwidget
from ooflib.engine.IO.GUI import sampleregclassfactory

from oofcanvas import oofcanvasgui

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# String displayed in the cross section chooser to mean that no cs is
# selected.
noCS = '<None>'

class CrossSectionToolboxGUI(toolboxGUI.GfxToolbox,
                             mousehandler.MouseHandler):
    def __init__(self, toolbox):
        toolboxGUI.GfxToolbox.__init__(
            self, utils.underscore2space(toolbox.name()), toolbox)

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                          margin=2)
        self.gtk.add(mainbox)

        sourceframe = Gtk.Frame(label="Source", shadow_type=Gtk.ShadowType.IN,
                                margin_start=2, margin_end=2,
                                margin_top=2, margin_bottom=2)
        mainbox.pack_start(sourceframe, fill=False, expand=False, padding=0)
        sourcescroll = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN,
                                          margin=2)
        gtklogger.logScrollBars(sourcescroll, "Source")
        sourceframe.add(sourcescroll)
        sourcescroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.NEVER)

        self.sourceText = Gtk.TextView(name="fixedfont", editable=False,
                                       wrap_mode=Gtk.WrapMode.WORD,
                                       cursor_visible=False,
                                       left_margin=2, right_margin=2,
                                       top_margin=2, bottom_margin=2)
        gtklogger.setWidgetName(self.sourceText, "text")
        sourcescroll.add(self.sourceText)

        csframe = Gtk.Frame(label="Cross Section",
                            shadow_type=Gtk.ShadowType.IN)
        mainbox.pack_start(csframe, expand=False, fill=False, padding=0)
        csbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                        margin=2)
        csframe.add(csbox)

        # Table contains the "current" and "points" widgets
        table = Gtk.Grid()
        csbox.pack_start(table, expand=False, fill=False, padding=0)

        # Widget which shows the name of the current cross-section.
        label = Gtk.Label(label="current: ", halign=Gtk.Align.END, hexpand=False)
        table.attach(label, 0,0, 1,1)
        self.csChooser = chooser.ChooserWidget(
            [], callback=self.csChooserCB, name='csList',
            hexpand=True, halign=Gtk.Align.FILL)
        table.attach(self.csChooser.gtk, 1,0,1,1)

        # Widget for how to sample the cross-section.
        label = Gtk.Label(label="points: ", halign=Gtk.Align.END, hexpand=False)
        table.attach(label, 0,1, 1,2)

        self.cs_sample_widget = sampleregclassfactory.SampleRCF(
            name="Sampling", 
            domainClass=analysisdomain.CrossSectionDomain,
            operationClass=analyze.DirectOutput,
            halign=Gtk.Align.FILL, hexpand=True)
        table.attach(self.cs_sample_widget.gtk, 1,1, 1,1)
        self.cs_sample_widget.update(analysissample.SampleSet.registry)
        self.int_valid_swcb = switchboard.requestCallbackMain(
            ('validity', self.cs_sample_widget), self.validCB)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       homogeneous=False,
                       margin_start=2, margin_end=2)
        csbox.pack_start(hbox, expand=False, fill=False, padding=0)
        # Rename button.
        self.renamebutton = Gtk.Button(label="Rename")
        gtklogger.setWidgetName(self.renamebutton, 'Rename')
        gtklogger.connect(self.renamebutton, 'clicked', self.csrenameCB)
        self.renamebutton.set_tooltip_text("Rename the current cross-section.")
        hbox.pack_start(self.renamebutton,fill=True,expand=True, padding=0)
        # Edit button
        self.editbutton = gtkutils.StockButton('document-edit-symbolic',
                                               "Edit...")
        gtklogger.setWidgetName(self.editbutton, 'Edit')
        gtklogger.connect(self.editbutton, 'clicked', self.cseditCB)
        self.editbutton.set_tooltip_text("Edit the current cross-section.")
        hbox.pack_start(self.editbutton, fill=True, expand=True, padding=0)
        # Copy button
        self.copybutton = gtkutils.StockButton("edit-copy-symbolic", "Copy...")
        gtklogger.setWidgetName(self.copybutton, 'Copy')
        gtklogger.connect(self.copybutton, 'clicked', self.cscopyCB)
        self.copybutton.set_tooltip_text("Copy the current cross-section.")
        hbox.pack_start(self.copybutton, fill=True, expand=True, padding=0)
        # Delete button.
        self.csdeletebutton = gtkutils.StockButton("edit-delete-symbolic",
                                                   "Remove")
        gtklogger.setWidgetName(self.csdeletebutton, 'Remove')
        gtklogger.connect(self.csdeletebutton, "clicked", self.csdeleteCB)
        self.csdeletebutton.set_tooltip_text(
            "Remove the current cross-section.")
        hbox.pack_start(self.csdeletebutton,fill=True,expand=True, padding=0)

        goframe = Gtk.Frame(label="Output", shadow_type=Gtk.ShadowType.IN)
        mainbox.pack_start(goframe, expand=False, fill=False, padding=0)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin=2)
        goframe.add(vbox)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       margin=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        
        label = Gtk.Label(label="Destination: ", halign=Gtk.Align.END)
        hbox.pack_start(label, expand=False, fill=False, padding=0)
        self.destwidget = outputdestinationwidget.TextDestinationWidget(
            name="Destination", hexpand=True, halign=Gtk.Align.FILL)
        self.dw_valid_swcb = switchboard.requestCallbackMain(
            ('validity', self.destwidget), self.validCB)
        hbox.pack_start(self.destwidget.gtk, expand=True, fill=True, padding=0)
        self.gobutton = gtkutils.StockButton("system-run-symbolic", "Go!")
        gtklogger.setWidgetName(self.gobutton, 'Go')
        vbox.pack_start(self.gobutton,expand=True, fill=True, padding=5)
        self.gobutton.set_tooltip_text("Send the output to the destination.")
        gtklogger.connect(self.gobutton, "clicked", self.goCB)
        
        self.startpoint = None
        self.endpoint = None

        # Data needed by the "go" button.  Set in "show_data", when
        # the state of all the widgets is examined.
        self.meshobj = None
        self.current_cs_name = None
        
        # Shut off non-GUI toolbox's switchboard callbacks.  We will
        # take them over at activate-time.
        self.toolbox.stop_callbacks()

    def __del__(self):
        switchboard.removeCallback(self.dw_valid_swcb)
        self.dw_valid_swcb = None
            
    def close(self):
        toolboxGUI.GfxToolbox.close(self)

    def activate(self):
        debug.mainthreadTest()
        ## TODO: Is this correct?  Why not GfxToolbox.activate(self)?
        self.toolbox.activate()
        self.gfxwindow().setMouseHandler(self)
        self.motionFlag = self.gfxwindow().allowMotionEvents(
            oofcanvasgui.MotionAllowed_MOUSEDOWN)
        self.gfxwindow().setRubberBand(oofcanvasgui.LineRubberBand())
        self.sb_callbacks = [
            switchboard.requestCallbackMain( (self.gfxwindow(),
                                              "layers changed"),
                                             self.newLayers ),
            switchboard.requestCallbackMain( (self.gfxwindow(),
                                              "new contourmap layer"),
                                             self.newLayers),
            # Need this signal to update the "current cross section" datum.
            switchboard.requestCallbackMain( "cross sections changed",
                                             self.show_data),
            switchboard.requestCallbackMain(("rename who", "Mesh"),
                                            self.newLayers)
            ]
        self.show_data()

    def deactivate(self):
        debug.mainthreadTest()
        ## TODO: Should this call GfxToolbox.deactivate(self)?
        self.gfxwindow().removeMouseHandler()
        self.gfxwindow().setRubberBand(None)
        self.gfxwindow().allowMotionEvents(self.motionFlag)
        for s in self.sb_callbacks:
            switchboard.removeCallback(s)
        self.sb_callbacks = []
        
    def validCB(self, valid):
        self.show_data()

    def csChooserCB(self, csname):
        if csname == noCS:
            self.toolbox.deselectCS()
        else:
            self.toolbox.selectCS(csname)
        self.cs_sample_widget.update(analysissample.SampleSet.registry)
        
    def show_data(self):
        debug.mainthreadTest()
        self.meshobj = self.toolbox.current_mesh
        meshok = self.meshobj is not None

        if meshok:
            srctext = "  mesh = " + mesh.meshes.getPath(self.meshobj)
        else:
            srctext = "No Mesh Displayed!"
        self.outputobj = self.toolbox.current_layer
        if self.outputobj is not None:
            srctext += "\noutput = " + self.outputobj.what.shortrepr()

        self.sourceText.get_buffer().set_text(srctext)

        csok = False
        if meshok:
            csname = self.meshobj.selectedCSName()
            csnames = self.meshobj.allCrossSectionNames()
            self.csChooser.update(csnames + [noCS])
            if csname:
                self.csChooser.set_state(csname)
            else:
                self.csChooser.set_state(noCS)
            self.current_cs_name = self.csChooser.get_value()
            csok = self.current_cs_name not in [noCS, None]
        else:
            self.csChooser.update([noCS])
        self.csdeletebutton.set_sensitive(csok)
        self.renamebutton.set_sensitive(csok)
        self.editbutton.set_sensitive(csok)
        self.copybutton.set_sensitive(csok)
                
        self.gobutton.set_sensitive(self.outputobj is not None
                                    and meshok and csok
                                    and self.destwidget.isValid())
        gtklogger.checkpoint(self.gfxwindow().name + " " +
                             self._name + " sensitized")
        
    def newLayers(self, *args):
        self.toolbox.newLayers()
        self.show_data()

    # Button callback for cross-section deletion -- removes the
    # current cross-section from the current mesh.  
    def csdeleteCB(self, gtkobj):
        meshobj = self.toolbox.current_mesh
        csname = meshobj.selectedCSName()
        menuitem = meshmenu.csmenu.Remove
        menuitem.callWithDefaults(
            mesh=meshobj.path(), name=csname)

    # Callback for the "Rename" button
    def csrenameCB(self, gtkobj):
        meshobj = self.toolbox.current_mesh
        csname = meshobj.selectedCSName()
        menuitem = meshmenu.csmenu.Rename
        newnameparam = menuitem.get_arg('name')
        newnameparam.value = csname
        if parameterwidgets.getParameterValues(
                newnameparam,
                parentwindow=self.gtk.get_toplevel(),
                title="Rename cross section " + csname):
            menuitem.callWithDefaults(mesh=meshobj.path(), cross_section=csname)

    def cseditCB(self, gtkobj):
        meshobj = self.toolbox.current_mesh
        csname = meshobj.selectedCSName()
        menuitem = meshmenu.csmenu.Edit
        csparam = menuitem.get_arg('cross_section')
        csparam.value = meshobj.selectedCS()
        if parameterwidgets.getParameterValues(
                csparam,
                parentwindow=self.gtk.get_toplevel(),
                title='Edit cross section ' + csname):
            menuitem.callWithDefaults(mesh=meshobj.path(), name=csname)
            
    def cscopyCB(self, gtkobj):
        meshobj = self.toolbox.current_mesh
        menuitem = meshmenu.csmenu.Copy
        csname = meshobj.selectedCSName()
        targetmeshparam = menuitem.get_arg('mesh')
        targetmeshparam.value = meshobj.path()
        targetnameparam = menuitem.get_arg('name')
        targetnameparam.value = csname
        if parameterwidgets.getParameters(
                targetmeshparam,
                targetnameparam,
                parentwindow=self.gtk.get_toplevel(),
                title='Copy cross section ' + csname):
            menuitem.callWithDefaults(current=meshobj.path(),
                                      cross_section=csname)
            
    # Actually write an output to the destination.
    def goCB(self, gtkobj):
        menuitem = analyzemenu.ops_menu.Direct_Output
        cs_domain = analysisdomain.CrossSectionDomain(
            self.csChooser.get_value())
        menuitem.callWithDefaults(mesh=mesh.meshes.getPath(self.meshobj),
                                  time=self.meshobj.getCurrentTime(),
                                  data=self.toolbox.current_layer.what,
                                  domain=cs_domain,
                                  sampling=self.cs_sample_widget.get_value(),
                                  destination=self.destwidget.get_value())
        
    # Mouse-handler stuff.
    def acceptEvent(self, event):
        return event=='up' or event=='down'
    def down(self, x, y, button, shift, ctrl, data):
        self.startpoint = primitives.Point(x,y)
    def up(self, x, y, button, shift, ctrl, data):
        self.endpoint = primitives.Point(x,y)
        self.toolbox.makeCS(self.startpoint, self.endpoint)





def _makeGUI(self):
    return CrossSectionToolboxGUI(self)

meshcstoolbox.CrossSectionToolbox.makeGUI = _makeGUI
