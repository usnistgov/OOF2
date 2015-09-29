# -*- python -*-
# $RCSfile: deputy.py,v $
# $Revision: 1.42 $
# $Author: langer $
# $Date: 2015/07/14 21:39:36 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# A DeputySkeleton is a lightweight way of representing a Skeleton
# which differs from a real Skeleton only in the positions of some of
# its nodes.  When the DeputySkeleton is being used as a Skeleton, it
# should be activated (with DeputySkeleton.activate()).  Only one
# DeputySkeleton of a given Skeleton can be active at one time.  When
# the DeputySkeleton is inactive, it's a mistake to move any of its
# nodes, and when it's active, it's a mistake to move any of the
# reference Skeleton's nodes.

# When a Deputy's Skeleton is about to be overwritten in the
# SkeletonContext's Ringbuffer, the Deputy must be promoted.  The
# various DeputyTrackers associated with the promoted Deputy must also
# be promoted.

# Note that, when this overwrite event occurs, the sheriff skeleton is
# marked as destroyed, but retains lists of nodes and elements, and
# various other things that deputies need to function.  The memory is
# not really released until the last deputy is destroyed, at which
# point the sheriff skeleton is also destroyed.  Deputies never
# actually really become sheriffs.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import timestamp
from ooflib.SWIG.engine import cskeleton
from ooflib.common import debug
from ooflib.common import parallel_enable
from ooflib.engine import deputytracker
from ooflib.engine import skeletonnode
if config.dimension() == 2:
    import ooflib.engine.skeleton as skeleton
elif config.dimension() == 3:
    import ooflib.engine.skeleton3d as skeleton

import sys

class DeputySkeleton(skeleton.SkeletonBase):
    def __init__(self, skel, id = None):       # skel may be a deputy
        skeleton.SkeletonBase.__init__(self)
        self.skeleton = skel.sheriffSkeleton()
        self.skeleton.addDeputy(self)
        self._illegal = skel._illegal
        # When the DeputySkeleton is active, the positions of its nodes
        # are stored in the actual nodes, and the positions of the
        # reference Skeleton's nodes are stored in the nodePositions
        # dictionary.  When it's inactive, it's the other way around.
        self.nodePositions = skel.getMovedNodes()
        self.active = 0
        self.timestamp = timestamp.TimeStamp()
        self.meshes = []
        self._destroyed = 0

        # parallel stuff -- temporary until the Skeleton gets proper
        # parallel display method
        if parallel_enable.enabled():
            self.all_skeletons = skel.all_skeletons


    def getIndexBase(self):
        return (self.skeleton.node_index,
                self.skeleton.segment_index,
                self.skeleton.element_index)
        
    def isDeputy(self):
        return 1
    
    def deputyCopy(self):
        return DeputySkeleton(self)

    def getMovedNodes(self):
        nodedict = {}
        if self.active:                 # copy positions from Skeleton
            for node in self.nodePositions:
                nodedict[node] = node.position()
        else:                           # copy positions from self
            nodedict.update(self.nodePositions)
        return nodedict

    def nodePosition(self, node):
        # Get the position of the node in this skeleton even if a
        # deputy is active.
        if self.active:
            return node.position()
        try:
            return self.nodePositions[node]
        except KeyError:
            return self.skeleton.nodePosition(node)

    def originalPosition(self, node):
        try:
            return self.nodePositions[node]
        except KeyError:
            return node.position()

    def sheriffSkeleton(self):
        return self.skeleton

    def activate(self):
        if not self.active:
            self.active = 1
            self.skeleton.deputize(self)
            self.swapPositions()

    def deactivate(self):
        # called when the master Skeleton or another Deputy is activated
        if self.active:
            self.active = 0
            self.swapPositions()
    def swapPositions(self):
        for node, position in self.nodePositions.items():
            self.nodePositions[node] = node.position()
            node.unconstrainedMoveTo(position)
        self.skeleton.needsHash()
        
    # Any attributes not defined here are obtained from the underlying
    # skeleton.  This is *not* a derived class, though, because the
    # point is that objects of this class require very little
    # storage.
    def __getattr__(self, attr):
        return getattr(self.skeleton, attr)

    def disconnect(self):
        pass

    def moveNodeTo(self, node, position):
        if node not in self.nodePositions:
            # Storing old position
            self.nodePositions[node] = node.position()
        node.moveTo(position)
        for partner in node.getPartners():
            if partner not in self.nodePositions:
                self.nodePositions[partner] = partner.position()
            partner.moveTo(position)

    def moveNodeBy(self, node, delta):
        if node not in self.nodePositions:
            self.nodePositions[node] = node.position()
        node.moveBy(delta)
        for partner in node.getPartners():
            if partner not in self.nodePositions:
                self.nodePositions[partner] = partner.position()
            partner.moveBy(delta)

    def moveNodeBack(self, node):
        node.moveBack()
        if node.position() == self.nodePositions[node]:
            del self.nodePositions[node]
        for partner in node.getPartners():
            partner.moveBack()
            if partner.position() == self.nodePositions[partner]:
                del self.nodePositions[partner]

    def destroy(self, context):
        skeleton.SkeletonBase.destroy(self)
        self.skeleton.removeDeputy(self, context)
        del self.skeleton
        del self.nodePositions
        meshes = self.meshes[:]
        for mesh in meshes:
            mesh.destroy()
        self.meshes = []
        self._destroyed = 1

    def destroyed(self):
        return self._destroyed

    def getTimeStamp(self):
        return max(self.timestamp, self.skeleton.MS.getTimeStamp())

    def mapBoundary(self, bdy, skeleton, **kwargs):
        pass

    def newSelectionTracker(self, selectionset):
        return deputytracker.DeputySelectionTracker(
            selectionset.seniorTracker(self.skeleton))

    def newGroupTracker(self, groupset):
        return deputytracker.DeputyGroupTracker(
            groupset.getTracker(self.skeleton))

    def newPinnedNodeTracker(self):
        return DeputyPinnedNodeTracker(self)

    def promoteTrackers(self, context):
        context.promoteDeputyTrackers(self)

    def __repr__(self):
        return "DeputySkeleton(%d, %d)" % (id(self), id(self.skeleton))

