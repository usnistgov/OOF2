# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Some of this stuff might want to live elsewhere, eventually... It's
# stuff that has been moved out of gtklogger.py to keep the public API
# file clean.

# This file also contains some global variables and access functions
# for them (so they're not really global variables...).  This helps to
# avoid import loops, because this files doesn't import anything else.

from gi.repository import Gtk
import string
import sys
import weakref

from . import checkpoint


class GtkLoggerException(Exception):
    def __init__(self, *args):
        self.msg = string.join(args, ' ')
    def __str__(self):
        return self.msg

#############################
    
# Any gtk.Widget that needs to have its signals logged and replayed
# must have a name, and enough of its widget ancestors must have names
# that the sequence of names uniquely identifies the widget.
# setWidgetName is used to assign the names.

def setWidgetName(widget, name):
    assert isinstance(widget, Gtk.Widget)
    assert name is not None
    # When saved in the log files, widget names are surrounded by
    # single quotation marks, so we have to make sure to use only
    # double quotes in widget names.  Since colons are used as
    # delimiters in widget paths, they must be replaced too, when they
    # occur in widget names.
    safename = name.replace("'", '"').replace(":", ";")
    
    widget.oofname = safename
    return safename

def getWidgetName(widget):
    return getattr(widget, 'oofname', None)

def getWidgetPath(widget):
    # Get the widget path as a list of strings.  This is the useful
    # form for everything other than I/O.
    name = getWidgetName(widget)
    if not name:
        raise GtkLoggerException("Unnamed widget!")
    return _parentWidgetPath(widget) + [name]

def getWidgetPathStr(widget):
    # Get the widget path as a colon separated string.  This is the
    # useful form for writing a log file and printing error messages.
    return ":".join(getWidgetPath(widget))

def _parentWidgetPath(widget):
    parent = widget.get_parent()
    while parent is not None and getWidgetName(parent) is None:
        parent = parent.get_parent()
    if parent is None:
        return []
    return _parentWidgetPath(parent) + [getWidgetName(parent)]

##############################

# Find a list of menu item names leading to the given
# Gtk.MenuItem.  This relies on setting Gtk.Menu.oofparent in
# gtklogger.set_submenu.  The return value is a tuple containing
# the parent widget of the top of the menu hierarchy and the list
# of menuitem names.

def getMenuPath(gtkmenuitem):
    path = [getWidgetName(gtkmenuitem)]
    parent = gtkmenuitem.get_parent()
    if isinstance(parent, Gtk.Menu):
        try:
            pp = parent.oofparent
        except AttributeError:
            # Parent is a Menu, but doesn't have oofparent set.
            # It must be a pop-up menu.
            pass
        else:
            pparent, ppath = getMenuPath(pp)
            return pparent, ppath+path
    return parent, path


##############################

# Dictionary of top level widgets keyed by name
topwidgets = weakref.WeakValueDictionary()

class GtkLoggerTopFailure(GtkLoggerException):
    pass

def getTopLevelWidget(name):
    try:
        return topwidgets[name]
    except KeyError:
        raise GtkLoggerTopFailure(name)

def getTopLevelWidgetName(widget):
    # This is just for debugging and doesn't have to be fast
    for name in topwidgets:
        if topwidgets[name] is widget:
            return name

def isTopLevelWidget(obj):
    return obj in topwidgets.values()

def getTopWidgetNames():
    ## TODO PYTHON3: Do we need to return a copy of the list? Is [:] needed?
    return list(topwidgets.keys())[:]

# Top-level widgets (mostly Gtk.Windows) must have their names
# assigned by newTopLevelWidget() instead of setWidgetName().

def newTopLevelWidget(widget, name):
    safename = setWidgetName(widget, name)
    widget.connect('map', _topmapCallback, safename)
    topwidgets[safename] = widget

def _topmapCallback(obj, name):
    checkpoint.checkpoint("toplevel widget mapped %s" % name)

##############################

## These findXXXX functions are mostly used within log files, but they
## can be useful within test functions as well. They're defined here
## so that test modules don't have to import replay.py.  replay.py
## imports the functions from here.

def findWidget(path):
    splitpath = path.split(':')
    top = getTopLevelWidget(splitpath[0])
    if len(splitpath) == 1:
        return top
    return _recursiveFindWidget(splitpath[1:], top)

# Given a path (list of widget names) and a base (starting widget),
# _recursiveFindGObject looks for and returns the Widget (or GObject)
# named by the path.  The search is a depth first search of the widget
# tree.
def _recursiveFindWidget(path, base):
    if not path:
        return base
    if isinstance(base, Gtk.Container):
        for child in base.get_children():
            childname = getWidgetName(child)
            if childname == path[0]:
                return _recursiveFindWidget(path[1:], child)
            if childname is None:
                result = _recursiveFindWidget(path, child)
                if result is not None:
                    return result
                # Didn't find anything using unnamed widgets.  Keep
                # looking at other children.

def findMenu(widget, path):
    assert isinstance(widget, Gtk.MenuShell)
    # widget is a Gtk.MenuShell (container for MenuItems)
    # path is a list of strings (menu item names)
    for child in widget.get_children(): # child is a Gtk.MenuItem
        if getWidgetName(child) == path[0]:
            if len(path) == 1:
                return child
            return findMenu(child.get_submenu(), path[1:])

