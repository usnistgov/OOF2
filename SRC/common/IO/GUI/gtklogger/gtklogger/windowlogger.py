# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from . import widgetlogger
from . import loggers
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class WindowLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.Window,)
    def record(self, obj, signal, *args):
        # Don't log "destroy" signals, because they're sent for every
        # object that's destroyed, not just the one that initiated the
        # action.
        if signal == 'destroy':
            return self.ignore
        if signal == 'delete-event':
            # The gtk2 version did something more complicated here.
            # If GtkWidget.event returned False, indicating the the
            # delete event wasn't handled, it inserted a gtklogger
            # "postpone" line that explicitly destroyed the window.
            # That doesn't appear to be necessary with gtk3, at least
            # when using Gtk.main_do_event instead of GtkWidget.Event.
            return [
                "event(Gdk.EventType.DELETE,window=%s.get_window())"
                % self.location(obj, *args),
            ]
        if signal == 'configure-event':
            event = args[0]
            return ["%s.resize(%d, %d)" % (self.location(obj, *args),
                                          event.width, event.height)]
        return super(WindowLogger, self).record(obj, signal, *args)
