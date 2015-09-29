# -*- python -*-
# $RCSfile: refine.py,v $
# $Revision: 1.117 $
# $Author: langer $
# $Date: 2010/12/04 03:49:58 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# Refinement works in two stages.  First a RefinementTarget object (from
# refinementtarget.py) checks the elements and marks edges for
# subdivision.  Then a RefinementRuleSet (from refinemethod.py) is
# used to actually refine the elements, according to how many times
# each edge is marked.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import progress
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import units
from ooflib.common import parallel_enable
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import refinementtarget
from ooflib.engine import refinemethod
from ooflib.engine import refinequadbisection
from ooflib.engine import skeletonmodifier
from ooflib.engine import skeletonsegment
from ooflib.engine import skeletonnode

import random

SkeletonSegment = skeletonsegment.SkeletonSegment

arbitrary_factor = 128          # used by findSignature().  Must be
				# larger than the largest number of
				# refinements of an edge.

################################

# The RefinementDegree classes specify how many times edges are
# divided initially by the RefinementTarget object, and also provide a
# 'markExtras' routine that marks additional edges for division after
# the check and mark stage.

# Changes as of Mar 04.
# Refinement Degree:
# - TriSection
# - BiSection
# Each degree has two rule sets.
# - Conservative: preserves topology, that is, if you refine a quad, you'll
#                 get only quads.
# - Liberal: MAY break topology

class RefinementDegree(registeredclass.RegisteredClass):
    registry = []
    def markExtras(self, skeleton, markedEdges):
        pass

    tip = "Number of subdivisions per segment."
    discussion = xmlmenudump.loadFile('DISCUSSIONS/engine/reg/refinementdegree.xml')

class Bisection(RefinementDegree):
    divisions = 1
    def __init__(self, rule_set):
        self.rule_set = rule_set
    def markExtras(self, skeleton, markedEdges):
        if self.rule_set.name == "conservative":
            refinequadbisection.markExtras(skeleton, markedEdges)
        
