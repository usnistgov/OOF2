# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

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
from ooflib.engine import skeletonnode

import time
from functools import reduce

##################

## TODO: Try a Segment-based method instead of an Element-based
## method.  That is, loop over Segments instead of Elements.  For both
## Nodes in a Segment, find the possible transition points on *all*
## Segments that contain each Node (picking the closest one if there
## are multiple transition points on a Segment).  Then examine all
## possible pair-wise moves of the two nodes, as well as the single
## node moves.

## The proposed method can do something that the current algorithm
## can't, namely aligning a Segment that crosses a material boundary
## to the boundary in one step.  The current algorithm can only align
## such as segment in two steps, because the transition points are in
## different elements.  If the intermediate configuration has a high
## energy, the alignment won't occur.

## TODO: Find out what happened to the code that snapped the neighbors
## of a snapped node before going on to other nodes.  Is it really
## gone?  Should it be recovered?

##################


# SnapNodeTargets determine which elements will have their nodes
# moved (or attempted to be moved).  A SnapNodeTargets must have a
# __call__ method that takes an element and a skeleton and returns 1
# or 0, depending on whether the element should move its nodes or not.
# They are slightly different than SkelModTargets, since SnapNode doesn't
# need properCopy(), instead it calls deputyCopy().

class SnapNodeTargets(registeredclass.RegisteredClass):
    registry = []
    def cleanSelection(self):
        pass

    tip = "Which nodes to snap?"
    discussion = """<para>
    Values for the <varname>targets</varname> parameter of the <xref
    linkend='RegisteredClass-SnapNodes'/> &skel; <link
    linkend='RegisteredClass-SkeletonModifier'>modifier</link>.
    <varname>targets</varname> determines which &node; moves should be
    attempted.
    </para>"""

class SnapAll(SnapNodeTargets):
    def __call__(self, context):
        return context.getObject().element_iterator()

registeredclass.Registration(
    'All Nodes',
    SnapNodeTargets,
    SnapAll,
    0,
    tip="Snap all nodes.",
    discussion="""<para>
    All &nodes; of the &skel; are <varname>targets</varname> of <xref
    linkend='RegisteredClass-SnapNodes'/>.
    </para>""")

class SnapSelected(SnapNodeTargets):
    def __call__(self, context):
        return context.elementselection.retrieveInOrder()

registeredclass.Registration(
    'Selected Elements',
    SnapNodeTargets,
    SnapSelected,
    1,
    tip="Snap selected elements.",
    discussion="""<para>
    All &nodes; of the currently selected &elems; are
    <varname>targets</varname> for <xref
    linkend='RegisteredClass-SnapNodes'/>.
    </para>""")

class SnapHeterogenous(SnapNodeTargets):
    def __init__(self, threshold):
        self.threshold = threshold
        
    def __call__(self, context):
        skel = context.getObject()
        elements = []
        for elem in skel.element_iterator():
            if elem.homogeneity(skel.MS, False) < self.threshold:
                elements.append(elem)
        return elements

registeredclass.Registration(
    'Heterogeneous Elements',
    SnapNodeTargets,
    SnapHeterogenous, 2,
    params=[
    parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.01), value=0.9,
          tip='Snap elements with homogeneity below the specified threshold.')],
    tip="Snap heterogeneous elements.",
    discussion="""<para>
    All &nodes; of the <link
    linkend='Section-Concepts-Skeleton-Homogeneity'>inhomogeneous</link>
    &elems; are <varname>targets</varname> for <xref
    linkend='RegisteredClass-SnapNodes'/>.  All &elems; whose
    homogeneity is less than the given <varname>threshold</varname>
    will be addressed.
    </para>""")

####################################

# The SnapNode machinery is element-based, but it's useful to be able
# to snap selected nodes.  This target does this by hacking around the
# problem -- it finds all the elements associated with the set of
# nodes, and pins all the nodes which are associated with those
# elements but which were not part of the initial set.  It then
# returns the element list to the SnapNode machinery, which is tricked
# into doing What We Want.  Afterwards, the SnapNodes.apply calls
# cleanSelection, where this object unpins all the nodes that it
# pinned.

