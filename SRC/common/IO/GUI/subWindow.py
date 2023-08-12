# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Base class for daughter windows of the main application window.
# This class catches the parent window's destroy signal, and
# calls the local destroy() function, which in turn destroys
# self.gtk, unless overridden.
#
# If you either override or pass in a callback, it should take two
# arguments.  The first will be "self" and the second will be the
# window emitting the signal (i.e. top.gtk).  It will be called
# instead of the default method when the subwindow should be
# destroyed.

# Construct the menu for the window's menubar.

from ooflib.SWIG.common import config
from ooflib.SWIG.common.guitop import top
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO.GUI import gfxmenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import quit 

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

## TODO: Menu creation here is clumsy and should be cleaned up.
## Currently the "menu" arg to the SubWindow constructor is expected
## to be either an OOFMenuItem or a string.  If it's a string, a menu
## is created with that name and File/Close and File/Quit are added to
## it, and the menu is attached to the window's menu bar.  If the
## "menu" arg is an OOFMenuItem, then it is attached to the menu bar
## without modification.

## A better scheme would be for the constructor arg to always be an
## OOFMenuItem, which could be in an existing OOFMenu or not.  The
## SubWindow constructor would always create File/Close and File/Quit
## menu items if they didn't already exist.  The subclasses could
## override the callback methods if necessary.  Having
## SubWindow.__init__ create the File/Quit would mean that the hack of
## setting File.Quit.data=self.gtk would be required in far fewer
## places.

## Subclasses of SubWindow and the menu arg they pass to SubWindow.__init__:
## GUIConsole (console.py)  passes _console_menu
## ActivityViewer, passes self.menu
## GfxWindowBase (uses self.menu from GhostGfxWindow, calls
##   SubWindow.__init__ from gfxwindow.py) passes self.menu
## MessageWindow (reporter_GUI.py)   passes self.menu_name
## TutorialClassGUI (tutorialsGUI.py) passes ""

class SubWindow:
    # Base class for non-modal windows which want to be destroyed when
    # the main OOF GUI window, which from here is top().gtk, gets
    # destroyed.
    def __init__(self, title, menu=None, callback=None, guiloggable=True):
        debug.mainthreadTest()
        self.gtk = Gtk.Window(type=Gtk.WindowType.TOPLEVEL, title=title)
        if guiloggable:
            gtklogger.newTopLevelWidget(self.gtk, title)
            gtklogger.connect_passive(self.gtk, 'delete-event')
            gtklogger.connect_passive(self.gtk, 'configure-event')
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                               spacing=2, margin=5)
        self.gtk.add(self.mainbox)

        # Checking the type is clumsy; the idea is that the caller
        # must provide either the name for the auto-generated menu, or
        # a menu to use instead.  See the TODO above.
        if isinstance(menu, (str, bytes)):
            # If no menu is provided, then build a non-logging local
            # one with 'Close' and 'Quit'.
            self.subwindow_menu = oofmenu.OOFMenuItem(
                menu, secret=1, gui_only=1, no_log=1)

            file_item = oofmenu.OOFMenuItem('File', gui_only=1, no_log=1)
            self.subwindow_menu.addItem(file_item)

            file_item.addItem(oofmenu.OOFMenuItem(
                'Close', help="Close this window.",
                callback=self.menu_close,
                no_log=1, gui_only=1, accel='w'))
            
            file_item.addItem(oofmenu.OOFMenuItem(
                'Quit', gui_callback=quit.queryQuit,
                no_log=1, gui_only=1,
                help="Quit the OOF application.",
                accel='q', threadable = oofmenu.UNTHREADABLE))
            # quit.queryQuit uses menuitem.data to know which window
            # to use as the base for its dialog box.
            file_item.Quit.data = self.gtk
                              
            mainmenu.OOF.addItem(self.subwindow_menu)
            self._local_menu = menu
        elif isinstance(menu, oofmenu.OOFMenuItem):
            self.subwindow_menu = menu
            self._local_menu = None # Flag indicating menu was passed in.
        else:
            raise TypeError("Incorrect type passed as menu to SubWindow.")

        # Build the menu bar and add it to the window.
##        self.menu_bar = None
        self.accel_group = Gtk.AccelGroup()
        self.gtk.add_accel_group(self.accel_group)
        self.menu_bar = gfxmenu.gtkOOFMenuBar(
            self.subwindow_menu, accelgroup=self.accel_group,
            parentwindow=self.gtk)
        if guiloggable:
            gtklogger.setWidgetName(self.menu_bar, "MenuBar")

        self.mainbox.pack_start(self.menu_bar, fill=False, expand=False,
                                padding=0)

        # Add the "Windows" menu to the bar.
        self.windows_gtk_menu_item = gfxmenu.gtkOOFMenu(
            mainmenu.OOF.Windows, self.accel_group, parentwindow=self.gtk)
        self.menu_bar.append(self.windows_gtk_menu_item)

        self.menu_bar.connect("destroy", self.menu_bar_destroyed)
        
        if callback is None:
            callback = self.destroySubWindow
        top().gtk.connect("destroy", callback)

    # It is assumed, here, that if the menu bar has been destroyed,
    # the destruction of the SubWindow wrapper object is imminent,
    # so it's safe to cut the menu loose.
    def menu_bar_destroyed(self, gtk):
        if self._local_menu:
            # Disconnect the menu.
            self.subwindow_menu.clearMenu()
            mainmenu.OOF.removeItem(self._local_menu)
            self.subwindow_menu = None
    
    # Default close routine, callback for the default menu item.
    def menu_close(self, menuitem):
        mainthread.runBlock(self.close_thread)
    def close_thread(self):
        debug.mainthreadTest()
        self.gtk.destroy()

    def destroySubWindow(self, *args):
        debug.mainthreadTest()
        if self.gtk:
            self.gtk.destroy()
            self.gtk = 0

    # This takes arguments so it can be used as a callback.
    def raise_window(self, *args):
        debug.mainthreadTest()
        self.gtk.present_with_time(Gtk.get_current_event_time())

# used by several of the subwindows for naming window.
def oofname():
    if config.dimension() == 2:
        return "OOF2"
    elif config.dimension() == 3:
        return "OOF3D"
    



