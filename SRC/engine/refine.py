# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Refine elements such that new nodes are always placed at transition
# points, where the pixel category changes.

# Refinement works in two stages.  First a RefinementTarget object (from
# refinementtarget.py) checks the elements and marks edges for
# subdivision.  Then a RefinementRuleSet (from refinemethod.py) is
# used to actually refine the elements, according to how many times
# each edge is marked.

## TODO PYTHON3: This currently doesn't deal with transition points at
## element corners.  If there is a transition point at a corner, we
## could use no more than one transition point on the adjacent edges,
## and keep the number of rules down.  Can we treat the point at the
## corner as the limit of a point *near* the corner, so that we can
## use the same signature machinery?  The refinement rules would have
## to notice that some quads become triangles and some triangles
## disappear.  getProvisionalElement could detect non-unique nodes and
## do the right thing.
##
## The TransitionPoints SegmentDivider is very good at creating
## transition points at element corners, and then being unable to
## remove them if the resulting edges are all homogeneous.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import coord
from ooflib.SWIG.common import progress
from ooflib.SWIG.engine import ooferror
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import registeredclass
from ooflib.common import units
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import refinementtarget
from ooflib.engine import refinemethod
from ooflib.engine import skeletonmodifier
from ooflib.engine import skeletonnode

import itertools
import math

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# SegmentDivider takes a Segment and places refinement marks
# on its edges.  Different kinds are used in different refinement
# methods.

# Refine.refinement() calls RefinementTarget.__call__, for the
# appropriate target type, passing in an appropriate
# SegmentDivider as its "divider" arg.  The result is a
# dictionary of SegmentMarks objects, keyed by the pairs of nodes at
# the ends of the segment.  SegmentMarks contains the new nodes to add
# the the segment.

class SegmentDivider(registeredclass.RegisteredClass):
    registry = []
    def __init__(self, minlength):
        self.minlength = minlength
        self.minLength2 = minlength*minlength
    tip="How segments are subdivided during refinement."
    discussion=xmlmenudump.loadFile("DISCUSSIONS/engine/reg/segmentdivider.xml")

minLengthParam = parameter.NonNegativeFloatParameter(
    "minlength", value=2.0,
    tip="Minimum refined segment length in pixel units.  A length of at least 2 is suggested.")

class Bisection(SegmentDivider):
    def markSegment(self, skeleton, node0, node1, segMarkings):
        if (node0.position() - node1.position()).norm2() >= 4*self.minLength2:
            segMarkings.insert(SegmentMarks(node0, node1, (1/2,)))
    def reduceMarks(self, maxMarks, markedSegs):
        pass

registeredclass.Registration(
    'Bisection',
    SegmentDivider,
    Bisection,
    ordering=1,
    params = [minLengthParam],
    tip="Divide segments in half.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/engine/reg/bisection.xml")
)

class Trisection(SegmentDivider):
    def markSegment(self, skeleton, node0, node1, segMarkings):
        if (node0.position() - node1.position()).norm2() >= 9*self.minLength2:
            segMarkings.insert(SegmentMarks(node0, node1, (1/3, 2/3)))
    def reduceMarks(self, maxMarks, markedSegs):
        pass

registeredclass.Registration(
    'Trisection',
    SegmentDivider,
    Trisection,
    ordering=2,
    params=[minLengthParam],
    tip="Divide segments into thirds.")

