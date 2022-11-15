# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from . import widgetlogger
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ComboBoxLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.ComboBox,)
    def record(self, obj, signal, *args):
        if signal == 'changed':
            index = obj.get_active()
            val = obj.get_model()[index][0]
            if isinstance(val, (str, bytes)):
                return ["setComboBox(%s, '%s')" % 
                        (self.location(obj, args), val)]
            else:
                return ["%s.set_active(%d)" %
                        (self.location(obj, *args), index)]
        return super(ComboBoxLogger, self).record(obj, signal, *args)

