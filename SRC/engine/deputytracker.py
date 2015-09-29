# -*- python -*-
# $RCSfile: deputytracker.py,v $
# $Revision: 1.7 $
# $Author: langer $
# $Date: 2014/09/27 21:40:42 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Code moved out of deputy.py to avoid an import loop.

from ooflib.common import debug

class DeputySelectionTracker:

    # SelectionTracker object that corresponds to a DeputySkeleton in
    # the SkeletonContext's skeleton stack.  DeputySkeletons don't
    # contain any data except for the positions of moved nodes, so the
    # selection state in a deputy must be exactly the same as in the
    # associated (sheriff) Skeleton. 
    
    def __init__(self, tracker):
        self.tracker = tracker
    def clone(self):
        # This is a no-op.  The null return value is used by
        # SelectionSet.clone() to flag the deputy trackers.
        pass
    def get(self):
        return self.tracker.get()

    ## All functions not explicitly declared here are executed by the
    ## associated non-deputy tracker.
    def __getattr__(self, attr):
        return getattr(self.tracker, attr)
    def implied_select(self, othertracker):
        pass
    
    # When selecting or deselecting objects up and down the Skeleton
    # stack, there's nothing to be done

    def selectDown(self, selectable, clist):
        if len(clist) > 1:
            clist[1].selectDown(selectable, clist[1:])
    def selectUp(self, selectable, plist):
        if len(plist) > 1:
            plist[1].selectUp(selectable, plist[1:])
    def deselectDown(self, selectable, clist):
        if len(clist) > 1:
            clist[1].deselectDown(selectable, clist[1:])
    def deselectUp(self, selectable, plist):
        if len(plist) > 1:
            plist[1].deselectUp(selectable, plist[1:])
    def __repr__(self):
        return "DeputySelectionTracker(%d, %d)" % (id(self), id(self.tracker))
    def sheriff(self):
        return self.tracker.sheriff()
    def promote(self):
        # Return a non-Deputy tracker that will act like this one.
        return self.tracker
    def redeputize(self, oldtracker, newtracker):
        if self.tracker is oldtracker:
            self.tracker = newtracker

class DeputyGroupTracker:
    def __init__(self, tracker):
        self.tracker = tracker
    def __getattr__(self, attr):
        return getattr(self.tracker, attr)
    def add_group(self, name):
        pass
    def clear_group(self, name):
        pass
    def remove_group(self, name):
        pass
    def rename_group(self, oldname, newname):
        pass
    def add(self, name, object):
        pass
    def remove(self, name, object):
        pass
    def addDown(self, group, selectable, clist):
        if len(clist) > 1:
            clist[1].addDown(group, selectable, clist[1:])
    def addUp(self, group, selectable, plist):
        if len(plist) > 1:
            plist[1].addUp(group, selectable, plist[1:])
    def removeDown(self, group, selectable, clist):
        if len(clist) > 1:
            clist[1].removeDown(group, selectable, clist[1:])
    def removeUp(self, group, selectable, plist):
        if len(plist) > 1:
            plist[1].removeUp(group, selectable, plist[1:])
    def sheriff(self):
        return self.tracker.sheriff()
    def promote(self):
        return self.tracker
    def __repr__(self):
        return "DeputyGroupTracker"
