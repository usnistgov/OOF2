# -*- python -*-
# $RCSfile: refineParallel.py,v $
# $Revision: 1.9 $
# $Author: langer $
# $Date: 2014/09/27 21:40:56 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## TODO: This file has not been updated to use new (April 2009)
## Progress objects.

from ooflib.SWIG.common import mpitools
from ooflib.SWIG.engine import cskeleton
from ooflib.common import debug
from ooflib.common import utils
from ooflib.engine import refine
from ooflib.engine.IO import skeletonIPC

_rank = mpitools.Rank()
_size = mpitools.Size()

# list=[1,2,3,4,5], signature=[2,3]
# output=[[1,2], [3,4,5]]
def listrize(list, signature):
    nsig = len(signature)
    count = 0
    output = [[] for i in range(nsig)]
    for i in range(nsig):
        for j in range(signature[i]):
            output[i].append(list[count])
            count += 1
    return output

# Compares two lists and get the common item (assumes they DO have a common item)
def common_item(list0, list1):
    if len(list0) == 1:
        return list0[0]
    if len(list1) == 1:
        return list1[0]
    # Both have multiple items
    for i in list0:
        if i in list1:
            return i

# Returns shared segments from all the marked ones.
def getSharedSegments(markedEdges, actual_node=False):
    global _size
    segs = [ [] for i in range(_size) ]
    for key in markedEdges.markings.keys():
        nd0 = key[0]  
        nd1 = key[1]
        if nd0.isShared() and nd1.isShared():
            # If they are both shared nodes, there's gotta be a common
            # process that is sharing the nodes.
            sharer = common_item(nd0.sharedWith(), nd1.sharedWith())
            if actual_node:
                segs[sharer].append(nd0)  # actual nd0
                segs[sharer].append(nd1)  # actual nd1
            else:
                segs[sharer].append(nd0.remoteIndex(sharer))  # remote index
                segs[sharer].append(nd1.remoteIndex(sharer))  # remote index
            segs[sharer].append(markedEdges.markings[key])  # "ndivs"
    return segs  # [[None for myself], [m0,m1,ndivs, ...], [n0,n1,ndivs] ...]

# Marks shared segments, if needed.
# A segment that is marked on the other side might not be marked on my side.
def shareMarkings(markedEdges, skeleton):
    global _rank
    global _size
    segs = getSharedSegments(markedEdges)  # shared segs per process
    sigs = [len(s) for s in segs]  # no. of shared segs per process: [0, m, n]
    # Now, collect all the shared segment data.
    allsigs = mpitools.Allgather_IntVec(sigs)  # Gathered version of sigs
    segs = reduce(lambda x,y: x+y, segs)  # Reduced version of segs
    allsegs = mpitools.Allgather_IntVec(segs)  # Gathered version of segs
    # Listrized version of allsegs: list of "segs" indexed by process id.
    allsegs = [listrize(seg, sig) for seg, sig in zip(allsegs, allsigs)]   
    
    for i in range(_size):

        if i == _rank: continue  # can't shared with myself
        # allsegs[i][_rank] contains information for (shared) segments
        # that are marked at i-th process.
        if len(allsegs[i][_rank]) == 0: continue  # nothing in it
        
        for j in range(len(allsegs[i][_rank])/3):
            # Ugly but efficient enough
            nd0 = skeleton.getNodeWithIndex(allsegs[i][_rank][3*j])
            nd1 = skeleton.getNodeWithIndex(allsegs[i][_rank][3*j+1])
            ndivs = allsegs[i][_rank][3*j+2]
            markedEdges.mark(nd0, nd1, ndivs)

# Sort nodes geometrically using distance from [0,0].
# Since there can be no nodes that have the same position, it just works.
# Returns indices of sorted nodes.
# TODO: Use normal sort!
def geometric_sort(nodes):
    dist_dict = {}
    distances = []
    for n in nodes:
        position = n.position()
        distance = position[0]*position[0] + position[1]*position[1]
        distances.append(distance)
        dist_dict[distance] = n.getIndex()
    distances.sort()
    sorted = [dist_dict[d] for d in distances]
    return sorted

# When a new node is created on a shared segment, it will inherit
# process-sharing data.
def shareCommonNodes(refiner, markedEdges, skeleton, newSkeleton):
    global _rank
    global _size
    segs = getSharedSegments(markedEdges, actual_node=True)
    nodes = [[] for i in range(_size)]
    for i in range(_size):
        if i != _rank and segs[i]:
            for j in range(len(segs[i])/3):  # iterate over segments
                nd0 = segs[i][3*j]
                nd1 = segs[i][3*j+1]
                ndivs = segs[i][3*j+2]
                nodes[i] += refiner.getNewEdgeNodes(nd0, nd1, ndivs, newSkeleton, skeleton)
                # These nodes are shared -- it is guaranteed that same nodes
                # exist on the other side but not necessarily in the same order.
                # Once they are re-arranged in the same order, updating
                # process-sharing info for these nodes can be easily done.
            nodes[i] = geometric_sort(nodes[i])

    sigs = [len(s) for s in nodes]  # Partition signature of nodes
    allsigs = mpitools.Allgather_IntVec(sigs)  # Gathered version of sigs
    nodes = reduce(lambda x,y: x+y, nodes)  # Reduced version of nodes
    allnodes = mpitools.Allgather_IntVec(nodes)  # Gathered version of segs
    # Listrized version of allnodes
    allnodes = [listrize(nds, sig) for nds, sig in zip(allnodes, allsigs)]

    mynodes = allnodes[_rank]  # Same as "nodes" before it was reduced.
    for i in range(_size):
        if i != _rank and mynodes[i]:
            for j in range(len(mynodes[i])):
                thenode = newSkeleton.getNodeWithIndex(mynodes[i][j])
                # mynodes[i] and allnodes[i][_rank] are lists of same size.
                # They contains indices of same nodes (position-wise) in
                # the same order.
                thenode.sharesWith(i, allnodes[i][_rank][j])  # proc, remote-index

