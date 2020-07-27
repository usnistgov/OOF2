# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This file adds GUI code to the menu items defined in common.IO.mainmenu

## TODO GTK3: This file should not be imported by anything except
## initialize.py

from ooflib.SWIG.common import guitop
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO.GUI import activityViewer
from ooflib.common.IO.GUI import fontselector
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import oofGUI
from ooflib.common.IO.GUI import parameterwidgets
from gi.repository import Gtk
import os

##########################

from ooflib.common.IO.GUI import quit
mainmenu.OOF.File.Quit.add_gui_callback(quit.queryQuit)
# All Quit menu items need to set menuitem.data so that their Dialogs
# appear over the window containing the menu.  It's safe to refer to
# guitop.top here because the GUI is created when oofGUI is imported.
assert guitop.top() is not None
mainmenu.OOF.File.Quit.data = guitop.top().gtk

############################

def open_activityviewer(menuitem):
    activityViewer.openActivityViewer()
    menuitem()                          # just logs this command
mainmenu.OOF.Windows.Activity_Viewer.add_gui_callback(open_activityviewer)

############################

def setFont_gui(menuitem):
    fontname = fontselector.getFontName()
    if fontname:
        menuitem.callWithDefaults(fontname=fontname)

mainmenu.OOF.Settings.Fonts.Widgets.add_gui_callback(setFont_gui)

def reallySetFont(fontname):
    debug.mainthreadTest()
    settings = Gtk.Settings.get_default()
    settings.set_property("gtk-font-name", fontname)
    switchboard.notify('gtk font changed')

switchboard.requestCallbackMain('change font', reallySetFont)

##############################

# Any widget that uses a fixed width font should have its CSS name set
# to "fixedfont".

def setFixedFontSize(fontsize):
    gtkutils.addStyle("#fixedfont { font: %dpx monospace; }" % fontsize)

setFixedFontSize(mainmenu.fixedFontSize)

switchboard.requestCallbackMain('change fixed font', setFixedFontSize)

##############################

themedirs = [Gtk.rc_get_theme_dir(),
             os.path.join(os.path.expanduser("~"), ".themes")]

themes = []
for dir in themedirs:
    try:
        themes += os.listdir(dir)
    except:
        pass

if themes:
    # This is ugly... We can't use an EnumParam for the theme, because the
    # theme names are only known when the GUI is loaded.  But it's easiest
    # to use a EnumParameter and a ParameterDialog to get the value.  So
    # we create an Enum and an EnumParameter just for the GUI, then pass
    # the string to the menuitem.

    class ThemeEnum(enum.EnumClass(*themes)): pass

    themeParam = enum.EnumParameter('theme', ThemeEnum)

    def setTheme_gui(menuitem):
        if parameterwidgets.getParameters(themeParam,
                                          parentwindow=oofGUI.gui.gtk,
                                          title="Choose a Gnome Theme"):
            themename = themeParam.value.name
            menuitem.callWithDefaults(theme=themename)

    mainmenu.OOF.Settings.Theme.add_gui_callback(setTheme_gui)

    def reallySetTheme(themename):
        debug.mainthreadTest()
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-theme-name", themename)

    switchboard.requestCallbackMain('change theme', reallySetTheme)
