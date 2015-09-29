# -*- python -*-
# $RCSfile: skeletonselectable.py,v $
# $Revision: 1.65 $
# $Author: reida $
# $Date: 2011/05/25 21:49:31 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import lock
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import timestamp
from ooflib.common import debug
from ooflib.common import ringbuffer
from ooflib.common import utils
from ooflib.engine import deputytracker
from ooflib.engine import skeletonselmodebase
import sys
import weakref

# A Selection object contains a RingBuffer of SelectionSets.  Undoing
# and redoing the selection changes the state of the RingBuffer and
# causes the newly current SelectionSet to be written into the
# SkeletonContext's stack of Skeletons (which is also a RingBuffer).
# A SelectionSet contains a dictionary of SelectionTrackers, one entry
# for each Skeleton in the SkeletonContext.


#########

# The SkeletonSelectable class.  This is the parent class of nodes,
# segments, and elements.  Every selectable can have zero or more parents
# and zero or more children, and should propagate its selection state
# upwards and downwards in a sensible way.  This allows the selection
# state to be propagated across skeleton modification events.  The
# "groups" datum contains identifiers of the groups of which this
# selectable is a member.

class SkeletonSelectable:
    def __init__(self, index):
        self.parent = []
        self.children = []
        self.selected = 0
        self.groups = set()
        self.index = index

    # # # #
    def isSelected(self):
        return self.selected


    # Comparison operators.  These are slightly strange, but there's a
    # good reason.  The __eq__ comparison is used to check for
    # duplicatesin lists, in particular the parent and child lists.
    # In the scenario where there is already an un-done skeleton on
    # the stack, being overwritten by a new skeleton, there is the
    # possibility of index duplication.  In this case, the addition of
    # child objects can be messed up if equal-index objects compare
    # equally.  You want an __eq__ operator in general so that
    # equality comparisons will be fast -- so, compare object IDs.
    # The __lt__ and __cmp__ operators are different, they are used
    # for ordering objects in uniquelists, in paritcular in the
    # "group" objects.  In this case, you *do* want to order by index,
    # because you want the ordering to be repeatable over different
    # runs or architectures.  So, in that case, use index comparison.
    # The pathology here is that you could have two selectables A and
    # B, with the properties that A is not less than B, B is not less
    # than A, and A is not equal to B.  This case doesn't arise.
    def __eq__(self, other):
        return id(self)==id(other)

    def __cmp__(self, other):
        if not isinstance(other, self.__class__):
            return -1
        return cmp(self.index, other.index)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return -1
        return self.index < other.index

    def __hash__(self):
        return self.index
    
    # On selection, recursively select_down all your children, then
    # select_up your parents.  The reason for the two selection paths
    # is to prevent having to process spurious selections from children.
    def select(self, clist, plist):
        self.selected = 1
        clist[0].add(self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].selectDown(c, clist[1:])
        if len(plist) > 1:
            for p in self.parent:
                plist[1].selectUp(p, plist[1:])
    def selectDown(self, clist):
        for p in self.parent:
            if not p.selected:
                return
        self.selected = 1
        clist[0].add(self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].selectDown(c, clist[1:])
    def selectUp(self, plist):
        for c in self.children:
            if not c.selected:
                return
        self.selected = 1
        plist[0].add(self)
        if len(plist) > 1:
            for p in self.parent:
                plist[1].selectUp(p, plist[1:])
        
    # Deselect the same way, except that the deselect only gets
    # propagated upwards if all the children are deselected.
    def deselect(self, clist, plist):
        self.selected = 0
        clist[0].remove(self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].deselectDown(c, clist[1:])
        if len(plist) > 1:
            for p in self.parent:
                plist[1].deselectUp(p, plist[1:])
    def deselectDown(self, clist):
        for p in self.parent:
            if p.selected:
                return
        self.selected = 0
        clist[0].remove(self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].deselectDown(c, clist[1:])
    def deselectUp(self, plist):
        for c in self.children:
            if c.selected:
                return
        self.selected = 0
        plist[0].remove(self)
        if len(plist) > 1:
            for p in self.parent:
                plist[1].deselectUp(p, plist[1:])

    # Also need nonrecursive "local" selection, for writing the
    # selection state.
    def local_select(self):
        self.selected = 1

    def local_deselect(self):
        self.selected = 0

    # Implied selection -- answers the question, "If I were selecting
    # you right now, whom else would I be selecting?"  "current" and
    # "new" are selection tracker objects, and the question is
    # answered by appending the appropriate children to the ".data"
    # member of the "new" selection tracker.  Note that actual
    # selection does not take place.  This is called to establish
    # trackers for new Skeletons.
    def implied_select(self, current, new):
        for c in self.children:
            # c will be selected if all of its parents are selected
            for p in c.parent:
                if p not in current.data:
                    break
            else:
                new.data.add(c)

    # # # #
        
    # Group membership -- assignment is mechanically like selection.
    # Child_track and parent_track are lists of GroupTracker objects
    # corresponding to appropriate skeletons, child being towards the
    # children starting from the current one, and parent being towards
    # the parent starting from the current one.

    def add_to_group(self, group, clist, plist):
        self.groups.add(group)
        clist[0].add(group, self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].addDown(group, c, clist[1:])
        if len(plist) > 1:
            for p in self.parent:
                plist[1].addUp(group, p, plist[1:])
    def addDown(self, group, clist):
        for p in self.parent:
            if group not in p.groups:
                return
        self.groups.add(group)
        clist[0].add(group, self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].addDown(group, c, clist[1:])
    def addUp(self, group, plist):
        for c in self.children:
            if group not in c.groups:
                return
        self.groups.add(group)
        plist[0].add(group, self)
        if len(plist) > 1:
            for p in self.parent:
                plist[1].addUp(group, p, plist[1:])

    # Removal is like deselection -- only remove the parent from the
    # group if all of the children are gone.

    def remove_from_group(self, group, clist, plist):
        self.groups.remove(group)
        clist[0].remove(group, self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].removeDown(group, c, clist[1:])
        if len(plist) > 1:
            for p in self.parent:
                plist[1].removeUp(group, p, plist[1:])
    def removeDown(self, group, clist):
        self.groups.remove(group)
        clist[0].remove(group, self)
        if len(clist) > 1:
            for c in self.children:
                clist[1].removeDown(c, clist[1:])
    def removeUp(self, group, plist):
        # Don't remove parent from the group unless all of its
        # children have been removed.
        for c in self.children:
            if group in c.groups:
                return
        self.groups.remove(group)
        plist[0].remove(group, self)
        if len(plist) > 1:
            for p in self.parent:
                plist[1].removeUp(p, plist[1:])

    # Local operations, not following parents or children.
    def add_group_to_local(self, group):
        self.groups.add(group)  # self.groups is a Set, always safe.

    def remove_group_from_local(self, group):
        self.groups.remove(group)
        
    # Create a copy of the original, which has the original as
    # its parent.  Provides the copy with the passed-in index.
    def copy_child(self,index,points=None):
        if points is None:
            new = self.new_child(index)
        else:
            new = self.new_child(index, points)
        new.parent = [self]
        self.children.append(new)
        return new

    # Add/remove parents and children.  Hides the implementation.
    # Does not promise consistency between parents and children.
    # *Does* promise uniqueness of objects in the lists.
    def add_parent(self, newparent):
        if newparent not in self.parent:
            self.parent.append(newparent)

    def remove_parent(self, oldparent):
        self.parent.remove(oldparent)

    def add_child(self, newchild):
        if newchild not in self.children:
            self.children.append(newchild)

    def remove_child(self, oldchild):
        self.children.remove(oldchild)

    # Implementation-independent way of accessing interior lists.
    # Return type is guaranteed to be a list for both of these routines.
    def getParents(self):
        return self.parent

    def getChildren(self):
        return self.children

    def makeSibling(self, newcomer):
        for p in self.parent:
            p.add_child(newcomer)
            newcomer.add_parent(p)
    
    # Routine to disconnect a selectable from its parents and children.
    def disconnect(self):
        for c in self.children:
            c.parent.remove(self)
        self.children = []
        for p in self.parent[:]:
            p.children.remove(self)
            self.parent.remove(p)
        self.parent = []

    # Utility function for identifying a "map" from an initial
    # selectable.  A "map" is two sets of selectables, s1 and s2,
    # related both topologically and familially.  All the selectables
    # in s2 are children of at least one selectable in s1, and all the
    # selectables in s1 are parents of at least one selectable in s2.
    # Maps should preserve connectivity, i.e. if nodes n1 and n2 are
    # connected in the parent set, then c(n1) and c(n2), if they
    # exist, should be connected in the child set.  There is also a
    # completeness requirement -- all the children of every selectable
    # in s1 should be present in s2, and all the parents of the
    # selectables in s2 should be present in s1.  It should also be
    # minimal, i.e. it should be the smallest set of selectables that
    # has the completeness property.
    def map(self):
        simple = 1
        parents = [self]
        children = self.children[:]

        for c in children:
            if len(c.parent)!=1:
                simple = 0
        if simple==1:
            # Note that this is also the return for the no-children case.
            return SelectableMap(source=parents, target=children)

        old_c = 0
        old_p = 0

        new_c = len(children)
        new_p = len(parents)

        while old_c!=new_c or old_p!=new_p:

            old_c = new_c
            old_p = new_p
            
            for c in children:
                for p in c.parent:
                    if p not in parents:
                        parents.append(p)
                    
            for p in parents:
                for c in p.children:
                    if c not in children:
                        children.append(c)
                    
            new_c = len(children)
            new_p = len(parents)
            
        return SelectableMap(source=parents, target=children)
            

