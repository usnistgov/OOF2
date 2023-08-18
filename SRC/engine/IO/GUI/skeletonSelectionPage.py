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
from ooflib.common import labeltree
from ooflib.common import mainthread
from ooflib.common import microstructure
from ooflib.common import subthread
from ooflib.common import utils
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import historian
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import skeletoncontext
from ooflib.engine import skeletonselmodebase

from ooflib.common.runtimeflags import digits

from gi.repository import Gtk
import sys


# Main GUI page for selecting Skeleton objects.

# Each type of selectable Skeleton object has an associate
# SkeletonSelectionMode subclass, of which there is one instance.  For
# each of these modes, the SkeletonSelectionPage creates a radio
# button to switch between modes, a list of groups, and a
# RegisteredClassFactory and Historian to modify the selection.  For
# each mode, all of this mode specific data is stored in a ModeData
# object.

class ModeData:
    def __init__(self, page, mode):
        self.page = page                # SkeletonSelectionPage
        self.mode = mode                # SkeletonSelectionMode object
        self.factory = None             # RCF of SelectionModifiers
        self.historybox = None          # HistoryBox obj, contains Historian
        self.button = None              # Radio button for selecting this mode
    def name(self):
        return self.mode.name
    def getSkeletonContext(self):
        return self.page.getCurrentSkeleton()
    def getSelectionContext(self, skelcontext):
        return self.mode.getSelectionContext(skelcontext)
    def getSelectionMenu(self):
        return self.mode.getSelectionMenu()
    def getGroupMenu(self):
        return self.mode.getGroupMenu()
    def getGroups(self, skeletoncontext):
        return self.mode.getGroups(skeletoncontext)
    def modifierApplied(self, modifier): # sb: mode.modifierappliedsignal
        if self.historybox is not None:
            if modifier is not None:
                self.historybox.historian.record(modifier)
                self.historybox.sensitize()
    def validityChangeCB(self, validity): # sb: ('validity', factory)
        self.ok_sensitize()
    def ok_sensitize(self):
        debug.mainthreadTest()
        skelcontext = self.getSkeletonContext()
        self.historybox.okbutton.set_sensitive(
            skelcontext is not None
            and not skelcontext.query_reservation()
            and self.factory.isValid())
        

