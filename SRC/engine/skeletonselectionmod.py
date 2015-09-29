# -*- python -*-
# $RCSfile: skeletonselectionmod.py,v $
# $Revision: 1.84 $
# $Author: langer $
# $Date: 2013/11/07 20:51:11 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.common import pixelgroup
from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import pixelgroupparam
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
if config.dimension() == 2:
    from ooflib.engine import skeletonelement
from ooflib.engine.IO import materialparameter
from ooflib.engine.IO import pbcparams
from ooflib.engine.IO import skeletongroupparams
import random
import types
#Interface branch
from ooflib.engine.IO import interfaceparameters

# TODO LATER: Can the Segment/Element/Node operations here all be derived
# from common SkeletonSelectable classes?

# The way this is going to work is that there will be One True Menu
# for nodeselectionmodifiers, segmentselectionmodifers, and
# elementselectionmodifiers, and each of these registered classes will
# add itself to the menu, taking as an argument the relevant
# skeletoncontext.  It will then operate on the skeletoncontext in the
# usual way.

# This is the function that actually runs a selection modification.
# It is the menu callback for the automatically-generated menu
# items in engine/IO/skeletonselectmenu.py.  This one routine
# works for node, segment, and element selections.

def modify(menuitem, skeleton, **params):
    registration = menuitem.data
    modifier = registration(**params)
    skelcontext = whoville.getClass('Skeleton')[skeleton]
    selection = modifier.getSelection(skelcontext)
    selection.begin_writing()
    try:
        modifier(skelcontext, selection)
    finally:
        selection.end_writing()

    selection.mode().modifierApplied(modifier) # sends switchboard signal
    selection.signal()

###########################################

class NodeSelectionModifier(registeredclass.RegisteredClass):
    registry = []
    def getSelection(self, skelcontext):
        return skelcontext.nodeselection

#######################
    
class NodeFromSelectedSegments(NodeSelectionModifier):
    def __call__(self, skeleton, selection):
        nodes = {}
        for segment in skeleton.segmentselection.retrieve():
            nodes[segment.nodes()[0]] = None
            nodes[segment.nodes()[1]] = None
        selection.start()
        selection.clear()
        selection.select(nodes.keys())

