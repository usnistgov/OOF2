# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import Gtk
import types

# The ChooserWidget creates a pull-down menu containing the given list
# of names.  The currently selected name is shown when the menu isn't
# being pulled down.

# Calls the callback, if specified, with the gtk-selecting object
# and the name.  Backward compatible with other callbacks that way.
# Also has an "update_callback" which gets called, with the new
# current selection, when the list of things is updated, with one
# exception -- it is *not* called at __init__-time.

# The ChooserListWidgets in this file have both a list of names that
# they display, and an optional list of objects corresponding to those
# names.  When asked for their 'value', they return the object, not
# the name.  For historical reasons, the ChooserWidget does not do
# this, although it could be made to do so easily.

## Changes for gtk3:

## The callback functions for different kinds of ChooserWidgets
## used to take different arguments.  Now they all pass the widget's
## current value, and not the widget.

## The ChooserWidget is a Gtk.Stack with a pop-up menu, instead of a
## Gtk.ComboBox with a Gtk.ListStore and Gtk.TreeView, because menu
## items can have tooltips but the cells in a TreeView can't.  The
## ChooserComboWidget can stay as a Gtk.ComboBox because it lists
## user-defined entries, which don't need tooltips.

## The separator_func for ChooserWidget is different from the
## separator_func for the other widgets defined here because
## ChooserWidget is not based on a Gtk.TreeView. Its separator_func
## takes a single string argument, and returns True if that string
## should be replaced by a separator in the pull down menu.

