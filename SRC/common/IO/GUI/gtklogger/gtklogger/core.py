# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## This file contains the API for gtk_logger.  Nothing outside of this
## file should have to be explicitly called by users.

from gi.repository import Gtk
import atexit
import os
import string
import subprocess
import sys
import types
import weakref

import loggers
import logutils

_allexceptions = [Exception]
_process = None

def start(filename, debugLevel=2, suppress_motion_events=True,
          comment_gui=True):
    global _suppress_motion_events
    logutils.set_debugLevel(debugLevel)
    _suppress_motion_events = suppress_motion_events
    if logutils.recording():
        logutils.logfile().close()
    try:
        if comment_gui:
            # Open a pipe to the loggergui process for inserting
            # comments into the output stream.  The pipe is
            # line-buffered so that comments appear in the right
            # places.
            from GUI import loggergui
            guifile = os.path.abspath(loggergui.__file__)
            global _process
            _process = subprocess.Popen(
                ["python",
                 "-u",          # unbuffered stdin on the subprocess
                 guifile, filename
                 ],
                bufsize=1, # 0 means unbuffered, 1 means line buffered
                stdin=subprocess.PIPE)
            logutils.set_logfile(_process.stdin)
        elif type(filename) is types.StringType:
            logutils.set_logfile(open(filename, "w"))
        else:                   # filename is assumed to be a file
            logutils.set_logfile(filename)
    except:
        logutils.set_logfile(None)
        raise

def stop():
    if logutils.recording():
        try:
            logutils.logfile().close()
            ## On Linux, the loggergui process doesn't quit properly
            ## when it's input pipe is closed, and it needs to be
            ## terminated here. But on macOS, terminating it here
            ## kills the process before it writes any data.  Since I
            ## don't know the correct solution, I've just commented
            ## out the termination, on the theory that making the user
            ## close the loggergui window manually on Linux is better
            ## than not creating a log file on macOS.
            ## TODO: Fix this, somehow.
            # global _process
            # if _process is not None:
            #     _process.terminate()
            #     _process = None
        finally:
            logutils.set_logfile(None)

atexit.register(stop)

# Utility functions to turn on motion-event recording on or off.  If
# the widget argument is not None, the call applies to the given
# widget and its children.

def log_motion_events(widget=None):
    logutils.log_motion_events()

def dont_log_motion_events(widget=None):
    logutils.dont_log_motion_events()

# suppress_motion_events(widget) returns True if motion events have
# been suppressed for the given widget, or globally if widget is None.

def suppress_motion_events(widget=None):
    return logutils.suppress_motion_events()

def add_exception(excclass):
    logutils.add_exception(excclass)

##################################

# Any Gtk.Widget that needs to have its signals logged and replayed
# must have a name, and enough of its widget ancestors must have names
# that the sequence of names uniquely identifies the widget.
# setWidgetName is used to assign the names.

# NOTE that this name is not the same as the name that you might set
# with Gtk.Widget.set_name().  That name is used to decide what CSS
# styles to apply to the widget and need not be unique.  This name is
# used to identify the widget in log files and must be unique.

def setWidgetName(widget, name):
    return logutils.setWidgetName(widget, name)

# Top-level widgets (mostly Gtk.Windows) must have their names
# assigned by newTopLevelWidget() instead of setWidgetName().

def newTopLevelWidget(widget, name):
    return logutils.newTopLevelWidget(widget, name)

# Gtk.GObjects which aren't gtk.Widgets but still need to have their
# signals logged should be registered with adoptGObject(). 'obj' is
# the object being registered.  'parent' is an actual Gtk.Widget, and
# 'access_method' is a method of the parent class that retrieves the
# adopted GObject.  For example, to make the gtk.Adjustment that's
# part of a gtk.Range loggable, call
#    adoptGObject(range.get_adjustment(), range, range.get_adjustment)
# If there's no such parent class method, then use access_function
# instead of access_method.  The function will be called with the
# parent widget as its first argument.  In either case, additional
# arguments to the function can be passed in as access_args or
# access_kwargs.

