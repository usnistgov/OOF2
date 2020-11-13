# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# GUI page for manipulating pixel groups.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.common import activeareamod
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import microstructure
from ooflib.common import utils
from ooflib.common.IO import mainmenu
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import historian
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from gi.repository import Gtk

class ActiveAreaPage(oofGUI.MainPage):
    def __init__(self):
        self.built = False
        oofGUI.MainPage.__init__(self, name="Active Area",
                                 ordering=71.1,
                                 tip="Modify active area.")

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        # Microstructure widget, centered at the top of the page.
        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER, margin_top=2)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        label = Gtk.Label('Microstructure=',
                          halign=Gtk.Align.END, hexpand=False)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        self.mswidget = whowidget.WhoWidget(microstructure.microStructures,
                                            scope=self)
        centerbox.pack_start(self.mswidget.gtk[0], expand=False, fill=False,
                             padding=0)

        mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                             wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(mainpane, 'notify::position')

        # Active area status in the left half of the main pane.
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2,
                       margin_start=2, margin_end=gtkutils.handle_padding,
                       margin_top=2, margin_bottom=2)
        mainpane.pack1(vbox, resize=True, shrink=False)
        aasframe = Gtk.Frame(label="Active Area Status")
        aasframe.set_shadow_type(Gtk.ShadowType.IN)
        vbox.pack_start(aasframe, expand=False, fill=False, padding=0)
        aasframe2 = Gtk.Frame(margin=2)
        aasframe.add(aasframe2)
        self.aainfo = Gtk.TextView(name="fixedfont",
                                   editable=False,
                                   cursor_visible=False,
                                   wrap_mode=Gtk.WrapMode.WORD,
                                   left_margin=10, right_margin=10,
                                   top_margin=2, bottom_margin=2)
        gtklogger.setWidgetName(self.aainfo, "Status")
        aasframe2.add(self.aainfo)

        naaframe = Gtk.Frame(label="Named Active Areas")
        naaframe.set_shadow_type(Gtk.ShadowType.IN)
        vbox.pack_start(naaframe, expand=True, fill=True, padding=0)
        naabox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        naaframe.add(naabox)
        self.aalist = chooser.ScrolledChooserListWidget(
            callback=self.aalistCB, dbcallback=self.aalistCB2,
            name="NamedAreas", margin=2)
        naabox.pack_start(self.aalist.gtk, expand=True, fill=True, padding=0)
        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                       spacing=2, margin=2)
        naabox.pack_start(bbox, expand=False, fill=False, padding=0)
        self.storebutton = Gtk.Button("Store...")
        bbox.pack_start(self.storebutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.storebutton, "Store")
        gtklogger.connect(self.storebutton, 'clicked', self.storeCB)
        self.storebutton.set_tooltip_text(
            "Save the current active area for future use.")
        self.renamebutton = Gtk.Button("Rename...")
        bbox.pack_start(self.renamebutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.renamebutton, "Rename")
        gtklogger.connect(self.renamebutton, 'clicked', self.renameCB)
        self.renamebutton.set_tooltip_text(
            "Rename the selected saved active areas.")
        self.deletebutton = Gtk.Button("Delete")
        bbox.pack_start(self.deletebutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.deletebutton, "Delete")
        gtklogger.connect(self.deletebutton, 'clicked', self.deleteCB)
        self.deletebutton.set_tooltip_text(
            "Delete the selected saved active areas.")
        self.restorebutton = Gtk.Button("Restore")
        bbox.pack_start(self.restorebutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.restorebutton, "Restore")
        gtklogger.connect(self.restorebutton, 'clicked', self.restoreCB)
        self.restorebutton.set_tooltip_text(
            "Use the selected saved active areas.")
        
        # Active area modification methods in the right half of the main pane
        modframe = Gtk.Frame(label="Active Area Modification",
                             margin_start=gtkutils.handle_padding,
                             margin_end=2, margin_top=2, margin_bottom=2)
        gtklogger.setWidgetName(modframe, "Modify")
        modframe.set_shadow_type(Gtk.ShadowType.IN)
        mainpane.pack2(modframe, resize=False, shrink=False)
        modbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                         spacing=2, margin=2)
        modframe.add(modbox)
        self.activeareaModFactory = regclassfactory.RegisteredClassFactory(
            activeareamod.ActiveAreaModifier.registry, title="Method:",
            scope=self, name="Method", margin=2,
            shadow_type=Gtk.ShadowType.NONE)
        modbox.pack_start(self.activeareaModFactory.gtk,
                          expand=True, fill=True, padding=0)
        self.historian = historian.Historian(self.activeareaModFactory.set,
                                             self.sensitizeHistory,
                                             setCBkwargs={'interactive':1})
        self.activeareaModFactory.set_callback(self.historian.stateChangeCB)

        # Prev, OK, and Next buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        modbox.pack_start(hbox, expand=False, fill=False, padding=0)
        self.prevbutton = gtkutils.prevButton()
        hbox.pack_start(self.prevbutton, expand=False, fill=False, padding=2)
        gtklogger.connect(self.prevbutton, 'clicked', self.historian.prevCB)
        self.prevbutton.set_tooltip_text(
            'Recall the previous active area modification operation.')
        self.okbutton = gtkutils.StockButton("gtk-ok", "OK")
        hbox.pack_start(self.okbutton, expand=True, fill=True, padding=2)
        gtklogger.setWidgetName(self.okbutton, "OK")
        gtklogger.connect(self.okbutton, 'clicked', self.okbuttonCB)
        self.okbutton.set_tooltip_text(
            'Perform the active area modification operation defined above.')
        self.nextbutton = gtkutils.nextButton()
        hbox.pack_start(self.nextbutton, expand=False, fill=False, padding=2)
        gtklogger.connect(self.nextbutton, 'clicked', self.historian.nextCB)
        self.nextbutton.set_tooltip_text(
            "Recall the next active area modification operation.")

        # Undo, Redo, Override
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        modbox.pack_start(hbox, expand=False, fill=False, padding=0)
        self.undobutton = gtkutils.StockButton("edit-undo-symbolic", "Undo")
        hbox.pack_start(self.undobutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.undobutton, "Undo")
        gtklogger.connect(self.undobutton, 'clicked', self.undoCB)
        self.undobutton.set_tooltip_text("Undo the previous operation.")

        self.redobutton = gtkutils.StockButton("edit-redo-symbolic", "Redo")
        hbox.pack_start(self.redobutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.redobutton, "Redo")
        gtklogger.connect(self.redobutton, 'clicked', self.redoCB)
        self.redobutton.set_tooltip_text("Redo an undone operation.")

        self.overridebutton = Gtk.ToggleButton('Override')
        hbox.pack_start(self.overridebutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.overridebutton, "Override")
        self.overridesignal = gtklogger.connect(self.overridebutton,
                                               'clicked', self.overrideCB)
        self.overridebutton.set_tooltip_text(
            "Temporarily activate the entire microstructure.")

        # Switchboard signals
        self.sbcallbacks = [
            switchboard.requestCallback(self.mswidget,
                                        self.mswidgetCB),
            switchboard.requestCallback("active area modified",
                                        self.aamodified),
            switchboard.requestCallbackMain("stored active areas changed",
                                            self.storedAAChanged),
            switchboard.requestCallbackMain(('validity',
                                             self.activeareaModFactory),
                                            self.validityChangeCB)
            ]

        self.built = True

    def installed(self):
        self.sensitize()
        self.sensitizeHistory()
        
    def getCurrentMSName(self):
        return self.mswidget.get_value()
    def getCurrentMS(self):
        try:
            return microstructure.microStructures[self.getCurrentMSName()]
        except KeyError:
            pass
    def getCurrentActiveArea(self):
        return self.aalist.get_value()

    # Callback functions for active area modification

    def okbuttonCB(self, button):
        modmeth = self.activeareaModFactory.getRegistration()
        if modmeth is not None:
            self.activeareaModFactory.set_defaults()
            menuitem = getattr(mainmenu.OOF.ActiveArea,
                               utils.space2underscore(modmeth.name()))
            menuitem.callWithDefaults(microstructure=self.getCurrentMSName())

    def undoCB(self, button):
        mainmenu.OOF.ActiveArea.Undo.callWithDefaults(
            microstructure=self.getCurrentMSName())

    def redoCB(self, button):
        mainmenu.OOF.ActiveArea.Redo.callWithDefaults(
            microstructure=self.getCurrentMSName())

    def overrideCB(self, button):
        mainmenu.OOF.ActiveArea.Override(microstructure=self.getCurrentMSName(),
                                         override=button.get_active())
        
    def mswidgetCB(self, *args, **kwargs): # switchboard self.mswidget
        # called only on a subthread
        self.updateAAInfo()
        mainthread.runBlock(self.updateAAList)
        self.sensitize()
        self.setOverrideButton()

    def aalistCB(self, name, interactive): # activearealist callback
        if self.built:
            self.sensitize()

    def aalistCB2(self, name):          # activearealist double-click callback
        self.sensitize()
        self.restoreCB(None)
        
    def storeCB(self, button):
        menuitem = mainmenu.OOF.ActiveArea.Store
        if parameterwidgets.getParameters(menuitem.get_arg('name'),
                                          title="Store the active area",
                                          parentwindow=self.gtk.get_toplevel()):
            menuitem.callWithDefaults(microstructure=self.getCurrentMSName())

    def renameCB(self, button):
        menuitem = mainmenu.OOF.ActiveArea.Rename
        namearg = menuitem.get_arg('newname')
        namearg.value = self.getCurrentActiveArea()
        oldname = self.getCurrentActiveArea()
        if parameterwidgets.getParameters(
                menuitem.get_arg('newname'),
                title="Rename active area '%s'" % oldname,
                parentwindow=self.gtk.get_toplevel()):
            menuitem.callWithDefaults(microstructure=self.getCurrentMSName(),
                                      oldname=oldname)

    def deleteCB(self, button):
        if reporter.query("Really delete %s?" % self.getCurrentActiveArea(),
                          "No", default="Yes",
                          parentwindow=self.gtk.get_toplevel()) == "Yes":
            mainmenu.OOF.ActiveArea.Delete(
                microstructure=self.getCurrentMSName(),
                name=self.getCurrentActiveArea())

    def restoreCB(self, button):
        mainmenu.OOF.ActiveArea.Restore(microstructure=self.getCurrentMSName(),
                               name=self.getCurrentActiveArea())
        

    def aamodified(self, modifier):
        # callback for switchboard signal "active area modified"
        # called only on a subthread
        self.updateAAInfo()
        self.updateHistory(modifier)
        self.sensitize()
        self.setOverrideButton()

    def storedAAChanged(self, name):
        # callback for switchboard signal "stored active areas changed"
        # called only on the main thread
        debug.mainthreadTest()
        self.updateAAList()
        try:
            self.aalist.set_selection(name)
        except KeyError:
            pass
        self.sensitize()

    def updateAAList(self):             # update list of named active areas
        debug.mainthreadTest()
        ms = self.getCurrentMS()
        if ms is not None:
            self.aalist.update(ms.getObject().activeAreaNames())
        else:
            self.aalist.update([])

    def updateAAInfo(self):             # must be called on subthread
        debug.subthreadTest()
        ms = self.getCurrentMS()
        if ms is not None:
            activearea = ms.getObject().activearea
            activearea.begin_reading()
            try:
                aasize = activearea.size()
                mssize = ms.getObject().sizeInPixels()
                mpxls = mssize[0] * mssize[1]
                pixstring="pixels"
                apxls = mpxls - aasize
                if ms.getObject().activearea.getOverride():
                    msg = "OVERRIDE: all %d pixels are active" % mpxls
                else:
                    msg = "%d of %d pixels are active (%g%%)" % \
                        (apxls, mpxls, 100.*apxls/mpxls)
            finally:
                activearea.end_reading()
        else:
            msg = "No Microstructure selected"
        mainthread.runBlock(self.aainfo.get_buffer().set_text, (msg,))
        gtklogger.checkpoint("active area status updated")

    def setOverrideButton(self):
        mainthread.runBlock(self.setOverrideButton_thread)
    def setOverrideButton_thread(self):
        ms = self.getCurrentMS()
        if ms is not None:
            self.overridesignal.block()
            self.overridebutton.set_active(
                ms.getObject().activearea.getOverride())
            self.overridesignal.unblock()

    def updateHistory(self, activeareaModifier):
        if activeareaModifier is not None:
            self.historian.record(activeareaModifier)
            
    def sensitize(self):
        mainthread.runBlock(self.sensitize_thread)
    def sensitize_thread(self):
        debug.mainthreadTest()
        ms = self.getCurrentMS()
        if ms is not None:
            activearea = ms.getObject().activearea
            self.undobutton.set_sensitive(activearea.undoable())
            self.redobutton.set_sensitive(activearea.redoable())
            self.overridebutton.set_sensitive(1)
            self.okbutton.set_sensitive(self.activeareaModFactory.isValid())
            self.storebutton.set_sensitive(1)
            aachosen = self.aalist.get_value() is not None
            self.restorebutton.set_sensitive(aachosen)
            self.deletebutton.set_sensitive(aachosen)
            self.renamebutton.set_sensitive(aachosen)
        else:
            self.undobutton.set_sensitive(0)
            self.redobutton.set_sensitive(0)
            self.overridebutton.set_sensitive(0)
            self.okbutton.set_sensitive(0)
            self.storebutton.set_sensitive(0)
            self.restorebutton.set_sensitive(0)
            self.deletebutton.set_sensitive(0)
            self.renamebutton.set_sensitive(0)

    def sensitizeHistory(self):
        debug.mainthreadTest()
        self.nextbutton.set_sensitive(self.historian.nextSensitive())
        self.prevbutton.set_sensitive(self.historian.prevSensitive())

    def validityChangeCB(self, validity):
        # called only on the main thread
        self.sensitize_thread()

####################################
        
aap = ActiveAreaPage()
