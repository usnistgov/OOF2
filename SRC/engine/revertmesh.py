# -*- python -*-
# $RCSfile: revertmesh.py,v $
# $Revision: 1.17 $
# $Author: langer $
# $Date: 2009/07/06 20:55:54 $

OBSOLETE

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


from ooflib.common import registeredclass
from ooflib.common import labeltree
from ooflib.common.IO import parameter
from ooflib.engine import errorestimator
from ooflib.engine import meshmod
from ooflib.engine import skeletonelement
from ooflib.engine import refine
from ooflib.engine import subproblemcontext
import string
#Interface branch
from ooflib.engine import bdycondition

# AdaptiveMeshRefinement
class RevertMesh(meshmod.MeshModification):
    def __init__(self, base_skeleton, init_field=1):
        self.base_skeleton = base_skeleton
        self.init_field = init_field

    def apply(self, meshcontext):
        old_femesh = meshcontext.femesh()  # the current one
        old_skel = meshcontext.getSkeleton()
        # Names of base skeletons are automatically generated and
        # users can't change them.  If there are 3 base skeletons,
        # they'll be "Base Skeleton 0", "Base Skeleton 1", "Base
        # Skeleton 2".  The numbers in the name string match their
        # positions in the buffer, which makes retrieving the object
        # simple.
        index = int(string.split(self.base_skeleton)[-1])
        new_skel = meshcontext.skeleton_buffer.makeCurrent(index)
        skelpath = labeltree.makePath(meshcontext.path())
        new_femesh = new_skel.femesh(
            meshcontext.elementdict,
            skeletonelement.SkeletonElement.realmaterial,
            skelpath[0]+":"+skelpath[1])
        new_femesh.set_rwlock(meshcontext.rwLock)
        
        meshcontext.setSkeleton(new_skel)  # replace old_skel

        notifications = []
        subprobs = []
        for old_subpctxt in meshcontext.subproblems():
            name = old_subpctxt.name()
            # Create a new subproblem with a temporary name.
            new_subpctxt = old_subpctxt.clone(
                meshcontext, copy_field=True, copy_equation=True,
                notifications=notifications)
            subprobs.append((old_subpctxt, new_subpctxt))
      
        meshcontext.setFEMesh(new_femesh)
        new_femesh.setCurrentTime(old_femesh.getCurrentTime())
      
        # Copy Field values from the old FEMesh
        for field in meshcontext.all_subproblem_fields():
            new_femesh.init_field(old_skel, old_femesh, field)
        
        # Destroy old subproblems (this has to happen *after* fields
        # are copied) and give new subproblems their correct names.
        for old_subpctxt, new_subpctxt in subprobs:
            oldname = labeltree.makePath(old_subpctxt.path())[-1]
            meshcontext.pause_writing()
            try:
                old_subpctxt.begin_writing()
                try:
                    old_subpctxt.destroy()
                finally:
                    old_subpctxt.end_writing()
                new_subpctxt.begin_writing()
                try:
                    new_subpctxt.rename(oldname)
                finally:
                    new_subpctxt.end_writing()
            finally:
                meshcontext.resume_writing()

        # put BC in new_femesh
        for (name, bc) in meshcontext.allBoundaryConds():
            #Interface branch
            #Don't copy the invisible Float BCs associated with
            #interfaces. (see femesh.spy)
            if name.find('_cntnty_')==0:
                continue
            #JumpBC's don't have an associated mesh boundary object
            if isinstance(bc,bdycondition.JumpBC):
                new_femesh.addInterfaceBC(name)
                continue
            bc.boundary_obj=new_femesh.getBoundary(bc.boundary)
            new_femesh.boundaries[bc.boundary].addCondition(bc)

        meshcontext.pause_writing()
        try:
            for subproblem in meshcontext.subproblems():
                subproblem.autoenableBCs()
        finally:
            meshcontext.resume_writing()
            
        old_femesh.destroy()
                
        # time stamp update
        meshcontext.changed("Copied.")

# Trivial parameter for skeletons of the mesh -- it will have a custom
# chooser widget.
class MeshSkeletonParameter(parameter.StringParameter):
    pass

registeredclass.Registration(
    'Revert Mesh',
    meshmod.MeshModification,
    RevertMesh,
    ordering=3,
    params=[
    MeshSkeletonParameter('base_skeleton', tip="Name of the base Skeleton."),
    parameter.BooleanParameter('init_field', 1, default=1,
                               tip="Initialize fields?")
    ],
    tip="Undo adaptive mesh refinement.",
    discussion="""<para>
    Refined &mesh; can be reverted back to its pre-refined stages, in case
    the refinement was not satisfactory. Field values (solution) may not be
    recovered properly in some cases.
    </para>"""
    )
