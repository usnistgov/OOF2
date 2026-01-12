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
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.image import oofimage
from ooflib.common import debug
from ooflib.common import oofenum
from ooflib.common import parallel_enable
from ooflib.common import registeredclass
from ooflib.common.IO import automatic
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.image import imagecontext

import numpy
import skimage
import sys

## TODO NUMPY: Review the tips and discussions for all classes.  Some
## still refer to the ImageMagick versions.

## TODO NUMPY: Can we use @skimage.adapt_rgb?
## https://scikit-image.org/docs/0.25.x/auto_examples/color_exposure/plot_adapt_rgb.html

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Base class for image modification methods.  Subclasses of
# ImageModifier need to have a "modify" method that takes an OOFImage
# argument and returns the modified numpy array.  The modified array
# can be the same object as the original array.

class ImageModifier(registeredclass.RegisteredClass):
    registry = []
    def modify(self, image):
        raise ooferror.PyErrPyProgrammingError(
            f"Modify method not defined for {self.__class__.__name__}.")

# ImageModifiers come in three flavors.  They may always produce a
# gray scale image, or always create an RGB image, or preserve the
# type of data in the original image.  The argument to resultIsGray is
# True if the original image is gray.
#
# newData() creates a new numpy array for the new image to use.  It is
# *not* necessary for ImageModifiers to call newData() if they have a
# better way to create the array.

class ImageModifierToGray(ImageModifier):
    def resultIsGray(self, original):
        return True
    def newData(self, oldImage):
        olddata = oldImage.npImage()
        if oldImage.isGray():
            return olddata.copy()
        # Converting RGB to gray.
        shape = olddata.shape[0:2]
        return numpy.empty(shape, olddata.dtype)

class ImageModifierToRGB(ImageModifier):
    def resultIsGray(self, original):
        return False
    def newData(self, oldImage):
        olddata = oldImage.npImage()
        if not oldImage.isGray():
            return olddata.copy()
        # Converting gray to RGB.
        shape = olddata.shape + (3,)
        return numpy.empty(shape, olddata.dtype)

class ImageModifierToEither(ImageModifier):
    def resultIsGray(self, original):
        return original
    def newData(self, oldImage):
        return oldImage.npImage().copy()

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

    # Create the ImageModifier object. menuitem.data is the
    # ImageModifier Registration, set in
    # imagemenu.buildImageModMenu().
    imageModifier = menuitem.data(**params)

    try:
        immidge = imagectxt.getObject()  # OOFImage object
        nporiginal = immidge.npImage()

        # Is the original gray or RGB?
        grayOriginal = immidge.isGray()
        # Is the result going to be gray or RGB?
        grayResult = imageModifier.resultIsGray(grayOriginal)

        imagectxt.begin_writing()
        try:
            # imageModifier.__call__() takes the old OOFImage object
            # and returns the numpy array for the new OOFImage object.
            # It can use newData() to create the array if necessary.
            modified = imageModifier.modify(immidge)
            assert modified is not None

            # Make a copy of the numpy array if necessary, to ensure
            # that the modified array is not a view of another array
            # and is contiguous.
            if modified.base is not None or not modified.flags.c_contiguous:
                modified = modified.copy()

            newimmidge = oofimage.OOFImage(immidge.name(), modified, grayResult)
            newimmidge.setSize(immidge.size())
            
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


class FlipDirection(oofenum.EnumClass(
    ('x', 'Flip the image about the x axis'),
    ('y', 'Flip the image about the y axis'),
    ('xy', 'Flip the image about both the x and y axes (ie, rotate by 180 degrees)'))):
    tip = "Axis about which to flip an Image."
    discussion = """<para>
    <classname>FlipDirection</classname> is used by <xref
    linkend='MenuItem-OOF.Image.Modify.Flip'/> to specify how to flip
    an &image;.
    </para>"""

class FlipImage(ImageModifierToEither):
    def __init__(self, axis):           # constructor
        self.axis = axis                # 'x', 'y', or 'xy'
    def modify(self, image):          # called by doImageMod
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
    ordering = 1.0, # position in menus
    params = [   # list of constructor arguments
    oofenum.EnumParameter('axis',             # argument name
                          FlipDirection,      # argument type
                          FlipDirection('x'), # initial value
                          tip="Flip the image about this axis") # helpful hint
    ],
    tip = "Flip the image about the x or y axis.",
    discussion = """<para> Flip an &image; about its center line, in
    either the x or y direction, or both. </para>"""
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def rgb2gray(image):
    # The skimage rgb2gray routine computes the luminance for
    # "contemporary CRT phosphors", defined by Y = 0.2125 R + 0.7154 G
    # + 0.0721 B.  The old, pre-numpy, version used CColor::getGray(),
    # which just averages R, G, and B. 

    if len(image.shape) == 2:
        return image
    return (image[:,:,0] + image[:,:,1] + image[:,:,2])/3.

