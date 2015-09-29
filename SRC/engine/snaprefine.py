# -*- python -*-
# $RCSfile: snaprefine.py,v $
# $Revision: 1.24 $
# $Author: langer $
# $Date: 2010/12/04 03:50:02 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This file implements "Snap Refine"
# (was called "Intelligent Refine" (pun intended)).
# New edge nodes are transition points.
# The "ruleset" is always liberal in 2D but 3D only has a conservative ruleset for now.

# Comment from the original refine.py
# Refinement works in two stages.  First a RefinementTarget object (from
# refinementtarget.py) checks the elements and marks edges for
# subdivision.  Then a RefinementRuleSet (from refinemethod.py) is
# used to actually refine the elements, according to how many times
# each edge is marked.

from ooflib.SWIG.common import config
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import parallel_enable
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import refinementtarget
if config.dimension() == 2:
    from ooflib.engine import refinequadbisection
from ooflib.engine import skeletonmodifier
from ooflib.engine import skeletonsegment
from ooflib.engine import skeletonnode
from ooflib.engine import refine
from ooflib.engine import snaprefinemethod

SkeletonSegment = skeletonsegment.SkeletonSegment

arbitrary_factor = 128          # used by findSignature().  Must be
				# larger than the largest number of
				# refinements of an edge.

#################################

