# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Other parts of the code can call atShutDown() to specify a function
# to be called before quitting.  This is in its own file because it
# needs to be included in places where including the rest of quit.py
# causes import loops.

_cleanUpActions = []

def atShutDown(fn, *args, **kwargs):
    _cleanUpActions.append((fn, args, kwargs))

def runShutDownFns():
    for fn, args, kwargs in _cleanUpActions:
        fn(*args, **kwargs)
