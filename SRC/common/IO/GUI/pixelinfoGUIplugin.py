# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import pixelgroup
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common import subthread
from ooflib.common.IO.GUI import gtklogger
from gi.repository import Gtk
import ooflib.common.microstructure

#####################

# PixelInfoPlugIn classes need the following things:
#   * ordering, at the class level
#   * nrows, at the class level
#   * A constructor with arguments (GtkTable, row) which inserts nrows
#     of widgets into the table starting at the given row.
#   * A function update(toolbox, iPoint) that updates the widgets
#   * A function close() that's called when the toolbox is closed.
#   * A function nonsense() that's called when the mouse click isn't sensible.
#   * A function clear() that's called when the clear button is pressed.

## TODO: Use a metaclass instead of registerPlugInClass.  See pixelinfo.py.

# Here's a nearly useless baseclass:
class PixelInfoGUIPlugIn:
    def __init__(self, toolbox):
        self.toolbox = toolbox
    def close(self):
        del self.toolbox
    def update(self, point):
        pass
    def nonsense(self):
        pass
    def clear(self):
        pass
    

plugInClasses = []

def registerPlugInClass(plugin):
    plugInClasses.append(plugin)
    plugInClasses.sort(key=lambda p: p.ordering)
    switchboard.notify('new pixelinfo GUI plugin')

####################################

class MicrostructurePlugIn(PixelInfoGUIPlugIn):
    ordering = 2
    nrows = 2
    def __init__(self, toolbox, table, row):
        debug.mainthreadTest()
        PixelInfoGUIPlugIn.__init__(self, toolbox)
        label = Gtk.Label('microstructure=',
                          halign=Gtk.Align.END, hexpand=False)
        table.attach(label, 0,row,1,1)
        self.microtext = Gtk.Entry(hexpand=True, halign=Gtk.Align.FILL)
        gtklogger.setWidgetName(self.microtext, 'MSText')
        self.microtext.set_width_chars(12)
        self.microtext.set_editable(False)
        table.attach(self.microtext, 1,row,1,1)

        label = Gtk.Label('pixel groups=',
                          halign=Gtk.Align.END, hexpand=False)
        table.attach(label, 0,row+1,1,1)
        self.grouplist = Gtk.TextView(left_margin=5, right_margin=5,
                                      top_margin=5, bottom_margin=5)
        self.grouplist.set_editable(False)
        self.grouplist.set_cursor_visible(False)
        self.grouplist.set_wrap_mode(Gtk.WrapMode.WORD)
        gtklogger.setWidgetName(self.grouplist, 'Group view')
        scroll = Gtk.ScrolledWindow(halign=Gtk.Align.FILL, hexpand=True)
        gtklogger.logScrollBars(scroll, "MSScroll")
        scroll.set_shadow_type(Gtk.ShadowType.IN)
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll.add(self.grouplist)
        table.attach(scroll, 1,row+1,1,1)

        self.sbcallbacks = [
            switchboard.requestCallbackMain('changed pixel group',
                                            self.grpchanged),
            switchboard.requestCallbackMain('changed pixel groups',
                                            self.grpschngd),
            switchboard.requestCallbackMain('destroy pixel group',
                                            self.grpdestroy),
            switchboard.requestCallbackMain('renamed pixel group',
                                            self.grprenamed)
            ]
        self.update(None)

    def close(self):
        switchboard.removeCallbacks(self.sbcallbacks)
        PixelInfoGUIPlugIn.close(self)

    def clear(self):
        debug.mainthreadTest()
        self.microtext.set_text("")
        self.grouplist.get_buffer().set_text("")
        
    def update(self, where):
        subthread.execute(self.update_thread, (where,))
    def update_thread(self, where):
        debug.subthreadTest()
        microstructure = self.toolbox.findMicrostructure()
        if microstructure and where is not None:
            mscntxt = ooflib.common.microstructure.getMSContextFromMS(
                microstructure)
            msname = microstructure.name()
            mscntxt.begin_reading()
            try:
                names = pixelgroup.pixelGroupNames(microstructure, where)
            finally:
                mscntxt.end_reading()
            grpnames = '\n'.join(names)
        else:
            msname = '(No microstructure)'
            grpnames = ''
        mainthread.runBlock(self.reallyupdate, (msname, grpnames))
    def reallyupdate(self, msname, grpnames):
        debug.mainthreadTest()
        self.microtext.set_text(msname)
        self.grouplist.get_buffer().set_text(grpnames)

    def nonsense(self):
        debug.mainthreadTest()
        self.grouplist.get_buffer().set_text('')
        self.microtext.set_text('???')
    def grpchanged(self, group, ms_name):
        microstructure = self.toolbox.findMicrostructure()
        if microstructure and microstructure.name() == ms_name:
            if group.name() in microstructure.groupNames():
                self.update(self.toolbox.currentPixel())
    def grpschngd(self, ms_name):
        microstructure = self.toolbox.findMicrostructure()
        if microstructure and microstructure.name() == ms_name:
            self.update(self.toolbox.currentPixel())
    def grpdestroy(self, group, ms_name):
        microstructure = self.toolbox.findMicrostructure()
        if microstructure and microstructure.name() == ms_name:
            self.update(self.toolbox.currentPixel())                
    def grprenamed(self, group, oldname, newname):
        microstructure = self.toolbox.findMicrostructure()
        if microstructure:
            if newname in microstructure.groupNames():
                self.update(self.toolbox.currentPixel())

registerPlugInClass(MicrostructurePlugIn)


