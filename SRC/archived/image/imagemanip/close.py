from image import imagemodifier
from common import registeredclass
from common.IO import parameter
from SWIG.image.imagemanip import close

class CloseModifier(imagemodifier.ImageModifier):
    def __init__(self, a, b, n, t, d):
        self.a = a
        self.b = b
        self.n = n
        self.t = t
        self.d = d
    def __call__(self, image):
        close.makeClosed(image, self.a, self.b, self.n, self.t, self.d)


registeredclass.Registration('Close',
                             imagemodifier.ImageModifier,
                             CloseModifier,
                             ordering=20.,
                             params=[
    parameter.FloatParameter('a', 3.0, tip='Gabor filter width'),
    parameter.FloatParameter('b', 5.0, tip='Gabor filter depth'),
    parameter.IntParameter('n', 6, tip='Number of orientations'),
    parameter.IntParameter('t', 40, tip='Thresholding cutoff'),
    parameter.IntParameter('d', 9,
                           tip='Diameter of structuring element for closing')
    ],
                             tip='Gabor filter with line closing')
