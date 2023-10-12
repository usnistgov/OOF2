# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

## A Segment-based snap node method instead of an Element-based
## method.  That is, it loops over Segments instead of Elements.  For
## both Nodes in a Segment, it finds the possible transition points on
## *all* Segments that contain either Node (picking the closest one if
## there are multiple transition points on a Segment).  Then it
## examines all possible pair-wise moves of the two nodes, as well as
## the single node moves.

## This method can do something that the previous algorithm couldn't,
## namely aligning a Segment that crosses a material boundary to the
## boundary in one step.  The old algorithm could only align such a
## segment in two steps, because the transition points on the
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

# Also, after nodes are moved, their neighboring nodes are moved to
# the head of the list of nodes to be considered next. This helps to
# ensure that two segments at different parts of a material boundary
# aren't snapped incompatibly:

#       |       |     |      |     
#       |       |     |      |     
# ------A-------B-----C------D-----   If AB is snapped to QR and
#       |       |     |      |        GH is snapped to ST, then there 
#       |       |     |      |        would be no way to snap BC or FG 
# ......Q.......R.....S......T.....   onto the material boundary RS.
# ......|.......|.....|......|.....
# ......|.......|.....|......|.....   But if BC is addressed after AB
# ......|.......|.....|......|.....   this situation is avoided, because
# ......|.......|.....|......|.....   C fill be snapped to S before G is
# ------E-------F-----G------H-----   moved.
# ......|.......|.....|......|.....


from ooflib.SWIG.common import config
from ooflib.SWIG.common import crandom 
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import progress
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common import utils
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
        

class SnapNodes(skeletonmodifier.SkeletonModifier):
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
            nodeiter = utils.ReorderableIterator(targetnodes)
            for i, node0 in enumerate(nodeiter):
                # TODO: Is this correct?  We continue looking at the
                # neighbors of node0 even after having moved it or one
                # of its other neighbors.  Should we end the node1
                # loop after one move?  Should we only choose a
                # bestchange after examining all node1s?
                
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
                                # If node1 was moved, put it at the
                                # head of the list of nodes to be
                                # moved.  This allows makes it less
                                # likely that two segments on the same
                                # pixel boundary will be snapped
                                # incompatibly.
                                ## TODO PYTHON3 LATER: Should the
                                ## *neighbors* of the moved nodes be
                                ## prioritized instead?
                                if node != node0:
                                    nodeiter.prioritize(node)

                prog.setFraction((i+1)/ntotal)
                prog.setMessage(f"Snapped {i+1}/{ntotal} nodes")
        finally:
            prog.finish()
        reporter.report(f"Snapped {len(usednodes)} node{'' if len(usednodes)==1 else 's'}.")
        return skel

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The SnapNodeTargets classes have a __call__ method that returns an
# iterable of SkeletonNodes.

## TODO PYTHON3 LATER: Does SnapNodes really need its own set of
## Target classes?  Different kinds of skeleton modifiers require
## different things from their Target classes, but the fundamental
## choices that the classes make are the same, as well as their
## appearance to the user.  All of the Target classes should have
## methods for supporting all of the modifiers, and none of those
## methods should be called __call__.  There might be some Targets
## that are inappropriate for some modifiers, so perhaps the
## modifiers' registrations could list the acceptable targets classes.

class SnapNodeTargets(registeredclass.RegisteredClass):
    registry = []
    tip="Which nodes will be snapped by SnapNodes"
    discussion="""<para>Ways of selecting &nodes; to be moved by <xref
    linkend="RegisteredClass-SnapNodes"/>.</para>"""

class SnapAll(SnapNodeTargets):
    def __call__(self, context):
        skel = context.getObject()
        return context.getObject().node_iterator(
            lambda n: n.active(skel) and n.movable())

registeredclass.Registration(
    'All Nodes',
    SnapNodeTargets,
    SnapAll,
    0,
    tip="Try to move all nodes to pixel boundaries.",
    discussion="""<para> In <xref
    linkend='RegisteredClass-SnapNodes'/>, move all &nodes; of
    the &skel; </para>""")

#=--=##=--=##=--=#

class SnapSelectedNodes(SnapNodeTargets):
    def __call__(self, context):
        skel = context.getObject()
        return context.nodeselection.retrieveInOrder(
            lambda n: n.active(skel) and n.movable())

