# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# GUI page for manipulating pixel selections.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import microstructure
from ooflib.common import pixelselectionmod
from ooflib.common import subthread
from ooflib.common import utils
from ooflib.common.IO import mainmenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import historian
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from gi.repository import Gtk

if config.dimension()==2:
    pixstring = "pixel"
    Pixstring = "Pixel"
elif config.dimension()==3:
    pixstring = "voxel"
    Pixstring = "Voxel"

class SelectionPage(oofGUI.MainPage):
    # Pixel selection manipulation
    def __init__(self):
        debug.mainthreadTest()
        oofGUI.MainPage.__init__(
            self,
            name="%s Selection"%Pixstring,
            ordering=71,
            tip="Modify the set of selected %ss."%pixstring)

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        # Microstructure widget, centered at the top of the page.
        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER, margin_top=2)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        label = Gtk.Label('Microstructure=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        self.mswidget = whowidget.WhoWidget(microstructure.microStructures,
                                            scope=self)
        centerbox.pack_start(self.mswidget.gtk[0],
                             expand=False, fill=False, padding=0)
        
        mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                             wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(mainpane, 'notify::position')

        # Pixel selection status in the left half of the main pane
        pssframe = Gtk.Frame(label="%s Selection Status"%Pixstring,
                             margin=2)
        pssframe.set_shadow_type(Gtk.ShadowType.IN)
        mainpane.pack1(pssframe, resize=True, shrink=False)
        self.datascroll = Gtk.ScrolledWindow(shadow_type=Gtk.ShadowType.IN,
                                             margin=2)
        gtklogger.logScrollBars(self.datascroll, "DataScroll")
        pssframe.add(self.datascroll)
        self.datascroll.set_policy(Gtk.PolicyType.AUTOMATIC,
                                   Gtk.PolicyType.AUTOMATIC)
        self.psdata = Gtk.TextView(name="fixedfont", margin=2)
        gtklogger.setWidgetName(self.psdata, 'DataView')
        self.psdata.set_editable(False)
        self.psdata.set_cursor_visible(False)
        self.psdata.set_wrap_mode(Gtk.WrapMode.WORD)
        self.datascroll.add(self.psdata)

        # Selection method in the right half of the main pane
        modframe = Gtk.Frame(label="%s Selection Modification"%Pixstring,
                             margin=2)
        gtklogger.setWidgetName(modframe, "SelectionModification")
        modframe.set_shadow_type(Gtk.ShadowType.IN)
        mainpane.pack2(modframe, resize=True, shrink=False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                       spacing=2, margin=2)
        modframe.add(vbox)
        self.selectionModFactory = regclassfactory.RegisteredClassFactory(
            pixelselectionmod.SelectionModifier.registry, title="Method:",
            scope=self, name="Method", margin=2)
        vbox.pack_start(self.selectionModFactory.gtk,
                        expand=True, fill=True, padding=0)
        self.historian = historian.Historian(self.selectionModFactory.set,
                                             self.sensitizeHistory,
                                             setCBkwargs={'interactive':1})
        self.selectionModFactory.set_callback(self.historian.stateChangeCB)
        
        # Prev, OK, and Next buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=2)
        self.prevmethodbutton = gtkutils.prevButton()
        gtklogger.connect(self.prevmethodbutton, 'clicked',
                          self.historian.prevCB)
        hbox.pack_start(self.prevmethodbutton,
                        expand=False, fill=False, padding=0)
        self.prevmethodbutton.set_tooltip_text(
            'Recall the previous selection modification operation.')
        self.okbutton = gtkutils.StockButton("gtk-ok", "OK")
        gtklogger.setWidgetName(self.okbutton, "OK")
        hbox.pack_start(self.okbutton, expand=True, fill=True, padding=0)
        gtklogger.connect(self.okbutton, 'clicked', self.okbuttonCB)
        self.okbutton.set_tooltip_text(
            'Perform the selection modification operation defined above.')
        self.nextmethodbutton = gtkutils.nextButton()
        gtklogger.connect(self.nextmethodbutton, 'clicked',
                          self.historian.nextCB)
        hbox.pack_start(self.nextmethodbutton,
                        expand=False, fill=False, padding=0)
        self.nextmethodbutton.set_tooltip_text(
            "Recall the next selection modification operation.")

        # Undo, Redo, and Clear buttons
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=0)
        self.undobutton = gtkutils.StockButton("edit-undo-symbolic", "Undo")
        self.redobutton = gtkutils.StockButton("edit-redo-symbolic", "Redo")
        hbox.pack_start(self.undobutton, expand=True, fill=False, padding=0)
        hbox.pack_start(self.redobutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.undobutton, "Undo")
        gtklogger.setWidgetName(self.redobutton, "Redo")
        gtklogger.connect(self.undobutton, 'clicked', self.undoCB)
        gtklogger.connect(self.redobutton, 'clicked', self.redoCB)
        self.undobutton.set_tooltip_text(
            "Undo the previous %s selection operation."%pixstring)
        self.redobutton.set_tooltip_text(
            "Redo an undone %s selection operation."%pixstring)
        self.clearbutton = gtkutils.StockButton("edit-clear-symbolic", "Clear")
        hbox.pack_start(self.clearbutton, expand=True, fill=False, padding=0)
        gtklogger.setWidgetName(self.clearbutton, "Clear")
        gtklogger.connect(self.clearbutton, 'clicked', self.clearCB)
        self.clearbutton.set_tooltip_text("Unselect all %ss." % pixstring)

        self.sbcallbacks = [
            switchboard.requestCallbackMain(self.mswidget,
                                            self.mswidgetCB),
            switchboard.requestCallbackMain('pixel selection changed',
                                            self.selectionChanged),
            switchboard.requestCallbackMain('modified pixel selection',
                                            self.updateHistory),
            switchboard.requestCallbackMain(
            pixelselectionmod.SelectionModifier,
            self.updateSelectionModifiers),
            switchboard.requestCallbackMain(('validity',
                                             self.selectionModFactory),
                                            self.validityChangeCB)
            ]

    def installed(self):
        self.updatePSInfo()
        self.sensitize()
        self.sensitizeHistory()

    def selectionChanged(self):    # switchboard 'pixel selection changed'
        self.sensitize()
        self.updatePSInfo()
        
    def validityChangeCB(self, validity):
        self.sensitize()

    def getCurrentMSName(self):
        return self.mswidget.get_value()
    
    def getCurrentMS(self):
        try:
            return microstructure.microStructures[self.getCurrentMSName()]
        except KeyError:
            pass
    def getSelectionContext(self):
        ms = self.getCurrentMS()
        if ms:
            return (ms, ms.getSelectionContext())
        return (None, None)
    
    def mswidgetCB(self, *args, **kwargs):
        self.updatePSInfo()
        self.sensitize()



    def updatePSInfo(self):
        debug.mainthreadTest()
        subthread.execute(self.updatePSInfo_subthread)

    def updatePSInfo_subthread(self):
        (ms, selection) = mainthread.runBlock(self.getSelectionContext)
        if selection is not None:
            selection.begin_reading()
            try:
                pssize = selection.size()
            finally:
                selection.end_reading()
            mssize = ms.getObject().sizeInPixels()
            msg = "%d of %d pixels selected (%g%%)" % \
                (pssize, mssize[0]*mssize[1], 100.*pssize/(mssize[0]*mssize[1]))
        else:
            msg = "No Microstructure selected."
        mainthread.runBlock(self.psdata.get_buffer().set_text, (msg,))
        gtklogger.checkpoint("pixel page updated")

    def sensitize(self):
        debug.mainthreadTest()
        subthread.execute(self.sensitize_subthread)

    def sensitize_subthread(self):

        def set_button_sensitivity(u, r, c):
            self.undobutton.set_sensitive(u)
            self.redobutton.set_sensitive(r)
            self.clearbutton.set_sensitive(c)

        def set_ok_sensitivity(selection):
            ok =  selection is not None and \
                 self.selectionModFactory.isValid()
            self.okbutton.set_sensitive(ok)

        (ms, selection) = mainthread.runBlock(self.getSelectionContext)
        if selection is not None:
            selection.begin_reading()
            try:
                u = selection.undoable()
                r = selection.redoable()
                c = selection.clearable()
            finally:
                selection.end_reading()
        else:
            (u,r,c) = (0,0,0)
        mainthread.runBlock(set_button_sensitivity, (u,r,c))
        mainthread.runBlock(set_ok_sensitivity, (selection,) )
        gtklogger.checkpoint("pixel page sensitized")

    def updateSelectionModifiers(self): # SB: New selection modifier created
        self.selectionModFactory.update(
            pixelselectionmod.SelectionModifier.registry)

    def sensitizeHistory(self):
        debug.mainthreadTest()
        self.nextmethodbutton.set_sensitive(self.historian.nextSensitive())
        self.prevmethodbutton.set_sensitive(self.historian.prevSensitive())

    def updateHistory(self, selectionModifier): # sb 'modified pixel selection'
        if selectionModifier is not None:
            self.historian.record(selectionModifier)

    def undoCB(self, button):
        mainmenu.OOF.PixelSelection.Undo(microstructure=self.getCurrentMSName())
    def redoCB(self, button):
        mainmenu.OOF.PixelSelection.Redo(microstructure=self.getCurrentMSName())
    def clearCB(self, button):
        mainmenu.OOF.PixelSelection.Clear(
            microstructure=self.getCurrentMSName())

    def okbuttonCB(self, *args):
        # Actually perform the current selection modification operation.
        modmeth = self.selectionModFactory.getRegistration()
        if modmeth is not None:
            # Copy parameters from widgets to the registration.
            self.selectionModFactory.set_defaults()
            # Invoke the method by calling the corresponding menu
            # item.  The menu item and method registration share a
            # parameter list.
            menuitem = getattr(mainmenu.OOF.PixelSelection,
                               utils.space2underscore(modmeth.name()))
            menuitem.callWithDefaults(microstructure=self.getCurrentMSName())

####################################
        
sp = SelectionPage()
