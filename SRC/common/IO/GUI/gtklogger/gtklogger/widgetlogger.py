# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import loggers
from gi.repository import Gdk
from gi.repository import Gtk
import logutils

import string

## TODO GTK3: Use gtk_main_do_event instead of Gtk.Widget.event?  See
## https://developer.gnome.org/gtk3/stable/GtkWidget.html#gtk-widget-event

class WidgetLogger(loggers.GtkLogger):
    classes = (Gtk.Widget,)

    def location(self, widget, *args):
        name = logutils.getWidgetName(widget)
        if not name:
            raise logutils.GtkLoggerException("Unnamed widget")
        path = self._parentWidgetPath(widget) + [name]
        if path[0] not in logutils.getTopWidgetNames():
            raise logutils.GtkLoggerException(string.join(path, ':') + 
                                     " is not contained in a top-level widget")
        return "findWidget('%s')" % string.join(path, ':')
    def _parentWidgetPath(self, widget):
        parent = widget.get_parent()
        while parent is not None and logutils.getWidgetName(parent) is None:
            parent = parent.get_parent()
        if parent is None:
            return []
        return self._parentWidgetPath(parent) + [logutils.getWidgetName(parent)]

    def record(self, obj, signal, *args):
        ## TODO GTK3: Keep a weak ref to the previous wvar and re-use
        ## the old one if the current one is the same.
        if signal in ('button-press-event', 'button-release-event'):
            evnt = args[0]
            if signal == 'button-press-event':
                eventname = "BUTTON_PRESS"
            else:
                eventname = "BUTTON_RELEASE"
            wvar = loggers.localvar('widget')
            return [
                "%s = %s" % (wvar, self.location(obj, *args)),
                "%s.event(event(Gdk.EventType.%s,x=%20.13e,y=%20.13e,button=%d,state=%d,window=%s.get_window()))"
                % (wvar, eventname,
                   evnt.x, evnt.y, evnt.button, evnt.state, wvar)
                ]

        if signal in ('key-press-event', 'key-release-event'):
            evnt = args[0]
            if signal == 'key-press-event':
                eventname = "KEY_PRESS"
            else:
                eventname = "KEY_RELEASE"
            wvar = loggers.localvar('widget')
            
            keymap = Gdk.Keymap.get_default()
            ok, keymapkeys = keymap.get_entries_for_keyval(evnt.keyval)
            print "keys=", [k.keycode for k in keymapkeys], \
                "event.hardware_keycode=", evnt.hardware_keycode

            return [
                # Including the hardware_keycode seems to be important
                # for getting the delete key to work.
                "%s = %s" % (wvar, self.location(obj, *args)),
                "%s.event(event(Gdk.EventType.%s, keyval=Gdk.keyval_from_name('%s'), state=%d, window=%s.get_window()))"
                % (wvar, eventname, Gdk.keyval_name(evnt.keyval), evnt.state,
                   wvar)
                ]
        
        if signal == 'motion-notify-event':
            evnt = args[0]
            if logutils.suppress_motion_events(obj):
                return self.ignore
            wvar = loggers.localvar('widget')
            return [
                "%s = %s" % (wvar, self.location(obj, *args)),
                "%s.event(event(Gdk.EventType.MOTION_NOTIFY,x=%20.13e,y=%20.13e,state=%d,window=%s.get_window()))"
                % (wvar, evnt.x, evnt.y, evnt.state, wvar)
                ]
        
        if signal == 'focus_in_event':
            wvar = loggers.localvar('widget')
            return [
       "%s=%s" % (wvar, self.location(obj, *args)),
       "%(widget)s.event(event(Gdk.EventType.FOCUS_CHANGE, in_=1, window=%(widget)s.get_window()))" % dict(widget=wvar)
                ]
        
        if signal == 'focus_out_event':
            wvar = loggers.localvar('widget')
            return [
       "%s=%s" % (wvar,self.location(obj, *args)),
       "%(widget)s.event(event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=%(widget)s.get_window()))" % dict(widget=wvar)
                ]

        if signal in ('enter-notify-event', 'leave-notify-event'):
            evnt = args[0]
            device = evnt.get_device()
            if signal == 'enter-notify-event':
                etype = "ENTER_NOTIFY"
            else:
                etype = "LEAVE_NOTIFY"
            wvar = loggers.localvar('widget')
            return [
        "%s=%s" % (wvar, self.location(obj, *args)),
        "%(widget)s.event(event(Gdk.EventType.%(etype)s, window=%(widget)s.get_window()))" % dict(etype=etype, widget=wvar)
            ]

        ## TODO GTK3: We should catch and log allocation events on top
        ## level windows only.  Currently we don't catch any
        ## size-allocate signals except within the OOFCanvas, and it
        ## doesn't use gtklogger.
        if signal == 'size-allocate':
            alloc = obj.get_allocation()
            parent = obj.get_parent()
            return ["%s.size_allocate(Gdk.Rectangle(%d, %d, %d, %d))" \
                   % (self.location(obj, *args),
                      alloc.x, alloc.y, alloc.width, alloc.height)]
        return super(WidgetLogger, self).record(obj, signal, *args)
