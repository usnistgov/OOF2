# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Menu commands for reading a Skeleton from a file.

# TODO: the name of the Skeleton appears many times in the file, in
# each menu command.  That makes it hard for the user to edit the file
# to change the name.  Ugly solution: have a global "currentskeleton"
# variable which is set by the initial Skeleton.New command.  Better
# solution: allow variables to be set locally *in* the data file, and
# store the skeleton name there.

# even easier solution: users can just use sed or the find/change
# option in most text editors

from ooflib.SWIG.common import config
from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.engine import materialmanager
from ooflib.engine import skeletonboundary
from ooflib.engine import skeletoncontext
from ooflib.engine.IO import materialmenu
import ooflib.common.microstructure
#Interface branch
from ooflib.engine import skeletonsegment
if config.dimension() == 2:
    import ooflib.engine.skeleton as skeleton
elif config.dimension() == 3:
    import ooflib.engine.skeleton3d as skeleton

from ooflib.common.utils import stringjoin

import sys

OOFMenuItem = oofmenu.OOFMenuItem

OOF = mainmenu.OOF

skelmenu = OOF.LoadData.addItem(OOFMenuItem('Skeleton'))

if config.dimension() == 2:

    def _newSkelPeriodic(menuitem, name, microstructure,
                         left_right_periodicity=False,
                         top_bottom_periodicity=False):
        skeleton.newEmptySkeleton(name, microstructure,
                                  left_right_periodicity,
                                  top_bottom_periodicity)
        
    periodicparams = [parameter.StringParameter('name', tip="Name for the Skeleton."),
                whoville.WhoParameter('microstructure',
                                      ooflib.common.microstructure.microStructures,
                                      tip=parameter.emptyTipString),
                parameter.BooleanParameter('left_right_periodicity',
                    tip="Whether the skeleton is periodic in the horizontal direction"),
                parameter.BooleanParameter('top_bottom_periodicity',
                    tip="Whether the skeleton is periodic in the vertical direction")]

elif config.dimension() == 3:

    def _newSkelPeriodic(menuitem, name, microstructure,
                         left_right_periodicity=False,
                         top_bottom_periodicity=False,
                         front_back_periodicity=False):
        skeleton.newEmptySkeleton(name, microstructure,
                                  left_right_periodicity,
                                  top_bottom_periodicity,
                                  front_back_periodicity)

    periodicparams = [parameter.StringParameter('name', tip="Name for the Skeleton."),
                whoville.WhoParameter('microstructure',
                                      ooflib.common.microstructure.microStructures,
                                      tip=parameter.emptyTipString),
                parameter.BooleanParameter('left_right_periodicity',
                    tip="Whether the skeleton has left-right periodicity"),
                parameter.BooleanParameter('top_bottom_periodicity',
                    tip="Whether the skeleton has top-bottom periodicity"),
                parameter.BooleanParameter('front_back_periodicity',
                    tip="Whether the skeleton has back-front periodicity")]


skelmenu.addItem(OOFMenuItem(
    'NewPeriodic',
    callback=_newSkelPeriodic,
    params=periodicparams,
    help="Load Skeleton. Used internally in data files.",
    discussion="<para>Initiate loading a &skel; from a data file.</para>"))

## Optional arguments don't work in binary data files, so for
## backwards compatibility we need a menu item called "New" that
## doesn't take periodicity arguments.

def _newSkelAperiodic(menuitem, name, microstructure):
    ooflib.engine.skeleton.newEmptySkeleton(name, microstructure,
                                            False, False)

skelmenu.addItem(OOFMenuItem(
    'New',
    callback=_newSkelAperiodic,
    params=[parameter.StringParameter('name', tip="Name for the Skeleton."),
            whoville.WhoParameter('microstructure',
                                  ooflib.common.microstructure.microStructures,
                                  tip=parameter.emptyTipString)],
    help="Load Skeleton. Used internally in data files.",
    discussion="<para>Initiate loading a &skel; from a data file.</para>"))

