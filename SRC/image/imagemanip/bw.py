from image import imagemodifier
from common import registeredclass
from common.IO import parameter
from SWIG.image.imagemanip import bw

class BWModifier(imagemodifier.ImageModifier):
    def __init__(self, a, b, n, t):
        self.a = a
        self.b = b
        self.n = n
        self.t = t
    def __call__(self, image):
        bw.makeBW(image, self.a, self.b, self.n, self.t)


registeredclass.Registration('BlackAndWhite',
                             imagemodifier.ImageModifier,
                             BWModifier,
                             ordering=20.,
                             params=[
    parameter.FloatParameter('a', 3.0, tip='Gabor filter width'),
    parameter.FloatParameter('b', 5.0, tip='Gabor filter depth'),
    parameter.IntParameter('n', 6, tip='Number of orientations'),
    parameter.IntParameter('t', 40, tip='Threshold level for the image'),
                             ],
                             tip='Converts the image to black and white (binary)')
