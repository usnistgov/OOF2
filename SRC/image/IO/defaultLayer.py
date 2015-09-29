# -*- python -*-
# $RCSfile: defaultLayer.py,v $
# $Revision: 1.15 $
# $Author: langer $
# $Date: 2014/09/27 21:41:33 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
if config.dimension() == 2:
    from ooflib.SWIG.image import oofimage
## elif config.dimension() == 3:
##     #from ooflib.SWIG.image import oofimage3d
##     from ooflib.image import oofimage3d
from ooflib.common.IO import bitmapdisplay
from ooflib.common.IO import ghostgfxwindow
from ooflib.image import imagecontext

def defaultImageDisplay():
    return bitmapdisplay.bitmapDisplay()

ghostgfxwindow.DefaultLayer(imagecontext.imageContexts, defaultImageDisplay)