class SnapEdgeMarkings(refine.EdgeMarkings):
    # Class for storing and returning how many divisions should be
    # performed on an edge.  Edges are defined by a pair of nodes.
    def __init__(self, newSkeleton, oldSkeleton, maxdelta2):
        self.markings = {}
        # New for Snap Refine
        self.newEdgeNodes = {}
        self.newSkeleton=newSkeleton
        self.newSkelMS=newSkeleton.MS
        self.oldSkeleton=oldSkeleton
        self.maxdelta2=maxdelta2

    def getTransitionPoints(self, n0pt, n1pt):
        #print "in getTransitionPoints"
        #Get a transition point starting from each end.
        transpt0 = self.newSkelMS.transitionPointWithPoints_unbiased(n0pt,n1pt)
        transpt1 = self.newSkelMS.transitionPointWithPoints_unbiased(n1pt,n0pt)

        if transpt0 and transpt1:
            #Check if the transition points are identical or too close together
            #Steve doesn't like this, unless self.maxdelta2==0.
            #He might prefer this instead: if transpt0 != transpt1: ...
            if (transpt0-transpt1)**2>self.maxdelta2:
                transptlist=[]
                if (transpt0-n0pt)**2>self.maxdelta2:
                    transptlist.append(transpt0)
                if (transpt1-n1pt)**2>self.maxdelta2:
                    transptlist.append(transpt1)
                return transptlist
            else:
                #Pick one. Check if it is at, or too close to, the end points.
                if (transpt0-n0pt)**2>self.maxdelta2 and \
                   (transpt0-n1pt)**2>self.maxdelta2:
                    return [transpt0]
                else:
                    return []
        elif transpt0:
            if (transpt0-n0pt)**2>self.maxdelta2 and \
                   (transpt0-n1pt)**2>self.maxdelta2:
                return [transpt0]
            else:
                return []
        elif transpt1:
            if (transpt1-n0pt)**2>self.maxdelta2 and \
                   (transpt1-n1pt)**2>self.maxdelta2:
                return [transpt1]
            else:
                return []
        return []

    # helper function for getSnapMarks 
    def getPeriodicTransPtHelper(self, transptlistCandidates, c1, c2, v1, v2, node0, node1):
        n0pt=node0.position()
        n1pt=node1.position()
        key=skeletonnode.canonical_order(node0,node1)
        partners=node0.getPartnerPair(node1)
        partnerKey = skeletonnode.canonical_order(partners[0], partners[1])

        #Get transpt closest to the endpoints
        transpt0=transptlistCandidates[0]
        transpt1=transptlistCandidates[0] #?
        transptlist = []
        transptnodelist = []
        #Squaring would not be necessary if we order
        #the operands correctly.
        min0=(transpt0[c2]-n0pt[c2])**2
        min1=(transpt1[c2]-n1pt[c2])**2
        for transpt in transptlistCandidates:
            mintmp=(transpt[c2]-n0pt[c2])**2
            if mintmp<min0:
                min0=mintmp
                transpt0=transpt
            mintmp=(transpt[c2]-n1pt[c2])**2
            if mintmp<min1:
                min1=mintmp
                transpt1=transpt
        transptlist.append(transpt0)
        if transpt0 != transpt1 and \
               (transpt0[c2]-transpt1[c2])**2>self.maxdelta2:
            transptlist.append(transpt1)
        #Fix the horizontal coordinates to match the location
        #of the edge when creating nodes.
        transptnodelistPartner=[]
        for transpt in transptlist:
            #For current edge
            transpt[c1]=v1
            transptnode = self.newSkeleton.newNodeFromPoint(transpt)
            transptnodelist.append(transptnode)
            #For partner
            transpt[c1]=v2
            transptnodePartner = self.newSkeleton.newNodeFromPoint(transpt)
            transptnode.addPartner(transptnodePartner)
            transptnodelistPartner.append(transptnodePartner)
        self.newEdgeNodes[key] = transptnodelist
        #transptnodelistPartner.reverse()
        self.newEdgeNodes[partnerKey] = transptnodelistPartner
        return transptnodelist


    # Modified from refine.py to take into account the
    # edge categories and transition points.
    # This method does the work of both getMarks and getNewEdgeNodes
    # This method selects which marked edges are to be bisected.
    def getSnapMarks(self, element):
        #print "in getSnapMarks"
        numinitmarks=0
        marks=[]
        cats=[]
        transpts=[]
        nnodes = element.nnodes()
        for node0, node1 in element.segment_node_iterator():
            n0pt=node0.position()
            n1pt=node1.position()
            key=skeletonnode.canonical_order(node0,node1)
            initmark=0
            try:
                initmark=self.markings[key]
                # If the edges are marked then the element should be
                # refined, even if we find no transition points.
                numinitmarks+=initmark
            except KeyError:
                pass
            if initmark>0:
                #print "initmark>0"
                #Marked for bisection or trisection, find or retrieve new edge nodes.
                try:
                    #See if we already created new edge nodes for this edge.
                    transptnodelist = self.newEdgeNodes[key][:] # Make a list copy
                    if config.dimension() == 2:
                        transptnodelist.reverse()
                except KeyError:
                    #print "not already in edge nodes"
                    partners=node0.getPartnerPair(node1)
                    #It can happen that partners contains the same two nodes (node1,node0)!
                    if partners and node0!=partners[1]:
                        ############## Begin Periodic Skeleton Node Construction ###################
                        partnerKey = skeletonnode.canonical_order(partners[0], partners[1])
                        #If the edge nodes have periodic partners, then find the transition
                        #points on the current edge and the partner edge. Get the pair of
                        #transition points that is closest to the endpoints (imagine joining
                        #together the two opposite edges).
                        n0pt_partner=partners[0].position()
                        n1pt_partner=partners[1].position()
                        transptlistCandidates=self.getTransitionPoints(n0pt,n1pt)+\
                                         self.getTransitionPoints(n0pt_partner,n1pt_partner)
                        size = self.newSkelMS.size()
                        if len(transptlistCandidates)>0:
                            #Case 1: boundary at left edge or face
                            if n0pt.x==0 and n1pt.x==0:
                                transptnodelist = self.getPeriodicTransPtHelper(transptlistCandidates, 0, 1, 0, size[0], node0, node1)
                            #Case 2: boundary at right edge or face
                            elif n0pt.x==size[0] and n1pt.x==size[0]: 
                                transptnodelist = self.getPeriodicTransPtHelper(transptlistCandidates, 0, 1, size[0], 0, node0, node1)
                            #Case 3: boundary at bottom edge or face
                            elif n0pt.y==0 and n1pt.y==0:
                                transptnodelist = self.getPeriodicTransPtHelper(transptlistCandidates, 1, 0, 0, size[1], node0, node1)
                            #Case 4: boundary at top edge or face
                            elif n0pt.y==size[1] and n1pt.y==size[1]:
                                transptnodelist = self.getPeriodicTransPtHelper(transptlistCandidates, 1, 0, size[1], 0, node0, node1)

                        else:
                            self.newEdgeNodes[key]=[]
                            self.newEdgeNodes[partnerKey]=[]
                            transptnodelist = []
                        ############## End Periodic Skeleton Node Construction ###################
                    else:
                        #print "non periodic case"
                        transptnodelist = [self.newSkeleton.newNodeFromPoint(pt)
                                           for pt in self.getTransitionPoints(n0pt, n1pt)]
                        self.newEdgeNodes[key] = transptnodelist

                if len(transptnodelist)==2:
                    transpt0 = transptnodelist[0].position()
                    transpt1 = transptnodelist[1].position()
                    #Order of the arguments to edgeHomogeneityCat are significant.
                    #If the edge n0pt-n1pt is horizontal or vertical and lies at
                    #a pixel boundary, then we want the function to use the pixels
                    #lying within the element in its calculations.
                    homog0, cat0 = self.newSkelMS.edgeHomogeneityCat(n0pt,transpt0)
                    homog1, cat1 = self.newSkelMS.edgeHomogeneityCat(transpt0,transpt1)
                    homog2, cat2 = self.newSkelMS.edgeHomogeneityCat(transpt1,n1pt)
                    marks.append(2)
                    cats.append((cat0,cat1,cat2))
                    transpts.append(transptnodelist)
                elif len(transptnodelist)==1:
                    transpt = transptnodelist[0].position()
                    homog0, cat0 = self.newSkelMS.edgeHomogeneityCat(n0pt,transpt)
                    homog1, cat1 = self.newSkelMS.edgeHomogeneityCat(transpt,n1pt)
                    marks.append(1)
                    cats.append((cat0,cat1))
                    transpts.append(transptnodelist)
                else:
                    marks.append(0)
                    homogedge,catedge=self.newSkelMS.edgeHomogeneityCat(n0pt,n1pt)
                    cats.append((catedge,))
                    transpts.append([])
            else:
                marks.append(0)
                homogedge,catedge=self.newSkelMS.edgeHomogeneityCat(n0pt,n1pt)
                cats.append((catedge,))
                transpts.append([])

        #print "end of getSnapMarks"
        return (numinitmarks, marks, cats, transpts)