class ChooserWidget(object):
    def __init__(self, namelist, callback=None, callbackargs=(),
                 update_callback=None, update_callback_args=(),
                 helpdict={}, name=None, separator_func=None,
                 homogeneous=False, **kwargs):
        debug.mainthreadTest()
        self.name = name
        # separator_func takes a string arg and returns true if that
        # string should be represented by a Gtk.SeparatorMenuItem.
        self.separator_func = separator_func
        self.current_string = None
        self.current_item = None # only exists while the menu is visible
        self.callback = callback
        self.callbackargs = callbackargs
        self.update_callback = update_callback
        self.update_callback_args = update_callback_args
        self.helpdict = {}
        # Initialize namelist to None instead of [] so that the first
        # call to update will install self.emptyMarker if appropriate.
        self.namelist = None

        self.gtk = Gtk.EventBox()
        gtklogger.setWidgetName(self.gtk, name)
        frame = Gtk.Frame(**kwargs)
        self.gtk.add(frame)
        # Using a Stack instead of a simple Label makes it easy to
        # make sure that the horizontal size of the Chooser doesn't
        # change when the visible label changes, if homogeneous=True. 
        self.stack = Gtk.Stack(homogeneous=homogeneous)
        gtklogger.setWidgetName(self.stack, 'stack')
        frame.add(self.stack)
        # When a chooser has nothing to display, it looks ugly.
        # emptyMarker is a placeholder to display when there's nothing
        # else, and self.empty indicates that it's in use.
        self.empty = False
        self.emptyMarker = self.makeSubWidget("---")
        self.emptyMarker.set_sensitive(False)
        self.emptyMarkerName = "despair"
        self.update(namelist, helpdict)
        
        gtklogger.connect(self.gtk, "button-press-event", self.buttonpressCB)

    def makeSubWidget(self, name):
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin=2)
        label = Gtk.Label(name, halign=Gtk.Align.START, hexpand=True, margin=5)
        image = Gtk.Image.new_from_icon_name('pan-down-symbolic',
                                             Gtk.IconSize.BUTTON)
        hbox.pack_start(label, expand=True, fill=True, padding=2)
        hbox.pack_start(image, expand=False, fill=False, padding=2)
        hbox.show_all()
        return hbox

    def update(self, namelist, helpdict={}):
        # update() returns True if something changed.
        debug.mainthreadTest()
        if namelist == self.namelist and helpdict == self.helpdict:
            return False
        self.namelist = namelist[:]
        self.helpdict = helpdict
        if self.namelist:
            self.gtk.set_sensitive(True)
            if self.empty:
                self.stack.remove(self.emptyMarker)
                self.empty = False
            for name in self.namelist:
                if not self.stack.get_child_by_name(name):
                    hbox = self.makeSubWidget(name)
                    self.stack.add_named(hbox, name)
            if self.current_string in self.namelist:
                self.set_state(self.current_string)
            else:
                self.set_state(self.namelist[0])
        else:
            # namelist is empty
            self.set_state(None)
            self.gtk.set_sensitive(False)
            if not self.empty:
                for widget in self.stack:
                    self.stack.remove(widget)
                self.empty = True
                self.stack.add_named(self.emptyMarker, self.emptyMarkerName)
                # self.stack.set_visible_child(self.emptyMarker)
        return True

    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def hide(self):
        debug.mainthreadTest()
        self.gtk.hide()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()
    def buttonpressCB(self, gtkobj, event):
        debug.mainthreadTest()
        self.popupMenu = Gtk.Menu()
        gtklogger.newTopLevelWidget(self.popupMenu, 'chooserPopup-'+self.name)
        self.popupMenu.set_size_request(self.gtk.get_allocated_width(), -1)
        newCurrentItem = None
        for name in self.namelist:
            if self.separator_func and self.separator_func(name):
                menuitem = Gtk.SeparatorMenuItem()
            else:
                menuitem = Gtk.MenuItem(name)
                gtklogger.setWidgetName(menuitem, name)
                gtklogger.connect(menuitem, 'activate', self.activateCB, name)
                gtklogger.connect(menuitem, 'enter-notify-event',
                                  self.enterItemCB)
                helpstr = self.helpdict.get(name, None)
                if helpstr:
                    menuitem.set_tooltip_text(helpstr)
                if name == self.current_string:
                    newCurrentItem = menuitem
            self.popupMenu.append(menuitem)
        if newCurrentItem:
            self.current_item = newCurrentItem
            self.current_item.select()
        else:
            self.current_item = None
        self.popupMenu.show_all()
        self.popupMenu.popup_at_widget(self.stack, Gdk.Gravity.SOUTH_WEST,
                                       Gdk.Gravity.NORTH_WEST, event)
        return False

    def activateCB(self, menuitem, name):
        debug.mainthreadTest()
        self.stack.set_visible_child_name(name)
        # TODO GTK3: It shouldn't be necessary to call
        # popupMenu.destroy() here, but during playback of a gtklogger
        # script the menu doesn't disappear unless it's explicitly
        # destroyed. The popup menu in the gfx window layer list does
        # *not* have this problem.  (popupMenu is stored in self only
        # so that it can be destroyed here.)
        self.popupMenu.destroy()
        self.popupMenu = None
        self.current_string = name
        if self.callback:
            self.callback(*(name,) + self.callbackargs)

    def enterItemCB(self, menuitem, event):
        debug.mainthreadTest()
        # When the mouse enters the pop-up menu, the initially
        # selected item has to be deselected manually.
        if self.current_item is not None and self.current_item is not menuitem:
            self.current_item.deselect()
            self.current_item = None

    def set_state(self, arg):
        # arg is either an integer position in namelist or a string in
        # namelist.
        debug.mainthreadTest()
        # Before the gtk3 upgrade, the equivalent of this routine
        # failed silently if arg was not None, a string, or an int, or
        # if it was a string that wasn't in the list.  It's now an
        # error.
        if not self.namelist and arg is None:
            # If the set of values is empty, None is the only legal arg.
            self.current_string = None
            return
        if arg is None:
            newstr = self.namelist[0]
        elif type(arg) == types.IntType:
            try:
                newstr = self.namelist[arg]
            except IndexError:
                raise ooferror.ErrPyProgrammingError(
                    "ChooserWidget index is out of range: %d" % arg)
        elif type(arg) == types.StringType:
            if arg not in self.namelist:
                raise ooferror.ErrPyProgrammingError(
                    "Invalid ChooserWidget argument: %s" % arg)
            newstr = arg
        else:
            raise ooferror.ErrPyProgrammingError(
                "Invalid ChooserWidget argument: %s %s" % (arg, arg.__class__))
        if newstr != self.current_string:
            self.stack.set_visible_child_name(newstr)
            self.current_string = newstr
            if self.update_callback:
                self.update_callback(*(self.current_string,) +
                                     self.update_callback_args)
            
    def get_value(self):
        return self.current_string
    def nChoices(self):
        return len(self.namelist)
    def choices(self):
        return self.namelist
            
                


class FakeChooserWidget:
    # For debugging only.
    def __init__(self, namelist, callback=None, callbackargs=(),
                 update_callback=None, update_callback_args=(), helpdict={}):
        debug.mainthreadTest()
        self.gtk = gtk.Label("Gen-u-wine Fake Widget")
        debug.fmsg(namelist)
    def show(self):
        pass
    def destroy(self):
        pass
    def setsize(self, namelist):
        pass
    def update(self, namelist, helpdict={}):
        debug.fmsg(namelist)
        return False
    def set_state(self, arg):
        pass
    def get_value(self):
        pass
    def nChoices(self):
        pass

## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ##

