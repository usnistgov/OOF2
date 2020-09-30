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

class WidgetLogger(loggers.GtkLogger):
    classes = (Gtk.Widget,)

    def location(self, widget, *args):
        path = logutils.getWidgetPath(widget)
        if path[0] not in logutils.getTopWidgetNames():
            raise logutils.GtkLoggerException(string.join(path, ':') + 
                                     " is not contained in a top-level widget")
        return "findWidget('%s')" % string.join(path, ':')

    def record(self, obj, signal, *args):
        ## TODO GTK3: Keep a weak ref to the previous wvar and re-use
        ## the old one if the current one is the same.
        if signal in ('button-press-event', 'button-release-event'):
            evnt = args[0]
            if signal == 'button-press-event':
                eventname = "BUTTON_PRESS"
            else:
                eventname = "BUTTON_RELEASE"
            return [
                "event(Gdk.EventType.%s,x=%20.13e,y=%20.13e,button=%d,state=%d,window=%s.get_window())"
                % (eventname, evnt.x, evnt.y, evnt.button, evnt.state,
                   self.location(obj, *args)),
            ]

        if signal in ('key-press-event', 'key-release-event'):
            # TODO: Is this needed?  Is it reliable?
            evnt = args[0]
            if signal == 'key-press-event':
                eventname = "KEY_PRESS"
            else:
                eventname = "KEY_RELEASE"
            # keymap = Gdk.Keymap.get_default()
            # ok, keymapkeys = keymap.get_entries_for_keyval(evnt.keyval)
            # print "keys=", [k.keycode for k in keymapkeys], \
            #     "event.hardware_keycode=", evnt.hardware_keycode

            return [
                # Including the hardware_keycode seems to be important
                # for getting the delete key to work, but it's not
                # portable, so I'm not sure what to do...
                "event(Gdk.EventType.%s, keyval=Gdk.keyval_from_name('%s'), state=%d, window=%s.get_window())"
                % (eventname, Gdk.keyval_name(evnt.keyval), evnt.state,
                   self.location(obj, *args))
            ]
        
        if signal == 'motion-notify-event':
            evnt = args[0]
            if logutils.suppress_motion_events(obj):
                return self.ignore
            return [
                "event(Gdk.EventType.MOTION_NOTIFY,x=%20.13e,y=%20.13e,state=%d,window=%s.get_window())"
                % (evnt.x, evnt.y, evnt.state, self.location(obj, *args))
            ]
        
        if signal == 'focus_in_event':
            return [
                "event(Gdk.EventType.FOCUS_CHANGE, in_=1, window=%s.get_window())" % self.location(obj, *args)
            ]

        # If a widget has lost focus because it's been destroyed for
        # some reason, then replaying the focus_out_event will fail.
        # The widget destruction was caused by a previous line in the
        # log file, so the widget will have been destroyed before the
        # focus_out_event is replayed.  Therefore it's necessary to
        # check that the widget still exists before issuing the
        # signal.
        if signal == 'focus_out_event':
            wvar = loggers.localvar('widget')
            return [
                "%s=%s" % (wvar,self.location(obj, *args)),
                "if %(widget)s: event(Gdk.EventType.FOCUS_CHANGE, in_=0, window=%(widget)s.get_window())" % dict(widget=wvar),
                "del %s" % wvar
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
                "event(Gdk.EventType.%(etype)s, window=%(widget)s.get_window())" % dict(etype=etype, widget=self.location(obj, *args))
            ]

        if signal == 'destroy':
            return ['%s.destroy()' % self.location(obj, *args)]

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
