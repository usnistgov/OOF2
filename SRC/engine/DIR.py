# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

dirname = ['engine']
clib = 'oof2engine'
clib_order = 1

subdirs = ['property', 'elements', 'IO']

if HAVE_PETSC:
    print "PETSC subdirectory appended"
    subdirs.append('PETSc')

cfiles = [
    'angle2color.C', 'bdyanalysis.C', 'boundarycond.C',
    'cconjugate.C', 'celectricfield.C', 'cnonlinearsolver.C',
    'compoundsubproblem.C', 'contourcell.C', 'corientation.C',
    'crystalsymmetry.C', 'cscpatch.C', 'cskeleton.C', 'cstrain.C',
    'csubproblem.C', 'dofmap.C', 'edge.C', 'edgeset.C',
    'eigenvalues.C', 'element.C', 'elementnodeiterator.C',
    'entiremeshsubproblem.C', 'equation.C', 'femesh.C', 'field.C',
    'fieldeqnlist.C', 'fieldindex.C', 'flux.C', 'fluxnormal.C',
    'freedom.C', 'gausspoint.C', 'invariant.C', 'linearizedsystem.C',
    'mastercoord.C', 'masterelement.C', 'material.C', 'materialset.C',
    'materialsubproblem.C', 'meshdatacache.C', 'meshiterator.C',
    'nodalequation.C', 'nodalfluxes.C', 'nodalscpatches.C', 'node.C',
    'ooferror.C', 'orientationimage.C', 'outputval.C',
    'pixelgroupsubproblem.C', 'pixelselectioncouriere.C',
    'pointdata.C', 'property.C', 'pypropertywrapper.C',
    'rank3tensor.C', 'recoveredflux.C', 'shapefunction.C',
    'shapefunctioncache.C', 'smallsystem.C', 'sparsemat.C',
    'steperrorscaling.C', 'symeig3.C', 'symmmatrix.C',
]

swigfiles = [
    'angle2color.swg', 'bdyanalysis.swg',
    'boundarycond.swg', 'cconjugate.swg', 'cmatrixmethods.swg',
    'cnonlinearsolver.swg', 'compoundsubproblem.swg',
    'contourcell.swg', 'corientation.swg', 'crystalsymmetry.swg',
    'cskeleton.swg', 'cstrain.swg', 'csubproblem.swg', 'dofmap.swg',
    'edge.swg', 'edgeset.swg', 'element.swg',
    'elementnodeiterator.swg', 'entiremeshsubproblem.swg',
    'equation.swg', 'femesh.swg', 'field.swg', 'fieldindex.swg',
    'flux.swg', 'freedom.swg', 'gausspoint.swg', 'invariant.swg',
    'linearizedsystem.swg', 'mastercoord.swg', 'masterelement.swg',
    'material.swg', 'materialsubproblem.swg', 'meshdatacache.swg',
    'meshiterator.swg', 'nodalequation.swg', 'node.swg',
    'ooferror2.swg', 'orientationimage.swg', 'outputval.swg',
    'pixelgroupsubproblem.swg', 'pixelselectioncouriere.swg',
    'planarity.swg', 'pointdata.swg', 'properties.swg',
    'pypropertywrapper.swg', 'rank3tensor.swg', 'smallsystem.swg',
    'sparsemat.swg', 'steperrorscaling.swg', 'symmmatrix.swg',
]

pyfiles = [
    'adaptivemeshrefinement.py', 'analysisdomain.py',
    'analysissample.py', 'anneal.py', 'autoskeleton.py',
    'bdycondition.py', 'boundary.py', 'boundarybuilder.py',
    'boundarymodifier.py', 'builtinprops.py', 'conjugate.py',
    'deputy.py', 'deputytracker.py', 'edgeswap.py',
    'errorestimator.py', 'euler.py', 'fiddlenodesbase.py',
    'fieldinit.py', 'initialize.py', 'instantnodemove.py',
    'interfaceplugin.py', 'materialmanager.py', 'materialplugin.py',
    'mergetriangles.py', 'mesh.py', 'meshbdyanalysis.py',
    'meshcrosssection.py', 'meshmod.py', 'meshstatus.py',
    'nonlinearsolver.py', 'nonlinearsolvercore.py',
    'outputschedule.py', 'pinnodesmodifier.py', 'pixelselect.py',
    'problem.py', 'profile.py', 'profilefunction.py',
    'propertyregistration.py', 'pyproperty.py', 'rationalize.py',
    'rationalsharp.py', 'rationalshort.py', 'rationalwide.py',
    'refine.py', 'refinementtarget.py', 'refinemethod.py',
    'refinequadbisection.py', 'relaxation.py', 'rk.py', 'scpatch.py',
    'skeleton.py', 'skeletonboundary.py', 'skeletoncontext.py',
    'skeletondiff.py', 'skeletonelement.py',
    'skeletonfilterparams.py', 'skeletongroups.py',
    'skeletonmodifier.py', 'skeletonnode.py', 'skeletonsegment.py',
    'skeletonselectable.py', 'skeletonselectionmethod.py',
    'skeletonselectionmod.py', 'skeletonselectionmodes.py',
    'skeletonselmodebase.py', 'snapnode.py', 'snaprefine.py',
    'snaprefinemethod.py', 'splitquads.py', 'ss22.py',
    'subproblemcontext.py', 'subproblemtype.py', 'symstate.py',
    'timestepper.py', 'twostep.py', 'vigilante.py',
]

