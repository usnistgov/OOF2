# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
from ooflib.common.IO.GUI import gtklogger 

tbpath = 'OOF2 Graphics 1:Pane0:Pane1:Pane2:TBScroll:Pixel Info'

def checkReferenceText(txt):
    # print gtklogger.findAllWidgets(tbpath +':misorientation')
    # print gtklogger.findAllWidgets(tbpath)
    #gtklogger.dumpAllWidgets(tbpath)
    return gtkTextviewCompare(tbpath + ':reference:text', txt)

def checkSetRefButton(state):
    if is_sensitive(tbpath + ':setref') == state:
        return True
    print >> sys.stderr, "Set Reference button sensitivity check failed."

def checkSetSymButton(state):
    if is_sensitive(tbpath + ':symmetry:set') == state:
        return True
    print >> sys.stderr, "Set Symmetry button sensitivity check failed"

def checkVisibleRefWidget(name):
    stack = gtklogger.findWidget(tbpath + ':reference')
    return stack.get_visible_child_name() == name

def checkVisibleOrientationWidget(name):
    stack = gtklogger.findWidget(tbpath + ':orientation')
    return stack.get_visible_child_name() == name

def checkSymmetry(expected):
    return gtkTextCompare(tbpath + ':symmetry:text', expected)

def checkMisorientation(expected, tolerance=None):
    return gtkTextCompare(tbpath + ':misorientation', expected,
                          tolerance=tolerance)

def checkInitialState():
    return (checkReferenceText(
            'Select a pixel and click "Set Reference Point" to make it the reference.')
            and
            checkVisibleRefWidget("reftext") and 
            checkSetRefButton(False) and
            checkSetSymButton(True) and
            checkSymmetry("Space Group 1") and
            checkMisorientation("???"))

def checkOrientationButNoReference():
    return (checkReferenceText(
            'Select a pixel and click "Set Reference Point" to make it the reference.')
            and
            checkVisibleOrientationWidget("widget") and
            checkVisibleRefWidget("reftext") and 
            checkSetRefButton(True) and
            checkSetSymButton(True) and
            checkSymmetry("Space Group 1") and
            checkMisorientation("???"))

def checkOrientation(oclass, **kwargs):
    if oclass:
        return (checkVisibleOrientationWidget("widget") and
                checkSetRefButton(True) and
                checkOrientationWidget(tbpath + ':orientation:dummy',
                                       oclass, **kwargs))
    return (checkVisibleOrientationWidget("text") and
            checkSetRefButton(False))
    
def checkReference(x, y, oclass, **kwargs):
    return (checkVisibleRefWidget("refwidget") and
            checkOrientationWidget(tbpath + ':reference:orientation',
                                   oclass, **kwargs))
        

def findAllWidgets():           # DEBUGGING
    print "===>", gtklogger.findAllWidgets(tbpath+":symmetry")