# The NewChooserWidget has a pulldown menu and a button.  The default
# text on the button is "New...".  The intent is that the callback for
# the button will create a new object to be listed in the pulldown
# menu. The button callback is responsible for updating the menu (with
# ChooserWidget.update) and selecting the new entry (with
# ChooserWidget.set_state).

class NewChooserWidget(ChooserWidget):
    def __init__(self, namelist, callback=None, callbackargs=(),
                 update_callback=None, update_callback_args=(),
                 button_callback=None, button_callback_args=(),
                 buttontext="New...",
                 separator_func=None):
        ChooserWidget.__init__(self, namelist,
                               callback=callback, callbackargs=callbackargs,
                               update_callback=update_callback,
                               update_callback_args=update_callback_args,
                               helpdict={}, separator_func=separator_func)

        self.button_callback = button_callback
        self.button_callback_args = button_callback_args
        
        # Wrap the ChooserWidget's gtk in a GtkHBox and make it become self.gtk
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hbox.pack_start(self.gtk, expand=True, fill=True, padding=2)
        self.gtk = hbox

        self.newbutton = Gtk.Button(buttontext)
        hbox.pack_start(self.newbutton, expand=False, fill=False, padding=2)
        gtklogger.connect(self.newbutton, 'clicked', self.newbuttonCB)
    def newbuttonCB(self, button):
        if self.button_callback:
            self.button_callback(*self.button_callback_args)
    def set_button_sensitivity(self, sensitivity):
        debug.mainthreadTest()
        self.newbutton.set_sensitive(sensitivity)
            

## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ##    

# Like a ChooserWidget, but makes a list instead of a pull-down menu.
# Locally stateful.  Callback gets called when selection state
# changes, with the newly-selected string or "None".  Takes both a
# list of objects, and a list of display strings for those objects.
# If comparison of two objects is nontrivial and not implemented by
# the objects' __eq__ function, the 'comparator' arg should be
# provided.  It should be a function of two objects that returns 1 if
# they are equal.

# 'callback' is called when an item is selected in the list.
# 'dbcallback' is called when an item is double-clicked, or 'return'
# is pressed when an item is selected and the list has focus.

## TODO MAYBE: Use helpdict to put tooltips on the list items.  This
## probably isn't important.  Most, maybe all, ChooserListWidgets
## display user-created objects, and don't have helpdicts.

class ChooserListWidgetBase:
    def __init__(self, objlist=None, displaylist=[], callback=None,
                 dbcallback=None, autoselect=True, helpdict={},
                 comparator=None, markup=False,
                 name=None, separator_func=None, **kwargs):
        debug.mainthreadTest()
        self.liststore = Gtk.ListStore(GObject.TYPE_STRING,
                                       GObject.TYPE_PYOBJECT)
        self.treeview = Gtk.TreeView(self.liststore, **kwargs)
        self.gtk = self.treeview
        self.treeview.set_property("headers-visible", 0)
        cell = Gtk.CellRendererText()
        if markup:
            # Expect to find pango markup in displaylist, which is
            # stored in column 0 of the ListStore.
            self.tvcol = Gtk.TreeViewColumn("", cell, markup=0)
        else:
            self.tvcol = Gtk.TreeViewColumn("", cell)
        self.treeview.append_column(self.tvcol)
        self.tvcol.add_attribute(cell, 'text', 0)
        self.autoselect = autoselect
        self.callback = callback or (lambda x, interactive=False: None)
        self.dbcallback = dbcallback or (lambda x: None)
        self.comparator = comparator or (lambda x, y: x == y)
        self.activatesignal = gtklogger.connect(self.treeview, 'row-activated',
                                               self.rowactivatedCB)

        # If separator_func is provided, it must be a function that
        # takes a Gtk.TreeModel and Gtk.TreeIter as arguments, and
        # return True if the row given by model[iter] is to be
        # represented by a separator in the TreeView.
        if separator_func:
            self.treeview.set_row_separator_func(separator_func)

        if name:
            gtklogger.setWidgetName(self.treeview, name)
        selection = self.treeview.get_selection()
        gtklogger.adoptGObject(selection, self.treeview,
                              access_method=self.treeview.get_selection)
        self.selectsignal = gtklogger.connect(selection, 'changed',
                                             self.selectionchangedCB)
        self.update(objlist or [], displaylist, helpdict=helpdict)

    def grab_focus(self):
        self.treeview.grab_focus()

    def suppress_signals(self):
        debug.mainthreadTest()
        self.activatesignal.block()
        self.selectsignal.block()
    def allow_signals(self):
        debug.mainthreadTest()
        self.activatesignal.unblock()
        self.selectsignal.unblock()

    def find_obj_index(self, obj):
        debug.mainthreadTest()
        if obj is not None:
            objlist = [r[1] for r in self.liststore]
            for which in range(len(objlist)):
                if self.comparator(obj, objlist[which]):
                    return which
        raise ValueError

    def rowactivatedCB(self, treeview, path, col):
        self.dbcallback(self.get_value())
    def selectionchangedCB(self, treeselection):
        self.callback(self.get_value(), interactive=True)

    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def hide(self):
        debug.mainthreadTest()
        self.gtk.hide()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

