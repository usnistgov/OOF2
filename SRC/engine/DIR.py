# -*- python -*-
# $RCSfile: DIR.py,v $
# $Revision: 1.68 $
# $Author: langer $
# $Date: 2012/02/28 22:24:57 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

dirname = ['engine']
if not DIM_3:
    clib = 'oof2engine'
else:
    clib = 'oof3dengine'
clib_order = 1

subdirs = ['property', 'elements', 'SparseLib++',
           'IO']

if HAVE_PETSC:
    print "PETSC subdirectory appended"
    subdirs.append('PETSc')

cfiles = [
    'angle2color.C', 'bdyanalysis.C', 'boundarycond.C',
    'cconjugate.C', 'celectricfield.C', 'cmatrixmethods.C',
    'compoundsubproblem.C', 'contourcell.C',
    'cnonlinearsolver.C',
    'cscpatch.C', 'cskeleton.C', 'cstrain.C', 'csubproblem.C',
    'diagpre.C', 'dofmap.C', 'edge.C', 'edgeset.C',
    'eigenvalues.C', 'element.C', 'elementnodeiterator.C',
    'entiremeshsubproblem.C', 'equation.C', 'femesh.C', 'field.C',
    'fieldeqnlist.C', 'fieldindex.C', 'flux.C', 'fluxnormal.C',
    'freedom.C', 'gausspoint.C',
    'icpre.C', 'ilupre.C', 'invariant.C',
    'linearizedsystem.C', 'mastercoord.C',
    'masterelement.C', 'material.C', 'materialset.C', 'materialsubproblem.C',
    'meshdatacache.C', 'meshiterator.C', 'nodalequation.C',
    'nodalfluxes.C', 'nodalscpatches.C', 'node.C', 'ooferror.C',
    'orientationimage.C', 'outputval.C', 'pixelgroupsubproblem.C',
    #'pixelintersection.C',
    'pixelselectioncouriere.C', 'pointdata.C', 'preconditioner.C',
    'property.C', 'pypropertywrapper.C', 'rank3tensor.C',
    'recoveredflux.C', 'shapefunction.C', 'shapefunctioncache.C',
    'smallsystem.C', 'sparsemat.C', 'steperrorscaling.C',
    'symeig3.C', 'symmmatrix.C', 'crystalsymmetry.C'
]

swigfiles = [
    'angle2color.swg', 'bdyanalysis.swg', 'boundarycond.swg',
    'cconjugate.swg', 'cmatrixmethods.swg', 'compoundsubproblem.swg',
    'contourcell.swg', 'cskeleton.swg', 'cstrain.swg',
    'cnonlinearsolver.swg',
    'csubproblem.swg', 'diagpre.swg', 'dofmap.swg', 'edge.swg',
    'edgeset.swg', 'element.swg', 'elementnodeiterator.swg',
    'entiremeshsubproblem.swg', 'equation.swg', 'femesh.swg', 'field.swg',
    'fieldindex.swg', 'flux.swg', 'freedom.swg', 'gausspoint.swg',
    'icpre.swg', 'ilupre.swg', 'invariant.swg', 'linearizedsystem.swg',
    'mastercoord.swg', 'masterelement.swg', 'material.swg',
    'materialsubproblem.swg', 'meshdatacache.swg', 'meshiterator.swg',
    'nodalequation.swg', 'node.swg', 'ooferror2.swg',
    'orientationimage.swg', 'outputval.swg', 'pixelgroupsubproblem.swg',
    'pixelselectioncouriere.swg', 'planarity.swg', 'preconditioner.swg',
    'pointdata.swg',
    'properties.swg', 'pypropertywrapper.swg', 'rank3tensor.swg',
    'smallsystem.swg', 'sparsemat.swg',
    'steperrorscaling.swg', 'symmmatrix.swg', 'crystalsymmetry.swg'
    ]

