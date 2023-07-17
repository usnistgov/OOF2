# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

## A Segment-based snap node method instead of an Element-based
## method.  That is, loop over Segments instead of Elements.  For both
## Nodes in a Segment, find the possible transition points on *all*
## Segments that contain each Node (picking the closest one if there
## are multiple transition points on a Segment).  Then examine all
## possible pair-wise moves of the two nodes, as well as the single
## node moves.

## The proposed method can do something that the current algorithm
## can't, namely aligning a Segment that crosses a material boundary
## to the boundary in one step.  The current algorithm can only align
## such a segment in two steps, because the transition points on the
## neighboring segments are in different elements.  If the
## intermediate configuration has a high energy, the alignment won't
## occur.

#       |       |
#       |       |                             The moves A->X and C->Y
# ------A-------D--------                     would align the element
#       |\      |                             boundary AC with the material
#       | \     |                             boundary XY if the two moves
# ......X..\....Y......  material boundary    can be made simultaneously
# ......|...\...|......                       even though the transition points
# ......|....\..|......                       X and Y are not in the same
# ......|.....\.|......                       element.
# ......|......\|......
# ------B-------C------  element boundary
# ......|.......|......



from ooflib.SWIG.common import config
from ooflib.SWIG.common import crandom 
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import progress
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import reporter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import deputy
from ooflib.engine import skeletonmodifier

# Since each node will be looked at multiple times (when looping over
# segments), keep a cache of the transition points on the adjacent
# segments, but make sure to mark transition points as out of date
# when one node on a segment is moved.

class NearestPoints:
    def __init__(self, node, skeleton):
        self.node = node
        self.skeleton = skeleton
        # transitions maps the nodes at the far end of a segments to
        # the transition point along the segment.  A value of None
        # means there is no transition point.  A value of "unknown"
        # means it hasn't been calculated.
        self._transitions = {}
        for other in node.neighborNodes(skeleton):
            self._transitions[other] = "unknown"

    def transition(self, othernode):
        if self._transitions[othernode] == "unknown":
            # TODO: getSegmentSections() won't return any section
            # smaller than minlength.  Should it be small and
            # positive?
            minlength = 0.0
            sections = self.skeleton.MS.getSegmentSections(
                self.node.position(), othernode.position(), minlength)
            if len(sections) == 1:
                self._transitions[othernode] = None
            else:
                self._transitions[othernode] = sections[0].physicalPt1()
        return self._transitions[othernode]

    # Get all possible points that this node can move to.
    def transitions(self):
        tps = []
        for other in self._transitions.keys():
            tp = self.transition(other, self.skeleton)
            if tp is not None:
                tps.append(tp)
        return tps

    def invalidate(self, othernode):
        self._transitions[othernode] = "unknown"

    def invalidateAll(self, tpcache):
        for other in self._transitions.keys():
            self._transitions[other] = "unknown"
            try:
                tpcache[other].invalidate[self.node]
            except:
                pass

    # Iterating over a NearestPoints object returns the coordinates of
    # the nearest transition points.
    def __iter__(self):
        for other in self._transitions.keys():
            tp = self.transition(other)
            if tp is not None:
                yield tp

    def __repr__(self):
        return f"NearestPoints({self._transitions})"
        
            