class ChooserListWidget(ChooserListWidgetBase):
    # Get the index of the current selection.
    def get_index(self):
        debug.mainthreadTest()
        treeselection = self.treeview.get_selection() # gtk.TreeSelection obj
        (model, iter) = treeselection.get_selected() #gtk.ListStore,gtk.TreeIter
        if iter is not None:
            return model.get_path(iter)[0]  # integer!
    def has_selection(self):
        debug.mainthreadTest()
        selection = self.treeview.get_selection()
        model, iter = selection.get_selected()
        return iter is not None
    def get_value(self):
        debug.mainthreadTest()
        selection = self.treeview.get_selection()
        model, iter = selection.get_selected()
        if iter is not None:
            return model[iter][1]
    def set_selection(self, obj):
        debug.mainthreadTest()
        self.suppress_signals()
        treeselection = self.treeview.get_selection()
        try:
            which = self.find_obj_index(obj)
        except ValueError:
            treeselection.unselect_all()
        else:
            treeselection.select_path(which)
            self.treeview.scroll_to_cell(which)
        self.allow_signals()

    def scroll_to_line(self, lineno):
        self.treeview.scroll_to_cell(lineno)
        
    # Replace the contents, preserving the selection state, if
    # possible.
    def update(self, objlist, displaylist=[], helpdict={}):
        debug.mainthreadTest()
        self.suppress_signals()
        old_obj = self.get_value()
        self.liststore.clear()

        if not objlist:
            self.liststore.append(["None", None])
            self.treeview.set_sensitive(False)
        else:
            self.treeview.set_sensitive(True)
            for obj, dispname in map(None, objlist, displaylist):
                if dispname is not None:
                    self.liststore.append([dispname, obj])
                else:
                    self.liststore.append([obj, obj])
        try:
            index = self.find_obj_index(old_obj)
        except ValueError:
            if self.autoselect and len(objlist) == 1:
                # select the only object in the list
                treeselection = self.treeview.get_selection()
                treeselection.select_path(0)
            # New value differs from old value, so callback must be invoked.
            self.callback(self.get_value(), interactive=False)
        else:                           # reselect current_obj
            treeselection = self.treeview.get_selection()
            treeselection.select_path(index)
        self.allow_signals()

# List widget that allows multiple selections

class MultiListWidget(ChooserListWidgetBase):
    def __init__(self, objlist, displaylist=[], callback=None,
                 dbcallback=None, autoselect=True, helpdict={},
                 comparator=None, name=None, separator_func=None,
                 markup=False, **kwargs):
        ChooserListWidgetBase.__init__(self, objlist, displaylist, callback,
                                       dbcallback, autoselect, helpdict,
                                       comparator=comparator, name=name,
                                       separator_func=separator_func,
                                       markup=markup, **kwargs)
        selection = self.treeview.get_selection()
        selection.set_mode(Gtk.SelectionMode.MULTIPLE)
    def get_value(self):
        debug.mainthreadTest()
        selection = self.treeview.get_selection()
        model, rows = selection.get_selected_rows()
        return [model[r][1] for r in rows]
    def has_selection(self):
        debug.mainthreadTest()
        selection = self.treeview.get_selection()
        model, rows = selection.get_selected_rows()
        return len(rows) > 0
    def update(self, objlist, displaylist=[], helpdict={}):
        debug.mainthreadTest()
        self.suppress_signals()
        old_objs = self.get_value()
        self.liststore.clear()
        for obj, dispname in map(None, objlist, displaylist):
            if dispname is not None:
                self.liststore.append([dispname, obj])
            else:
                self.liststore.append([obj, obj])
        treeselection = self.treeview.get_selection()
        for obj in old_objs:
            try:
                index = self.find_obj_index(obj)
            except ValueError:
                pass
            else:
                treeselection.select_path(index)
                
        self.allow_signals()
    def set_selection(self, selectedobjs):
        # does not unselect anything, or emit signals
        debug.mainthreadTest()
        self.suppress_signals()
        objlist = [r[1] for r in self.liststore]
        treeselection = self.treeview.get_selection()
        if selectedobjs:
            for obj in selectedobjs:
                try:
                    index = self.find_obj_index(obj)
                except ValueError:
                    pass
                else:
                    treeselection.select_path(index)
        self.allow_signals()
        self.callback(self.get_value(), interactive=False)

    def clear(self):
        debug.mainthreadTest()
        self.suppress_signals()
        selection = self.treeview.get_selection()
        selection.unselect_all()
        self.allow_signals()