class TransitionPoints(SegmentDivider):
    def markSegment(self, skeleton, node0, node1, segMarkings):
        # Get transition points
        micro = skeleton.MS
        sections = micro.getSegmentSections(node0.position(), node1.position(),
                                            self.minlength)
        # if debug.debug():
        #     if len(sections) > 1:
        #         for section in sections:
        #             if section.pixelLength() < self.minlength:
        #                 debug.fmsg(f"node0={node0} {node0.position()}",
        #                            f"node1={node1} {node1.position()}",
        #                            f"sections={sections}")
        #                 raise ooferror.PyErrPyProgrammingError(
        #                     "section too short!")

        # Compute fractions and categories
        fractions = []
        span = node1.position() - node0.position()
        length = math.sqrt(span*span)
        for section in sections[:-1]:
            diff = section.physicalPt1() - node0.position()
            fractions.append(math.sqrt(coord.dot(diff, diff))/length)
        marks = SegmentMarks(node0, node1, fractions)

        # Add the new marks to the set of all marks, and check for
        # compatibility if they're already there.
        if segMarkings.insert(marks):
            # SegmentMarkings.insert returns True if the segment has
            # already been marked.  If so, merge the old marks with
            # the new, and update them in segMarkings.
            
            # Get the preexisting markings. fetch() ensures that the
            # data goes from node0 to node1, the same way as the
            # current data.
            othermarks = segMarkings.fetch(node0, node1)
            if len(marks) == len(othermarks) == 0:
                return
            
            # Merge the fractions in this set of marks and the other
            # set of marks into a single sorted list.  If a pair of
            # fractions in the two lists are almost equal, just put
            # the average value in.  There should not be any chance
            # that one fraction in one list is close to two fractions
            # in the other list, if getSegmentSections is working
            # properly.
            #
            # minfrac defines what we mean by "too
            # close". It should be greater than 1/plen (the fractional
            # size of one pixel). A segment that is colinear with a
            # pixel step will have intersection points in the two
            # lists that differ by 1 pixel unit, but we don't want to
            # treat them as two intersection points.

            # ............| pixel boundary
            # ............|                      If A and B are one
            # ............|                      pixel apart, they
            # ======A=====B=== element segment   aren't independent
            # ......|                            intersection points
            # ......| 
            # ......| pixel boundary
            #
            pspan = micro.physical2Pixel(span) # span in pixel coords
            plen = math.sqrt(pspan*pspan) # total segment size in pixel coords
            minfrac = self.minlength/plen # merge fractions closer than this

            newfracs = []
            i0 = i1 = 0
            while i0 < len(marks.fractions) and i1 < len(othermarks.fractions):
                f0 = marks.fractions[i0]
                f1 = othermarks.fractions[i1]
                if abs(f1 - f0) <= minfrac:
                    newfracs.append(0.5*(f0 + f1))
                    i0 += 1
                    i1 += 1
                elif f0 < f1:
                    newfracs.append(f0)
                    i0 += 1
                else:
                    newfracs.append(f1)
                    i1 += 1
            # If we reached the end of one list, put the rest of the
            # fractions in the other list into newfracs.
            if i0 < len(marks.fractions):
                newfracs.extend(marks.fractions[i0:])
            if i1 < len(othermarks.fractions):
                newfracs.extend(othermarks.fractions[i1:])

            segMarkings.update(node0, node1, newfracs)

            # If the nodes have periodic partners, the fractions will
            # be the same on the periodic partner segment.
            partners = node0.getPartnerPair(node1)
            if partners and node0 != partners[1]:
                segMarkings.update(partners[0], partners[1], newfracs)
    def reduceMarks(self, maxMarks, markedSegs):
        markedSegs.reduceMarks(maxMarks)

registeredclass.Registration(
    "TransitionPoints",
    SegmentDivider,
    TransitionPoints,
    params = [minLengthParam],
    tip="Divide segments at the intersections with pixel boundaries.",
    discussion=xmlmenudump.loadFile(
        "DISCUSSIONS/engine/reg/transitionpoint.xml"),
    ordering=3)
        
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Marks indicating where a segment should be divided. The nodes used
# to define segments are nodes in the *old* Skeleton.

