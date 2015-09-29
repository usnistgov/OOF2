# -*- python -*-
# $RCSfile: refinequadbisection.py,v $
# $Revision: 1.19 $
# $Author: langer $
# $Date: 2010/12/07 21:57:03 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# A function "markExtras" (at the end of the file) is responsible for
# conservative QuadBiSection and rest of functions are little ones
# used in "markExtras".

# N-marked element : element with N marked segment(s)
# odd-marked element : element with odd number(s) of marked segment(s)

from ooflib.common import debug
from ooflib.common.IO import reporter
import random

def makeOddList(skeleton, markedEdges):
    # Make a list of odd-marked elements from skeleton.elements
    oddlist = []
    for element in skeleton.element_iterator():
        if element.nnodes() == 3: continue  # Triangles have no business here.
        marks = markedEdges.getMarks(element)
        # "marks", for quads, typically looks like this; [0, 1, 0, 0], which
        # indicates the second segment of the element is marked.
        # Since it's bisection, the sum of "marks" is no. of marked edges.
        nmark = marks[0]+marks[1]+marks[2]+marks[3]
        if nmark == 1 or nmark == 3: oddlist.append(element)
    return oddlist
    
def countNeighborOdd(element, markedEdges, skeleton):
    # With a given element, it counts no. of marked-odd neighbors
    neighbors = element.edgeNeighbors(skeleton)
    count = 0
    for nghbr in neighbors:
        if nghbr and nghbr.nnodes() == 4:
            nmark = markedEdges.getNMarkedEdges(nghbr)
            if nmark == 1 or nmark == 3: count += 1
    return count

# Takes care of an odd-marked element with no odd-marked element
# in its neighbors.
def noOdd(element, skeleton, markedEdges, oddlist, ninfo):
    # if the element is on edge boundary
    if "on_edge" in ninfo.nmark:
        # Element is containing edge boundary, which is very good.
        # If this one is at the corner of mesh(two edge boundary seg.s),
        # it chooses any edge boundary segement comes first.
        for i in range(4):
            n0 = element.nodes[i]
            n1 = element.nodes[(i+1)%4]
            if ninfo.nmark[i] == "on_edge" and not markedEdges.getMark(n0, n1):
                markedEdges.mark(n0, n1, 1)
                del oddlist[-1]
                return 1
            
    # Pretty desperate situation from here on --
    # have to mark an unmarked segment of mark-even element, which
    # means this to-be-marked element becomes mark-odd element and thus,
    # it has to be added to "oddlist".

    # First, if three edges are marked in this element ....
    # A solution seems to be pretty obvious.
    if markedEdges.getNMarkedEdges(element) == 3:
        for i in range(4):
            n0 = element.nodes[i]
            n1 = element.nodes[(i+1)%4]
            if not markedEdges.getMark(n0, n1):
                markedEdges.mark(n0, n1, 1)
                del oddlist[-1]
                if ninfo.neighbors[i].nnodes() == 4:
                    oddlist.append(ninfo.neighbors[i])
                return 1

    # Now, this element should be a mark-one element.
    # To use one of its neighbors as a bridge to another mark-odd element,
    # it looks for a neighbor that has ONE mark-odd element.
    for i in range(4):
        if ninfo.nmark[i] != 0 and ninfo.nmark[i] != 2:
            continue
        if countNeighborOdd(ninfo.neighbors[i], markedEdges, skeleton) == 1:
            n0 = element.nodes[i]
            n1 = element.nodes[(i+1)%4]
            if not markedEdges.getMark(n0, n1):
                markedEdges.mark(n0, n1, 1)
                del oddlist[-1]
                if ninfo.neighbors[i].nnodes() == 4:
                    oddlist.append(ninfo.neighbors[i])
                return 1
                
    # Totally helpless situation. Mark any markable edge.
    for i in range(4):
        if ninfo.nmark[i] == 0 or ninfo.nmark[i] == 2:
            n0 = element.nodes[i]
            n1 = element.nodes[(i+1)%4]
            if not markedEdges.getMark(n0, n1):
                markedEdges.mark(n0, n1, 1)
                del oddlist[-1]
                if ninfo.neighbors[i].nnodes()==4:
                    oddlist.append(ninfo.neighbors[i])
                return 1

    return 0