class SnapSelectedNodes(SnapNodeTargets):
    def __init__(self):
        self.molested_nodes = []
    def __call__(self, context):
        elements = set()
        all_nodes = {} # Keyed by nodes -- 0 means move, 1 means pin. 
        skel = context.getObject()
        nodes = context.nodeselection.retrieveInOrder()
        for n in nodes:
            all_nodes[n]=0 # Do not molest the nodes we like.
            
        for n in nodes:
            for e in n.aperiodicNeighborElements():
                if e not in elements:
                    elements.add(e)
                    for x in e.nodes:
                        if x not in all_nodes:
                            all_nodes[x]=1 # Pin all extra nodes.
                            
        for (node, p) in all_nodes.items():
            if p==1:
                if not node.pinned():
                    node.setPinned(1)
                    self.molested_nodes.append(node)
            
        return elements
            

    # Use this hook to unpin the nodes we changed.
    def cleanSelection(self):
        for n in self.molested_nodes:
            n.setPinned(0)
        self.molested_nodes=[]
        

registeredclass.Registration(
    'Selected Nodes',
    SnapNodeTargets,
    SnapSelectedNodes, 3,
    tip="Snap selected nodes.",
    discussion="""<para>
    Use only the currently selected &nodes; as the
    <varname>targets</varname> for <xref
    linkend='RegisteredClass-SnapNodes'/>.
    </para>""")

######################################################################

# The SnapNodes SkeletonModifier moves element corners in a more or
# less deterministic fashion, to the points along the element's edges
# at which the pixel category changes ("transition points").  For each
# element, if the element meets a target criterion embodied in the given
# SnapNodeTargets object, SnapNodes first finds the transition points,
# and schedules the nodes to be moved by creating an appropriate
# NodeSnapper object.  Different kinds of NodeSnappers apply to different
# element and transition point topologies.  After all the NodeSnapper
# objects have been created, SnapNodes applies them to the skeleton in
# a random order, but giving precedence to ones with a lower
# "priority".  (Different kinds of NodeSnappers have different
# priorities-- edge motions are performed before single node motions.)
# Moves are accepted only if they lower the skeleton's total shape and
# homogeneity energy.

## TODO: This sometimes does strange things, leaving a node at a new
## position that is *not* on a pixel boundary.  Is that a result of
## applying a NodeSnapper to a Skeleton that has already been modified
## by previous NodeSnappers, so that the Skeleton is not the same as
## it was when the snapper was created?  For example, create an 8x8
## quad Skeleton on small.ppm, set the random number seed to 17, and
## snap all nodes, with average energy alpha=1.0.