class SegmentMarks:
    def __init__(self, node0, node1, fractions):
        self.node0 = node0
        self.node1 = node1
        self.fractions = fractions # mark is at (1-f)*node0 + f*node1
    def key(self):
        return skeletonnode.canonical_order(self.node0, self.node1)
    def reversed(self):
        return SegmentMarks(self.node1, self.node0,
                            [1-f for f in reversed(self.fractions)])
    def __len__(self):
        return len(self.fractions)
    def positions(self, node0, node1):
        assert ((node0 is self.node0 and node1 is self.node1) or
                (node1 is self.node0 and node0 is self.node1))
        p0 = self.node0.position()
        p1 = self.node1.position()
        if node0 is self.node0:
            fracs = self.fractions
        else:
            fracs = reversed(self.fractions)
        for f in fracs:
            yield (1-f)*p0 + f*p1
    def periodicPartnerMarks(self):
        partners = self.node0.getPartnerPair(self.node1)
        # It can happen that the partners of (n0, n1) are (n1, n0), in
        # which case we don't do anything. (Maybe if the skeleton is
        # 1x1 and fully periodic? That is not a likely situation.)
        if partners and self.node0 != partners[1]:
            return SegmentMarks(partners[0], partners[1], self.fractions)
    def reduceMarks(self, maxMarks):
        # Reduce the number of marks on this edge to at most maxMarks.
        if len(self.fractions) <= maxMarks:
            return
        if maxMarks == 1:
            # Find the mark that's closest to the average, and use it.
            avg = sum(self.fractions)/len(self.fractions)
            closest = self.fractions[0]
            delta = abs(closest - avg)
            for frac in self.fractions[1:]:
                diff = abs(frac - avg)
                if diff < delta:
                    closest = frac
                    delta = diff
            self.fractions = [closest]
        elif maxMarks == 2:
            # Choose the two fractions that are spaced most evenly.
            # That will be the fractions fi and fj > fi that minimize
            #      fi**2 + (fj-fi)**2 + (1-fj)**2
            # which would be what you'd compute for the mean squared
            # deviation of the fractional section lengths, given that
            # the average fractional section length is always 1/3.
            bestdev = 10
            fibest = None
            fjbest = None
            # TODO: This is an o(n^2) algorithm. Can it be improved?
            for i in range(len(self.fractions)-1):
                fi = self.fractions[i]
                fi2 = fi*fi
                for j in range(i+1, len(self.fractions)):
                    fj = self.fractions[j]
                    deviation = fi2 + (fj-fi)**2 + (1-fj)**2
                    if deviation < bestdev:
                        bestdev = deviation
                        fibest = fi
                        fjbest = fj
            self.fractions = [fibest, fjbest]
        else:
            # TODO: This is even worse. Can it be improved?  Do we
            # need it?  It would only be used if we have rules for
            # tetrasecting (quadrisecting) edges.
            bestsubset = None
            bestdev = 10        # bigger than any deviation
            for subset in itertools.combinations(self.fractions, maxMarks):
                fsum = subset[0]**2 + (1-subset[-1])**2
                for i in range(1,maxMarks):
                    fsum += (subset[i] - subset[i-1])**2
                if fsum < bestdev:
                    bestdev = fsum
                    bestsubset = subset
            self.fractions = bestsubset
    def __repr__(self):
        return f"SegmentMarks({self.node0}, {self.node1}, {self.fractions})"

class EmptyMarks:
    def positions(self):
        return []
    def reversed(self):
        return self
    def __len__(self):
        return 0
    def reduceMarks(self, maxMarks):
        pass
    def __repr__(self):
        return "EmptyMarks()"

emptyMarks = EmptyMarks()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Container for all the SegmentMarks in a refinement.  Each Segment
# (identified by nodes in the old Skeleton) occurs only once.

class SegmentMarkings:
    def __init__(self):
        self.markings = {}
    def insert(self, marks):
        # Insert the SegmentMarks object "marks" into this
        # SegmentMarkings set.  
        key = marks.key()
        if key in self.markings:
            return True         # didn't insert, marks are already present

        if key[0] is marks.node1:
            self.markings[key] = marks.reversed()
        else:
            self.markings[key] = marks

        # Check for periodic partners.  When marks are inserted for a
        # segment, they are also inserted for its periodic partner, if
        # there is one.  We don't have to check that the partner's
        # marks have already been inserted -- if they had been, this
        # segment's marks would have been too.
        partnerMarks = marks.periodicPartnerMarks()
        if partnerMarks is not None:
            partnerKey = partnerMarks.key()
            if partnerKey[0] is partnerMarks.node1:
                self.markings[partnerKey] = partnerMarks.reversed()
            else:
                self.markings[partnerKey] = partnerMarks
        return False
    def update(self, pt0, pt1, fractions):
        marks = SegmentMarks(pt0, pt1, fractions)
        self.markings[marks.key()] = marks
    def fetch(self, n0, n1):
        key = skeletonnode.canonical_order(n0, n1)
        marks = self.markings.get(key, emptyMarks)
        if key[0] is n1:
            return marks.reversed()
        return marks
    def getMarks(self, element):
        return [self.fetch(nodes[0], nodes[1])
                for nodes in element.segment_node_iterator()]
    def reduceMarks(self, maxMarks):
        for marking in self.markings.values():
            marking.reduceMarks(maxMarks)
    def dump(self, phile):
        for key, marks in self.markings.items():
            print(f"{key}: {marks}", file=phile)
        
                               
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#


