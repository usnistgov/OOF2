# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import switchboard
from ooflib.SWIG.common import config
from ooflib.SWIG.image import oofimage
from ooflib.common import debug
from ooflib.common import enum
from ooflib.common import parallel_enable
from ooflib.common import registeredclass
from ooflib.common import utils
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.image import imagecontext

import numpy
import skimage
import sys

# Base class for image modification methods.  Subclasses of
# ImageModifier need to have a __call__ method that takes an OOFImage
# argument and returns the modified numpy array.

class ImageModifier(registeredclass.RegisteredClass):
    registry = []
    def __call__(self, image):
        pass

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# OOFMenu callback, installed automatically for each ImageModifier
# class by the switchboard callback invoked when the class is
# registered.

def doImageMod(menuitem, image, **params):
    if parallel_enable.enabled():
        from ooflib.image.IO import oofimageIPC
        paramenu = oofimageIPC.modmenu.getItem(menuitem.name)
        paramenu(image=image, **params)

    # image is the image name, actually
    imagectxt = imagecontext.imageContexts[image]
    imagectxt.reserve()
    try:
        immidge = imagectxt.getObject()  # OOFImage object
        # Create a new OOFImage object to hold the modified image.
        # Originally it's just a copy of the unmodified image.
        ## TODO NUMPY: Create the new image with a read-only view of
        ## the original numpy data.  The modifier can act on the
        ## orginal data as long as it doesn't change it in place.
        if config.use_skimage():
            nporiginal = immidge.npImage()
            npcopy = nporiginal.copy()
            newimmidge = immidge.clone(immidge.name(), npcopy)
        else:
            newimmidge = immidge.clone(immidge.name())
            
        registration = menuitem.data
        imageModifier = registration(**params) # create ImageModifier obj
        imagectxt.begin_writing()
        try:
            modified = imageModifier(newimmidge) # perform the modification
            assert modified is not None
            # Make a copy of numpy array if needed to be sure that the
            # modified numpy image is not a view of another array and
            # is contiguous.
            if modified.base is not None or not modified.flags.c_contiguous:
                consolidated = modified.copy()
                newimmidge.setNpImage(consolidated)
            else:
                newimmidge.setNpImage(modified)
            oofimage.pushModification(image, newimmidge)
        finally:
            imagectxt.end_writing()
    finally:
        imagectxt.cancel_reservation()
    switchboard.notify('modified image', imageModifier, image)
    switchboard.notify('redraw')

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
#
# ImageModifier subclasses and their Registrations
#
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class FlipDirection(enum.EnumClass(
    ('x', 'Flip the image about the x axis'),
    ('y', 'Flip the image about the y axis'),
    ('xy', 'Flip the image about both the x and y axes (ie, rotate by 180 degrees)'))):
    tip = "Axis about which to flip an Image."
    discussion = """<para>
    <classname>FlipDirection</classname> is used by <xref
    linkend='MenuItem-OOF.Image.Modify.Flip'/> to specify how to flip
    an &image;.
    </para>"""

class FlipImage(ImageModifier):
    def __init__(self, axis):           # constructor
        self.axis = axis                # 'x', 'y', or 'xy'
    def __call__(self, image):          # called by doImageMod
        if self.axis == 'x':
            return numpy.flip(image.npImage(), 1)
        if self.axis == 'y':
            return numpy.flip(image.npImage(), 0)
        # flip both
        newimg = numpy.flip(image.npImage(), 0)
        return numpy.flip(newimg, 1)

# Registering the FlipImage class like this installs it in the menus
# and GUI.  The names of the Parameters in the params list *must* be
# the same as the arguments to the __init__ method.

