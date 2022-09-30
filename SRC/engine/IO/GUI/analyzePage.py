# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.engine import ooferror2
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import utils
from ooflib.common.IO import placeholder
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import analysisdomain
from ooflib.engine import namedanalysis
from ooflib.engine.IO import analyze
from ooflib.engine.IO import analyzemenu
from ooflib.engine.IO.GUI import outputdestinationwidget
from ooflib.engine.IO.GUI import outputwidget
from ooflib.engine.IO.GUI import sampleregclassfactory
import ooflib.engine.mesh

from gi.repository import Gdk
from gi.repository import Gtk

# A page on which various aspects of the solved mesh can be queried --
# cross-section and statistical outputs will live here, with the
# ability to be put into files, and so forth. 

# Base class for AnalyzePage and BoundaryAnalysisPage.

## TODO: "Go" button isn't desensitized when XY function arg is empty

class BaseAnalysisPage(oofGUI.MainPage):
    def buildBottomRow(self, mainbox):
        # Build the bottom row of widgets, containing the named
        # analysis buttons, the Destination chooser, and the Go
        # button.
        # Box along the bottom of the page, containing Named Analyses,
        # Destination, and Go.
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       homogeneous=True, margin=2)
        mainbox.pack_start(hbox, expand=False, fill=False, padding=0)

        # Named Analyses
        nameframe = Gtk.Frame(label="Named Analyses",
                              shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(nameframe, 'Name')
        hbox.pack_start(nameframe, expand=True, fill=True, padding=0)
        namebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                          margin=2)
        nameframe.add(namebox)

        namedOpsBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                              margin=2)
        namebox.pack_start(namedOpsBox, expand=True, fill=True, padding=0)
        self.createNamedOpButton = Gtk.Button('New...')
        gtklogger.setWidgetName(self.createNamedOpButton, "New")
        gtklogger.connect(self.createNamedOpButton, 'clicked', self.createCB)
        self.createNamedOpButton.set_tooltip_text(
            "Name and store the current analysis settings.")
        namedOpsBox.pack_start(self.createNamedOpButton,
                               expand=True, fill=True, padding=0)
        
        self.saveNamedOpButton = Gtk.Button('Save...')
        gtklogger.setWidgetName(self.saveNamedOpButton, "Save")
        gtklogger.connect(self.saveNamedOpButton, 'clicked', self.savenamedCB)
        self.saveNamedOpButton.set_tooltip_text(
            "Save the definitions of the named analyses in a file.")
        namedOpsBox.pack_start(self.saveNamedOpButton,
                               expand=True, fill=True, padding=0)

        self.deleteNamedOpButton = Gtk.Button('Delete...')
        gtklogger.setWidgetName(self.deleteNamedOpButton, "Delete")
        gtklogger.connect(self.deleteNamedOpButton, 'clicked', self.deleteCB)
        self.deleteNamedOpButton.set_tooltip_text("Delete a named analysis.")
        namedOpsBox.pack_start(self.deleteNamedOpButton,
                               expand=True, fill=True, padding=0)
         
        # Display the name of the current analysis, if there is one.
        hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        namebox.pack_start(hbox4, expand=False, fill=False, padding=0)
        hbox4.pack_start(Gtk.Label("Current:"),
                         expand=False, fill=False, padding=0)
        self.namedAnalysisChooser = chooser.ChooserWidget(
            [], callback=self.retrieveCB, name="Retrieve", allowNone=True)
        hbox4.pack_start(self.namedAnalysisChooser.gtk,
                         expand=True, fill=True, padding=0)

        # Destination
        destinationframe = Gtk.Frame(label="Destination",
                                     shadow_type=Gtk.ShadowType.IN)
        hbox.pack_start(destinationframe, expand=True, fill=True, padding=0)
        destbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                          margin=2)
        destinationframe.add(destbox)

        self.destwidget = outputdestinationwidget.TextDestinationWidget(
            name="Destination", framed=False)
        destbox.pack_start(self.destwidget.gtk,
                           expand=True, fill=True, padding=0)
        
        # Go button
        self.go_button = gtkutils.StockButton("system-run-symbolic", "Go",
                                              halign=Gtk.Align.CENTER,
                                              valign=Gtk.Align.CENTER)
        gtklogger.setWidgetName(self.go_button, 'Go')
        gtklogger.connect(self.go_button, "clicked", self.go_buttonCB)
        self.go_button.set_tooltip_text("Send the output to the destination.")
        hbox.pack_start(self.go_button, fill=True, expand=False, padding=0)

    def sensitizeBottomRow(self, createOK, namedOK):
        self.createNamedOpButton.set_sensitive(createOK)
        self.deleteNamedOpButton.set_sensitive(namedOK)
        self.saveNamedOpButton.set_sensitive(namedOK)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# DataOperationFactory is a RegisteredClassFactory that only lists the
