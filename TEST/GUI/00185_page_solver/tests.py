# -*- python -*-
# $RCSfile: tests.py,v $
# $Revision: 1.1 $
# $Author: langer $
# $Date: 2011/06/08 19:04:53 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


from generics import *
import sys

def time_deriv_settable(bcname):
    path = 'Dialog-Initialize BC %s:initializer:Minimum:time_derivative' % bcname
    return gtklogger.findWidget(path) is not None

def value_settable(bcname):
    path = 'Dialog-Initialize BC %s:initializer:Minimum:value' % bcname
    return gtklogger.findWidget(path) is not None

def optionsCheck(bcname):
    path = 'Dialog-Initialize BC %s:initializer:Chooser' % bcname
    return chooserCheck(path, ["Minimum", "Maximum", "Average"])

def checkInitializees(*names):
    path='OOF2:Solver Page:VPane:FieldInit:Scroll:Initializers'
    displayed = [d.name() for d in treeViewColValues(path, 0)]
    ok = (displayed == list(names))
    if not ok:
        print >> sys.stderr, "Expected", names
        print >> sys.stderr, "Got", displayed
    return ok
