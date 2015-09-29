# -*- python -*-
# $RCSfile: boundarymodifier.py,v $
# $Revision: 1.18 $
# $Author: langer $
# $Date: 2010/12/02 21:09:25 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# This file defines registered class objects which actually
# build boundaries.   Structure is similar to skeletonselectionmod.

from ooflib.SWIG.common import ooferror
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import placeholder
from ooflib.common.IO import xmlmenudump
from ooflib.engine import skeletonsegment # for the segSequence function.
from ooflib.engine.IO import skeletongroupparams


# Classes for adding or removing points or segments from a skeleton
# boundary.  These are separated out according to the type of boundary
# they work on, so that the UI can present them in a sensible way.
        

class BoundaryModifier(registeredclass.RegisteredClass):
    registry = []
    tip = "Tools to modify Skeleton boundaries."
    discussion = """<para>
    <classname>BoundaryModifiers</classname> are used as the
    <varname>modifier</varname> parameter in <xref
    linkend='MenuItem-OOF.Skeleton.Boundary.Modify'/>.  They make
    changes in a &skel; <link
    linkend='Section-Concepts-Skeleton-Boundary'>boundary</link>.
    </para>"""



class PointBoundaryModifier(BoundaryModifier):
    pass

class EdgeBoundaryModifier(BoundaryModifier):
    pass


# This class's init automatically determines the subclass of
# the boundary, and records it.  The provided subclass must be a
# subclass of a known type.
class BoundaryModifierRegistration(registeredclass.Registration):
    def __init__(self, name, regclass,
                 ordering, params=[], secret=0, tip=None,
                 **kwargs):
        registeredclass.Registration.__init__(self, name, BoundaryModifier,
                                              regclass, ordering,
                                              params=params, secret=secret,
                                              tip=tip, **kwargs)
        if issubclass(regclass, PointBoundaryModifier):
            self.modifiertype = PointBoundaryModifier
        elif issubclass(regclass, EdgeBoundaryModifier):
            self.modifiertype = EdgeBoundaryModifier
        else:
            raise ooferror.ErrPyProgrammingError(
                "Attempt to register unknown type of boundary modifier.")


# Special parameter so we can have a special widget.
class BoundaryModifierParameter(parameter.RegisteredParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        parameter.RegisteredParameter.__init__(
            self, name, BoundaryModifier, value=value,
            default=default, tip=tip)

# ## ### #### ##### ###### ####### ######## ####### ###### ##### #### ### ## #

# Special parameter class, so we can have a context-aware widget which
# will only be valid for legal operations.
class BdyModSegmentAggregateParameter(
    skeletongroupparams.SegmentAggregateParameter):
    pass

# Modifier that adds selected segments (from a group or selection) to
# the indicated boundary.  Obviously this will fail if the boundary is
# not an edge boundary.
class AddSegments(EdgeBoundaryModifier):
    def __init__(self, group):
        self.group = group
        
    def attempt(self, skelcontext, boundary):
        skelobj = skelcontext.getObject()

        if self.group == placeholder.selection:
            seg_set = skelcontext.segmentselection.retrieve()
        else:
            seg_set = skelcontext.segmentgroups.get_group(self.group)

        return skelcontext.try_appendSegstoBdy(boundary, seg_set)

        
    def __call__(self, skelcontext, boundary):
        skelobj = skelcontext.getObject()

        if self.group == placeholder.selection:
            seg_set = skelcontext.segmentselection.retrieve()
        else:
            seg_set = skelcontext.segmentgroups.get_group(self.group)
        
        skelcontext.appendSegstoBdy(boundary, seg_set)

BoundaryModifierRegistration(
    "Add segments",
    AddSegments,
    ordering=200,
    params=[BdyModSegmentAggregateParameter('group',
                         tip="The segments to add to the boundary.")],
    tip="Add a set of segments to an existing edge boundary.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/add_segments.xml'))



class RemoveSegments(EdgeBoundaryModifier):
    def __init__(self, group):
        self.group = group

    def attempt(self, skelcontext, boundary):
        skelobj = skelcontext.getObject()
        
        if self.group == placeholder.selection:
            seg_set = skelcontext.segmentselection.retrieve()
        else:
            seg_set = skelcontext.segmentgroups.get_group(self.group)
          
        return skelcontext.try_removeSegsfromBdy(boundary, seg_set)

        
    def __call__(self, skelcontext, boundary):
        skelobj = skelcontext.getObject()

        if self.group == placeholder.selection:
            seg_set = skelcontext.segmentselection.retrieve()
        else:
            seg_set = skelcontext.segmentgroups.get_group(self.group)
          
        skelcontext.removeSegsfromBdy(boundary, seg_set)

BoundaryModifierRegistration(
    "Remove segments",
    RemoveSegments,
    ordering=201,
    params=[BdyModSegmentAggregateParameter('group',
                              tip="The segments to remove from the boundary")],
    tip="Remove a set of segments from an existing boundary.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/remove_segments.xml')
    )

class ReverseBoundary(EdgeBoundaryModifier):
    def __call__(self, skelcontext, boundary):
        skelcontext.reverseBoundary(boundary)

BoundaryModifierRegistration(
    "Reverse direction",
    ReverseBoundary,
    ordering=202,
    tip="Reverse the direction of an edge boundary.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/reverse_bdy.xml')
    )
        
# Modifier for adding nodes from a group or the selection to a point boundary.
class AddNodes(PointBoundaryModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skelcontext, boundary):
        skelobj = skelcontext.getObject()

        if self.group == placeholder.selection:
            node_set = skelcontext.nodeselection.retrieve()
        else:
            node_set = skelcontext.nodegroups.get_group(self.group)

        skelcontext.addNodestoBdy(boundary, node_set)

BoundaryModifierRegistration(
    "Add nodes",
    AddNodes,
    ordering=302,
    params=[skeletongroupparams.NodeAggregateParameter('group',
                                   tip="The nodes to add to the boundary.")],
    tip="Add a set of nodes to an existing point boundary.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/add_nodes.xml')
    )

class RemoveNodes(PointBoundaryModifier):
    def __init__(self, group):
        self.group = group
    def __call__(self, skelcontext, boundary):
        skelobj = skelcontext.getObject()

        if self.group == placeholder.selection:
            node_set = skelcontext.nodeselection.retrieve()
        else:
            node_set = skelcontext.nodegroups.get_group(self.group)
        
        skelcontext.removeNodesfromBdy(boundary, node_set)

BoundaryModifierRegistration(
    "Remove nodes",
    RemoveNodes,
    ordering=303,
    params=[skeletongroupparams.NodeAggregateParameter('group',
                             tip="The nodes to remove from the boundary")],
    tip="Remove a set of nodes from an existing point boundary.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/remove_nodes.xml')
    )

