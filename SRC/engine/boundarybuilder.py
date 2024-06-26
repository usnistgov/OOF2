# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This file defines registered class objects which actually
# build boundaries.   Structure is similar to skeletonselectionmod.

from ooflib.SWIG.common import config 
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import director
from ooflib.common import registeredclass
from ooflib.common import runtimeflags
from ooflib.common import primitives
from ooflib.common.IO import automatic
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.engine import skeletoncontext
from ooflib.engine import skeletonsegment # for the segSequence function.
from ooflib.engine.IO import skeletongroupparams
import math
#Interface branch
from ooflib.engine.IO import interfaceparameters

########################
# Boundary naming components.

# This resolver can return "None" in the skelname==None case, which
# occurs when the registeredclassfactory switches around.
def bdynameresolver(param, startname):
    if param.automatic():
        basename='boundary'
    else:
        basename = startname
    skelname = param.group['skeleton'].value
    skelcontext = skeletoncontext.skeletonContexts[skelname]
    return skelcontext.uniqueBoundaryName(basename)


skeletonparam = whoville.WhoParameter(
    'skeleton', skeletoncontext.skeletonContexts,
    tip="The Skeleton containing the  boundary.")

nameparam = parameter.AutomaticNameParameter('name', bdynameresolver,
                                             value=automatic.automatic,
                                             tip="Name for this boundary.")

paramgroup = parameter.ParameterGroup(skeletonparam, nameparam)

########################


class BoundaryConstructor(registeredclass.RegisteredClass):
    registry = []
    tip = "Tools to build Skeleton boundaries."
    discussion = """<para>
    <classname>BoundaryConstructor</classname> objects are used by the
    <xref linkend='MenuItem-OOF.Skeleton.Boundary.Construct'/> command
    to build <link
    linkend='Section-Concepts-Skeleton-Boundary'>boundaries</link> in
    a &skel;.
    </para>"""
    xrefs=["Section-Tasks-SkeletonBoundaries"]

# Utility function -- given a bunch of segments and an orientation,
# it returns (startnode, seg_list), where seg_list is suitably
# ordered, and startnode is at the start.  Throws an exception if
# it fails.
def _segset2seglist(seg_set, direction, skel):

    if len(seg_set)==0:
        raise ooferror.PyErrUserError("Attempt to sequence null segment set.")
    
    (seg_list, node_list, winding_number) = skeletonsegment.segSequence(seg_set)
    
    # At this point, seg_list is an ordered list of adjacent
    # segments, and "node_list" is the corresponding set of nodes.
    # The path is a loop if node_list[0]==node_list[-1], otherwise
    # it's a simple path.

    # We may want to reverse this list, depending on the
    # setting of "direction".
    firstnode = node_list[0]
    lastnode = node_list[-1]
    
    startnode = firstnode
    # The winding number is used to handle the cases where the line
    # crosses a periodic boundary.
    if (firstnode != lastnode and firstnode not in lastnode.getPartners()) \
       or winding_number != [0,0]:
        # In case the first node and last node are partners, we set them
        # equal so that we can compare positions properly.
        if lastnode in firstnode.getPartners():
            lastnode = firstnode
        if direction == director.Director('Left to right'):
            if firstnode.position().x > \
               lastnode.position().x + winding_number[0]*skel.MS.size()[0]:
                seg_list.reverse()
                startnode = lastnode
        elif direction == director.Director('Right to left'):
            if firstnode.position().x < \
               lastnode.position().x + winding_number[0]*skel.MS.size()[0]:
                seg_list.reverse()
                startnode = lastnode
        elif direction == director.Director('Top to bottom'):
            if firstnode.position().y < \
               lastnode.position().y + winding_number[1]*skel.MS.size()[1]:
                seg_list.reverse()
                startnode = lastnode
        elif direction == director.Director('Bottom to top'):
            if firstnode.position().y > \
               lastnode.position().y + winding_number[1]*skel.MS.size()[1]:
                seg_list.reverse()
                startnode = lastnode
        else:
            # User specified clockwise or counterclockwise for a
            # non-loop segment set.  This is an error.
            raise ooferror.PyErrUserError(
                "Clockwise or counterclockwise is for closed loops.")

    # Use the total area swept out by vectors from the origin to the
    # nodes along the path as we traverse the path in order to
    # determine if the existing sequence traces a clockwise or
    # counterclockwise path.  If two consecutive nodes in the
    # node_list are not the endpoints of a segment, we are crossing a
    # periodic boundary.  In this case, use the positions not to find
    # the area swept out, but to increment the position_adjustment
    # needed to unwrap the periodic boundary conditions.
    else: # firstnode==lastnode, loop case.
        startnode = None
        area = 0.0
        p0 = node_list[0].position()
        position_adjustment = primitives.Point(0,0)
        for i in range(1,len(node_list)):
            p1 = node_list[i].position() + position_adjustment
            if skel.findSegment(node_list[i],node_list[i-1]) is not None:
                area += p0.x * p1.y - p1.x * p0.y
                p0 = p1
            else:
                position_adjustment += p0 - p1
                # setting p0 = p1 here will be redundant as we
                # must now adjust positions by p0 - p1
            
        if direction == director.Director('Clockwise'):
            if area > 0.0:
                seg_list.reverse()
        elif direction == director.Director('Counterclockwise'):
            if area < 0.0:
                seg_list.reverse()
        else:
            # User specified an endpoint orientation on a loop.
            raise ooferror.PyErrUserError(
                "Closed loops need clockwise or counterclockwise direction.")

    return (startnode, seg_list)


# ## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ## #


# Convert a group name and skeleton context into an actual list of segments.
def segments_from_seg_aggregate(skelcontext, group):
    if group == placeholder.selection:
        seg_set = skelcontext.segmentselection.retrieve()
    else:
        seg_set = skelcontext.segmentgroups.get_group(group)
    return seg_set

# Build an edge boundary from a segment set.
class EdgeFromSegments(BoundaryConstructor):
    def __init__(self, group, direction):
        self.group = group
        self.direction = direction

    def __call__(self, skelcontext, name):
        skelobj = skelcontext.getObject()

        seg_set = segments_from_seg_aggregate(skelcontext, self.group)
        
        (startnode, seg_list) = _segset2seglist(seg_set, self.direction, skelobj)
        # At this point, we have a correctly-sequenced list of segments.
        # Actually create the boundary.  The context will create it in
        # the underlying object.
        skelcontext.createEdgeBoundary(name, seg_list, startnode)
    


registeredclass.Registration(
    "Edge boundary from segments",
    BoundaryConstructor,
    EdgeFromSegments,
    ordering=100,
    params = [skeletongroupparams.SegmentAggregateParameter('group',
                              tip="Construct the boundary from these segments"),
              director.DirectorParameter('direction',
                                         director.Director('Clockwise'),
                                         tip="Direction of the boundary.")],
    tip="Construct an edge boundary from a set of segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/edge_from_segments.xml'))


    
# ## ### #### ##### ###### ####### ######## ####### ##### #### ### ## #

  
# Finds the perimeter of an elementgroup.  Requires that the element
# group have a topologically simple (non-self-intersecting,
# non-disjoint) boundary.

# Utility function for extracting a segment list from elements.
# Also used by the DirectorWidget.
def segments_from_el_aggregate(skelcontext, group):
    seg_set = {}

    skelobj = skelcontext.getObject()
    
    if group == placeholder.selection:
        elements = skelcontext.elementselection.retrieve()
    else:
        elements = skelcontext.elementgroups.get_group(group)
        
    # We want to retain the boundary segments -- these occur
    # exactly once in the element set, and all the others occur
    # exactly twice, so iterate over all the segments, adding them
    # to a dictionary, unless they already appear, in which case
    # remove them.
    for e in elements:
        for s in e.getSegments(skelcontext.getObject()):
            try:
                del seg_set[s]
            except KeyError:
                seg_set[s]=1

    # now post process to see if any remaining segments coincide
    # on the periodic boundaries.
    # perhaps partnered segments would be useful for this?
    # (seg_set changes, so make copy of keys before looping.)
    for s in list(seg_set.keys()):
        nodes = s.get_nodes()
        partners = nodes[0].getPartnerPair(nodes[1])
        if partners is not None:
            ps = skelobj.findSegment(partners[0],partners[1])
            if ps in seg_set:
                del seg_set[ps]
                del seg_set[s]

    return list(seg_set.keys())

class EdgeFromElements(BoundaryConstructor):
    def __init__(self, group, direction):
        self.group = group
        self.direction = direction

    def __call__(self, skelcontext, name):
        skelobj = skelcontext.getObject()
        seg_list = segments_from_el_aggregate(skelcontext, self.group)
        (startnode, seg_list) = _segset2seglist(
            seg_list, self.direction, skelobj)
        skelcontext.createEdgeBoundary(name, seg_list, startnode)

registeredclass.Registration(
    "Edge boundary from elements",
    BoundaryConstructor,
    EdgeFromElements,
    ordering=101,
    params = [skeletongroupparams.ElementAggregateParameter('group',
                           tip="Construct the boundary from these elements"),
              director.DirectorParameter('direction',
                                         director.Director('Clockwise'),
                                         tip="Direction of Boundary.")],
    tip="Construct an edge boundary around a set of elements.",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/edge_from_elements.xml')
)


# ## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ## #

# segments_from_node_aggregate is called by EdgeFromNodes, below, and
# also by DirectorWidget.loop_check() in boundarybuilderGUI.py, via
# the segmenter dict from skeletongroupwidgets.py.

# To unambiguously build an edge boundary from a set of nodes, it's
# necessary to find a unique linearly ordered set of segments that
# connect all of the nodes.  Constructing a path through a linked set
# of nodes (a graph, in the graph theory sense of the word) such that
# each node is visited once is called the Hamiltonian Path Problem,
# and is NP complete.  See
# https://en.wikipedia.org/wiki/Hamiltonian_path_problem
# and 
# A Search Procedure for Hamilton Paths and Circuits, Frank Rubin
# https://dl.acm.org/doi/pdf/10.1145/321850.321854
# Fortunately we don't expect to have to solve extremely large or
# complicated graphs, and can use a brute force approach.  I think.

class SequenceError(Exception): pass

def representativeNode(node, periodicmap):
    # Get the representative for the given node. A node that's not a
    # key in periodic map is its own representative.
    return periodicmap.get(node, node)

def segments_from_node_aggregate(skelcontext, group):
    if group == placeholder.selection:
        originalnodes = set(skelcontext.nodeselection.retrieve())
    else:
        originalnodes = set(skelcontext.nodegroups.get_group(group))

    skel = skelcontext.getObject()

    # When the skeleton has periodic boundary conditions, the periodic
    # partners of a node are all considered to be one point, as far as
    # the graph is concerned.  All of the periodic partners are
    # represented by a single representative node and tracked by the
    # periodicmap dict.
    periodicmap = {}

    # nodeset contains the nodes to be sequenced, after taking
    # periodicity into account.
    nodeset = set()

    # Find nodeset and periodicmap.
    for node in originalnodes:
        # Add node to nodeset only if none of its periodic partners
        # are already in nodeset.
        for p in node.getPartners():
            if p in nodeset:
                break
        else:
            nodeset.add(node)
            # At this point we don't know which periodic partners of
            # the node will be used, so put them all in periodic map.
            # It's easier to do this now than it is to search for them
            # later, when looking for a connection to a neighbor of
            # one of the partners.
            periodicmap[node] = node
            for p in node.getPartners():
                periodicmap[p] = node

    # Construct the graph.
    connections = {}
    for node in nodeset:
        for other in node.neighborNodes(skel):
            nother = periodicmap.get(other, other)
            if nother in nodeset:
                if node in connections:
                    connections[node].add(nother)
                else:
                    connections[node] = set([nother])

    # If there are isolated nodes that don't have any neighbors in the
    # set, then the set is not sequenceable.  The isolated nodes won't
    # be in connections.
    if len(connections) != len(nodeset):
        return []

    # The final path must either have two endpoints, or be a loop with
    # no endpoints.  The endpoints are nodes with only one neighbor.
    # See if there are 0 or 2 of them.  Also look for a point with
    # only two neighbors, because it will be a good starting point
    # when searching for a loop.
    endpoints = []
    twopoint = None             # a point with only two neighbors
    for node, nbrs in connections.items():
        if len(nbrs) == 1:
            endpoints.append(node)
        if not twopoint and len(nbrs) == 2:
            twopoint = node
    nendpts = len(endpoints)

    # Identify the start and end points and the first step in the
    # path.  Choosing the first step now guarantees that we won't
    # accidentally identify the path and its reverse and think that
    # we've found two paths.
    if nendpts == 2:
        startpt = endpoints[0]
        path = [startpt, next(iter(connections[startpt]))]
        endpt = endpoints[1]
    elif nendpts == 0 and  twopoint is not None:
        startpt = twopoint
        # The two points connected to startpt are the next point in
        # the path after startpt, and endpt.  Which is which doesn't
        # matter here.
        nextpt, endpt = iter(connections[startpt])
        path = [startpt, nextpt]
    else:
        # If we didn't find a starting point, the node set isn't
        # sequenceable.  (That statement might not be true for general
        # graphs, but it's true for planar graphs constructed from
        # corners and edges of tilings.  We think.)
        return []

    # Search for Hamiltonian paths, joining startpt to endpt.
    hampaths = []
    try:
        _extend_path(connections, path, endpt, hampaths) # recursive search
    except SequenceError:
        # More than one Hamiltonian path was found. 
        return []
    if len(hampaths) != 1:
        # There's no path or more than one path. 
        return []

    hampath = hampaths[0]       # The unique Hamiltonian path
    if nendpts == 0:
        hampath.append(hampath[0]) # Close the loop
        
    # Convert the path, which is a list of nodes, to a set of segments.
    ## TODO: we're discarding the connectivity information, which will
    ## be regenerated later by skeletonsegment.segSequence. That is
    ## inefficient. Do we care?  Probably not. 
    segset = set()
    for i in range(1, len(hampath)):
        nodeA = hampath[i-1]
        nodeB = hampath[i]
        seg = skel.findSegment(nodeA, nodeB)
        if seg is not None:
            segset.add(seg)
        else:
            # Because the nodes we were using are the representative
            # nodes, it's possible that a step in the path uses nodes
            # from opposite sides of the Skeleton. In that case, the
            # above call to findSegment will fail.  We should replace
            # one or both nodes with one of their periodic partners.
            nodes0 = [nodeA] + nodeA.getPartners() 
            nodes1 = [nodeB] + nodeB.getPartners()
            # Look for a pair of nodes that are periodic partners of
            # nodeA and nodeB, define a segment in the Skeleton, and
            # are in the original set of nodes (ie not simply periodic
            # partners).
            for n0 in nodes0:
                if seg:
                    break
                if n0 in originalnodes: 
                    for n1 in nodes1:
                        if n1 in originalnodes:
                            seg = skel.findSegment(n0, n1)
                            if seg:
                                break
            else:
                # Try again, without requiring the nodes to be in the
                # original set.
                for n0 in nodes0:
                    if seg:
                        break
                    for n1 in nodes1:
                        seg = skel.findSegment(n0, n1)
                        if seg:
                            break
            if seg is not None:
                segset.add(seg)
            else:
                raise ooferror.PyErrPyProgrammingError(
                    "segments_from_node_aggregate failed.")
    return segset

def _extend_path(connections, path, endpt, hampaths):
    # Extend the path in all possible directions by adding a
    # neighboring point and calling this routine again.  If there are
    # no points to add, see if the path is complete.  
    currentpt = path[-1]
    foundone = False
    for nextpt in connections[currentpt]:
        # TODO: Checking that nextpt isn't already in the path is
        # o(n), which might be slow.  It could be made o(1) by giving
        # each node an index in [0, len(nodeset)) and working with
        # indices instead of node objects.  Then an array of bools
        # indexed by the node index would say if a node is already in
        # the path.  However, the set of nodes is not likely to be
        # large, and if it is, the python recursion limit or the
        # combinational complexity of searching all paths is likely to
        # be more limiting than this o(n) search.

        # TODO: to limit recursion, maybe make trivial steps
        # non-recursively?  Trivial steps are when nextpt only has two
        # connections and isn't in the path.
        if nextpt not in path:
            foundone = True
            path.append(nextpt)
            _extend_path(connections, path, endpt, hampaths)
            path.pop()          # remove nextpt
    if not foundone:
        # There's nothing to add.  Are we done?
        if len(path) == len(connections) and path[-1] == endpt:
            if len(hampaths) == 1:
                # We found a path before this one, so the sequence
                # isn't unique.
                raise SequenceError
            hampaths.append(path[:])
    

class EdgeFromNodes(BoundaryConstructor):
    def __init__(self, group, direction):
        self.group = group
        self.direction = direction

    def __call__(self, skelcontext, name):
        path_segs = segments_from_node_aggregate(skelcontext, self.group)
        (startnode, seg_list) = _segset2seglist(path_segs, self.direction,
                                                skelcontext.getObject())
        skelcontext.createEdgeBoundary(name, seg_list, startnode)

registeredclass.Registration(
    "Edge boundary from nodes",
    BoundaryConstructor,
    EdgeFromNodes,
    ordering=102,
    params=[skeletongroupparams.NodeAggregateParameter('group',
                            tip="Node group from which to deduce segments"),
            director.DirectorParameter('direction',
                                       director.Director('Clockwise'),
                                       tip="Direction of Boundary.")],
    tip="Construct an edge boundary from a collection of nodes.",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/engine/reg/edge_from_nodes.xml')
    )

# ## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ## #


# Point boundary construction can be done from either
# segments or nodes, both cases are very simple.
class PointFromNodes(BoundaryConstructor):
    def __init__(self, group):
        self.group = group

    def __call__(self, skelcontext, name):
        skelobj = skelcontext.getObject()

        if self.group == placeholder.selection:
            nodelist = skelcontext.nodeselection.retrieve()
        else:
            nodelist = skelcontext.nodegroups.get_group(self.group)

        skelcontext.createPointBoundary(name, nodelist)

registeredclass.Registration(
    "Point boundary from nodes",
    BoundaryConstructor,
    PointFromNodes,
    ordering=103,
    params = [skeletongroupparams.NodeAggregateParameter('group',
                               tip="Construct the boundary from these nodes")],
    tip="Construct a point boundary from a set of nodes.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/point_from_nodes.xml')
    )


class PointFromSegments(BoundaryConstructor):
    def __init__(self, group):
        self.group = group

    def __call__(self, skelcontext, name):
        skelobj = skelcontext.getObject()

        nodes = {}

        if self.group == placeholder.selection:
            segments = skelcontext.segmentselection.retrieve()
        else:
            segments = skelcontext.segmentgroups.get_group(self.group)

        for s in segments:
            nodes[s.nodes()[0]]=s
            nodes[s.nodes()[1]]=s

        skelcontext.createPointBoundary(name, nodes.keys())

registeredclass.Registration(
    "Point boundary from segments",
    BoundaryConstructor,
    PointFromSegments,
    ordering=104,
    params = [skeletongroupparams.SegmentAggregateParameter('group',
                         tip="Construct the boundary from these segments")],
    tip="Construct a point boundary from the endpoints of a set of segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/point_from_segments.xml'))

class PointFromElements(BoundaryConstructor):
    def __init__(self, group):
        self.group = group

    def __call__(self, skelcontext, name):
        skelobj = skelcontext.getObject()

        if self.group == placeholder.selection:
            elements = skelcontext.elementselection.retrieve()
        else:
            elements = skelcontext.elementgroups.get_group(self.group)

        nodes = set()
        for element in elements:
            for i in range(element.nnodes()):
                n0 = element.nodes[i]
                n1 = element.nodes[(i+1)%element.nnodes()]
                seg = skelobj.getSegment(n0, n1)
                # A segment is on the boundary of the selection if it
                # belongs to only one element.
                n = 0
                for el in seg.getElements():
                    if el in elements: n += 1
                if n == 1:
                    nodes.add(n0)
                    nodes.add(n1)

        skelcontext.createPointBoundary(name, nodes) 

registeredclass.Registration("Point boundary from elements",
                             BoundaryConstructor,
                             PointFromElements,
                             ordering=105,
                             params = [
        skeletongroupparams.ElementAggregateParameter('group', tip="Construct the boundary from these elements")],
                             tip="Construct a point boundary surrounding a set of elements.",
                             discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/point_from_elements.xml'))

###############################################################
#Interface branch

# Build an edge boundary from segments along an interface
class EdgeFromInterface(BoundaryConstructor):
    def __init__(self, interface, direction):
        self.interface = interface
        self.direction = direction

    def __call__(self, skelcontext, name):
        skelobj = skelcontext.getObject()

        (seg_set, direction_set)=skelobj.getInterfaceSegments(
            skelcontext, self.interface)

        if self.direction==director.Director('Non-sequenceable'):
            skelcontext.createNonsequenceableEdgeBoundary(name, seg_set, direction_set)
        else:
            (startnode, seg_list) = _segset2seglist(seg_set, self.direction, skelobj)
            # At this point, we have a correctly-sequenced list of segments.
            # Actually create the boundary.  The context will create it in
            # the underlying object.
            skelcontext.createEdgeBoundary(name, seg_list, startnode)

if runtimeflags.surface_mode:
    registeredclass.Registration(
        "Edge boundary from interface segments",
        BoundaryConstructor,
        EdgeFromInterface,
        ordering=200,
        params = [
            interfaceparameters.InterfacesParameter('interface',
                                                    tip='Construct the boundary from these interface segments.'),
            ##    skeletongroupparams.SegmentAggregateParameter('group',
            ##                                                  tip="Construct the boundary from these segments"),
    director.DirectorInterfacesParameter('direction',
                                         director.Director('Clockwise'),
                                         tip="Direction of the boundary.")],
        tip="Construct an edge boundary from a set of interface segments.",
        discussion = """<para>

        Create an edge boundary from segments specified by an
        interface definition.  If the interface segments are
        disconnected, the corresponding edge boundary is also
        disconnected, and it will be labeled as not sequenceable.

    </para>"""
    )