def adoptGObject(obj, parent, access_method=None, access_function=None,
                 access_args=(), access_kwargs={}):
    assert not hasattr(obj, 'oofparent')
    assert parent is not None
    assert access_method is not None or access_function is not None
    obj.oofparent = parent
    if access_method is not None:
        obj.oofparent_access_method = access_method.__name__
    else:
        obj.oofparent_access_function = access_function.__name__
    obj.oofparent_access_args = access_args
    obj.oofparent_access_kwargs = access_kwargs

# set_submenu should be used instead of Gtk.MenuItem.set_submenu.

def set_submenu(menuitem, submenu):
    menuitem.set_submenu(submenu)
    submenu.oofparent = menuitem

# debug_connect makes the connection process very verbose.  It's useful
# if you need to find out what handlers go with which objects.  If you
# uncomment this function, also uncomment the @debug_connect lines
# below.

# def debug_connect(func):
#     def wrapper(obj, signal, *args, **kwargs):
#         guisignals = func(obj, signal, *args, **kwargs)
#         print "debug_connect: obj=", obj, "signal=", signal, \
#             "handlers=", guisignals.signals
#         return guisignals
#     return wrapper

# To have a Gtk.GObject's actions logged, use gtklogger.connect or
# gtklogger.connect_after instead of Gtk.GObject.connect.  If a widget
# that otherwise would have no callback needs to be logged, use
# gtklogger.connect_passive. 

# @debug_connect
def connect(obj, signal, callback, *args, **kwargs):
    logger = kwargs.get("logger", None)
    return GUISignals(
        obj,
        obj.connect(
            signal,
            CallBackWrapper(signal, callback=callback, logger=logger),
            *args)
    )

# @debug_connect
def connect_after(obj, signal, callback, *args, **kwargs):
    logger = kwargs.get("logger", None)
    return GUISignals(
        obj,
        obj.connect_after(
            signal,
            CallBackWrapper(signal, callback=callback, logger=logger),
            *args)
    )

# connect_passive should be used when an action needs to be logged and
# replayed, but wouldn't otherwise have a callback.  For example,
# keypresses in a Gtk.Entry often aren't connected, but still need to
# be logged.

# @debug_connect
def connect_passive(obj, signal, *args, **kwargs):
    logger = kwargs.get("logger", None)
    return GUISignals(
        obj,
        obj.connect(signal, CallBackWrapper(signal, logger=logger), *args)
        )

# @debug_connect
def connect_passive_after(obj, signal, *args, **kwargs):
    logger = kwargs.get("logger", None)
    return GUISignals(
        obj,
        obj.connect_after(signal, CallBackWrapper(signal, logger=logger), *args)
        )


class CallBackWrapper(object):
    def __init__(self, signal, callback=None, logger=None):
        self.callback = callback
        self.signal = signal
        self.logger = logger    # If None, will look up default logger for obj
    def __call__(self, obj, *args):
        loggers.signalLogger(obj, self.signal, self.logger, *args)
        if self.callback:
            return self.callback(obj, *args)
        return False

# GUISignals basically just makes it easier to block and unblock
# signals, since the gtk method is sort of klunky.  It used to be more
# important, because gtklogger used to connect *two* signals for each
# call to gtklogger.connect.
class GUISignals:
    def __init__(self, widget, *signals):
        self.signals = signals
        self.alive = True
        self.widget = weakref.ref(widget)
        if isinstance(widget, Gtk.Widget):
            widget.connect('destroy', self.destroyCB)
    def block(self):
        if self.alive:
            map(self.widget().handler_block, self.signals)
    def unblock(self):
        if self.alive:
            map(self.widget().handler_unblock, self.signals)
    def disconnect(self):
        if self.alive:
            map(self.widget().disconnect, self.signals)
        self.signals = ()
    def destroyCB(self, *args):
        self.alive = False
    def __repr__(self):
        return "(widget=%s,signals=%s)" % (self.widget, self.signals)

# We need to be able to tell if a dialog is running (see
# GUILogLineRunner in replay.py).  We do that by using a modified
# Dialog class that keeps track of how many dialogs are open.
        