##################################################

class ChooserComboWidget:
    def __init__(self, namelist, callback=None, name=None, **kwargs):
        # If a callback is provided, it's called a *lot* of times.
        # It's called for every keystroke in the entry part of the
        # widget and every time a selection is made in the list part
        # of the widget.
        debug.mainthreadTest()
        liststore = Gtk.ListStore(GObject.TYPE_STRING)
        self.combobox = Gtk.ComboBox.new_with_model_and_entry(liststore,
                                                              **kwargs)
        self.combobox.set_entry_text_column(0)
        if name:
            gtklogger.setWidgetName(self.combobox, name)
        self.gtk = self.combobox
        self.namelist = []
        self.current_string = None
        self.update(namelist)
        self.signal = gtklogger.connect(self.combobox, 'changed',
                                        self.changedCB)
        self.callback = callback

    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()

    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

    def suppress_signals(self):
        self.signal.block()
    def allow_signals(self):
        self.signal.unblock()

    def update(self, namelist):
        debug.mainthreadTest()
        current_string = self.combobox.get_child().get_text()
        try:
            current_index = namelist.index(current_string)
        except ValueError:
            if len(namelist) > 0:
                current_index = 0
            else:
                current_index = -1
        liststore = self.combobox.get_model()
        liststore.clear()
        for name in namelist:
            liststore.append([name])
        self.combobox.set_active(current_index)

    def changedCB(self, combobox):
        self.callback(self.get_value())

    def get_value(self):
        debug.mainthreadTest()
        val = self.combobox.get_child().get_text()
        return val

    def set_state(self, arg):
        debug.mainthreadTest()
        if type(arg) == types.IntType:
            liststore = self.combobox.get_model()
            self.combobox.get_child().set_text(liststore[arg][0])
        elif type(arg) == types.StringType:
            self.combobox.get_child().set_text(arg)
        self.combobox.get_child().set_position(-1)


        
## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ##
## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ##

# Variants of the above widgets...

class FramedChooserListWidget(ChooserListWidget):
    def __init__(self, objlist=None, displaylist=[],
                 callback=None, dbcallback=None, autoselect=True,
                 comparator=None, name=None, **kwargs):
        ChooserListWidget.__init__(self,
                                   objlist=objlist,
                                   displaylist=displaylist,
                                   callback=callback,
                                   dbcallback=dbcallback,
                                   autoselect=autoselect,
                                   comparator=comparator,
                                   name=name)
        quargs = kwargs.copy()
        quargs.setdefault("shadow_type", Gtk.ShadowType.IN)
        self.gtk = Gtk.Frame(**quargs)
        self.gtk.add(self.treeview)

class ScrolledChooserListWidget(ChooserListWidget):
    def __init__(self, objlist=None, displaylist=[], callback=None,
                 dbcallback=None, autoselect=True, comparator=None, name=None,
                 separator_func=None, markup=False, **kwargs):
        ChooserListWidget.__init__(self,
                                   objlist=objlist,
                                   displaylist=displaylist,
                                   callback=callback,
                                   dbcallback=dbcallback,
                                   autoselect=autoselect,
                                   comparator=comparator,
                                   name=name,
                                   separator_func=separator_func,
                                   markup=markup)
        quargs = kwargs.copy()
        quargs.setdefault('shadow_type', Gtk.ShadowType.IN)
        self.gtk = Gtk.ScrolledWindow(**quargs)
        gtklogger.logScrollBars(self.gtk, name=name+"Scroll")
        self.gtk.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.gtk.add(self.treeview)


class ScrolledMultiListWidget(MultiListWidget):
    def __init__(self, objlist=None, displaylist=[], callback=None, name=None,
                 separator_func=None, **kwargs):
        MultiListWidget.__init__(self, objlist, displaylist, callback,
                                 name=name, separator_func=separator_func)
        mlist = self.gtk
        self.gtk = Gtk.ScrolledWindow(**kwargs)
        self.gtk.set_shadow_type(Gtk.ShadowType.IN)
        self.gtk.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.gtk.add(mlist)
        