# Handy object for aggregating the info.
class SelectableMap:
    def __init__(self, source=None, target=None):
        self.source = source or []
        self.target = target or []
    def __repr__(self):
        return "SelectableMap(source=%s, target=%s)" % \
               (`self.source`, `self.target`)
        


##############################################################

# Object for keeping track of selections in a SelectionSet on a
# per-skeleton basis.  The various SelectionSets (Element, Segment,
# and Node) have a dictionary keyed by skeletons in which these
# objects are stored, and pass lists of the objects on to to the
# skeletonselectable's select routine.  This is similar to the way the
# GroupTrackers operate.

# The base class doesn't actually contain any reference to selection
# per se, so that it can be used to track pinned nodes and other
# skeleton object attributes, if any.  Derived classes need to provide
# a clear() function that empties the data list (in the base class)
# and clears the selection state (or pinned state, or whatever) in the
# objects.

class SelectionTrackerBase:
    def __init__(self):
        self.data = set()  # set of SkeletonSelectables
    def add(self, object):
        self.data.add(object)
    def clone(self):
        shakes = self.__class__()
        shakes.data = self.data.copy()
        return shakes
    def remove(self, obj):
        # TODO: Replacing 'discard' by 'remove' in the following line
        # causes the Direct_Pin_Nodes.UnPin test in
        # skeleton_select_test.py to fail.  The difference between
        # remove and discard is that discard doesn't complain if the
        # object isn't found.  So this may be a symptom of something
        # else going wrong, or maybe it's supposed to work this way
        # and is just sloppy programming and/or commenting.
        self.data.discard(obj)
    def get(self):
        return self.data                # Returns the host uniqueList.
    def size(self):
        return len(self.data)
    def copy(self, other):
        self.data = other.data.copy()
    def promote(self):
        return self
    def sheriff(self):
        return self
    