class SkeletonSelectionPage(oofGUI.MainPage):
    def __init__(self):
        self.built = False
        oofGUI.MainPage.__init__(
            self, name="Skeleton Selection",
            ordering = 135,
            tip = "Manipulate selectable skeleton objects.")

        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(self.mainbox)

        self.skelwidgetbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                     spacing=2, halign=Gtk.Align.CENTER,
                                     margin_top=2)
        self.mainbox.pack_start(self.skelwidgetbox,
                                expand=False, fill=False, padding=0)
        self.skelwidget = whowidget.WhoWidget(skeletoncontext.skeletonContexts,
                                              scope=self)
        self.skelwidget.verbose = True
        label = Gtk.Label(label='Microstructure=', halign=Gtk.Align.END)
        self.skelwidgetbox.pack_start(label,
                                      expand=False, fill=False, padding=0)
        self.skelwidgetbox.pack_start(self.skelwidget.gtk[0],
                                      expand=False, fill=False, padding=0)
        label = Gtk.Label(label='Skeleton=',
                          halign=Gtk.Align.END, margin_start=5)
        self.skelwidgetbox.pack_start(label,
                                      expand=False, fill=False, padding=0)
        self.skelwidgetbox.pack_start(self.skelwidget.gtk[1],
                                      expand=False, fill=False, padding=0)

        self.modebox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                               spacing=3, halign=Gtk.Align.CENTER)
        gtklogger.setWidgetName(self.modebox, 'Mode')
        self.mainbox.pack_start(self.modebox,
                                expand=False, fill=False, padding=0)
        label = Gtk.Label(label="Selection Mode:", halign=Gtk.Align.END)
        self.modebox.pack_start(label, expand=False, fill=False, padding=0)

        # Construct buttons for switching between selection modes, and
        # the ModeData objects that contain the mode-specific data and
        # widgets.
        self.modedict = {}
        firstbutton = None
        for mode in skeletonselmodebase.SkeletonSelectionMode.modes:
            name = mode.name
            modedata = self.modedict[name] = ModeData(self, mode)
            if firstbutton:
                button = Gtk.RadioButton(label=name+'s', group=firstbutton)
            else:
                button = Gtk.RadioButton(label=name+'s')
                firstbutton = button
                self.activemode = modedata
            gtklogger.setWidgetName(button, name)
            modedata.button = button
            button.set_tooltip_text("Select " + name + "s")
            self.modebox.pack_start(button, expand=False, fill=False, padding=0)
            gtklogger.connect(button, 'clicked', self.pickerCB, modedata)
            switchboard.requestCallbackMain(
                modedata.mode.changedselectionsignal,
                self.newSelection, mode=modedata)
            switchboard.requestCallbackMain(
                modedata.mode.modifierappliedsignal,
                self.modifiedSelection, mode=modedata)
        firstbutton.set_active(True)

        self.mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                                  wide_handle=True)
        gtklogger.setWidgetName(self.mainpane, 'Pane')
        self.mainbox.pack_start(self.mainpane,
                                expand=True, fill=True, padding=0)
        gtklogger.connect_passive(self.mainpane, 'notify::position')
        
        # Status and Group are on the left side of the page.
        self.leftbox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=5,
            margin_top=2, margin_bottom=2,
            margin_start=2, margin_end=gtkutils.handle_padding)
        self.mainpane.pack1(self.leftbox, resize=True, shrink=False)

        # Status box.
        self.statusframe = Gtk.Frame(shadow_type=Gtk.ShadowType.IN)
        self.leftbox.pack_start(self.statusframe,
                                expand=False, fill=False, padding=0)
        sframe2 = Gtk.Frame(margin=2)
        self.statusframe.add(sframe2)
        self.status = Gtk.TextView(name="fixedfont", editable=False,
                                   cursor_visible=False,
                                   wrap_mode=Gtk.WrapMode.WORD,
                                   left_margin=10, right_margin=10,
                                   top_margin=2, bottom_margin=2)
        gtklogger.setWidgetName(self.status, 'status')
        sframe2.add(self.status)

        # Group operations.
        self.groupgui = GroupGUI(self)
        self.leftbox.pack_start(self.groupgui.gtk,
                                expand=True, fill=True, padding=0)

        # Selection operations on the right side of the page.
        self.selectiongui = SelectionGUI(self)
        self.mainpane.pack2(self.selectiongui.gtk, resize=False, shrink=False)

        switchboard.requestCallbackMain(("new who", "Microstructure"),
                                        self.new_microstructure)
        switchboard.requestCallbackMain(self.skelwidget, self.skelwidgetCB)
        switchboard.requestCallbackMain("materials changed in skeleton",
                                        self.matchangedCB)

        switchboard.requestCallbackMain("made reservation",
                                        self.reservationChanged)
        switchboard.requestCallbackMain("cancelled reservation",
                                        self.reservationChanged)

    def installed(self):
        if not self.built:
            # initialize, arbitrarily, to the first mode listed
            self.set_mode(self.modedict[skeletonselmodebase.firstMode().name])
            self.built = True

    def getCurrentSkeletonName(self):
        return self.skelwidget.get_value()
    def getCurrentSkeleton(self):
        name = self.getCurrentSkeletonName()
        path = labeltree.makePath(name)
        try:
            return skeletoncontext.skeletonContexts[name]
        except KeyError:
            return None

    def getCurrentMicrostructureName(self):
        return self.skelwidget.get_value(depth=1)
    def getCurrentMicrostructureContext(self):
        try:
            return microstructure.microStructures[
                self.getCurrentMicrostructureName()]
        except KeyError:
            return None
        
    # Must run on a subthread, because of the lock.
    def selectionSize(self):
        debug.subthreadTest()
        skelcontext = mainthread.runBlock(self.getCurrentSkeleton)
        if skelcontext is not None:
            skelcontext.begin_reading()
            try:
                if not skelcontext.defunct():
                    ctxt = self.activemode.getSelectionContext(skelcontext)
                    return ctxt.size()
            finally:
                skelcontext.end_reading()
        return 0

    def selectionSizeAndMax(self):
        debug.subthreadTest()
        skelcontext = mainthread.runBlock(self.getCurrentSkeleton)
        if skelcontext is not None:
            skelcontext.begin_reading()
            try:
                if not skelcontext.defunct():
                    selectionctxt = \
                        self.activemode.getSelectionContext(skelcontext)
                    return selectionctxt.size(), selectionctxt.maxSize()
            finally:
                skelcontext.end_reading()
        return None

    def update(self):
        skelctxt = self.getCurrentSkeleton()
        subthread.execute(self.update_subthread, (skelctxt,))

    def update_subthread(self, skelcontext):
        # Get the selection from the skeleton context
        if skelcontext:
            n, m = self.selectionSizeAndMax()    # requires subthread
            if m > 0:
                status_text = (f"{n} of {m} "
                               f"{self.activemode.name()}s selected "
                               f"({100.*n/m:.{digits()}g}%)")
            else:
                status_text = "0 %s%s selected." % \
                    (self.activemode.name(), 's'*(n!=1))
        else:
            status_text = "No Skeleton selected."

        mainthread.runBlock(self.status.get_buffer().set_text, (status_text,))
        gtklogger.checkpoint("skeleton selection page updated")
        
    def pickerCB(self, radiobutton, modedata):  # new selection mode chosen
        # This is called for the button that's turned off as well as
        # the one that's turned on, so check before doing anything.
        if radiobutton.get_active():
            self.set_mode(modedata)

    def set_mode(self, modedata):
        self.statusframe.set_label(modedata.name() + ' Selection Status')
        self.activemode = modedata
        self.groupgui.pickerCB(modedata)
        self.selectiongui.pickerCB(modedata)
        self.update()       # doesn't set self.activemode anymore

    def skelwidgetCB(self, interactive): # skeleton widget sb callback
        debug.mainthreadTest()
        skelcontext = self.getCurrentSkeleton()
        self.groupgui.new_skeleton(skelcontext)
        self.selectiongui.new_skeleton(skelcontext)
        self.update()

    def new_microstructure(self, msname): # sb ("new who", "Microstructure")
        # Switch to a new Microstructure only if there is no current Skeleton
        if not self.getCurrentSkeletonName():
            self.skelwidget.set_value(msname)
    
    def show(self):
        debug.mainthreadTest()
        self.gtk.show()
        self.mainbox.show()
        self.skelwidgetbox.show_all()
        self.modebox.show_all()
        self.mainpane.show()
        self.leftbox.show_all()
        self.groupgui.show()
        self.selectiongui.show()

    # switchboard callback for mode.modifierappliedsignal
    def modifiedSelection(self, modifier, mode):
        if mode is self.activemode:
            self.groupgui.sensitize()
            self.selectiongui.sensitize()
            # self.update must come last, so that the checkpoint is
            # issued after everything has changed.
            self.update()

    # switchboard callback for mode.changedselectionsignal
    def newSelection(self, mode):
        if mode is self.activemode:
            self.groupgui.sensitize()
            self.selectiongui.sensitize()
            # self.update must come last, so that the checkpoint is
            # issued after everything has changed.
            self.update()

    def matchangedCB(self, skelctxt):
        if skelctxt is self.getCurrentSkeleton():
            self.groupgui.draw_grouplist()

    # switchboard callback for "made reservation" or "cancelled reservation"
    def reservationChanged(self, who):
        if self.getCurrentSkeleton() is who:
            self.groupgui.sensitize()
            self.selectiongui.sensitize()