###

## The order of the nodes in a Skeleton must not change when the
## Skeleton is saved and reloaded, or the Field values on an
## associated Mesh will be assigned to the wrong nodes. See comment in
## meshIO.py.

def _loadNodes(menuitem, skeleton, points):
##    debug.fmsg()
    # read nodes as (x,y) tuples of floats
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    for node in points:
        skeleton.newNode(*node)
    if config.dimension() == 2:
        skelcontext.updateGroupsAndSelections()
    switchboard.notify(('who changed', 'Skeleton'), skelcontext)

skelmenu.addItem(OOFMenuItem(
    'Nodes',
    callback=_loadNodes,
    params=[whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                                  tip=parameter.emptyTipString),
            parameter.ListOfTuplesOfFloatsParameter('points',
                                                    tip="List of points (nodes).")],
    help="Load Nodes. Used internally in data files.",
    discussion="<para>Load <link linkend='Section-Concepts-Skeleton-Node'>nodes</link> from a <link linkend='MenuItem-OOF.File.Save.Skeleton'>saved</link> Skeleton.</para>"
    ))

###

def _loadPartnerships(menuitem, skeleton, partnerlists):
    # Read partners as (i,j,k,l) tuples of int node indices.  Each
    # node in the tuple is a partner of every other node.
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    for nodes in partnerlists:
        nnodes = len(nodes)
        for i in range(nnodes-1):
            for j in range(i+1, nnodes):
                node0 = skeleton.getNode(nodes[i])
                node1 = skeleton.getNode(nodes[j])
                node0.addPartner(node1) # updates partner info for *both* nodes
    skelcontext.updateGroupsAndSelections()
    switchboard.notify(('who changed', 'Skeleton'), skelcontext)

skelmenu.addItem(OOFMenuItem(
    'Partnerships',
    callback=_loadPartnerships,
    params=[whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                                  tip=parameter.emptyTipString),
            parameter.ListOfTuplesOfIntsParameter('partnerlists',
                                                    tip="List of tuples containing partner sets.")],
    help="Load Partnerships. Used internally in data files.",
    discussion="<para>Load node partnerships for periodic skeletons from a <link linkend='MenuItem-OOF.File.Save.Skeleton'>saved</link> Skeleton.</para>"
    ))

###

def _loadElements(menuitem, skeleton, nodes):
##    debug.fmsg()
    # read elements as tuples of node indices
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    for nodelist in nodes:
        skeleton.loadElement(*nodelist)
    skelcontext.getTimeStamp(None).increment()
    skeleton.updateGeometry()
    if config.dimension() == 2:
        skelcontext.updateGroupsAndSelections()
    switchboard.notify(('who changed', 'Skeleton'), skelcontext)

skelmenu.addItem(OOFMenuItem(
    'Elements',
    callback=_loadElements,
    params=[whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                                  tip=parameter.emptyTipString),
            parameter.ListOfTuplesOfIntsParameter('nodes',
                                                  tip="List of element connectivities (List of node indices).")],
    help="Load Elements. Used internally in data files.",
    discussion="<para>Load <link linkend='Section-Concepts-Skeleton-Element'>elements</link> from a <link linkend='MenuItem-OOF.File.Save.Skeleton'>saved</link> Skeleton.</para>"
    ))

###

def _loadPinnedNodes(menuitem, skeleton, nodes):
##    debug.fmsg()
    # "nodes" is a list of integer indices into skeleton.nodes
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    pinned = skelcontext.pinnednodes
    pinned.pin([skeleton.nodes[i] for i in nodes])
    pinned.signal()