class SnapNodes(skeletonmodifier.SkeletonModifier):
    def __init__(self, targets, criterion):
        self.targets = targets  # SnapNodeTargets
        self.criterion = criterion  # Acceptance criterion

    def apply(self, oldskeleton, context):
        prog = progress.getProgress("SnapNodes", progress.DEFINITE)
        prog.setMessage("examining elements...")
        skel = oldskeleton.deputyCopy()
        skel.activate()

        # Examine elements and create NodeSnapper objects
        movedict = {}                   # dict of all moves, keyed by element
        movelists = {}         # dict of lists of all moves, keyed by priority
        elements = self.targets(context)

        # Big try-finally block to ensure that
        # self.targets.cleanSelection() gets called if something goes
        # wrong.
        try:
            stored_tps = {}  # keyed by node pair
            nel = len(elements)
            for i, element in enumerate(elements):
                if element.homogeneity(skel.MS, False) == 1.0:
                    continue  # no need to even look at it!
                if element.active(oldskeleton):
                    #nnodes = element.nnodes()
                    # Common segments will be looked at only once.
                    # With a small Skeleton, this takes more time due to
                    # additional book-keeping stuff.
                    transitionpts = []
                    for n, nodes in enumerate(element.segment_node_iterator()):
                        key = skeletonnode.canonical_order(nodes[0], nodes[1])
                        try:
                            transitionpts.append(stored_tps[key])
                        except KeyError:
                            tp = element.transitionPoint(skel, n)
                            stored_tps[key] = tp
                            transitionpts.append(tp)
                    nodemotion = getNodeSnapper(element, transitionpts)
                    if nodemotion is not None:
                        movedict[element] = nodemotion
                        try:
                            movelists[nodemotion.priority].append(nodemotion)
                        except KeyError:
                            movelists[nodemotion.priority] = [nodemotion]
                if prog.stopped() :
                    return None
                prog.setFraction((i+1)/nel)
                prog.setMessage("examined %d/%d elements" % (i+1, nel))
            # end loop over elements
            
            # Perform node motions in random order within their
            # priority classes
            priorities = sorted(list(movelists.keys()))
            # A set to keep track of moved nodes & use them to assist
            # movers that are associated with these nodes.
            movednodes = set()
            for p in priorities:
                movelist = movelists[p]
                crandom.shuffle(movelist)
                nmv = len(movelist)
                for i in range(nmv):
                    move = movelist[i]
                    move.perform(skel, self.criterion, movedict, movednodes)
                    if prog.stopped():
                        return None
                    prog.setFraction((i+1)/nmv)
                    prog.setMessage("Type %d: %d/%d" % (p, i+1, nmv))
            nmoved = len(movednodes)
        finally:  
            self.targets.cleanSelection()
            prog.finish()

        # Only need to clean up the skeleton if we're going to return it.
        skel.cleanUp()
        reporter.report("Snapped %d node%s." % (nmoved, "s"*(nmoved != 1)))
        return skel

###################################

