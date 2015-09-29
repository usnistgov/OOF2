# -*- python -*-
# $RCSfile: DIR.py,v $
# $Revision: 1.14 $
# $Author: langer $
# $Date: 2014/09/27 21:41:34 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'SEGMENTATION'
clib = 'oof2image'

# C++ files
cfiles = ['canny.C', 'classify.C',  'fixborders.C', 'mask.C', 'skeletonize.C', 'diffusionRHS.C', 'imageops.C', 'thresholding.C', 'newgabor.C']


# C++ headers
hfiles = ['canny.h', 'classify.h',  'fixborders.h', 'mask.h', 'skeletonize.h', 'diffusionRHS.h', 'imageops.h', 'thresholding.h', 'newgabor.h']


# swig input files
swigfiles = ['skeletonize.swg', 'imageops.swg', 'diffusionRHS.swg', 'thresholding.swg', 'fixborders.swg', 'classify.swg', 'segmenter.swg']

# python files to be included directly in swig output
swigpyfiles = ['segmenter.spy', 'diffusionRHS.spy', 'fixborders.spy', 'thresholding.spy', 'skeletonize.spy']

# pure python files, if any
pyfiles = ['initialize.py']                            

def set_clib_flags(clib):
    clib.externalLibs.append('oof2engine')
