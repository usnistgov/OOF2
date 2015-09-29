# -*- python -*-
# $RCSfile: layereditorGUI.py,v $
# $Revision: 1.90 $
# $Author: langer $
# $Date: 2010/12/01 20:43:42 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common.IO import display
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import layereditor
from ooflib.common.IO import oofmenu
from ooflib.common.IO import whoville
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gfxmenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO.GUI import quit
from ooflib.common.IO.GUI import subWindow
from ooflib.common.IO.GUI import tooltips
from ooflib.common.IO.GUI import whowidget
from ooflib.common.IO.GUI import widgetscope
import gtk

class LayerEditorGUI(layereditor.LayerEditor, subWindow.SubWindow,
                     widgetscope.WidgetScope):

    def __init__(self):
        debug.mainthreadTest()
        self.built = False
        layereditor.LayerEditor.__init__(self)
        gtklogger.checkpoint("layereditor layerset changed")

        self.suppressCallbacks = 0

        widgetscope.WidgetScope.__init__(self, None)

        self.setData("gfxwindow", None) # widgetscope data, that is
        
        self.sbcallbacks = [
            switchboard.requestCallbackMain('open graphics window',
                                            self.gfxwindowChanged),
            switchboard.requestCallbackMain('close graphics window',
                                            self.gfxwindowChanged)
            ]


        self.menu.File.Quit.gui_callback = quit.queryQuit

        subWindow.SubWindow.__init__(
            self, title="%s Graphics Layer Editor"%subWindow.oofname(),
            menu=self.menu)
##        self.gtk.set_policy(1, 1, 0)
        self.gtk.set_default_size(600, 250)
        self.gtk.connect('destroy', self.destroyCB)

        mainpane = gtk.HPaned()
        mainpane.set_border_width(3)
        mainpane.set_position(300)
        self.mainbox.pack_start(mainpane, expand=1, fill=1)

        # The left side of the layer editor is for choosing the object
        # being drawn.
        whoframe = gtk.Frame('Displayed Object')
        mainpane.pack1(whoframe, resize=1, shrink=0)
        wscroll = gtk.ScrolledWindow()
        gtklogger.logScrollBars(wscroll, "ObjectScroll")
        wscroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        whoframe.add(wscroll)
        vbox = gtk.VBox()
        wscroll.add_with_viewport(vbox)
        cmd = self.menu.LayerSet.DisplayedObject
        # This creates a table containing a WhoClassWidget and a WhoWidget:
        ptable = parameterwidgets.ParameterTable(
            [cmd.get_arg('category'), cmd.get_arg('object')],
            scope=self)
        vbox.pack_start(ptable.gtk, expand=0, fill=0)

        # The right side of the layer editor lists the display methods
        # for the object on the left side.
        methframe = gtk.Frame('Display Methods')
        gtklogger.setWidgetName(methframe, "DisplayMethods")
        mainpane.pack2(methframe, resize=1, shrink=0)
        mvbox = gtk.VBox()
        methframe.add(mvbox)
        mhbox = gtk.HBox()
        mvbox.pack_start(mhbox, expand=1, fill=1)
        self.methodList = chooser.ScrolledChooserListWidget(
            callback=self.singleClickMethodCB,
            dbcallback=self.doubleClickMethodCB,
            comparator=lambda x, y: (not x.inequivalent(y)),
            name="List")
        mhbox.pack_start(self.methodList.gtk, expand=1, fill=1, padding=3)

        # The who widget is replaced each time the who class widget is
        # activated, so its switchboard callback must be reset often,
        # and is done in findWidget().
        self.whowidgetsignal = None
        self.findWhoWidget()

        buttonbox = gtk.HBox()
        mvbox.pack_start(buttonbox, expand=0, fill=0, padding=3)

        self.newMethodButton = gtkutils.StockButton(gtk.STOCK_NEW, 'New...')
        buttonbox.pack_start(self.newMethodButton, expand=0, fill=0)
        gtklogger.setWidgetName(self.newMethodButton, "New")
        gtklogger.connect(self.newMethodButton, 'clicked',
                          self.newMethodButtonCB)
        self.editMethodButton = gtkutils.StockButton(gtk.STOCK_EDIT, 'Edit...')
        buttonbox.pack_start(self.editMethodButton, expand=0, fill=0)
        gtklogger.setWidgetName(self.editMethodButton, "Edit")
        gtklogger.connect(self.editMethodButton, 'clicked',
                          self.editMethodButtonCB)
        self.copyMethodButton = gtkutils.StockButton(gtk.STOCK_COPY, 'Copy')
        buttonbox.pack_start(self.copyMethodButton, expand=0, fill=0)
        gtklogger.setWidgetName(self.copyMethodButton, "Copy")
        gtklogger.connect(self.copyMethodButton, 'clicked',
                          self.copyMethodButtonCB)
        self.deleteMethodButton = gtkutils.StockButton(gtk.STOCK_DELETE,
                                                       'Delete')
        buttonbox.pack_start(self.deleteMethodButton, expand=0, fill=0)
        gtklogger.setWidgetName(self.deleteMethodButton, "Delete")
        gtklogger.connect(self.deleteMethodButton, 'clicked',
                          self.deleteMethodButtonCB)

        self.mainbox.pack_start(gtk.HSeparator(), expand=0, fill=0)

        # Buttons at the bottom governing LayerSet operations:
        # New LayerSet, Send to Gfx Window, etc.
        
        mainbuttonbox = gtk.HBox()
        self.mainbox.pack_start(mainbuttonbox, expand=0, fill=0, padding=3)

        newLayerButton = gtkutils.StockButton(gtk.STOCK_NEW, 'New Layer')
        mainbuttonbox.pack_start(newLayerButton, expand=0, fill=0, padding=3)
        gtklogger.setWidgetName(newLayerButton, "NewLayer")
        gtklogger.connect(newLayerButton, 'clicked', self.newLayerButtonCB)

        self.sendButton = gtkutils.StockButton(gtk.STOCK_GO_FORWARD, 'Send',
                                               reverse=1)
