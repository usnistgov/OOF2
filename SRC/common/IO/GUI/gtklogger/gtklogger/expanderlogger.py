# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from . import widgetlogger

class ExpanderLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.Expander,)
    def record(self, obj, signal, *args):
        if signal == 'activate':
            return ["%s.set_expanded(%d)" % (self.location(obj, *args),
                                            obj.get_expanded())]
        return super(ExpanderLogger, self).record(obj, signal, *args)