class Refine(skeletonmodifier.SkeletonModifier):
    def __init__(self, targets, divider, rules, alpha=1):
        self.targets = targets      # RefinementTarget instance
        self.divider = divider      # Method for dividing edges
        self.rules = rules          # Methods for dividing elements
        # alpha is used for deciding between different possible
        # refinements, using effective energy
        self.alpha = alpha 
        # Available rules
        self.ruleset = refinemethod.getRuleSet(self.rules.string())

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

    def refinement(self, oldSkeleton, newSkeleton, context, prog):
        markedSegs = SegmentMarkings()

        # newEdgeNodes is a dict keyed by pairs of nodes in the old
        # Skeleton.  Its values are lists of new nodes in the new
        # Skeleton.  The values are inserted when getNewEdgeNodes is
        # called.
        newEdgeNodes = {} 

        # Use the RefinementTarget to mark the edges that should be
        # refined. 
        self.targets(oldSkeleton, context, self.divider, markedSegs)

        # Reduce the number of marks on edges to the number allowed by
        # the refinement rules.  This is done via the divider, because
        # it's not necessary for all division methods.
        self.divider.reduceMarks(self.ruleset.maxMarks(), markedSegs)

        # connectedsegs contains new segments that have had their
        # parentage set.
        connectedsegments = set()

        # Refine elements and segments
        eliter = oldSkeleton.element_iterator()
        for oldElement in eliter:
            oldnnodes = oldElement.nnodes()
            # Get list of subdivisions on each edge ("marks")
            marks =  markedSegs.getMarks(oldElement)
            # Find the canonical order for the marks. (The order is
            # ambiguous due to the arbitrary choice of the starting
            # edge.  Finding the canonical order allows the refinement
            # rule to be found in the rule table.)  rotation is the
            # offset into the elements node list required to match the
            # refinement rule to the element's marked edges.
            # signature is the canonical ordering of the marks.
            rotation, signature = findSignature(marks)
            
            # Create new nodes on segments.  The marks refer to the
            # old Skeleton, but new nodes are created in the new
            # Skeleton.
            edgenodes = [
                self.getNewEdgeNodes(nodes[0], nodes[1], emarks, newSkeleton,
                                     newEdgeNodes)
                for emarks, nodes in zip(
                        marks, oldElement.segment_node_iterator())]

            # Apply refinement rules to create new elements
            newElements = self.ruleset[signature].apply(
                oldElement, rotation, edgenodes, newSkeleton, self.alpha)
            if not newElements:
                debug.fmsg(f"{oldElement=}")
                debug.fmsg(f"{signature=} {rotation=}")
            assert newElements, "Refinement failed!"

            if debug.debug():
                for el in newElements:
                    if el.illegal():
                        debug.fmsg("Illegal refined element!")
                        debug.fmsg("    oldElement=", oldElement)
                        debug.fmsg("    newElement=", newElement)
                        debug.fmsg("    signature=", signature)

            # If the old element's homogeneity is 1, it's safe to say that
            # new elements' homogeneities are 1.
            if oldElement.homogeneity(oldSkeleton.MS, False) == 1.0:
                for el in newElements:
                    el.copyHomogeneity(oldElement)

            # The calls to Skeleton.newElement() made by the
            # refinement rules have created new SkeletonSegments in
            # newSkeleton, but have not set the parentage of those
            # segments.  We have to fix that here.
            for newElement in newElements:
                for segment in newElement.getSegments(newSkeleton):
                    # Only look at each segment once.
                    if segment not in connectedsegments:
                        connectedsegments.add(segment)
                        pseg = findParentSegment(oldSkeleton, newElement,
                                                 segment,
                                                 edgenodes)
                        if pseg:
                            pseg.add_child(segment)
                            segment.add_parent(pseg)
            if prog.stopped():
                return None
            prog.setFraction(eliter.fraction())
            prog.setMessage(f"{eliter.nexamined()}/{eliter.ntotal()} elements")
       
        newSkeleton.cleanUp()
        
        return newSkeleton

    def getNewEdgeNodes(self, node0, node1, marks, newSkeleton, newEdgeNodes):
        # Create new nodes on the edge joining the nodes corresponding
        # to node0 and node1 in the new skeleton.  node0 and node1 are
        # in the *old* skeleton.
        if len(marks) < 1:
            return []
        key = skeletonnode.canonical_order(node0, node1)
        try:
            # Look for already created nodes
            nodes = newEdgeNodes[key]
        except KeyError:
            # Nodes have not been created on this edge yet. 
            pt0 = node0.position()
            pt1 = node1.position()
            # marks.positions() returns positions in the correct order
            # for the directed segment going from n0 to n1.
            nodes = [newSkeleton.newNodeFromPoint(pt)
                     for pt in marks.positions(node0, node1)]
            newEdgeNodes[key] = nodes
            
            # Create periodic nodes if necessary
            partners = node0.getPartnerPair(node1)
            # It can happen that partners contains the same two nodes
            # (node1,node0). Maybe only in perverse situations, though.
            if partners and node0 != partners[1]:
                partnerKey = skeletonnode.canonical_order(partners[0],
                                                          partners[1])
                # Make new edge nodes on the partner edge, using the
                # same marks.
                sz = newSkeleton.MS.size()
                # partnerdict[c] = v means to set the c component of
                # the new node positions to v
                partnerdict = {}
                if newSkeleton.left_right_periodicity:
                    if pt0.x == pt1.x == 0:
                        # segment along left edge
                        partnerdict[0] = sz[0]
                    elif pt0.x == pt1.x == sz[0]:
                        # segment along right edge
                        partnerdict[0] = 0
                if newSkeleton.top_bottom_periodicity:
                    if pt0.y == pt1.y == 0:
                        # segment along bottom edge
                        partnerdict[1] = sz[1]
                    elif pt0.y == pt1.y == sz[1]:
                        # segment along top edge
                        partnerdict[1] = 0
                partnernodes = [None] * len(marks)
                for i, pt in enumerate(marks.positions(node0, node1)):
                    # Compute the location of the new node, which is
                    # the same as the location of the old node, but
                    # shifted to the other boundary via partnerdict.
                    newpt = nodes[i].position()
                    for c, v in partnerdict.items():
                        newpt[c] = v
                    newnodepartner = newSkeleton.newNodeFromPoint(newpt)
                    nodes[i].addPartner(newnodepartner)
                    partnernodes[i] = newnodepartner

                newEdgeNodes[partnerKey] = partnernodes
        else: # no exception in newEdgeNodes lookup
            # Nodes were already created on this edge.  They were
            # created when this segment or its periodic partner was
            # traversed in the other direction, so we need to return
            # them in the opposite order.
            nodes.reverse()

        return nodes
        

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

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
        if freechild in edgenodes[nodeidx]:
            next = (nodeidx+1)%nnodes
            return oldSkeleton.findSegment(parentnode, oldElement.nodes[next])
        prev = (nodeidx - 1 + nnodes) % nnodes
        if freechild in edgenodes[prev]:
            return oldSkeleton.findSegment(parentnode, oldElement.nodes[prev])
                    
                    

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

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

