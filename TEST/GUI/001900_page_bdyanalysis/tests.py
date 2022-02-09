# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
import types

def goSensitive(sensitive):
    return is_sensitive("OOF2:Boundary Analysis Page:Go") == sensitive

def bdyList(*bdys):
    return chooserListCheck(
        "OOF2:Boundary Analysis Page:Pane:frame:BoundaryListScroll:BoundaryList",
        bdys)


def msgFloat(*expectedvals, **kwargs):
    tolerance = kwargs.get('tolerance', 1.e-10)
    msgbuffer = gtklogger.findWidget("OOF2 Messages 1:Text").get_buffer()
    text = msgbuffer.get_text(msgbuffer.get_start_iter(),
                              msgbuffer.get_end_iter(), False)
    lastline = text.split('\n')[-2]
    actualvals = eval(lastline)
    if not isinstance(actualvals, tuple):
        actualvals = (actualvals,)
    if len(actualvals) != len(expectedvals):
        print("Expected %d values, but found $d" % (len(expectedvals), 
                                                  len(actualvals)), file=sys.stderr)
    for actual, expected in zip(actualvals, expectedvals):
        if abs(actual - expected) > tolerance:
            print("Expected %g, got %g" % (expected, actual), file=sys.stderr)
            return False
    return True

