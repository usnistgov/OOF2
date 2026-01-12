# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import config
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import automatic
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.image import imagemodifier

import numpy
import skimage

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The ThresholdMethod class describes different ways of computing the
# threshold for the Threshold ImageModifier.  Subclasses of
# ThresholdMethod must define threshold(self, image), which returns
# the threshold value for the given gray scale image.  The threshold
# can either be a single number between 0 and 1 or a numpy array
# containing a threshold for each pixel.

class ThresholdMethod(registeredclass.RegisteredClass):
    registry = []
    tip = "Various ways of thresholding an image."
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/thresholdmethod.xml')
    xrefs=["MenuItem-OOF.Image.Modify.Threshold"]

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
    
class ManualThreshold(ThresholdMethod):
    def __init__(self, value):
        self.value = value
    def threshold(self, image):
        return self.value

registeredclass.Registration(
    'Manual',
    ThresholdMethod,
    ManualThreshold,
    ordering=0,
    params = [
        # TODO NUMPY: Use a GrayParameter w/ special widget?
        parameter.FloatRangeParameter(
            'value', (0,1,.01), value=0.5, tip="Threshold value.")
    ],
    tip = "Make all pixels brighter than the given value white, and the rest black.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/image/reg/thresholdmanual.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MeanThreshold(ThresholdMethod):
    def threshold(self, image):
        return skimage.filters.threshold_mean(image)

registeredclass.Registration(
    'Mean',
    ThresholdMethod,
    MeanThreshold,
    ordering=1,
    tip="All pixels brighter than the mean brightness of the image will be white, and the rest black.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/image/reg/thresholdmean.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MinimumThreshold(ThresholdMethod):
    def threshold(self, image):
        return skimage.filters.threshold_minimum(image)

registeredclass.Registration(
    'Minimum',
    ThresholdMethod,
    MinimumThreshold,
    ordering=2,
    tip="Choose a threshold at the minimum in the smoothed histogram of gray values",
    discussion=xmlmenudump.loadFile(
        "DISCUSSIONS/image/reg/thresholdminimum.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MinimumEntropyThreshold(ThresholdMethod):
    def __init__(self, tolerance):
        self.tolerance = tolerance
    def threshold(self, image):
        if self.tolerance == automatic.automatic:
            tol = None
        else:
            tol = self.tolerance
        return skimage.filters.threshold_li(image, tolerance=tol)

registeredclass.Registration(
    "MinimumEntropy",
    ThresholdMethod,
    MinimumEntropyThreshold,
    ordering=3,
    params=[
        parameter.AutoFloatParameter(
            "tolerance", automatic.automatic,
            tip="Stop iterating when the threshold change is less than this.")
        ],
    tip="Compute the threshold value by Li’s iterative Minimum Cross Entropy method.",
    discussion=xmlmenudump.loadFile(
        "DISCUSSIONS/image/reg/thresholdminimumentropy.xml")
)
    
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# LocalThreshold computes a different threshold at each pixel, using a
# LocalAverageMethod to compute the average brightness of the
# neighborhood of the pixel.  Subclasses of LocalAverageMethod must
# define methodparam(), which returns a string passed to
# skimage.filters.threshold_local() via its "method" parameter,
# telling it what averaging method to use. Some averaging methods
# require more input, which is returned by
# LocalAverageMethod.paramparam() and passed to threshold_local()'s
# "param" parameter.

class LocalAverageMethod(registeredclass.RegisteredClass):
    registry = []
    def paramparam(self):
        return None
    tip="How to compute the local average intensity."
    discussion="""
    <para><classname>LocalAverageMethod</classname> subclasses are used as
    the <varname>average</varname> parameter to the <xref
    linkend="RegisteredClass-LocalThreshold"/> image thresholding
    method.</para>  """
    xrefs=["MenuItem-OOF.Image.Modify.Threshold",
           "RegisteredClass-LocalThreshold"]
    
class LocalMean(LocalAverageMethod):
    def methodparam(self):
        return 'mean'

registeredclass.Registration(
    'mean',
    LocalAverageMethod,
    LocalMean,
    ordering=0,
    tip="The threshold is the mean of the gray values in the local area.",
    discussion="""<para>
    Compute a local threshold from the mean of the intensity values in
    the local area.  </para>"""
)

class LocalMedian(LocalAverageMethod):
    def methodparam(self):
        return 'median'

registeredclass.Registration(
    'median',
    LocalAverageMethod,
    LocalMedian,
    ordering=1,
    tip="The threshold is the median of the gray values in the local area.",
    discussion="""<para>
    Compute a local threshold from the median of the intensity values in
    the local area.  </para>"""
)

class LocalGaussian(LocalAverageMethod):
    def __init__(self, sigma):
        self.sigma = sigma
    def methodparam(self):
        return 'gaussian'
    def paramparam(self):
        if self.sigma is automatic.automatic:
            return None
        return self.sigma

registeredclass.Registration(
    'gaussian',
    LocalAverageMethod,
    LocalGaussian,
    ordering=2,
    params=[
        parameter.PositiveAutoFloatParameter(
            'sigma', automatic.automatic, tip='Width of the gaussian')],
    tip="The threshold is the gaussian weighted mean of the gray values in the local area.",
    discussion="""<para>
        Compute a local threshold from the gaussian weighted mean of the
    intensity values in the local area.  </para>"""
)


class LocalThreshold(ThresholdMethod):
    def __init__(self, radius, average, offset):
        self.radius = radius
        self.average = average
        self.offset = offset
    def threshold(self, image):
        block_size = 2*self.radius + 1
        return skimage.filters.threshold_local(
            image, block_size,
            method=self.average.methodparam(),
            offset=self.offset,
            param=self.average.paramparam())

registeredclass.Registration(
    'Local',
    ThresholdMethod,
    LocalThreshold,
    ordering=4,
    params=[
        parameter.PositiveIntParameter(
            'radius', 10,
            tip='Half width of the local neighborhood.'),
        parameter.RegisteredParameter(
            'average', LocalAverageMethod,
            tip="How to compute local average brightness."),
        parameter.FloatRangeParameter(
            'offset', (-1,1,.01), value=0,
            tip='Offset from the mean')
    ],
    tip="Use a different threshold at each point, computed from the local neighborhood.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/image/reg/thresholdlocal.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class IsoDataThreshold(ThresholdMethod):
    def threshold(self, image):
        return skimage.filters.threshold_isodata(image)

registeredclass.Registration(
    'Isodata',
    ThresholdMethod,
    IsoDataThreshold,
    ordering=5,
    tip="Automatically select a threshold via the Ridler-Calvert method.",
    discussion=xmlmenudump.loadFile(
        "DISCUSSIONS/image/reg/thresholdisodata.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class OtsuThreshold(ThresholdMethod):
    def threshold(self, image):
        return skimage.filters.threshold_otsu(image)

registeredclass.Registration(
    'Otsu',
    ThresholdMethod,
    OtsuThreshold,
    ordering=6,
    tip="Choose a threshold T such that the average of the means of the intensities below and above T equals T.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/image/reg/thresholdotsu.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class TriangleThreshold(ThresholdMethod):
    def __init__(self, nbins):
        self.nbins = nbins
    def threshold(self, image):
        return skimage.filters.threshold_triangle(image, self.nbins)

registeredclass.Registration(
    "Triangle",
    ThresholdMethod,
    TriangleThreshold,
    ordering=7,
    params=[
        parameter.PositiveIntParameter(
            'nbins', 256, tip="Number of histogram bins")
        ],
    tip="Use the triangle method to compute the threshold value.",
    discussion=xmlmenudump.loadFile(
        "DISCUSSIONS/image/reg/thresholdtriangle.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# https://ieeexplore.ieee.org/document/366472

class YenThreshold(ThresholdMethod):
    def __init__(self, nbins):
        self.nbins = nbins
    def threshold(self, image):
        return skimage.filters.threshold_yen(image, self.nbins)

registeredclass.Registration(
    "Yen",
    ThresholdMethod,
    YenThreshold,
    ordering=8,
    params=[
        parameter.PositiveIntParameter(
            'nbins', 256, tip="Number of histogram bins")
        ],
    tip="Use Yen's method to compute the threshold value.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/image/reg/thresholdyen.xml")
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class Threshold(imagemodifier.ImageModifierToGray):
    def __init__(self, method):
        self.method = method
    def modify(self, image):  # arg is an OOFImage
        grayscale = imagemodifier.rgb2gray(image.npImage())
        t = self.method.threshold(grayscale)
        return skimage.util.img_as_float(grayscale > t)
                                    
registeredclass.Registration(
    'Threshold',
    imagemodifier.ImageModifier,
    Threshold,
    ordering=100,
    params=[
        parameter.RegisteredParameter("method", ThresholdMethod,
                                      tip="How to compute the threshold")
        ],
    tip="Make all pixels brighter than a given threshold white, and all others black.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/threshold.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# ThresholdImage is the old OOF2 method from before we were using
# scikit-image. It was functionally identical to Threshold with
# method=ManualThreshold.  The menuitem is preserved for backwards
# compatibility.

class ThresholdImage(imagemodifier.ImageModifierToGray):
    def __init__(self, T):
        self.T=T
    def modify(self, image):
        mod = Threshold(method=ManualThreshold(value=self.T))
        return mod(image)

registeredclass.Registration(
    'ThresholdImage',
    imagemodifier.ImageModifier,
    ThresholdImage,
    ordering = 100,
    secret = True,
    params = [
        parameter.FloatRangeParameter('T', (0,1,.01),
                                      value=0.5, tip="Threshold value.") ],
    tip = "Threshold the pixel values to obtain a black and white image.",
    #discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/threshold.xml')
    )

