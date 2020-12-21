# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def _getStatusText():
    textviewer = gtklogger.findWidget('OOF2:Pixel Selection Page:Pane:DataScroll:DataView')
    buffer = textviewer.get_buffer()
    return buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter())
    
def pixelSelectionPageStatusCheck(npix, total):
    if total > 0:
        # Don't just check the numerical value of the selection
        # percentage.  Check the printed version.
        ptext = "%g" % (100.*npix/total)
        txt = "%d of %d pixels selected (%s%%)" % (npix, total, ptext)
    else:
        txt = "%d of %d pixels selected" % (npix, total)

    return gtkTextviewCompare(
        "OOF2:Pixel Selection Page:Pane:DataScroll:DataView", txt)