class GrayImage(ImageModifierToGray):
    def modify(self, image):
        return rgb2gray(image.npImage())

registeredclass.Registration(
    'Gray',
    ImageModifier,
    GrayImage,
    ordering = 0.5,
    tip = 'Convert image to grayscale.',
    discussion = """ <para>
    Convert a color &image; to grayscale by averaging each pixel's red,
    green, and blue components.
    </para>"""
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class FadeImage(ImageModifierToEither):
    def __init__(self, factor):
        self.factor = factor
    def modify(self, image):
        return 1.0 - (1-image.npImage())*(1-self.factor)

registeredclass.Registration(
    'Fade',
    ImageModifier,
    FadeImage,
    ordering = 1.1,
    params = [
        parameter.FloatRangeParameter(
            'factor', (0, 1, 0.01), 0.1,
            tip="0 does nothing, 1 fades to white.")
    ],
    tip = "Fade the image by the given factor.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/fadeimage.xml'))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class DimImage(ImageModifierToEither):
    def __init__(self, factor):
        self.factor = factor
    def modify(self, image):
        return image.npImage() * self.factor

registeredclass.Registration(
    'Dim',
    ImageModifier,
    DimImage,
    ordering = 1.2,
    params = [
        parameter.FloatRangeParameter('factor', (0, 1, 0.01), value=0.9,
                                      tip="0 fades to black, 1 does nothing.")
    ],
    tip = "Dim the image by the given factor.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/dimimage.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class BlurImage(ImageModifierToEither):
    def __init__(self, radius, sigma):
        self.radius = radius
        self.sigma = sigma
    def modify(self, image):
        # The skimage 'truncate' parameter is the radius of the filter
        # in units of the standard deviation.  The old ImageMagick
        # 'radius' parameter was the radius in pixels, not counting
        # the central pixel.

        # scikit-image docs for channel_axis: If None, the image is
        # assumed to be a grayscale (single channel) image. Otherwise,
        # this parameter indicates which axis of the array corresponds
        # to channels.
        img = skimage.filters.gaussian(
            image.npImage(),
            self.sigma,
            truncate=(self.radius+1)/self.sigma,
            channel_axis = None if image.isGray() else -1)
        img = numpy.minimum(img, 1.0)
        img = numpy.maximum(img, 0.0)
        return img

registeredclass.Registration(
    'Blur',
    ImageModifier,
    BlurImage,
    ordering = 2.00,
    params = [
        parameter.PositiveFloatParameter(
            'radius', 1.0,
            tip="Radius of the Gaussian, in pixels, not counting the center pixel."),
        parameter.PositiveFloatParameter(
            'sigma', 1.0,
            tip="Standard deviation of the Gaussian, in pixels")
    ],
    tip = "Blur an image by convolving it with a Gaussian.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/blurimage.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# AddNoise can be used to generate images for the test suite.  It's
# probably not useful otherwise.

class AddNoise(ImageModifierToEither):
    def __init__(self, sigma, seed):
        self.sigma = sigma
        self.seed = seed
    def modify(self, image):
        seed = None if self.seed == automatic.automatic else self.seed
        img = skimage.util.random_noise(image.npImage(), var=self.sigma**2,
                                        rng=seed)
        img = numpy.minimum(img, 1.0)
        img = numpy.maximum(img, 0.0)
        return img

registeredclass.Registration(
    'AddNoise',
    ImageModifier,
    AddNoise,
    ordering=10000,
    params = [
        parameter.PositiveFloatParameter('sigma', 0.1,
                                 tip="Width of the noise distribution"),
        parameter.AutoIntParameter('seed', automatic.automatic,
                                   tip="Seed for the random number generator")
        ],
    tip = "Add random noise to the image",
    discussion=
    """<para>
    This is used to generate images for the test suite.  Gaussian
    noise with deviation <varname>sigma</varname> is added to each
    pixel.  If <varname>seed</varname> is &automatic; the random number
    generator is not reinitialized before use.
    </para>"""
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Enhance contrast, using the algorithm described (sort of) in the
# scikit-image documentation, without using the scikit-image
# routines. Scikit-image replaces each pixel by the local maximum if
# the pixel *gray value* is closer to the local maximum than the local
# minimum. Otherwise it replaces it by the local minimum.
# OOFImage::enhance_contrast() applies the method to each channel
# separately.  Also, it doesn't require converting the image data to 8
# bits.
#
# https://scikit-image.org/docs/stable/api/skimage.filters.rank.html#skimage.filters.rank.enhance_contrast


class ContrastImage(ImageModifierToEither):
    def __init__(self, radius):
        self.radius = radius

    def modify(self, image):
        newimage = numpy.empty_like(image.npImage())
        image.enhance_contrast(skimage.morphology.disk(self.radius), newimage)
        return newimage
                
registeredclass.Registration(
    'Contrast',
    ImageModifier,
    ContrastImage,
    ordering = 2.0,
    secret = False,
    params = [
        parameter.PositiveIntParameter(
            'radius', 5,
            tip='Radius of the pixel neighborhood')
    ],
    tip = "Enhance intensity differences using scikit-image.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/contrast.xml')
)


# This version of ContrastImage only uses Python calls to numpy and
# scikit-image routines.  It is faster than the other version but
# only works with 8 bit images, so there is a loss of precision.  It's
# here for future reference, but marked "secret".

class ContrastImageSK(ImageModifierToEither):
    def __init__(self, radius):
        self.radius = radius
    def modify(self, image):
        np_image = image.npImage()
        new_image = numpy.empty_like(np_image)
        # Not converting the image, or converting it to 16-bit ints
        # produces warning messages from scikit-image.
        image_as_bytes = skimage.util.img_as_ubyte(np_image)
        disk = skimage.morphology.disk(self.radius,
                                       dtype=image_as_bytes.dtype)
        # Each image channel needs to be handled separately.
        for k in range(np_image.shape[2]):
            new_image[...,k] = skimage.filters.rank.enhance_contrast(
                                         image_as_bytes[...,k], disk)/255.0
        return skimage.util.img_as_float64(new_image)
    
registeredclass.Registration(
    'ContrastSK',
    ImageModifier,
    ContrastImageSK,
    ordering = 2.021,
    secret = True,              
    params = [
        parameter.PositiveIntParameter(
            'radius', 5,
            tip='Radius of the pixel neighborhood')
    ],
    tip = "Enhance intensity differences using scikit-image.",
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class Edge(ImageModifierToEither):
    def modify(self, image):
        return skimage.filters.sobel(image.npImage())

registeredclass.Registration(
    'Edge',
    ImageModifier,
    Edge,
    ordering=2.031,
    tip="Use a Sobel filter to find edges in an image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/edge.xml'))

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class EqualizeImage(ImageModifierToEither):
    def modify(self, image):
        return skimage.exposure.equalize_adapthist(image.npImage())

registeredclass.Registration(
    'Equalize',
    ImageModifier,
    EqualizeImage,
    ordering = 2.05,
    tip = 'Apply adaptive histogram equalization to the image.',
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/equalize.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MedianFilterImage(ImageModifierToEither):
    def __init__(self, radius):
        self.radius = radius
    def modify(self, image):
        disk = skimage.morphology.disk(self.radius)
        npimage = image.npImage()
        newimage = numpy.empty_like(npimage)
        if image.isGray():
            newimage = skimage.filters.median(npimage, disk)
        else:
            for k in range(npimage.shape[2]):
                newimage[:,:,k] = skimage.filters.median(npimage[:,:,k], disk)
        return newimage

registeredclass.Registration(
    'MedianFilter',
    ImageModifier,
    MedianFilterImage,
    ordering = 2.06,
    params = [
        parameter.PositiveIntParameter(
            'radius', 2,
            tip="Radius of the median filter in units of the pixel size.") ],
    tip = "Reduce noise by replacing each pixel color with the median over a local region.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/median.xml'),
    xrefs=["MenuItem-OOF.Image.Modify.Denoise"]
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NegateImage(ImageModifierToEither):
    def modify(self, image):
        return 1.0 - image.npImage()

registeredclass.Registration(
    'Negate',
    ImageModifier,
    NegateImage,
    ordering = 2.065,
    tip = "Negate the colors in the image.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/negate.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NormalizeImage(ImageModifierToEither):
    def modify(self, image):
        return skimage.exposure.rescale_intensity(
            image.npImage(),
            in_range='image',
            out_range=(0.0, 1.0))

registeredclass.Registration(
    'Normalize',
    ImageModifier,
    NormalizeImage,
    ordering = 2.07,
    tip = "Normalize the image by rescaling pixel intensity values.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/normalize.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class SharpenMode(oofenum.EnumClass(
        ('RGB', 'Sharpen the RGB channels separately.'),
        ('HSV', 'Sharpen the Value channel only.'))):
    tip="How to apply the unsharp_mask algorithm"
    discussion="""
    Possible values of the <varname>mode</varname> parameter for <xref
    linkend="MenuItem-OOF.Image.Modify.Sharpen"/>.
    """
                  
class SharpenImage(ImageModifierToEither):
    def __init__(self, radius, amount, mode):
        self.radius = radius
        self.amount = amount
        self.mode = mode
    def modify(self, image):
        # Mode is irrelevant for gray images.
        if image.isGray():
            return skimage.filters.unsharp_mask(
                image.npImage(), self.radius, self.amount)
        
        # Scikit-image documentation says: When applying this filter
        # to several color layers independently, color bleeding may
        # occur. More visually pleasing result can be achieved by
        # processing only the brightness/lightness/intensity channel
        # in a suitable color space such as HSV, HSL, YUV, or YCbCr.

        if self.mode == 'HSV':
            hsv = skimage.color.rgb2hsv(image.npImage())
            # Documentation for the radius arg says: "If sequence is
            # given, then there must be exactly one radius for each
            # dimension except the last dimension for multichannel
            # images. Note that 0 radius means no blurring, and
            # negative values are not allowed."  This does not seem to
            # work, so extract just the V data and pass it to the
            # filter by itself.
            sharp = hsv.copy()
            sharp[...,-1] = skimage.filters.unsharp_mask(
                hsv[...,-1],
                self.radius,
                self.amount)
            return skimage.color.hsv2rgb(sharp)
        # mode == RGB 
        newImage = skimage.filters.unsharp_mask(
            image.npImage(), self.radius, self.amount,
            channel_axis=2)
        return newImage

registeredclass.Registration(
    'Sharpen',
    ImageModifier,
    SharpenImage,
    ordering = 2.09,
    params = [
        parameter.PositiveFloatParameter(
            'radius', 5.0,
            tip='Radius of the Gaussian blur, in pixels.'),
        parameter.PositiveFloatParameter(
            'amount', 1.0,
            tip='Amplification factor for image details.'),
        oofenum.EnumParameter(
            'mode',
            SharpenMode,
            SharpenMode('HSV'),
            tip='Sharpen RGB channels or just the V from HSV.')
    ],
    tip = "Sharpen the image by comparing it to a blurred version of itself.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/sharpen.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# ReIlluminateImage scales the brightness of each pixel by the ratio
# of the global average brightness to the local average brightness,
# which is computed in a region around the pixel.  This has the effect
# of correcting a micrograph that was made with non-uniform
# illumination.  It can create artifacts, though.

class ReIlluminateImage(ImageModifierToEither):
    def __init__(self, radius):
        self.radius = radius

    def getFactors(self, imgbytes, dtype):
        mask = skimage.morphology.disk(self.radius)
        globalavg = numpy.mean(imgbytes)
        localavg = skimage.filters.rank.mean(imgbytes, mask)
        nonzeromask = localavg!=0 # where the local average isn't 0
        factors = numpy.ones(imgbytes.shape, dtype)
        factors[nonzeromask] = globalavg/localavg[nonzeromask]
        return factors
        
    def modify(self, image):
        npimage = image.npImage()
        if image.isGray():
            factors = self.getFactors(skimage.util.img_as_ubyte(npimage),
                                      npimage.dtype)
            newimage = factors*npimage
        else:
            hsv = skimage.color.rgb2hsv(npimage)
            imgbytes = skimage.util.img_as_ubyte(hsv[...,2])
            factors = self.getFactors(imgbytes, npimage.dtype)
            hsv[...,2] = factors*hsv[...,2]
            newimage = skimage.color.hsv2rgb(hsv)

        return skimage.exposure.rescale_intensity(
            newimage, in_range='image', out_range=(0.0, 1.0))


registeredclass.Registration(
    'Reilluminate',
    ImageModifier,
    ReIlluminateImage,
    ordering = 3.0,
    params = [
        parameter.PositiveIntParameter(
            'radius', 10,
            tip='Radius of the averaging region in pixels.')
    ],
    tip = 'Adjust brightness so that the whole image is evenly illuminated.',
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/reilluminate.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# When we used ImageMagick we had a Despeckle command for which
# there's no scikit-image equivalent.  The ImageMagick routine is
# described at https://imagemagick.org/api/effect.php, which says:
#   DespeckleImage() reduces the speckle noise in an image while
#   preserving the edges of the original image. A speckle removing
#   filter uses a complementary hulling technique (raising pixels that
#   are darker than their surrounding neighbors, then complementarily
#   lowering pixels that are brighter than their surrounding
#   neighbors) to reduce the speckle index of that image (reference
#   Crimmins speckle removal).

# https://homepages.inf.ed.ac.uk/rbf/HIPR2/crimmins.htm has a detailed
# discussion of Crimmins.  It seems to require a small bit depth and
# is otherwise pretty ugly, so it won't be implemented here unless
# requested.