##        self.sendButton.set_usize(80, -1)
        mainbuttonbox.pack_end(self.sendButton, expand=0, fill=0, padding=3)
        gtklogger.setWidgetName(self.sendButton, "Send")
        gtklogger.connect(self.sendButton, 'clicked', self.sendCB)
        self.destinationMenu = chooser.ChooserWidget([], name="Destination")
        mainbuttonbox.pack_end(self.destinationMenu.gtk, expand=0, fill=0)
        self.updateDestinationMenu()
        label=gtk.Label('Destination=')
        tooltips.set_tooltip_text(label,
            'The graphics window(s) that will display the layer(s).')
        label.set_alignment(1.0, 0.5)
        mainbuttonbox.pack_end(label, expand=0, fill=0)

        self.mainbox.pack_start(gtk.HSeparator(), expand=0, fill=0, padding=3)

        # When the lhs widgets change state the rhs might have to
        # change too.  The widgets referred to here are inside the
        # ParameterTable constructed above.
        self.whoclasswidget = self.findWidget(
            lambda w: isinstance(w, whowidget.WhoClassParameterWidget))
        self.whoclasswidgetsignal = switchboard.requestCallbackMain(
            self.whoclasswidget, self.whoClassChangedCB)
        self.sbcallbacks.append(self.whoclasswidgetsignal)

        self.built = True
        self.sensitize()
        self.gtk.show_all()
        
    ##############

    def destroyCB(self, *args, **kwargs):
        if self.gtk is not None:        # recursion suppression
            selfgtk = self.gtk
            self.gtk = None
            map(switchboard.removeCallback, self.sbcallbacks)
            if self.whowidgetsignal:
                switchboard.removeCallback(self.whowidgetsignal)
            mainthread.runBlock(selfgtk.destroy)
            layereditor.LayerEditor.destroy(self)

    def show(self):
        mainthread.runBlock(self.show_thread)
    def show_thread(self):
        debug.mainthreadTest()
        self.gtk.show_all()
        self.raise_window()

    def close(self):
        self.destroyCB()
        
    #############

    def sensitize(self):
        debug.mainthreadTest()
        self.sendButton.set_sensitive(not self.currentLayerSet.invalid())
        okwho = self.currentLayerSet.who is not None \
                and self.currentWhoClass is not whoville.noclass
        oksel = self.methodList.has_selection()
        oklyr = oksel and self.methodList.get_value() is not display.emptyLayer
        
        self.newMethodButton.set_sensitive(okwho)
        self.editMethodButton.set_sensitive(okwho and oksel)
        self.copyMethodButton.set_sensitive(oklyr)
        self.deleteMethodButton.set_sensitive(oklyr)

    #############            

    def initialize(self, gfxwindow, layerNumber=None):
        layereditor.LayerEditor.initialize(self, gfxwindow, layerNumber)
        gtklogger.checkpoint("layereditor layerset changed")
        self.setData("gfxwindow", gfxwindow)
        if gfxwindow is not None:
            mainthread.runBlock(self.destinationMenu.set_state,
                                (gfxwindow.name,))

    def gfxwindowChanged(self, window):
        # switchboard callback: "open graphics window", "close graphics window"
        self.updateDestinationMenu()
        self.setData("gfxwindow", window)
        self.sensitize()

    def updateDestinationMenu(self):
        windownames = [w.name for w in gfxmanager.gfxManager.windows]
        if len(windownames) > 1:
            windownames.append('all')
        self.destinationMenu.update(windownames)

    #############

    # The following functions simply add a checkpoint to the base
    # class functions that modify self.currentLayerSet.  The
    # checkpoint is required so that functions that call self.ready()
    # in GUI tests don't call it too soon.

    def addMethodCB(self, method):
        layereditor.LayerEditor.addMethodCB(self, method)
        gtklogger.checkpoint("layereditor layerset changed")

    def copyMethodCB(self, layernumber):
        layereditor.LayerEditor.copyMethodCB(self, layernumber)
        gtklogger.checkpoint("layereditor layerset changed")

    def replaceMethodCB(self, layernumber, method):
        layereditor.LayerEditor.replaceMethodCB(self, layernumber, method)
        gtklogger.checkpoint("layereditor layerset changed")

    def deleteMethodCB(self, layernumber):
        layereditor.LayerEditor.deleteMethodCB(self, layernumber)
        gtklogger.checkpoint("layereditor layerset changed")
        
    #############

    def newLayerButtonCB(self, button):
        self.menu.LayerSet.New(window=None)

    def destinations(self):
        destination = self.destinationMenu.get_value()
        if destination == 'all':
            return gfxmanager.gfxManager.windows
        if destination is None:
            return []
        return [gfxmanager.gfxManager.getWindow(destination)]

    def sendCB(self, button):
        self.reallySend()
    def autoSend(self):
        # Overrides null function in base class.  This is called at
        # the completion of menu commands that change the current
        # layerset.
        if layereditor.autoSendFlag:
            self.reallySend()
    def reallySend(self):
        ## This violates the rule that menu items should never invoke
        ## other menu items (because it leads to unnecessary
        ## proliferation of commands in scripts during an execute,
        ## save, execute cycle).  But if the menu item is *not*
        ## invoked, then a script saved in GUI mode and run in text
        ## mode might not put the same layers in a window.  Since the
        ## LayerEditor will go away soon (we hope), it's not worth
        ## fixing this.
        for destination in self.destinations():
            self.menu.LayerSet.Send(window=destination.name)

    def updateWho(self):                # overrides def'n in LayerEditor
        mainthread.runBlock(self.updateWho_thread)
    def updateWho_thread(self):
        debug.mainthreadTest()
        self.whoclasswidgetsignal.block()
        if self.currentWhoClass is not None:
            self.whoclasswidget.set_value(self.currentWhoClass.name())
        else:
            self.whoclasswidget.set_value(None)
        self.whoclasswidgetsignal.unblock()
        self.findWhoWidget()
        self.whowidgetsignal.block()
        if self.currentLayerSet.who is not None:
            self.whowidget.set_value(self.currentLayerSet.who.path())
        else:
            self.whowidget.set_value(None)
        self.whowidgetsignal.unblock()

    def updateMethodList(self, selected=None): # overrides def'n in LayerEditor
        mainthread.runBlock(self.updateMethodList_thread, (selected,))
    def updateMethodList_thread(self, selected):
        debug.mainthreadTest()
        names = []
        methods = []
        for layer in self.currentLayerSet:
            name = layer.name()
            if layer.acceptsWhoClass(self.currentWhoClass):
                names.append(name)
            else:
                names.append('(invalid) ' + name)
        self.methodList.update(self.currentLayerSet, names)
        if selected is not None:
            self.methodList.set_selection(selected)
        self.sensitize()
        gtklogger.checkpoint("layer editor updated")

    ##############

    def findWhoWidget(self):
        # Set up the signals for the WhoWidget for the AnyWhoParameter
        # that underlies the 'object' argument to the
        # LayerSet.DisplayedObject command.  This widget is replaced
        # each time the WhoClassParameterWidget changes state, so
        # communications have to be reestablished.
        debug.mainthreadTest()
        if self.whowidgetsignal is not None:
            block = self.whowidgetsignal.is_blocked()
            switchboard.removeCallback(self.whowidgetsignal)
        else:
            block = 0
        self.whowidget = self.findWidget(
            lambda w: isinstance(w, whowidget.WhoWidget))
        self.whowidgetsignal = switchboard.requestCallbackMain(
            self.whowidget, self.whoChangedCB)
        if block:
            self.whowidgetsignal.block()

    def whoChangedCB(self, interactive): # who widget switchboard callback
        # The coupling between the who widget and the whoclass widget
        # means that the recursion suppression in the ChooserWidget
        # isn't sufficient to prevent an infinite loop here, so we
        # have to kluge it with self.suppressCallbacks.  The loop
        # arises when a widget callback calls a menu command and the
        # menu command sets the state of the widget.
        if not self.suppressCallbacks:
            self.suppressCallbacks += 1
            whoclassname = self.whoclasswidget.get_value()
            whoname = self.whowidget.get_value()
            if interactive:
                self.menu.LayerSet.DisplayedObject(category=whoclassname,
                                                   object=whoname)
            else:
                self.changeDisplayedObject(whoclassname, whoname)
            self.suppressCallbacks -= 1

    def whoClassChangedCB(self, interactive): # sb callback from WhoClassWidget
        self.findWhoWidget()
        self.whoChangedCB(interactive=interactive)


    #####################

    def methodDialogTitle(self):
        if self.currentLayerSet.who is None:
            return "New Display Method for %s" % self.currentWhoClass.name()
        else:
            return "New Display Method for %s %s" % \
                   (self.currentWhoClass.name(),
                    self.currentLayerSet.who.name())

    def newMethodButtonCB(self, button):      # gtk callback
        menuitem = self.menu.LayerSet.Add_Method
        methodarg = menuitem.get_arg('method')

        # The 'method' parameter must have a suitable initial value,
        # or the widget won't be created properly.
        whoclassname = self.currentWhoClass.name()
        if methodarg.value is None or \
               whoclassname not in methodarg.value.getRegistration().whoclasses:
            for registration in display.DisplayMethod.registry:
                if whoclassname in registration.whoclasses:
                    methodarg.value = registration()
                    break

        if parameterwidgets.getParameters(methodarg,
                                          parentwindow=self.gtk,
                                          title=self.methodDialogTitle(),
                                          scope=self):
            menuitem.callWithDefaults()
            
    def editMethodButtonCB(self, button):
        oldmethod = self.methodList.get_value()
        menuitem = self.menu.LayerSet.Replace_Method
        methodarg = menuitem.get_arg('method')
        if oldmethod is not display.emptyLayer:
            methodarg.value = oldmethod
        else:
            methodarg.value = None
        if parameterwidgets.getParameters(methodarg,
                                          parentwindow=self.gtk,
                                          title=self.methodDialogTitle(),
                                          scope=self):
            layernumber = self.methodList.get_index()
            menuitem.callWithDefaults(layer_number=layernumber)

    # Single clicks can change the selection state.
    def singleClickMethodCB(self, method, interactive):
        if self.built:
            self.sensitize() 

    def doubleClickMethodCB(self, method):
        menuitem = self.menu.LayerSet.Replace_Method
        methodarg = menuitem.get_arg('method')
        methodarg.value = method
        if parameterwidgets.getParameters(methodarg,
                                          parentwindow=self.gtk,
                                          title=self.methodDialogTitle(),
                                          scope=self):
            layernumber = self.methodList.get_index()
            menuitem.callWithDefaults(layer_number=layernumber)

    def copyMethodButtonCB(self, button):
        debug.mainthreadTest()
        layernumber = self.methodList.get_index()
        self.menu.LayerSet.Copy_Method(layer_number=layernumber)

    def deleteMethodButtonCB(self, button):
        debug.mainthreadTest()
        layernumber = self.methodList.get_index()
        self.menu.LayerSet.Delete_Method(layer_number=layernumber)

##############################

def newLayerEditor():
    return LayerEditorGUI()

# Called from oofGUI "stop" function, which closes all open non-modal
# windows as a precaution.
def destroyLayerEditor():               
    if layereditor.layerEditor is not None:
        layereditor.layerEditor.close()

layereditor.newLayerEditor = newLayerEditor