registeredclass.Registration(
    'Snap Nodes',
    skeletonmodifier.SkeletonModifier,
    SnapNodes,
    ordering = 1,
    params=[parameter.RegisteredParameter('targets', SnapNodeTargets,
                                          tip='Which elements to snap.'),
            parameter.RegisteredParameter('criterion',
                                          skeletonmodifier.SkelModCriterion,
                                          tip='Acceptance criterion.')
    ],
    tip="Move nodes directly to pixel boundaries.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/snapnodes.xml'))


####################################

# To associate the proper NodeSnapper class with a element, we compute a
# node motion signature and compare it with the signatures that each
# NodeSnapper can handle.  (Node motion signatures are similar to
# refinement signatures, but simpler.)  The signature is a tuple with
# an entry for each edge of the element.  The entry is 1 if there's a
# transition point (possible target for node motion) on the edge, and
# 0 if there's not.  To make the signature independent of the choice
# of edge number, the signature tuple is rotated so that it's
# maximized when read as a binary number.

def findSignature(transitionpoints):
    # Returns the rotation and signature.
    n = len(transitionpoints)
    sig = [pt is not None for pt in transitionpoints] # 0's and 1's
    # put in canonical order
    max = -1
    rotation = None
    for i in range(n):
        key = reduce(lambda x,y: 2*x+y, sig[i:]+sig[:i], 0)
        if key > max:
            max = key
            rotation = i
    return rotation, tuple(sig[rotation:] + sig[:rotation])

# Dictionary of NodeSnappers, keyed by signature
moverRegistry = {}              

def registerNodeSnapper(moverclass, *signatures):
    for sig in signatures:
        moverRegistry[sig] = moverclass

def getNodeSnapper(element, transitionpoints):
    signature_info = findSignature(transitionpoints)
    sig = signature_info[1]
    try:
        moverclass = moverRegistry[sig] # NodeSnapper class
    except KeyError:
        return
    return moverclass(element, signature_info, transitionpoints) # NodeSnapper object

    ###########################

class NodeSnapper:
    # NodeSnappers must have an apply() method which actually performs
    # the move if it's acceptable.  If it performs the move, it should
    # call NodeSnapper.perform() for the movers of the adjacent
    # elements.  It should return the *total* number of nodes moved.
    def __init__(self, element, signature_info, transitionpoints):
        self.element = element
        self.rotation = signature_info[0] # rotation of nodes wrt signature
        self.transitionpoints = transitionpoints

    def perform(self, skel, criterion, movedict, movednodes):
        self.apply(skel, criterion, movedict, movednodes)

    def rotate(self, vec):
        return vec[self.rotation:] + vec[:self.rotation]

    def make_a_move(self, skel, criterion, movednodes, movelist):
        # Moving!
        changes = []
        for ml in movelist:
            changes.append(deputy.DeputyProvisionalChanges())
            for (node, destination) in ml:
                changes[-1].moveNode(node, destination, skel) 
        # Pick the best change, and move the nodes.
        bestchange = criterion(changes, skel)
        if bestchange is not None:
            bestchange.accept(skel)
            # Make sure that these nodes won't be moved again during
            # this application of SnapNodes.
            for mn in bestchange.movednodes:
                movednodes.add(mn.node)

    def apply(self, skel, criterion, movedict, movednodes):
        movelist = [nodemove for nodemove in self.get_movelist(movednodes)
                    if _legalMove(nodemove)]
        self.make_a_move(skel, criterion, movednodes, movelist)

def _legalMove(nodemove):
    for node, destination in nodemove:
        if not node.canMoveTo(destination):
            return False
    return True


class QuadEdgeSnapper(NodeSnapper):
    priority = 1

    #  3-----T1---2
    #  |      ....|  T0 and T1 are the transition points.
    #  |      ....|  Possible sets of moves are (3->T1, 0->T0)
    #  |     .....|                         and (2->T1, 1->T0)
    #  |    ......|
    #  0----T0----1

    # Single node moves (besides those where the other node has
    # already been moved to where we want) are not considered because
    # we assume that the neighboring elements will take care of them.
    # We want the case where a whole edge is snapped to have top
    # priority.

    def get_movelist(self, movednodes):
        nodes = self.rotate(self.element.nodes)
        points = self.rotate(self.transitionpoints)
        # How many nodes have already been moved?
        count = 0
        moved = []
        unmoved = []
        for i in range(4):
            if nodes[i] in movednodes:
                count += 1
                moved.append(nodes[i])
            else:
                unmoved.append(i)
        # Transition points
        T0 = points[0]
        T1 = points[2]
        # Index map for Ts
        Tmap = {0:T0, 1:T0, 2:T1, 3:T1}
        # Building movelist
        default0 = [(nodes[0], T0), (nodes[3], T1)]
        default1 = [(nodes[1], T0), (nodes[2], T1)]
        if count == 0:
            movelist = [default0, default1]
        elif count == 1:
            if moved[0] is nodes[0]:
                # 1. n0 move to T0 : n3 to T1
                # 2. n0 != T0 : n1 to T0 & n2 to T2
                if moved[0].position() == T0:
                    movelist = [[(nodes[3], T1)]]
                else:
                    movelist = [default1]
            elif moved[0] is nodes[1]:
                if moved[0].position() == T0:
                    movelist = [[(nodes[2], T1)]]
                else:
                    movelist = [default0]
            elif moved[0] is nodes[2]:
                if moved[0].position() == T1:
                    movelist = [[(nodes[1], T0)]]
                else:
                    movelist = [default0]
            else:  # nodes[3]
                if moved[0].position() == T1:
                    movelist = [[(nodes[0], T0)]]
                else:
                    movelist = [default1]
        elif count == 2:
            if moved[0] is nodes[0] and moved[1] is nodes[3]:
                if moved[0].position() == T0 and moved[1].position() == T1:
                    return []
                else:
                    movelist = [default1]
            elif moved[0] is nodes[1] and moved[1] is nodes[2]:
                if moved[0].position() == T0 and moved[1].position() == T1:
                    return []
                else:
                    movelist = [default0]
            else:
                movelist = [[(nodes[um], Tmap[um])] for um in unmoved]

        elif count == 3:
            movelist = [[(nodes[um], Tmap[um])] for um in unmoved]
        else:
            return []
        return movelist


registerNodeSnapper(QuadEdgeSnapper, (1,0,1,0))

###########################

class TriangleEdgeSnapper(NodeSnapper):
    priority = 2

    #     0
    #     |\      T0 and T1 are the transition points
    #     | \     Move 0->T0 and/or 2->T1
    #     |  \    OR 1->(T0+T1)/2
    #     T0  \ 
    #     |.   \
    #     |..   \
    #     |...   \
    #     1---T1--2


    def get_movelist(self, movednodes):
        moved = []
        nodes = self.rotate(self.element.nodes)
        points = self.rotate(self.transitionpoints)
        # Transition points
        T0 = points[0]
        T1 = points[1]
        # Building movelist
        movelist = []
        if nodes[0] not in movednodes:
            movelist.append([(nodes[0], T0)])
            if nodes[2] not in movednodes:
                movelist.append([(nodes[0], T0), (nodes[2], T1)])
        if nodes[1] not in movednodes:
            movelist.append([(nodes[1], (T0+T1)*0.5)])
            movelist.append([(nodes[1], T0)])
            movelist.append([(nodes[1], T1)])
        if nodes[2] not in movednodes:
            movelist.append([(nodes[2], T1)])
        return movelist


registerNodeSnapper(TriangleEdgeSnapper, (1,1,0))

###########################

class QuadCornerSnapper(NodeSnapper):
    priority = 3

    # Move to two transition points on adjacent edges, in cases where
    # an edge move is impossible.  This can only happen on
    # quadrilaterals.

    #    2-----T1-----1
    #    |........    |   T0 and T1 are the transition points.
    #    |..........  |   
    #    |............T0  Pick the best of the following moves:  
    #    |............|      a) 0->T0  1->T1
    #    |............|      b) 0->T0  2->T1
    #    |............|      c) 1->T0  2->T1
    #    3------------0      d-g) the single node moves (4 total)
    #                        h) 1->(T0+T1)/2

    def get_movelist(self, movednodes):
        nodes = self.rotate(self.element.nodes)
        points = self.rotate(self.transitionpoints)
        # Transition points
        T0 = points[0]
        T1 = points[1]
        # Building movelist
        moved = [n in movednodes for n in nodes]
        movelist = []
        if not moved[0]:
            movelist.append([(nodes[0], T0)])
            if not moved[1]:
                movelist.append([(nodes[0], T0), (nodes[1], T1)])
            if not moved[2]:
                movelist.append([(nodes[0], T0), (nodes[2], T1)])
        if not moved[1]:
            movelist.extend([[(nodes[1], T0)],
                             [(nodes[1], T1)],
                             [(nodes[1], (T0+T1)*0.5)]])
            if not moved[2]:
                movelist.append([(nodes[1], T0), (nodes[2], T1)])
        if not moved[2]:
            movelist.append([(nodes[2], T1)])
        return movelist


registerNodeSnapper(QuadCornerSnapper, (1,1,0,0))


###########################

class SingleNodeSnapper(NodeSnapper):
    priority = 4

    #   ----1
    #       |    Move either 0 or 1 to T.
    #       |
    #       T
    #       |
    #       |
    #       |
    #   ----0  

    def get_movelist(self, movednodes):
        nodes = self.rotate(self.element.nodes)
        T = self.rotate(self.transitionpoints)[0]
        movelist = []
        if nodes[0] not in movednodes:
            movelist.append([(nodes[0], T)])
        if nodes[1] not in movednodes:
            movelist.append([(nodes[1], T)])
        return movelist

registerNodeSnapper(SingleNodeSnapper, (1,0,0), (1,0,0,0))

