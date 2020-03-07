# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common.IO.GUI import gtklogger
from gi.repository import Gtk

# TODO: Add gui logging somehow


fsdialog = None
defaultfont = "Mono 12"

def getFontName(parentwindow=None):
    global fsdialog, defaultfont
    if not fsdialog:
        fsdialog = Gtk.FontChooserDialog("OOF2 Font Chooser", parentwindow)
    fsdialog.set_font(defaultfont)
    result = fsdialog.run()
    newfont = fsdialog.get_font()
    fsdialog.hide()
    if result in (Gtk.ResponseType.CANCEL,
                  Gtk.ResponseType.DELETE_EVENT,
                  Gtk.ResponseType.NONE):
        return None
    defaultfont = newfont
    return newfont
