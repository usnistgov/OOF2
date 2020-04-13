# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import utils
from ooflib.common.IO import mainmenu
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import regclassfactory
from ooflib.common.IO.GUI import whowidget
from ooflib.engine import pinnodesmodifier
from ooflib.engine import skeletoncontext

from gi.repository import Gtk

class PinNodesPage(oofGUI.MainPage):
    def __init__(self):
        oofGUI.MainPage.__init__(self, name="Pin Nodes", ordering=120.1,
                                 tip='Pin and unpin nodes')

        mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(mainbox)

        centerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                            halign=Gtk.Align.CENTER, spacing=3)
        mainbox.pack_start(centerbox, expand=False, fill=False, padding=0)
        self.skelwidget = whowidget.WhoWidget(whoville.getClass('Skeleton'),
                                              callback=self.select_skeletonCB)
        label = Gtk.Label('Microstructure=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.skelwidget.gtk[0],
                             expand=False, fill=False, padding=0)
        label = Gtk.Label('Skeleton=', halign=Gtk.Align.END)
        centerbox.pack_start(label, expand=False, fill=False, padding=0)
        centerbox.pack_start(self.skelwidget.gtk[1],
                             expand=False, fill=False, padding=0)

        mainpane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL,
                              wide_handle=True)
        gtklogger.setWidgetName(mainpane, 'Pane')
        mainbox.pack_start(mainpane, expand=True, fill=True, padding=0)
        gtklogger.connect_passive(mainpane, 'notify::position')

        # Pinned nodes status in the left half of the main pane
        pnsframe = Gtk.Frame(label="Pinned Nodes Status",
                             shadow_type=Gtk.ShadowType.IN)
        self.datascroll = Gtk.ScrolledWindow()
        gtklogger.logScrollBars(self.datascroll, "StatusScroll")
        pnsframe.add(self.datascroll)
        self.datascroll.set_policy(Gtk.PolicyType.AUTOMATIC,
                                   Gtk.PolicyType.AUTOMATIC)
        self.psdata = Gtk.TextView(name="fixedfont", editable=False,
                                   wrap_mode=Gtk.WrapMode.WORD,
                                   cursor_visible=False)
        self.datascroll.add(self.psdata)
        mainpane.pack1(pnsframe, resize=True, shrink=False)
        
        # Pin nodes method
        modframe = Gtk.Frame(label="Pin Nodes Methods",
                             shadow_type=Gtk.ShadowType.IN)
        gtklogger.setWidgetName(modframe, 'Modify')
        # box for "methods" and "buttons"
        modbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        modframe.add(modbox)
        self.pinModFactory = regclassfactory.RegisteredClassFactory(
            pinnodesmodifier.PinNodesModifier.registry,
            title="Method:", scope=self, name="Method")
        modbox.pack_start(self.pinModFactory.gtk,
                          expand=True, fill=True, padding=0)

        # buttons
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        modbox.pack_start(hbox1, expand=False, fill=False, padding=0)
        self.okbutton = gtkutils.StockButton('gtk-ok', 'OK')
        gtklogger.setWidgetName(self.okbutton, 'OK')
        gtklogger.connect(self.okbutton, "clicked", self.okCB)
        self.okbutton.set_tooltip_text("Pin nodes with the selected method.")
        self.undobutton = gtkutils.StockButton('edit-undo-symbolic', 'Undo')
        gtklogger.setWidgetName(self.undobutton, 'Undo')
        gtklogger.connect(self.undobutton, "clicked", self.undoCB)
        self.undobutton.set_tooltip_text("Undo the latest action.")
        self.redobutton = gtkutils.StockButton('edit-redo-symbolic', 'Redo')
        gtklogger.setWidgetName(self.redobutton, 'Redo')
        gtklogger.connect(self.redobutton, "clicked", self.redoCB)
        self.redobutton.set_tooltip_text("Redo the latest undone action.")
        hbox1.pack_start(self.undobutton, expand=False, fill=True, padding=0)
        hbox1.pack_start(self.okbutton, expand=True, fill=True, padding=0)
        hbox1.pack_end(self.redobutton, expand=False, fill=True, padding=0)

        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                        homogeneous=True, spacing=2)
        modbox.pack_start(hbox2, expand=False, fill=False, padding=0)
        self.unpinallbutton = Gtk.Button("Unpin All")
        gtklogger.setWidgetName(self.unpinallbutton, 'Unpin All')
        gtklogger.connect(self.unpinallbutton, "clicked", self.unpinallCB)
        self.unpinallbutton.set_tooltip_text("Unpin all the pinned nodes.")
        self.invertbutton = Gtk.Button("Invert")
        gtklogger.setWidgetName(self.invertbutton, 'Invert')
        gtklogger.connect(self.invertbutton, "clicked", self.invertCB)
        self.invertbutton.set_tooltip_text(
            "Invert - pin the unpinned and unpin the pinned.")
        hbox2.pack_start(self.unpinallbutton, expand=True, fill=True, padding=0)
        hbox2.pack_start(self.invertbutton, expand=True, fill=True, padding=0)
        
        mainpane.pack2(modframe, resize=False, shrink=False)

        # Switchboard callbacks
        switchboard.requestCallbackMain(('who changed', 'Skeleton'),
                                        self.changeSkeleton)
        switchboard.requestCallbackMain(('new who', 'Microstructure'),
                                        self.newMS)
        switchboard.requestCallbackMain("new pinned nodes",
                                        self.newNodesPinned)
        switchboard.requestCallbackMain(self.skelwidget,
                                        self.skel_update)
        switchboard.requestCallbackMain("made reservation",
                                        self.reservationChanged)
        switchboard.requestCallbackMain("cancelled reservation",
                                        self.reservationChanged)

    def installed(self):
        self.sensitize()

    # Switchboard callbacks
    def changeSkeleton(self, skelcontext):
        if skelcontext is self.currentSkelContext():
            self.update()

    def newMS(self, msname):
        if not self.currentSkelName():
            self.skelwidget.set_value(msname)

    def newNodesPinned(self, pinnednodes, skelcontext):
        if self.currentSkelContext() is skelcontext:
            self.update()

    def skel_update(self, *args, **kwargs):  # Switchboard "self.skelwidget"
        skeleton = self.currentSkelName()
        self.update()

    def reservationChanged(self, who):
        if self.currentSkelContext() is who:
            self.sensitize()

    def update(self):
        debug.mainthreadTest()
        skelctxt = self.currentSkelContext()
        if skelctxt is not None:
            nnodes = skelctxt.getObject().nnodes()
            npinned = skelctxt.pinnednodes.npinned()
            self.psdata.get_buffer().set_text(
                "Total No. of Nodes: %d\nNo. of Pinned Nodes: %d\n" %
                (nnodes, npinned))
        else:
            self.psdata.get_buffer().set_text("")
        self.sensitize()

    def select_skeletonCB(self, *args):
        self.update()

    def currentSkelName(self):
        return self.skelwidget.get_value()
    
    def currentSkelContext(self):
        try:
            return skeletoncontext.skeletonContexts[self.currentSkelName()]
        except KeyError:
            return None

    def sensitize(self):
        debug.mainthreadTest()
        skelcontext = self.currentSkelContext()
        skelok = (skelcontext is not None 
                  and not skelcontext.query_reservation())
        self.okbutton.set_sensitive(skelok)
        self.undobutton.set_sensitive(skelok and
                                      skelcontext.pinnednodes.undoable())
        self.redobutton.set_sensitive(skelok and
                                      skelcontext.pinnednodes.redoable())
        self.unpinallbutton.set_sensitive(skelok and
                                          skelcontext.pinnednodes.npinned() > 0)
        self.invertbutton.set_sensitive(skelok)


    def okCB(self, *args):
        modmethod = self.pinModFactory.getRegistration()
        if modmethod is not None:
            self.pinModFactory.set_defaults()
            menuitem = getattr(mainmenu.OOF.Skeleton.PinNodes,
                               utils.space2underscore(modmethod.name()))
            menuitem.callWithDefaults(skeleton=self.currentSkelName())

    def undoCB(self, *args):
        mainmenu.OOF.Skeleton.PinNodes.Undo(skeleton=self.currentSkelName())
    
    def redoCB(self, *args):
        mainmenu.OOF.Skeleton.PinNodes.Redo(skeleton=self.currentSkelName())

    def unpinallCB(self, *args):
        mainmenu.OOF.Skeleton.PinNodes.UnpinAll(skeleton=self.currentSkelName())

    def invertCB(self, *args):
        mainmenu.OOF.Skeleton.PinNodes.Invert(skeleton=self.currentSkelName())


# Create the page.
pinnodesPage = PinNodesPage()
