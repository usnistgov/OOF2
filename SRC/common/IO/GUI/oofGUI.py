# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## TODO SANITY: There are too many redundant switchboard notifications
## being sent to the GUI.  Besides cluttering up the gui tests with
## extra checkpoints, this may slow down the interface.  The extra
## calls could be reduced if each menu item (Worker?) stored the calls
## and removed redundant ones before emitting them at the appropriate
## time.  The appropriate time might be hard to define.  For most
## menuitems, it might be when the callback returns.  Other menu items
## might need to force switchboard notifications to be emitted
## immediately.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import guitop
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import runtimeflags
from ooflib.common import thread_enable
from ooflib.common import utils
from ooflib.common.IO import gfxmanager
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import reporter
from ooflib.common.IO.GUI import chooser
from ooflib.common.IO.GUI import gfxmenu
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from ooflib.common.IO.GUI import historian
from ooflib.common.IO.GUI import mainthreadGUI
from ooflib.common.IO.GUI import quit
from ooflib.common.IO.GUI import widgetscope
import ooflib.common.quit

from gi.repository import Gtk

allPages = {}                           # dictionary of pages keyed by name
pagenames = []                          # ordered list of pages

if config.dimension() == 2:
    oofname = "OOF2"
elif config.dimension() == 3:
    oofname = "OOF3D"

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class oofGUI(widgetscope.WidgetScope):
    def __init__(self):
        debug.mainthreadTest()
        widgetscope.WidgetScope.__init__(self, None)
        self.gtk = Gtk.Window(Gtk.WindowType.TOPLEVEL)
        self.gtk.set_title(oofname)
        initial_width, initial_height = map(int,
                                            runtimeflags.geometry.split('x'))
        self.gtk.set_default_size(initial_width, initial_height)
        gtklogger.newTopLevelWidget(self.gtk, oofname)
        gtklogger.connect(self.gtk, "delete-event", self.deleteEventCB)
        gtklogger.connect_passive(self.gtk, "configure-event")
        self.gtk.connect("destroy", self.destroyCB)
        guitop.setTop(self)
        
        map(self.addStyle, gtkutils.styleStrings)
        
        self.mainbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                               spacing=2, margin=5)
        self.gtk.add(self.mainbox)

        self.menubar = Gtk.MenuBar()
        self.mainbox.pack_start(self.menubar, expand=False, fill=False, padding=0)
        accelgrp = Gtk.AccelGroup()
        self.gtk.add_accel_group(accelgrp)

        self.mainmenu = mainmenu.OOF
        self.oofmenu = gfxmenu.gtkOOFMenuBar(self.mainmenu, bar=self.menubar,
                                             accelgroup=accelgrp,
                                             parentwindow=self.gtk)
        gtklogger.setWidgetName(self.oofmenu, "MenuBar")
        self.pageChooserFrame = Gtk.Frame()
        self.pageChooserFrame.set_shadow_type(Gtk.ShadowType.IN)
        self.mainbox.pack_start(self.pageChooserFrame,
                                expand=False, fill=False, padding=2)

        chooserBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                             halign=Gtk.Align.CENTER, spacing=3,
                             border_width=2)
        gtklogger.setWidgetName(chooserBox, 'Navigation')
        self.pageChooserFrame.add(chooserBox)

        self.historian = historian.Historian(self.historianCB,
                                             self.sensitizeHistory)

        label = Gtk.Label('Task:')
        chooserBox.pack_start(label, expand=False, fill=False, padding=2)
        
        self.prevHistoryButton = gtkutils.StockButton('go-first-symbolic')
        chooserBox.pack_start(self.prevHistoryButton, expand=False, fill=False, 
                              padding=0)
        gtklogger.setWidgetName(self.prevHistoryButton, 'PrevHist')
        gtklogger.connect(self.prevHistoryButton, 'clicked', 
                          self.historian.prevCB)
        self.prevHistoryButton.set_tooltip_text(
            "Go to the chronologically previously page.")

        self.prevPageButton = gtkutils.StockButton('go-previous-symbolic')
        chooserBox.pack_start(self.prevPageButton, expand=False, fill=False,
                              padding=0)
        gtklogger.setWidgetName(self.prevPageButton, 'Prev')
        gtklogger.connect(self.prevPageButton, 'clicked', self.prevPageCB)
        self.pageChooser = chooser.ChooserWidget([],
                                                 callback=self.pageChooserCB,
                                                 name="PageMenu",
                                                 homogeneous=True)
        chooserBox.pack_start(self.pageChooser.gtk, expand=False, fill=False,
                              padding=0)
        self.currentPageName = None

        self.nextPageButton = gtkutils.StockButton('go-next-symbolic')
        chooserBox.pack_start(self.nextPageButton, expand=False, fill=False,
                              padding=0)
        gtklogger.setWidgetName(self.nextPageButton, 'Next')
        gtklogger.connect(self.nextPageButton, 'clicked', self.nextPageCB)

        self.nextHistoryButton = gtkutils.StockButton('go-last-symbolic')
        chooserBox.pack_start(self.nextHistoryButton, expand=False, fill=False,
                              padding=0)
        gtklogger.setWidgetName(self.nextHistoryButton, 'NextHist')
        gtklogger.connect(self.nextHistoryButton, 'clicked',
                          self.historian.nextCB)
        self.nextHistoryButton.set_tooltip_text(
            "Go to the chronologically next page.")

        # Add a GUI callback to the "OOF2" windows item.
        oof2_item = self.mainmenu.Windows.OOF2
        oof2_item.add_gui_callback(self.menu_raise)

        # Frame around main pages.  GUI pages are added and removed
        # from it by installPage().
        self.pageframe = Gtk.Frame()
        self.pageframe.set_shadow_type(Gtk.ShadowType.IN)
        self.mainbox.pack_start(self.pageframe, expand=True, fill=True,
                                padding=0)
        self.pageStack = Gtk.Stack(homogeneous=True)
        self.pageframe.add(self.pageStack)

        # Add pages that may have been created before the main GUI was built.
        for pagename in pagenames:
            self.addPage(allPages[pagename])

    def addStyle(self, stylestring):
        styleContext = self.gtk.get_style_context()
        screen = self.gtk.get_screen()
        styleProvider = Gtk.CssProvider()
        styleProvider.load_from_data(stylestring)
        styleContext.add_provider_for_screen(
            screen, styleProvider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def installPage(self, pagename):
        debug.mainthreadTest()
        oldPage = None
        if self.currentPageName is not None:
            oldPage = allPages[self.currentPageName]
        self.currentPageName = pagename
        self.pageStack.set_visible_child_name(pagename)
        if oldPage is not None:
            oldPage.hidden()
        allPages[self.currentPageName].installed()
        self.sensitize()
        gtklogger.checkpoint("page installed " + self.currentPageName)

    def show(self, messages=[]):
        # Called as an idle callback by the start() function at the
        # bottom of this file.
        debug.mainthreadTest()
        for page in allPages.values():
            page.show()

        # don't use self.gtk.show_all(), since there may be page
        # components that shouldn't yet be shown.
        self.menubar.show_all()
        self.pageChooserFrame.show_all()
        self.pageframe.show()
        self.pageStack.show()
        for page in allPages.values():
            page.show() 
        self.mainbox.show()
        self.gtk.show()

        if self.currentPageName is None:
            self.installPage(pagenames[0])
            self.pageChooser.set_state(self.currentPageName)
            self.historian.record(pagenames[0])

        for m in messages:
            reporter.report(m)
        
    def addPage(self, page):
        self.pageStack.add_named(page.gtk, page.name)
        debug.mainthreadTest()
        pagetips = {}
        for pg in allPages.values():
            if pg.tip:
                pagetips[pg.name] = pg.tip
        self.pageChooser.update(pagenames, pagetips)
        self.sensitize()

    def pageChooserCB(self, pagename):
        self.installPage(pagename)
        self.historian.record(pagename)

    def nextPageCB(self, button):
        which = pagenames.index(self.currentPageName)
        newpage = pagenames[which+1]
        self.installPage(newpage)
        self.pageChooser.set_state(newpage)
        self.historian.record(newpage)

    def prevPageCB(self, button):
        which = pagenames.index(self.currentPageName)
        newpage = pagenames[which-1]
        self.installPage(newpage)        
        self.pageChooser.set_state(newpage)
        self.historian.record(newpage)

    def historianCB(self, pagename):
        self.installPage(pagename)
        self.pageChooser.set_state(pagename)

    def sensitize(self):
        debug.mainthreadTest()
        # If currentPageName is None, then the GUI hasn't been shown yet.
        if self.currentPageName is not None:
            which = pagenames.index(self.currentPageName)
            self.nextPageButton.set_sensitive(which != len(pagenames)-1)
            self.prevPageButton.set_sensitive(which != 0)

            if which < len(pagenames)-1:
                self.nextPageButton.set_tooltip_text(
                    "Go to the %s page" % allPages[pagenames[which+1]].name)
            else:
                self.nextPageButton.set_tooltip_text("Go to the next page.")
            if which > 0:
                self.prevPageButton.set_tooltip_text(
                    "Go to the %s page" % allPages[pagenames[which-1]].name)
            else:
                self.prevPageButton.set_tooltip_text("Go to the previous page.")
        self.sensitizeHistory()

    def sensitizeHistory(self):
        debug.mainthreadTest()
        self.nextHistoryButton.set_sensitive(self.historian.nextSensitive())
        self.prevHistoryButton.set_sensitive(self.historian.prevSensitive())
        next = self.historian.nextVal()
        if next is not None:
            self.nextHistoryButton.set_tooltip_text(
                "Go to the chronologically next page, %s." % next)
        else:
            self.nextHistoryButton.set_tooltip_text(
                "Go to the chronologically next page.")
        prev = self.historian.prevVal()
        if prev is not None:
            self.prevHistoryButton.set_tooltip_text(
                "Go the chronologically previous page, %s." % prev)
        else:
            self.prevHistoryButton.set_tooltip_text(
                "Go the chronologically previous page.")
            

    def deleteEventCB(self, *args):
        # quit.queryQuit() asks for confirmation and then either quits
        # or doesn't.  Since the quitting process begins on another
        # thread (waiting for other threads to finish) queryQuit()
        # will actually return if if it's really quitting.
        quit.doQueryQuit(self.gtk)
        return 1  # Don't destroy the window.  If we're really
                  # quitting, self.destroy() will be called in due
                  # course.
    def destroyCB(self, gtk):
        self.gtk = None
        guitop.setTop(None)
    def destroy(self):
        debug.mainthreadTest()
        if self.gtk:
            self.gtk.destroy()

            
    def stop(self):
        # Called at exit-time by the Quit menu item, including when
        # exit is triggered by closing the main OOF window.

        # Order of operations matters if there are layer editor
        # windows and graphics windows open, it's important that the
        # layer editors get shut down first.  So, we explicitly close
        # those subwindows here.  Other subwindows don't have these
        # constraints.
        debug.mainthreadTest()

        for window in gfxmanager.gfxManager.getAllWindows():
            gfxmanager.gfxManager.closeWindow(window)
          
        from ooflib.common.IO.GUI import console
        if console.current_console:
            console.current_console.gtk.destroy()

        from ooflib.common.IO.GUI import activityViewer
        if activityViewer.activityViewer:
            activityViewer.activityViewer.close()

        from ooflib.common.IO.GUI import reporter_GUI
        # iterate over a copy of the set so that its size doesn't
        # change during iteration.
        for m in set(reporter_GUI.allMessageWindows):
            m.gtk.destroy()

        # *This* line *is* required.
        Gtk.main_quit()


    # GUI callback for "OOF2" entry in Windows menu.  Normally,
    # the "subwindow" class provides this functionality, but the main
    # window is not a subwindow.
    def menu_raise(self, menuitem):
        debug.mainthreadTest()
        self.gtk.present_with_time(Gtk.get_current_event_time())
        

    
####################################################

# Pages added to the main OOF window must be subclasses of MainPage.
# The subclass's __init__ should call MainPage.__init__ and install
# all of its widgets into self.gtk, which is a GtkFrame constructed by
# MainPage.__init__.  A single instance of the subclass should be
# created.

class MainPage(widgetscope.WidgetScope):
    def __init__(self, name, ordering, tip=None):
        debug.mainthreadTest()
        widgetscope.WidgetScope.__init__(self, parent=gui)
        self.name = name
        self.ordering = ordering
        self.tip = tip
        self.gtk = Gtk.Frame()
        self.gtk.set_shadow_type(Gtk.ShadowType.NONE)
        # Insert the page in the proper spot
        for i in range(len(pagenames)):
            if self.ordering < allPages[pagenames[i]].ordering:
                pagenames.insert(i, name)
                if guitop.top():        # gui may not be constructed yet!
                    guitop.top().addPage(self)
                break
        else:                           # page goes at the end
            pagenames.append(name)
            if guitop.top():            # gui may not be constructed yet!
                guitop.top().addPage(self)
        allPages[name] = self
        gtklogger.setWidgetName(self.gtk, name+' Page')

        # Page sensitization can occur through a number of channels.
        # When more than one operation is taking place sequentially,
        # it's best to suppress sensitization until the last one
        # completes.  Those operations should be enclosed in a
        # suppressSensitization(True)...suppressSensitization(False)
        # block, which should be followed by the routine that actually
        # does the sensitization. That routine should only do anything
        # if sensitizable() return True.
        self.suppressSensitizationCount = 0

    # MainPage.show() should be redefined in subclasses that don't
    # always want to show all their widgets.  show() should call the
    # gtk.show method on the components of the page.  It's called when
    # the page is constructed.  It's *not* called when the GUI
    # switches to the page.  For that, see installed() and hidden(),
    # below.
    def show(self):
        self.gtk.show_all()
    def hide(self):                     # This seems not be called at all...
        self.gtk.hide()

    # Pages that have to do some calculation when they become visible
    # can redefine installed() and hidden(). 
    def installed(self):
        pass
    def hidden(self):           # TODO: rename to "uninstalled"
        pass
    def is_current(self):
        return gui.currentPageName == self.name

    def suppressSensitization(self, yes):
        if yes:
            self.suppressSensitizationCount += 1
        else:
            self.suppressSensitizationCount -= 1
            assert self.suppressSensitizationCount >= 0
    def sensitizable(self):
        return self.suppressSensitizationCount == 0

gui = oofGUI()

def start(messages=[]):
    debug.mainthreadTest()
    guitop.setMainLoop(True)
    # gui.show() can be run only after the main loop has started.
    # Some gui components need to have the whole threading machinery
    # available when they're starting up.  run_gui() installs
    # gui.show() as an idle callback which will run once the main loop
    # is running.
    mainthreadGUI.run_gui(gui.show, (messages,))
    try:
        Gtk.main()
    finally:
        guitop.setMainLoop(False)
        
    # if thread_enable.enabled():
    #     gtk.gdk.threads_init()
    #     ## We used to call gtk.gdk.threads_enter() and threads_leave()
    #     ## here, but they appear not to be necessary on OS X or Linux
    #     ## and to be detrimental on NetBSD.
    #     # gtk.gdk.threads_enter()
    # try:
    #     gtk.main()
    # finally:
    #     guitop.setMainLoop(False)
    #     # if thread_enable.enabled():
    #     #     gtk.gdk.threads_leave()