registeredclass.Registration(
    'Flip',    # name appearing in menus & GUI
    ImageModifier, # base class
    FlipImage, # derived class
    ordering=1.0, # position in menus
    params=[   # list of constructor arguments
    enum.EnumParameter('axis',         # argument name
                       FlipDirection,     # argument type
                       FlipDirection('x'), # initial value
                       tip="Flip the image about this axis") # helpful hint
    ],
    tip="Flip the image about the x or y axis.",
    discussion="""<para>
    Flip an &image; about its center line, in either the x or y direction.
    </para>"""
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class GrayImage(ImageModifier):
    def __call__(self, image):
        # The skimage rgb2gray routine computes the luminance for
        # "contemporary CRT phosphors", defined by Y = 0.2125 R +
        # 0.7154 G + 0.0721 B.  The old, pre-numpy, version used
        # CColor::getGray(), which just averages R, G, and B.
        # TODO NUMPY: Is it important to preserve the old behavior?
        # gray = skimage.color.rgb2gray(image.npImage())
        # return skimage.color.gray2rgb(gray)

        # This reproduces the old behavior:
        npdata = image.npImage()
        gray = (npdata[:,:,0] + npdata[:,:,1] + npdata[:,:,2])/3.
        return skimage.color.gray2rgb(gray)
            
registeredclass.Registration(
    'Gray',
    ImageModifier,
    GrayImage,
    ordering=0.5,
    tip='Convert image to gray scale.',
    discussion=""" <para>
    Convert a color &image; to gray.  Each pixel color is replaced by
    a gray value equal to the average of the color's red, green, and
    blue components.
    </para>"""
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class FadeImage(ImageModifier):
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, image):
        return 1. - (1-image.npImage())*(1-self.factor)

registeredclass.Registration(
    'Fade',
    ImageModifier,
    FadeImage,
    ordering=1.1,
    params=[parameter.FloatRangeParameter('factor', (0, 1, 0.01), 0.1,
                   tip="0 does nothing, 1 fades to white.")],
    tip="Fade the image by the given factor.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/fadeimage.xml'))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class DimImage(ImageModifier):
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, image):
        return image.npImage() * self.factor

registeredclass.Registration(
    'Dim',
    ImageModifier,
    DimImage,
    ordering=1.2,
    params=[parameter.FloatRangeParameter('factor', (0, 1, 0.01), value=0.9,
                        tip="0 fades to black, 1 does nothing.")
    ],
    tip="Dim the image by the given factor.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/dimimage.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class BlurImage(ImageModifier):
    def __init__(self, radius, sigma):
        self.radius = radius
        self.sigma = sigma
    def __call__(self, image):
        # The skimage 'truncate' parameter is the radius of the filter
        # in units of the standard deviation.  The old ImageMagick
        # 'radius' parameter was the radius in pixels, not counting
        # the central pixel.
        return skimage.filters.gaussian(image.npImage(),
                                        self.sigma,
                                        truncate=(self.radius+1)/self.sigma,
                                        channel_axis=-1)

registeredclass.Registration(
    'Blur',
    ImageModifier,
    BlurImage,
    ordering=2.00,
    params=[parameter.FloatParameter('radius', 0.0,
      tip="Radius of the Gaussian, in pixels, not counting the center pixel."),
            parameter.FloatParameter('sigma', 1.0,
      tip="Standard deviation of the Gaussian, in pixels")
    ],
    tip="Blur an image by convolving it with a Gaussian operator of the given radius and standard deviation (sigma).",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/blurimage.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ContrastImage(ImageModifier):
    def __init__(self, sharpen):
        self.sharpen = sharpen
    def __call__(self, image):
        image.contrast(self.sharpen)

registeredclass.Registration(
    'Contrast',
    ImageModifier,
    ContrastImage,
    ordering=2.02,
    params=[parameter.BooleanParameter('sharpen', 1,
                                       tip='false to dull, true to sharpen')
            ],
    tip="Enhance intensity differences.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/contrast.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class DespeckleImage(ImageModifier):
    def __call__(self, image):
        image.despeckle()

registeredclass.Registration(
    'Despeckle',
    ImageModifier,
    DespeckleImage,
    ordering=2.03,
    tip= "Reduce the speckle noise while preserving the edges in an image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/despeckle.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class EdgeImage(ImageModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, image):
        image.edge(self.radius)

registeredclass.Registration(
    'Edge',
    ImageModifier,
    EdgeImage,
    ordering=2.031,
    params=[parameter.FloatParameter('radius', 0.0,
                                     tip="Radius for the operation.")
            ],
    tip="Find edges in an image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/edge.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class EnhanceImage(ImageModifier):
    def __call__(self, image):
        image.enhance()

registeredclass.Registration(
    'Enhance',
    ImageModifier,
    EnhanceImage,
    ordering=2.04,
    tip='Enhance the image by minimizing noise.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/enhance.xml')
    )

class EqualizeImage(ImageModifier):
    def __call__(self, image):
        image.equalize()

registeredclass.Registration(
    'Equalize',
    ImageModifier,
    EqualizeImage,
    ordering=2.05,
    tip='Apply histogram equalization to the image.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/equalize.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MedianFilterImage(ImageModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, image):
        image.medianFilter(self.radius)

if config.dimension() == 2:
    filterparam =[parameter.FloatParameter('radius', 1.0,
                                           tip="Radius of the filter.")]
elif config.dimension() == 3:
    filterparam =[parameter.IntParameter('radius', 1,
                                           tip="Radius of the filter.")]
    
registeredclass.Registration(
    'MedianFilter',
    ImageModifier,
    MedianFilterImage,
    ordering=2.06,
    params=filterparam,
    tip="Reduce noice by replacing each pixel color with its median over a local region.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/median.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NegateImage(ImageModifier):
    def __call__(self, image):
        return 1. - image.npImage()
        
registeredclass.Registration(
    'Negate',
    ImageModifier,
    NegateImage,
    ordering=2.065,
    tip="Negate the colors in the image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/negate.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NormalizeImage(ImageModifier):
    def __call__(self, image):
        image.normalize()
registeredclass.Registration(
    'Normalize',
    ImageModifier,
    NormalizeImage,
    ordering=2.07,
    tip="Enhance contrast by normalizing the image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/normalize.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ReduceNoise(ImageModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, image):
        image.reduceNoise(self.radius)

registeredclass.Registration(
    'ReduceNoise',
    ImageModifier,
    ReduceNoise,
    ordering=2.08,
    params=[parameter.FloatParameter('radius', 0.0,
                                     tip='Size of the pixel neighborhood.')],
    tip="Reduce noise while preserving edges.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/reducenoise.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class SharpenImage(ImageModifier):
    def __init__(self, radius, sigma):
        self.radius = radius
        self.sigma = sigma
    def __call__(self, image):
        image.sharpen(self.radius, self.sigma)
registeredclass.Registration(
    'Sharpen',
    ImageModifier,
    SharpenImage,
    ordering=2.09,
    params=[parameter.FloatParameter('radius', 0.0,
                                     tip='Radius of the Gaussian.'),
            parameter.FloatParameter('sigma', 1.0,
                                     tip='Standard deviation of the Gaussian.')
    ],
    tip="Sharpen the image by convolving with a Gaussian.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/sharpen.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ReIlluminateImage(ImageModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, image):
        image.evenly_illuminate(self.radius)

registeredclass.Registration(
    'Reilluminate',
    ImageModifier,
    ReIlluminateImage,
    ordering=3.0,
    params=[parameter.IntParameter('radius', 10,
                                   tip='Size of the averaging region.')
            ],
    tip='Adjust brightness so that the whole image is evenly illuminated.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/reilluminate.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ThresholdImage(ImageModifier):
    def __init__(self, T):
        self.T=T
    def __call__(self, image):
        if config.dimension() == 2:
            dbls = oofimage.grayify(image)
            bools = oofimage.threshold(dbls,self.T)
            oofimage.setFromBool(image,bools)
        elif config.dimension() == 3:
            image.threshold(self.T)
        
registeredclass.Registration(
    'ThresholdImage',
    ImageModifier,
    ThresholdImage,
    ordering=100,
    params=[parameter.FloatRangeParameter('T', (0,1,.01),value=.5,
                                          tip="Threshold value."),
            ],
    tip="Threshold an image given a threshold value.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/threshold.xml')
    )


