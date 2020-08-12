# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import loggers
from gi.repository import Gtk
import logutils
import widgetlogger

class LayoutLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.Layout,)

    def record(self, obj, signal, *args):
        comment = []
        if signal == "button-press-event":
            wx, wy = obj.get_size()
            comment = ["# layout size (%d, %d)" %(wx, wy)]
        return comment + super(LayoutLogger, self).record(obj, signal, *args)