skelmenu.addItem(OOFMenuItem(
    'PinnedNodes',
    callback = _loadPinnedNodes,
    params = [
    whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                          tip=parameter.emptyTipString),
    parameter.ListOfIntsParameter('nodes', tip="List of indices of pinned nodes.")],
    help="Load pinned Nodes. Used internally in data files.",
    discussion="<para>Load <link linkend='MenuItem-OOF.Graphics_n.Toolbox.Pin_Nodes.Pin'>pinned</link> nodes from a &skel; data file.</para>"
    ))

###
    
def _loadPointBoundary(menuitem, skeleton, name, nodes, exterior):
##    debug.fmsg()
    # "nodes" is a list of integer indices into skeleton.nodes
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    skelcontext.createPointBoundary(name, [skeleton.nodes[i] for i in nodes],
                                    exterior, autoselect=0)
    # autoselect=0 prevents the boundary from being selected in the
    # skelcontext. Selection shouldn't happen except by explicit user
    # action.

skelmenu.addItem(OOFMenuItem(
    'PointBoundary',
    callback=_loadPointBoundary,
    params=[
    whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                          tip=parameter.emptyTipString),
    parameter.StringParameter('name', tip="Name of Point Boundary."),
    parameter.ListOfIntsParameter('nodes', tip="List of node indices."),
    parameter.IntParameter('exterior', 0, tip="1 (true) for the exterior boundary and 0 (false) for otherwise.")],
    help="Load Point Boundary. Used internally in data files.",
    discussion="<para>Load a <link linkend='Section-Concepts-Skeleton-Boundary-Point'><classname>PointBoundary</classname></link> from a Skeleton data file.</para>"
    ))

###

def _loadEdgeBoundary(menuitem, skeleton, name, edges, exterior):
##    debug.fmsg()
    # "edges" is a list of pairs of integer indices into skeleton.nodes
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    seglist = [skeleton.getSegment(
        *[skeleton.nodes[i] for i in e] )
               for e in edges]
    #Interface branch
    try:
        (segs, nodes, winding) = skeletonsegment.segSequence(seglist)
        startnode = skeleton.nodes[edges[0][0]]
        skelcontext.createEdgeBoundary(name, seglist, startnode,
                                       exterior, autoselect=0)
    except skeletonsegment.SequenceError:
        directionlist=[]
        for i in range(len(edges)):
            if seglist[i].get_nodes()[0]==skeleton.nodes[edges[i][0]]:
                directionlist.append(1)
            else:
                directionlist.append(-1)
        skelcontext.createNonsequenceableEdgeBoundary(name, seglist,
                                                      directionlist,
                                                      exterior, autoselect=0)

    # autoselect=0 prevents the boundary from being selected in the
    # skelcontext. Selection shouldn't happen except by explicit user
    # action.

    
skelmenu.addItem(OOFMenuItem(
    'EdgeBoundary',
    callback=_loadEdgeBoundary,
    params=[
    whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                          tip=parameter.emptyTipString),
    parameter.StringParameter('name', tip="Name of Edge Boundary."),
    parameter.ListOfTuplesOfIntsParameter('edges',
                                          tip="List of Edges -- tuple of two nodes."),
    parameter.IntParameter('exterior', 0, tip="1 (true) for the exterior boundary and 0 (false) for otherwise.")],
    help="Load Edge Boundary. Used internally in data files.",
    discussion="<para>Load a <link linkend='Section-Concepts-Skeleton-Boundary-Edge'><classname>EdgeBoundary</classname></link> from a Skeleton data file.</para>"
    ))

######

def _loadNodeGroup(menuitem, skeleton, name, nodes):
##    debug.fmsg()
    # nodes is a list of integer indices into skeleton.nodes.
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    groupset = skelcontext.nodegroups
    groupset.addGroup(name)
    groupset.addToGroup(**{name : [skeleton.nodes[i] for i in nodes]})

