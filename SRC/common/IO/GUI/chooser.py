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
import sys
import types

# The ChooserWidget creates a pull-down menu containing the given list
# of objects.  The currently selected object is shown when the menu
# isn't being pulled down.

# The objects are converted to displayed names by str(obj), which must
# return plain text.  No markup is allowed.  This is because the
# ChooserWidget uses markup to indicate the current selection, so it
# has to replace any angle braces in the selection's name with &lt;
# and &gt;.  If the name contained markup the replacement would
# destroy it.

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

## The values for a ChooserWidget can be any kind of object and don't
## have to be strings.  str() is used to convert the values to strings
## for display, but get_value() and set_state() work with the raw
## objects.

## ChooserWidget.set_state(arg) no longer allows arg to be an integer
## index.

class ChooserWidget:
    def __init__(self, objlist, callback=None, callbackargs=(),
                 update_callback=None, update_callback_args=(),
                 helpdict={}, name=None, separator_func=None,
                 allowNone=None, homogeneous=False, **kwargs):
        debug.mainthreadTest()
        self.name = name
        # separator_func takes a string arg and returns true if that
        # string should be represented by a Gtk.SeparatorMenuItem.
        self.separator_func = separator_func
        self.current_string = None
        self.callback = callback
        self.callbackargs = callbackargs
        self.update_callback = update_callback
        self.update_callback_args = update_callback_args
        self.helpdict = {}
        # Initialize namelist to None instead of [] so that the first
        # call to update will install self.emptyMarker if appropriate.
        self.namelist = None
        # If allowNone is True, then set_state(None) is allowed.  It
        # will display emptyMarker in the event box.
        self.allowNone = allowNone

        self.gtk = Gtk.EventBox()
        # The docs say that event boxes should generally be invisible
        # to avoid rendering artifacts, but then they need to be above
        # their children to propagate events properly.  HOWEVER,
        # setting visible=False somehow prevents the window from
        # opening when replaying a gui log file.  The button press
        # event is not processed.
        ##self.gtk.set_visible_window(False)
        ##self.gtk.set_above_child(True)
        gtklogger.setWidgetName(self.gtk, name)
        frame = Gtk.Frame(**kwargs)
        self.gtk.add(frame)
        # Using a Stack instead of a simple Label makes it easy to
        # make sure that the horizontal size of the Chooser doesn't
        # change when the visible label changes, if homogeneous=True.
        self.stack = Gtk.Stack(homogeneous=homogeneous)
        self.stack.set_can_focus(True)
        self.stack.set_focus_on_click(True)
        gtklogger.setWidgetName(self.stack, 'stack')
        frame.add(self.stack)
        # When a chooser has nothing to display, it looks ugly.
        # emptyMarker is a placeholder to display when there's nothing
        # else to display.
        self.emptyMarker = self.makeSubWidget("---")
        self.emptyMarker.set_sensitive(False)
        # Has the user asked for the widget to be sensitive? 
        self.user_sensitive = True

        self.update(objlist, helpdict)

        gtklogger.connect(self.gtk, "button-press-event", self.buttonpressCB)

        # Catch key press events so that hitting <Return> when the
        # widget has focus brings up the menu.
        self.gtk.add_events(Gdk.EventMask.KEY_PRESS_MASK)
        gtklogger.connect(self.gtk, "key-press-event", self.keyPressCB)

    def makeSubWidget(self, name):
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin=2)
        label = Gtk.Label(name, halign=Gtk.Align.START, hexpand=True, margin=5)
        image = Gtk.Image.new_from_icon_name('pan-down-symbolic',
                                             Gtk.IconSize.BUTTON)
        hbox.pack_start(label, expand=True, fill=True, padding=2)
        hbox.pack_start(image, expand=False, fill=False, padding=2)
        hbox.show_all()
        return hbox

    # update() returns True if something changed.
    def update(self, objlist, helpdict={}):
        debug.mainthreadTest()
        self.objlist = list(objlist) # objlist might be an iterator
        namelist = [str(n) for n in self.objlist]
        if namelist == self.namelist and helpdict == self.helpdict:
            return False
        self.namelist = namelist
        self.helpdict = helpdict

        for child in self.stack.get_children():
            self.stack.remove(child)
        self.stack.add(self.emptyMarker)
        for name in self.namelist:
            # Separators appear in the pull down menu but don't get a
            # stack entry.  The gui tests get the Chooser contents
            # from the stack, not the menu, and ignore separators.
            if not (self.separator_func and self.separator_func(name)):
                hbox = self.makeSubWidget(name)
                self.stack.add_named(hbox, name)
        if self.current_string not in self.namelist:
            if self.allowNone:
                newstr = None
            else:
                if namelist:
                    newstr = self.namelist[0]
                else:
                    newstr = None
        else:
            newstr = self.current_string

        self.set_state(newstr)
        self.sensitize()
        return True

    def grab_focus(self):
        self.stack.grab_focus()

    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()
    def hide(self):
        debug.mainthreadTest()
        self.gtk.hide()
    def destroy(self):
        debug.mainthreadTest()
        self.gtk.destroy()

    def buildPopUpMenu(self):
        self.popupMenu = gtklogger.newPopupMenu('chooserPopup-'+self.name)
        self.popupMenu.set_size_request(self.gtk.get_allocated_width(), -1)
        for name in self.namelist:
            if self.separator_func and self.separator_func(name):
                menuitem = Gtk.SeparatorMenuItem()
            else:
                # Since there's no point to switching to the current
                # value, make its entry insensitive, and in italics,
                # to give the user a clue to the current location in
                # the list.  It would be nice to just start in the
                # current location when the menu is popped up, like a
                # GtkComboBox, but that's not possible with a GtkMenu.
                # If the GtkComboBox allowed tooltips, we'd use it
                # instead.
                if name == self.current_string:
                    menuitem = Gtk.MenuItem.new_with_label("")
                    gtklogger.setWidgetName(menuitem, name)
                    label = menuitem.get_child()
                    ## TODO: If we want to allow markup in names, then
                    ## we need to do something smarter here.
                    nm = name.replace("&", "&amp;").\
                        replace("<", "&lt;").replace(">", "&gt;")
                    label.set_markup("<i>" + nm + "</i>")
                    menuitem.set_sensitive(False)
                else:
                    menuitem = Gtk.MenuItem(name)
                    gtklogger.setWidgetName(menuitem, name)
                    gtklogger.connect(menuitem, 'activate', self.activateCB,
                                      name)
                helpstr = self.helpdict.get(name, None)
                if helpstr:
                    menuitem.set_tooltip_text(helpstr)
            self.popupMenu.append(menuitem)
        self.popupMenu.show_all()
        
    def buttonpressCB(self, gtkobj, event):
        debug.mainthreadTest()
        # Rebuild menu each time it's used, so that the current item
        # is desensitized.
        self.buildPopUpMenu()
        self.popupMenu.popup_at_widget(self.stack, Gdk.Gravity.SOUTH_WEST,
                                       Gdk.Gravity.NORTH_WEST, event)
        return False

    def keyPressCB(self, eventbox, event):
        # Hitting <Return> when the widget has keyboard focus is the
        # same as clicking on it with the mouse.
        if event.keyval == Gdk.keyval_from_name('Return') and not event.state:
            self.buttonpressCB(None, event)
            return True         # this event has been handled
        return False            # invoke other handlers

    def activateCB(self, menuitem, name):
        debug.mainthreadTest()
        self.stack.set_visible_child_name(name)
        self.current_string = name
        # After the menu is used, focus returns to it so that it's not
        # randomly reassigned elsewhere.
        self.stack.grab_focus()
        if self.callback:
            self.callback(*(name,) + self.callbackargs)

    def set_state(self, arg):
        # arg is either an integer position in namelist or a string in
        # namelist.
        debug.mainthreadTest()
        # Before the gtk3 upgrade, the equivalent of this routine
        # failed silently if arg was not None, a string, or an int, or
        # if it was a string that wasn't in the list.  It's now an
        # error.  Also, ints aren't accepted as indices into the
        # list. They're accepted if they're in objlist.
        if (self.allowNone and arg is None) or self.nChoices() == 0:
            self.stack.set_visible_child(self.emptyMarker)
            newstr = None
        else:
            newstr = str(arg)
            if not newstr in self.namelist:
                raise ooferror.PyErrPyProgrammingError(
                    "Invalid ChooserWidget argument: %s" % arg)
            self.stack.set_visible_child_name(newstr)

        if newstr != self.current_string:
            self.current_string = newstr
            if self.update_callback:
                self.update_callback(*(self.current_string,) +
                                     self.update_callback_args)
    def set_sensitive(self, sens):
        self.user_sensitive = sens
        self.sensitize()
    def sensitize(self):
        self.gtk.set_sensitive(self.user_sensitive and self.nChoices() > 0)
            
    def get_value(self):
        if self.current_string is None:
            assert self.allowNone or not self.namelist
            return None
        which = self.namelist.index(self.current_string)
        return self.objlist[which]

    def nChoices(self):
        return len(self.namelist)
    def choices(self):
        return self.objlist
            
    def dumpState(self, comment):
        print(comment, self.current_string, file=sys.stderr)

                


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
        displist = list(displaylist)

        if not objlist:
            self.liststore.append(["None", None])
            self.treeview.set_sensitive(False)
        else:
            self.treeview.set_sensitive(True)
            for i, obj in enumerate(objlist):
                try:
                    dispname = displist[i]
                except IndexError:
                    self.liststore.append([obj, obj])
                else:
                    self.liststore.append([dispname, obj])
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
        displist = list(displaylist)
        for i, obj in enumerate(objlist):
            try:
                dispname = displist[i]
            except IndexError:
                dispname = obj
            self.liststore.append([obj, dispname])
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
        # We're not passing kwargs to the ComboBox constructor because
        # the constructor doesn't accept all the values that are in
        # kwargs, eg, halign.  This doesn't seem to be a problem in
        # the few cases in which this widget is used.  kwargs is set
        # (I think) by ParameterTable.makeSingleWidget().
        ## TODO GTK3? Don't use Gtk.ComboBox, because it looks
        ## different from the chooser widget varieties used elsewhere.
        ## Build a new widget in the style of ChooserWidget.  This
        ## will be a fair amount of work for a small aesthetic gain.
        self.combobox = Gtk.ComboBox.new_with_model_and_entry(liststore)
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
        if type(arg) == int:
            liststore = self.combobox.get_model()
            self.combobox.get_child().set_text(liststore[arg][0])
        elif isinstance(arg, (str, bytes)):
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
        