# It will only take care of node move changes.
class DeputyProvisionalChanges:
    def __init__(self):
        self.movednodes = []  # list of MoveNode objects
        self.elements = set()    # Elements involved.
        self.cachedDeltaE = None  # Energy difference
        self.cachedDeltaEBound = None  # Energy difference
        self.cachedIllegal = None  # Illegality
        self.cachedNewHomogeneity = {}  # Homogeneity objs, Keyed by element

        # For parallel mode
        self.parallelHomog0 = []
        self.parallelHomog1 = []
        self.parallelShape0 = []
        self.parallelShape1 = []
        
    class MoveNode:                     # nested class definition
        def __init__(self, node=None, position=None):
            self.node = node
            self.position = position

    def moveNode(self, node, position, deputy):
        self.movednodes.append(
            self.MoveNode(node=node, position=position))
        for el in node.neighborElements():
            self.elements.add(el)

    def elBefore(self):
        return self.elements
    
    def elAfter(self):
        return self.elements

    def makeNodeMove(self, deputy):
        for mvnode in self.movednodes:
            deputy.moveNodeTo(mvnode.node, mvnode.position)
#         if config.dimension()==3:
#             for element in self.elements:
#                 element.updateVtkCellPoints()

    def moveNodeBack(self, deputy):
        for mvnode in self.movednodes:
            deputy.moveNodeBack(mvnode.node)