skelmenu.addItem(OOFMenuItem(
    'NodeGroup',
    callback=_loadNodeGroup,
    params=[
    whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                          tip=parameter.emptyTipString),
    parameter.StringParameter('name', tip="Name for the node group."),
    parameter.ListOfIntsParameter('nodes', tip="List of node indices.")],
    help="Load Node Group. Used internally in data files.",
    discussion="<para>Load a node <link linkend='Section-Concepts-Skeleton-Groups'>group</link>.</para>"
    ))

def _loadElementGroup(menuitem, skeleton, name, elements):
##    debug.fmsg()
    # elements is a list of integer indices into skeleton.elements.
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    groupset = skelcontext.elementgroups
    groupset.addGroup(name)
    groupset.addToGroup(**{name : [skeleton.elements[i] for i in elements]})

skelmenu.addItem(OOFMenuItem(
    'ElementGroup',
    callback=_loadElementGroup,
    params=[
    whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                          tip=parameter.emptyTipString),
    parameter.StringParameter('name', tip="Name for the element group."),
    parameter.ListOfIntsParameter('elements', tip="List of element indices")],
    help="Load Element Group. Used internally in data files.",
    discussion="<para>Load an element <link linkend='Section-Concepts-Skeleton-Groups'>group</link>.</para>"
    ))

def _loadSegmentGroup(menuitem, skeleton, name, segments):
##    debug.fmsg()
    # segments is a list of tuples of integer indices into skeleton.nodes.
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    skeleton = skelcontext.getObject()
    groupset = skelcontext.segmentgroups
    groupset.addGroup(name)
    groupset.addToGroup(**{name : [skeleton.getSegment(skeleton.nodes[i],
                                                       skeleton.nodes[j])
                                   for (i,j) in segments]})

skelmenu.addItem(OOFMenuItem(
    'SegmentGroup',
    callback=_loadSegmentGroup,
    params=[
    whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                          tip=parameter.emptyTipString),
    parameter.StringParameter('name', tip="Name for the segment group."),
    parameter.ListOfTuplesOfIntsParameter('segments', tip="List of segments -- tuple of two node indices.")],
    help="Load Segment Group. Used internally in data files.",
    discussion="<para>Load a segment <link linkend='Section-Concepts-Skeleton-Groups'>group</link>.</para>"
    ))

def _addMaterialToElementGroup(menuitem, skeleton, group, material):
    skelcontext = skeletoncontext.skeletonContexts[skeleton]
    groupset = skelcontext.elementgroups
    groupset.assignMaterial(group, materialmanager.getMaterial(material))

skelmenu.addItem(OOFMenuItem(
    'AddMaterialToGroup',
    callback=_addMaterialToElementGroup,
    params=[
        whoville.WhoParameter('skeleton', skeletoncontext.skeletonContexts,
                              tip=parameter.emptyTipString),
        parameter.StringParameter('group', tip="Name of the element group"),
        parameter.StringParameter('material', tip="Name of the material.")],
    help="Add a Material to an Element Group.  Used internally in data files.",
    discussion="<para>Add a Material to an Element Group.</para>"    
    ))

#############

