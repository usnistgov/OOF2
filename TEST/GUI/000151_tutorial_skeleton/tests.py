# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from generics import *
import os

# # Make sure that the skeleton.dat output file doesn't already exist.
# removefile('skeleton.dat')

def skeletonElementSelectionSizeCheck(skeleton, n):
    from ooflib.common.IO import whoville
    sc = whoville.getClass('Skeleton')[skeleton]
    return sc.elementselection.size() == n

def skeletonSizeCheck(skeleton, nel, nnode):
    from ooflib.common.IO import whoville
    skel = whoville.getClass('Skeleton')[skeleton].getObject()
    return skel.nelements() == nel and skel.nnodes() == nnode

def homogeneityIndex(val, tolerance=1.e-10):
    lines = gtkTextviewGetLines(
        'OOF2:Skeleton Page:Pane:StatusScroll:SkeletonText')
    # Look for a line of the form "Homogeneity Index: xxx"
    for line in lines:
        if line.startswith("Homogeneity Index"):
            try:
                homog = float(line.split()[2])
                return abs(homog - val) <= tolerance
            except:
                # line isn't of the expected form
                return False
