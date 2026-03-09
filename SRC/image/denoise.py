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
from ooflib.common import oofenum
from ooflib.common import registeredclass
from ooflib.common.IO import automatic
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.image import imagemodifier

from packaging import version
import numpy
import skimage

# The various scikit-image denoising methods are wrapped registered
# classes which are used as arguments to a single DenoiseImage
# ImageModifier.

class DenoiseMethod(registeredclass.RegisteredClass):
    registry = []
    tip="A technique for removing noise from an image."
    discussion=\
"""Subclasses of <classname>DenoiseMethod</classname> are used by
<xref linkend="MenuItem-OOF.Image.Modify.Denoise"/> to remove noise from an &image;."""

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## TODO NUMPY LATER: DenoiseBilateral shifts the image down and to the
## right, which seems to be a bug in the skimage routine.  Until it's
## fixed, the Registration is marked "secret".

class DenoiseBilateral(DenoiseMethod):
    def __init__(self, window_size, sigma_color, sigma_spatial, bins):
        self.window_size = window_size
        self.sigma_color = sigma_color
        self.sigma_spatial = sigma_spatial
        self.bins = bins
    def denoise(self, image):
        win_size = (None if self.window_size==automatic.automatic
                    else self.window_size)
        sigma_color = (None if self.sigma_color==automatic.automatic
                       else self.sigma_color)
        if imagemodifier.skimage_version_ge('0.19'):
            return skimage.restoration.denoise_bilateral(
                image.npImage(),
                win_size=win_size ,
                sigma_color=sigma_color,
                sigma_spatial=self.sigma_spatial,
                bins = self.bins,
                mode='edge',
                channel_axis=(None if image.isGray() else 2))
        else:
            return skimage.restoration.denoise_bilateral(
                image.npImage(),
                win_size=win_size ,
                sigma_color=sigma_color,
                sigma_spatial=self.sigma_spatial,
                bins = self.bins,
                mode='edge',
                multichannel=not image.isGray())