def writeSkeleton(datafile, skelcontext):
    skelcontext.begin_reading()
    try:
        skeleton = skelcontext.getObject()
        skelpath = skelcontext.path()

        # Create skeleton.
        datafile.startCmd(skelmenu.NewPeriodic)
        datafile.argument('name', skelcontext.name())
        datafile.argument('microstructure', skeleton.MS.name())
        datafile.argument('left_right_periodicity', skeleton.left_right_periodicity)
        datafile.argument('top_bottom_periodicity', skeleton.top_bottom_periodicity)
        if config.dimension() == 3:
            datafile.argument('front_back_periodicity', skeleton.front_back_periodicity)            
        datafile.endCmd()

        # Define nodes.
        datafile.startCmd(skelmenu.Nodes)
        datafile.argument('skeleton', skelpath)
        if config.dimension()==2:
            datafile.argument('points', [(nd.position().x, nd.position().y)
                                         for nd in skeleton.nodes])
        elif config.dimension()==3:
            datafile.argument('points', [(nd.position().x, nd.position().y, nd.position().z)
                                         for nd in skeleton.nodes])
        datafile.endCmd()

        # Nodes are written and read in the order in which they're stored
        # in the Skeleton's nodes list.  This is not the same as the
        # nodes' internal index, so we need to create a dictionary of
        # indices in the nodes list so that the elements' node tuples are
        # correct.
        nodedict = {}
        c = 0
        for node in skeleton.nodes:
            nodedict[node] = c
            c += 1
        # same for elements
        elementdict = {}
        c = 0
        for element in skeleton.elements:
            elementdict[element] = c
            c += 1

        # Write node partnerships using the node indices in nodedict
        if skeleton.left_right_periodicity or skeleton.top_bottom_periodicity \
               or (config.dimension()==3 and skeleton.front_back_periodicity):
            partners = []
            for node in skeleton.nodes:
                nodeno = nodedict[node]
                partnernos = [nodedict[n] for n in node.getPartners()]
                # Only save nontrivial partnerships, and only save
                # each set of partners once.  Partnerships are saved
                # as a tuple of node indices.  Order is unimportant.
                if partnernos and nodeno < min(partnernos):
                    partners.append(tuple([nodeno] + partnernos))
            datafile.startCmd(skelmenu.Partnerships)
            datafile.argument('skeleton', skelpath)
            datafile.argument('partnerlists', partners)
            datafile.endCmd()

        # Define elements, using the node indices in nodedict.
        datafile.startCmd(skelmenu.Elements)
        datafile.argument('skeleton', skelpath)
        datafile.argument('nodes', [tuple([nodedict[node] for node in el.nodes])
                                    for el in skeleton.elements])
        datafile.endCmd()


        # we don't have groups and boundaries set up in 3d yet.
        # TODO 3D: enable this in 3d when needed
        if config.dimension() == 2:
            # Node groups
            for group in skelcontext.nodegroups.groups:
                datafile.startCmd(skelmenu.NodeGroup)
                datafile.argument('skeleton', skelpath)
                datafile.argument('name', group)
                datafile.argument(
                    'nodes', 
                    [nodedict[node]
                     for node in skelcontext.nodegroups.get_group(group)])
                datafile.endCmd()

            # Element groups
            for group in skelcontext.elementgroups.groups:
                datafile.startCmd(skelmenu.ElementGroup)
                datafile.argument('skeleton', skelpath)
                datafile.argument('name', group)
                datafile.argument(
                    'elements',
                    [elementdict[el]
                     for el in skelcontext.elementgroups.get_group(group)])
                datafile.endCmd()

            for group in skelcontext.segmentgroups.groups:
                datafile.startCmd(skelmenu.SegmentGroup)
                datafile.argument('skeleton', skelpath)
                datafile.argument('name', group)
                nodepairs = [
                    seg.nodes()
                    for seg in skelcontext.segmentgroups.get_group(group)]
                datafile.argument(
                    'segments',
                    [(nodedict[n1], nodedict[n2]) for (n1, n2) in nodepairs])
                datafile.endCmd()

            # Materials assigned to Element Groups.  If a Material
            # isn't assigned to pixels in the Microstructure, be sure
            # to save the Material's definition first.
            msmatls = ooflib.SWIG.engine.material.getMaterials(skeleton.MS)
            groupmats = skelcontext.elementgroups.getAllMaterials()
            # skelmatls is a list of Materials used in the Skeleton
            # that aren't in the Microstructure.
            skelmatls = [m for (g, m) in groupmats if m not in msmatls]
            # Construct a list of Properties already defined in the
            # data file, so that they're not written twice.
            excludeProps = {}
            for mat in msmatls:
                for prop in mat.properties:
                    excludeProps[prop.registration().name()] = prop
            materialmenu.writeMaterials(datafile, skelmatls, excludeProps)
            # Now assign Materials to Groups.
            for group, material in groupmats:
                datafile.startCmd(skelmenu.AddMaterialToGroup)
                datafile.argument('skeleton', skelpath)
                datafile.argument('group', group)
                datafile.argument('material', material.name())
                datafile.endCmd()

            # Pinned nodes
            datafile.startCmd(skelmenu.PinnedNodes)
            datafile.argument('skeleton', skelpath)
            datafile.argument(
                'nodes',
                [nodedict[node] for node in skelcontext.pinnednodes.retrieve()])
            datafile.endCmd()

        # Point boundaries
        # sort keys to print in a consistent order
        sortedKeys = sorted(skeleton.pointboundaries.keys())
        for pbname in sortedKeys:
            pbdy = skeleton.pointboundaries[pbname]
            datafile.startCmd(skelmenu.PointBoundary)
            datafile.argument('skeleton', skelpath)
            datafile.argument('name', pbname)
            datafile.argument('nodes', [nodedict[node] for node in pbdy.nodes])
            exterior = 0
            if isinstance(pbdy, skeletonboundary.ExteriorSkeletonPointBoundary):
                exterior = 1
            datafile.argument('exterior', exterior)
            datafile.endCmd()

        # Edge boundaries
        # sort keys to print in a consistent order
        sortedKeys = sorted(skeleton.edgeboundaries.keys())
        for ebname in sortedKeys:
            ebdy = skeleton.edgeboundaries[ebname]
            datafile.startCmd(skelmenu.EdgeBoundary)
            datafile.argument('skeleton', skelpath)
            datafile.argument('name', ebname)
            #Interface branch
            if ebdy._sequenceable:
                edgeset = rearrangeEdges([
                    tuple([nodedict[x] for x in edge.get_nodes()])
                    for edge in ebdy.edges
                    ])
            else:
                edgeset = [
                    tuple([nodedict[x] for x in edge.get_nodes()])
                    for edge in ebdy.edges
                    ]
            datafile.argument('edges', edgeset)
            exterior = 0
            if isinstance(ebdy, skeletonboundary.ExteriorSkeletonEdgeBoundary):
                exterior = 1
            datafile.argument('exterior', exterior)
            datafile.endCmd()

            #Interface branch
            interfacematname=skelcontext.getBoundary(ebname)._interfacematerial
            if interfacematname is not None:
                datafile.startCmd(OOF.LoadData.Material.Interface.Assign)
                datafile.argument('microstructure',skeleton.MS.name())
                datafile.argument('material',interfacematname)
                datafile.argument('interfaces',[skelcontext.name()+":"+ebname])
                datafile.endCmd()

    finally:
        skelcontext.end_reading()

