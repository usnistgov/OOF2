# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common.IO import reporter
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
from ooflib.engine.IO import scheduledoutput
from ooflib.engine.IO import scheduledoutputmenu
import ooflib.engine.mesh

from gi.repository import GObject
from gi.repository import Gtk

outputmenu = scheduledoutputmenu.outputmenu

## TODO: It would be nice to have tooltips on the cells in the
## TreeView, so that if a cell is too small to show all of its text,
## the full text can appear in the tooltip.

class OutputPage(oofGUI.MainPage):
    def __init__(self):
        oofGUI.MainPage.__init__(
            self, name="Scheduled Output", ordering=236,
            tip="Set output quantities to be computed during time evolution.")
        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=3,
                            halign=Gtk.Align.CENTER, margin_top=2)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        self.meshwidget = whowidget.WhoWidget(ooflib.engine.mesh.meshes,
                                              scope=self)
        switchboard.requestCallbackMain(self.meshwidget, self.meshCB)
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

        mainbox.pack_start(
            Gtk.Label("Skip this page if you're only solving static problems.",
                      halign=Gtk.Align.CENTER),
            expand=False, fill=False, padding=2)

        # Buttons along the top: New, Delete All, Rewind All
        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       halign=Gtk.Align.CENTER)
        mainbox.pack_start(bbox, expand=False, fill=False, padding=0)
        # New
        self.newOutputButton = gtkutils.StockButton('document-new-symbolic',
                                                    "New")
        gtklogger.setWidgetName(self.newOutputButton, "New")
        gtklogger.connect(self.newOutputButton, 'clicked', self.newOutputCB)
        bbox.pack_start(self.newOutputButton, expand=True, fill=True, padding=0)
        self.newOutputButton.set_tooltip_text("Define a new output operation.")
        # Delete All
        self.deleteAllButton = gtkutils.StockButton('edit-delete-symbolic',
                                                    "Delete All")
        gtklogger.setWidgetName(self.deleteAllButton, "DeleteAll")
        gtklogger.connect(self.deleteAllButton, 'clicked', self.deleteAllCB)
        bbox.pack_start(self.deleteAllButton, expand=True, fill=True, padding=0)
        self.deleteAllButton.set_tooltip_text("Delete all output operations")
        # Rewind All
        self.rewindAllDestsButton = gtkutils.StockButton(
            'media-seek-backward-symbolic', "Rewind All")
        gtklogger.setWidgetName(self.rewindAllDestsButton, "RewindAll")
        gtklogger.connect(self.rewindAllDestsButton, 'clicked',
                          self.rewindAllDestinationsCB)
        bbox.pack_start(self.rewindAllDestsButton,
                        expand=True, fill=True, padding=0)
        self.rewindAllDestsButton.set_tooltip_text(
            "Go back to the start of all output files.")

        self.outputList = Gtk.ListStore(GObject.TYPE_PYOBJECT)

        # TreeView listing all of the scheduled Outputs
        scrollWindow = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN,
                                          margin_start=2, margin_end=2)
        mainbox.pack_start(scrollWindow, expand=True, fill=True, padding=0)
        self.outputView = Gtk.TreeView(self.outputList)
        self.outputView.set_grid_lines(Gtk.TreeViewGridLines.VERTICAL)
        gtklogger.setWidgetName(self.outputView, "list")
        scrollWindow.add(self.outputView)
        gtklogger.connect(self.outputView, 'row-activated',
                          self.outputDoubleClickCB)

        # Check box for enabling/disabling an Output
        self.enableCell = Gtk.CellRendererToggle()
        enableCol = Gtk.TreeViewColumn()
        enableCol.set_resizable(False)
        enableCol.pack_start(self.enableCell, expand=False)
        enableCol.set_cell_data_func(self.enableCell, self.renderEnableCell)
        self.outputView.append_column(enableCol)
        gtklogger.adoptGObject(self.enableCell, self.outputView,
                               access_function=gtklogger.findCellRenderer,
                               access_kwargs=dict(col=0,rend=0))
        gtklogger.connect(self.enableCell, 'toggled', self.enableCellCB)

        # Name of the Output
        outputCell = Gtk.CellRendererText()
        self.outputCol= Gtk.TreeViewColumn("Output")
        self.outputCol.set_resizable(True)
        self.outputCol.pack_start(outputCell, expand=True)
        self.outputCol.set_cell_data_func(outputCell, self.renderOutputCell)
        self.outputView.append_column(self.outputCol)

        # Output Schedule
        schedCell = Gtk.CellRendererText()
        self.schedCol = Gtk.TreeViewColumn("Schedule")
        self.schedCol.set_resizable(True)
        self.schedCol.pack_start(schedCell, expand=True)
        self.schedCol.set_cell_data_func(schedCell, self.renderSchedule)
        self.outputView.append_column(self.schedCol)

        # Destination
        destCell = Gtk.CellRendererText()
        self.destCol = Gtk.TreeViewColumn("Destination")
        self.destCol.set_resizable(True)
        self.destCol.pack_start(destCell, expand=True)
        self.destCol.set_cell_data_func(destCell, self.renderDestination)
        self.outputView.append_column(self.destCol)

        # Buttons for operating on the selected output

        masterButtonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                  margin=2)
        mainbox.pack_start(masterButtonBox, expand=False, fill=False, padding=0)

        outputBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        masterButtonBox.pack_start(outputBox,
                                   expand=True, fill=False, padding=0)
        outputBox.pack_start(Gtk.Label("Output", halign=Gtk.Align.CENTER),
                           expand=False, fill=False, padding=0)
        grid = Gtk.Grid(row_homogeneous=True, column_homogeneous=True)
        outputBox.pack_start(grid, expand=False, fill=False, padding=0)
        
        # Edit output
        self.editOutputButton = gtkutils.StockButton(
            "document-edit-symbolic", "Edit")
        gtklogger.connect(self.editOutputButton, 'clicked', self.editOutputCB)
        gtklogger.setWidgetName(self.editOutputButton, 'EditOutput')
        grid.attach(self.editOutputButton, 0,0, 1,1)
        self.editOutputButton.set_tooltip_text(
            "Redefine or rename the selected output operation.")

        # Rename output
        self.renameOutputButton = gtkutils.StockButton('document-edit-symbolic',
                                                       "Rename")
        gtklogger.setWidgetName(self.renameOutputButton, "Rename")
        gtklogger.connect(self.renameOutputButton, 'clicked', self.renameCB)
        grid.attach(self.renameOutputButton, 0,1, 1,1)
        self.renameOutputButton.set_tooltip_text(
            "Rename the selected output operation.")

        # Copy output
        self.copyOutputButton = gtkutils.StockButton(
            "edit-copy-symbolic", "Copy")
        gtklogger.setWidgetName(self.copyOutputButton, "CopyOutput")
        gtklogger.connect(self.copyOutputButton, 'clicked', self.copyOutputCB)
        grid.attach(self.copyOutputButton, 1,0, 1,1)
        self.copyOutputButton.set_tooltip_text(
            "Copy the selected output and its schedule and destination.")

        # Delete output
        self.deleteOutputButton = gtkutils.StockButton(
            'edit-delete-symbolic', "Delete")
        gtklogger.setWidgetName(self.deleteOutputButton, "DeleteOutput")
        gtklogger.connect(self.deleteOutputButton, 'clicked',
                          self.deleteOutputCB)
        grid.attach(self.deleteOutputButton, 1,1, 1,1)
        self.deleteOutputButton.set_tooltip_text(
            "Delete the selected output operation.")

        scheduleBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        masterButtonBox.pack_start(scheduleBox,
                                   expand=True, fill=False, padding=0)
        scheduleBox.pack_start(Gtk.Label("Schedule", halign=Gtk.Align.CENTER),
                               expand=False, fill=False, padding=0)
        grid = Gtk.Grid(row_homogeneous=True, column_homogeneous=True)
        scheduleBox.pack_start(grid, expand=False, fill=False, padding=0)

        # Set/edit schedule
        self.editScheduleButton = gtkutils.StockButton(
            'document-edit-symbolic', "Edit")
        gtklogger.setWidgetName(self.editScheduleButton, "NewSchedule")
        gtklogger.connect(self.editScheduleButton, 'clicked', self.editSchedCB)
        grid.attach(self.editScheduleButton, 0,0, 1,1)
        self.editScheduleButton.set_tooltip_text(
            "Add a Schedule to the selected Output")

        # Copy schedule
        self.copyScheduleButton = gtkutils.StockButton(
            'edit-copy-symbolic', "Copy")
        gtklogger.setWidgetName(self.copyScheduleButton, "CopySchedule")
        gtklogger.connect(self.copyScheduleButton, 'clicked', self.copySchedCB)
        grid.attach(self.copyScheduleButton, 0,1, 1,1)
        self.copyScheduleButton.set_tooltip_text(
            "Copy the selected Schedule to another Output")

        destBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        masterButtonBox.pack_start(destBox,
                                   expand=True, fill=False, padding=0)
        destBox.pack_start(Gtk.Label("Destination", halign=Gtk.Align.CENTER),
                               expand=False, fill=False, padding=0)
        grid = Gtk.Grid(row_homogeneous=True, column_homogeneous=True)
        destBox.pack_start(grid, expand=False, fill=False, padding=0)

        # Set destination
        self.editDestinationButton = gtkutils.StockButton(
            'document-edit-symbolic', "Edit")
        gtklogger.setWidgetName(self.editDestinationButton, "Set")
        gtklogger.connect(self.editDestinationButton, 'clicked',
                          self.editDestinationCB)
        grid.attach(self.editDestinationButton, 0,0, 1,1)
        self.editDestinationButton.set_tooltip_text(
            "Assign a destination to the selected Output")

        # Rewind destination
        self.rewindDestButton = gtkutils.StockButton(
            'media-seek-backward-symbolic', "Rewind")
        gtklogger.setWidgetName(self.rewindDestButton, "Rewind")
        gtklogger.connect(self.rewindDestButton, 'clicked',
                          self.rewindDestinationCB)
        grid.attach(self.rewindDestButton, 0,1, 1,1)
        self.rewindDestButton.set_tooltip_text(
            "Go back to the start of the output file.")