registeredclass.Registration(
    'Bisection',
    RefinementDegree,
    Bisection,
    1,
    params = [enum.EnumParameter('rule_set', refinemethod.RuleSet,
                                 refinemethod.conservativeRuleSetEnum(),
                                 tip='How to subdivide elements.')
    ],
    tip="Divide element edges into two.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/bisection.xml'))

if config.dimension() == 2:
    class Trisection(RefinementDegree):
        divisions = 2
        def __init__(self, rule_set):
            self.rule_set = rule_set

    registeredclass.Registration(
        'Trisection',
        RefinementDegree,
        Trisection,
        0,
        params = [enum.EnumParameter('rule_set', refinemethod.RuleSet,
                                     refinemethod.conservativeRuleSetEnum(),
                                     tip='How to subdivide elements')
                  ],
        tip="Gallia est omnis divisa in partes tres, as are the edges of the elements.",
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/trisection.xml'))

#################################

class EdgeMarkings:
    # Class for storing and returning how many divisions should be
    # performed on an edge.  Edges are defined by a pair of nodes.
    def __init__(self):
        self.markings = {}
        
    def mark(self, node0, node1, ndivs):
        # arguments are the nodes defining the edge, and the number of
        # new nodes to add to that edge.
        key = skeletonnode.canonical_order(node0, node1)
        try:
            # Only mark an edge if it's not already marked for more
            # divisions.
            if self.markings[key] < ndivs:
                self.markings[key] = ndivs
        except KeyError:
            self.markings[key] = ndivs

        # mark the partner segment, if it exists
        partners = node0.getPartnerPair(node1)
        if partners is not None:
            partnerKey = skeletonnode.canonical_order(partners[0], partners[1])
            try:
                # Only mark an edge if it's not already marked for more
                # divisions.
                if self.markings[partnerKey] < ndivs:
                    self.markings[partnerKey] = ndivs
            except KeyError:
                self.markings[partnerKey] = ndivs
                

    def getMark(self, node0, node1):
        key = skeletonnode.canonical_order(node0, node1)
        try:
            return self.markings[key]
        except KeyError:
            return 0

    def getMarks(self, element):
        return [self.getMark(nodes[0], nodes[1]) 
                for nodes in element.segment_node_iterator()]

    def getNMarkedEdges(self, element):
        marks = self.getMarks(element)
        nmarks = 0
        for m in marks:
            if m: nmarks += 1
        return nmarks


    # parallel function
    if parallel_enable.enabled():
        def getSharedSegments(self):
            pass  # Look in "refineParallel.py"

class RefinementCriterion(registeredclass.RegisteredClass):
    registry = []

    tip = "Restrict the set of Elements considered for refinement."
    discussion = """<para>

    Objects in the <classname>RefinementCriterion</classname> class
    are used as values of the <varname>criterion</varname> parameter
    when <link linkend='RegisteredClass-Refine'>refining</link>
    &skels;.  Only &elems; that satisfy the criterion are considered
    for refinement.

    </para>"""


class Unconditionally(RefinementCriterion):
    def __call__(self, skeleton, element):
        return 1
registeredclass.Registration(
    'Unconditional',
    RefinementCriterion,
    Unconditionally,
    ordering=0,
    tip='Consider all Elements for possible refinement.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/unconditionally.xml')
    )

if config.dimension() == 2:
    class MinimumArea(RefinementCriterion):
        def __init__(self, threshold, units):
            self.threshold = threshold
            self.units = units
        def __call__(self, skeleton, element):
            if self.units == 'Pixel':
                return element.area() > self.threshold*skeleton.MS.areaOfPixels()
            elif self.units == 'Physical':
                return element.area() > self.threshold
            elif self.units == 'Fractional':
                return element.area() > self.threshold*skeleton.MS.area()

    registeredclass.Registration(
        'Minimum Area',
        RefinementCriterion,
        MinimumArea,
        ordering=1,
        params=[parameter.FloatParameter('threshold', 10,
                                         tip="Minimum acceptable element area."),
                enum.EnumParameter('units', units.Units, units.Units('Pixel'),
                                   tip='Units for the minimum area')],
        tip='Only refine elements with area greater than the given threshold.',
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/minimumarea.xml')
        )

elif config.dimension() == 3:
    class MinimumVolume(RefinementCriterion):
        def __init__(self, threshold, units):
            self.threshold = threshold
            self.units = units
        def __call__(self, skeleton, element):
            if self.units == 'Voxel':
                return element.volume() > self.threshold*skeleton.MS.volumeOfPixels()
            elif self.units == 'Physical':
                return element.volume() > self.threshold
            elif self.units == 'Fractional':
                return element.area() > self.threshold*skeleton.MS.volume()

    registeredclass.Registration(
        'Minimum Volume',
        RefinementCriterion,
        MinimumVolume,
        ordering=1,
        params=[parameter.FloatParameter('threshold', 10,
                                         tip="Minimum acceptable element volume."),
                enum.EnumParameter('units', units.Units, units.Units('Voxel'),
                                   tip='Units for the minimum volume')],
        tip='Only refine elements with volume greater than the given threshold.',
        discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/minimumarea.xml')
        )

###################################
            
class Refine(skeletonmodifier.SkeletonModifier):
    def __init__(self, targets, criterion, degree, alpha):
        self.targets = targets      # RefinementTarget instance
        self.criterion = criterion  # Criterion for refinement
        self.degree = degree        # RefinementDegree instance
        # alpha is used for deciding between different possible
        # refinements, using effective energy
        self.alpha = alpha 
        # Available rules for the specified rule_set of refinement degree
        self.rules = refinemethod.getRuleSet(self.degree.rule_set.name)
    #########

    def apply(self, skeleton, context):
        prog = progress.getProgress("Refine", progress.DEFINITE)
        try:
            newSkeleton = skeleton.improperCopy(skeletonpath=context.path())
            return self.refinement(skeleton, newSkeleton, context, prog)
        finally:
            prog.finish()

    def applyAMR(self, skeleton):       # for adaptive mesh refinement
        prog = progress.getProgress("Refine", progress.DEFINITE)
        try:
            newSkeleton = skeleton.improperCopy(fresh=True)
            return self.refinement(skeleton, newSkeleton, None, prog)
        finally:
            prog.finish()
    
    def refinement(self, skeleton, newSkeleton, context, prog):
        # Copy the old skeleton, without copying the elements.
##         newSkeleton = skeleton.improperCopy()
        markedEdges = EdgeMarkings()
        self.newEdgeNodes = {}          # allows sharing of new edge nodes

        # Primary marking
        self.targets(skeleton, context, self.degree.divisions, markedEdges,
                     self.criterion)
        # Additional marking
        if config.dimension() == 2:
            self.degree.markExtras(skeleton, markedEdges)

        # Refine elements and segments
        segmentdict = {}                # which segments have been handled
        n = len(skeleton.elements)
        if config.dimension() == 2:
            elements = skeleton.elements
        # for 3d, we reorder the elements so that those with
        # edgemarkings that can lead to deadlocks are treated first.
        if config.dimension() == 3:
            elements = []
            nondeadlockable = []
            for ii in range(n):
                oldElement = skeleton.elements[ii]
                marks = markedEdges.getMarks(oldElement)
                signature = findSignature(marks)
                if signature in refinemethod.deadlockableSignatures:
                    elements.append(oldElement)
                else:
                    nondeadlockable.append(oldElement)
            random.shuffle(elements)
            elements.extend(nondeadlockable)

        for ii in range(n):
            oldElement = elements[ii]
            oldnnodes = oldElement.nnodes()
            # For 2D: Find the canonical order for the marks. (The
            # order is ambiguous due to the arbitrary choice of the
            # starting edge.  Finding the canonical order allows the
            # refinement rule to be found in the rule table.)
            # rotation (the first member of signature_info) is the
            # offset into the elements node list required to match the
            # refinement rule to the element's marked edges.
            # signature is the canonical ordering of the marks.  For
            # 3D: The signature info is simply a tuple listing the
            # marked edges in order.  We can no longer use a canonical
            # order and rotation since the ordering of the edges is no
            # longer arbitrary.

            # Get list of number of subdivisions on each edge ("marks")
            marks = markedEdges.getMarks(oldElement)
            signature_info = findSignature(marks)
            # Create new nodes along the subdivided element edges
            edgenodes = [
                self.getNewEdgeNodes(nodes[0], nodes[1], 
                                     marks[i], newSkeleton, skeleton)
                for nodes, i in zip(oldElement.segment_node_iterator(),
                                    range(oldElement.getNumberOfEdges()))
                ]

            # Create new elements
            if config.dimension() == 2: signature = signature_info[1]
            elif config.dimension() == 3: signature = signature_info
            newElements = self.rules[signature].apply(
                oldElement, signature_info, edgenodes, newSkeleton, self.alpha)

            # If the old element's homogeneity is "1", it's safe to say that
            # new elements' homogeneities are "1".
            if oldElement.homogeneity(skeleton.MS) == 1.0:
                for el in newElements:
                    el.copyHomogeneity(oldElement)

            # The calls to Skeleton.newElement() made by the
            # refinement rules have created new SkeletonSegments in
            # newSkeleton, but have not set the parentage of those
            # segments.  We have to fix that here.
            for newElement in newElements:
                for segment in newElement.getSegments(newSkeleton):
                    # Only look at each segment once.
                    if segment not in segmentdict:
                        segmentdict[segment] = 1
                        pseg = findParentSegment(skeleton, newElement,
                                                 segment,
                                                 edgenodes)
                        if pseg:
                            pseg.add_child(segment)
                            segment.add_parent(pseg)
            if prog.stopped():
                return None
            else:
                prog.setFraction(1.0*(ii+1)/n)
                prog.setMessage("%d/%d" % (ii+1, n))
            
        newSkeleton.cleanUp()

        # Make sure not to keep a reference to anything in the
        # Skeleton, or the Skeleton won't be deleted properly.  This
        # Refine object might nto be deleted, since it's kept in a
        # history buffer.
        del self.newEdgeNodes

        return newSkeleton

    ################
    
    def getNewEdgeNodes(self, node0, node1, ndivs, newSkeleton, oldSkeleton):
        # Create ndivs new nodes between node0 and node1 in the
        # skeleton.  node0 and node1 are from the old skeleton
        if ndivs < 1:
            return []
        key = skeletonnode.canonical_order(node0, node1)
        try:
            #Unlike in snaprefine.py, we don't make a list copy.
            nodes = self.newEdgeNodes[key]
            if config.dimension() == 2:
                # Since this is the second time we're using this list
                # of nodes, we must be looking at them from the other
                # side, and the nodes should be in the opposite order.
                # Reversing them in place like this would be wrong if
                # the list weren't being used immediately, as it is in
                # Refine.apply() 
                # don't do this in 3D because for now
                # we are only doing bisection, and because order
                # doesn't have the same meaning in 3d.
                nodes.reverse()
        except KeyError:
            nodes = [None]*ndivs
            p0 = node0.position()
            p1 = node1.position()
            delta = (p1 - p0)/(ndivs+1)
            for i in range(ndivs):
                pt = p0 + (i+1)*delta
                nodes[i] = newSkeleton.newNodeFromPoint(pt)
            self.newEdgeNodes[key] = nodes

            ## Begin Periodic Skeleton Node Construction ###################
            partners=node0.getPartnerPair(node1)
            # It can happen that partners contains the same two nodes
            # (node1,node0), if the Skeleton is only one element wide!
            if partners and node0!=partners[1]:
                partnerKey = skeletonnode.canonical_order(partners[0],
                                                          partners[1])
                # Make new edge nodes for the partner-edge.  ndivs for
                # the current edge and the partner-edge must be the
                # same.
                nodespartner = [None]*ndivs
                s = newSkeleton.MS.size()
                n0pt=node0.position()
                n1pt=node1.position()
                # in 2D only one of the first four cases can be met,
                # but in 3D a combination of two of the following six
                # cases can be met and we must test that the
                # appropriate periodicity is in the skeleton
                partnerdict = {}
                # Case 1: boundary at left edge or face
                if n0pt.x==0 and n1pt.x==0 and newSkeleton.left_right_periodicity:
                    partnerdict[0]=s[0]
                # Case 2: boundary at right edge or face
                elif n0pt.x==s[0] and n1pt.x==s[0] and newSkeleton.left_right_periodicity:
                    partnerdict[0]=0
                # Case 3: boundary at bottom edge or face
                if n0pt.y==0 and n1pt.y==0 and newSkeleton.top_bottom_periodicity:
                    partnerdict[1]=s[1]
                # Case 4: boundary at top edge or face
                elif n0pt.y==s[1] and n1pt.y==s[1] and newSkeleton.top_bottom_periodicity:
                    partnerdict[1]=0
                if config.dimension() == 3:
                    # Case 5: boundary at back edge or face
                    if n0pt.z==0 and n1pt.z==0 and newSkeleton.front_back_periodicity:
                        partnerdict[2]=s[2]
                    # Case 6: boundary at front edge or face
                    elif n0pt.z==s[2] and n1pt.z==s[2] and newSkeleton.top_bottom_periodicity:
                        partnerdict[2]=0
                    
                for i in range(ndivs):
                    pt = nodes[i].position()
                    for c,v in partnerdict.iteritems():
                        pt[c]=v
                    newnodepartner = newSkeleton.newNodeFromPoint(pt)
                    nodes[i].addPartner(newnodepartner)
                    nodespartner[i] = newnodepartner
                self.newEdgeNodes[partnerKey] = nodespartner
                ## End Periodic Skeleton Node Construction ###################

        return nodes
    
    # parallel fuctions
    if parallel_enable.enabled():
        def apply_parallel(self, skeleton, context):
            newSkeleton = skeleton.improperCopy(skeletonpath=context.path())  # fresh=False
            return self.refinement_parallel(skeleton, newSkeleton, context)

        def refinement_parallel(self, skeleton, newSkeleton, context):
            pass  # Look in "refineParallel.py"

        def shareCommonNodes(self, markedEdges, skeleton, newSkeleton):
            pass  # Look in "refineParallel.py"
    
#################################

def findParentSegment(oldSkeleton, element, segment, edgenodes):
    n0, n1 = segment.nodes()            # nodes of the segment
    parents = n0.getParents()
    if parents:
        p0 = parents[-1]
    else:
        p0 = None
        
    parents = n1.getParents()
    if parents:
        p1 = parents[-1]
    else:
        p1 = None    
    oldElement = element.getParents()[-1]
    nnodes = oldElement.nnodes()

    if p0 is not None and p1 is not None:
        pseg = oldSkeleton.findSegment(p0, p1)
        if pseg:
            # Trivial case: the parent nodes define a segment in the
            # parent skeleton.  That segment is this segment's parent.
            return pseg
        # Both nodes have parents, but the parent nodes don't define a
        # segment in the old skeleton.  (This is unlikely to happen
        # during refinement.)  The segment does not have a parent.
        return None

    elif p0 is not None or p1 is not None:
        # Exactly one new endpoint has a parent in the old element.
        # The other endpoint may lie on an old segment.  If that
        # segment's other node is the parent of the new node, then
        # that segment is the parent of this segment.
        if p0 is None:
            parentnode = p1
            childnode = n1
            freechild = n0
        else:
            parentnode = p0
            childnode = n0
            freechild = n1
        nodeidx = oldElement.nodes.index(parentnode)
        if config.dimension() == 2:
            if freechild in edgenodes[nodeidx]:
                next = (nodeidx+1)%nnodes
                return oldSkeleton.findSegment(parentnode, oldElement.nodes[next])
            prev = (nodeidx - 1 + nnodes) % nnodes
            if freechild in edgenodes[prev]:
                return oldSkeleton.findSegment(parentnode, oldElement.nodes[prev])
        elif config.dimension() == 3:
            seg_map = oldElement.segToNodeMap()
            for segidx in range(len(seg_map)):
                if freechild in edgenodes[segidx]:
                    if nodeidx == seg_map[segidx][0]:
                        return oldSkeleton.findSegment(parentnode, oldElement.nodes[seg_map[segidx][1]])
                    if nodeidx == seg_map[segidx][1]:
                        return oldSkeleton.findSegment(parentnode, oldElement.nodes[seg_map[segidx][0]])
                    
                    

    elif p0 is None and p1 is None:
        # Neither new endpoint has a parent.  If the new endpoints are
        # consecutive nodes in the list of new nodes added to a parent
        # element segment, then that parent segment is the parent
        # we're looking for.
        for i in range(nnodes):
            nodelist = edgenodes[i]
            try:
                which0 = nodelist.index(n0)
                which1 = nodelist.index(n1)
            except ValueError:
                pass
            else:
                if abs(which0 - which1) == 1:
                    return oldSkeleton.findSegment(oldElement.nodes[i],
                                                   oldElement.nodes[(i+1)%
                                                                    nnodes])

################################

def findSignature(marks):
    if config.dimension() == 2:
        # Given a list of subdivisions of sides (marks), rotate a
        # canonical starting point for the list, so that it can be used as
        # an index into a table of refinement functions.  For a list
        # [x,y,z], the canonical order is that which maximizes the number
        # xyz in base arbitrary_factor.  This will fail if edges are ever
        # divided into more than arbitrary_factor segments in one
        # refinement operation.
        n = len(marks)
        max = -1
        imax = None
        for i in range(n):
            key = marks[i]
            for j in range(1, n):
                key = arbitrary_factor*key + marks[(i+j)%n]
            if key > max:
                max = key
                imax = i
        return imax, tuple([marks[(i+imax)%n] for i in range(n)])
    elif config.dimension() == 3:
        sig = []
        for i in range(len(marks)):
            if marks[i]:
                sig.append(i)
        return tuple(sig)


####################

registeredclass.Registration(
    'Refine',
    skeletonmodifier.SkeletonModifier,
    Refine,
    ordering=0,
    params=[parameter.RegisteredParameter('targets',
                                          refinementtarget.RefinementTarget,
                                          tip='Target elements to be refined.'),
            parameter.RegisteredParameter('criterion', RefinementCriterion,
                                          tip='Exclude certain elements.'),
            parameter.RegisteredParameter('degree', RefinementDegree,
                                    tip='Preferred way of subdividing a side.'),
            skeletonmodifier.alphaParameter
            ],
    tip="Subdivide elements.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/refine.xml'))
