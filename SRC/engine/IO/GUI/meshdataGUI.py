# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Window for displaying mesh data.

## TODO: The window needs to be updated when the Microstructure,
## Skeleton, or Mesh is renamed.

## TODO: Put the output widgets their values in a table, so that the
## values are to the right of and lined up with the widgets.  Then
## there would be no confusion about which values go with widgets.
## Nested Concatenated outputs would look odd, though.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import primitives
from ooflib.common import subthread
from ooflib.common import utils
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import quit
from ooflib.common.IO.GUI import subWindow
from ooflib.common.IO.GUI import whowidget
from ooflib.common.IO.GUI import widgetscope
from ooflib.engine import mesh
from ooflib.engine.IO.GUI import outputvalwidgets
import ooflib.engine.IO.output

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import sys

allMeshDataWindows = []

mdWindowMenu = mainmenu.OOF.Windows.addItem(oofmenu.OOFMenuItem("Mesh_Data"))

class MeshDataGUI(widgetscope.WidgetScope):
    count = 1
    def __init__(self, gfxwindow, time, position, output=None):
        mainthread.runBlock(self.__init__thread,
                            (gfxwindow, time, position, output))

    def __init__thread(self, gfxwindow, time, position, output):
        debug.mainthreadTest()
        allMeshDataWindows.append(self)
        widgetscope.WidgetScope.__init__(self, None)

        current_count = MeshDataGUI.count
        MeshDataGUI.count += 1
        self._name = "Mesh_Data_%d" % current_count
        self.output = output
        self.time = time
        self.position = position
        self.sbcallbacks = []
        self.gsbcallbacks = []          # callbacks from a specific gfx window
        self.updateLock = lock.Lock()

        self.outputparam = \
                     ooflib.engine.IO.output.AggregateOutputParameter('output')

        # Although it's not displayed, we need a mesh widget in the
        # widgetscope, or the OutputParameterWidget won't work.
        # TODO LATER: Is this ugly, or what?
        self.meshWidget = whowidget.WhoWidget(mesh.meshes, scope=self,
                                              name="Godot")

        title = utils.underscore2space(self._name)
        self.gtk = Gtk.Window(type=Gtk.WindowType.TOPLEVEL, title=title)
        gtklogger.newTopLevelWidget(self.gtk, title)
        gtklogger.connect_passive(self.gtk, 'delete-event')
        gtklogger.connect_passive(self.gtk, 'configure-event')
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                               spacing=2, margin=5)
        self.gtk.add(self.mainbox)

        # Put this window into the Windows menu.  The menu item can't
        # be logged, since the creation and operation of the window
        # aren't logged, so scripts shouldn't refer to it at all.
        mainmenu.OOF.Windows.Mesh_Data.addItem(oofmenu.OOFMenuItem(
            self._name,
            no_log=True,
            help="Raise Mesh Data window %d." % current_count,
            threadable=oofmenu.UNTHREADABLE,
            callback=self.raiseWindow))

        expander = Gtk.Expander(label="Source")
        gtklogger.setWidgetName(expander, 'ViewSource')
        gtklogger.connect_passive_after(expander, 'activate')
        self.mainbox.pack_start(expander, expand=False, fill=False, padding=0)
        expander.set_expanded(True)
        
        self.table = Gtk.Grid(margin=2, row_spacing=2, column_spacing=2)
        expander.add(self.table)

        label = Gtk.Label(label="Source Window:", halign=Gtk.Align.END)
        self.table.attach(label, 0,0, 1,1)
        label.set_tooltip_text(
            "Display data for mouse clicks in this Graphics window.")

        self.gfxWindowChooser = chooser.ChooserWidget([],
                                                      callback=self.chooserCB,
                                                      name='GfxWindow')
        self.table.attach(self.gfxWindowChooser.gtk, 1,0, 1,1)

        label = Gtk.Label(label="Mesh:", halign=Gtk.Align.END)
        self.table.attach(label, 0,1, 1,1)
        label.set_tooltip_text("Data is displayed for values on this mesh.")

        self.meshText = Gtk.Entry(editable=False,
                                  hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.meshText, "meshname")
        self.meshText.set_width_chars(12)
        self.table.attach(self.meshText, 1,1, 1,1)

        # Position controls
        label = Gtk.Label(label="position x:", halign=Gtk.Align.END)
        self.table.attach(label, 0,2, 1,1)
        self.xText = Gtk.Entry(hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.xText, 'x')
        self.xText.set_width_chars(12)
        self.table.attach(self.xText, 1,2, 1,1)
        self.xText.set_tooltip_text(
            "x coordinate of the mouse click on the undisplaced Mesh")
        self.xsignal = gtklogger.connect(self.xText, 'changed',
                                         self.posChangedCB)

        label = Gtk.Label(label="position y:", halign=Gtk.Align.END)
        self.table.attach(label, 0,3, 1,1)
        self.yText = Gtk.Entry(hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.yText, 'y')
        self.yText.set_width_chars(12)
        self.table.attach(self.yText, 1,3, 1,1)
        self.yText.set_tooltip_text(
            "y coordinate of the mouse click on the undisplaced Mesh")
        self.ysignal = gtklogger.connect(self.yText, 'changed',
                                         self.posChangedCB)

        timerow = 5

        # Time controls.  Typing in the time widget does not
        # immediately update the displayed data, because interpolating
        # to a new time is an expensive computation, and shouldn't be
        # done while the user is in the middle of typing.  Instead,
        # the time widget is normally desensitized and uneditable.
        # When the user clicks the "Edit" button, the widget becomes
        # editable, the rest of the window is desensitized, and the
        # "Edit" button changes do a "Done" button.  When the user
        # clicks "Done" the data is updated and the time widget
        # becomes uneditable again.
        label = Gtk.Label(label="time:", halign=Gtk.Align.END)
        self.table.attach(label, 0,5, 1,1)
        tBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       hexpand=True, halign=Gtk.Align.FILL)
        self.table.attach(tBox, 1,5, 1,1)
        self.tText = Gtk.Entry(editable=False, sensitive=False)
        tBox.pack_start(self.tText, expand=True, fill=True, padding=0)
        gtklogger.setWidgetName(self.tText, 't')
        self.tText.set_width_chars(12)
        self.tEditButton = Gtk.Button(label="Edit")
        tBox.pack_start(self.tEditButton, expand=False, fill=False, padding=0)
        gtklogger.setWidgetName(self.tEditButton, "tEdit")
        gtklogger.connect(self.tEditButton, 'clicked', self.tEditCB)
        self.tEditMode = False
 
        # Output selection
        label = Gtk.Label(label="Output:", halign=Gtk.Align.END)
        label.set_alignment(1.0, 0.5)
        self.table.attach(label, 0,7, 1,1)
        label.set_tooltip_text("Choose which data is displayed.")
        
        self.outputwidget = self.outputparam.makeWidget(scope=self,
                                                        hexpand=True,
                                                        halign=Gtk.Align.FILL)
        self.table.attach(self.outputwidget.gtk, 1,7, 1,1)
        switchboard.requestCallback(self.outputwidget, self.outputwidgetCB)

        # Data display panel
        frame = Gtk.Frame(label="Data", shadow_type=Gtk.ShadowType.IN, margin=5)
        gtklogger.setWidgetName(frame, 'Data')
        self.mainbox.pack_start(frame, expand=True, fill=True, padding=0)
        # databox is where the data widget goes
        self.databox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                               margin=2)
        frame.add(self.databox)
        self.datawidget = None       # set by updateData

        # Buttons at the bottom of the window
        buttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.mainbox.pack_start(buttonbox, expand=False, fill=False, padding=2)
        # Freeze buttons 
        freezeframe = Gtk.Frame(label="Freeze", shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(freezeframe, "Freeze")
        buttonbox.pack_start(freezeframe, expand=True, fill=True, padding=0)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        freezeframe.add(hbox)
        # Freeze Space button
        self.freezeSpaceFlag = False
        self.freezeSpaceButton = Gtk.CheckButton(label='Space')
        gtklogger.setWidgetName(self.freezeSpaceButton, 'Space')
        hbox.pack_start(self.freezeSpaceButton,
                        expand=True, fill=False, padding=0)
        self.freezeSpaceButton.set_active(self.freezeSpaceFlag)
        gtklogger.connect(self.freezeSpaceButton, 'clicked', 
                          self.freezeSpaceButtonCB)
        self.freezeSpaceButton.set_tooltip_text(
            "Prevent the data in this window from being updated "
            "when the sample position changes.")
        # Freeze Time button
        self.freezeTimeFlag = False
        self.freezeTimeButton = Gtk.CheckButton(label='Time')
        gtklogger.setWidgetName(self.freezeTimeButton, "Time")
        hbox.pack_start(self.freezeTimeButton,
                        expand=True, fill=False, padding=0)
        self.freezeTimeButton.set_active(self.freezeTimeFlag)
        gtklogger.connect(self.freezeTimeButton,'clicked',
                          self.freezeTimeButtonCB)
        self.freezeTimeButton.set_tooltip_text(
            "Prevent the data in this window from being updated "
            "when the Mesh's time changes.")

        # Clone button
        self.cloneButton = gtkutils.StockButton('edit-copy-symbolic', 'Clone')
        gtklogger.setWidgetName(self.cloneButton, 'Clone')
        gtklogger.connect(self.cloneButton, 'clicked', self.cloneButtonCB)
        buttonbox.pack_start(self.cloneButton,
                             expand=False, fill=False, padding=0)
        self.cloneButton.set_tooltip_text(
            "Make a copy of this window with its current settings.")

        # Close button
        self.closeButton = gtkutils.StockButton("window-close-symbolic",
                                                "Close")
        gtklogger.setWidgetName(self.closeButton, 'Close')
        gtklogger.connect(self.closeButton, 'clicked', self.closeButtonCB)
        buttonbox.pack_end(self.closeButton,
                           expand=False, fill=False, padding=0)

        self.gtk.connect('destroy', self.destroyCB)

        self.updateGfxWindowChooser()
        if gfxwindow:
            self.gfxWindowChooser.set_state(gfxwindow.name)
        if position is not None:
            self.updatePosition(position)
        self.currentMesh = None
        self.updateMesh()

        self.setupSwitchboard()         # gfx window dependent callbacks
        self.sbcallbacks += [
            switchboard.requestCallbackMain('open graphics window',
                                            self.gfxwindowChanged),
            switchboard.requestCallbackMain('close graphics window',
                                            self.gfxwindowChanged),
            switchboard.requestCallbackMain('mesh data changed',
                                            self.meshDataChanged),
            switchboard.requestCallbackMain((gfxwindow, "time changed"),
                                            self.timeChanged)
            ]

        
        self.gtk.show_all()

    def raiseWindow(self, menuitem):
        debug.mainthreadTest()
        self.gtk.present_with_time(Gtk.get_current_event_time())

    def sensitize(self):
        self.xText.set_sensitive(not self.tEditMode)
        self.yText.set_sensitive(not self.tEditMode)
        self.tText.set_sensitive(self.tEditMode)
        self.meshWidget.set_sensitive(not self.tEditMode)
        self.databox.set_sensitive(not self.tEditMode)
        self.freezeTimeButton.set_sensitive(not self.tEditMode)
        self.freezeSpaceButton.set_sensitive(not self.tEditMode)
        self.gfxWindowChooser.gtk.set_sensitive(not self.tEditMode)
        self.meshText.set_sensitive(not self.tEditMode)
        self.outputwidget.gtk.set_sensitive(not self.tEditMode)
        gtklogger.checkpoint(self._name+" sensitized")

    ###################

    # Gfx window management

    def gfxwindowChanged(self, window): # sb callback, window opened or closed
        self.updateGfxWindowChooser()

    def updateGfxWindowChooser(self):
        self.gfxWindowChooser.update(
            [w.name for w in gfxmanager.gfxManager.windows])

    def chooserCB(self, gfxwindowname):
        self.setupSwitchboard()
        self.updateMesh()               # calls updateData if needed

    def setupSwitchboard(self):
        switchboard.removeCallbacks(self.gsbcallbacks)
        window = self.currentGfxWindow()
        if window is not None:
            self.gsbcallbacks = [
                switchboard.requestCallback((window, "layers changed"),
                                            self.layersChangedCB),
                switchboard.requestCallbackMain((window, "meshinfo click"),
                                                self.updatePosition)
            ]
        else:
            self.gsbcallbacks = []

    def currentGfxWindow(self):
        name = self.gfxWindowChooser.get_value()
        if name:
            return gfxmanager.gfxManager.getWindow(name)

    ##############

    def closeButtonCB(self, button):
        self.gtk.destroy()

    def destroyCB(self, *args):         # gtk callback
        mainmenu.OOF.Windows.Mesh_Data.removeItem(self._name)
        switchboard.removeCallback(self.sbcallbacks)
        switchboard.removeCallback(self.gsbcallbacks)
        allMeshDataWindows.remove(self)

    ##############
        
    def cloneButtonCB(self, button):
        newviewer = openMeshData(self.currentGfxWindow(), self.time,
                                 self.position, self.output)
        if self.freezeTimeFlag:
            newviewer.freezeTimeButton.clicked()
        if self.freezeSpaceFlag:
            newviewer.freezeSpaceButton.clicked()

    ##############

    def freezeSpaceButtonCB(self, button):
        debug.mainthreadTest()
        self.freezeSpaceFlag = button.get_active()
        if not self.freezeSpaceFlag:
            self.updatePosition(self.position)
            subthread.execute(self.updateData)

    def freezeTimeButtonCB(self, button):
        debug.mainthreadTest()
        self.freezeTimeFlag = button.get_active()
        if not self.freezeTimeFlag:
            self.updateTime(self.currentGfxWindow().displayTime)

    ##############

    def meshDataChanged(self, meshctxt): # sb "mesh data changed"
        debug.mainthreadTest()
        if (meshctxt is self.currentMesh and
            (not self.freezeTimeFlag or
             self.time == self.currentMesh.getCurrentTime())):
            subthread.execute(self.updateData)

    def layersChangedCB(self):
        debug.subthreadTest()
        mainthread.runBlock(self.updateMesh)
        self.updateData()

    def outputwidgetCB(self, interactive): # chosen output has changed
        debug.subthreadTest()
        self.updateData()

    def posChangedCB(self, gtkobj): # text edited in x & y Gtk.Entries
        debug.mainthreadTest()
        try:
            self.position = primitives.Point(_getval(self.xText),
                                             _getval(self.yText))
        except:
            # The user has typed something that can't be evaluated,
            # but maybe there's more typing to come. Ignore the error.
            if self.datawidget:
                self.datawidget.gtk.set_sensitive(False)
        else:
            subthread.execute(self.updateData)
            # Since the user has typed a new position, assume that
            # s/he really wants it, and don't overwrite it when the
            # mouse is clicked on the Mesh.
            self.freezeSpaceFlag = True
            self.freezeSpaceButton.set_active(True)

    def timeChanged(self): # sb callback. Time changed in gfx window.
        debug.mainthreadTest()
        if not self.freezeTimeFlag and not self.tEditMode:
            self.updateTime(self.currentGfxWindow().displayTime)
            
    def tEditCB(self, button):
        if not self.tEditMode:
            # Switch to time editing mode
            self.tEditMode = True
            self.tEditButton.set_label("Done")
            self.tText.set_editable(True)
        else:
            # Switch out of time editing mode
            self.tEditMode = False
            self.tText.set_editable(False)
            self.tEditButton.set_label("Edit")
            try:
                t = utils.OOFeval(self.tText.get_text().lstrip())
            except:
                pass
            else:
                self.time = t
                subthread.execute(self.updateData)
                # Since the user has entered a new time, don't
                # overwrite it when the graphics window's display time
                # changes.
                self.freezeTimeFlag = True
                self.freezeTimeButton.set_active(True)
        self.sensitize()

    ##############

    def updateMesh(self):
        debug.mainthreadTest()
        window = self.currentGfxWindow()
        newmesh = None
        if window:
            newmesh = window.topwho('Mesh')
            if newmesh:
                self.meshText.set_text(newmesh.path())
            else:
                self.meshText.set_text('<No Mesh in window!>')
        else:
            self.meshText.set_text('---')
        if not self.freezeTimeFlag:
            self.updateTime(window.displayTime)
        if newmesh is not self.currentMesh:
            self.currentMesh = newmesh
            subthread.execute(self.updateData)
        if newmesh is not None:
            self.meshWidget.set_value(newmesh.path())
        else:
            self.meshWidget.set_value(None)
        gtklogger.checkpoint(self._name+" mesh updated")

    def updatePosition(self, position):
        # Switchboard callback for (gfxwindow, "meshinfo click").
        # Also called when freezeSpaceFlag is unset, and during window
        # construction.
        debug.mainthreadTest()
        if not self.freezeSpaceFlag:
            if position != self.position:
                self.position = position
                subthread.execute(self.updateData)
            self.xsignal.block()
            self.ysignal.block()
            try:
                if position is not None:
                    # Strip blanks to the right of the number so that they
                    # don't get in the way when the user edits the
                    # position.
                    self.xText.set_text(("%-13.6g" % position.x).rstrip())
                    self.yText.set_text(("%-13.6g" % position.y).rstrip())
                else:
                    # Probably not required -- position is initially None,
                    # and having once been set, probably can't become
                    # None.
                    self.xText.set_text("")
                    self.yText.set_text("")
                    if config.dimension() == 3:
                        self.zText.set_text("")
            finally:
                self.xsignal.unblock()
                self.ysignal.unblock()
                if config.dimension() == 3:
                    self.zsignal.unblock()
            gtklogger.checkpoint(self._name+" position updated")

    def updateTime(self, time):
        if not self.freezeTimeFlag and not self.tEditMode:
            if time != self.time:
                self.time = time
                subthread.execute(self.updateData)
            if time is None:
                self.tText.set_text("")
            else:
                # Strip blanks to the right of the number so that they
                # don't get in the way when the user edits the
                # position.
                self.tText.set_text(("%-13.6g" % self.time).rstrip())
            gtklogger.checkpoint(self._name+" time updated")

    def updateData(self):
        debug.subthreadTest()
        self.updateLock.acquire()
        try:
            if self.datawidget:
                mainthread.runBlock(self.datawidget.destroy)
                self.datawidget = None

            op = mainthread.runBlock(self.outputwidget.get_value)

            if (self.currentMesh is not None and
                self.position is not None and op is not None):
                #self.currentMesh.begin_reading()

                self.currentMesh.restoreCachedData(self.time)
                val = None
                try:
                    # precompute *must* be called on a subthread
                    self.currentMesh.precompute_all_subproblems()

                    ## TODO: If op is a ConcatenateOutput and just one
                    ## of its inputs is incomputable, it would be nice
                    ## to still display the other one.  That doesn't
                    ## happen with the current structure because
                    ## op.incomputable is True if just one input is
                    ## incomputable.
                    
                    if (op is not None and 
                        not op.incomputable(self.currentMesh)):
                        element = self.currentMesh.enclosingElement(
                            self.position)
                        # op.evaluate eventually calls mesh precompute
                        # for the "Energy" or "Strain" selections in
                        # the Data Viewer, so we can't put these in
                        # updateDataMain below (running it with
                        # mainthread.runBlock), otherwise we get a
                        # lock error.
                        if element is not None:
                            masterpos = element.to_master(self.position)
                            val = op.evaluate(self.currentMesh.getObject(),
                                              [element], [[masterpos]])[0]
                finally:
                    self.currentMesh.releaseCachedData()
                    #self.currentMesh.end_reading()
                mainthread.runBlock(self.updateDataMain, (val,))
            gtklogger.checkpoint(self._name+" data updated")
        finally:
            self.updateLock.release()

    def updateDataMain(self, val):
        debug.mainthreadTest()
        self.datawidget = outputvalwidgets.makeWidget(
            val, hexpand=True, halign=Gtk.Align.FILL)
        self.databox.pack_start(self.datawidget.gtk,
                                expand=True, fill=True, padding=3)
        self.datawidget.show()


def _getval(widget):
    text = widget.get_text().lstrip()
    if text:
        return utils.OOFeval(text)
    return 0.0

###############################
        
def openMeshData(gfxwindow, time, position, output=None):
    return MeshDataGUI(gfxwindow, time, position, output)

