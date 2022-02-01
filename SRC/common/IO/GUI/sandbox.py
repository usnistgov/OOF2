# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# The sandbox is a subwindow for testing Gtk code in the OOF2
# environment.  The menu item for opening the sandbox only appears in
# debug mode.  No real OOF2 code is in this file.

from gi.repository import Gtk, GObject, Gdk

from ooflib.common.IO.GUI import subWindow
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import parameterwidgets
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common import debug
from ooflib.common.IO import mainmenu

sandbox = None

def openSandbox(menuitem):
    debug.fmsg()
    global sandbox
    if sandbox is None:
        sandbox = SandBox()
    sandbox.gtk.present_with_time(Gtk.get_current_event_time())

if debug.debug():
    mainmenu.OOF.Help.Debug.Sandbox.add_gui_callback(openSandbox)

class SandBox(subWindow.SubWindow):
    def __init__(self):
        subWindow.SubWindow.__init__(self, title="Sandbox", menu="dummy")
        self.names = ["no dialog", "dialog", "event"]
        self.chooser = chooser.ChooserWidget(self.names,
                                             name="chooooser",
                                             callback=self.chooserCB)
        self.mainbox.pack_start(self.chooser.gtk,
                                expand=True, fill=True, padding=0)

        liszt = Gtk.ListStore(GObject.TYPE_STRING)
        self.treeview = Gtk.TreeView(liszt)
        gtklogger.setWidgetName(self.treeview, "tree")
        self.mainbox.pack_start(self.treeview,
                                expand=True, fill=True, padding=0)
        cell = Gtk.CellRendererToggle()
        col = Gtk.TreeViewColumn("Sand")
        col.pack_start(cell, expand=True)
        self.treeview.append_column(col)

        gtklogger.connect(self.treeview, 'button-press-event',
                          self.treeViewButtonCB)

        button = Gtk.Button("Button")
        self.mainbox.pack_start(button, expand=False, fill=True, padding=0)
        gtklogger.connect(button, 'clicked', self.buttonCB)

        self.gtk.show_all()

    def chooserCB(self, name):
        debug.fmsg("Chooser:", name)
        if name.startswith("dialog"):
            self.do_dialog()

    def treeViewButtonCB(self, gtkobj, event):
        popup = gtklogger.newPopupMenu('buttonmenu')
        for name in self.names:
            item = Gtk.MenuItem(name)
            gtklogger.setWidgetName(item, name)
            gtklogger.connect(item, 'activate', self.activateCB, name)
            popup.append(item)
        # nested menu
        submenu = Gtk.Menu()
        item = Gtk.MenuItem("submenu")
        gtklogger.setWidgetName(item, "submenu")
        popup.append(item)
        gtklogger.set_submenu(item, submenu)
        for name in self.names:
            item = Gtk.MenuItem(name)
            gtklogger.setWidgetName(item, name)
            gtklogger.connect(item, 'activate', self.activateCB,
                              name+' submenu')
            submenu.append(item)
        popup.show_all()
        popup.popup_at_pointer(event)

    def activateCB(self, menuitem, name):
        debug.fmsg("Popup menu", name)
        if name.startswith("dialog"):
            self.do_dialog()
        if name.startswith("event"):
            Gtk.main_iteration_do(False) # False == don't block
  
    def do_dialog(self):
        params = [
            parameter.IntParameter("i", 1),
            parameter.FloatParameter("x", 3.14)
        ]
        vals = parameterwidgets.getParameterValues(
            *params, title="dialog", parentwindow=self.gtk)
        debug.fmsg(vals)


    def buttonCB(self, button):
        # Try to open and activate a pop-up menu "manually"
        popup = Gtk.Menu()
        items = [self.makeItem(name, popup) for name in ("A", "B", "C")]
        popup.show_all()
        popup.popup_at_widget(button,
                              Gdk.Gravity.SOUTH_WEST, Gdk.Gravity.NORTH_WEST,
                              None)
        items[0].activate()
        # Why is it not necessary to call deactivate() or popdown()
        # here when the MenuItem activate callback opens a Dialog?
        #popup.deactivate()
    def makeItem(self, name, menu):
        item = Gtk.MenuItem(name)
        item.connect('activate', self.buttonmenuCB, name)
        menu.append(item)
        return item
    def buttonmenuCB(self, menuitem, name):
        print("buttonmenuCB:", name)
        dialog = Gtk.Dialog()
        button = dialog.add_button("Push", 0)
        response = dialog.run()
        print("response=", response)
        dialog.close()
        
