# -*- python -*-
# $RCSfile: initialize.py,v $
# $Revision: 1.147 $
# $Author: langer $
# $Date: 2011/04/28 19:52:57 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# All components of engine that need initialization *before* they're
# used should be imported here.  Using OOFexec makes the names
# available in the __main__ environment in text mode.

from ooflib.common import debug
from ooflib.common import parallel_enable
from ooflib.common import utils
import ooflib.SWIG.engine.ooferror2
from ooflib.SWIG.common import config


import ooflib.engine.materialplugin
utils.OOFexec('from ooflib.engine.problem import *')
import ooflib.engine.IO.propertymenu
import ooflib.engine.IO.materialmenu
import ooflib.engine.builtinprops
if config.dimension() == 2:
    import ooflib.engine.skeleton
elif config.dimension() == 3:
    import ooflib.engine.skeleton3d
import ooflib.engine.skeletoncontext
import ooflib.engine.skeletonselectionmodes
import ooflib.SWIG.engine.masterelement
import ooflib.SWIG.engine.material
import ooflib.engine.boundary
import ooflib.engine.IO.outputDefs
import ooflib.engine.IO.xmloutputs
import ooflib.engine.IO.displaymethods
import ooflib.engine.IO.contourdisplay
import ooflib.engine.IO.centerfilldisplay
import ooflib.engine.fieldinit
import ooflib.engine.elements.initialize
import ooflib.engine.conjugate
import ooflib.SWIG.engine.angle2color
import ooflib.engine.errorestimator

import ooflib.engine.IO.skeletonmenu
import ooflib.engine.IO.pinnodesmenu
import ooflib.engine.IO.boundarymenu
import ooflib.engine.IO.boundaryconditionmenu
import ooflib.engine.mesh
import ooflib.SWIG.engine.femesh
import ooflib.engine.IO.meshmenu
import ooflib.engine.IO.scheduledoutputmenu

# skeleton and mesh modification stuff
import ooflib.engine.refine
import ooflib.engine.refinementtarget
import ooflib.engine.rationalize
import ooflib.engine.autoskeleton
import ooflib.engine.snaprefine
import ooflib.engine.snapnode
import ooflib.engine.edgeswap
if config.dimension() == 2:
    import ooflib.engine.splitquads
    import ooflib.engine.rationalshort
    import ooflib.engine.rationalwide
    import ooflib.engine.rationalsharp
    import ooflib.engine.mergetriangles
elif config.dimension() == 3:
    import ooflib.engine.rationalbadtet
import ooflib.engine.fiddlenodesmethods
import ooflib.engine.relaxation
import ooflib.engine.vigilante
import ooflib.engine.meshmod
import ooflib.engine.skeletonmodifier

import ooflib.SWIG.engine.materialsubproblem
import ooflib.SWIG.engine.pixelgroupsubproblem
import ooflib.SWIG.engine.entiremeshsubproblem
import ooflib.SWIG.engine.compoundsubproblem

import ooflib.engine.pixelselect
import ooflib.SWIG.engine.pixelselectioncouriere
import ooflib.engine.skeletonselectionmod
import ooflib.engine.IO.skeletonselectiontoolbox
import ooflib.engine.IO.skeletoninfo
import ooflib.engine.IO.meshinfo
import ooflib.engine.IO.movenode
import ooflib.engine.IO.pinnodes
import ooflib.engine.IO.meshcstoolbox

import ooflib.engine.IO.skeletoninfodisplay
import ooflib.engine.IO.meshinfodisplay
import ooflib.engine.IO.movenodedisplay
import ooflib.engine.IO.pinnodesdisplay
if config.dimension() == 2: 
    import ooflib.engine.IO.meshcsdisplay

import ooflib.engine.IO.elementselectdisplay
import ooflib.engine.IO.nodeselectdisplay
import ooflib.engine.IO.segmentselectdisplay
import ooflib.engine.IO.skeletonbdydisplay
import ooflib.engine.IO.skeletonselectmenu
import ooflib.engine.IO.skeletongroupmenu
import ooflib.engine.IO.microstructuredisplay
##import ooflib.engine.IO.solvermenu
import ooflib.engine.IO.subproblemmenu
import ooflib.engine.IO.analyzemenu
import ooflib.engine.IO.meshbdymenu

import ooflib.engine.evolve
import ooflib.engine.timestepper
import ooflib.engine.euler
import ooflib.engine.rk
import ooflib.engine.ss22
import ooflib.engine.twostep
import ooflib.engine.staticstep
import ooflib.engine.IO.animationtimes

import ooflib.SWIG.engine.cstrain

import ooflib.common.runtimeflags

if config.dimension() == 2 and  ooflib.common.runtimeflags.surface_mode:
    import ooflib.engine.IO.interfacemenu

if parallel_enable.enabled():
    import ooflib.engine.IO.materialmenuIPC
    import ooflib.engine.IO.skeletonIPC
    import ooflib.engine.deputyParallel
    import ooflib.engine.refineParallel
    import ooflib.engine.IO.meshIPC
    import ooflib.engine.IO.boundaryconditionIPC
    import ooflib.engine.IO.propertymenuIPC
    import ooflib.engine.IO.solvermenuIPC
