# -*- python -*- 
# $RCSfile: DIR.py,v $
# $Revision: 1.6 $
# $Author: langer $
# $Date: 2014/09/27 21:41:28 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modifed
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

dirname = 'GRAINBDY'

cfiles = ['imageops.C', 'igf.C', 'mask.C', 'modifiedGabor.C', 'rgf.C',
    'close.C', 'skeletonize.C', 'connectEdge.C', 'histogram.C',
    'newGabor.C', 'sobel.C', 'gaussSmooth.C', 'laplacian.C',
    'laplacianGauss.C', 'hysteresis.C', 'nonmaxSuppression.C',
    'compare.C', 'hough.C']

swigfiles = ['imageops.swg']

pyfiles = ['initialize.py', 'wrappers.py', 'imagefilter.py']

hfiles = ['imageops.h', 'igf.h', 'mask.h', 'modifiedGabor.h', 'rgf.h',
    'close.h', 'skeletonize.h', 'connectEdge.h', 'histogram.h',
    'newGabor.h', 'sobel.h', 'gaussSmooth.h', 'laplacian.h',
    'laplacianGauss.h', 'hysteresis.h', 'nonmaxSuppression.h',
    'compare.h', 'hough.h']

if not DIM_3:
    clib='oof2image'
else:
    clib='oof3dimage'
