# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from gi.repository import Gtk
from ooflib.common.IO.GUI import gtklogger
from ooflib.common import debug

# CanvasLogger is a subclass of gtklogger WidgetLogger that is
# specialized for a particular OOFCanvas in a GfxWindow.  It bypasses
# the usual record and replay methods for GtkLayout in order to record
# only the *user* coordinates of an event.  The translation from
# device to user coordinates can depend on the size of the canvas
# widget, which can be affected by things like the gtk theme or font
# sizes.  That means that if an event is recorded by its device
# coordinates in a log file recorded on one computer, it might
# translate into different user coordinates on a different computer.
# The solution is to record only the user coordinates.

# Translate Gdk event names to the simpler ones we use.  Any event
# whose name is a key in this dict will be handled by this logger.
# Other events will be passed on to the base class logger.
events = {"button-press-event" : "down",
          "button-release-event": "up",
          "motion-notify-event": "move"}

class CanvasLogger(gtklogger.widgetlogger.WidgetLogger):
    def __init__(self, gfxwindow):
        self.gfxwindow = gfxwindow
        # TODO GTK3: lastbutton is stored so that we can use a single
        # callback function for mouse button and mouse motion events,
        # even though mouse motion events don't have any button data.
        # This is ugly.  We should just have two kinds of callbacks,
        # and if the GfxWindow or the Toolbox or whoever wants to know
        # the button for motion event, it can keep track itself.
        self.lastbutton = 0
    def record(self, obj, signal, *args):
        # obj is the object that was clicked on to produce this event.
        # It should be the GtkLayout inside the given gfxwindow.  We
        # already have a reference to the window, so we don't need it.
        try:
            ename = events[signal]
        except KeyError:
            pass
        else:
            evnt = args[0]
            # logMouse returns a lists of strings to be inserted in
            # the gui log file.  When the log file is replayed,
            # executing the strings will reproduce the event, as if
            # the GfxWindow's mouse callback had been called.
            if ename in ("down", "up"):
                btn = self.lastbutton = evnt.button
            else:
                btn = self.lastbutton
            return self.gfxwindow.logMouse(ename, evnt.x, evnt.y, btn,
                                           evnt.state)
        return super(CanvasLogger, self).record(obj, signal, *args)
