# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import threadstate
from ooflib.common import debug
from ooflib.common import thread_enable
from ooflib.common.IO.GUI import mainthreadGUI
import gobject
import gtk
import threading

# Thread-safe GTK mainiteration call -- wraps the gtk.mainiteration in
# threads_enter and threads_leave in the appropriate circumstances,
# i.e. when the main thread is in an idle or timeout callback.  This
# is required because idle callbacks and timeout callbacks need to
# acquire the GTK lock before making GTK calls.

## TOOO GTK3: We probably don't need these functions anymore, since
## all Gtk3 calls must be from the main thread.  The old version used
## gdk.threads_enter and gdk.threads_leave here.

def mainiteration(block=True):
     debug.mainthreadTest()
     Gtk.main_iteration_do(block)
          

# Looping version, processes the full event queue.  This also wraps
# the events_pending call, which is necessary to prevent blocking.

def mainiteration_loop(block=True):
     debug.mainthreadTest()
     while Gtk.events_pending():
          Gtk.main_iteration_do(block)

