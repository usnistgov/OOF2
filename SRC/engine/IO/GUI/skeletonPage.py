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
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import mainthread
from ooflib.common import subthread
from ooflib.common.IO import mainmenu
from ooflib.common.IO import parameter, reporter
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import historian
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import skeletoncontext
from ooflib.engine import skeletonelement
from ooflib.engine import skeletonmodifier

from gi.repository import Gtk
from gi.repository import Pango

# Define some convenience variables.
OOF = mainmenu.OOF
skeletonmenu = mainmenu.OOF.Skeleton
SkeletonModifier = skeletonmodifier.SkeletonModifier
itORthem = ["it", "them"]

class SkeletonPage(oofGUI.MainPage):
    def __init__(self):
        self.postponed_update = False
        oofGUI.MainPage.__init__(self, name="Skeleton", ordering=120,
                                 tip='Construct and modify mesh skeletons')

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             halign=Gtk.Align.CENTER, margin_top=2, spacing=2)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        self.skelwidget = whowidget.WhoWidget(whoville.getClass('Skeleton'),
                                              scope=self)
        label = Gtk.Label('Microstructure=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.skelwidget.gtk[0],
                             expand=True, fill=True, padding=0)
        label = Gtk.Label('Skeleton=', halign=Gtk.Align.END, margin_start=5)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.skelwidget.gtk[1],
                             expand=True, fill=True, padding=0)

        # Centered box of buttons
        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       halign=Gtk.Align.CENTER,
                       homogeneous=False, spacing=3)
        mainbox.pack_start(bbox, expand=False, fill=False, padding=0)

        self.newbutton = gtkutils.StockButton('document-new-symbolic', 'New...')
        gtklogger.setWidgetName(self.newbutton, "New")
        gtklogger.connect(self.newbutton, 'clicked', self.new_skeleton_CB)
        self.newbutton.set_tooltip_text(
            "Create a new skeleton from the current microstructure.")
        bbox.pack_start(self.newbutton, expand=True, fill=True, padding=0)
        
        self.simplebutton = Gtk.Button('Simple...')
        gtklogger.setWidgetName(self.simplebutton, "Simple")
        gtklogger.connect(self.simplebutton, 'clicked', self.simple_skeleton_CB)
        self.simplebutton.set_tooltip_text(
            "Create a new skeleton from the current microstructure in a naive"
            " fashion, by creating one quadrilateral or two triangular"
            " elements per pixel.  Material boundaries will be inherently"
            " jagged, which may cause errors in finite element solutions.")
        bbox.pack_start(self.simplebutton, expand=True, fill=True, padding=0)

        self.autobutton = Gtk.Button('Auto...')
        gtklogger.setWidgetName(self.autobutton, 'Auto')
        gtklogger.connect(self.autobutton, 'clicked', self.autoCB)
        self.autobutton.set_tooltip_text(
            "Create and automatically refine a Skeleton.")
        bbox.pack_start(self.autobutton, expand=True, fill=True, padding=0)
        
        self.renamebutton = gtkutils.StockButton('document-edit-symbolic',
                                                 'Rename...')
        gtklogger.setWidgetName(self.renamebutton, "Rename")
        gtklogger.connect(self.renamebutton, 'clicked', self.rename_skeleton_CB)
        self.renamebutton.set_tooltip_text("Rename the current skeleton.")
        bbox.pack_start(self.renamebutton, expand=True, fill=True, padding=0)

        self.copybutton = gtkutils.StockButton('edit-copy-symbolic', 'Copy...')
        gtklogger.setWidgetName(self.copybutton, 'Copy')
        gtklogger.connect(self.copybutton, 'clicked', self.copy_skeleton_CB)
        self.copybutton.set_tooltip_text("Copy the current skeleton.")
        bbox.pack_start(self.copybutton, expand=True, fill=True, padding=0)

        self.deletebutton = gtkutils.StockButton('edit-delete-symbolic',
                                                 'Delete')
        gtklogger.setWidgetName(self.deletebutton, 'Delete')
        gtklogger.connect(self.deletebutton, 'clicked', self.delete_skeletonCB)
        self.deletebutton.set_tooltip_text("Delete the current skeleton.")
        bbox.pack_start(self.deletebutton, expand=True, fill=True, padding=0)

        self.savebutton = gtkutils.StockButton('document-save-symbolic',
                                               'Save...')
        gtklogger.setWidgetName(self.savebutton, "Save")
        gtklogger.connect(self.savebutton, 'clicked', self.save_skeletonCB)
        self.savebutton.set_tooltip_text("Save the current skeleton to a file.")
        bbox.pack_start(self.savebutton, expand=True, fill=True, padding=0)
        
        mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                              wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(mainpane, 'notify::position')

        self.skelframe = Gtk.Frame(label="Skeleton Status", margin=2,
                                   shadow_type=Gtk.ShadowType.IN)
        mainpane.pack1(self.skelframe, resize=True, shrink=False)
        scroll = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN, margin=2)
        gtklogger.logScrollBars(scroll, "StatusScroll")
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.skelframe.add(scroll)
        self.skelinfo = Gtk.TextView(name="fixedfont", editable=False,
                                     cursor_visible=False,
                                     wrap_mode=Gtk.WrapMode.WORD)
        gtklogger.setWidgetName(self.skelinfo, "SkeletonText")
        ## TODO GTK3: I have no idea if this works.
        self.boldTag = self.skelinfo.get_buffer().create_tag(
            "bold", weight=Pango.Weight.BOLD)
        scroll.add(self.skelinfo)

        # End of left-side of skeleton info frame.

        # Start of right-side

        skelmodframe = Gtk.Frame(label="Skeleton Modification", margin=2,
                                 shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(skelmodframe, 'Modification')
        skelmodbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        skelmodframe.add(skelmodbox)

        self.skelmod = regclassfactory.RegisteredClassFactory(
            skeletonmodifier.SkeletonModifier.registry, title="Method= ",
            callback=self.skelmodCB, scope=self, name="Method", margin=2)
        self.historian = historian.Historian(self.skelmod.set,
                                             self.sensitizeHistory,
                                             setCBkwargs={'interactive':1})

        skelmodbox.pack_start(self.skelmod.gtk,
                              expand=True, fill=True, padding=0)

        # Buttons for "Previous", "OK", and "Next"
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       margin_left=2, margin_right=2)
        skelmodbox.pack_start(hbox, expand=False, fill=False, padding=0) 

        self.prevskelmodbutton = gtkutils.prevButton()
        gtklogger.connect(self.prevskelmodbutton, 'clicked', self.prevskelmod)
        self.prevskelmodbutton.set_tooltip_text(
            'Recall the previous skeleton modification operation.')
        hbox.pack_start(self.prevskelmodbutton,
                        expand=False, fill=False, padding=0)

        self.okbutton = gtkutils.StockButton('gtk-ok', 'OK')
        gtklogger.setWidgetName(self.okbutton, 'OK')
        gtklogger.connect(self.okbutton, 'clicked', self.okskelmod)
        self.okbutton.set_tooltip_text(
            'Perform the skeleton modification operation defined above.')
        hbox.pack_start(self.okbutton, expand=True, fill=True, padding=0)

        self.nextskelmodbutton = gtkutils.nextButton()
        gtklogger.connect(self.nextskelmodbutton, 'clicked', self.nextskelmod)
        self.nextskelmodbutton.set_tooltip_text(
            'Recall the next skeleton modification operation.')
        hbox.pack_start(self.nextskelmodbutton,
                        expand=False, fill=False, padding=0)

        # Buttons for "Undo", "Redo"
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2,
                       margin=2)
        skelmodbox.pack_start(hbox, expand=False, fill=False, padding=0)

        self.undobutton = gtkutils.StockButton('edit-undo-symbolic', 'Undo')
        gtklogger.setWidgetName(self.undobutton, 'Undo')
        gtklogger.connect(self.undobutton, 'clicked', self.undoskelmod)
        self.undobutton.set_tooltip_text(
            'Undo the latest skeleton modification.')
        hbox.pack_start(self.undobutton, expand=True, fill=False, padding=0)

        self.redobutton = gtkutils.StockButton('edit-redo-symbolic', 'Redo')
        gtklogger.setWidgetName(self.redobutton, 'Redo')
        gtklogger.connect(self.redobutton, 'clicked', self.redoskelmod)
        self.redobutton.set_tooltip_text(
            'Redo the latest undone skeleton modification.')
        hbox.pack_start(self.redobutton, expand=True, fill=False, padding=0)


        mainpane.pack2(skelmodframe, resize=False, shrink=False)
        # End of right-side

        self.sbcallbacks = [
            switchboard.requestCallback("made reservation",
                                        self.update_ok_button),
            switchboard.requestCallback("cancelled reservation",
                                        self.update_ok_button),
            switchboard.requestCallback("skeleton homogeneity changed",
                                        self.homogeneityChangeCB),
            switchboard.requestCallbackMain("Skeleton modified",
                                            self.recordModifier),
            switchboard.requestCallback(('who changed', 'Skeleton'),
                                        self.changeSkeleton),
            switchboard.requestCallbackMain(SkeletonModifier,
                                            self.updateskelmod),
            switchboard.requestCallbackMain(("new who", "Microstructure"),
                                            self.newMicrostructure),
            switchboard.requestCallbackMain(("new who", 'Skeleton'),
                                            self.newSkeleton),
            # Pages should catch the signal from updates to the widget
            # which don't originate on this page, e.g. deletions via
            # menu command.
            switchboard.requestCallback(self.skelwidget, self.skel_update),

            switchboard.requestCallback(('validity', self.skelmod),
                                        self.validityChangeCB),
            # Node movements can change the homogeneity of elements,
            # thus changing the state.
            switchboard.requestCallback("skeleton nodes moved", self.nodesMoved)
            ]

    def installed(self):       # called by oofGUI when switching pages
        subthread.execute(self.installed_subth)
    def installed_subth(self):
        self.sensitize()
        if self.postponed_update:
            self.postponed_update = False
            self.update(self.skelwidget.get_value(), locked=False)

    def skelmodCB(self, reg):
        subthread.execute(self.skelmodCB_subthread, (reg,))

    def skelmodCB_subthread(self, reg):
        self.historian.stateChangeCB(reg)
        self.sensitize()

    def legalityCheck(self):
        reg = self.skelmod.getRegistration()
        if hasattr(reg, "ok_illegal"):
            return 1
        return not self.currentSkeleton().illegal()

    def currentMSName(self):
        path = labeltree.makePath(mainthread.runBlock(self.skelwidget.get_value,
                                                      (), {'depth':1}))
        if path:
            return path[0]

    def currentSkeletonName(self):
        path = labeltree.makePath(
            mainthread.runBlock(self.skelwidget.get_value))
        if path:
            return path[-1]

    def currentSkeletonFullName(self):
        return mainthread.runBlock(self.skelwidget.get_value)

    def currentSkeletonContext(self):
        try:
            return skeletoncontext.skeletonContexts[self.currentSkeletonFullName()]
        except KeyError:
            return None
    def currentSkeleton(self):
        ctxt = self.currentSkeletonContext()
        if ctxt:
            return ctxt.getObject()

    def skel_update(self, *args, **kwargs):  # Switchboard "self.skelwidget"
        skelname = self.currentSkeletonFullName()
        self.update(skelname, locked=False)
        
    def nodesMoved(self, context):      # switchboard "skeleton nodes moved"
        cname = context.path()
        if self.currentSkeletonFullName() == cname:
            self.update(cname, locked=False)
        
    def newSkeleton(self, whoname):     # switchboard ("new who", "Skeleton")
        self.skelwidget.set_value(whoname)

    def changeSkeleton(self, skelcontext): # sb ('who changed', "Skeleton")
        try:
            path = skelcontext.path()
        except KeyError:
            return
        if self.currentSkeletonFullName() == path:
            self.update(path, locked=True)

    def newMicrostructure(self, msname): # sb ("new who", "Microstructure")
        # Switch to a new Microstructure only if there isn't a
        # currently selected Skeleton.
        if not self.currentSkeletonFullName():
            self.skelwidget.set_value(msname)

    # switchboard callback for "skeleton homogeneity changed", sent
    # when pixel groups or materials have changed in the
    # microstructure.
    def homogeneityChangeCB(self, skel_name):
        if self.currentSkeletonFullName()==skel_name:
            self.update(skel_name, locked=False)

    def recordModifier(self, path, modifier):
        if modifier:
            self.historian.record(modifier)

    def update(self, skelname, locked):
        debug.subthreadTest()
        # Most pages are updated when their info changes even if
        # they're not currently visible.  Because the Skeleton Page
        # displays the homogeneity which may be slow to compute, it's
        # not updated unless it's currently visible.
        if not self.is_current():       # not displayed in the GUI
            self.postponed_update = True
            return
        self.postponed_update = False
        skelpath = labeltree.makePath(skelname)
        if skelpath:
            skelctxt = skeletoncontext.skeletonContexts[skelpath]
            skel = skelctxt.getObject()
            ## Updating the state info is done in two stages, because
            ## the homogeneity index can take a while to compute.  In
            ## the first stage, the quick stuff is computed, and the
            ## homogeneity index is displayed as '????'. 
            if not locked:
                skelctxt.begin_reading()
            try:
                ms_name = skel.MS.name()
                nNodes = len(skel.nodes)
                nElements = len(skel.elements)
                illegalcount = skel.getIllegalCount()
                shapecounts = skel.countShapes()
                lr_periodicity = skel.left_right_periodicity
                tb_periodicity = skel.top_bottom_periodicity
                if config.dimension() == 3:
                    fb_periodicity = skel.front_back_periodicity
                else:
                    fb_periodicity = False
            finally:
                if not locked:
                    skelctxt.end_reading()
            mainthread.runBlock(self.writeInfoBuffer,
                                (nNodes, nElements, illegalcount, shapecounts,
                                 None, lr_periodicity, tb_periodicity,
                                 fb_periodicity))
            # Homogeneity Index stuff.  
            if not locked:
                skelctxt.begin_writing()
            try:
                homogIndex = skel.getHomogeneityIndex()
            finally:
                if not locked:
                    skelctxt.end_writing()
            mainthread.runBlock(self.writeInfoBuffer,
                                (nNodes, nElements, illegalcount, shapecounts,
                                 homogIndex, lr_periodicity, tb_periodicity,
                                 fb_periodicity))
        else:
            mainthread.runBlock(self.deleteInfoBuffer)
        self.sensitize()
            
    def deleteInfoBuffer(self):
        buffer = self.skelinfo.get_buffer()
        buffer.delete(buffer.get_start_iter(), buffer.get_end_iter())
        buffer.insert(buffer.get_end_iter(),
                      "No skeleton selected.\n")

    def writeInfoBuffer(self, nNodes, nElements, illegalcount, shapecounts,
                        homogIndex, left_right_periodicity,
                        top_bottom_periodicity, front_back_periodicity):
        # Called by update() to actually fill in the data on the
        # main thread.
        debug.mainthreadTest()
        buffer = self.skelinfo.get_buffer()
        buffer.delete(buffer.get_start_iter(), buffer.get_end_iter())
        if illegalcount > 0 :
            buffer.insert_with_tags(buffer.get_end_iter(),
                                    "WARNING: %d ILLEGAL ELEMENT%s.\n" %
                                    (illegalcount, "S"*(illegalcount!=1)),
                                    self.boldTag)
            buffer.insert(buffer.get_end_iter(),
                          "Element data is unreliable.\n")

            buffer.insert(buffer.get_end_iter(),
                          "Remove %s before proceeding.\n\n"
                          % itORthem[illegalcount!=1])

        buffer.insert(buffer.get_end_iter(), "No. of Nodes: %d\n" % nNodes)
        buffer.insert(buffer.get_end_iter(),
                      "No. of Elements: %d\n" % nElements)

        for name in skeletonelement.ElementShapeType.names:
            buffer.insert(buffer.get_end_iter(),
                          "No. of %ss: %d\n" % (name, shapecounts[name]))

        buffer.insert(buffer.get_end_iter(),
                          "Left-Right Periodicity: %s\n" % left_right_periodicity)
        buffer.insert(buffer.get_end_iter(),
                          "Top-Bottom Periodicity: %s\n" % top_bottom_periodicity)
        if config.dimension() == 3:
            buffer.insert(buffer.get_end_iter(),
                          "Front-Back Periodicity: %s\n" % front_back_periodicity)
            

        if homogIndex is not None:
            buffer.insert(buffer.get_end_iter(),
                          "Homogeneity Index: %s\n" % homogIndex)
        else:
            buffer.insert(buffer.get_end_iter(),
                          "Homogeneity Index: ????\n")

        gtklogger.checkpoint("skeleton page info updated")

    def new_skeleton_CB(self, gtkobj): # gtk callback for "New..." button
        paramset = filter(lambda x: x.name!='microstructure',
                          skeletonmenu.New.params)
        if parameterwidgets.getParameters(title='New skeleton', *paramset):
            skeletonmenu.New.callWithDefaults(
                microstructure=self.currentMSName())

    def simple_skeleton_CB(self, gtkobj): # gtk callback for "Simple..." button
        paramset = filter(lambda x: x.name!='microstructure',
                          skeletonmenu.Simple.params)
        if parameterwidgets.getParameters(title='Simple skeleton', *paramset):
            skeletonmenu.Simple.callWithDefaults(
                microstructure=self.currentMSName())
    def autoCB(self, gtkobj):           # gtk callback for "Auto..." button
        paramset = filter(lambda x: x.name!='microstructure',
                          skeletonmenu.Auto.params)
        if parameterwidgets.getParameters(title='Automatic skeleton',
                                          *paramset):
            skeletonmenu.Auto.callWithDefaults(
                microstructure=self.currentMSName())

    def copy_skeleton_CB(self, gtkobj): # gtk callback for "Copy..." button
        menuitem = skeletonmenu.Copy
        namearg = menuitem.get_arg('name')
        if parameterwidgets.getParameters(namearg, title='Copy skeleton'):
            menuitem.callWithDefaults(skeleton=self.skelwidget.get_value())

    def rename_skeleton_CB(self, gtkobj): # gtk callback for "Rename..." button
        menuitem = skeletonmenu.Rename
        namearg = menuitem.get_arg('name')
        namearg.value = labeltree.makePath(self.skelwidget.get_value())[-1]
        if parameterwidgets.getParameters(namearg, title='Rename skeleton'):
            menuitem.callWithDefaults(skeleton=self.skelwidget.get_value())

    def delete_skeletonCB(self, gtkobj): # gtk callback for Delete button.
        skelname = self.currentSkeletonName()
        if reporter.query("Delete skeleton %s?" % skelname,
                          "OK", "Cancel", default="OK")=="OK":
            menuitem = skeletonmenu.Delete
            menuitem.callWithDefaults(skeleton=self.skelwidget.get_value())

    def getSkeletonAvailability(self):
        try:
            currentSkel = self.skelwidget.get_value() # colon separated string
            ctxt = skeletoncontext.skeletonContexts[currentSkel]
            return not ctxt.query_reservation()
        except KeyError:
            return 1
        
    def sensitize(self):
        debug.subthreadTest()
        context = self.currentSkeletonContext()
        if context is not None:
            skelselected = True
            context.begin_reading()
            try:
                undoable = context.undoable()
                redoable = context.redoable()
                not_illegal = self.legalityCheck()
            finally:
                context.end_reading()
        else:
            skelselected = False
            undoable = redoable = False
            not_illegal = False
        mainthread.runBlock(self.sensitize_thread,
                            (skelselected, undoable, redoable, not_illegal))

    def sensitize_thread(self, skelselected, undoable, redoable, not_illegal):
        debug.mainthreadTest()
        self.okbutton.set_sensitive(skelselected and self.skelmod.isValid()
                                    and not_illegal)
        self.undobutton.set_sensitive(undoable)
        self.redobutton.set_sensitive(redoable)
        
        msclass = whoville.getClass('Microstructure')
        havems = msclass is not None and msclass.nActual() > 0
        self.newbutton.set_sensitive(havems)
        self.simplebutton.set_sensitive(havems)
        self.autobutton.set_sensitive(havems)
        self.deletebutton.set_sensitive(skelselected)
        self.renamebutton.set_sensitive(skelselected)
        self.copybutton.set_sensitive(skelselected)
        self.savebutton.set_sensitive(skelselected)

        if not self.getSkeletonAvailability():
            self.okbutton.set_sensitive(0)
            self.undobutton.set_sensitive(0)
            self.redobutton.set_sensitive(0)
        self.sensitizeHistory_thread()
        gtklogger.checkpoint("skeleton page sensitized")
        
    def sensitizeHistory(self):
        mainthread.runBlock(self.sensitizeHistory_thread)
    def sensitizeHistory_thread(self):
        debug.mainthreadTest()
        self.nextskelmodbutton.set_sensitive(self.historian.nextSensitive())
        self.prevskelmodbutton.set_sensitive(self.historian.prevSensitive())

    def validityChangeCB(self, validity):
        self.sensitize()

    def updateskelmod(self):
        self.skelmod.update(SkeletonModifier.registry)

    def currentFullSkeletonName(self):
        return self.skelwidget.get_value()
    
    def update_ok_button(self, who):
        if self.currentSkeletonContext() is who:
            self.sensitize()
            
    def okskelmod(self,gtkobj):
        path = self.skelwidget.get_value()
        modifier = self.skelmod.get_value()
        if path and modifier:
            OOF.Skeleton.Modify(skeleton=path, modifier=modifier)
        else:
            reporter.report("Can't modify!!!!")

    def prevskelmod(self,gtkobj):
        self.historian.prevCB()

    def nextskelmod(self,gtkobj):
        self.historian.nextCB()

    def undoskelmod(self,gtkobj):
        path = self.skelwidget.get_value()
        OOF.Skeleton.Undo(skeleton = path)

    def redoskelmod(self,gtkobj):
        path = self.skelwidget.get_value()
        OOF.Skeleton.Redo(skeleton = path)

    def save_skeletonCB(self, button):
        menuitem = mainmenu.OOF.File.Save.Skeleton
        skelname = self.skelwidget.get_value()
        params = filter(lambda x: x.name!="skeleton", menuitem.params)
        if parameterwidgets.getParameters(title='Save Skeleton "%s"' % skelname,
                                          *params):
            menuitem.callWithDefaults(skeleton=skelname)

# Create the page.
skeletonpage = SkeletonPage()