class SelectionTracker(SelectionTrackerBase):
    def clear(self):
        for e in self.data:
            e.local_deselect()
        self.data.clear()
    def write(self):
        for e in self.data:
            e.local_select()
    def clearskeleton(self):
        for e in self.data:
            e.local_deselect()
    def implied_select(self, othertracker):
        for e in othertracker.get():
            e.implied_select(othertracker, self)
    def selectDown(self, selectable, clist):
        selectable.selectDown(clist)
    def selectUp(self, selectable, plist):
        selectable.selectUp(plist)
    def deselectDown(self, selectable, clist):
        selectable.deselectDown(clist)
    def deselectUp(self, selectable, plist):
        selectable.deselectUp(plist)
    def redeputize(self, oldtracker, newtracker):
        pass
    def __repr__(self):
        return "SelectionTracker(%d)" % id(self)
        
            
#############################
        
# SelectionSet objects occupy the undo/redo stack of the various
# Selection objects.  Each SelectionSet contains a WeakKeyDictionary
# of SelectionTrackers, keyed by the Skeleton to which the tracker
# belongs.  The dictionary is weak so that the trackers go away when
# the Skeleton is destroyed.

# The base class doesn't contain any references to selection, so that
# the machinery can be used for pinned nodes and other such skeleton
# component attributes.  See SelectionSet (below) for the functions
# that a derived class must provide.