signature_base = 32

def findSignature(marks):
    # Given a list of SementMarks for each side of an element, rotate
    # a canonical starting point for the list, so that it can be used
    # as an index into a table of refinement functions.  For a list
    # [x,y,z], the canonical order is that which maximizes the number
    # xyz in base signature_base.  This will fail if edges are ever
    # divided into more than signature_base segments in one refinement
    # operation.
    n = len(marks)              # number of segments
    maxkey = -1
    imax = None
    for i in range(n):
        key = 0                 
        for j in range(n):
            key = signature_base*key + len(marks[(i+j)%n])
        if key > maxkey:
            maxkey = key
            imax = i
    return imax, tuple(len(marks[(i+imax)%n]) for i in range(n))


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

registeredclass.Registration(
    'Refine',
    skeletonmodifier.SkeletonModifier,
    Refine,
    ordering=0,
    params=[
        parameter.RegisteredParameter(
            'targets',
            refinementtarget.RefinementTarget,
            tip='Target elements to be refined.'),
        parameter.RegisteredParameter(
            'divider',
            SegmentDivider,
            tip="How to divide the edges of the refined elements."),
        enum.EnumParameter(
            'rules', refinemethod.RuleSet,
            refinemethod.defaultRuleSetEnum(),
            tip="The set of rules used to divide elements after their segments are divided."),
        skeletonmodifier.alphaParameter
            ],
    tip="Subdivide elements.",
    ## TODO PYTHON3: Update docs!
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/refine.xml')
)