registeredclass.Registration(
    'Bilateral',
    DenoiseMethod,
    DenoiseBilateral,
    ordering = 1,
    secret = True,   
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

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class TotalVariation(DenoiseMethod):
    def __init__(self, weight, eps, max_iterations):
        self.weight = weight
        self.eps = eps
        self.max_iterations = max_iterations
    def denoise(self, image):
        if imagemodifier.skimage_version_ge('0.19'):
            return skimage.restoration.denoise_tv_chambolle(
                image.npImage(),
                weight=self.weight,
                eps=self.eps,
                max_num_iter=self.max_iterations,
                channel_axis=(None if image.isGray() else 2))
        else:
            return skimage.restoration.denoise_tv_chambolle(
                image.npImage(),
                weight=self.weight,
                eps=self.eps,
                n_iter_max=self.max_iterations,
                multichannel=not image.isGray())

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
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/denoise_tv.xml'),
    xrefs=["MenuItem-OOF.Image.Modify.Denoise"]
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## TODO NUMPY LATER: Wavelet denoising appears not to work. It returns
## RGB values that are outside the range [0,1].  Is it assuming that
## the data is [-1,1] instead of [0,1]?

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
            sigma = None if self.sigma == automatic.automatic else self.sigma
            wavelet_levels = (None if self.wavelet_levels == automatic.automatic
                              else self.wavelet_levels)
            if imagemodifier.skimage_version_ge('0.19'):
                result= skimage.restoration.denoise_wavelet(
                    image.npImage(),
                    sigma=sigma ,
                    wavelet=self.wavelet,
                    mode=self.mode.string(),
                    wavelet_levels=wavelet_levels,
                    convert2ycbcr=True,
                    method=self.method.string(),
                    channel_axis=(None if image.isGray() else 2))
                debug.fmsg(f"Back from denoise_wavelet, range=({result.min()}, {result.max()})")
            else:
                result= skimage.restoration.denoise_wavelet(
                    image.npImage(),
                    sigma=sigma ,
                    wavelet=self.wavelet,
                    mode=self.mode.string(),
                    wavelet_levels=wavelet_levels,
                    convert2ycbcr=True,
                    method=self.method.string(),
                    multichannel=not image.isGray())
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
            # There are many possible values for 'wavelet', so it's
            # not feasible to use an EnumParameter for them.  The
            # values can be printed with:
            #    import pywt; print(pywt.wavelist())
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

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class NonlocalMeans(DenoiseMethod):
    def __init__(self, patch_size, patch_distance, h, sigma):
        self.patch_size = patch_size
        self.patch_distance = patch_distance
        self.h = h
        self.sigma = sigma
    def denoise(self, image):
        sigma= 0 if self.sigma == automatic.automatic else self.sigma
        if imagemodifier.skimage_version_ge('0.19'):
            return skimage.restoration.denoise_nl_means(
                image.npImage(),
                patch_size=self.patch_size,
                patch_distance=self.patch_distance,
                fast_mode=True,
                h=self.h,
                sigma=sigma,
                channel_axis=(None if image.isGray() else 2))
        else:
            return skimage.restoration.denoise_nl_means(
                image.npImage(),
                patch_size = self.patch_size,
                patch_distance = self.patch_distance,
                fast_mode=True,
                h=self.h,
                sigma=sigma,
                multichannel=not image.isGray())

registeredclass.Registration(
    'NonlocalMeans',
    DenoiseMethod,
    NonlocalMeans,
    ordering = 2.083,
    params = [
        parameter.PositiveIntParameter(
            'patch_size', 7,
            tip='Size of patches used for denoising, in pixel units.'),
        parameter.PositiveIntParameter(
            'patch_distance', 11,
            tip='Maximum distance over which to search for similar patches, in pixel units.'),
        parameter.FloatParameter(
            'h', 0.1,
            tip="Cut-off, in gray levels. A higher h results in a smoother image."),
        parameter.PositiveAutoFloatParameter(
            'sigma', automatic.automatic,
            tip='The standard deviation of the noise.')
    ],
    tip = "Denoise using nonlocal means filtering (suitable for images with regions of repetitive texture).",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/image/reg/denoise_nlmeans.xml'),
    xrefs=["MenuItem-OOF.Image.Modify.Denoise"]
    )

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class DenoiseImage(imagemodifier.ImageModifierToEither):
    def __init__(self, method):
        self.method = method
    def modify(self, image):
        return self.method.denoise(image)

registeredclass.Registration(
    'Denoise',
    imagemodifier.ImageModifier,
    DenoiseImage,
    ordering = 2.08,
    params=[
        parameter.RegisteredParameter("method", DenoiseMethod,
                                      tip="How to denoise the image.")
        ],
    tip="Apply various methods to remove noise from an image.",
    discussion=xmlmenudump.loadFile("DISCUSSIONS/image/reg/denoise.xml"),
    xrefs=["MenuItem-OOF.Image.Modify.MedianFilter"])


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# ReduceNoise is kept for backward compatibility with an ImageMagick
# routine.  The registration is marked "secret" because it doesn't
# work.  Perhaps the description in the ImageMagick docs is wrong.
# The documentation says "Smooth the contours of an image while still
# preserving edge information. The algorithm works by replacing each
# pixel with its neighbor closest in value. The neighbors of a pixel
# are defined as those pixels within the given radius, specified in
# units of the pixel size. A suitable radius will be chosen
# automatically if radius is zero."
# TODO NUMPY MAYBE: Fix this.  See comment in reducenoise.C.

class ReduceNoise(imagemodifier.ImageModifierToRGB):
    def __init__(self, radius=1.0):
        self.radius = radius
    def modify(self, image):
        newimage = numpy.empty_like(image.npImage())
        image.reduce_noise(skimage.morphology.disk(self.radius), newimage)
        return newimage

registeredclass.Registration(
    'ReduceNoise',
    imagemodifier.ImageModifier,
    ReduceNoise,
    secret=True,                # See above
    ordering = 2.08,
    params = [parameter.PositiveFloatParameter(
        'radius', 5.0,
        tip='Radius of the pixel neighborhood in pixel units.')],
    tip = "Reduce noise while preserving edges.",
    #discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/reducenoise.xml')
    )