class SelectionSetBase:
    def __init__(self, skeletoncontext):
        self.skeletoncontext = skeletoncontext

        # Dictionary of Trackers, keyed by Skeletons
        self.selected = weakref.WeakKeyDictionary()

    def getTracker(self, skeleton):
        return self.selected[skeleton]

    def promoteDeputyTracker(self, deputyskeleton):
        olddeputytracker = self.selected[deputyskeleton]
        newtracker = olddeputytracker.promote()
        self.selected[deputyskeleton] = newtracker

    # Copy the selection state from the tracker into the actual
    # selected objects in the skeleton.
    def writeskeleton(self, skeleton):
        self.selected[skeleton].write()

    # Copy the selection state from all of the trackers into their
    # associated skeletons.
    def writestate(self):
        for tracker in self.selected.values():
            tracker.write()
    
    # Optimizing shortcut -- we know in advance that the correct
    # entries are empty SelectionTrackers corresponding to each key in
    # the selection's tracker dictionary.  Note that this actually
    # operates on the selectables.
    def clear(self):
        for tracker in self.selected.values():
            tracker.clear()                  

    def clearable(self):
        for tracker in self.selected.values():
            if tracker.size() > 0:
                return 1
        return 0

    # NB repr is not constructor, but shows selection state.
    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, id(self))
    

class SelectionSet(SelectionSetBase):

    # Do implied-selections for new skeletons.  Creates a tracker and
    # copies the selection state from the old skeleton to the new
    # skeleton.
    def implied_select(self, oldskel, newskel):
        tracker = newskel.newSelectionTracker(self)
        self.selected[newskel] = tracker
        if oldskel is not newskel:      # ie, not the initial skeleton
            oldtracker = self.selected[oldskel]
            tracker.implied_select(oldtracker)
    

    # clearskeletons() is called when undoing or redoing a selection
    # operation.  It clears the selection state of all objects in the
    # selection set.  It does not change the trackers, just the
    # objects to which they refer. 
    def clearskeletons(self):
        for tracker in self.selected.values(): 
            tracker.clearskeleton()

    def clone(self):
        # SelectionSets are cloned by SelectionBase.start(), which is
        # called at the beginning of an undoable selection operation.
        # (That's undo-able, not un-doable.)
        flippo = self.__class__(self.skeletoncontext)

        # deputy trackers can't be cloned directly, since they have to
        # refer to non-deputy trackers in the new SelectionSetBase.
        # This first pass only clones the non-deputies, because
        # DeputySelectionTracker.clone() is a no-op.
        for (skel,tracker) in self.selected.items():
            if not skel.destroyed():
                flippo.selected[skel] = tracker.clone()

        # The second pass looks for trackers that weren't cloned in
        # the first pass and creates deputies referring to the correct
        # non-deputies.
        for (skel, tracker) in flippo.selected.items():
            if not tracker:
                tracker = flippo.seniorTracker(skel)
                flippo.selected[skel] = \
                                deputytracker.DeputySelectionTracker(tracker)
        return flippo

    def seniorTracker(self, skel):
        # Among the set of trackers and deputy trackers in this
        # SelectionSet, return the most senior tracker that refers to
        # the given skeleton or to one of its deputies.  "Most senior"
        # means that the tracker is either the sheriff or the next to
        # be promoted to sheriff.
        sheriff = skel.sheriffSkeleton()
        try:
            return self.selected[sheriff]
        except KeyError:
            pass
        for deputy in sheriff.deputylist:
            try:
                return self.selected[deputy]
            except KeyError:
                pass
                                     
        
        

##++--++####++--++####++--++####++--++####++--++####++--++####++--++##


# The selection object for all the selections and the set of pinned
# nodes.  This is the master object, which lives at the
# SkeletonContext level, and holds the ringbuffer of SelectionSets.
# SelectionSets themselves have dictionaries of SelectionTrackers.

# SelectionBase doesn't contain any references to selection, so that
# its machinery can be used for pinning as well as selecting.  The
# derived classes must provide functions that actually do the
# selecting (or whatever).  Their __init__()s must call
# SelectionBase.__init__() and then push an appropriate SelectionSet
# object onto self.stack.

