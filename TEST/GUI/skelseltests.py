# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Test functions used in the Skeleton Selection Page tests.

from ooflib.common.IO.GUI import gtklogger
import generics

def _statusText():
    bfr = gtklogger.findWidget(
        'OOF2:Skeleton Selection Page:Pane:status').get_buffer()
    return bfr.get_text(bfr.get_start_iter(), bfr.get_end_iter(), True)

    
def selectionSizeCheck(n):
    if n is None:
        return _statusText() == "No Skeleton selected."
    return int(_statusText().split()[0]) == n

def selectionModeCheck(name):
    return _statusText().split()[3] == name

def historySensitizationCheck(mode, prev, ok, next):
    return generics.sensitizationCheck(
        {'Prev': prev, 'OK': ok, 'Next': next},
        base="OOF2:Skeleton Selection Page:Pane:Selection:%sHistory" % mode)

def groupCheck(names):
    return generics.chooserListCheck(
        'OOF2:Skeleton Selection Page:Pane:Groups:GroupListScroll:GroupList',
        names)