swigpyfiles = [
    'angle2color.spy', 'compoundsubproblem.spy', 'contourcell.spy',
    'corientation.spy', 'crystalsymmetry.spy', 'cstrain.spy',
    'csubproblem.spy', 'edge.spy', 'edgeset.spy', 'element.spy',
    'elementnodeiterator.spy', 'entiremeshsubproblem.spy',
    'equation.spy', 'femesh.spy', 'field.spy', 'fieldindex.spy',
    'flux.spy', 'invariant.spy', 'linearizedsystem.spy',
    'mastercoord.spy', 'masterelement.spy', 'material.spy',
    'materialsubproblem.spy', 'meshdatacache.spy', 'node.spy',
    'ooferror2.spy', 'outputval.spy', 'pixelgroupsubproblem.spy',
    'property.spy', 'pypropertywrapper.spy', 'rank3tensor.spy',
    'steperrorscaling.spy', 'symmmatrix.spy',
]

hfiles = [
    'angle2color.h', 'bdyanalysis.h', 'boundarycond.h',
    'cconjugate.h', 'celectricfield.h', 'cmatrixmethods.h',
    'cnonlinearsolver.h', 'compoundsubproblem.h', 'constraint.h',
    'contourcell.h', 'corientation.h', 'crystalsymmetry.h',
    'cscpatch.h', 'cskeleton.h', 'cstrain.h', 'csubproblem.h',
    'dofmap.h', 'edge.h', 'edgeset.h', 'eigenvalues.h', 'element.h',
    'elementnodeiterator.h', 'entiremeshsubproblem.h', 'equation.h',
    'femesh.h', 'field.h', 'fieldeqnlist.h', 'fieldindex.h', 'flux.h',
    'fluxnormal.h', 'freedom.h', 'gausspoint.h', 'group.h',
    'indextypes.h', 'invariant.h', 'linearizedsystem.h',
    'mastercoord.h', 'masterelement.h', 'material.h', 'materialset.h',
    'materialsubproblem.h', 'meshdatacache.h', 'meshiterator.h',
    'nodalequation.h', 'nodalfluxes.h', 'nodalscpatches.h', 'node.h',
    'nodegroup.h', 'ooferror.h', 'orientationimage.h', 'outputval.h',
    'pixelgroupsubproblem.h', 'pixelselectioncouriere.h',
    'planarity.h', 'pointdata.h', 'predicatesubproblem.h',
    'property.h', 'pypropertywrapper.h', 'rank3tensor.h',
    'recoveredflux.h', 'shapefunction.h', 'shapefunctioncache.h',
    'smallsystem.h', 'sparsemat.h', 'steperrorscaling.h', 'symeig3.h',
    'symmmatrix.h',
]


def set_clib_flags(clib):
    import oof2setuputils
    addOOFlibs(clib, 'oof2common')
    oof2setuputils.pkg_check("cairomm-1.0", CAIROMM_VERSION, clib)
    oof2setuputils.pkg_check("pango", PANGO_VERSION, clib)
    oof2setuputils.pkg_check("pangocairo", PANGOCAIRO_VERSION, clib)
    
if HAVE_MPI:
    cfiles.extend(['cfiddlenodesbaseParallel.C'])
    swigfiles.extend(['cfiddlenodesbaseParallel.swg'])
    swigpyfiles.extend(['cfiddlenodesbaseParallel.spy'])
    hfiles.extend(['cfiddlenodesbaseParallel.h'])
    pyfiles.extend(['fiddlenodesbaseParallel.py', 'refineParallel.py'])