class SnapNodes2(skeletonmodifier.SkeletonModifier):
    def __init__(self, targets, criterion):
        self.targets = targets
        self.criterion = criterion

    def apply(self, oldskeleton, context):
        prog = progress.getProgress("SnapNodes", progress.DEFINITE)
        skel = oldskeleton.deputyCopy()
        skel.activate()
        micro = skel.MS

        targetnodes = list(self.targets(context))
        crandom.shuffle(targetnodes)
        ntotal = len(targetnodes)

        # initialize the transition point cache
        tpcache = {}
        for node in targetnodes:
            tpcache[node] = NearestPoints(node, skel)

        # Keep track of which segments have been handled already
        ## TODO PYTHON3: Only move nodes once?
        usedsegments = set()
        usednodes = set()

        try:
            for i, node0 in enumerate(targetnodes):
                for node1 in node0.neighborNodes(skel):
                    segment = skel.findSegment(node0, node1)
                    if segment not in usedsegments:
                        usedsegments.add(segment) # don't examine this seg again
                        changes = []
                        # Create provisional Skeleton changes for all
                        # combinations of node0 moves and node1 moves.
                        for move0 in tpcache[node0]:
                            # Move node0 but not node1
                            change = deputy.DeputyProvisionalChanges(skel)
                            change.moveNode(node0, move0, skel)
                            changes.append(change)
                            for move1 in tpcache.get(node1, []):
                                # Move node0 and node1
                                change = deputy.DeputyProvisionalChanges(skel)
                                change.moveNode(node0, move0, skel)
                                change.moveNode(node1, move1, skel)
                                changes.append(change)
                        for move1 in tpcache.get(node1, []):
                            # Move node1 but not node0
                            change = deputy.DeputyProvisionalChanges(skel)
                            change.moveNode(node1, move1, skel)
                            changes.append(change)

                        bestchange = self.criterion(changes, skel)
                        if bestchange is not None:
                            bestchange.accept()
                            # If a node was moved, its cached transition
                            # points may need to be recomputed.
                            movednodes = [n.node for n in bestchange.movednodes]
                            for node in movednodes:
                                usednodes.add(node)
                                tpcache[node].invalidateAll(tpcache)

                prog.setFraction((i+1)/ntotal)
                prog.setMessage(f"Snapped {i+1}/{ntotal} nodes")
        finally:
            prog.finish()
        reporter.report(f"Snapped {len(usednodes)} node{'' if len(usednodes)==1 else 's'}.")
        return skel

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The SnapNodeTargets2 classes have a __call__ method that returns an
# iterable of SkeletonNodes.

class SnapNodeTargets2(registeredclass.RegisteredClass):
    registry = []

class SnapAll2(SnapNodeTargets2):
    def __call__(self, context):
        skel = context.getObject()
        return context.getObject().node_iterator(lambda n: n.active(skel))

registeredclass.Registration(
    'All Nodes',
    SnapNodeTargets2,
    SnapAll2,
    0,
    tip="Snap all nodes.",
    discussion="""<para>
    All &nodes; of the &skel; are <varname>targets</varname> of <xref
    linkend='RegisteredClass-SnapNodes'/>.
    </para>""")

class SnapSelectedNodes2(SnapNodeTargets2):
    def __call__(self, context):
        skel = context.getObject()
        return context.nodeselection.retrieveInOrder(lambda n: n.active(skel))

registeredclass.Registration(
    'Selected Nodes',
    SnapNodeTargets2,
    SnapSelectedNodes2,
    1,
    tip="Snap selected nodes.")

class SnapHeterogeneousElements2(SnapNodeTargets2):
    def __init__(self, threshold):
        self.threshold = threshold
    def __call__(self, context):
        skel = context.getObject()
        elements = skel.element_iterator(
            lambda e: (e.active(skel) and e.homogeneity(skel.MS,False)
                       < self.threshold))
        nodes = set()
        for element in elements:
            nodes.update(element.nodes())
        return nodes

## TODO: Finish these.
class SnapHeterogeneousSegments2(SnapNodeTargets2):
    pass

class SnapSelectedElements2(SnapNodeTargets2):
    pass

class SnapSelectedSegments2(SnapNodeTargets2):
    pass
    
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

registeredclass.Registration(
    'Snap Nodes 2',
    skeletonmodifier.SkeletonModifier,
    SnapNodes2,
    ordering=1.1,
    params=[parameter.RegisteredParameter('targets', SnapNodeTargets2,
                                           tip="Which segments to snap."),
            parameter.RegisteredParameter('criterion',
                                          skeletonmodifier.SkelModCriterion,
                                          tip='Acceptance criterion')
            ],
    tip="Move nodes directly to pixel boundaries.")