# GroupGUI contains the big list of groups, which changes when a new
# category is picked by the picker, or when a new skeletoncontext is
# selected by the mesh widget.  The GroupGUI has a local selection
# state.

class GroupGUI:
    def __init__(self, parent):
        debug.mainthreadTest()
        self.parent = parent
        self.gtk = Gtk.Frame(shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(self.gtk, 'Groups')
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                      margin=2)
        self.gtk.add(box)
        # Set in chooserCB, the widget callback for the chooser list.
        self.current_group_name = None
        # List of buttons which are sensitive only when a group is selected.
        self.groupbuttons = []
        # List of buttons which are sensitive when there is a group
        # and a selection.
        self.groupandselectionbuttons = []

        # Left-hand button box.  New/Auto/Rename/Copy/Delete/DeleteAll
        lbuttons = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        box.pack_start(lbuttons, fill=False, expand=False, padding=0)

        self.new_button = Gtk.Button(label="New...")
        gtklogger.setWidgetName(self.new_button, 'New')
        lbuttons.pack_start(self.new_button,
                            fill=False, expand=False, padding=0)
        gtklogger.connect(self.new_button, "clicked", self.newGroupCB)
        self.new_button.set_tooltip_text("Create a new empty group.")

        self.auto_button = Gtk.Button(label="Auto")
        gtklogger.setWidgetName(self.auto_button, 'Auto')
        lbuttons.pack_start(self.auto_button,
                            fill=False, expand=False, padding=0)
        gtklogger.connect(self.auto_button, 'clicked', self.autoGroupCB)
        self.auto_button.set_tooltip_text(
            "Automatically create groups from the current pixel groups.")
        
        self.rename_button = Gtk.Button(label="Rename...")
        gtklogger.setWidgetName(self.rename_button, 'Rename')
        lbuttons.pack_start(self.rename_button,
                            fill=False, expand=False, padding=0)
        self.groupbuttons.append(self.rename_button)
        gtklogger.connect(self.rename_button, "clicked", self.renameGroupCB)
        self.rename_button.set_tooltip_text("Rename the selected group.")

        self.copy_button = Gtk.Button(label="Copy...")
        gtklogger.setWidgetName(self.copy_button, 'Copy')
        lbuttons.pack_start(self.copy_button,
                            fill=False, expand=False, padding=0)
        self.groupbuttons.append(self.copy_button)
        gtklogger.connect(self.copy_button, "clicked", self.copyGroupCB)
        self.copy_button.set_tooltip_text("Copy the selected group.")

        self.delete_button = Gtk.Button(label="Delete")
        gtklogger.setWidgetName(self.delete_button, 'Delete')
        lbuttons.pack_start(self.delete_button,
                            fill=False, expand=False, padding=0)
        self.groupbuttons.append(self.delete_button)
        gtklogger.connect(self.delete_button, "clicked", self.deleteGroupCB)
        self.delete_button.set_tooltip_text("Deleted the selected group.")

        self.deleteAll_button = Gtk.Button(label="Delete All")
        gtklogger.setWidgetName(self.deleteAll_button, 'DeleteAll')
        lbuttons.pack_start(self.deleteAll_button,
                            fill=False, expand=False, padding=0)
        gtklogger.connect(self.deleteAll_button, 'clicked', self.deleteAllCB)
        self.deleteAll_button.set_tooltip_text("Delete all groups.")
        
        # Groups list.
        self.grouplist = chooser.ScrolledChooserListWidget(
            callback=self.chooserCB, name="GroupList",
            margin_top=2, margin_bottom=2)
        box.pack_start(self.grouplist.gtk, fill=True, expand=True, padding=0)
        
        # Right-hand button box.  Add/Remove/Clear/ClearAll/Info
        rbuttons = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        box.pack_start(rbuttons, fill=False, expand=False, padding=0)

        self.add_button = Gtk.Button(label="Add")
        gtklogger.setWidgetName(self.add_button, 'Add')
        rbuttons.pack_start(self.add_button,
                            fill=False, expand=False, padding=0)
        self.groupandselectionbuttons.append(self.add_button)
        gtklogger.connect(self.add_button, "clicked", self.addToGroupCB)
        self.add_button.set_tooltip_text(
            "Add the currently selected pixels to the selected group.")

        self.remove_button = Gtk.Button(label="Remove")
        gtklogger.setWidgetName(self.remove_button, 'Remove')
        rbuttons.pack_start(self.remove_button,
                            fill=False, expand=False, padding=0)
        self.groupandselectionbuttons.append(self.remove_button)
        gtklogger.connect(self.remove_button, "clicked", self.removeFromGroupCB)
        self.remove_button.set_tooltip_text(
            "Remove the currently selected pixels from the selected group.")
        
        self.clear_button = Gtk.Button(label="Clear")
        gtklogger.setWidgetName(self.clear_button, 'Clear')
        rbuttons.pack_start(self.clear_button,
                            fill=False, expand=False, padding=0)
        gtklogger.connect(self.clear_button, "clicked", self.clearGroupCB)
        self.clear_button.set_tooltip_text(
            "Remove all pixels from the selected group.")

        self.clearAll_button = Gtk.Button(label="Clear All")
        gtklogger.setWidgetName(self.clearAll_button, 'ClearAll')
        rbuttons.pack_start(self.clearAll_button,
                            fill=False, expand=False, padding=0)
        gtklogger.connect(self.clearAll_button, "clicked", self.clearAllCB)
        self.clearAll_button.set_tooltip_text(
            "Remove all pixels from all groups.")

        self.info_button = Gtk.Button(label="Info")
        gtklogger.setWidgetName(self.info_button, 'Info')
        rbuttons.pack_start(self.info_button,
                            fill=False, expand=False, padding=0)
        self.groupbuttons.append(self.info_button)
        gtklogger.connect(self.info_button, "clicked", self.queryGroupCB)
        self.info_button.set_tooltip_text(
            "Display information about the selected group in the"
            " OOF Messages window.")
        
        ## TODO: Hide this frame when mode.materialsallowed is False.
        matframe = Gtk.Frame(label="Material", shadow_type=Gtk.ShadowType.IN,
                             valign=Gtk.Align.END)
        rbuttons.pack_end(matframe, expand=False, fill=False, padding=0)
        matbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                         margin_start=2, margin_end=2, margin_bottom=2)
        matframe.add(matbox)

        self.addmaterial_button = Gtk.Button(label="Assign")
        gtklogger.setWidgetName(self.addmaterial_button, 'AddMaterial')
        matbox.pack_start(self.addmaterial_button,
                          fill=False, expand=False, padding=0)
        gtklogger.connect(self.addmaterial_button, "clicked",
                          self.addMaterialCB)
        self.addmaterial_button.set_tooltip_text(
            "Assign a material to the members of the selected group."
            " This overrides any material assigned to the pixels.")

        self.removematerial_button = Gtk.Button(label="Remove")
        matbox.pack_start(self.removematerial_button,
                          fill=False, expand=False, padding=0)
        gtklogger.connect(self.removematerial_button, "clicked",
                          self.removeMaterialCB)
        self.removematerial_button.set_tooltip_text(
            "Remove an explicitly assigned material from the members"
            " of the selected group.")
        
        # Need to be notified when groupset memberships change.
        switchboard.requestCallback("groupset member added", self.group_added),
        switchboard.requestCallback("groupset member renamed",
                                    self.group_added),
        switchboard.requestCallback("groupset changed", self.groupset_changed),
        switchboard.requestCallback("groupset member resized",
                                    self.group_resized)
        switchboard.requestCallback("new pixel group", self.pxlgroup_added)
        switchboard.requestCallback("destroy pixel group", self.pxlgroup_added)

        self.sensitize()

    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()

    def activemode(self):
        return self.parent.activemode

    def getGroupSet(self):
        skelcontext = self.parent.getCurrentSkeleton()
        # If this is being called in indirect response to a
        # switchboard signal, the skeleton may be in the process of
        # being dismantled, and getGroups might fail.  So check for
        # that by calling defunct() before doing anything.
        ## TODO: That's a general problem with switchboard signals
        ## that invoke other switchboard signals, perhaps combined
        ## with subthread/mainthread calls.
        if skelcontext and not skelcontext.defunct():
            return self.activemode().getGroups(skelcontext)

        
    # Called from the ChooserListWidget when a new selection is
    # made, including "None" for a deselection.
    def chooserCB(self, name, interactive):
        if self.parent.built:
            self.sensitize()


    # For the following three callbacks, it's tempting to just have
    # them be requested on subthreads, but there's actually no
    # guarantee that the notifying thread will not be the main thread,
    # and the locks *must* be on a subthread.  So we do it this way.

    # Utility function, conditional for the callbacks.
    def check_skel_and_gset(self, skelctxt, gset):
        page_skel = self.parent.getCurrentSkeleton()
        if skelctxt is page_skel:
            gst = self.getGroupSet()
            if gset is gst:
                return gset
        return False

    # Switchboard callback, called when member groups are added to or removed
    # from a groupset.  Arguments are the host skeletonContext
    # and the groupset.
    def group_added(self, skelcontext, gset, name):
        debug.subthreadTest()
        gset = mainthread.runBlock(self.check_skel_and_gset, (skelcontext,gset))
        if gset:
            skelcontext.begin_reading()
            try:
                names = gset.allGroups()
            finally:
                skelcontext.end_reading()
            self.update_grouplist(names, map(gset.displayString, names))
            mainthread.runBlock(self.grouplist.set_selection,
                                    (name,) )
        else:
            self.sensitize_subthread()
        switchboard.notify("redraw skeletongroups", skelcontext)

    def groupset_changed(self, skelcontext, gset):
        debug.subthreadTest()
        gset = mainthread.runBlock(self.check_skel_and_gset, (skelcontext,gset))
        if gset:
            skelcontext.begin_reading()
            try:
                names = gset.allGroups()
            finally:
                skelcontext.end_reading()
            self.update_grouplist(names, map(gset.displayString, names))
        # Must sensitize -- if the current group has become empty,
        # the "clear" button's sensitivity will have changed.
        self.sensitize_subthread()
        switchboard.notify("redraw skeletongroups", skelcontext)    

    def group_resized(self, skelcontext, gset):
        debug.subthreadTest()
        gset = mainthread.runBlock(self.check_skel_and_gset, (skelcontext,gset))
        if gset:
            skelcontext.begin_reading()
            try:
                names = gset.allGroups()
            finally:
                skelcontext.end_reading()
            self.update_grouplist(names, map(gset.displayString, names))
        # Must sensitize -- if the resize was to or away from size 0,
        # the clear button needs updating.
        self.sensitize_subthread()

    def pxlgroup_added(self, group, *args):
        # switchboard callback when pixel groups are added or
        # removed. The auto button has to be sensitized.
        self.sensitize_subthread()
    
    # Button callback for the "new group" button.
    def newGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        menuitem = self.activemode().getGroupMenu().New_Group
        group_param = menuitem.get_arg('name')
        if parameterwidgets.getParameters(
                group_param,
                parentwindow=self.gtk.get_toplevel(),
                title='Create a new %s group' % self.activemode().name()):
            menuitem.callWithDefaults(skeleton=skelpath)

    def autoGroupCB(self, gtkobj): # "auto group" button callback
        skelpath = self.parent.getCurrentSkeletonName()
        menuitem = self.activemode().getGroupMenu().Auto_Group
        menuitem.callWithDefaults(skeleton=skelpath)

    # Button callback for the "rename group" button.
    def renameGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Rename_Group
        new_group_param = menuitem.get_arg('new_name')
        new_group_param.value = current_group
        if parameterwidgets.getParameters(
                new_group_param,
                parentwindow=self.gtk.get_toplevel(),
                title='Rename group %s' % current_group):
            menuitem.callWithDefaults(skeleton=skelpath,
                                      group=current_group)

    # Button callback for the "copy group" button.
    def copyGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Copy_Group
        new_group_param = menuitem.get_arg('new_name')
        if parameterwidgets.getParameters(
                new_group_param,
                parentwindow=self.gtk.get_toplevel(),
                title='Copy group %s' % current_group):
            menuitem.callWithDefaults(skeleton=skelpath,
                                      group=current_group)

    # Button callback for the "delete group" button.
    def deleteGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Delete_Group
        menuitem(skeleton=skelpath, group=current_group)

    def deleteAllCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        menuitem = self.activemode().getGroupMenu().Delete_All
        menuitem(skeleton=skelpath)

    # Button callback for the "add" button, adds selection to group.
    def addToGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Add_to_Group
        menuitem(skeleton=skelpath, group=current_group)

    # Button callback for the "remove" button, removes the current
    # selection from the current group.
    def removeFromGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Remove_from_Group
        menuitem(skeleton=skelpath, group=current_group)

    # Button callback for the "clear" button, removes all members
    # from the current group.
    def clearGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Clear_Group
        menuitem(skeleton=skelpath, group=current_group)

    def clearAllCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()        
        menuitem = self.activemode().getGroupMenu().Clear_All
        menuitem(skeleton=skelpath)
        
    def queryGroupCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Query_Group
        menuitem(skeleton=skelpath, group=current_group)

    def addMaterialCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Assign_Material
        if parameterwidgets.getParameters(
                menuitem.get_arg('material'),
                parentwindow=self.gtk.get_toplevel(),
                title="Assign a material to a %s group" % self.activemode().name()):
            menuitem.callWithDefaults(skeleton=skelpath, group=current_group)

    def removeMaterialCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        current_group = self.grouplist.get_value()
        menuitem = self.activemode().getGroupMenu().Remove_Material
        menuitem(skeleton=skelpath, group=current_group)
    
    # Called from the parent when the skeleton widget has a new
    # skeletoncontext, including "None".
    def new_skeleton(self, skelcontext):
        self.draw_grouplist()
        self.sensitize()

    # Called from the parent when the "picker" chooses a new selection mode.
    def pickerCB(self, mode):
        self.gtk.set_label(mode.name() + " group operations")
        self.draw_grouplist()
        # Don't call self.sensitize here.  It's already been called
        # via self.draw_grouplist.

    def draw_grouplist(self):
        groupset = self.getGroupSet()
        if groupset:
            namelist = groupset.allGroups()
            self.update_grouplist(namelist,
                                  map(groupset.displayString, namelist))
        else:
            self.update_grouplist([], [])

    def update_grouplist(self, names, objs):
        mainthread.runBlock(self.update_grouplist_thread, (names, objs))
    def update_grouplist_thread(self, names, objs):
        # Updating the chooser calls self.chooserCB, which calls
        # self.sensisitize, so methods that call update_grouplist
        # should *not* call sensitize.
        self.grouplist.update(names, objs) 
        gtklogger.checkpoint("skeleton selection page grouplist "
                             + self.activemode().name())

    # This little two-step is required because the selectionSize()
    # query locks the selection object, and so can't be on the main
    # thread, but all the other sensitize operations are GUI
    # operations and must be on the main thread.
    def sensitize(self):
        subthread.execute(self.sensitize_subthread)

    def sensitize_subthread(self):
        debug.subthreadTest()
        ssize = self.parent.selectionSize() # requires subthread
        mainthread.runBlock(self.sensitize_mainagain, (ssize,))

    def sensitize_mainagain(self, ssize):
        debug.mainthreadTest()
        skelctxt = self.parent.getCurrentSkeleton()
        curskel = skelctxt is not None and not skelctxt.query_reservation()
        groupset = self.getGroupSet()

        self.new_button.set_sensitive(curskel)

        # The Auto button is sensitive if the microstructure has any
        # pixel groups.
        ms = self.parent.getCurrentMicrostructureContext()
        self.auto_button.set_sensitive(
            ms is not None and curskel and ms.getObject().nGroups() > 0)

        # The Delete All button is sensitive if the Skeleton has any
        # Element/Node/Segment groups.
        self.deleteAll_button.set_sensitive(curskel and
                                            groupset is not None and 
                                            groupset.nGroups() > 0)

        # The Clear All button is sensitive if at least one group is
        # non-empty.
        if groupset is not None:
            for group in groupset.allGroups():
                if groupset.sizeOfGroup(group) > 0:
                    self.clearAll_button.set_sensitive(True)
                    break
            else:
                self.clearAll_button.set_sensitive(False)
        else:
            self.clearAll_button.set_sensitive(False)
        
        # Set the buttons in the groupbuttons list, if there is a group.
        groupstate = self.grouplist.get_value() is not None
        for b in self.groupbuttons:
            b.set_sensitive(groupstate)

        # Set the groupandselectionbuttons if there's a group selected,
        # and the skeletoncontext has a selection of the appropriate type
        # which is of nonzero size.
        g = self.grouplist.get_value()
        groupselectstate = g is not None and ssize > 0
        for b in self.groupandselectionbuttons:
            b.set_sensitive(groupselectstate)

        groupset = self.getGroupSet()
        self.clear_button.set_sensitive(groupset is not None and g is not None
                                        and groupset.sizeOfGroup(g) > 0)

        matok = (g is not None and
                 self.activemode().mode.materialsallowed is not None)

        self.addmaterial_button.set_sensitive(matok)
        self.removematerial_button.set_sensitive(matok)
        gtklogger.checkpoint("skeleton selection page groups sensitized "
                             + self.activemode().name())
                             
            
