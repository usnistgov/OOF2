from image import imagemodifier
from common import registeredclass
from common.IO import parameter
from SWIG.image.imagemanip import gabor

class GaborModifier(imagemodifier.ImageModifier):
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
    def __call__(self, image):
        gabor.makeGabor(image, self.a, self.b, self.n)


registeredclass.Registration('Gabor',
                             imagemodifier.ImageModifier,
                             GaborModifier,
                             ordering=20.,
                             params=[
    parameter.FloatParameter('a', 3.0, tip='Gabor filter width'),
    parameter.FloatParameter('b', 5.0, tip='Gabor filter depth'),
    parameter.IntParameter('n', 6, tip='Number of orientations')
    ],
                             tip='Gabor filter')
