# -*- python -*-
# $RCSfile: adaptivemeshrefinement.py,v $
# $Revision: 1.38 $
# $Author: langer $
# $Date: 2014/09/27 21:40:39 $

OBSOLETE

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


from ooflib.SWIG.common import ooferror
from ooflib.common import debug
from ooflib.common import labeltree
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine import errorestimator
from ooflib.engine import meshmod
from ooflib.engine import rationalize
from ooflib.engine import refine
from ooflib.engine import skeletonboundary
from ooflib.engine import skeletonelement
from ooflib.engine import skeletonmodifier
from ooflib.engine import subproblemcontext
#Interface branch
from ooflib.common.IO import whoville
from ooflib.engine import bdycondition

SkeletonEdgeBoundary = skeletonboundary.SkeletonEdgeBoundary
ExteriorSkeletonEdgeBoundary = skeletonboundary.ExteriorSkeletonEdgeBoundary
SkeletonPointBoundary = skeletonboundary.SkeletonPointBoundary
ExteriorSkeletonPointBoundary = skeletonboundary.ExteriorSkeletonPointBoundary

# AdaptiveMeshRefinement
class AdaptiveMeshRefinement(meshmod.MeshModification):
    #AMR subproblem
    def __init__(self, subproblem, estimator, criterion, degree, alpha,
                 rationalize=0):
        self.estimator = estimator  # ErrorEstimator instance
        self.criterion = criterion  # RefinementCriterion instance
        self.degree = degree        # RefinementDegree instance
        self.alpha = alpha
        self.rationalize = rationalize
        self.subproblem=subproblem # subproblem path for AMR
        
    def doTheBoundary_old(self, old_skel, new_skel):
        # Point boundary propagation.
        for pbdy in old_skel.sheriffSkeleton().pointboundaries.values():
            pbdy.makeContextBoundary(
                None, pbdy.get_name(), old_skel).map(old_skel, new_skel)
        # Edge boundary propagation.
        for ebdy in old_skel.sheriffSkeleton().edgeboundaries.values():
            ebdy.makeContextBoundary(
                None, ebdy.get_name(), old_skel).map(old_skel, new_skel)

    def doTheBoundary(self, old_skel, new_skel, skelcontext):
        # Point boundary propagation.
        for pbdy in skelcontext.pointboundaries.values():
            #pbdy is a XXXContextXXX
            new_skel.mapBoundary(pbdy, old_skel)
        # Edge boundary propagation.
        for ebdy in skelcontext.edgeboundaries.values():
            new_skel.mapBoundary(ebdy, old_skel)

    # This function has a meshcontext parameter because the other
    # meshmod routines need it
    def apply(self, meshcontext):
        subproblemctxt=subproblemcontext.subproblems[self.subproblem]
        subproblemobj=subproblemctxt.getObject()

        if meshcontext!=subproblemobj.meshcontext:
            raise ooferror.ErrUserError(
                "Mismatch between meshcontext and subproblem's meshcontext!")

        # refine the skeleton.
        refinstance = refine.Refine(
            errorestimator.AdaptiveMeshRefine(subproblemctxt.path(),
                                              self.estimator),
            self.criterion, self.degree, self.alpha)

        
        old_skel = meshcontext.getSkeleton()
        new_skel = refinstance.applyAMR(old_skel)

        if not new_skel:
            return              # refinement was interrupted or failed
        
        # Boundary propagation.
        #self.doTheBoundary_old(old_skel, new_skel)
        self.doTheBoundary(old_skel, new_skel, meshcontext.getParent())

        # Only the second Skeleton needs to be disconnected.
        if meshcontext.skeleton_buffer.isFirstInLine(old_skel):
            new_skel.disconnect()

        # rationalize the skeleton
        if self.rationalize:
            newer_skel = new_skel.properCopy(fresh=True)
            targets = skeletonmodifier.AllElements()
            criterion = skeletonmodifier.AverageEnergy(0.8)  # alpha
            for ratreg in rationalize.Rationalizer.registry:
                # Create a Rationalizer from a Registration
                # with default values.
                ratmethod = ratreg()
                ratmethod(newer_skel, None, targets, criterion,
                          ratmethod.findAndFix)
            newer_skel.cleanUp()
            self.doTheBoundary(new_skel, newer_skel)
            new_skel = newer_skel

        meshcontext.pushSkeleton(new_skel)

        # convert the refined skeleton into an femesh
        old_femesh = meshcontext.femesh()
        # realmaterial is a function which tells the elements of the
        # created femesh how to get their materials.
        realmaterial = skeletonelement.SkeletonElement.realmaterial
        #Interface branch, pass skeleton path to femesh
        skelpath=labeltree.makePath(meshcontext.path())
        new_femesh = new_skel.femesh(meshcontext.elementdict,
                                     realmaterial,
                                     skelpath[0]+":"+skelpath[1])
        new_femesh.set_rwlock(meshcontext.rwLock)

        
        # This code is vaguely similar to that in copyMesh in
        # meshmenu.py (the callback for OOF.Mesh.Copy), but is *not*
        # identical.  That's because in this case we're replacing the
        # FEMesh inside a Mesh context, instead of simply creating a
        # whole new Mesh context.

        # Copy subproblems, their fields and equations.  The tricky
        # bit here is that the new subproblems must live in the same
        # Mesh as the old ones and must have the same names, but they
        # refer to different FEMeshes.  If the old subproblems are
        # deleted before the new ones are created, then their Field
        # values in the old FEMesh will be deleted before they can be
        # copied to the new FEMesh.  On the other hand, if the old
        # subproblems are kept, then their names will conflict with
        # the new ones.  Therefore, we have to create the new
        # subproblems with altered names, and change the names after
        # the old subproblems are deleted.  Also, we can't actually
        # insert the new subproblems into the Mesh context until the
        # new FEMesh has been installed...

        # First, gather data about subproblems and their fields and
        # equations.
        class SubProbState:
            pass
        subpstates = {}
        for old_subpctxt in meshcontext.subproblems():
            old_subp = old_subpctxt.getObject()
            subpstate = subpstates[old_subpctxt.path()] = SubProbState()
            subpstate.old_subp = old_subp
            subpstate.new_subptype = old_subpctxt.subptype.clone()
            subpstate.new_subp = subpstate.new_subptype.create()
            subpstate.fields = old_subpctxt.all_fields() # all defined fields
            subpstate.activefields = [f for f in subpstate.fields
                                      if old_subp.is_active_field(f)]
            subpstate.eqns = old_subp.all_equations() # all active equations
            
        # replace old_femesh
        meshcontext.setFEMesh(new_femesh)

        # Install new subproblems and their fields and equations
        for subppath, subpstate in subpstates.items():
            tempname = subproblemcontext.subproblems.uniqueName(subppath)
            subpstate.tempname = tempname
            #Enclosing between pause_writing and resume_writing fixes
            #a blocking problem. May not be the final word...
            #This is also done in interfaceplugin.py.
            #It may also be necessary in revertmesh.py.
            meshcontext.pause_writing()
            meshcontext.newSubProblem(subpstate.new_subp,
                                      subpstate.new_subptype,
                                      meshcontext.path() + ":" + tempname)
            meshcontext.resume_writing()
            for field in subpstate.fields:
                subpstate.new_subp.define_field(field)
                new_femesh.set_in_plane(field, old_femesh.in_plane(field))
            for field in subpstate.activefields:
                subpstate.new_subp.activate_field(field)
            for equation in subpstate.eqns:
                subpstate.new_subp.activate_equation(equation)

        # Copy Field values from the old FEMesh
        for field in meshcontext.all_subproblem_fields():
            new_femesh.init_field(old_skel, old_femesh, field)

        # Destroy old subproblems (this has to happen *after* fields
        # are copied) and give new subproblems their correct names.
        meshcontext.pause_writing()
        try:
            for subppath, subpstate in subpstates.items():
                oldname = labeltree.makePath(subppath)[-1]
                subpctxt = subproblemcontext.subproblems[subppath]
                subpctxt.begin_writing()
                try:
                    subpctxt.destroy()
                finally:
                    subpctxt.end_writing()
                temppath = meshcontext.path() + ':' + subpstate.tempname
                newctxt = subproblemcontext.subproblems[temppath]
                newctxt.begin_writing()
                try:
                    newctxt.rename(oldname)
                finally:
                    newctxt.end_writing()
                    
        finally:
            meshcontext.resume_writing()
            
##        # copy field status
##        for field in meshcontext.all_fields():
##            new_femesh.define_field(field)
##            new_femesh.activate_field(field)
##            new_femesh.set_in_plane(field, old_femesh.in_plane(field))
        
##        # copy equation status
##        for equation in meshcontext.all_equations():
##            new_femesh.get_subproblem().activate_equation(equation)


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
        meshcontext.changed("Refined")

# The widget is set in IO/GUI/adaptivemeshrefineWidget.py
class AMRMeshWhoParameter(whoville.WhoParameter):
    pass

