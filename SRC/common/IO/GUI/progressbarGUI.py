# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import lock
from ooflib.SWIG.common import progress
from ooflib.common import debug
from ooflib.common import mainthread
from ooflib.common.IO import progressbar
from ooflib.common.IO import progressbar_delay
from ooflib.common.IO import activityviewermenu
from ooflib.common.IO.GUI import activityViewer
from ooflib.common.IO.GUI import gtklogger
from ooflib.common.IO.GUI import gtkutils
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Pango

import sys

## TODO: Group progress bars from a single command/thread together.

class GUIProgressBar(progressbar.ProgressBar):
    idcounter = 0               # used in unique gtklogger names 
    def __init__(self, progress):
        debug.mainthreadTest()
        self.lock = lock.Lock()

        progressbar.ProgressBar.__init__(self, progress)
        self.dismissable = False
        progress.setProgressBar(self)

        self.gtk = Gtk.Frame()
        self.gtk.set_shadow_type(Gtk.ShadowType.IN)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.gtk.add(vbox)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        vbox.pack_start(hbox, expand=False, fill=False, padding=2)

        self.gtkprogressbar = Gtk.ProgressBar(
            name="fixedfont", # piggyback on the font styling for text widgets
            orientation=Gtk.Orientation.HORIZONTAL)
        self.gtkprogressbar.set_show_text(True)
        self.gtkprogressbar.set_ellipsize(Pango.EllipsizeMode.END)
        hbox.pack_start(self.gtkprogressbar, expand=1, fill=1, padding=0)

        self.stopbutton = gtkutils.StockButton("process-stop-symbolic", "Stop")
        gtklogger.setWidgetName(self.stopbutton, "Stop%d"%self.idcounter)
        self.idcounter += 1
        gtklogger.connect(self.stopbutton, 'clicked', self.stopButtonCB)
        hbox.pack_start(self.stopbutton, expand=False, fill=False, padding=0)

        self.timeout_id = None
        
    def schedule(self):
        # Schedule the bar for periodic updates via the gtk timeout
        # events.  The time is specified in milliseconds.
        self.timeout_id = GObject.timeout_add(progressbar_delay.period,
                                              self._updateGUI)

    def show(self):
        debug.mainthreadTest()
        self.gtk.show_all()

    def destroy(self):
        debug.mainthreadTest()
        if self.gtk is not None:
            self._disconnect()
            self._destroy()
    def _destroy(self):
        debug.mainthreadTest()
        if self.gtk is not None:
            if activityViewer.activityViewer is not None:
                activityViewer.activityViewer.dismissGTKBar(self)
            gtkobj = self.gtk
            self.gtk = None
            gtkobj.destroy()

    def disconnect(self):
        debug.mainthreadTest()
        # Called by the ActivityViewer when it closes and by Progress
        # objects when they're finished or destroyed, via the
        # mechanism in progressGUI.C.  
        self._disconnect()
        if activityviewermenu.autoDismiss:
            self._destroy()
        else:
            self.switchButton()
        activityViewer.sensitize()

    def _disconnect(self):      
        # called by disconnect() and destroy()
        debug.mainthreadTest()
        if self.timeout_id is not None:
            pgrs = self.progress
            pgrs.acquireThreadLock()
            try:
                timeout_id = self.timeout_id
                self.timeout_id = None
                self.progress = None
                pgrs.disconnectBar(self)
                GObject.source_remove(timeout_id)
            finally:
                pgrs.releaseThreadLock()

    def _updateGUI(self):       # timeout callback
        # Progress.acquireThreadLock() prevents the ThreadState from
        # deleting the Progress object until
        # Progress.releaseThreadLock() is called. 
        self.progress.acquireThreadLock()
        try:
            self.updateGUI()
            return True         # re-invoke the timeout callback
        finally:
            self.progress.releaseThreadLock()

    def updateGUI(self):        
        debug.mainthreadTest()
        # Display a new message on the bar, or erase an old one
        msg = self.progress.message()
        name = self.progress.name()
        if name and msg:
            lbl = name + ': ' + msg
        elif name:
            lbl = name
        elif msg:
            lbl = msg
        else:
            lbl = ""
        self.gtkprogressbar.set_text(lbl)
        # Update the bar itself
        self.progress.updateGUIBar(self.gtkprogressbar)

    def stopButtonCB(self, button):
        if not self.dismissable:
            if not (self.progress.finished() or self.progress.stopped()):
                self.progress.stop()
                if activityviewermenu.autoDismiss:
                    self.destroy()
                else:
                    self.switchButton()
        else:
            self.destroy()

    def switchButton(self): # Change the "Stop" button to a "Dismiss" button
        debug.mainthreadTest()
        if not self.dismissable:
            label = gtkutils.findChild(Gtk.Label, self.stopbutton)
            label.set_text("Dismiss")
            image = gtkutils.findChild(Gtk.Image, self.stopbutton)
            image.set_from_stock("gtk-cancel", Gtk.IconSize.BUTTON)
            self.dismissable = True
            activityViewer.sensitize()
        
#############

def _makeGUIBar(self):
    return GUIProgressBar(self)

progress.ProgressPtr.makeGUIBar = _makeGUIBar

def _updateDefiniteBar(self, gtkbar):
    debug.mainthreadTest()
    frac = self.getFraction()
    if frac > 1.0:
        frac = 1.0
    if frac < 0.0:
        frac = 0.0
    gtkbar.set_fraction(frac)

progress.DefiniteProgressPtr.updateGUIBar = _updateDefiniteBar

def _updateIndefiniteBar(self, gtkbar):
    debug.mainthreadTest()
    try:
        prevpulse = self.prevpulse
    except AttributeError:
        prevpulse = None
    if self.pulsecount() != prevpulse:
        self.prevpulse = prevpulse
        gtkbar.pulse()

progress.IndefiniteProgressPtr.updateGUIBar = _updateIndefiniteBar