registeredclass.Registration('Select from Selected Segments',
                             NodeSelectionModifier,
                             NodeFromSelectedSegments, ordering=0.1,
                             tip="Select nodes from selected segments.",
                             discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/nodes_from_segments.xml'))

#######################

class NodeFromSelectedElements(NodeSelectionModifier):
    def __init__(self, internal=0, boundary=1):
        self.internal = internal
        self.boundary = boundary

    def getAllNodes(self, context):
        nodes = set()
        for element in context.elementselection.retrieve():
            for nd in element.nodes:
                nodes.add(nd)
        return list(nodes)      # TODO: Leave as a set?

    def getBoundaryNodes(self, context):
        # A segment is on the boundary of the selection if it
        # belongs to only one selected element.
        skel = context.getObject()
        segdict = {}   # counts how many times each segment has been seen
        for element in context.elementselection.retrieve():
            for i in range(element.nnodes()):
                n0 = element.nodes[i]
                n1 = element.nodes[(i+1)%element.nnodes()]
                seg = skel.findSegment(n0, n1)
                segdict[seg] = segdict.get(seg, 0) + 1
        bdysegs = [seg for seg,count in segdict.items() if count == 1]
        nodes = set()
        for seg in bdysegs:
            segnodes = seg.nodes()
            nodes.add(segnodes[0])
            nodes.add(segnodes[1])
        return list(nodes)      # TODO: Leave as a set?

    def getInternalNodes(self, context, allnodes):
        bound = self.getBoundaryNodes(context)
        internal = []
        for nd in allnodes:
            if nd not in bound:
                internal.append(nd)
        return internal

    def __call__(self, skeleton, selection):
        if self.internal and self.boundary:
            selected = self.getAllNodes(skeleton)
        elif not self.internal and self.boundary:
            selected = self.getBoundaryNodes(skeleton)
        elif self.internal and not self.boundary:
            allnodes = self.getAllNodes(skeleton)
            selected = self.getInternalNodes(skeleton, allnodes)
        else:
            selected = []
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration('Select from Selected Elements',
                             NodeSelectionModifier,
                             NodeFromSelectedElements, ordering=1,
                             params = [
    parameter.BooleanParameter('internal', 0, tip='Select interior nodes?'),
    parameter.BooleanParameter('boundary', 1, tip='Select exterior nodes?')],
                             tip="Select nodes from selected elements.",
                             discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/nodes_from_elements.xml'))

#######################

class SelectInternalBoundaryNodes(NodeSelectionModifier):
    def __init__(self, ignorePBC=False):
        self.ignorePBC = ignorePBC
    def __call__(self, skeleton, selection):
        skel = skeleton.getObject()
        nodelist = []
        for node in skel.nodes:
            if self.ignorePBC:
                elements = node.aperiodicNeighborElements()
            else:
                elements = node.neighborElements()
            cat = elements[0].dominantPixel(skel.MS)
            for element in elements[1:]:
                if cat != element.dominantPixel(skel.MS):
                    nodelist.append(node)
                    break
        selection.start()
        selection.clear()
        selection.select(nodelist)
                    
registeredclass.Registration(
    'Select Internal Boundaries',
    NodeSelectionModifier, SelectInternalBoundaryNodes,
    ordering=2.5,
    params=[pbcparams.PBCBooleanParameter('ignorePBC', False,
                                          tip='Ignore periodicity?')],
    tip="Select all nodes on material or group boundaries.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/boundary_nodes.xml'))

#######################

class SelectNamedBoundaryNodes(NodeSelectionModifier):
    def __init__(self, boundary):
        self.boundary = boundary
    def __call__(self, skeleton, selection):
        bdy = skeleton.getBoundary(self.boundary)
        nodes = bdy.boundary(skeleton.getObject()).nodes
        selection.start()
        selection.clear()
        selection.select(nodes)

registeredclass.Registration(
    'Select Named Boundary',
    NodeSelectionModifier,
    SelectNamedBoundaryNodes,
    ordering=7,
    params=[skeletongroupparams.SkeletonPointBoundaryParameter('boundary',
                                     tip="Select nodes in this boundary")],
    tip="Select nodes belonging to the given skeleton point boundary.",
    discussion="""<para>

    Select all the &nodes; contained in the given &skel;
    <link linkend="Section-Concepts-Skeleton-Boundary">boundary</link>.
    The boundary must be a
    <link linkend="Section-Concepts-Skeleton-Boundary-Point">point</link>
    boundary.
    
    </para>"""
    )

#######################

class SelectPeriodicPartnerNodes(NodeSelectionModifier):
    def __call__(self, skeleton, selection):
        oldnodes = skeleton.nodeselection.retrieve()
        newnodes = set()
        for node in oldnodes:
            for p in node.getPartners():
                newnodes.add(p)
        selection.start()
        selection.select(newnodes)

registeredclass.Registration(
    'Select Periodic Partners',
    NodeSelectionModifier,
    SelectPeriodicPartnerNodes,
    ordering=8,
    tip="Select nodes whose periodic partners are already selected.",
    discussion="""<para>

    If the &skel; is
    <link linkend="Section-Concepts-Skeleton-Periodicity">periodic</link>,
    every &node; on a periodic boundary has a partner on the opposite boundary.
    This command selects the periodic partners of the currently selected
    &nodes;, without unselecting any &nodes;.

    </para>"""
    )

###########################################

class ExpandCriterion(registeredclass.RegisteredClass):
    registry = []
    def expand(self, skeleton):
        pass
    tip = "Ways of expanding the node selection."
    discussion = """<para>
    Objects of the <classname>ExpandCriterion</classname> are used as
    the <varname>criterion</varname> parameter of <xref
    linkend='MenuItem-OOF.NodeSelection.Expand_Node_Selection'/>.
    They describe different ways of expanding the set of currently
    selected &nodes; in a &skel;.
    </para>"""

class ExpandByElements(ExpandCriterion):
    def expand(self, skeleton, ignorePBC):
        # Get the current set of selected nodes
        oldnodes = set(skeleton.nodeselection.retrieve())
        # Define a function to retrieve the desired neighbor elements
        if ignorePBC:
            def elf(n):
                return n.aperiodicNeighborElements()
        else:
            def elf(n):
                return n.neighborElements()
        # Get the set of nodes of the neighbor elements.  We don't
        # bother to check for duplications, because the Set machinery
        # will do that for us.  We also don't bother to check to see
        # if an element is on the boundary of the original set of
        # nodes, because checking for boundary-ness is just as hard as
        # looping over all the nodes and putting them in the Set.
        newnodes = set()
        for node in oldnodes:
            for el in elf(node):
                newnodes.update(el.nodes)
        return oldnodes.union(newnodes)

registeredclass.Registration(
    'By Elements',
    ExpandCriterion, ExpandByElements,
    ordering=0,
    tip="Expand the node selection by selecting all nodes of neighboring elements.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/expand_by_elements.xml'))

class ExpandBySegments(ExpandCriterion):
    def expand(self, skeleton, ignorePBC):
        skel = skeleton.getObject()
        oldnodes = set(skeleton.nodeselection.retrieve())
        if ignorePBC:
            def elf(n):
                return n.aperiodicNeighborNodes(skel)
        else:
            def elf(n):
                return n.neighborNodes(skel)
        newnodes = set()
        for n in oldnodes:
            newnodes.update(elf(n))
        return oldnodes.union(newnodes)

registeredclass.Registration(
    'By Segments',
    ExpandCriterion, ExpandBySegments,
    ordering=1,
    tip="Expand the node selection by selecting all nodes of neighboring segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/expand_by_segments.xml'))
    
class ExpandNodeSelection(NodeSelectionModifier):
    def __init__(self, criterion, ignorePBC=False):
        self.criterion = criterion
        self.ignorePBC = ignorePBC
    def __call__(self, skeleton, selection):
        selected = self.criterion.expand(skeleton, self.ignorePBC)
        selection.start()
        selection.clear()
        selection.select(selected)        

registeredclass.Registration(
    'Expand Node Selection',
    NodeSelectionModifier, ExpandNodeSelection,
    ordering=2.6,
    params=[parameter.RegisteredParameter("criterion", ExpandCriterion,
                                          tip="How to select new nodes."),
            pbcparams.PBCBooleanParameter("ignorePBC", False,
                                          tip='Ignore periodicity?')
            ],
    tip="Expand node selection by either neighboring elements or segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/expand_node.xml'))

#######################

# Select the indicated group.

class NodeSelectGroup(NodeSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        # Retrieve the members first -- if an exception occurs, the
        # system state will be as before.
        members = skeleton.nodegroups.get_group(self.group)
        selection.start()
        selection.clear()
        selection.select(members)

registeredclass.Registration(
    'Select Group',
    NodeSelectionModifier,
    NodeSelectGroup,
    ordering=3,
    params=[
    skeletongroupparams.NodeGroupParameter('group', tip="Node group to select.")
    ],
    tip='Select the members of a group, discarding the current selection.',
    discussion="""<para>
    Select all the &nodes; in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link>.  The
    currently selected &nodes; will first be deselected.  To select a
    group without first deselecting, use <xref
    linkend='MenuItem-OOF.NodeSelection.Add_Group'/>.
    </para>""")

#######################

# Unselect the indicated group.

class NodeDeselectGroup(NodeSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        members = skeleton.nodegroups.get_group(self.group)
        selection.start()
        selection.deselect(members)

registeredclass.Registration(
    'Unselect Group',
    NodeSelectionModifier,
    NodeDeselectGroup,
    ordering=4,
    params=[skeletongroupparams.NodeGroupParameter('group',
                                             tip="Node group to deselect.")],
    tip='Unselect the members of a group.',
    discussion="""<para>
    Deselect all of the &nodes; that are members of the specified
    <link linkend='Section-Concepts-Skeleton-Groups'>group</link>.
    Any &nodes; that are members of the group but that are not
    currently selected will be unaffected.
    </para>""")

#######################

# Add the group to the selection, retaining the current selection.

class NodeAddSelectGroup(NodeSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        members = skeleton.nodegroups.get_group(self.group)
        selection.start()
        # Minor inefficiency, this reselects already-selected group members.
        selection.select(members)


registeredclass.Registration(
    'Add Group',
    NodeSelectionModifier,
    NodeAddSelectGroup,
    ordering=5,
    params=[skeletongroupparams.NodeGroupParameter('group',
                                                   tip="Node group to select.")
            ],
    tip='Select the members of a group, retaining the current selection.',
    discussion="""<para>
    Select all of the &nodes; in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link> in
    addition to all of the currently selected &nodes;.  To select
    <emphasis>only</emphasis> the &nodes; in a group, discarding the
    previous selection, use <xref
    linkend='MenuItem-OOF.NodeSelection.Select_Group'/>.
    </para>""")

#######################

# Select the intersection of the group and the selection.

class NodeIntersectGroup(NodeSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        nlist = skeleton.nodegroups.get_group(self.group)
        ilist = filter(lambda x: x.selected, nlist)
        selection.start()
        selection.clear()
        selection.select(ilist)

registeredclass.Registration(
    'Intersect Group',
    NodeSelectionModifier,
    NodeIntersectGroup,
    ordering=6,
    params=[skeletongroupparams.NodeGroupParameter('group',
                                                   tip="Node group to select.")
            ],
    tip='Select the intersection of a group and the current selection.',
    discussion="""<para>
    Select the &nodes; that are both in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link> and in the
    current selection.
    </para>""")


###########################################################################

# Segments.

class SegmentSelectionModifier(registeredclass.RegisteredClass):
    registry = []
    def getSelection(self, skelcontext):
        return skelcontext.segmentselection

#######################
    
class SegFromSelectedElements(SegmentSelectionModifier):
    def __init__(self, internal=0, boundary=1):
        self.internal = internal
        self.boundary = boundary

    def getAllSegments(self, context):
        segments = set()
        skel = context.getObject()
        for element in context.elementselection.retrieve():
            el_segments = element.getSegments(skel)
            for seg in el_segments:
                segments.add(seg)
#             for i in range(element.nnodes()):
#                 n0 = element.nodes[i]
#                 n1 = element.nodes[(i+1)%element.nnodes()]
#                 seg = skel.findSegment(n0, n1)
#                 segments[seg] = None
        return list(segments)   # TODO: Leave as a set?

    def getBoundarySegments(self, context):
        bound = []
        skel = context.getObject()
        for element in context.elementselection.retrieve():
            el_segments = element.getSegments(skel)
            for seg in el_segments:
#                 segments[seg] = None
#             for i in range(element.nnodes()):
#                 n0 = element.nodes[i]
#                 n1 = element.nodes[(i+1)%element.nnodes()]
#                 seg = skel.findSegment(n0, n1)
                # A segment is on the boundary of the selection if it
                # belongs to only one element.
                # TODO 3D: In 3D we'll need to get the faces that have
                # only one element, but this will have to wait until
                # we have face selections.
                n = 0
                for el in seg.getElements():
                    if el.selected: n += 1
                if n == 1:
                    bound.append(seg)
        return bound

    def getInternalSegments(self, context, allsegs):
        bound = self.getBoundarySegments(context)
        internal = []
        for seg in allsegs:
            if seg not in bound:
                internal.append(seg)
        return internal

    def __call__(self, skeleton, selection):
        if self.internal and self.boundary:
            selected = self.getAllSegments(skeleton)
        elif not self.internal and self.boundary:
            selected = self.getBoundarySegments(skeleton)
        elif self.internal and not self.boundary:
            allsegs = self.getAllSegments(skeleton)
            selected = self.getInternalSegments(skeleton, allsegs)
        else:
            selected = []
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select from Selected Elements',
    SegmentSelectionModifier,
    SegFromSelectedElements, ordering=1,
    params = [
    parameter.BooleanParameter('internal', 0, tip='Select internal segments.'),
    parameter.BooleanParameter('boundary', 1, tip='Select boundary segments.')],
    tip="Select segments from selected elements.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/segments_from_elements.xml'))

#######################

class SelectInternalBoundarySegments(SegmentSelectionModifier):
    def __init__(self, ignorePBC=False):
        self.ignorePBC = ignorePBC
    def __call__(self, skeleton, selection):
        skel = skeleton.getObject()
        seglist = []
        for segment in skel.segments.values():
            elements = segment.getElements()
            if len(elements) == 2 and elements[0].dominantPixel(skel.MS) != \
                   elements[1].dominantPixel(skel.MS):
                seglist.append(segment)
            elif not self.ignorePBC and len(elements) == 1:
                p = segment.getPartner(skel)
                if p and (p.getElements()[0].dominantPixel(skel.MS) !=
                          elements[0].dominantPixel(skel.MS)):
                    seglist.append(segment)
        selection.start()
        selection.clear()
        selection.select(seglist)

registeredclass.Registration(
    'Select Internal Boundary Segments',
    SegmentSelectionModifier,
    SelectInternalBoundarySegments,
    ordering=1.25,
    params=[pbcparams.PBCBooleanParameter("ignorePBC", value=False,
                                          tip="Ignore periodicity?")],
    tip="Select segments on material or group boundaries.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/boundary_segments.xml'))

#######################
#Interface branch
class SelectInterfaceSegments(SegmentSelectionModifier):
    def __init__(self, interface):
        self.interface = interface
    def __call__(self, skeleton, selection):
        skel = skeleton.getObject()
        interfacemsplugin=skel.MS.getPlugIn("Interfaces")
        try:
            interfacedef=interfacemsplugin.namedinterfaces[self.interface]
        except KeyError:
            #Should not happen
            raise ooferror.ErrPyProgrammingError("Interface not found!")
        seglist = []
        for segment in skel.segments.values():
            yes,side1elem=interfacedef.isInterfaceSegment(segment,skel)
            if yes:
                seglist.append(segment)
        selection.start()
        selection.clear()
        selection.select(seglist)

registeredclass.Registration(
    'Select Interface Segments',
    SegmentSelectionModifier,
    SelectInterfaceSegments,
    ordering=8,
    params=[
    interfaceparameters.InterfacesParameter('interface',
                                            tip='Select segments in this interface.')],
    tip="Select segments from an interface definition.",
    discussion="""<para>

    Select all the &sgmts; that belong to the given interface definition.
    
    </para>"""
    )

#######################

class SelectNamedBoundarySegments(SegmentSelectionModifier):
    def __init__(self, boundary):
        self.boundary = boundary
    def __call__(self, skeleton, selection):
        bdy = skeleton.getBoundary(self.boundary)
        edges = bdy.boundary(skeleton.getObject()).edges
        selection.start()
        selection.clear()
        selection.select([edge.segment for edge in edges])

registeredclass.Registration(
    'Select Named Boundary',
    SegmentSelectionModifier,
    SelectNamedBoundarySegments,
    ordering=6,
    params=[skeletongroupparams.SkeletonEdgeBoundaryParameter('boundary',
                                     tip="Select segments in this boundary")],
    tip="Select segments belonging to the given skeleton edge boundary.",
    discussion="""<para>

    Select all the &sgmts; contained in the given &skel;
    <link linkend="Section-Concepts-Skeleton-Boundary">boundary</link>.
    The boundary must be a
    <link linkend="Section-Concepts-Skeleton-Boundary-Edge">edge</link>
    boundary.
    
    </para>"""
    )

#######################

class SelectPeriodicPartnerSegments(SegmentSelectionModifier):
    def __call__(self, skeleton, selection):
        oldsegs = skeleton.segmentselection.retrieve()
        newsegs = set()
        skel = skeleton.getObject()
        for seg in oldsegs:
            partner = seg.getPartner(skel)
            if partner:
                newsegs.add(partner)
        selection.start()
        selection.select(newsegs)

registeredclass.Registration(
    'Select Periodic Partners',
    SegmentSelectionModifier,
    SelectPeriodicPartnerSegments,
    ordering=7,
    tip="Select the periodic partners of the currently selected Segments.",
    discussion="""<para>

    If the &skel; is
    <link linkend="Section-Concepts-Skeleton-Periodicity">periodic</link>,
    every &sgmt; on a periodic boundary has a partner on the opposite boundary.
    This command selects the periodic partners of the currently selected
    &sgmts;, without unselecting any &sgmts;.
    
    </para>""")

#######################

class SegmentHomogeneity(SegmentSelectionModifier):
    def __init__(self, threshold=0.9):
        self.threshold = threshold

    def __call__(self, skeleton, selection):
        selected = []
        skel = skeleton.getObject()
        for segment in skel.segment_iterator():
            if segment.homogeneity(skel.MS) < self.threshold:
                selected.append(segment)
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select by Homogeneity',
    SegmentSelectionModifier,
    SegmentHomogeneity,
    ordering=1.5,
    params = [parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.01),
                                            value=0.9,
                                            tip='The threshold homogeneity.')],
    tip="Select segments with homogeneity less than the given threshold.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/hetero_segments.xml'))

#######################

# Select the indicated group.
class SegmentSelectGroup(SegmentSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        # Group retrieval may throw an exception -- do it first.
        members = skeleton.segmentgroups.get_group(self.group)
        selection.start()
        selection.clear()
        selection.select(members)

registeredclass.Registration(
    'Select Group',
    SegmentSelectionModifier,
    SegmentSelectGroup,
    ordering=2,
    params=[skeletongroupparams.SegmentGroupParameter('group',
                                                      tip="Name of the group")],
    tip='Select the members of a group, discarding the current selection.',
    discussion="""<para>
    Select all of the &sgmts; in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link> after unselecting
     all of the currently selected &sgmts;.  To select
    <emphasis>only</emphasis> the &sgmts; in a group, retaining the
    previous selection, use <xref
    linkend='MenuItem-OOF.SegmentSelection.Add_Group'/>.
    </para>"""
)

#######################

# Unselect the indicated group.
class SegmentDeselectGroup(SegmentSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        members = skeleton.segmentgroups.get_group(self.group)
        selection.start()
        selection.deselect(members)

registeredclass.Registration(
    'Unselect Group',
    SegmentSelectionModifier,
    SegmentDeselectGroup,
    ordering=3,
    params=[
    skeletongroupparams.SegmentGroupParameter('group',
                                              tip="Segment group to select.")],
    tip='Unselect the members of a group.',
    discussion="""<para>
    Deselect all of the &sgmts; that are members of the specified
    <link linkend='Section-Concepts-Skeleton-Groups'>group</link>.
    Any &sgmts; that are members of the group but that are not
    currently selected will be unaffected.
    </para>""")

#######################

# Add the group to the selection, retaining the current selection.
class SegmentAddSelectGroup(SegmentSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        members = skeleton.segmentgroups.get_group(self.group)
        selection.start()
        selection.select(members)

registeredclass.Registration(
    'Add Group',
    SegmentSelectionModifier,
    SegmentAddSelectGroup,
    ordering=4,
    params=[
    skeletongroupparams.SegmentGroupParameter('group',
                                              tip="Segment group to select.")],
    tip='Select the members of a group, retaining the current selection.',
    discussion="""<para>
    Select all of the &sgmts; in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link> in
    addition to all of the currently selected &sgmts;.  To select
    <emphasis>only</emphasis> the &sgmts; in a group, discarding the
    previous selection, use <xref
    linkend='MenuItem-OOF.SegmentSelection.Select_Group'/>.
    </para>""")

#######################

# Select the intersection of the group and the selection.
class SegmentIntersectGroup(SegmentSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        slist = skeleton.segmentgroups.get_group(self.group)
        ilist = filter(lambda x: x.selected, slist)
        selection.start()
        selection.clear()
        selection.select(ilist)

registeredclass.Registration(
    'Intersect Group',
    SegmentSelectionModifier,
    SegmentIntersectGroup,
    ordering=5,
    params=[
    skeletongroupparams.SegmentGroupParameter('group',
                                              tip="Segment group to select.")],
    tip='Select the intersection of a group and the current selection.',
    discussion="""<para>
    Select the &sgmts; that are both in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link> and in the
    current selection.
    </para>""")

###########################################################################

# Elements

class ElementSelectionModifier(registeredclass.RegisteredClass):
    registry = []
    def getSelection(self, skelcontext):
        return skelcontext.elementselection

#######################

if config.dimension() == 2:

    class ByElementType(ElementSelectionModifier):
        def __init__(self, shape):
            self.shape = shape

        def __call__(self, skeleton, selection):
            selected = []
            for element in skeleton.getObject().element_iterator():
                if element.type() == self.shape:
                    selected.append(element)
            selection.start()
            selection.clear()
            selection.select(selected)

    registeredclass.Registration(
        'Select by Element Type',
        ElementSelectionModifier,
        ByElementType,
        ordering=1,
        params = [
        enum.EnumParameter('shape', skeletonelement.ElementShapeType,
                           skeletonelement.ElementShapeType('triangle'),
                           tip="Element shape.")],
        tip='Select elements by shape.',
        discussion="""<para>
        <command>Select_By_Element_Type</command> selects all &elems; of a
        given topology, <foreignphrase>i.e,</foreignphrase> triangular or
        quadrilateral.
        </para>""")

#######################

class ByElementMaterial(ElementSelectionModifier):
    def __init__(self, material):
        self.material = material
    def __call__(self, skeleton, selection):
        selected = []
        skel = skeleton.getObject()
        if self.material == '<Any>':
            for element in skel.element_iterator():
                if element.material(skeleton) is not None:
                    selected.append(element)
        elif self.material == '<None>':
            for element in skel.element_iterator():
                if element.material(skeleton) is None:
                    selected.append(element)
        else:
            for element in skel.element_iterator():
                matl = element.material(skeleton)
                if matl is not None and matl.name() == self.material:
                    selected.append(element)
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select by Material',
    ElementSelectionModifier,
    ByElementMaterial,
    ordering=1.5,
    params=[materialparameter.AnyMaterialParameter('material',
                                tip="Select elements with this material.")],
    tip="Select all Elements with a given Material.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/bymaterial.xml'))

#######################

class ElementHomogeneity(ElementSelectionModifier):
    def __init__(self, threshold=0.9):
        self.threshold = threshold

    def __call__(self, skeleton, selection):
        selected = []
        skel = skeleton.getObject()
        for element in skel.element_iterator():
            if element.homogeneity(skel.MS) < self.threshold:
                selected.append(element)
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select by Homogeneity',
    ElementSelectionModifier,
    ElementHomogeneity,
    ordering=2,
    params = [
    parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.01), value=0.9,
                                  tip='Threshold homogeneity.')],
    tip="Select Elements with homogeneity less than the threshold homogeneity.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/hetero_elements.xml')
    )

#######################

class ElementShapeEnergy(ElementSelectionModifier):
    def __init__(self, threshold = 0.8):
        self.threshold = threshold
    def __call__(self, skeleton, selection):
        selected = []
        for element in skeleton.getObject().element_iterator():
            if element.energyShape() > self.threshold:
                selected.append(element)
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select by Shape Energy',
    ElementSelectionModifier,
    ElementShapeEnergy,
    ordering=3,
    params = [
    parameter.FloatRangeParameter('threshold', (0.0, 1.0, 0.01), value=0.8,
                                  tip='Select Elements with shape-energy greater than this.')],
    tip="Select elements by shape-energy. The greater the shape-energy the uglier the element.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/element_by_shape.xml'))

#######################

class ElementIllegal(ElementSelectionModifier):
    def __call__(self, skeleton, selection):
        selected = []
        for element in skeleton.getObject().element_iterator():
            if element.illegal():
                selected.append(element)
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select Illegal Elements',
    ElementSelectionModifier,
    ElementIllegal,
    ordering=3.05,
    tip="Select illegal elements.",
    discussion="""  <para>
    <command>Select_Illegal_Elements</command> selects all of the
    <link
    linkend="Section-Concepts-Skeleton-Illegality">illegal</link>
    &elems; in the given &skel;.  Illegal &elems; are hard to create,
    but if they have been created somehow, this command can be useful
    in eradicating them.
    </para>"""
    )

#######################

class ElementFromSelectedNodes(ElementSelectionModifier):
    def __call__(self, skeleton, selection):
        selected = set()
        for node in skeleton.nodeselection.retrieve():
            selected.update(node.aperiodicNeighborElements())
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select from Selected Nodes',
    ElementSelectionModifier,
    ElementFromSelectedNodes,
    ordering=3.1,
    tip="Select every element containing a selected node.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/elements_from_nodes.xml'))

#######################

class ElementFromSelectedSegments(ElementSelectionModifier):
    def __call__(self, skeleton, selection):
        selected = set()
        skel = skeleton.getObject()
        for segment in skeleton.segmentselection.retrieve():
            selected.update(segment.getElements())
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select from Selected Segments',
    ElementSelectionModifier,
    ElementFromSelectedSegments,
    ordering=3.15,
    tip="Select every element adjacent to selected segments.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/elements_from_segments.xml'))

#######################

class ExpandElementSelection(ElementSelectionModifier):
    def __init__(self, ignorePBC=False):
        self.ignorePBC = ignorePBC

    def __call__(self, skeleton, selection):
        if self.ignorePBC:
            def elf(n):
                return n.aperiodicNeighborElements()
        else:
            def elf(n):
                return n.neighborElements()
        newelements = set()
        for element in selection.retrieve():
            for node in element.nodes:
                newelements.update(elf(node))
        selection.start()
        selection.clear()
        selection.select(newelements)
                
registeredclass.Registration(
    'Expand Element Selection',
    ElementSelectionModifier,
    ExpandElementSelection,
    ordering=3.2,
    params=[pbcparams.PBCBooleanParameter("ignorePBC", False,
                                          tip="Ignore periodicity?")],
    tip="Select the neighbors of the selected elements.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/menu/expand_elements.xml'))

#######################

# Select the indicated group.

class ElementSelectGroup(ElementSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        members = skeleton.elementgroups.get_group(self.group)
        selection.start()
        selection.clear()
        selection.select(members)

registeredclass.Registration(
    'Select Group',
    ElementSelectionModifier,
    ElementSelectGroup,
    ordering=4,
    params=[
    skeletongroupparams.ElementGroupParameter('group', tip="Name of the group.")
    ],
    tip='Select the members of a group, discarding the current selection.',
    discussion="""<para>
    Select all the &elems; in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link>.  The
    currently selected &elems; will first be deselected.  To select a
    group without first deselecting, use <xref
    linkend='MenuItem-OOF.ElementSelection.Add_Group'/>.
    </para>""")

#######################

# Unselect the indicated group.

class ElementDeselectGroup(ElementSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        members = skeleton.elementgroups.get_group(self.group)
        selection.start()
        selection.deselect(members)

registeredclass.Registration(
    'Unselect Group',
    ElementSelectionModifier,
    ElementDeselectGroup,
    ordering=5,
    params=[
    skeletongroupparams.ElementGroupParameter('group', tip="Name of the group.")
    ],
    tip='Unselect the members of a group.',
    discussion="""<para>
    Deselect all of the &elems; that are members of the specified
    <link linkend='Section-Concepts-Skeleton-Groups'>group</link>.
    Any &elems; that are members of the group but that are not
    currently selected will be unaffected.
    </para>""")

#######################

# Add the group to the selection, retaining the current selection.

class ElementAddSelectGroup(ElementSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        members = skeleton.elementgroups.get_group(self.group)
        selection.start()
        selection.select(members)

registeredclass.Registration(
    'Add Group',
    ElementSelectionModifier,
    ElementAddSelectGroup,
    ordering=6,
    params=[
    skeletongroupparams.ElementGroupParameter('group', tip="Name of the group.")
    ],
    tip='Select the members of a group, retaining the current selection.',
    discussion="""<para>
    Select all of the &elems; in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link> in
    addition to all of the currently selected &elems;.  To select
    <emphasis>only</emphasis> the &elems; in a group, discarding the
    previous selection, use <xref
    linkend='MenuItem-OOF.NodeSelection.Select_Group'/>.
    </para>"""
    )

#######################

# Select the intersection of the group and the selection.

class ElementIntersectGroup(ElementSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        elist = skeleton.elementgroups.get_group(self.group)
        ilist = filter(lambda x: x.selected, elist)
        selection.start()
        selection.clear()
        selection.select(ilist)


registeredclass.Registration(
    'Intersect Group',
    ElementSelectionModifier, ElementIntersectGroup,
    ordering=7,
    params=[
    skeletongroupparams.ElementGroupParameter('group', tip="Name of the group.")
    ],
    tip='Select the intersection of a group and the current selection.',
    discussion="""<para>
    Select the &elems; that are both in the given <link
    linkend='Section-Concepts-Skeleton-Groups'>group</link> and in the
    current selection.
    </para>""")

#######################

class ElementByPixelGroup(ElementSelectionModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skeleton, selection):
        selected = []
        ms = skeleton.getMicrostructure()
        skel = skeleton.getObject()
        pxlgrp = ms.findGroup(self.group)
        for element in skel.element_iterator():
            where = ms.getRepresentativePixel(element.dominantPixel(skel.MS))
            grpnames = pixelgroup.pixelGroupNames(ms, where)
            if self.group in grpnames:
                selected.append(element)
        selection.start()
        selection.clear()
        selection.select(selected)

registeredclass.Registration(
    'Select by Pixel Group',
    ElementSelectionModifier,
    ElementByPixelGroup,
    ordering=8,
    params=[pixelgroupparam.PixelGroupParameter('group',
                                                tip='The name of a pixel group.')],
    tip="Select all Elements whose dominant pixel is in a given pixel group.",
    discussion="""<para>

    This command selects all &skel; &elems; whose
    <link linkend="Section-Concepts-Skeleton-Homogeneity">dominant pixel</link>
    is a member of the given &pixelgroup;.

   </para>""")