class SelectionGUI:
    def __init__(self, parent):
        debug.mainthreadTest()
        self.parent = parent
        self.gtk = Gtk.Frame(
            shadow_type=Gtk.ShadowType.IN,
            margin_start=gtkutils.handle_padding, margin_end=2,
            margin_top=2, margin_bottom=2)
        gtklogger.setWidgetName(self.gtk, 'Selection')
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(self.vbox)

        self.actionbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                                 spacing=2)
        self.vbox.pack_start(self.actionbox, expand=True, fill=True, padding=0)

        self.historyline = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                                   spacing=2)
        self.vbox.pack_start(self.historyline,
                             expand=False, fill=False, padding=0)

        for modeobj in parent.modedict.values():
            modeobj.factory = regclassfactory.RegisteredClassFactory(
                modeobj.mode.modifierclass.registry,
                title="Method= ",
                scope=parent, name=modeobj.name()+"Action",
                shadow_type=Gtk.ShadowType.NONE
            )
            modeobj.historybox = HistoryBox(self.setCB, self.okCB)
            gtklogger.setWidgetName(modeobj.historybox.gtk,
                                    modeobj.name()+"History")
            modeobj.factory.set_callback(
                modeobj.historybox.historian.stateChangeCB)
            # Sensitize the history stuff when the selections are modified.
            switchboard.requestCallbackMain(modeobj.mode.modifierappliedsignal,
                                            modeobj.modifierApplied)
            switchboard.requestCallbackMain(('validity', modeobj.factory),
                                            modeobj.validityChangeCB)

        # Slightly misleading name, includes undo, redo and clear.
        self.undoredoline = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                    spacing=2, margin_start=2, margin_end=2,
                                    margin_bottom=2)
        
        self.undo_button = gtkutils.StockButton('edit-undo-symbolic', 'Undo')
        gtklogger.setWidgetName(self.undo_button, 'Undo')
        gtklogger.connect(self.undo_button, "clicked", self.undoCB)
        self.undo_button.set_tooltip_text(
            "Undo the latest selection operation.")
        self.undoredoline.pack_start(self.undo_button, expand=True, fill=False,
                                     padding=0)

        self.redo_button = gtkutils.StockButton('edit-redo-symbolic', 'Redo')
        gtklogger.setWidgetName(self.redo_button, 'Redo')
        gtklogger.connect(self.redo_button, "clicked", self.redoCB)
        self.redo_button.set_tooltip_text(
            'Redo the latest undone selection operation.')
        self.undoredoline.pack_start(self.redo_button,
                                     expand=True, fill=False, padding=0)

        self.clear_button = gtkutils.StockButton('edit-clear-symbolic', 'Clear')
        gtklogger.setWidgetName(self.clear_button, 'Clear')
        gtklogger.connect(self.clear_button, "clicked", self.clearCB)
        self.clear_button.set_tooltip_text(
            'Reset selection by clearing the current selection.')        
        self.undoredoline.pack_start(self.clear_button,
                                     expand=True, fill=False, padding=0)

        self.invert_button = Gtk.Button(label="Invert")
        gtklogger.setWidgetName(self.invert_button, 'Invert')
        gtklogger.connect(self.invert_button, "clicked", self.invertCB)
        self.invert_button.set_tooltip_text('Toggle the current selection.')
        self.undoredoline.pack_start(self.invert_button,
                                     expand=True, fill=False, padding=0)
        
        self.vbox.pack_start(self.undoredoline,
                             expand=False, fill=False, padding=0)

        # Add all the action and history widgets.  They do not
        # all get shown, see this class's "show" routine for the drill.
        for modeobj in parent.modedict.values():
            self.actionbox.pack_start(modeobj.factory.gtk,
                                      expand=True, fill=True, padding=0)
            self.historyline.pack_start(modeobj.historybox.gtk,
                                        expand=False, fill=False, padding=0)

        self.sensitize()

    def activemode(self):
        return self.parent.activemode
    
    # Show the appropriate factory and historybox.
    def show(self):
        debug.mainthreadTest()
        self.gtk.show()
        self.vbox.show()
        self.actionbox.show()
        self.historyline.show()
        for mode in self.parent.modedict.values():
            mode.historybox.gtk.hide()
            mode.factory.gtk.hide()
        self.activemode().historybox.gtk.show_all()
        self.activemode().factory.gtk.show_all()
        self.undoredoline.show_all()
        

    # Show the correct factory in the actionbox, put the right
    # historybox up, and sensitize everything.
    def pickerCB(self, mode):
        debug.mainthreadTest()
        for v in self.parent.modedict.values():
            v.historybox.gtk.hide()
            v.factory.gtk.hide()
        mode.factory.gtk.show_all()
        mode.historybox.gtk.show_all()
        mode.historybox.sensitize()
        self.gtk.set_label(mode.name() + ' Selection Operations')
        self.new_skeleton(self.parent.getCurrentSkeleton())
        

    # Called from the parent when the mesh widget state changes,
    # and also from pickerCB when the picker changes the mode.
    def new_skeleton(self, skelcontext):
        self.sensitize()
        for v in self.parent.modedict.values():
            v.ok_sensitize()

    def currentSelection(self):
        skelcontext = self.parent.getCurrentSkeleton()
        if skelcontext is not None:
            return self.activemode().getSelectionContext(skelcontext)

    # Callback from the current HistoryBox's OK button.  All the
    # historyboxes are connected to this, but only the current one can
    # have sent the signal, so it's the only one operated on.
    def okCB(self, gtkobj):
        mod = self.activemode().factory.getRegistration()
        if mod is not None:
            self.activemode().factory.set_defaults()
            menuitem = getattr(self.activemode().getSelectionMenu(),
                               utils.space2underscore(mod.name()) )
            skelpath = self.parent.getCurrentSkeletonName()

            # Set the skeleton parameter and call the registered class.
            menuitem.callWithDefaults(skeleton=skelpath)
            
    # Called when the historian switches to a new object. 
    def setCB(self, object):
        self.activemode().factory.set(object,interactive=True)
        self.activemode().historybox.sensitize()

    def undoCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        self.activemode().getSelectionMenu().Undo(skeleton=skelpath)

    def redoCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        self.activemode().getSelectionMenu().Redo(skeleton=skelpath)

    def clearCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        self.activemode().getSelectionMenu().Clear(skeleton=skelpath)

    def invertCB(self, gtkobj):
        skelpath = self.parent.getCurrentSkeletonName()
        self.activemode().getSelectionMenu().Invert(skeleton=skelpath)

    # Check the current selection object, and sensitize the selection
    # buttons accordingly.
    def sensitize(self):
        current_selection = self.currentSelection()
        skelcontext = self.parent.getCurrentSkeleton()
        subthread.execute(self.sensitize_subthread, (skelcontext, 
                                                     current_selection) )

    def sensitize_subthread(self, skelcontext, current_selection):
        debug.subthreadTest()
        # Locks are only allowed on the subthread, but GUI updates
        # must be on the main thread.
        (c,u,i,r)=(0,0,0,0)
        if skelcontext is not None and current_selection is not None:
            current_selection.begin_reading()
            if not skelcontext.defunct():
                try:
                    c = current_selection.clearable()
                    u = current_selection.undoable()
                    i = current_selection.invertable()
                    r = current_selection.redoable()
                finally:
                    current_selection.end_reading()
        mainthread.runBlock(self._set_buttons, (c,u,i,r))
            
    def _set_buttons(self, c,u,i,r):
        skelctxt = self.parent.getCurrentSkeleton()
        skelok = (skelctxt is not None and not skelctxt.query_reservation()
                  and not skelctxt.defunct())
        self.clear_button.set_sensitive(c and skelok)
        self.undo_button.set_sensitive(u and skelok)
        self.invert_button.set_sensitive(i and skelok)
        self.redo_button.set_sensitive(r and skelok)
        self.activemode().historybox.sensitize()
        self.activemode().ok_sensitize()
        gtklogger.checkpoint("skeleton selection page selection sensitized "
                             + self.activemode().name())
        