def oneOdd(element, markedEdges, oddlist, ninfo):
    if 1 in ninfo.nmark:
        i = ninfo.nmark.index(1)
    else:
        i = ninfo.nmark.index(3)
    n0 = element.nodes[i]
    n1 = element.nodes[(i+1)%4]
    if not markedEdges.getMark(n0, n1):
        markedEdges.mark(n0, n1, 1)
        del oddlist[-1]
        if ninfo.neighbors[i] in oddlist:
            oddlist.remove(ninfo.neighbors[i])
        return 1

    return 0

def someOdds(element, skeleton, markedEdges, oddlist, ninfo):
    # looks for a neighbor element(mark-odd itself) with
    # one mark-odd element to bridge each other.
    for i in range(4):
        if ninfo.nmark[i] != 1 and ninfo.nmark[i] != 3:
            continue
        if countNeighborOdd(ninfo.neighbors[i], markedEdges, skeleton)==1:
            n0 = element.nodes[i]
            n1 = element.nodes[(i+1)%4]
            if not markedEdges.getMark(n0, n1):
                markedEdges.mark(n0, n1, 1)
                del oddlist[-1]
                if ninfo.neighbors[i] in oddlist:
                    oddlist.remove(ninfo.neighbors[i])
                return 1
            
    # First come, first service
    for i in range(4):
        if ninfo.nmark[i] != 1 and ninfo.nmark[i] != 3:
            continue
        n0 = element.nodes[i]
        n1 = element.nodes[(i+1)%4]
        if not markedEdges.getMark(n0, n1):
            markedEdges.mark(n0, n1, 1)
            del oddlist[-1]
            if ninfo.neighbors[i] in oddlist:
                oddlist.remove(ninfo.neighbors[i])
            return 1
        
    return 0

# A container for various infos concerning an element's neighbors
class NeighborInfo:
    def __init__(self, element, skeleton, markedEdges):
        self.neighbors = element.edgeNeighbors(skeleton)
        self.nmark = ["on_edge"]*4
        self.odds = 0  # no. of odd-marked elements in the neighborhood
        for i in range(4):
            if self.neighbors[i] and self.neighbors[i].nnodes() == 4:
                self.nmark[i] = markedEdges.getNMarkedEdges(self.neighbors[i])
                if self.nmark[i] == 1 or self.nmark[i] == 3:
                    self.odds += 1
            elif self.neighbors[i] and self.neighbors[i].nnodes() == 3:
                self.nmark[i] = None

def markExtras(skeleton, markedEdges):
    oddlist = makeOddList(skeleton, markedEdges)
    repeat = 0  # How many times it's repeating itself to get things resolved.
    
    random.shuffle(oddlist)
    while oddlist:
        element = oddlist[-1]
        ninfo = NeighborInfo(element, skeleton, markedEdges)

        # no odd-marked neighbors
        if ninfo.odds == 0:
            done = noOdd(element, skeleton, markedEdges, oddlist, ninfo)
        # one odd-marked neighbor
        elif ninfo.odds == 1:
            done = oneOdd(element, markedEdges, oddlist, ninfo)
        # either two or three odd-marked neighbors
        elif ninfo.odds == 2 or ninfo.odds == 3:
            done = someOdds(element, skeleton, markedEdges, oddlist, ninfo)

        if not done:
            repeat += 1
            ## TODO: Is there a better way of determining that the
            ## method has failed?

            # The magic number "100" is just an arbitrary choice.
            if repeat>10:
                reporter.report("Failed to preserve quadrilateral topology for %s." % element)
                break
