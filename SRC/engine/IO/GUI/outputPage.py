# -*- python -*-
# $RCSfile: outputPage.py,v $
# $Revision: 1.15 $
# $Author: langer $
# $Date: 2011/04/21 21:34:55 $

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
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import tooltips
from ooflib.common.IO.GUI import whowidget
from ooflib.engine.IO import scheduledoutput
from ooflib.engine.IO import scheduledoutputmenu
import ooflib.engine.mesh

import gobject
import gtk

outputmenu = scheduledoutputmenu.outputmenu

## TODO: Create an output using an OutputStream.  Clear the
## destination list on the Analysis or Bdy Analysis pages.  What
## should happen to the OutputStream on this page?

class OutputPage(oofGUI.MainPage):
    def __init__(self):
        oofGUI.MainPage.__init__(
            self, name="Scheduled Output", ordering=235,
            tip="Set output quantities to be computed during time evolution.")
        mainbox = gtk.VBox(spacing=2)
        self.gtk.add(mainbox)

        align = gtk.Alignment(xalign=0.5)
        mainbox.pack_start(align, expand=0, fill=0)
        centerbox = gtk.HBox(spacing=3)
        align.add(centerbox)
        self.meshwidget = whowidget.WhoWidget(ooflib.engine.mesh.meshes,
                                              scope=self)
        switchboard.requestCallbackMain(self.meshwidget, self.meshCB)
        label = gtk.Label("Microstructure=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.meshwidget.gtk[0], expand=0, fill=0)

        label = gtk.Label("Skeleton=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.meshwidget.gtk[1], expand=0, fill=0)

        label = gtk.Label("Mesh=")
        label.set_alignment(1.0, 0.5)
        centerbox.pack_start(label, expand=0, fill=0)
        centerbox.pack_start(self.meshwidget.gtk[2], expand=0, fill=0)

        align = gtk.Alignment(xalign=0.5)
        mainbox.pack_start(align, expand=0, fill=0, padding=3)
        align.add(gtk.Label(
                "Skip this page if you're only solving static problems."))

        # The four columns (enable, output, schedule, and destination)
        # are each displayed in their own gtk.TreeView, each of which
        # is in a pane of a gtk.HPaned.  It would have been better to
        # put each column in a different gtk.TreeViewColumn in the
        # same gtk.TreeView, but that would have made it hard to put
        # buttons at the bottom of each column.

        hpane0 = gtk.HPaned()
        gtklogger.setWidgetName(hpane0, 'HPane0')
        gtklogger.connect_passive(hpane0, 'notify::position')
        mainbox.pack_start(hpane0, expand=1, fill=1)

        hpaneL = gtk.HPaned()
        gtklogger.setWidgetName(hpaneL, 'HPaneL')
        gtklogger.connect_passive(hpaneL, 'notify::position')
        hpane0.pack1(hpaneL, resize=True, shrink=False)

        hpaneR = gtk.HPaned()
        gtklogger.setWidgetName(hpaneR, 'HPane2')
        gtklogger.connect_passive(hpaneR, 'notify::position')
        hpane0.pack2(hpaneR, resize=True, shrink=False)

        self.outputList = gtk.ListStore(gobject.TYPE_PYOBJECT)

        # The "Enable" column has a check box for each output
        self.enableFrame = gtk.Frame()
        self.enableFrame.set_shadow_type(gtk.SHADOW_IN)
        hpaneL.pack1(self.enableFrame, resize=False, shrink=False)
        vbox = gtk.VBox()
        self.enableFrame.add(vbox)
        self.enableView = gtk.TreeView(self.outputList)
        gtklogger.setWidgetName(self.enableView, "enable")
        vbox.pack_start(self.enableView, expand=True, fill=True)
        self.enablecell = gtk.CellRendererToggle()
        enablecol = gtk.TreeViewColumn("")
        enablecol.set_resizable(False)
        enablecol.pack_start(self.enablecell, expand=False)
        enablecol.set_cell_data_func(self.enablecell, self.renderEnableCell)
        self.enableView.append_column(enablecol)
        gtklogger.adoptGObject(self.enablecell, self.enableView,
                               access_function=gtklogger.findCellRenderer,
                               access_kwargs={'col':0, 'rend':0})
        gtklogger.connect(self.enablecell, 'toggled', self.enableCellCB)
        # Extra space at the bottom of the column.  The other columns
        # have button boxes at the bottom, so this one needs a strut
        # to keep its rows aligned with the others.
        self.enableStrut = gtk.VBox()
        vbox.pack_start(self.enableStrut, expand=False, fill=False)
        
        # The "Output" pane lists the name of each output
        self.outputFrame = gtk.Frame()
        self.outputFrame.set_shadow_type(gtk.SHADOW_IN)
        gtklogger.setWidgetName(self.outputFrame, "Output")
        hpaneL.pack2(self.outputFrame, resize=True, shrink=False)
        outputVBox = gtk.VBox()
        self.outputFrame.add(outputVBox)
        self.outputView = gtk.TreeView(self.outputList)
        gtklogger.setWidgetName(self.outputView, "list")
        outputVBox.pack_start(self.outputView, expand=True, fill=True)
        self.outputHScroll = gtk.HScrollbar()
        outputVBox.pack_start(self.outputHScroll, expand=False, fill=False)
        self.outputView.set_hadjustment(self.outputHScroll.get_adjustment())
        self.outputcell = gtk.CellRendererText()
        outputcol = gtk.TreeViewColumn("Output")
        outputcol.pack_start(self.outputcell, expand=True)
        outputcol.set_cell_data_func(self.outputcell, self.renderOutputCell)
        self.outputView.append_column(outputcol)
        gtklogger.connect(self.outputView, 'row-activated',
                          self.outputDoubleClickCB)
        # Buttons for the Output pane.  The extra VBox is used so that
        # the sizes of the button boxes can be synchronized.
        self.outputBBox = gtk.VBox(homogeneous=True)
        outputVBox.pack_start(self.outputBBox, expand=False, fill=False)
        bbox = gtk.HBox(homogeneous=False)
        self.outputBBox.pack_start(bbox, expand=True, fill=True)
        # New Output
        self.newOutputButton = gtkutils.StockButton(gtk.STOCK_NEW, "New")
        gtklogger.setWidgetName(self.newOutputButton, "New")
        gtklogger.connect(self.newOutputButton, 'clicked', self.newOutputCB)
        bbox.pack_start(self.newOutputButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.newOutputButton,
                             "Define a new output operation.")
        # Edit Output
        self.editOutputButton = gtkutils.StockButton(gtk.STOCK_EDIT, "Edit")
        gtklogger.setWidgetName(self.editOutputButton, "Edit")
        gtklogger.connect(self.editOutputButton, 'clicked', self.editOutputCB)
        bbox.pack_start(self.editOutputButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.editOutputButton,
                             "Redefine the selected output operation.")
        # Copy Output
        self.copyOutputButton = gtkutils.StockButton(gtk.STOCK_COPY, "Copy")
        gtklogger.setWidgetName(self.copyOutputButton, "Copy")
        gtklogger.connect(self.copyOutputButton, 'clicked', self.copyOutputCB)
        bbox.pack_start(self.copyOutputButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.copyOutputButton,
            "Copy the selected output and its schedule and destination.")
        # Second row of buttons
        bbox = gtk.HBox(homogeneous=False)
        self.outputBBox.pack_start(bbox, expand=True, fill=True)
        # Rename Output
        self.renameOutputButton = gtkutils.StockButton(gtk.STOCK_EDIT, "Rename")
        gtklogger.setWidgetName(self.renameOutputButton, "Rename")
        gtklogger.connect(self.renameOutputButton, 'clicked', self.renameCB)
        bbox.pack_start(self.renameOutputButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.renameOutputButton,
                             "Rename the selected output operation.")
        # Delete Output
        self.deleteOutputButton = gtkutils.StockButton(gtk.STOCK_DELETE, 
                                                       "Delete")
        gtklogger.setWidgetName(self.deleteOutputButton, "Delete")
        gtklogger.connect(self.deleteOutputButton, 'clicked',
                          self.deleteOutputCB)
        tooltips.set_tooltip_text(self.deleteOutputButton,
                             "Delete the selected output operation.")
        bbox.pack_start(self.deleteOutputButton, expand=True, fill=True)
        # Delete all outputs
        self.deleteAllButton = gtkutils.StockButton(gtk.STOCK_DELETE,
                                                    "Delete All")
        gtklogger.setWidgetName(self.deleteAllButton, "DeleteAll")
        gtklogger.connect(self.deleteAllButton, 'clicked', self.deleteAllCB)
        bbox.pack_start(self.deleteAllButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.deleteAllButton,
                             "Delete all output operations")
        

        # Schedule pane
        self.schedFrame = gtk.Frame()
        self.schedFrame.set_shadow_type(gtk.SHADOW_IN)
        gtklogger.setWidgetName(self.schedFrame, "Schedule")
        hpaneR.pack1(self.schedFrame, resize=True, shrink=False)
        scheduleVBox = gtk.VBox()
        self.schedFrame.add(scheduleVBox)
        self.schedView = gtk.TreeView(self.outputList)
        gtklogger.setWidgetName(self.schedView, "list")
        scheduleVBox.pack_start(self.schedView, expand=True, fill=True)
        schedHScroll = gtk.HScrollbar()
        scheduleVBox.pack_start(schedHScroll, expand=False, fill=False)
        self.schedView.set_hadjustment(schedHScroll.get_adjustment())
        self.schedcell = gtk.CellRendererText()
        schedcol = gtk.TreeViewColumn("Schedule")
        schedcol.pack_start(self.schedcell, expand=True)
        schedcol.set_cell_data_func(self.schedcell, self.renderScheduleCB)
        self.schedView.append_column(schedcol)
        gtklogger.connect(self.schedView, 'row-activated',
                          self.schedDoubleClickCB)
        # Buttons for the Schedule pane.  
        self.schedBBox = gtk.VBox(homogeneous=True)
        scheduleVBox.pack_start(self.schedBBox, expand=False, fill=False)
        bbox = gtk.HBox(homogeneous=False)
        self.schedBBox.pack_start(bbox, expand=True, fill=True)
        # Set Schedule
        self.setScheduleButton = gtkutils.StockButton(gtk.STOCK_NEW, "Set")
        gtklogger.setWidgetName(self.setScheduleButton, "New")
        gtklogger.connect(self.setScheduleButton, 'clicked', self.setSchedCB)
        bbox.pack_start(self.setScheduleButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.setScheduleButton,
                             "Add a Schedule to the selected Output")
        # Copy Schedule
        self.copyScheduleButton = gtkutils.StockButton(gtk.STOCK_COPY, "Copy")
        gtklogger.setWidgetName(self.copyScheduleButton, "Copy")
        gtklogger.connect(self.copyScheduleButton, 'clicked', self.copySchedCB)
        bbox.pack_start(self.copyScheduleButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.copyScheduleButton,
                             "Copy the selected Schedule to another Output")
        # Second row of buttons in the Schedule pane
        bbox = gtk.HBox(homogeneous=False)
        self.schedBBox.pack_start(bbox, expand=True, fill=True)
        # Delete Schedule
        self.deleteScheduleButton = gtkutils.StockButton(gtk.STOCK_DELETE,
                                                         "Delete")
        gtklogger.setWidgetName(self.deleteScheduleButton, "Delete")
        gtklogger.connect(self.deleteScheduleButton, 'clicked',
                          self.deleteSchedCB)
        bbox.pack_start(self.deleteScheduleButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.deleteScheduleButton,
                             "Delete the selected Schedule.")
        

        # Destination pane
        self.destFrame = gtk.Frame()
        self.destFrame.set_shadow_type(gtk.SHADOW_IN)
        gtklogger.setWidgetName(self.destFrame, "Destination")
        hpaneR.pack2(self.destFrame, resize=True, shrink=False)
        destVBox = gtk.VBox()
        self.destFrame.add(destVBox)
        destScroll = gtk.ScrolledWindow()
        destScroll.set_shadow_type(gtk.SHADOW_NONE)
        destScroll.set_policy(gtk.POLICY_ALWAYS, gtk.POLICY_ALWAYS)
        destVBox.pack_start(destScroll, expand=True, fill=True)
        self.destView = gtk.TreeView(self.outputList)
        gtklogger.setWidgetName(self.destView, "list")
        destScroll.add(self.destView)
        self.destcell = gtk.CellRendererText()
        destcol = gtk.TreeViewColumn("Destination")
        destcol.pack_start(self.destcell, expand=True)
        destcol.set_cell_data_func(self.destcell, self.renderDestinationCB)
        self.destView.append_column(destcol)
        gtklogger.connect(self.destView, 'row-activated',
                          self.destDoubleClickCB)
        # Buttons for the Destination pane
        self.destBBox = gtk.VBox(homogeneous=True)
        destVBox.pack_start(self.destBBox, expand=False, fill=True)
        bbox = gtk.HBox(homogeneous=False)
        self.destBBox.pack_start(bbox, expand=True, fill=True)
        # Set Destination
        self.setDestinationButton = gtkutils.StockButton(gtk.STOCK_NEW, "Set")
        gtklogger.setWidgetName(self.setDestinationButton, "Set")
        gtklogger.connect(self.setDestinationButton, 'clicked',
                          self.setDestinationCB)
        bbox.pack_start(self.setDestinationButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.setDestinationButton,
                             "Assign a destination to the selected Output")
        # Delete Dest
        self.deleteDestButton = gtkutils.StockButton(gtk.STOCK_DELETE,
                                                         "Delete")
        gtklogger.setWidgetName(self.deleteDestButton, "Delete")
        gtklogger.connect(self.deleteDestButton, 'clicked',
                          self.deleteDestCB)
        bbox.pack_start(self.deleteDestButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.deleteDestButton,
                             "Delete the selected Destination.")
        # Second row of buttons in the Dest pane
        bbox = gtk.HBox(homogeneous=False)
        self.destBBox.pack_start(bbox, expand=True, fill=True)
        # Rewind
        self.rewindDestButton = gtkutils.StockButton(gtk.STOCK_MEDIA_REWIND,
                                                     "Rewind")
        gtklogger.setWidgetName(self.rewindDestButton, "Rewind")
        gtklogger.connect(self.rewindDestButton, 'clicked',
                          self.rewindDestinationCB)
        bbox.pack_start(self.rewindDestButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.rewindDestButton,
                             "Go back to the start of the output file.")
        # Rewind All
        self.rewindAllDestsButton = gtkutils.StockButton(gtk.STOCK_MEDIA_REWIND,
                                                         "Rewind All")
        gtklogger.setWidgetName(self.rewindAllDestsButton, "RewindAll")
        gtklogger.connect(self.rewindAllDestsButton, 'clicked',
                          self.rewindAllDestinationsCB)
        bbox.pack_start(self.rewindAllDestsButton, expand=True, fill=True)
        tooltips.set_tooltip_text(self.rewindAllDestsButton,
                             "Go back to the start of all output files.")

        # Synchronize the vertical scrolling of all the panes.
        self.schedView.set_vadjustment(destScroll.get_vadjustment())
        self.outputView.set_vadjustment(destScroll.get_vadjustment())
        self.enableView.set_vadjustment(destScroll.get_vadjustment())


        self.allViews = (self.enableView, self.outputView, self.schedView,
                         self.destView)

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

        # Catch selection changes in the lists
        self.selectionsignals = {}
        for view in self.allViews:
            gtklogger.adoptGObject(view.get_selection(), view,
                                   access_method=view.get_selection)
            self.selectionsignals[view] = gtklogger.connect(
                view.get_selection(), 'changed', self.selectionCB)

        switchboard.requestCallbackMain("scheduled outputs changed",
                                        self.outputsChangedCB)
        switchboard.requestCallbackMain("new scheduled output",
                                        self.newOutputSBCB)

        switchboard.requestCallbackMain("gtk font changed", self.setSizes)


    def setSizes(self, *args):
        ## TODO: There's something wrong here.  If the font size
        ## is changed, the subwidgets don't resize properly.

        # Make the vertical size of each frame the same, and make the
        # minimum horizontal size the natural size of their button
        # boxes.
        vsize = self.destFrame.size_request()[1]
        self.outputFrame.set_size_request(self.outputBBox.size_request()[0],
                                          vsize)
        self.schedFrame.set_size_request(self.schedBBox.size_request()[0],
                                         vsize)
        self.destFrame.set_size_request(self.destBBox.size_request()[0], -1)
        self.enableFrame.set_size_request(-1, vsize)

        # make all button boxes the same height
        bsize = max(x.size_request()[1]
                    for x in (self.outputBBox, self.schedBBox, self.destBBox))
        self.outputBBox.set_size_request(-1, bsize)
        self.schedBBox.set_size_request(-1, bsize)
        self.destBBox.set_size_request(-1, bsize)
        self.enableStrut.set_size_request(
            -1, bsize+self.outputHScroll.size_request()[1])
        
        # Make all of the TreeViews have the same line height.
        xoff, yoff, width, height = self.outputcell.get_size(self.outputView)
        ypad = self.outputcell.get_property("ypad")
        height -= ypad
        self.enablecell.set_fixed_size(-1, height)
        self.outputcell.set_fixed_size(-1, height)
        self.schedcell.set_fixed_size(-1, height)
        self.destcell.set_fixed_size(-1, height)

    def installed(self):
        self.update()
        self.sensitize()
        self.setSizes()

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
        selection = self.allViews[0].get_selection()
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
        for signal in self.selectionsignals.values():
            signal.block()
        self.outputList.clear()
        for signal in self.selectionsignals.values():
            signal.unblock()
        if meshctxt is not None:
            for output in meshctxt.outputSchedule.outputs:
                it = self.outputList.append([output])
            self.selectOutput(current)

    def selectOutput(self, name):
        for rowno, row in enumerate(self.outputList):
            # row is a TreeModelRow object. row[0] is a ScheduledOutput
            if row[0].name() == name:
                for view, signal in self.selectionsignals.items():
                    selection = view.get_selection()
                    signal.block()
                    try:
                        selection.select_path(rowno)
                    finally:
                        signal.unblock()
                    view.scroll_to_cell(rowno)
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
        self.editOutputButton.set_sensitive(outputok)
        self.copyOutputButton.set_sensitive(outputok)
        self.renameOutputButton.set_sensitive(outputok)
        self.deleteOutputButton.set_sensitive(outputok)
        self.deleteAllButton.set_sensitive(outputsExist)

        scheduleok = outputok and output.schedule is not None
        self.setScheduleButton.set_sensitive(outputok)
        self.deleteScheduleButton.set_sensitive(scheduleok)
        self.copyScheduleButton.set_sensitive(scheduleok)

        destinationok = (outputok and output.settableDestination and
                         output.destination is not None)
        self.setDestinationButton.set_sensitive(outputok and
                                                output.settableDestination)
        self.deleteDestButton.set_sensitive(destinationok)
        self.rewindDestButton.set_sensitive(
            destinationok and output.destination.getRegistration().rewindable)
        self.rewindAllDestsButton.set_sensitive(outputsExist)

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

    ##############

    # TreeView selection and double click callbacks.  There's only one
    # selection callback because selections are synchronized.

    def selectionCB(self, treeselection):
        debug.mainthreadTest()
        model, iter = treeselection.get_selected()
        if iter:
            for view, signal in self.selectionsignals.items():
                if view.get_selection() is not treeselection:
                    signal.block()
                    try:
                        view.get_selection().select_iter(iter)
                    finally:
                        signal.unblock()
            self.dummyOutputWidget.set(self.currentOutput(), interactive=False)
        else:
            for view, signal in self.selectionsignals.items():
                if view.get_selection() is not treeselection:
                    signal.block()
                    try:
                        view.get_selection().unselect_all()
                    finally:
                        signal.unblock()
        self.sensitize()

    def outputDoubleClickCB(self, treeview, path, col):
        self.editOutputCB()
            
    def schedDoubleClickCB(self, treeview, path, col):
        if self.setScheduleButton.get_property("sensitive"):
            self.setSchedCB()

    def destDoubleClickCB(self, treeview, path, col):
        if self.setDestinationButton.get_property("sensitive"):
            self.setDestinationCB()

    ##############

    def renderEnableCell(self, column, cell_renderer, model, iter):
        debug.mainthreadTest()
        output = model[iter][0]
        cell_renderer.set_active(output.active)

    def enableCellCB(self, cell_renderer, path):
        debug.mainthreadTest()
        output = self.outputList[path][0]
        outputmenu.Enable(mesh=self.currentFullMeshName(),
                          output=output.name(),
                          enable=(not output.active))

    def renderOutputCell(self, column, cell_renderer, model, iter):
        debug.mainthreadTest()
        output = model[iter][0]
        cell_renderer.set_property('text', output.name())

        
    def renderScheduleCB(self, column, cell_renderer, model, iter):
        debug.mainthreadTest()
        output = model[iter][0]
        if output.schedule is not None:
            cell_renderer.set_property('text', output.schedule.shortrepr())
        else:
            cell_renderer.set_property('text', '---')

    def renderDestinationCB(self, column, cell_renderer, model, iter):
        debug.mainthreadTest()
        output = model[iter][0]
        if output.destination is not None:
            cell_renderer.set_property('text', output.destination.shortrepr())
        else:
            cell_renderer.set_property('text', '---')

    ############

    # Output button callbacks

    def newOutputCB(self, gtkbutton):
        # Create a new scheduled output
        menuitem = outputmenu.New
        params = filter(lambda a: a.name != 'mesh', menuitem.params)
        if parameterwidgets.getParameters(title='Define a new Output',
                                          scope=self,
                                          parentwindow=guitop.top().gtk,
                                          *params):
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

    def deleteOutputCB(self, gtkbutton):
        outputmenu.Delete.callWithDefaults(mesh=self.currentFullMeshName(),
                                           output=self.currentOutputName())
    def deleteAllCB(self, gtkbutton):
        outputmenu.DeleteAll.callWithDefaults(mesh=self.currentFullMeshName())

    ##############

    # Schedule button callbacks
        
    def setSchedCB(self, *args):
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

    def deleteSchedCB(self, gtkbutton):
        outputmenu.Schedule.Delete.callWithDefaults(
            mesh=self.currentFullMeshName(),
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

    ###############

    # Destination button callbacks

    def setDestinationCB(self, *args):
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

    def rewindAllDestinationsCB(self, gtkbutton):
        menuitem = outputmenu.Destination.RewindAll
        menuitem.callWithDefaults(mesh=self.currentFullMeshName())

    def deleteDestCB(self, gtkbutton):
        outputmenu.Destination.Delete.callWithDefaults(
            mesh=self.currentFullMeshName(),
            output=self.currentOutputName())

op = OutputPage()