class SelectionBase:
    def __init__(self, skeletoncontext):
        self.timestamp = timestamp.TimeStamp()
        self.skeletoncontext = skeletoncontext
        self.rwLock = lock.RWLock()

        self.sbcallbacks = [
            # switchboard.requestCallback(('who changed', 'Skeleton'),
            #                             self.newSkeleton),
            switchboard.requestCallback(('whodoundo push',
                                         'Skeleton'),
                                        self.whoChanged0)
            ]

    def destroy(self):
        map(switchboard.removeCallback, self.sbcallbacks)
        self.stack.clear()      # break circular references
        
    # "Start" should be called prior to operations which are
    # meant to be undoable.
    def start(self):
        self.stack.push(self.stack.current().clone())

    def whoChanged0(self, context, oldskeleton, newskeleton):
        if self.skeletoncontext is context:
            # Loop over SelectionSets in the RingBuffer.
            for set in self.stack:
                set.implied_select(oldskeleton, newskeleton)
            self.stack.current().writeskeleton(newskeleton)

    # Response to mesh modification events [('who changed', 'Skeleton') signal]
    def newSkeleton(self, skelcontext):
        if skelcontext is self.skeletoncontext:
            self.timestamp.increment()  # enforces a redraw.
            self.signal()

    # This returns a SelectionSet object, which has the current state
    # for the entire stack.  To get the current skeleton's current
    # selection, use "retrieve", below.
    def currentSelection(self):
        return self.stack.current()

    # Selection retrieval function -- returns the list of currently
    # selected elements in the current skeleton of the current
    # context.  This is what the user almost certainly understands to
    # be "the selection".
    def retrieve(self):
        # self.stack.current().selected is a WeakKeyDict of
        # SelectionTrackers, keyed by Skeleton.
        return \
         self.stack.current().selected[self.skeletoncontext.getObject()].get()

    def retrieveFromSkeleton(self, skel):
        return self.stack.current().selected[skel].get()

    def trackerlist(self):
        set = self.stack.current()
        # Get trackers for all child and parent skeletons at the
        # current selection state.  The current skeleton's tracker is
        # element 0 of both lists.
        clist = [set.selected[x]
                 for x in self.skeletoncontext.getChildList()]
        plist = [set.selected[x]
                 for x in self.skeletoncontext.getParentList()]
        return clist, plist

    def promoteDeputyTrackers(self, deputyskeleton):
        for set in self.stack:
            set.promoteDeputyTracker(deputyskeleton)

    # Selection stack manipulation stuff.
    def undo(self):
        if self.undoable():
            self.stack.current().clearskeletons()
            self.stack.prev()
            self.stack.current().writestate()
            self.timestamp.increment()

    def redo(self):
        if self.redoable():
            self.stack.current().clearskeletons()
            self.stack.next()
            self.stack.current().writestate()
            self.timestamp.increment()
            
    def getTimeStamp(self):
        return self.timestamp

    
    def undoable(self):
        return not self.stack.atBottom()
    
    def redoable(self):
        return not self.stack.atTop()

    # Stack is clearable if there is any selection, even if it's invisible.
    def clearable(self):
        return self.stack.current().clearable()

    def invertable(self):
        return 1

    def clear(self):
        # Clear the current tracker set directly.  SelectionSet's
        # "clear" routine is a special exception that modifies the
        # selectables directly.
        self.stack.current().clear()
        self.timestamp.increment()

    # New size:  # of selected objects in the current skeleton.
    def size(self):
        skeleton = self.skeletoncontext.getObject()
        return self.stack.current().selected[skeleton].size()

    def begin_reading(self):
        ## debug.fmsg()
        self.rwLock.read_acquire()
    def end_reading(self):
        ## debug.fmsg()
        self.rwLock.read_release()

    def begin_writing(self):
        ## debug.fmsg()
        self.rwLock.write_acquire()
    def end_writing(self):
        ## debug.fmsg()
        self.rwLock.write_release()

    def pause_writing(self):
        ## debug.fmsg()
        self.rwLock.write_pause()
    def resume_writing(self):           # a useful skill for job applicants
        ## debug.fmsg()
        self.rwLock.write_resume()
        

    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, len(self.retrieve()))

# Base class for selections, but not for the set of pinned nodes.

