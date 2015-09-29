# -*- python -*-
# $RCSfile: meshmod.py,v $
# $Revision: 1.23 $
# $Author: langer $
# $Date: 2011/04/29 20:22:42 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Mesh modification operations.  There shouldn't be too many of these,
# since most modifications are performed on a Skeleton instead.

from ooflib.SWIG.common import switchboard
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import materialmanager
from ooflib.engine import meshstatus
from ooflib.engine import skeletoncontext
from ooflib.engine.IO import materialmenu
from ooflib.engine.IO import materialparameter
from ooflib.engine.IO import skeletongroupparams

##############

# class MeshModTargets(registeredclass.RegisteredClass):
#     registry = []
#     tip = "Target elements for Mesh modification."
#     discussion = """<para>
#     Objects in the <classname>MeshModTargets</classname> class are
#     used as the <varname>target</varname> argument of <xref
#     linkend='RegisteredClass-MeshModification'/> subclasses. They
#     specify to which &mesh; elements a modification applies.
#     </para>"""

# class AllMeshElements(MeshModTargets):
#     def __call__(self, meshcontext):
#         els = []
#         iter = meshcontext.getObject().element_iterator()
#         while not iter.end():
#             els.append(iter.element())
#             iter.next()
#         return els

# registeredclass.Registration(
#     'All Elements',
#     MeshModTargets,
#     AllMeshElements,
#     ordering=0,
#     tip="Operate on all Mesh elements",
#     discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/all_elements.xml')
#     )
                             
# class SelectedMeshElements(MeshModTargets):
#     def __call__(self, meshcontext):
#         mesh = meshcontext.getObject()
#         skel = meshcontext.skeleton
#         skelcontext = skeletoncontext.skeletonContexts[
#             skeletoncontext.extractSkeletonPath(meshcontext.path())]
#         elements = skelcontext.elementselection.retrieveFromSkeleton(skel)
#         return [mesh.getElement(el.meshindex) for el in elements]

# registeredclass.Registration(
#     'Selected Elements',
#     MeshModTargets,
#     SelectedMeshElements,
#     ordering=1,
#     tip="Operate on Mesh elements that are selected in the corresponding Skeleton.",
#     discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/selected_elements.xml')
#     )

# class MeshElementGroup(MeshModTargets):
#     def __init__(self, group):
#         self.group = group
#     def __call__(self, meshcontext):
#         mesh = meshcontext.getObject()
#         skel = meshcontext.skeleton
#         skelcontext = skeletoncontext.skeletonContexts[
#             skeletoncontext.extractSkeletonPath(meshcontext.path())]
#         elements = skelcontext.elementgroups.get_groupFromSkeleton(self.group,
#                                                                    skel)
#         return [mesh.getElement(el.meshindex) for el in elements]

# registeredclass.Registration(
#     'Element Group',
#     MeshModTargets,
#     MeshElementGroup,
#     ordering=2,
#     params=[
#     skeletongroupparams.ElementGroupParameter('group',
#                                               tip='Assign the Material to elements in this group.')
#     ],
#     tip="Operate on Mesh elements in a given element group.",
#     discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/element_group.xml'))
                      

###############
    
class MeshModification(registeredclass.RegisteredClass):
    registry = []
    # Subclasses must define an "apply" function.
    # Also, if a Subclass needs a different type of progress bar,
    # it should be overridden.
    def get_progressbar_type(self):
        return "continuous"
    # setStatus and signal are called after the modifier is applied.
    # They should set the mesh status and send the appropriate
    # switchboard signals.
    def setStatus(self, meshcontext):
        pass
    def signal(self, meshcontext):
        pass

    tip = "Tools to modify a Mesh."
    discussion = """<para>
    <classname>MeshModification</classname> objects modify &meshes;.
    They are used as the <varname>modifier</varname> argument of the
    <xref linkend='MenuItem-OOF.Mesh.Modify'/> command.
    </para>"""


class RebuildMesh(MeshModification):
    def apply(self, meshcontext):
        meshcontext.rebuildMesh()
    def signal(self, meshcontext):
        switchboard.notify("mesh changed", meshcontext)
        switchboard.notify("mesh boundaries changed", meshcontext.getObject())
        switchboard.notify("redraw")
    def setStatus(self, meshcontext):
        meshcontext.setStatus(meshstatus.Unsolved("Rebuilt"))

registeredclass.Registration(
    'Rebuild',
    MeshModification,
    RebuildMesh,
    ordering=1,
    tip="Rebuild a Mesh after its Skeleton has changed.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/engine/reg/rebuildmesh.xml")
    )