registeredclass.Registration(
    'Selected Nodes',
    SnapNodeTargets,
    SnapSelectedNodes,
    ordering=1,
    tip="Try to move the selected nodes to pixel boundaries.",
    discussion="""<para> In <xref
    linkend='RegisteredClass-SnapNodes'/>, move the currently
    selected &nodes; of the &skel; </para>"""
)

#=--=##=--=##=--=#

class SnapHeterogeneousElements(SnapNodeTargets):
    def __init__(self, threshold):
        self.threshold = threshold
    def __call__(self, context):
        skel = context.getObject()
        elements = skel.element_iterator(
            lambda e: (e.active(skel) and e.homogeneity(skel.MS,False)
                       < self.threshold))
        nodes = utils.OrderedSet()
        for element in elements:
            nodes.update(n for n in element.nodes if n.movable())
        return nodes

registeredclass.Registration(
    'Heterogeneous Elements',
    SnapNodeTargets,
    SnapHeterogeneousElements,
    params = [parameter.FloatRangeParameter(
        'threshold', (0.0, 1.0, 0.01),
        value=0.9,
        tip='Move nodes in elements whose homogeneity is less than this.')],
    ordering=2,
    tip="Try to move nodes in heterogeneous elements to pixel boundaries.",
    discussion="""<para>In <xref
    linkend='RegisteredClass-SnapNodes'/>, move only those
    &nodes; that belong to <link
    linkend="Section-Concepts-Skeleton-Homogeneity">heterogeneous</link>
    &elems;.</para>"""
)

#=--=##=--=##=--=#

class SnapSelectedElements(SnapNodeTargets):
    def __call__(self, context):
        skel = context.getObject()
        els = context.elementselection.retrieveInOrder(lambda e: e.active(skel))
        nodes = utils.OrderedSet()
        for element in els:
            nodes.update(n for n in element.nodes if n.movable())
        return nodes

registeredclass.Registration(
    'Selected Elements',
    SnapNodeTargets,
    SnapSelectedElements,
    ordering=3,
    tip="Try to move the nodes in the selected elements to pixel boundaries.",
    discussion="""<para>In <xref
    linkend='RegisteredClass-SnapNodes'/>, move only those
    &nodes; that belong to currently selected &elems;.</para>"""
)

#=--=##=--=##=--=#

class SnapHeterogeneousSegments(SnapNodeTargets):
    def __init__(self, threshold):
        self.threshold = threshold
    def __call__(self, context):
        skel = context.getObject()
        segs = skel.segment_iterator(
            lambda s: (s.active(skel) and
                       s.homogeneity(skel.MS) < self.threshold))
        nodes = utils.OrderedSet()
        for segment in segs:
            nodes.update(n for n in segment.nodes() if n.movable())
        return nodes

registeredclass.Registration(
    'Heterogeneous Segments',
    SnapNodeTargets,
    SnapHeterogeneousSegments,
    ordering=4,
    params=[
        parameter.FloatRangeParameter(
            'threshold', (0.0, 1.0, 0.01),
            value=0.9,
            tip='Move nodes in elements whose homogeneity is less than this.')],
    tip="Try to move nodes on heterogeneous segments to pixel boundaries.",
    discussion="""<para>In <xref
    linkend='RegisteredClass-SnapNodes'/>, move only those
    &nodes; that belong to heterogeneous &sgmts;.</para>"""
)

#=--=##=--=##=--=#

class SnapSelectedSegments(SnapNodeTargets):
    def __call__(self, context):
        skel = context.getObject()
        segs = context.segmentselection.retrieveInOrder(
            lambda s: s.active(skel))
        nodes = utils.OrderedSet()
        for segment in segs:
            nodes.update(n for n in segment.nodes() if n.movable)
        return nodes

registeredclass.Registration(
    'Selected Segments',
    SnapNodeTargets,
    SnapSelectedSegments,
    ordering=5,
    tip="Try to move nodes on selected segments to pixel boundaries.",
    discussion="""<para>In <xref
    linkend='RegisteredClass-SnapNodes'/>, move only those
    &nodes; that belong to selected &sgmts;.</para>"""
)
    
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

registeredclass.Registration(
    'Snap Nodes',
    skeletonmodifier.SkeletonModifier,
    SnapNodes,
    ordering=1.1,
    params=[parameter.RegisteredParameter('targets', SnapNodeTargets,
                                           tip="Which segments to snap."),
            parameter.RegisteredParameter('criterion',
                                          skeletonmodifier.SkelModCriterion,
                                          tip='Acceptance criterion')
            ],
    tip="Move nodes directly to pixel boundaries.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/snapnodes.xml')
)