###########################################################

# A function to put edges in a right order.
def rearrangeEdges(edges):
    # 'edges' is a list of tuples of integers.  Each tuple is an edge,
    # and each integer is a node index (from nodedict in
    # writeSkeleton, above).
    if len(edges) == 1:
        return edges

    # Construct dictionaries of edges keyed by their starting and end points.
    tails = {}           
    heads = {}
    minedge = 0                 # which edge starts at the min node index
    for i, edge in enumerate(edges):
        heads[edge[0]] = edge
        tails[edge[1]] = edge
        if edge[0] < edges[minedge][0]:
            minedge = i

    # Start with the edge with the lowest index at its start point.
    # This has no effect on the result unless the edges form a loop.
    # If they do form a loop, differences in the order of the items in
    # the given edges list will affect the order of the edges in the
    # saved file, and that can cause the test suite to fail.  The
    # order of the items in the edges list depends on the order in
    # which they're retrieved from a Python set, and can vary with the
    # Python version.
    newedges = [edges[minedge]]

    # Build the list of contiguous edges going backwards from the
    # start point of edges[minedge].  This loop exits when either it runs
    # out of tails and throws a key error, or when it loops back on
    # itself and the conditional fails.
    lastpt = edges[minedge][0]
    try:
        ## TODO: This is doing a linear search, since newedges is a
        ## list.  It would be better to remove items from heads and
        ## tails as they're used, and stop when a connecting edge
        ## isn't found.  It's probably not a high priority
        ## optimization, though.  Boundaries aren't that big.
        while tails[lastpt] not in newedges:
            nextedge = tails[lastpt]
            newedges.append(nextedge)
            lastpt = nextedge[0]

    except KeyError:
        pass

    newedges.reverse()

    # Extend the list of contiguous edges going forwards from the end
    # point of edges[0].  If the previous block found a loop, then
    # this block's while-conditional will fail, and it will do
    # nothing.
    lastpt = edges[minedge][1]
    try:
        while heads[lastpt] not in newedges:
            nextedge = heads[lastpt]
            newedges.append(nextedge)
            lastpt = nextedge[1]
    except KeyError:
        pass

    return newedges


