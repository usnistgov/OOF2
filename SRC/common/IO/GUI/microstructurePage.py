# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import lock
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import microstructure
from ooflib.common import subthread
from ooflib.common.IO import mainmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import whowidget
from types import *
from gi.repository import Gtk
from gi.repository import Pango
import sys

if config.dimension()==2:
    pixstring = "pixel"
    Pixstring = "Pixel"
elif config.dimension()==3:
    pixstring = "voxel"
    Pixstring = "Voxel"

class MicrostructurePage(oofGUI.MainPage):
    def __init__(self):
        debug.mainthreadTest()
        self.built = False

        oofGUI.MainPage.__init__(
            self, name="Microstructure", ordering=10,
            tip="Define Microstructure and %s Group objects."%Pixstring)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(vbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER, margin_top=2)
        vbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        label = Gtk.Label('Microstructure=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        self.mswidget = whowidget.WhoWidget(microstructure.microStructures,
                                            callback=self.msCB)
        centerbox.pack_start(self.mswidget.gtk[0],
                             expand=False, fill=False, padding=0)
        
        # first row of ms buttons
        self.newbuttonbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                                    halign=Gtk.Align.CENTER,
                                    homogeneous=False, spacing=3)
        vbox.pack_start(self.newbuttonbox, expand=False, fill=False, padding=0)

        self.newbutton = gtkutils.StockButton("document-new-symbolic", 'New...')
        gtklogger.setWidgetName(self.newbutton, "New")
        gtklogger.connect(self.newbutton,'clicked', self.newEmptyCB)
        self.newbutton.set_tooltip_text(
            "Create a new microstructure that is NOT associated with images.")
        self.newbuttonbox.pack_start(self.newbutton,
                                     expand=True, fill=True, padding=0)
        
        # Other buttons can be added to the row of "New" buttons by
        # other modules.  When they're added, by addNewButton(), a
        # function can be specified for sensitizing the button.  This
        # is the list of those functions:
        self.sensitizeFns = []

        # Other modules can contribute strings to be displayed on the
        # info page.  This is the list of
        # MicrostructurePageInfoPlugIns that retrieve those strings.
        self.infoplugins = []

        # second row of ms buttons
        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER,
                            homogeneous=True, spacing=3)
        vbox.pack_start(centerbox, expand=False, fill=False, padding=0)

        self.renamebutton = gtkutils.StockButton("document-edit-symbolic",
                                                 'Rename...')
        gtklogger.setWidgetName(self.renamebutton, "Rename")
        gtklogger.connect(self.renamebutton, 'clicked', self.renameMSCB)
        self.renamebutton.set_tooltip_text(
            "Rename the current microstructure.")
        centerbox.pack_start(self.renamebutton,
                             expand=True, fill=True, padding=0)

        self.copybutton = gtkutils.StockButton("edit-copy-symbolic", 'Copy...')
        gtklogger.setWidgetName(self.copybutton, "Copy")
        gtklogger.connect(self.copybutton, 'clicked', self.copyMSCB)
        self.copybutton.set_tooltip_text("Copy the current microstructure.")
        centerbox.pack_start(self.copybutton,
                             expand=True, fill=True, padding=0)

        self.deletebutton = gtkutils.StockButton("edit-delete-symbolic",
                                                 'Delete')
        gtklogger.setWidgetName(self.deletebutton, "Delete")
        gtklogger.connect(self.deletebutton, 'clicked', self.deleteMSCB)
        self.deletebutton.set_tooltip_text(
                                  "Delete the current microstructure.")
        centerbox.pack_start(self.deletebutton,
                             expand=True, fill=True, padding=0)

        self.savebutton = gtkutils.StockButton("document-save-symbolic",
                                               'Save...')
        gtklogger.setWidgetName(self.savebutton, "Save")
        gtklogger.connect(self.savebutton, 'clicked', self.saveMSCB)
        self.savebutton.set_tooltip_text(
            "Save the current microstructure to a file.")
        centerbox.pack_start(self.savebutton,
                             expand=True, fill=True, padding=0)

        pane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                         wide_handle=True)
        gtklogger.setWidgetName(pane, "Pane")
        vbox.pack_start(pane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(pane, 'notify::position')

        #######
        
        infoframe = Gtk.Frame(
            label='Microstructure Info',
            margin_start=2, margin_end=gtkutils.handle_padding,
            margin_top=2, margin_bottom=2)
        infoframe.set_shadow_type(Gtk.ShadowType.IN)
        pane.pack1(infoframe, resize=True, shrink=False)
        scroll = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN, margin=2)
        gtklogger.logScrollBars(scroll, "InfoFrameScroll")
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        infoframe.add(scroll)
        self.infoarea = Gtk.TextView(name="fixedfont", margin=2,
                                     left_margin=5, right_margin=5,
                                     top_margin=5, bottom_margin=5)
        self.infoarea.set_editable(0)
        self.infoarea.set_cursor_visible(False)
        self.infoarea.set_wrap_mode(Gtk.WrapMode.WORD)
        scroll.add(self.infoarea)
        
        ########
        
        ## TODO: PixelGroup buttons should be desensitized when
        ## Microstructure is busy.

        self.grouplock = lock.Lock()
        groupframe = Gtk.Frame(
            label = '%s Groups'%Pixstring,
            margin_start=gtkutils.handle_padding, margin_end=2,
            margin_top=2, margin_bottom=2)
        gtklogger.setWidgetName(groupframe, "%sGroups"%Pixstring)
        groupframe.set_shadow_type(Gtk.ShadowType.IN)
        pane.pack2(groupframe, resize=True, shrink=False)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       margin=2)
        groupframe.add(hbox)
        # buttons on L side of pixel group list
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                       spacing=2)
        hbox.pack_start(vbox, expand=False, fill=False, padding=2)

        # frame for the list of groups
        frame = Gtk.Frame(shadow_type=Gtk.ShadowType.IN)
        hbox.pack_start(frame, expand=True, fill=True, padding=0)
        self.grparea = Gtk.Stack()
        gtklogger.setWidgetName(self.grparea, "Stack")
        frame.add(self.grparea)

        # only one of grplist and grpmsg is visible at a time
        self.grplist = chooser.ScrolledChooserListWidget( # list of pixel groups
            callback=self.listItemChosen, name="GroupList",
            vexpand=True, valign=Gtk.Align.FILL,
            shadow_type=Gtk.ShadowType.NONE)
        self.grparea.add(self.grplist.gtk)

        self.grpmsg = Gtk.Label() # helpful message when there are no grps
        gtklogger.setWidgetName(self.grpmsg, "Message")
        self.grparea.add(self.grpmsg)
        self.grparea.set_visible_child(self.grpmsg)

        self.newgroupbutton = Gtk.Button('New...')
        gtklogger.setWidgetName(self.newgroupbutton, "New")
        vbox.pack_start(self.newgroupbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.connect(self.newgroupbutton, 'clicked', self.newGroupButtonCB)
        self.newgroupbutton.set_tooltip_text(
            "Create a new empty %s group in the current microstructure."
            % pixstring)

        self.autogroupbutton = Gtk.Button('Auto...')
        gtklogger.setWidgetName(self.autogroupbutton, "Auto")
        vbox.pack_start(self.autogroupbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.connect(self.autogroupbutton, 'clicked',
                          self.autoGroupButtonCB)
        self.autogroupbutton.set_tooltip_text(
            "Automatically create groups for all pixels"
            " in the current microstructure with a statistical method.")

        self.renamegroupbutton = Gtk.Button('Rename...')
        gtklogger.setWidgetName(self.renamegroupbutton, "Rename")
        vbox.pack_start(self.renamegroupbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.connect(self.renamegroupbutton, 'clicked',
                         self.renameGroupButtonCB)
        self.renamegroupbutton.set_tooltip_text(
            "Rename the selected %s group." % pixstring)

        self.copygroupbutton = Gtk.Button('Copy...')
        gtklogger.setWidgetName(self.copygroupbutton, "Copy")
        vbox.pack_start(self.copygroupbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.connect(self.copygroupbutton, 'clicked',
                         self.copyGroupButtonCB)
        self.copygroupbutton.set_tooltip_text(
            "Create a new group containing the same %ss as the selected group."
            % pixstring)

        self.delgroupbutton = Gtk.Button('Delete')
        gtklogger.setWidgetName(self.delgroupbutton, "Delete")
        vbox.pack_start(self.delgroupbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.connect(self.delgroupbutton, 'clicked',
                         self.deleteGroupButtonCB)
        self.delgroupbutton.set_tooltip_text(
            "Delete the selected %s group from the microstructure." % pixstring)

        self.delallgroupsbutton = Gtk.Button('Delete All')
        gtklogger.setWidgetName(self.delallgroupsbutton, 'DeleteAll')
        vbox.pack_start(self.delallgroupsbutton,
                        expand=False, fill=False, padding=0)
        gtklogger.connect(self.delallgroupsbutton, 'clicked',
                          self.deleteAllGroupsButtonCB)
        self.delallgroupsbutton.set_tooltip_text(
            "Delete all pixel groups from the microstructure.")

        self.meshablebutton = Gtk.CheckButton('Meshable')
        gtklogger.setWidgetName(self.meshablebutton, "Meshable")
        vbox.pack_start(self.meshablebutton,
                        expand=False, fill=False, padding=0)
        self.meshablesignal = gtklogger.connect(self.meshablebutton, 'clicked',
                                                self.meshableGroupCB)
        self.meshablebutton.set_tooltip_text(
            "Should adaptive meshes follow the boundaries of the selected %s group?"
            % pixstring)


        # buttons on rhs of pixelgroup list
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        hbox.pack_start(vbox, expand=False, fill=False, padding=2)

        self.addbutton = Gtk.Button('Add')
        gtklogger.setWidgetName(self.addbutton, "Add")
        vbox.pack_start(self.addbutton, expand=False, fill=False, padding=0)
        gtklogger.connect(self.addbutton, 'clicked', self.addPixelsCB)
        self.addbutton.set_tooltip_text(
            "Add the currently selected %ss to the selected group." % pixstring)

        self.removebutton = Gtk.Button('Remove')
        gtklogger.setWidgetName(self.removebutton, "Remove")
        vbox.pack_start(self.removebutton, expand=False, fill=False, padding=0)
        gtklogger.connect(self.removebutton, 'clicked', self.removePixelsCB)
        self.removebutton.set_tooltip_text(
            "Remove the currently selected %ss from the selected group."
            % pixstring)

        self.clearbutton = Gtk.Button('Clear')
        gtklogger.setWidgetName(self.clearbutton, "Clear")
        vbox.pack_start(self.clearbutton, expand=False, fill=False, padding=0)
        gtklogger.connect(self.clearbutton, 'clicked', self.clearPixelsCB)
        self.clearbutton.set_tooltip_text(
            "Reset the selected group by removing all the %ss from the group."
            % pixstring)
        
        self.infobutton = Gtk.Button('Info')
        gtklogger.setWidgetName(self.infobutton, "Info")
        vbox.pack_start(self.infobutton, expand=False, fill=False, padding=0)
        gtklogger.connect(self.infobutton, 'clicked', self.queryPixelsCB)
        self.infobutton.set_tooltip_text(
            "Display information about the selected group in the Messages window.")        

        self.built = True

        self.sbcallbacks = [
            switchboard.requestCallback('new pixel group', self.newpixgrp),
            switchboard.requestCallback('destroy pixel group', self.destpixgrp),
            #
            switchboard.requestCallback('changed pixel group', self.destpixgrp),
            switchboard.requestCallback('changed pixel groups', self.chngdgrps),
            switchboard.requestCallback(('new who', 'Microstructure'),
                                        self.newwhoMS),
            switchboard.requestCallback(('new who', 'Image'), self.newwhoImage),
            switchboard.requestCallback(('rename who', 'Image'),
                                        self.displayMSInfo),
            switchboard.requestCallback('remove who', self.removewho),
            switchboard.requestCallback('renamed pixel group',
                                        self.renamepixgrp),
            switchboard.requestCallback('pixel selection changed',
                                        self.selectionchanged),
            switchboard.requestCallback(
            'images changed in microstructure', self.displayMSInfo)
            ]
        # Don't call redisplay_all here!  It would be called before
        # the main gtk loop starts, so the mainthread/subthread
        # mechanism won't be in place, and the grouplock will complain
        # about potential deadlocking.

    def redisplay_all(self):
        self.rebuild_grouplist()        # hides either grplist or grpmsg.
        self.displayMSInfo()
        self.sensitize()

    def installed(self):
        # If redisplay_all is called by show() rather than by shown()
        # it can be called by gui start up code, which may be running
        # concurrently with other start up operations, including
        # gtklogging initialization.  If that happens, the recording
        # of checkpoints reached by redisplay_all will depend on race
        # conditions.  So redisplay_all must be called by shown(),
        # which is guaranteed (less likely?) to be called before gui
        # initialization is complete.
        subthread.execute(self.redisplay_all)
        
    def currentMSName(self):
        return mainthread.runBlock(self.mswidget.get_value)

    def currentMScontext(self):
        msname = self.currentMSName()
        if msname:
            try:
                return microstructure.microStructures[msname]
            except KeyError:
                return None

    def currentMS(self):
        ctxt = self.currentMScontext()
        if ctxt:
            return ctxt.getObject()
        
    def currentGroupName(self):
        return mainthread.runBlock(self.grplist.get_value)

    def currentGroup(self):
        name = self.currentGroupName()
        if name:
            ms = self.currentMS()
            if ms is not None:
                return ms.findGroup(name)

    def rebuild_grouplist(self):
        debug.subthreadTest()
        mscontext = self.currentMScontext()
        msg = None
        if mscontext is not None:
            mscontext.begin_reading()
            ms = mscontext.getObject()
            try:
                if ms.nGroups() > 0:
                    grpnames = ms.groupNames()
                    dispnames = grpnames[:]
                    for i in range(len(grpnames)):
                        grpname = grpnames[i]
                        grp = ms.findGroup(grpname)
                        dispnames[i] += " (%d %s%s" % (len(grp), pixstring,
                                                          "s"*(len(grp)!=1))
                        if grp.is_meshable():
                            dispnames[i] += ", meshable)"
                        else:
                            dispnames[i] += ")"
                else:
                    msg = 'No %s groups defined!'%pixstring
            finally:
                mscontext.end_reading()
        else:                           # ms is None
            msg = 'No Microstructure defined!'
        if msg:
            mainthread.runBlock(self.set_group_message, (msg,))
        else:
            mainthread.runBlock(self.set_group_list, (grpnames, dispnames))
        self.setMeshableButton()

    def set_group_message(self, msg):
        debug.mainthreadTest()
        self.grpmsg.set_text(msg)
        self.grparea.set_visible_child(self.grpmsg)
    def set_group_list(self, grpnames, dispnames=[]):
        debug.mainthreadTest()
        self.grplist.update(grpnames, dispnames)
        self.grparea.set_visible_child(self.grplist.gtk)

    def addNewButton(self, gtkobj, sensitizefn):
        debug.mainthreadTest()
        self.newbuttonbox.pack_start(gtkobj, expand=True, fill=True, padding=0)
        gtkobj.show()
        if sensitizefn is not None:
            self.sensitizeFns.append(sensitizefn)

    def addMicrostructureInfo(self, msinfoplugin):
        self.infoplugins.append(msinfoplugin)
        self.infoplugins.sort()
        return msinfoplugin

    def displayMSInfo(self, *args):
        # *args is given because this is used as a switchboard
        # callback for ('rename who', 'Image') as well as being called
        # directly.  This indicates either slovenliness or efficiency
        # on the part of the programmer.
        debug.subthreadTest()
        mscontext = self.currentMScontext()
        text = ""
        if mscontext is not None:
            mscontext.begin_reading()
            try:
                # ms might be None if the context was destroyed while
                # we were waiting for the read lock.
                ms = mscontext.getObject()
                if ms is not None:
                    size = ms.sizeInPixels()
                    if config.dimension() == 2:
                        text += 'Pixel size: %dx%d\n' % (size.x, size.y)
                        size = ms.size()
                        text += 'Physical size: %sx%s\n' % (size.x, size.y)
                    elif config.dimension() == 3:
                        text += 'Voxel size: %dx%dx%d\n' % (
                            size.x, size.y, size.z)
                        size = ms.size()
                        text += 'Physical size: %sx%sx%s\n' % (
                            size.x, size.y, size.z)
                    imagenames = ms.imageNames()
                    if imagenames:
                        text += 'Images:\n'
                        for name in imagenames:
                            text += '  ' + name + '\n'
                    for infoplugin in self.infoplugins:
                        plugintext = infoplugin(mscontext)
                        if plugintext:
                            text += plugintext + '\n'
            finally:
                mscontext.end_reading()
        mainthread.runBlock(self.infoarea.get_buffer().set_text, (text,))

    def setMeshableButton(self):
        debug.subthreadTest()
        mscontext = self.currentMScontext()
        if mscontext:
            mscontext.begin_reading()
            try:
                grp = self.currentGroup()
                meshable = grp is not None and grp.is_meshable()
            finally:
                mscontext.end_reading()
        else:
            meshable = False
        mainthread.runBlock(self.setMeshableButton_thread, (meshable,))
    def setMeshableButton_thread(self, meshable):
        debug.mainthreadTest()
        self.meshablesignal.block()
        self.meshablebutton.set_active(meshable)
        self.meshablesignal.unblock()
        gtklogger.checkpoint("meshable button set")

    def sensitize(self):
        debug.subthreadTest()
        ms_available = False
        grp_selected = False
        nonemptygrp = False
        pixelsselected = False
        ngrps = 0
        msctxt = self.currentMScontext()
        if msctxt:
            # TODO: This is incorrect.  Don't call begin_reading here.
            # The ms may be doing some long calculation, and the
            # buttons should be desensitized because of it.  Calling
            # begin_reading will lock and prevent densensitization
            # until after the calculation is done!
            msctxt.begin_reading()
            try:
                ms = msctxt.getObject()
                if ms is not None:
                    ms_available = True
                    grp = self.currentGroup()
                    grp_selected = (grp is not None) and ms_available
                    nonemptygrp = grp_selected and len(grp) > 0
                    pixelsselected = ms.pixelselection.size() > 0
                    ngrps = ms.nGroups()
            finally:
                msctxt.end_reading()
        mainthread.runBlock(self.sensitize_thread,
                            (ms_available, grp_selected, pixelsselected,
                             nonemptygrp, ngrps))
    def sensitize_thread(self, ms_available, grp_selected, pixelsselected,
                         nonemptygrp, ngrps):
        debug.mainthreadTest()
        self.renamebutton.set_sensitive(ms_available)
        self.copybutton.set_sensitive(ms_available)
        self.deletebutton.set_sensitive(ms_available)
        self.savebutton.set_sensitive(ms_available)

        self.newgroupbutton.set_sensitive(ms_available)
        self.autogroupbutton.set_sensitive(ms_available)
        self.renamegroupbutton.set_sensitive(grp_selected)
        self.copygroupbutton.set_sensitive(grp_selected)
        self.delgroupbutton.set_sensitive(grp_selected)
        self.delallgroupsbutton.set_sensitive(ngrps > 0)
        self.meshablebutton.set_sensitive(grp_selected)
        self.infobutton.set_sensitive(grp_selected)

        self.addbutton.set_sensitive(grp_selected and pixelsselected)
        self.removebutton.set_sensitive(nonemptygrp and pixelsselected)
        self.clearbutton.set_sensitive(nonemptygrp)

        for fn in self.sensitizeFns:
            fn()
        gtklogger.checkpoint("microstructure page sensitized")

    def selectionchanged(self):         # switchboard 'pixel selection changed'
        self.sensitize()

    ###############################

    def renameMSCB(self, button):
        menuitem = mainmenu.OOF.Microstructure.Rename
        namearg = menuitem.get_arg('name')
        namearg.value = self.currentMSName()
        if parameterwidgets.getParameters(
                namearg,
                parentwindow=self.gtk.get_toplevel(),
                title='Rename Microstructure '+self.currentMSName()):
            menuitem.callWithDefaults(microstructure=self.currentMSName())

    def copyMSCB(self, button):
        menuitem = mainmenu.OOF.Microstructure.Copy
        namearg = menuitem.get_arg('name')
        if parameterwidgets.getParameters(namearg,
                                          parentwindow=self.gtk.get_toplevel(),
                                          title='Copy microstructure'):
            menuitem.callWithDefaults(microstructure=self.currentMSName())

    def deleteMSCB(self, button):
        if reporter.query("Really delete %s?" % self.currentMSName(),
                          "No", default="Yes",
                          parentwindow=self.gtk.get_toplevel()) == "Yes":
            mainmenu.OOF.Microstructure.Delete(
                microstructure=self.currentMSName())

    def listItemChosen(self, name, interactive): # Chooser callback
        if self.built:
            subthread.execute(self.listItemChosen_thread, (name,))
    def listItemChosen_thread(self, name):
        self.grouplock.acquire()
        try:
            self.sensitize()
            self.setMeshableButton()
        finally:
            self.grouplock.release()
        
    def newpixgrp(self, group):  # switchboard callback 'new pixel group'
        ## TODO: This should check the group's Microstructure, and not
        ## do anything unless it is the page's current Microstructure.
        ## The code as it is now will change the selected group if
        ## it's in a different Microstructure but has the same name as
        ## one in the current Microstructure.
        self.grouplock.acquire()
        try:
            self.rebuild_grouplist()
            # This makes the newly added pixel group automatically selected.
            mainthread.runBlock(self.grplist.set_selection, (group.name(),))
            self.setMeshableButton()
            self.sensitize()
        finally:
            self.grouplock.release()

    def destpixgrp(self, group, ms_name):
        # switchboard 'destroy pixel group' or 'changed pixel group'
        self.grouplock.acquire()
        try:
            if ms_name==self.currentMSName():
                self.rebuild_grouplist()
                self.sensitize()
        finally:
            self.grouplock.release()
    def chngdgrps(self, ms_name):       # 'changed pixel groups'
        self.grouplock.acquire()
        try:
            if ms_name == self.currentMSName():
                self.rebuild_grouplist()
                self.sensitize()
        finally:
            self.grouplock.release()
    
    def newwhoMS(self, whoname): # switchboard ('new who', 'Microstructure')
        # whoname is a list of strings
        self.grouplock.acquire()
        try:
            mainthread.runBlock(self.mswidget.set_value, (whoname,))
            self.rebuild_grouplist()
            self.displayMSInfo()
            self.sensitize()
        finally:
            self.grouplock.release()

    def newwhoImage(self, whoname):     # switchboard ('new who', 'Image')
        self.displayMSInfo()            # displays image name
        self.sensitize()

    def removewho(self, whoclassname, whoname): # switchboard 'remove who'
        if whoclassname == 'Microstructure':
            self.grouplock.acquire()
            try:
                self.rebuild_grouplist()
                self.displayMSInfo()
                self.sensitize()
            finally:
                self.grouplock.release()
        elif whoclassname == 'Image':
            self.sensitize()

    def msCB(self, *args):              # whowidget callback
        subthread.execute(self.redisplay_all)

    def newEmptyCB(self, *args):
        menuitem = mainmenu.OOF.Microstructure.New
        if parameterwidgets.getParameters(title='Create Microstructure',
                                          parentwindow=self.gtk.get_toplevel(),
                                          *menuitem.params):
            menuitem.callWithDefaults()

    def newGroupButtonCB(self, button):
        menuitem = mainmenu.OOF.PixelGroup.New
        nameparam = menuitem.get_arg('name')
        if parameterwidgets.getParameters(
                nameparam,
                parentwindow=self.gtk.get_toplevel(),
                title='Create new %s group'%pixstring):
            menuitem.callWithDefaults(microstructure=self.currentMSName())

    def autoGroupButtonCB(self, button):
        # Use WidgetScope setData/findData to tell the WhoWidgets in
        # the params that the Microstructure has to be the current
        # Microstructure.  We can't just set a Microstructure
        # parameter and exclude its widget from the dialog in the
        # usual way, because the WhoParams aren't direct parameters
        # of this menu item, and the WhoWidgets are inside
        # PixelDistributionFactory RCFs.
        # scopedata key,value pairs are passed to WidgetScope.setData().
        # WidgetScope.findData() searches its own data and that of its parents.
        menuitem = mainmenu.OOF.PixelGroup.AutoGroup
        scopedata = {'fixed whoclass': ('Microstructure', self.currentMSName())}
        if parameterwidgets.getParameters(title="AutoGroup", scope=self,
                                          parentwindow=self.gtk.get_toplevel(),
                                          data=scopedata, *menuitem.params):
            menuitem.callWithDefaults()

    def renameGroupButtonCB(self, button):
        menuitem = mainmenu.OOF.PixelGroup.Rename
        nameparam = menuitem.get_arg('new_name')
        nameparam.value = self.currentGroupName()
        if parameterwidgets.getParameters(
                nameparam,
                parentwindow=self.gtk.get_toplevel(),
                title = 'Rename %sgroup '%pixstring + self.currentGroupName()):
            menuitem.callWithDefaults(
                microstructure=self.currentMSName(),
                group=self.currentGroupName())

    def renamepixgrp(self, group, oldname, newname):
        # switchboard 'rename pixel group'
        debug.subthreadTest()
        self.grouplock.acquire()
        try:
            mscontext = self.currentMScontext()
            if mscontext:
                mscontext.begin_reading()
                try:
                    ms = mscontext.getObject()
                    ok = group.name() in ms.groupNames()
                finally:
                    mscontext.end_reading()
                if ok:
                    # Ensure that the new pixel group is selected.
                    self.rebuild_grouplist()
                    mainthread.runBlock(self.grplist.set_selection, (newname,))
                    self.sensitize()
        finally:
            self.grouplock.release()

    def deleteGroupButtonCB(self, button):
        if reporter.query("Really delete %s?" % self.currentGroupName(),
                          "No", default="Yes",
                          parentwindow=self.gtk.get_toplevel()) == "Yes":
            mainmenu.OOF.PixelGroup.Delete(microstructure=self.currentMSName(),
                                           group=self.currentGroupName())

    def deleteAllGroupsButtonCB(self, button):
        if reporter.query("Really delete all pixel groups?", "No",
                          default="Yes",
                          parentwindow=self.gtk.get_toplevel()) == "Yes":
            mainmenu.OOF.PixelGroup.DeleteAll(
                microstructure=self.currentMSName())

    def copyGroupButtonCB(self, button):
        menuitem = mainmenu.OOF.PixelGroup.Copy
        nameparam = menuitem.get_arg('name')
        if parameterwidgets.getParameters(
                nameparam,
                parentwindow=self.gtk.get_toplevel(),
                title='Copy group '+self.currentGroup().name()):
            menuitem.callWithDefaults(microstructure=self.currentMSName(),
                                      group=self.currentGroupName())

    def meshableGroupCB(self, button):
        self.meshablesignal.block()
        mainmenu.OOF.PixelGroup.Meshable(microstructure=self.currentMSName(),
                                group=self.currentGroupName(),
                                meshable=self.meshablebutton.get_active())
        self.meshablesignal.unblock()

    def addPixelsCB(self, button):
        mainmenu.OOF.PixelGroup.AddSelection(
            microstructure=self.currentMSName(),
            group=self.currentGroupName())

    def removePixelsCB(self, button):
        mainmenu.OOF.PixelGroup.RemoveSelection(
            microstructure=self.currentMSName(),
            group=self.currentGroupName())

    def clearPixelsCB(self, button):
        mainmenu.OOF.PixelGroup.Clear(microstructure=self.currentMSName(),
                             group=self.currentGroupName())

    def queryPixelsCB(self, button):
        mainmenu.OOF.PixelGroup.Query(microstructure=self.currentMSName(),
                             group=self.currentGroupName())

    def saveMSCB(self, button):
        menuitem = mainmenu.OOF.File.Save.Microstructure
        msname = self.currentMSName()
        if parameterwidgets.getParameters(
                menuitem.get_arg('filename'),
                menuitem.get_arg('mode'),
                menuitem.get_arg('format'),
                parentwindow=self.gtk.get_toplevel(),
                title="Save Microstructure '%s'" % msname):
            menuitem.callWithDefaults(microstructure=msname)

mp = MicrostructurePage()

#######################################

## Extension mechanisms

# Add a button (or any other gtk widget) to the row of "New..."
# buttons.  sensitizefn will be called when the page's components are
# sensitized, and should do whatever's appropriate to the new widget.

def addNewButton(gtkobj, sensitizefn=None):
    mp.addNewButton(gtkobj, sensitizefn)

# Add more info to the info pane.  The callback will be called with
# the Microstructure context as an argument, and should return a
# string, or None.  addMicrostructureInfo returns a
# MicrostructurePageInfoPlugIn object whose update() method can be
# called to force the info pane to redraw.

def addMicrostructureInfo(callback, ordering):
    return mp.addMicrostructureInfo(MicrostructurePageInfoPlugIn(callback,
                                                                 ordering))
class MicrostructurePageInfoPlugIn:
    def __init__(self, callback, ordering):
        self.ordering = ordering
        self.callback = callback
    def __call__(self, ms):
        return self.callback(ms)
    def __cmp__(self, other):
        return cmp(self.ordering, other.ordering)
    def update(self):
        mp.displayMSInfo()

    