# operations consistent with the setting of the Scalar/Aggregate
# buttons on the Analysis page.
class DataOperationFactory(regclassfactory.RegisteredClassFactory):
    def __init__(self, page, *args, **kwargs):
        self.page = page
        regclassfactory.RegisteredClassFactory.__init__(self, *args, **kwargs)
    def includeRegistration(self, registration):
        return registration.acceptsOutput(self.page.getOutput())
        
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

pshrink = False # can the Paneds shrink below the size of their contents?

class AnalyzePage(BaseAnalysisPage):
    def __init__(self):
        oofGUI.MainPage.__init__(
            self, name="Analysis", ordering=259,
            tip="Query the mesh, examine fields and fluxes.")
        
        self.timeparam = placeholder.TimeParameter('time', value=0.0)

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER, margin_top=2,
                            spacing=2)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        self.meshwidget = whowidget.WhoWidget(ooflib.engine.mesh.meshes,
                                              scope=self)
        # The mesh widget callback is not required, because the field
        # and flux widgets in the "output" widget (which are members
        # of a parameter table, which is a component of the
        # OutputWidget) are context-sensitive and update themselves
        # automatically.
        label = Gtk.Label("Microstructure=", halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.meshwidget.gtk[0],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label("Skeleton=", halign=Gtk.Align.END, margin_start=5)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.meshwidget.gtk[1],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label("Mesh=", halign=Gtk.Align.END, margin_start=5)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.meshwidget.gtk[2],
                             expand=False, fill=False, padding=0)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            spacing=3, halign=Gtk.Align.CENTER)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)

        self.timeWidget = self.timeparam.makeWidget(scope=self)
        centerbox.pack_start(Gtk.Label("Time="),
                             expand=False, fill=False, padding=0)
        centerbox.pack_start(self.timeWidget.gtk,
                             expand=False, fill=False, padding=0)

        mainvpane = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL,
                              wide_handle=True,
                              margin_start=2, margin_end=2)
        mainbox.pack_start(mainvpane, expand=True, fill=True, padding=0)
        gtklogger.setWidgetName(mainvpane, 'mainpane')
        gtklogger.connect_passive(mainvpane, 'notify::position')
        self.topPane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                                 wide_handle=True)
        gtklogger.setWidgetName(self.topPane, 'top')
        mainvpane.pack1(self.topPane, resize=True, shrink=False)
        self.btmPane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                                 wide_handle=True)
        gtklogger.setWidgetName(self.btmPane, 'bottom')
        mainvpane.pack2(self.btmPane, resize=True, shrink=False)
        # The four panes (Output, Domain, Operation, and Sampling) are
        # contained in the top and bottom Paneds.  The dividers
        # between the sub panes are synchronized with each other.
        # Since Paneds don't have a dedicated signal indicating that
        # their dividers have been moved, we have to use the the
        # generic 'notify' signal.
        self.paneSignals = {
            self.topPane : gtklogger.connect(self.topPane,
                                             'notify::position', 
                                             self.paneMovedCB,
                                             self.btmPane),
            self.btmPane : gtklogger.connect(self.btmPane,
                                             'notify::position',
                                             self.paneMovedCB,
                                             self.topPane)
        }

        self.outputframe = Gtk.Frame(
            label="Output", shadow_type=Gtk.ShadowType.IN,
            margin_end=gtkutils.handle_padding,
            margin_bottom=gtkutils.handle_padding)
        output_scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(output_scroll, "Output")
        output_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.outputframe.add(output_scroll)
        output_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                             margin=2)
        output_type_selector_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        output_box.pack_start(output_type_selector_box,
                              expand=False, fill=False, padding=0)

        self.scalar_output_button = Gtk.RadioButton("Scalar")
        gtklogger.setWidgetName(self.scalar_output_button, 'ScalarMode')
        self.aggregate_output_button = Gtk.RadioButton(
            "Aggregate", group=self.scalar_output_button)
        gtklogger.setWidgetName(self.aggregate_output_button, 'AggregateMode')
        output_type_selector_box.pack_start(self.scalar_output_button,
                                            expand=False, fill=False, padding=0)
        output_type_selector_box.pack_start(self.aggregate_output_button,
                                            expand=False, fill=False, padding=0)
        self.scalarSignal = gtklogger.connect(self.scalar_output_button,
                                              "clicked",
                                              self.scalar_button_CB)
        self.aggregateSignal = gtklogger.connect(self.aggregate_output_button,
                                                 'clicked',
                                                 self.scalar_button_CB)

        # Both aggregate and scalar widgets are built here, and they
        # are switched by show/hide.
        ## TODO: Use the ValueOutputWidget here.  In incorporates both
        ## the aggregate and scalar widgets.
        self.scalar_output_button.set_active(1)
        self.scalar_output_obj = outputwidget.ScalarOutputParameterWidget(
            None, scope=self, name="Scalar",
            shadow_type=Gtk.ShadowType.NONE)
        self.aggregate_output_obj = \
            outputwidget.AggregateOutputParameterWidget(
                None, scope=self, name="Aggregate",
                shadow_type=Gtk.ShadowType.NONE)
        
        self.output_obj = self.scalar_output_obj
        output_box.pack_start(self.scalar_output_obj.gtk,
                              expand=False, fill=False, padding=0)
        output_box.pack_start(self.aggregate_output_obj.gtk,
                              expand=False, fill=False, padding=0)
        self.aggregate_output_obj.gtk.hide()
        
        output_scroll.add_with_viewport(output_box)
        self.topPane.pack1(self.outputframe, resize=True, shrink=pshrink)

        # Operation
        self.operationframe = Gtk.Frame(
            label="Operation", shadow_type=Gtk.ShadowType.IN,
            margin_top=gtkutils.handle_padding,
            margin_end=gtkutils.handle_padding)
        op_scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(op_scroll, "Operation")
        op_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.op_obj = DataOperationFactory(
            self, analyze.DataOperation.registry, scope=self,
            name="OperationRCF", callback = self.newOperationCB,
            shadow_type=Gtk.ShadowType.NONE)
        self.operationframe.add(op_scroll)

        op_scroll.add(self.op_obj.gtk)
        self.btmPane.pack1(self.operationframe, resize=True, shrink=pshrink)

        # Domain
        self.domainframe = Gtk.Frame(
            label="Domain",
            margin_bottom=gtkutils.handle_padding,
            margin_start=gtkutils.handle_padding)
        dom_scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(dom_scroll, "Domain")
        dom_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.domain_obj = regclassfactory.RegisteredClassFactory(
            analysisdomain.Domain.registry, scope=self, name="DomainRCF",
            callback = self.newDomainCB, shadow_type=Gtk.ShadowType.NONE)
        self.domainframe.add(dom_scroll)
        dom_scroll.add(self.domain_obj.gtk)
        self.topPane.pack2(self.domainframe, resize=True, shrink=pshrink)
        
        # Sampling.  The SampleRCF class uses the WidgetScope
        # mechanism to find the Operation and Domain widgets, so that
        # it can display only the relevant SampleSet classes. 
        self.sampleframe = Gtk.Frame(
            label="Sampling", shadow_type=Gtk.ShadowType.IN,
            margin_start=gtkutils.handle_padding,
            margin_top=gtkutils.handle_padding)
        sam_scroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(sam_scroll, "Sampling")
        sam_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.sample_obj = sampleregclassfactory.SampleRCF(
            scope=self, name="Sampling", callback=self.newSampleCB,
            shadow_type=Gtk.ShadowType.NONE)
        self.sampleframe.add(sam_scroll)
        sam_scroll.add(self.sample_obj.gtk)
        self.btmPane.pack2(self.sampleframe, resize=True, shrink=pshrink)

        self.buildBottomRow(mainbox)
        
        # Whenever fields or fluxes are defined or undefined on the
        # mesh, we need to update the output object widget, and
        # possibly invalidate the currently-displayed data, once we
        # start displaying data.

        switchboard.requestCallbackMain(("new who", "Mesh"), self.new_mesh)
        switchboard.requestCallbackMain(("new who", "Skeleton"), self.new_skel)
        
        switchboard.requestCallbackMain(('validity', self.timeWidget),
                                        self.sensitize_widgets)
        switchboard.requestCallbackMain(('validity', self.domain_obj),
                                        self.sensitize_widgets)
        switchboard.requestCallbackMain(('validity', self.op_obj),
                                        self.sensitize_widgets)

        # If the Output changes, the allowed Operations change.
        # updateOperations calls sensitize_widgets too.
        switchboard.requestCallbackMain(self.aggregate_output_obj,
                                        self.updateOperations)
        switchboard.requestCallbackMain(self.scalar_output_obj,
                                        self.updateOperations)

        switchboard.requestCallbackMain(('validity', self.destwidget),
                                        self.sensitize_widgets)
        switchboard.requestCallbackMain("named analyses changed",
                                        self.analysesChanged)
        switchboard.requestCallbackMain("retrieve analysis",
                                        self.retrieve_analysis)
        switchboard.requestCallbackMain("mesh status changed",
                                        self.sensitize_widgets)

        # These signals need to be suppressed when retrieving a named
        # analysis to avoid a signalling loop.
        self.namedAnalysisSignals = [
            switchboard.requestCallbackMain(self.domain_obj,
                                            self.setNamedAnalysisChooser),
            switchboard.requestCallbackMain(self.op_obj,
                                            self.setNamedAnalysisChooser),
            switchboard.requestCallbackMain(self.scalar_output_obj,
                                            self.setNamedAnalysisChooser),
            switchboard.requestCallbackMain(self.aggregate_output_obj,
                                            self.setNamedAnalysisChooser),
            switchboard.requestCallbackMain(self.sample_obj,
                                            self.setNamedAnalysisChooser)
            ]

    menuWidgetName = 'NamedOpsMenu'
    def show(self):
        # show() is called once, when the page is first created.
        # installed(), below, is called each time the user switches to
        # the page.
        debug.mainthreadTest()
        self.gtk.show_all()
        if self.scalar_output_button.get_active():
            self.aggregate_output_obj.gtk.hide()
        else:
            self.scalar_output_obj.gtk.hide()
        
    def installed(self):
        self.sensitize_widgets()

    # Synchronize the top and bottom panes
    def paneMovedCB(self, pane, gparamspec, otherpane):
        # If a pane is moved to a point where the other pane can't
        # follow, then this callback is called for *both* panes, even
        # though the signal is blocked.  Probably gtk is trying to
        # move the pane to an impossible position while the signal is
        # blocked, and then moving it back to its legal position after
        # the signal is unblocked.
        
        pos = pane.get_position()
        # Try to move the other pane to the position of the one
        # that just moved and triggered this callback.
        self.paneSignals[otherpane].block()
        try:
            otherpane.set_position(pos)
        finally:
            self.paneSignals[otherpane].unblock()

    def currentMeshContext(self):
        meshname = self.meshwidget.get_value()
        try:
            return ooflib.engine.mesh.meshes[meshname]
        except KeyError:
            return None
        
    def sensitize_widgets(self, *args):
        debug.mainthreadTest()
        meshctxt = self.currentMeshContext()
        meshok = meshctxt and not meshctxt.outOfSync()
        go_sensitive = bool(meshok and 
                            self.op_obj.isValid() and
                            self.output_obj.isValid() and 
                            self.destwidget.isValid() and
                            self.domain_obj.isValid() and 
                            self.sample_obj.isValid() and
                            self.timeWidget.isValid())
        self.go_button.set_sensitive(go_sensitive)
        namedok = len(namedanalysis.bulkAnalysisNames()) > 0
        self.sensitizeBottomRow(go_sensitive, namedok)
        self.namedAnalysisChooser.gtk.set_sensitive(namedok)

    def getOutput(self):
        return self.output_obj.get_value()

    def analysesChanged(self, *args):
        self.sensitize_widgets()
        self.setNamedAnalysisChooser()

    # GUI callback for the button that switches the widget.  Also
    # switches "self.output_obj", so it can be mindlessly read by the
    # "go"-button callback.
    def scalar_button_CB(self, gtkobj):
        debug.mainthreadTest()
        # This callback is called when the radio buttons are both set
        # and unset, which means that it's called twice for each user
        # action, which is unnecessary.
        if not gtkobj.get_active():
            return
        if gtkobj is self.scalar_output_button:
            self.output_obj = self.scalar_output_obj
            self.aggregate_output_obj.gtk.hide()
            self.scalar_output_obj.show()
        else:
            self.output_obj = self.aggregate_output_obj
            self.scalar_output_obj.gtk.hide()
            self.aggregate_output_obj.show()
        self.op_obj.refresh()
        self.sensitize_widgets()

    def updateOperations(self, gtkobj):
        self.op_obj.refresh()
        self.sensitize_widgets()

    def scalarMode(self):
        return self.output_obj is self.scalar_output_obj
    def aggregateMode(self):
        return self.output_obj is self.aggregate_output_obj
        
    # Switchboard, ("new who", "Mesh")
    def new_mesh(self, mesh):
        path = labeltree.makePath(mesh)
        self.meshwidget.set_value(path)
        self.sensitize_widgets()

    def new_skel(self, skeleton):       # switchboard ("new who", "Skeleton")
        # Switch automatically to a new Skeleton only if there is no
        # current Mesh.
        if not self.meshwidget.get_value(): # no mesh
            self.meshwidget.set_value(skeleton)

    # Callback from "operation" registered callback.
    def newOperationCB(self, registration):
        self.sensitize_widgets()

    def newDomainCB(self, registration):
        self.sensitize_widgets()

    def newSampleCB(self, registration):
        self.sensitize_widgets()

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # Manipulation of named analyses.

    def setNamedAnalysisChooser(self, *args):
        # Display the name for the current analysis if the current
        # settings happen to match a named analysis.  Call this
        # whenever anything on the page changes.
        
        # TODO: Just creating a Microstructure or Skeleton generates 9
        # calls to setNamedAnalysisChooser, which seems like a lot.
        # This checks the oldname and whether the chooser state has
        # actually changed before issuing a checkpoint, but a better
        # solution would be to figure out why the function is being
        # called so often, and to fix it.

        oldname = self.namedAnalysisChooser.get_value()
        
        self.namedAnalysisChooser.update(namedanalysis.bulkAnalysisNames())

        # If the get_value calls fail, the widgets aren't in a valid
        # state, and therefore there's no current name.
        # findNamedBulkAnalysis returns None if it can't find a match.
        try:
            currentname = namedanalysis.findNamedBulkAnalysis(
                self.op_obj.get_value(),
                self.output_obj.get_value(),
                self.domain_obj.get_value(),
                self.sample_obj.get_value())
        except:
            currentname = None
        if currentname != oldname:
            self.namedAnalysisChooser.set_state(currentname)
            gtklogger.checkpoint("named analysis chooser set")

    def createCB(self, gtkobj):  # create a named analysis
        menuitem = analyzemenu.namedanalysismenu.Create
        if parameterwidgets.getParameters(menuitem.get_arg('name'),
                                          parentwindow=self.gtk.get_toplevel(),
                                          title='Name an analysis operation',
                                          scope=self):
            menuitem.callWithDefaults(
                operation=self.op_obj.get_value(),
                data=self.output_obj.get_value(),
                domain=self.domain_obj.get_value(),
                sampling=self.sample_obj.get_value())
        
    def deleteCB(self, gtkobj): # delete named analysis
        menuitem = analyzemenu.namedanalysismenu.Delete
        if parameterwidgets.getParameters(menuitem.get_arg('name'),
                                          parentwindow=self.gtk.get_toplevel(),
                                          title='Delete a named analysis',
                                          scope=self):
            menuitem.callWithDefaults()

    def retrieveCB(self, name): # retrieve named analysis
        if name:                        # can be empty
            menuitem = analyzemenu.namedanalysismenu.RetrieveNamedAnalysis
            menuitem.get_arg('name').value = name
            menuitem.callWithDefaults()

    # "Retrieve" means fetch a value from the store of named analyses
    # and put it into the widgets so that the user can use it or edit
    # it.

    def retrieve_analysis(self, name): # switchboard "retrieve analysis"
        assert name is not None
        analysis = namedanalysis.getNamedBulkAnalysis(name)
        for signal in self.namedAnalysisSignals:
            signal.block()
        try:
            self.op_obj.set(analysis.operation, interactive=False)
            if analysis.data.isScalarOutput():
                self.scalar_output_button.set_active(1) # sets output_obj
            elif analysis.data.isAggregateOutput():
                self.aggregate_output_button.set_active(1) # sets output_obj
            else:
                raise ooferror2.PyErrPyProgrammingError(
                    "Unclassifiable output?")
            self.output_obj.set_value(analysis.data)
            self.domain_obj.set(analysis.domain, interactive=False)
            self.sample_obj.set(analysis.sampling, interactive=False)
        finally:
            for signal in self.namedAnalysisSignals:
                signal.unblock()
        gtklogger.checkpoint("retrieved named analysis")
        # If this call was triggered by the namedAnalysisChooser,
        # setting the chooser's value is redundant but harmless. If
        # the call was triggered by a script, setting the chooser's
        # value is required.
        self.setNamedAnalysisChooser()

    def savenamedCB(self, gtkobj): # save named analysis defs to a file
        menuitem = analyzemenu.namedanalysismenu.SaveAnalysisDefs
        if parameterwidgets.getParameters(title="Save Analysis Definitions",
                                          ident="SaveAnalysis",
                                          parentwindow=self.gtk.get_toplevel(),
                                          *menuitem.params):
            menuitem.callWithDefaults()

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # "Go" button callback -- fill in the basic parameters, and
    # perform the action.
    def go_buttonCB(self, gtkobj):
        op_reg = self.op_obj.get_value()
        regname = op_reg.getRegistration().name()
        menuitem = analyzemenu.ops_menu.getItem(
            utils.space2underscore(regname))

        menuitem.callWithDefaults(mesh=self.meshwidget.get_value(),
                                  time=self.timeWidget.get_value(),
                                  data=self.output_obj.get_value(),
                                  domain=self.domain_obj.get_value(),
                                  sampling=self.sample_obj.get_value(),
                                  destination=self.destwidget.get_value())
        

        
analyzepage = AnalyzePage()
