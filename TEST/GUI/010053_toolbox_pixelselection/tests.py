# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *

def pixelSelectionSize(n):
    gtkentry = gtklogger.findWidget(
        'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Selection:size')
    txt = gtkentry.get_text()
    size = int(txt.split(' ')[0])
    if size == n:
        return True
    print >> sys.stderr, "Wrong pixel selection size. Expected %d, got %d" \
        % (n, size)
    return False