#TODO: May need to be updated for interfaces. Don't know yet how abaqus
#handles adjacent elements that don't share a node.
##########
# ABAQUS #
##########

import datetime

def writeABAQUSfromSkeleton(filename, mode, skelcontext):
    skelcontext.begin_reading()
    try:
        skeleton = skelcontext.getObject()

        buffer="*HEADING\nABAQUS-style file created by OOF2 on %s from a skeleton " % (datetime.datetime.today())
        buffer+="of the microstructure %s.\n" % skeleton.MS.name()

        # Build dictionary (instead of using index()) for elements and nodes
        #  as was done in previous writeXXX() methods
        nodedict = {}
        i = 1
        for node in skeleton.nodes:
            nodedict[node] = i
            i += 1
        # same for elements
        elementdict = {}
        i = 1
        for el in skeleton.elements:
            elementdict[el] = i
            i += 1

        debug.fmsg("made dicts")
        
        # Collect elements with the same dominant material together in a
        #  dictionary, with a key given by the material name.
        #  Some elements may not have a material assigned and
        #  these should not be included in the dictionary(?). Have a feeling
        #  something like this has been done in the OOF universe.
        materiallist={}
        elementlist={}
        for el in skeleton.elements:
            matl = el.material(skelcontext)
            if matl:
                matname = matl.name()
                # Steve's suggestion
                elindex = elementdict[el]
                try:
                    elementlist[matname].append(elindex)
                except KeyError:
                    elementlist[matname] = [elindex]
                    materiallist[matname] = el.material(skelcontext)
        debug.fmsg("made materiallist and elementlist")

        buffer+="** Materials defined by OOF2:\n"
        for matname, details in materiallist.items():
            buffer+="**   %s:\n" % (matname)
            for prop in details.properties:
                for param in prop.registration().params:
                    buffer+="**     %s: %s\n" % (param.name,param.value)
        debug.fmsg("wrote materials")

        buffer+="** Notes:\n**   The nodes for a skeleton are always located at vertices or corners.\n"
        buffer+="**   More information may be obtained by saving ABAQUS from a mesh.\n"

        listbuf=["*NODE\n"]
        for node in skeleton.nodes:
            listbuf.append("%d, %s, %s\n" % (nodedict[node],node.position().x,node.position().y))
        buffer+=stringjoin(listbuf,"")

        # Only expecting 3 or 4 noded skeleton elements
        for numnodes in [3,4]:
            listbuf=["** The element type provided for ABAQUS is only a guess " \
                     "and may have to be modified by the user to be meaningful.\n*ELEMENT, TYPE=CPS%d\n" % numnodes]
            for el in skeleton.elements:
                if el.nnodes()==numnodes:
                    listbuf2=["%d" % (elementdict[el])]
                    for node in el.nodes:
                        listbuf2.append("%d" % (nodedict[node]))
                    listbuf.append(stringjoin(listbuf2,", ")+"\n")
            if len(listbuf)>1:
                buffer+=stringjoin(listbuf,"")

        debug.fmsg("wrote elements")

        # Sort groups for reproducibility in tests.
        grpnames = list(skelcontext.nodegroups.groups)
        grpnames.sort()
        for group in grpnames:
            buffer+="*NSET, NSET=%s\n" % (group)
            listbuf=[]
            i=0
            for node in skelcontext.nodegroups.get_group(group):
                if i>0 and i%16==0:
                    listbuf.append("\n%d" % (nodedict[node]))
                else:
                    listbuf.append("%d" % (nodedict[node]))
                i+=1
            buffer+=stringjoin(listbuf,", ")+"\n"
        debug.fmsg("wrote node groups")

        grpnames = list(skelcontext.elementgroups.groups)
        grpnames.sort()
        for elgroup in grpnames:
            buffer+="*ELSET, ELSET=%s\n" % (elgroup)
            listbuf=[]
            i=0
            for el in skelcontext.elementgroups.get_group(elgroup):
                if i>0 and i%16==0:
                    listbuf.append("\n%d" % (elementdict[el]))
                else:
                    listbuf.append("%d" % (elementdict[el]))
                i+=1
            buffer+=stringjoin(listbuf,", ")+"\n"
        debug.fmsg("wrote element groups")

        grps = list(skeleton.pointboundaries.items())
        grps.sort()
        buffer+="** Include point and edge boundaries from OOF2.\n"
        for pbname, pbdy in grps:
            buffer+="*NSET, NSET=%s\n" % (pbname)
            listbuf=[]
            i=0
            for node in pbdy.nodes:
                if i>0 and i%16==0:
                    listbuf.append("\n%d" % (nodedict[node]))
                else:
                    listbuf.append("%d" % (nodedict[node]))
                i+=1
            buffer+=stringjoin(listbuf,", ")+"\n"
        debug.fmsg("wrote boundaries")

        # Use rearrangeEdges() to chain the edges together, then pick the
        #  unique nodes. It seems the edges can't be selected if they
        #  are empty, so edgeset=[(a,b),(b,c),...] is not checked
        #  for null content
        bdys = list(skeleton.edgeboundaries.items())
        bdys.sort()
        for ebname, ebdy in bdys:
            edgeset = rearrangeEdges([
                tuple([nodedict[node] for node in edge.get_nodes()])
                for edge in ebdy.edges
                ])
            buffer+="*NSET, NSET=%s\n" % (ebname)
            listbuf=["%d" % edgeset[0][0]]
            i=1
            for edge in edgeset:
                if i%16==0:
                    listbuf.append("\n%d" % (edge[1]))
                else:
                    listbuf.append("%d" % (edge[1]))
                i+=1
            buffer+=stringjoin(listbuf,", ")+"\n"

        for matname in materiallist:
            buffer+="*ELSET, ELSET=%s\n" % matname
            listbuf=[]
            i=0
            for elindex in elementlist[matname]:
                if i>0 and i%16==0:
                    listbuf.append("\n%d" % (elindex))
                else:
                    listbuf.append("%d" % (elindex))
                i+=1
            buffer+=stringjoin(listbuf,", ")+"\n*SOLID SECTION, ELSET=%s, MATERIAL=%s\n" % (matname,matname)
        debug.fmsg("wrote material elsets")
            
        for matname in materiallist:
            buffer+="*MATERIAL, NAME=%s\n** Use the information in the header to complete these fields under MATERIAL\n" % matname

        # Save/Commit to file. Perhaps should be done outside the current method
        debug.fmsg("opening file")
        fp=open(filename,mode)
        debug.msg("writing buffer")
        fp.write(buffer)
        debug.fmsg("done writing buffer")
        fp.close()
    finally:
        skelcontext.end_reading()