###################################
            
class SnapRefine(refine.Refine):
    #Unlike refine.py, alpha parameter not used (yet?)
    def __init__(self, targets, criterion, min_distance, alpha=1):
        self.targets = targets      # RefinementTarget instance
        self.criterion = criterion  # Criterion for refinement
        # alpha is used for deciding between different possible
        # refinements, using effective energy
        self.alpha = alpha 
        # Available rules
        self.rules = snaprefinemethod.getRuleSet('liberal')

        self.min_distance=min_distance
    #########

    # TODO: This still overlaps quite a bit with refine.py - when
    # moving this to C, we should try to clean this up somewhat, also,
    # it would be good to have a signature scheme that works in both
    # 2D and 3D.

    def refinement(self, skeleton, newSkeleton, context, prog):
        maxdelta = max(newSkeleton.MS.sizeOfPixels())
        maxdelta2=(self.min_distance*maxdelta)**2
        markedEdges = SnapEdgeMarkings(newSkeleton,skeleton,maxdelta2)
        self.newEdgeNodes = {}          # allows sharing of new edge nodes

        # Primary marking (bisections only!)
        self.targets(skeleton, context, 1, markedEdges,
                     self.criterion)

        # Additional marking
        #self.degree.markExtras(skeleton, markedEdges)

        # Refine elements and segments
        segmentdict = {}                # which segments have been handled
        n = len(skeleton.elements)
        elements = skeleton.elements
        
        for ii in range(n):
            #print ii, n
            oldElement = elements[ii]
            oldnnodes = oldElement.nnodes()
            # For 2D:
            # Get list of number of subdivisions on each edge ("marks")
            (numinitmarks,marks,cats,edgenodes) = \
                      markedEdges.getSnapMarks(oldElement)
            # Find the canonical order for the marks. (The order is
            # ambiguous due to the arbitrary choice of the starting
            # edge.  Finding the canonical order allows the refinement
            # rule to be found in the rule table.)  rotation is the
            # offset into the elements node list required to match the
            # refinement rule to the element's marked edges.
            # signature is the canonical ordering of the marks.
            #rotation, signature = findSignature(marks)
            signature_info = findSignature(marks)
            if config.dimension() == 2: signature = signature_info[1]
            elif config.dimension() == 3: signature = signature_info
            #print numinitmarks, signature

            # Create new elements
            # TODO: It's annoying that we have a separate
            # "unrefinedelement" method.  It would be cleaner if this
            # were called automatically using the signature.  We
            # should do this when we move things to C.
            if numinitmarks>0:
                newElements = self.rules[signature].apply(
                    oldElement, signature_info, cats,
                    edgenodes, newSkeleton, maxdelta2)
            else:

                newElements = snaprefinemethod.unrefinedelement(
                    oldElement, signature_info, newSkeleton)

            # If the old element's homogeneity is 1, it's safe to say that
            # new elements' homogeneities are 1.
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
            prog.setFraction(1.0*(ii+1)/n)
            prog.setMessage("%d/%d elements" % (ii+1, n))
       
        newSkeleton.cleanUp()
        #print "end of refinement"

        return newSkeleton

#################################

findParentSegment = refine.findParentSegment
findSignature = refine.findSignature

####################

registeredclass.Registration(
    'Snap Refine',
    skeletonmodifier.SkeletonModifier,
    SnapRefine,
    ordering=400,
    params=[
        parameter.RegisteredParameter(
            'targets',
            refinementtarget.RefinementTarget,
            tip='Target elements to be refined.'),
        parameter.RegisteredParameter(
            'criterion',
            refine.RefinementCriterion,
            tip='Exclude certain elements.'),
        parameter.FloatRangeParameter(
            'min_distance',
            (0.01, 3.0, 0.01),
            value=1.0,
            tip=
"""Minimum distance of transition points along a given edge
from each other and the end-points, in units of the maximum pixel dimension.""")
#            ,skeletonmodifier.alphaParameter
            ],
    tip="Subdivide elements along pixel boundaries.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/snaprefine.xml')
    )