def setComboBox(widget, name):
    # Set the state of a ComboBox to a given string.  This assumes
    # that the ComboBox's first CellRenderer is a CellRendererText.
    model = widget.get_model()
    names = [row[0] for row in model]
    index = names.index(name)
    widget.set_active(index)

# findCellRenderer can be used as the access_function argument when
# adopting a CellRenderer used in a Gtk.TreeView.  It takes two
# integer arguments, col and rend, that must be passed in via
# adoptGObject's access_kwargs argument.  col specifies a column of
# the TreeView, and rend specifies which of the CellRenderers in the
# column is being logged.

def findCellRenderer(treeview, col, rend):
    return treeview.get_column(col).get_cells()[rend]

# findAllWidgets returns the paths to all named widgets under (and
# including) the given widget.  It *won't* find adopted non-widget
# objects.  It's mostly for debugging.

def findAllWidgets(topname):
    if isinstance(topname, Gtk.Widget):
        return _findAllWidgets(topname)
    return _findAllWidgets(findWidget(topname))
def _findAllWidgets(top):
    topname = getWidgetName(top)
    childpaths = []
    if isinstance(top, Gtk.Container):
        for child in top.get_children():
            childpaths.extend(_findAllWidgets(child))
    if topname:
        childpaths = [topname] + \
                     [string.join([topname, path], ':') for path in childpaths]
    return childpaths

# dumpAllWidgets prints the paths and widgets of all named widgets
# under and including the given widget.
def dumpAllWidgets(topname):
    aw = sorted(findAllWidgets(topname)[:]) ## TODO PYTHON3: Do we need [:] ?
    basepath = ':'.join(topname.split(':')[:-1])
    for name in aw:
        print("dumpAllWidgets:", name, findWidget(basepath
                                                                 + ':' + name), file=sys.stderr)

##############################

# Keep track of the run level, which is the gtk run level plus the
# number of open modal dialogs.  See the comment in
# GUILogLineRunner.__call__.

dialog_level = 0
def run_level():
    return Gtk.main_level() + dialog_level
def increment_dialog_level():
    global dialog_level
    dialog_level += 1

def decrement_dialog_level():
    global dialog_level
    dialog_level -= 1

###

_replaying = False
def replaying():
    return _replaying

def set_replaying(val):
    global _replaying
    _replaying = val

###

_logfile = None

def recording():
    return _logfile is not None

def logfile():
    return _logfile

def set_logfile(fileobj):
    global _logfile
    _logfile = fileobj


###

_debugLevel = 0

def debugLevel():
    return _debugLevel

def set_debugLevel(n):
    global _debugLevel
    _debugLevel = n

         
###

## log_motion_events() and dont_log_motion_events() control whether or
## not motion-notify-events will be logged.  If called with a widget
## argument, logging will be turned on or off for the specified widget
## and its children.  If the argument is omitted or None, logging will
## be turned on or off for all widgets, even those which had been the
## arguments of earlier calls to the functions.

## (The argument doesn't actually have to be a Gtk.Widget -- if a
## Logger has been created for some other type of object, it can use
## this machinery as well. If the object has a get_parent() method
## then turning logging on or off for an object will apply to its
## children.  If there's no get_parent() method, the logging state
## only applies to the specified object.

## suppress_motion_events(widget) returns a boolean, specifying
## whether or not motion events should be suppressed (not logged) for
## the given widget.  If the argument is omitted or None, it returns
## the default value which applies to all widgets that have *not* been
## the argument of log_motion_events() or dont_log_motion_events().
## suppress_motion_events() should only be used inside Loggers.

## In practice, if it's necessary to turn motion event logging on and
## off for a widget, it may be easier to toggle the return value of
## the event handler.  If the user's event handler runs before
## gtklogger's handler, returning true from the user's handler will
## suppress gtklogger's handler.

_suppress_motion_events = True
_suppression_dict = weakref.WeakKeyDictionary()

def log_motion_events(widget=None):
    global _suppress_motion_events
    if widget is not None:
        _suppression_dict[widget] = False
    else:
        ## No widget specified.  Apply globally.
        _suppress_motion_events = False
        _suppression_dict.clear()

def dont_log_motion_events(widget=None):
    global _suppress_motion_events
    if widget is not None:
        _suppression_dict[widget] = True
    else:
        ## No widget specified.  Apply globally.
        _suppress_motion_events = True
        _suppression_dict.clear()

def suppress_motion_events(widget=None):
    if widget is not None:
        try:
            return _suppression_dict[widget]
        except KeyError:
            # See if the widget has a parent that's in the dictionary
            parent = _get_parent(widget)
            while parent is not None:
                try:
                    return _suppression_dict[parent]
                except KeyError:
                    pass
                parent = _get_parent(parent)
    return _suppress_motion_events

# Utility fn used by suppress_motion_events.  widget might not
# actually be a pygtk Widget.
def _get_parent(widget):                
    try:
        return widget.get_parent()
    except AttributeError:
        return  None


###

_allexceptions = [Exception]

def add_exception(excclass):
    _allexceptions.append(excclass)

def exceptions():
    return tuple(_allexceptions)

