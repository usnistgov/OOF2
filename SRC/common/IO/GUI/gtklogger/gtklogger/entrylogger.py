# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from gi.repository import Gtk
from . import widgetlogger

class EditableLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.Editable, Gtk.Entry)
    def record(self, obj, signal, *args):
        if signal == 'changed':
            text = obj.get_text().replace('\\', '\\\\')
            return ["%s.set_text('%s')" % (self.location(obj, *args),text)]
        if signal == 'insert_text':
            text = args[0]
            # args[2] should be the position, but it's not.  See
            # https://stackoverflow.com/questions/40074977/how-to-format-the-entries-in-gtk-entry/40163816
            pos = obj.get_position()
            return [
                "%s.insert_text('%s', %d)" % (self.location(obj, *args),
                                              text, pos)
                    ]
        if signal == 'delete_text':
            first = args[0]
            last = args[1]
            return [
                "%s.delete_text(%d, %d)" % (self.location(obj, *args),
                                            first, last)
                ]
                
        return super(EditableLogger, self).record(obj, signal, *args)

            