# Debug function.
def report_skeleton(skeleton, simple=False):
    if simple:
        debug.fmsg("NO. of NODES:", skeleton.nnodes(),
                   "NO. of ELEMENTS:", skeleton.nelements())
    else:
        debug.fmsg("NO. of NODES:", skeleton.nnodes(),
                   "NO. of ELEMENTS:", skeleton.nelements())
        debug.fmsg("#NODES")
        for nd in skeleton.node_iterator():
            debug.fmsg("Node #", nd.getIndex(),
                       nd.position(), nd._remote_index)
        debug.fmsg("#ELEMENTS")
        for el in skeleton.element_iterator():
            debug.fmsg("Element #", el.getIndex(),
                       [n.getIndex() for n in el.nodes])

# Parallel version of refinement.
def _refinement(self, skeleton, newSkeleton, context):
    global _rank
    if _rank == 0:
        pBar = progressbar.getProgress()
        
    markedEdges = refine.EdgeMarkings()
    self.newEdgeNodes = {}  # allows sharing of new edge nodes

    # Primary marking
    self.targets(skeleton, context, self.degree.divisions, markedEdges,
                 self.criterion)
    # Additional marking -- only for (conservative) bisection at this point.
    self.degree.markExtras(skeleton, markedEdges)

    # Now, share the marking information on the boundary
    shareMarkings(markedEdges, skeleton)

    # Refine elements and segments
    segmentdict = {}  # which segments have been handled already.
    elements = skeleton.elements

    # At this point, to properly update progress bar, every process has
    # loop over the same range(maxn).
    # TODO: Is progress bar not supposed to work within IPC call?
    n = len(elements)
    alln = mpitools.Allgather_Int(n)
    maxn = max(alln)
    nelem = 0
    ntotal = reduce(lambda x,y: x+y, alln)
    for ii in range(maxn):
        try:
            oldElement = elements[ii]
            count = 1
            
            oldnnodes = oldElement.nnodes()
            # Get list of number of subdivisions on each edge ("marks")
            marks = markedEdges.getMarks(oldElement)
            # Find the canonical order for the marks. (The order is
            # ambiguous due to the arbitrary choice of the starting
            # edge.  Finding the canonical order allows the refinement
            # rule to be found in the rule table.)  rotation is the
            # offset into the elements node list required to match the
            # refinement rule to the element's marked edges.
            # signature is the canonical ordering of the marks.
            rotation, signature = refine.findSignature(marks)
            # Create new nodes along the subdivided element edges
            edgenodes = [self.getNewEdgeNodes(oldElement.nodes[i],
                                              oldElement.nodes[(i+1)%oldnnodes],
                                              marks[i], newSkeleton, skeleton)
                         for i in range(oldnnodes)]
            # Create new elements
            newElements = self.rules[signature].apply(oldElement, rotation,
                                                      edgenodes, newSkeleton,
                                                      self.alpha)
            # If the old element's homogeneity is "1", it's safe to say that
            # new elements' homogeneities are "1".
            if oldElement.homogeneity(skeleton.MS) == 1.:
                for el in newElements:
                    el.copyHomogeneity(oldElement)

            # The calls to Skeleton.newElement() made by the
            # refinement rules have created new SkeletonSegments in
            # newSkeleton, but have not set the parentage of those
            # segments.  We have to fix that here.
            for newElement in newElements:
                for segment in newElement.getSegments(newSkeleton):
                    # Only look at each segment once.
                    if not segmentdict.has_key(segment):
                        segmentdict[segment] = 1
                        pseg = refine.findParentSegment(skeleton, newElement,
                                                        segment, edgenodes)
                        if pseg:
                            pseg.add_child(segment)
                            segment.add_parent(pseg)

        except IndexError:
            count = 0
            
        # No. of elements done.
        nelem_step = mpitools.Allgather_Int(count)
        nelem += reduce(lambda x,y: x+y, nelem_step)
        if _rank == 0:
            if pBar.query_stop():
                pBar.set_failure()
                pBar.set_message("Failed")
                mpitools.Isend_Bool(False, range(1,_size))
                return None
            else:
                pBar.set_progress(1.0*(nelem)/ntotal)
                pBar.set_message("refining skeleton: %d/%d" % (nelem, ntotal))
                mpitools.Isend_Bool(True, range(1,_size))
        else:
            if not mpitools.Recv_Bool(0):
                return
            
    # New nodes that are created from the segments that are shared,
    # have to be informed bertween sharers.
    shareCommonNodes(self, markedEdges, skeleton, newSkeleton)
    # Collecting Skeletons
    skeletonIPC.collect_pieces(newSkeleton)

    newSkeleton.cleanUp()
##    report_skeleton(newSkeleton)
##    if _rank == 0:
##        debug.fmsg(newSkeleton.all_skeletons)
    return newSkeleton
    
refine.Refine.refinement_parallel = _refinement