class Selection(SelectionBase):
    def __init__(self, skeletoncontext):
        SelectionBase.__init__(self, skeletoncontext)
        # Ringbuffer of SelectionSet objects -- these contain
        # selections for undo/redo.
        self.stack = ringbuffer.RingBuffer(self.mode().stacksize)
        self.stack.push(SelectionSet(self.skeletoncontext))
        self.sbcallbacks.append(switchboard.requestCallback(
            ('skelselection ringbuffer resize', self.mode().name),
            self.setUndoBufferSizeCB))

    def setUndoBufferSizeCB(self, size):
        self.stack.resize(size)
        self.signal()

    def trackerlist(self):
        clist, plist = SelectionBase.trackerlist(self)
        # Make sure that the starting point isn't a DeputyTracker.
        while clist[0].sheriff() is not clist[0]:
            clist[0:0] = [plist[1]]
            del plist[0]
        return (clist, plist)
    
    # The Four Selection Operations.
    def select(self, objlist):
        (clist, plist) = self.trackerlist()
        skeleton = self.skeletoncontext.getObject()
        for o in objlist:
            if o.active(skeleton):
                o.select(clist, plist) 
        self.timestamp.increment()

    def deselect(self, objlist):
        (clist, plist) = self.trackerlist()
        skeleton = self.skeletoncontext.getObject()
        for o in objlist:
            if o.active(skeleton):
                o.deselect(clist, plist)
        self.timestamp.increment()
        
    def toggle(self, objlist):
        (clist, plist) = self.trackerlist()
        skeleton = self.skeletoncontext.getObject()
        for o in objlist:
            if o.active(skeleton):
                if o.selected:
                    o.deselect(clist, plist)
                else:
                    o.select(clist, plist)
        self.timestamp.increment()

    def invert(self):
        # Invert the selection status of all objects.  Loop over all
        # elements is unavoidable in this case, since very object must
        # be operated on.
        (clist, plist) = self.trackerlist()
        skeleton = self.skeletoncontext.getObject()
        for o in self.all_objects():
            if o.active(skeleton):
                if o.selected:
                    o.deselect(clist, plist)
                else:
                    o.select(clist, plist)
        self.timestamp.increment()

    # Selects objects from already selected ones
    def selectSelected(self, objlist):
        (clist, plist) = self.trackerlist()
        skeleton = self.skeletoncontext.getObject()        
        for o in self.all_objects():
            if o.active(skeleton) and o.selected and o not in objlist:
                o.deselect(clist, plist)
        self.timestamp.increment()

    def clear(self):
        (clist, plist) = self.trackerlist()
        skeleton = self.skeletoncontext.getObject()
        for o in self.all_objects():
            if o.active(skeleton) and o.selected:
                o.deselect(clist, plist)
        self.timestamp.increment()

    def signal(self):
        switchboard.notify(self.mode().changedselectionsignal)
        switchboard.notify("redraw")

# Subclasses of Selection must have a "mode" function that returns the
# corresponding SkeletonSelectionMode object, so that the generic
# selection manipulation routines can send the correct switchboard
# signals.  They are also distinguished by their method for getting
# all of the objects in the current skeleton, which is needed by
# "invert".  The "retrieveInOrder" function is used by certain
# Skeleton modification routines that need predictability in debug
# mode.  It ensures that the objects are returned in the same order
# each time.

class ElementSelection(Selection):
    def all_objects(self):
        return self.skeletoncontext.getObject().elements
    def mode(self):
        return skeletonselmodebase.getMode("Element")
    def retrieveInOrder(self):
        skel = self.skeletoncontext.getObject()
        nelem = len(self.retrieve())
        ordered = []
        count = 0
        for e in skel.element_iterator():
            if e.selected:
                ordered.append(e)
                count += 1
                if count == nelem:
                    return ordered
        return []

class SegmentSelection(Selection):
    def all_objects(self):
        return self.skeletoncontext.getObject().segments.values()
    def mode(self):
        return skeletonselmodebase.getMode("Segment")

class NodeSelection(Selection):
    def all_objects(self):
        return self.skeletoncontext.getObject().nodes
    def mode(self):
        return skeletonselmodebase.getMode("Node")
    def retrieveInOrder(self):
        skel = self.skeletoncontext.getObject()
        nnode = len(self.retrieve())
        ordered = []
        count = 0
        for n in skel.node_iterator():
            if n.selected:
                ordered.append(n)
                count += 1
                if count == nnode:
                    return ordered
        else:
            return []