class Dialog(Gtk.Dialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        connect_passive(self, 'delete-event')
        connect_passive(self, 'configure-event')
    def run(self):
        logutils.increment_dialog_level()
        try:
            result = super(Dialog, self).run()
        finally:
            logutils.decrement_dialog_level()
        return result
    def add_button(self, name, response_id):
        # Just to be nice to the programmer, turn on logging for the
        # buttons automatically.  Perhaps this should be optional.
        button = super(Dialog, self).add_button(name, response_id)
        assert type(name) is types.StringType
        setWidgetName(button, name)
        connect_passive(button, 'clicked')
        return button
    def add_action_widget(self, child, response_id):
        super(Dialog, self).add_action_widget(child, response_id)
        if logutils.getWidgetName(child) is None:
            if isinstance(response_id, Gtk.ResponseType):
                name = response_id.value_name
            else:
                name = response_id
            logutils.setWidgetName(child, 'widget_%s'%name)
        # "child" must be a 'activatable' widget, according to the
        # docs.  Presumably that means that it implements the
        # GtkActivatable interface.  The docs for GtkActivatable don't
        # mention which signals are emitted, so it's not obvious what
        # to connect to here.  Gtk.Button has an 'activate' signal,
        # but the docs say not to use it. Other GtkActivatable widgets
        # also have 'activate' signals, so I'm just hoping that it's
        # the right thing to connect to here.
        if isinstance(child, Gtk.Button):
            connect_passive(child, 'clicked')
        else:
            connect_passive(child, 'activate')

popupCount = 0

def newPopupMenu(name=None, **kwargs):
    menu = Gtk.Menu(**kwargs)
    global popupCount
    if name:
        pname = name
    else:
        pname = 'PopUp-'+`popupCount`
        popupCount += 1
    newTopLevelWidget(menu, pname)
    # When recording a gui log file, it's necessary to log the
    # 'deactivate' signal when a menu is closed without activating any
    # of its menuitems.  If 'deactivate' is not logged, the session
    # will hang when replayed.  However, if a menuitem *is* activated,
    # it's redundant to log both the menuitem's activation and the
    # menu's deactivation (and leads to a Gdk-CRITICAL error), because
    # activating the menuitem automatically deactivates the menu.
    # Unfortunately, the menu's deactivation signal is emitted before
    # the menuitem's activation signal, so the redundancy can be fixed
    # only by postprocessing the log file.
    connect_passive(menu, 'deactivate')
    return menu

# logScrollBars should be called on any ScrolledWindow whose scroll
# bars need to be logged.  It just encapsulates the adoptGObject calls
# that would otherwise be necessary.  It returns a pair of GUISignals
# objects, one for each scroll bar.  The return value can probably be
# ignored in most cases.

def logScrollBars(window, name=None):
    assert isinstance(window, Gtk.ScrolledWindow)
    if name is not None:
        setWidgetName(window, name)
    adoptGObject(window.get_hadjustment(), window,
                 access_method=window.get_hadjustment)
    adoptGObject(window.get_vadjustment(), window,
                 access_method=window.get_vadjustment)
    return (
        connect_passive(window.get_hadjustment(), 'value-changed'),
        connect_passive(window.get_vadjustment(), 'value-changed'))



## Test for uniqueness by finding all named widgets and checking that
## findWidget(gtkPath(widget))==widget.

def sanity_check(widget, path=[]):
    widgetname = logutils.getWidgetName(widget)
    if widgetname:
        path = path + [widgetname]
        if logutils.findWidget(string.join(path, ':')) is not widget:
            raise ValueError("%s is not a unique widget name" % path)
#         else:
#             print "ok:", path, widget.__class__.__name__
    if isinstance(widget, gtk.Container):
        for child in widget.get_children():
            sanity_check(child, path)

def comprehensive_sanity_check():
    for widget in logutils.topwidgets.values():
        sanity_check(widget)
    
##################

# Insert a comment in the log file.
def comment(*args):
    if logutils.recording():
        print >> logutils.logfile(), ' '.join(map(str, ("#",) + args))
        if logutils.debugLevel() >= 2:
            print >> sys.stderr, ' '.join(map(str, ("#",) + args))
