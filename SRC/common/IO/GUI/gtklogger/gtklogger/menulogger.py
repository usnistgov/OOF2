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
from . import logutils
from . import loggers

class MenuItemLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.MenuItem,)
    def location(self, menuitem, *args):
        parent, path = logutils.getMenuPath(menuitem)
        parentcode = loggers.findLogger(parent).location(parent)
        return "findMenu(%s, %s)" % (parentcode, path)

    def record(self, obj, signal, *args):
        if signal == "activate":
            # If the menu is a pop-up menu, we need to deactivate it
            # after it's used, sometimes.  Apparently menu items that
            # open dialog boxes don't require the menu to be
            # explicitly deactivated, but menu items that don't open
            # dialog boxes do.  This makes no sense at all.  In any
            # case we don't know whether or not the menu needs to be
            # deactivated.  deactivatePopup() attempts to deactivate
            # the pop-up, and ignores the exception that is raised if
            # it can't find it.
            parent, path = logutils.getMenuPath(obj)
            if isinstance(parent, Gtk.Menu):
                # obj is a pop-up menu.
                return ["%s.activate() # MenuItemLogger"
                        % self.location(obj, args),
                        "deactivatePopup('%s') # MenuItemLogger"
                        % logutils.getWidgetName(parent)]
            # Not a pop-up menu.
            return ["%s.activate()" % self.location(obj, args)]
        return super(MenuItemLogger, self).record(obj, signal, *args)


class RadioMenuItemLogger(MenuItemLogger):
    classes = (Gtk.RadioMenuItem,)
    def record(self, obj, signal, *args):
        # The "toggled" signal will be issued for both the
        # RadioMenuItem that's being activated and the one that's
        # being deactivated.  One call to set_active() will recreate
        # both signals.
        if signal == "toggled":
            if obj.get_active():
                return ["%s.set_active(True)" % self.location(obj, args)]
            else:
                return loggers.GtkLogger.ignore
        return super(RadioMenuItemLogger, self).record(obj, signal, *args)
    

class MenuLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.MenuShell,)
    def record(self, obj, signal, *args):
        if signal == 'deactivate':
            return ["%s.deactivate() # MenuLogger" % self.location(obj, args)]
        if signal == 'cancel':
            return ["%s.cancel() # MenuLogger" % self.location(obj, args)]
        return super(MenuLogger, self).record(obj, signal, *args)