class HistoryBox:
    def __init__(self, set_callback, ok_callback):
        debug.mainthreadTest()
        self.gtk = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.set_callback = set_callback
        self.historian = historian.Historian(self.setCB, self.sensitize)

        # Buttons:  Previous, OK, and next.
        self.prevbutton = gtkutils.prevButton(margin_start=2)
        gtklogger.connect(self.prevbutton, "clicked", self.historian.prevCB)
        self.prevbutton.set_tooltip_text(
            "Recall the previous selection modification operation.")
        self.gtk.pack_start(self.prevbutton,
                            expand=False, fill=False, padding=0)

        self.okbutton = gtkutils.StockButton('gtk-ok', 'OK')
        gtklogger.setWidgetName(self.okbutton, 'OK')
        gtklogger.connect(self.okbutton, "clicked", ok_callback)
        self.gtk.pack_start(self.okbutton, expand=True, fill=True, padding=0)
        self.okbutton.set_tooltip_text(
            "Perform the selection modification operation.")
        self.okbutton.set_sensitive(False)
        
        self.nextbutton = gtkutils.nextButton(margin_end=2)
        gtklogger.connect(self.nextbutton, "clicked", self.historian.nextCB)
        self.nextbutton.set_tooltip_text(
            "Recall the next selection modification operation.")
        self.gtk.pack_start(self.nextbutton,
                            expand=False, fill=False, padding=0)
        
        
    def setCB(self, obj):
        if self.set_callback:
            self.set_callback(obj)

            
    def sensitize(self):
        debug.mainthreadTest()
        self.nextbutton.set_sensitive(self.historian.nextSensitive())
        self.prevbutton.set_sensitive(self.historian.prevSensitive())
            
########

ssp = SkeletonSelectionPage()