#         if config.dimension()==3:
#             for element in mvnode.node.neighborElements():
#                 element.updateVtkCellPoints()
        

    def illegal(self, deputy):
        # Will this change produce any illegal elements?
        if self.cachedIllegal is None:
            self.makeNodeMove(deputy)
            for element in self.elements:
                if element.illegal():
                    self.moveNodeBack(deputy)
                    self.cachedIllegal = 1
                    break
            else:
                self.moveNodeBack(deputy)
                self.cachedIllegal = 0
        return self.cachedIllegal

    def deltaE(self, deputy, alpha):
        # Return the change in energy per element if this move were to
        # be accepted.
        if self.cachedDeltaE is None:
            nelements = len(self.elements)
            # Energy before the change
            oldE = 0.0
            for el in self.elements:
                oldE += el.energyTotal(deputy, alpha)
            # Move nodes accordingly to simulate the change
            self.makeNodeMove(deputy)
            # Energy after the change
            newE = 0.0
            for el in self.elements:
                key = el.getPositionHash()
                try:
                    homogeneity = deputy.cachedHomogeneities[key]
                    el.setHomogeneityData(homogeneity)
                except KeyError:
                    el.findHomogeneityAndDominantPixel(deputy.MS);
                    homogeneity = el.getHomogeneityData()
                    deputy.cachedHomogeneities[key] = homogeneity
                newE += el.energyTotal(deputy, alpha)
                self.cachedNewHomogeneity[el] = homogeneity
            # Move node back
            self.moveNodeBack(deputy)

            # In parallel-mode, deltaE's from other processes
            # have to be considered too.
            if parallel_enable.enabled():
                for h0,h1, s0,s1 in zip(self.parallelHomog0,
                                        self.parallelHomog1,
                                        self.parallelShape0,
                                        self.parallelShape1):
                    oldE += (alpha*h0+(1.-alpha)*s0)
                    newE += (alpha*h1+(1.-alpha)*s1)
                nelements += len(self.parallelHomog0)
                
            # Averaged energy differnce due to the change
            self.cachedDeltaE = (newE - oldE)/nelements
            
        return self.cachedDeltaE

    def deltaEBound(self, deputy, alpha):
        # Return the maximum possible deltaE -- assuming all elements
        # become homogenous after the change
        if self.cachedDeltaEBound is None:
            # Energy before the change
            oldE = 0.0
            for element in self.elBefore():
                oldE += element.energyTotal(deputy, alpha)
            oldE /= len(self.elBefore())
            # Move nodes accordingly to simulate the change
            self.makeNodeMove(deputy)
            # Energy after the change
            newE = 0.0
            for element in self.elAfter():
                newE += (1.-alpha)*element.energyShape()
            newE /= len(self.elAfter())
            # Move node back
            self.moveNodeBack(deputy)
            # Energy differnce due to the change
            self.cachedDeltaEBound = newE - oldE        
        return self.cachedDeltaEBound

    def accept(self, deputy):
        for mvnode in self.movednodes:
            deputy.moveNodeTo(mvnode.node, mvnode.position)
        for el, cached in self.cachedNewHomogeneity.items():
            el.setHomogeneityData(cached)

    # for parallel-mode
    def augmentData(self, homog0, homog1, shape0, shape1):
        self.parallelHomog0 = homog0
        self.parallelHomog1 = homog1
        self.parallelShape0 = shape0
        self.parallelShape1 = shape1

    def removeAddedNodes(self, skeleton):
        # should be defined in a common base class for
        # DeputyProvisionalChanges and ProvisionalChanges
        pass

class DeputyPinnedNodeTracker(skeletonnode.PinnedNodeTracker):
    # Unlike the other deputy trackers, the DeputyPinnedNodeTracker
    # has its own data and doesn't refer to another tracker.  That's
    # because the same node can be pinned in a skeleton and unpinned
    # in a deputy skeleton.  DeputyPinnedNodeTrackers and
    # PinnedNodeTrackers differ only in how the pinned state is
    # propagated from skeleton to skeleton.

    def pinDown(self, node, clist, where):
        node.pinDown(clist, where)
        
    def pinUp(self, node, plist, where):
        node.pinUp(plist, where)

    def unpinDown(self, node, clist, where):
        node.unpinDown(clist, where)

    def unpinUp(self, node, plist, where):
        node.unpinUp(plist, where)

    def implied_pin(self, oldtracker):
        for n in oldtracker.get():
            there = oldtracker.nodePosition(n)
            here = self.nodePosition(n)
            if here == there:
                self.add(n)

    def __repr__(self):
        return "DeputyPinnedNodeTracker"