pyfiles = [
    'adaptivemeshrefinement.py', 'analysisdomain.py', 'analysissample.py',
    'anneal.py', 'autoskeleton.py', 'bdycondition.py', 'boundary.py',
    'boundarybuilder.py', 'boundarymodifier.py', 'builtinprops.py',
    'conjugate.py', 'deputy.py', 'deputytracker.py',
    'edgeswap.py', 'errorestimator.py', 'euler.py', 'fiddlenodesbase.py',
    'fieldinit.py', 'initialize.py', 'instantnodemove.py',
    'nonlinearsolver.py', 'nonlinearsolvercore.py', 'interfaceplugin.py',
    'materialmanager.py', 'materialplugin.py', 'mergetriangles.py',
    'mesh.py', 'meshbdyanalysis.py', 'meshcrosssection.py', 'meshmod.py',
    'meshstatus.py',
    'outputschedule.py', 'pinnodesmodifier.py', 'pixelselect.py',
    'problem.py', 'profile.py', 'profilefunction.py',
    'propertyregistration.py', 'pyproperty.py', 'rationalize.py',
    'rationalsharp.py', 'rationalshort.py', 'rationalwide.py',
    'refine.py', 'refinementtarget.py', 'refinemethod.py',
    'refinequadbisection.py', 'relaxation.py', 'rk.py',
    'scpatch.py', 'skeleton.py', 'skeletonboundary.py',
    'skeletoncontext.py', 'skeletondiff.py', 'skeletonelement.py',
    'skeletongroups.py', 'skeletonmodifier.py', 'skeletonnode.py',
    'skeletonsegment.py', 'skeletonselectable.py',
    'skeletonselectionmethod.py', 'skeletonselectionmod.py',
    'skeletonselectionmodes.py', 'skeletonselmodebase.py', 'snapnode.py',
    'snaprefine.py', 'snaprefinemethod.py', 'splitquads.py', 'ss22.py',
    'subproblemcontext.py', 'subproblemtype.py', 'symstate.py',
    'timestepper.py', 'twostep.py', 'vigilante.py', 'skeletonfilterparams.py'
]

swigpyfiles = [
    'angle2color.spy', 'compoundsubproblem.spy',
    'contourcell.spy', 'cstrain.spy',
    'csubproblem.spy', 'edge.spy', 'edgeset.spy',
    'element.spy', 'elementnodeiterator.spy', 'equation.spy',
    'femesh.spy', 'field.spy', 'fieldindex.spy', 'flux.spy',
    'invariant.spy', 'mastercoord.spy', 'linearizedsystem.spy',
    'masterelement.spy', 'material.spy', 'materialsubproblem.spy',
    'meshdatacache.spy', 'node.spy', 'ooferror2.spy', 'outputval.spy',
    'pixelgroupsubproblem.spy', 'preconditioner.spy', 'property.spy',
    'pypropertywrapper.spy', 'rank3tensor.spy',
    'steperrorscaling.spy', 'symmmatrix.spy', 'entiremeshsubproblem.spy',
    'crystalsymmetry.spy'
    ]

hfiles = [
    'angle2color.h', 'bdyanalysis.h',
    'boundarycond.h', 'cconjugate.h', 'celectricfield.h',
    'cmatrixmethods.h', 'compoundsubproblem.h', 'constraint.h',
    'cnonlinearsolver.h',
    'contourcell.h', 'cscpatch.h', 'cskeleton.h',
    'cstrain.h', 'csubproblem.h', 'diagpre.h', 'dofmap.h',
    'edge.h', 'edgeset.h', 'eigenvalues.h', 'element.h',
    'elementnodeiterator.h', 'entiremeshsubproblem.h', 'equation.h',
    'femesh.h', 'field.h', 'fieldeqnlist.h', 'fieldindex.h', 'flux.h',
    'fluxnormal.h', 'freedom.h', 'gausspoint.h', 'group.h', 'icpre.h',
    'ilupre.h', 'indextypes.h', 'invariant.h', 'linearizedsystem.h',
    'mastercoord.h', 'masterelement.h', 'material.h', 'materialset.h',
    'materialsubproblem.h', 'meshdatacache.h', 'meshiterator.h',
    'nodalequation.h', 'nodalfluxes.h', 'nodalscpatches.h', 'node.h',
    'nodegroup.h', 'ooferror.h', 'orientationimage.h', 'outputval.h',
    'pixelgroupsubproblem.h', 'pixelselectioncouriere.h',
    'pointdata.h', 'planarity.h',
    'preconditioner.h', 'predicatesubproblem.h', 'property.h',
    'pypropertywrapper.h', 'rank3tensor.h', 'recoveredflux.h',
    'shapefunction.h', 'shapefunctioncache.h',
    'smallsystem.h', 'sparsemat.h', 'steperrorscaling.h', 'symeig3.h',
    'symmmatrix.h', 'crystalsymmetry.h'
]


if DIM_3:
    pyfiles.append("skeleton3d.py")
    hfiles.append("elementlocator.h")
    swigfiles.append("elementlocator.swg")


def set_clib_flags(clib):
    if not DIM_3:
        clib.externalLibs.append('oof2common')
    else:
        clib.externalLibs.append('oof3dcommon')


if HAVE_MPI:
    cfiles.extend(['cfiddlenodesbaseParallel.C'])
    swigfiles.extend(['cfiddlenodesbaseParallel.swg'])
    swigpyfiles.extend(['cfiddlenodesbaseParallel.spy'])
    hfiles.extend(['cfiddlenodesbaseParallel.h'])
    pyfiles.extend(['fiddlenodesbaseParallel.py', 'refineParallel.py'])


