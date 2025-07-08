# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common.IO import mainmenu
from ooflib.SWIG.common import pixelgroup
from ooflib.SWIG.image import pixeldifferentiator
from ooflib.common import oofenum

class ImagePixelInfo(pixelgroup.PixelGroupInfoPlugIn):
    def __call__(self, menuitem, microstructure, pixelset, **kwargs):
        results = []
        # Print color statistics for each image in the microstructure
        # separately.
        for image in microstructure.getImageContexts():
            imageobj = image.getObject()
            (ncolors, mean, dev) =  pixeldifferentiator.groupColorStats(
                imageobj, pixelset)
            results.append(f"Image: {image.name()}")
            results.append(f"   Number of colors: {ncolors}")
            results.append(f"   Average color: r={mean.getRed()} g={mean.getGreen()} b={mean.getBlue()}")
            results.append(f"   Deviation: r={dev.getRed()} g={dev.getGreen()} b={dev.getBlue()}")
        return "\n".join(results)