g        
        # This is a hack.  Some of the dialogs use widgets that need
        # to find out what the current Output is, using the
        # WidgetScope mechanism.  The TreeView isn't a
        # ParameterWidget, so it doesn't use WidgetScopes.  So here we
        # construct a ParameterWidget just so that it can be found.
        # It's kept up to date with the selected Output.  It's not
        # actually placed in the GUI.
        self.dummyOutputParam = parameter.RegisteredParameter(
            'output', scheduledoutput.ScheduledOutput)
        self.dummyOutputWidget = self.dummyOutputParam.makeWidget(scope=self)

        gtklogger.adoptGObject(self.outputView.get_selection(),
                               self.outputView,
                               access_method=self.outputView.get_selection)
        self.selectionsignal = gtklogger.connect(
            self.outputView.get_selection(), 'changed', self.selectionCB)

        switchboard.requestCallbackMain("scheduled outputs changed",
                                        self.outputsChangedCB)
        switchboard.requestCallbackMain("new scheduled output",
                                        self.newOutputSBCB)

        

        
    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # TreeView rendering methods
    
    def renderEnableCell(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        output = model[iter][0]
        cell_renderer.set_active(output.active)

    def enableCellCB(self, cell_renderer, path):
        debug.mainthreadTest()
        output = self.outputList[path][0]
        outputmenu.Enable(mesh=self.currentFullMeshName(),
                          output=output.name(),
                          enable=(not output.active))

    def renderOutputCell(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        output = model[iter][0]
        cell_renderer.set_property('text', output.name())

    def renderSchedule(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        output = model[iter][0]
        if output.schedule is not None:
            cell_renderer.set_property(
                'text',
                output.scheduleType.shortrepr()+ "/" +
                output.schedule.shortrepr())
        else:
            cell_renderer.set_property('text', '---')

    def renderDestination(self, column, cell_renderer, model, iter, data):
        debug.mainthreadTest()
        output = model[iter][0]
        if output.destination is not None:
            cell_renderer.set_property('text', output.destination.shortrepr())
        else:
            cell_renderer.set_property('text', '---')

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    def outputsChangedCB(self, meshctxt):
        # switchboard "scheduled outputs changed"
        if meshctxt is self.currentMeshContext():
            self.update()
            self.sensitize()

    def newOutputSBCB(self, meshctxt, outputname):
        # switchboard "new scheduled output"
        if meshctxt is self.currentMeshContext():
            self.update()
            self.selectOutput(outputname)
            self.sensitize()

    def meshCB(self, *args, **kwargs): # mesh widget changed state
        self.update()
        self.sensitize()

    def currentFullMeshName(self):
        return self.meshwidget.get_value()
    
    def currentMeshName(self):
        path = labeltree.makePath(self.currentFullMeshName())
        if path:
            return path[2]
        
    def currentMeshContext(self):
        try:
            return ooflib.engine.mesh.meshes[self.currentFullMeshName()]
        except KeyError:
            return None

    def currentMesh(self):
        ctxt = self.currentMeshContext()
        if ctxt:
            return ctxt.getObject()

    def currentOutput(self):
        debug.mainthreadTest()
        selection = self.outputView.get_selection()
        model, iter = selection.get_selected()
        if iter:
            return model[iter][0]

    def currentOutputName(self):
        o = self.currentOutput()
        if o:
            return o.name()


    def update(self):
        # update() does *not* call sensitize(), because there are some
        # cases in which other things need to be done first.  Any
        # function that calls update() should probably call
        # sensitize() too.
        debug.mainthreadTest()
        meshctxt = self.currentMeshContext()
        current = self.currentOutputName()
        # It's important to block the selection signals while clearing
        # the list, or else gtklogger will log the deselection of the
        # current selection.  Since selectOutput() blocks the signals,
        # the reselection won't be logged, and the next operation on
        # the selection will fail when a log script is replayed.
        
        self.selectionsignal.block()
        self.outputList.clear()
        self.selectionsignal.unblock()
        if meshctxt is not None:
            for output in meshctxt.outputSchedule.outputs:
                it = self.outputList.append([output])
            self.selectOutput(current)
        
    def selectOutput(self, name):
        for rowno, row in enumerate(self.outputList):
            # row is a TreeModelRow object. row[0] is a ScheduledOutput
            if row[0].name() == name:
                selection = self.outputView.get_selection()
                self.selectionsignal.block()
                try:
                    selection.select_path(rowno)
                finally:
                    self.selectionsignal.unblock()
                self.outputView.scroll_to_cell(rowno)
                self.dummyOutputWidget.set(row[0], interactive=False)
                return

    def sensitize(self):
        debug.mainthreadTest()
        meshok = self.currentMeshContext() is not None
        output = self.currentOutput()
        outputok = output is not None
        outputsExist = (meshok and 
                        self.currentMeshContext().outputSchedule.nOutputs() > 0)

        self.newOutputButton.set_sensitive(meshok)
        self.deleteAllButton.set_sensitive(outputsExist)
        self.rewindAllDestsButton.set_sensitive(outputsExist)

        self.editOutputButton.set_sensitive(outputok)
        self.copyOutputButton.set_sensitive(outputok)
        self.deleteOutputButton.set_sensitive(outputok)
        self.renameOutputButton.set_sensitive(outputok)

        scheduleok = outputok and output.schedule is not None
        self.editScheduleButton.set_sensitive(outputok)
        self.copyScheduleButton.set_sensitive(scheduleok)

        destinationok = (outputok and output.settableDestination and
                         output.destination is not None)
        self.editDestinationButton.set_sensitive(outputok and
                                                output.settableDestination)
        self.rewindDestButton.set_sensitive(
            destinationok and output.destination.getRegistration().rewindable)
        
    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

    # TreeView callbacks

    def selectionCB(self, treeselection):
        debug.mainthreadTest()
        model, iterator = treeselection.get_selected()
        if iterator:
            self.dummyOutputWidget.set(self.currentOutput(), interactive=False)

        self.sensitize()

    def outputDoubleClickCB(self, treeview, path, col):
        if col is self.outputCol:
            self.editOutputCB()
        elif col is self.schedCol:
            self.editSchedCB()
        elif col is self.destCol:
            self.editDestinationCB()

    #=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
        
    ## Button callbacks

    def newOutputCB(self, gtkbutton):
        # Create a new scheduled output
        menuitem = outputmenu.New
        params = filter(lambda a: a.name != 'mesh', menuitem.params)
        if parameterwidgets.getParameters(title='Define a new Output',
                                          scope=self,
                                          parentwindow=guitop.top().gtk,
                                          *params):
            menuitem.callWithDefaults(mesh=self.currentFullMeshName())
    
    def deleteAllCB(self, gtkbutton):
        if reporter.query("Really delete all scheduled outputs?", "Yes", "No") \
           == "Yes":
            outputmenu.DeleteAll.callWithDefaults(
                mesh=self.currentFullMeshName())

    def rewindAllDestinationsCB(self, gtkbutton):
        menuitem = outputmenu.Destination.RewindAll
        menuitem.callWithDefaults(mesh=self.currentFullMeshName())

    def editOutputCB(self, *args):
        menuitem = outputmenu.Edit
        output = self.currentOutput()
        newoutputparam = menuitem.get_arg('new_output')
        newoutputparam.set(output)
        params = filter(lambda a: a.name not in ('mesh', 'output'), 
                        menuitem.params)
        if parameterwidgets.getParameters(title='Redefine an Output',
                                          scope=self,
                                          parentwindow=guitop.top().gtk,
                                          *params):
            menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                      output=self.currentOutputName())

    def renameCB(self, gtkbutton):
        menuitem = outputmenu.Rename
        nameparam = menuitem.get_arg('name')
        name = self.currentOutputName()
        nameparam.set(name)
        if parameterwidgets.getParameters(nameparam,
                                          title='Rename output "%s"'%name,
                                          scope=self,
                                          parentwindow=guitop.top().gtk):
            menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                      output=self.currentOutputName())
            
    def copyOutputCB(self, gtkbutton):
        menuitem = outputmenu.Copy
        output = self.currentOutput()
        targetmeshparam = menuitem.get_arg('targetmesh')
        targetmeshparam.set(self.currentFullMeshName())
        if parameterwidgets.getParameters(targetmeshparam,
                                          menuitem.get_arg('copy'),
                                          scope=self,
                                          title="Copy an Output",
                                          parentwindow=guitop.top().gtk):
            menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                      source=self.currentOutputName())
    def deleteOutputCB(self, gtkbutton):
        outputmenu.Delete.callWithDefaults(mesh=self.currentFullMeshName(),
                                           output=self.currentOutputName())

    def editSchedCB(self, *args):
        menuitem = outputmenu.Schedule.Set
        schedparam = menuitem.get_arg('schedule')
        schedtypeparam = menuitem.get_arg('scheduletype')
        if self.currentOutput().schedule is not None:
            schedparam.set(self.currentOutput().schedule)
            schedtypeparam.set(self.currentOutput().scheduleType)
        if parameterwidgets.getParameters(schedtypeparam, schedparam,
                                          parentwindow=guitop.top().gtk,
                                          title='Set an Output Schedule',
                                          scope=self):
            menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                      output=self.currentOutputName())
    def copySchedCB(self, gtkbutton):
        menuitem = outputmenu.Schedule.Copy
        targetmeshparam = menuitem.get_arg('targetmesh')
        targetmeshparam.set(self.currentFullMeshName())
        targetparam = menuitem.get_arg('target')
        if parameterwidgets.getParameters(targetmeshparam, targetparam,
                                          parentwindow=guitop.top().gtk,
                                          title="Copy an Output Schedule",
                                          scope=self):
            menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                      source=self.currentOutputName())

    def editDestinationCB(self, *args):
        assert self.currentOutput() is not None
        menuitem = outputmenu.Destination.Set
        destparam = menuitem.get_arg('destination')
        if self.currentOutput().destination is not None:
            destparam.set(self.currentOutput().destination)
        if parameterwidgets.getParameters(destparam,
                                          parentwindow=guitop.top().gtk,
                                          title='Set an Output Destination',
                                          scope=self):
            menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                      output=self.currentOutputName())
    def rewindDestinationCB(self, gtkbutton):
        menuitem = outputmenu.Destination.Rewind
        menuitem.callWithDefaults(mesh=self.currentFullMeshName(),
                                  output=self.currentOutputName())

op = OutputPage()
