# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from gi.repository import Gtk
import widgetlogger
import logutils
import loggers

import string, sys

debugOption = 'B1'  # explicitly deactivate all pop-ups
#debugOption = 'B2' # explicitly deactivate parent of all nested pop-ups
#debugOption = 'B3' # don't explicitly deactivate any pop-ups

class MenuItemLogger(widgetlogger.WidgetLogger):
    classes = (Gtk.MenuItem,)
    def location(self, menuitem, *args):
        parent, path = logutils.getMenuPath(menuitem)
        parentcode = loggers.findLogger(parent).location(parent)
        return "findMenu(%s, %s)" % (parentcode, path)

    def record(self, obj, signal, *args):
        if signal == "activate":
            # If the menu is a nested pop-up menu, we need to hide or
            # destroy it after it's used. (Not sure why this is
            # necessary, but it seems to be.) Whether it needs to be
            # hidden or destroyed depends on whether the code is
            # reusing the pop-up, which we don't know.  TODO GTK3:
            # pop-up menus will need to be popped-up by gtklogger code
            # which can mark it as a pop-up (so checking here will be
            # easier) and also say if it is transient or not.
            parent, path = logutils.getMenuPath(obj)
            if debugOption != 'B3':
                if isinstance(parent, Gtk.Menu):
                    # obj is a pop-up menu.
                    if debugOption == 'B1':
                        return ["%s.activate() # MenuItemLogger" %
                                self.location(obj, args),
                                "%s.deactivate() # MenuItemLogger" %
                                loggers.findLogger(parent).location(parent)]
                    if debugOption == 'B2':
                        cmds = ["%s.activate() # MenuItemLogger" %
                                self.location(obj, args)]
                        if len(path) > 1:
                            # obj is a nested pop-up menu.  Its parent menu
                            # must be deactivated explicitly, inexplicably.

                            ## Chooser widget also needs to be explicitly
                            ## deactivated here.  WTF?
                            cmds.append("%s.deactivate() # MenuItemLogger" %
                                        loggers.findLogger(parent).location(parent))
                        return cmds
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
