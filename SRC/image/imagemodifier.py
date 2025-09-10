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

# Base class for image modification methods.  Subclasses of
# ImageModifier need to have a __call__ method that takes an OOFImage
# argument and returns the modified numpy array.  The modified array
# can be the same object as the original array.
## TODO: Have the image modifiers always operate in-place, and don't
## have anything returned from imageModifier.__call__.  The input data
## to the modifiers is already a copy of the original image.
## Modifiers that need to make a temporary copy can do so if they
## want.  OTOH: It's easier to create a new numpy array in Python and
## pass it inas an argument.

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
        nporiginal = immidge.npImage()
        npcopy = nporiginal.copy()
        newimmidge = immidge.clone(immidge.name(), npcopy)

        registration = menuitem.data
        imageModifier = registration(**params) # create ImageModifier obj
        imagectxt.begin_writing()
        try:
            # imageModifier.__call__ performs the modification on
            # newimmidge's numpy data, and returns the modified data.
            modified = imageModifier(newimmidge)
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
    ordering = 1.0, # position in menus
    params = [   # list of constructor arguments
    oofenum.EnumParameter('axis',             # argument name
                          FlipDirection,      # argument type
                          FlipDirection('x'), # initial value
                          tip="Flip the image about this axis") # helpful hint
    ],
    tip = "Flip the image about the x or y axis.",
    discussion = """<para>
    Flip an &image; about its center line, in either the x or y direction.
    </para>"""
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def rgb2gray(image):
    # The skimage rgb2gray routine computes the luminance for
    # "contemporary CRT phosphors", defined by Y = 0.2125 R + 0.7154 G
    # + 0.0721 B.  The old, pre-numpy, version used CColor::getGray(),
    # which just averages R, G, and B.  TODO NUMPY: Is it important to
    # preserve the old behavior?

    # return skimage.color.rgb2gray(image)
    return (image[:,:,0] + image[:,:,1] + image[:,:,2])/3.

class GrayImage(ImageModifier):
    def __call__(self, image):
        gray = rgb2gray(image.npImage())
        # OOF2 uses RGB images, even if R=G=B.
        return skimage.color.gray2rgb(gray)

