# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

## This file defines a menu item that aggregates a bunch of other menu
## items in an attempt to create and adapt a Skeleton completely
## automatically.  The user must provide two length scales -- the size
## of the largest and smallest features of interest in the
## microstructure.  An initial Skeleton is created at the larger
## length scale and refined by homogeneity (using the provided
## threshold) to the smaller scale.  Then SnapRefine is applied once,
## the Skeleton is Rationalized, and finally it's Smoothed (after
## pinning internal boundary nodes).

from ooflib.SWIG.common import config
from ooflib.SWIG.common import progress
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import utils
from ooflib.common.IO import automatic
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
import ooflib.common.microstructure
import math
import sys

def autoSkeleton(menuitem, name, microstructure,
                  left_right_periodicity, top_bottom_periodicity,
                  maxscale, minscale, units, threshold):
    # Run the actual callback in the main namespace, so that it can
    # use menu and registeredclass names trivially.
    ## TODO: Why is the progress bar title showing up as "Thread-XX"?
    prog = progress.getProgress(menuitem.name, progress.DEFINITE)
    utils.OOFrun(_autoSkeletonMain, prog, name, microstructure,
                 left_right_periodicity, top_bottom_periodicity,
                 False, maxscale, minscale,
                 units, threshold)

# Autoskeleton takes a progress argument, and increments it as it goes
# along. If it gets a "stop" signal from the user, it just returns --
# since this operation is "script-like", stopping the process does not
# prevent the incremental skeleton modifications from being pushed on
# the stack, but the user can still "undo" them using the regular
# skeleton undo mechanism.
def _autoSkeletonMain(prog, name, microstructure,
                      left_right_periodicity,
                      top_bottom_periodicity,
                      front_back_periodicity,
                      maxscale, minscale, units,
                      threshold):
    ms = ooflib.common.microstructure.microStructures[microstructure]
    if units == 'Pixel':
        size = ms.getObject().sizeInPixels()
        n0 = size/maxscale
        n1 = size/minscale
    elif units == 'Physical':
        size = ms.getObject().size()
        n0 = size/maxscale
        n1 = size/minscale
    else:    # A fraction of the x and y dimensions of the microstructure
        n = 1.0/maxscale
        n0 = [1./maxscale]*config.dimension()
        n1 = [1./minscale]*config.dimension()

    n0 = [max(n0[i],1) for i in range(config.dimension())]
    
    nrefine = int(math.ceil(max([math.log(n1[i]/n0[i])/math.log(2)
                                 for i in range(config.dimension())])))

    # Magic number -- total number of lines executed is the number of
    # refines plus the "New", the "SnapRefine", the Rationalize, the
    # boundary node pinning, the smoothing, and the unpinning.  Total
    # is seven.
    total_lines = nrefine + 6
    lcount = 0

    skelname = microstructure+":"+name

    prog.setFraction(lcount/total_lines)
    prog.setMessage(f"{lcount}/{total_lines} operations")
    if prog.stopped():
        return
    
    OOF.Skeleton.New(name=name, 
                     microstructure=microstructure,
                     x_elements=int(math.ceil(n0[0])),
                     y_elements=int(math.ceil(n0[1])),
                     skeleton_geometry=QuadSkeleton(
                         left_right_periodicity=left_right_periodicity,
                         top_bottom_periodicity=top_bottom_periodicity))
    lcount += 1
                     
    prog.setFraction(lcount/total_lines)
    prog.setMessage(f"{lcount}/{total_lines} operations")
    if prog.stopped():
        return
    
    for i in range(nrefine):
        OOF.Skeleton.Modify(
            skeleton=skelname,
            modifier=Refine(targets=CheckHomogeneity(threshold=threshold),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.8))
        lcount += 1
        prog.setFraction(lcount/total_lines)
        prog.setMessage(f"{lcount}/{total_lines} operations")
        if prog.stopped():
            return

    # For TMFKA SnapRefine, set the min_distance between nodes to be
    # 1/10 of the pixel size.  This is arbitrary, but should be good
    # enough.  It's virtually zero on any meaningful physical scale,
    # but not so small that round-off can create illegal elements.
    ## TODO PYTHON3: Should mindist be larger?  1.0?
    mindist = 0.1
    OOF.Skeleton.Modify(
        skeleton=skelname,
        modifier=Refine(targets=CheckHomogeneity(threshold=threshold),
                        divider=TransitionPoints(minlength=mindist),
                        rules='Quick',
                        alpha=0.8))
    lcount += 1
    prog.setFraction(lcount/total_lines)
    prog.setMessage(f"{lcount}/{total_lines} operations")
    if prog.stopped():
        return
    
    OOF.Skeleton.Modify(
        skeleton=skelname,
        modifier=Rationalize(
            targets=AllElements(),
            criterion=AverageEnergy(alpha=0.8),
            method=SpecificRationalization(
                rationalizers=[
                    RemoveShortSide(ratio=5.0),
                    QuadSplit(angle=150),
                    RemoveBadTriangle(acute_angle=15,obtuse_angle=150)]),
            iterations=2
        ))
    lcount += 1
    prog.setFraction(lcount/total_lines)
    prog.setMessage(f"{lcount}/{total_lines} operations")
    if prog.stopped():
        return
        
    OOF.Skeleton.PinNodes.Pin_Internal_Boundary_Nodes(skeleton=skelname)
    lcount += 1
    prog.setFraction(lcount/total_lines)
    prog.setMessage(f"{lcount}/{total_lines} operations")
    if prog.stopped():
        return
    
    OOF.Skeleton.Modify(
        skeleton=skelname,
        modifier=Smooth(targets=AllNodes(),
                        criterion=AverageEnergy(alpha=0.3),
                        T=0.0,
                        iteration=FixedIteration(iterations=5)))
    lcount += 1
    prog.setFraction(lcount/total_lines)
    prog.setMessage(f"{lcount}/{total_lines} operations")
    if prog.stopped():
        return
    
    OOF.Skeleton.PinNodes.Undo(skeleton=skelname)
    lcount += 1
    prog.setFraction(lcount/total_lines)
    prog.setMessage(f"{lcount}/{total_lines} operations")

    prog.finish()
    