registeredclass.Registration(
    'Gray',
    ImageModifier,
    GrayImage,
    ordering = 0.5,
    tip = 'Convert image to gray scale.',
    discussion = """ <para>
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

class DimImage(ImageModifier):
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, image):
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

class BlurImage(ImageModifier):
    def __init__(self, radius, sigma):
        self.radius = radius
        self.sigma = sigma
    def __call__(self, image):
        # The skimage 'truncate' parameter is the radius of the filter
        # in units of the standard deviation.  The old ImageMagick
        # 'radius' parameter was the radius in pixels, not counting
        # the central pixel.
        img = skimage.filters.gaussian(
            image.npImage(),
            self.sigma,
            truncate=(self.radius+1)/self.sigma,
            channel_axis=-1)
        img = numpy.minimum(img, 1.0)
        img = numpy.maximum(img, 0.0)
        return img

registeredclass.Registration(
    'Blur',
    ImageModifier,
    BlurImage,
    ordering = 2.00,
    params = [
        parameter.FloatParameter(
            'radius', 0.0,
            tip="Radius of the Gaussian, in pixels, not counting the center pixel."),
        parameter.FloatParameter(
            'sigma', 1.0,
            tip="Standard deviation of the Gaussian, in pixels")
    ],
    tip = "Blur an image by convolving it with a Gaussian operator of the given radius and standard deviation (sigma).",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/blurimage.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# AddNoise can be used to generate images for the test suite.  It's
# probably not useful otherwise.

## TODO NUMPY:  Don't add rgb noise to a gray image!

class AddNoise(ImageModifier):
    def __init__(self, sigma):
        self.sigma = sigma
    def __call__(self, image):
        img = skimage.util.random_noise(image.npImage(), var=self.sigma**2)
        img = numpy.minimum(img, 1.0)
        img = numpy.maximum(img, 0.0)
        return img

registeredclass.Registration(
    'AddNoise',
    ImageModifier,
    AddNoise,
    ordering=10000,
    params = [
        parameter.FloatParameter('sigma', 0.1,
                                 "Width of the noise distribution")
        ],
    tip = "Add random noise to the image",
    discussion=
    """<para>
    This is used to generate images for the test suite.
    It might be amusing elsewhere.
    </para>"""
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Enhance contrast, using the algorithm described in the scikit-image
# documentation.  Scikit-image replaces each pixel by the local
# maximum if the pixel gray value is closer to the local maximum than
# the local minimum. Otherwise it replaces it by the local minimum.
# OOFImage::enhance_contrast() applies the method to channel
# separately.  Also, it doesn't require converting the image data to 8
# bits.
#
# https://scikit-image.org/docs/stable/api/skimage.filters.rank.html#skimage.filters.rank.enhance_contrast


class ContrastImage(ImageModifier):
    def __init__(self, radius):
        self.radius = radius

    def __call__(self, image):
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
        parameter.PositiveFloatParameter(
            'radius', 5,
            tip='radius of the pixel neighborhood')
    ],
    tip = "Enhance intensity differences using scikit-image.",
    #discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/contrast.xml')
)


# This version of ContrastImage only uses Python calls to numpy and
# scikit-image routines.  It is faster than the other version but
# only works with 8 bit images, so there is a loss of precision.  It's
# here for future reference, but marked "secret".

class ContrastImageSK(ImageModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, image):
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
        parameter.PositiveFloatParameter(
            'radius', 5,
            tip='radius of the pixel neighborhood')
    ],
    tip = "Enhance intensity differences using scikit-image.",
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# The various scikit-image denoising methods are wrapped registered
# classes which are used as arguments to a single DenoiseImage
# ImageModifier.

class DenoiseMethod(registeredclass.RegisteredClass):
    registry = []

class DenoiseImage(ImageModifier):
    def __init__(self, method):
        self.method = method
    def __call__(self, image):
        return self.method.denoise(image)

registeredclass.Registration(
    'Denoise',
    ImageModifier,
    DenoiseImage,
    ordering = 2.08,
    params=[
        parameter.RegisteredParameter("method", DenoiseMethod,
                                      tip="How to denoise the image.")
        ],
    tip="Apply various methods to remove noise from an image.")

#=--=##=--=##=--=##=--=#

# Denoising methods

class DenoiseBilateral(DenoiseMethod):
    def __init__(self, window_size, sigma_color, sigma_spatial, bins):
        self.window_size = window_size
        self.sigma_color = sigma_color
        self.sigma_spatial = sigma_spatial
        self.bins = bins
    def denoise(self, image):
        return skimage.restoration.denoise_bilateral(
            image.npImage(),
            win_size = (None if self.window_size==automatic.automatic
                        else self.window_size),
            sigma_color = (None if self.sigma_color==automatic.automatic
                           else self.sigma_color),
            sigma_spatial = self.sigma_spatial,
            bins = self.bins,
            mode='reflect',
            channel_axis=-1)


registeredclass.Registration(
    'Bilateral',
    DenoiseMethod,
    DenoiseBilateral,
    ordering = 1,
    secret = False,              # TODO NUMPY: Why was this secret?
    params = [
        parameter.PositiveAutoIntParameter(
            'window_size', automatic.automatic,
            tip="Window size for filtering."
#            tip='Window size for filtering. If win_size is not specified (i.e. set to 0), it is calculated as max(5, 2 * ceil(3 * sigma_spatial) + 1)'
        ),
        parameter.PositiveAutoFloatParameter(
            'sigma_color', automatic.automatic,
            tip="Standard deviation for color distance. A larger value causes averaging of pixels with larger radiometric differences. If 'automatic', the standard deviation of the image will be used."
            # tip='Standard deviation for grayvalue/color distance (radiometric similarity). A larger value results in averaging of pixels with larger radiometric differences. If None, the standard deviation of image will be used.'
        ),
        parameter.PositiveFloatParameter(
            'sigma_spatial', 1.0,
            tip='Standard deviation for range distance. A larger value results in averaging of pixels with larger spatial differences.'),
        parameter.PositiveIntParameter(
            'bins', 10000,
            tip='Number of discrete values for Gaussian weights of color filtering. A larger value results in improved accuracy.')
        ],
    tip = "Denoise using bilateral filter to preserve edges.",
    # discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/denoisebilateral.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class TotalVariation(DenoiseMethod):
    def __init__(self, weight, eps, max_iterations):
        self.weight = weight
        self.eps = eps
        self.max_iterations = max_iterations
    def denoise(self, image):
        return skimage.restoration.denoise_tv_chambolle(
            image.npImage(),
            weight=self.weight,
            eps=self.eps,
            max_num_iter=self.max_iterations,
            channel_axis=-1)

registeredclass.Registration(
    'TotalVariation',
    DenoiseMethod,
    TotalVariation,
    ordering = 2.082,
    params = [
        parameter.FloatParameter(
            'weight', 0.1,
            tip='Larger values remove more noise, at the expense of image fidelity.'                     
#            tip='Denoising weight. It is equal to 1/lambda in the total variation model. Therefore, the greater the weight, the more denoising (at the expense of fidelity to image).'
        ),
        parameter.PositiveFloatParameter(
            'eps', 0.0002,
            tip='Stop iterating when the estimated error is below this value.',
#            tip='Tolerance eps>0 for the stop criterion (compares to absolute value of relative difference of the cost function for TV-denoising).'
        ),
        parameter.IntParameter(
            'max_iterations', 200,
            tip='Maximum number of iterations.')
        ],
    tip = "Denoise using total variation regularization, suitable for piecewise constant images.",
    #discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/denoisetv.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## NUMPY: Wavelet denoising appears not to work. It returns RGB
## values that are outside the range [0,1].

if False:
    class WaveletDenoisingMode(oofenum.EnumClass(
            ('soft',
             'Coefficients below the threshold set to zero. Others are reduced.'),
            ('hard',
             'Coefficients below the threshold are zeroed. Others are unchanged.'))
                               ):
        tip = 'The type of wavelet denoising to be performed.'
        discussion = """<para> <classname>WaveletDenoisingMode</classname>
        specifies the type of denoising performed by <xref
        linkend='RegisteredClass-Wavelet'/>.  </para>"""

    class WaveletThresholdingMethod(oofenum.EnumClass(
        ('BayesShrink', 'Adaptively apply thresholds to wavelet subbands'),
        ('VisuShrink',  'Apply a single threshold to all wavelet coefficients.'))):
        tip = 'The wavelet thresholding method to use.'
        discussion = """<para>
        <classname>WaveletThresholdingMethod</classname> specifies the
        thresholding method used by <xref
        linkend='RegisteredClass-Wavelet'/> denoising.  </para>"""

    class Wavelet(DenoiseMethod):
        def __init__(self, sigma, wavelet, mode, wavelet_levels, method):
            self.sigma = sigma #None if sigma==0 else sigma
            self.wavelet = wavelet
            self.mode = mode
            self.wavelet_levels = wavelet_levels #None if wavelet_levels==0 else wavelet_levels
            self.method = method
        def denoise(self, image):
            debug.fmsg(f"Calling denoise_wavelet, range=({image.npImage().min()}, {image.npImage().max()})")
            result= skimage.restoration.denoise_wavelet(
                image.npImage(),
                sigma= None if self.sigma == automatic.automatic else self.sigma,
                wavelet=self.wavelet,
                mode=self.mode.string(),
                wavelet_levels= (None if self.wavelet_levels == automatic.automatic
                                 else self.wavelet_levels),
                convert2ycbcr = True,
                method=self.method.string(),
                channel_axis=2)
            debug.fmsg(f"Back from denoise_wavelet, range=({result.min()}, {result.max()})")
            assert result.min() >= 0.0 and result.max() <= 1.0
            return result

    registeredclass.Registration(
        'Wavelet',
        DenoiseMethod,
        Wavelet,
        ordering = 2.083,
        params = [
            parameter.PositiveAutoFloatParameter(
                'sigma',
                automatic.automatic,
                tip='The standard deviation of the noise used when computing the wavelet detail coefficient threshold(s).'),
            ## TODO NUMPY: Change this to an EnumParameter and generate
            ## the values directly from pywt.wavelist?
            ##    import pywt; print(pywt.wavelist())
            ## There are very many possible values.  Better just to check
            ## the given value against the list, and/or print the list in
            ## an error message if the given value is illegal.
            parameter.StringParameter('wavelet', 'db1',
                tip='The type of wavelet to perform.  Type "import pywt; print(pywt.wavelist()" in the OOF2 console to see all the choices.'),
            oofenum.EnumParameter(
                'mode',
                WaveletDenoisingMode,
                WaveletDenoisingMode('soft'),
                tip='The type of wavelet denoising to be performed.'),
            parameter.PositiveAutoIntParameter(
                'wavelet_levels',
                automatic.automatic,
                tip='The number of wavelet decomposition levels to use.', # The default, specified by setting the value of 0, is three less than the maximum number of possible decomposition levels.'
            ),
            oofenum.EnumParameter(
                'method',
                WaveletThresholdingMethod,
                WaveletThresholdingMethod('BayesShrink'),
                tip='Thresholding method to be used.')
            ],
        tip = "Denoise using wavelet thresholding.",
        # discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/denoisewavelet.xml')
        )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NonlocalMeans(DenoiseMethod):
    def __init__(self, patch_size, patch_distance, h, sigma):
        self.patch_size = patch_size
        self.patch_distance = patch_distance
        self.h = h
        self.sigma = sigma
    def denoise(self, image):
        return skimage.restoration.denoise_nl_means(
            image.npImage(),
            patch_size=self.patch_size,
            patch_distance=self.patch_distance,
            fast_mode=True,
            h=self.h,
            sigma= (0 if self.sigma == automatic.automatic else self.sigma),
            channel_axis=-1)

registeredclass.Registration(
    'NonlocalMeans',
    DenoiseMethod,
    NonlocalMeans,
    ordering = 2.083,
    params = [
        parameter.PositiveIntParameter(
            'patch_size', 7,
            tip='Size of patches used for denoising.'),
        parameter.PositiveIntParameter(
            'patch_distance', 11,
            tip='Maximal distance in pixels where to search patches used for denoising.'),
        parameter.FloatParameter(
            'h', 0.1,
            tip="Cut-off distance (in gray levels). A higher h results in a smoother image."
#'Cut-off distance (in gray levels). The higher h, the more permissive one is in accepting patches. A higher h results in a smoother image, at the expense of blurring features. For a Gaussian noise of standard deviation sigma, a rule of thumb is to choose the value of h to be sigma or slightly less.'
        ),
        parameter.PositiveAutoFloatParameter(
            'sigma', automatic.automatic,
            tip='The standard deviation of the (Gaussian) noise.' # If provided, a more robust computation of patch weights is computed that takes the expected noise variance into account.'
        )
        ],
    tip = "Denoise using nonlocal means filtering (suitable for images with regions of repetitive texture).",
    # discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/denoisenonlocalmeans.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# ReduceNoise is kept for backward compatibility.  It's redundant with
# DenoiseNonlocalMeans.

## TODO NUMPY: The old documentation for the ImageMagick routine says
## "Smooth the contours of an image while still preserving edge
## information. The algorithm works by replacing each pixel with its
## neighbor closest in value. The neighbors of a pixel are defined as
## those pixels within the given radius, specified in units of the
## pixel size. A suitable radius will be chosen automatically if
## radius is zero."
##
## Is DenoiseNonlocalMeans really the correct substitute?

class ReduceNoise(ImageModifier):
    def __init__(self, radius=1.0):
        self.radius = radius
    def __call__(self, image):
        denoised_image = skimage.restoration.denoise_nl_means(
            image.npImage(),
            patch_size=7, patch_distance=11, fast_mode=True,
            h=0.1, sigma=0.0, channel_axis=-1)
        return denoised_image

registeredclass.Registration(
    'ReduceNoise',
    ImageModifier,
    ReduceNoise,
    ordering = 2.08,
    secret = True, 
    params = [parameter.FloatParameter('radius', 0.0,
                                       tip='Size of the pixel neighborhood.')],
    tip = "Reduce noise while preserving edges.",
    #discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/reducenoise.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class DespeckleImage(ImageModifier):
    def __init__(self, radius=2.0):
        self.radius = radius
    def __call__(self, image):
        disk = skimage.morphology.disk( self.radius )
        disk2 = skimage.color.gray2rgb( disk )
        return skimage.filters.median( image.npImage(), disk2 )

registeredclass.Registration(
    'Despeckle',
    ImageModifier,
    DespeckleImage,
    ordering = 2.03,
    secret = True, # we can remove this class b/c it is the same as medianFilter, thus redundant.
    #params = [parameter.FloatParameter('radius', 2.0, tip="Radius of the median filter.")],
    tip = "Reduce the speckle noise using a median filter.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/despeckle.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class EdgeImage(ImageModifier):
    def __init__(self, radius=None): # for backwards compatibility.
        pass
    def __call__(self, image):
        return skimage.filters.sobel(image.npImage())

registeredclass.Registration(
    'Edge',
    ImageModifier,
    EdgeImage,
    ordering = 2.031,
    tip = "Find edges in an image using Sobel edge filter.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/edge.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class EnhanceImage(ImageModifier):
    def __call__(self, image):
        enhanced_image = skimage.restoration.denoise_nl_means(
            image.npImage(),
            patch_size=7, patch_distance=11, fast_mode=True,
            h=0.1, sigma=0.0, channel_axis=-1)
        return enhanced_image

registeredclass.Registration(
    'Enhance',
    ImageModifier,
    EnhanceImage,
    ordering = 2.04,
    secret = True,              # TODO NUMPY: Why is this secret?
    tip = 'Enhance the image by minimizing noise.',
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/enhance.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class EqualizeImage(ImageModifier):
    def __call__(self, image):
        return skimage.exposure.equalize_adapthist( image.npImage() )

registeredclass.Registration(
    'Equalize',
    ImageModifier,
    EqualizeImage,
    ordering = 2.05,
    tip = 'Apply adaptive histogram equalization to the image.',
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/equalize.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class MedianFilterImage(ImageModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, image):
        disk = skimage.morphology.disk(self.radius)
        npimage = image.npImage()
        newimage = numpy.empty_like(npimage)
        for k in range(npimage.shape[2]):
            newimage[:,:,k] = skimage.filters.median(npimage[:,:,k], disk)
        return newimage

registeredclass.Registration(
    'MedianFilter',
    ImageModifier,
    MedianFilterImage,
    ordering = 2.06,
    params = [ parameter.FloatParameter('radius', 2.0, tip="Radius of the median filter.") ],
    tip = "Reduce noise by replacing each pixel color with its median over a local region.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/median.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NegateImage(ImageModifier):
    def __call__(self, image):
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

class NormalizeImage(ImageModifier):
    def __call__(self, image):
        return skimage.exposure.rescale_intensity(
            image.npImage(),
            in_range='image',
            out_range='image')

registeredclass.Registration(
    'Normalize',
    ImageModifier,
    NormalizeImage,
    ordering = 2.07,
    tip = "Normalize the image by rescaling pixel intensity values.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/normalize.xml')
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class SharpenImage(ImageModifier):
    def __init__(self, radius, amount):
        self.radius = radius
        self.amount = amount
    def __call__(self, image):
        newImage = skimage.filters.unsharp_mask(
            image.npImage(), self.radius, self.amount)
        return newImage

registeredclass.Registration(
    'Sharpen',
    ImageModifier,
    SharpenImage,
    ordering = 2.09,
    params = [
        parameter.FloatParameter('radius', 1.0,
                                 tip='Radius of the Gaussian blur.'),
        parameter.FloatParameter('amount', 1.0,
                                 tip='Amplification factor for image details.')
    ],
    tip = "Sharpen the image by convolving with a Gaussian: The sharp details are identified as the difference between the original image and its blurred version. These details are then scaled, and added back to the original image.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/sharpen.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class ReIlluminateImage(ImageModifier):
    def __init__(self, radius):
        self.radius = radius
    def __call__(self, image):
        image.evenly_illuminate(self.radius)
        return image.npImage()

registeredclass.Registration(
    'Reilluminate',
    ImageModifier,
    ReIlluminateImage,
    ordering = 3.0,
    params = [
        parameter.IntParameter('radius', 10,
                               tip='Size of the averaging region.')
    ],
    tip = 'Adjust brightness so that the whole image is evenly illuminated.',
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/reilluminate.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

