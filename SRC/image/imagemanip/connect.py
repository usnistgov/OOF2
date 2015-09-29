from image import imagemodifier
from common import registeredclass
from common.IO import parameter
from SWIG.image.imagemanip import connect

class ConnectModifier(imagemodifier.ImageModifier):
    def __init__(self, a, b, n, t, d, numEdgeIter, boxSize, trim):
        self.a = a
        self.b = b
        self.n = n
        self.t = t
        self.d = d
        self.numEdgeIter = numEdgeIter
        self.boxSize = boxSize
        self.trim = trim
    def __call__(self, image):
        connect.makeConnected(image, self.a, self.b, self.n, self.t, self.d, self.numEdgeIter, self.boxSize, self.trim)


registeredclass.Registration('Connect',
                             imagemodifier.ImageModifier,
                             ConnectModifier,
                             ordering=20.,
                             params=[
    parameter.FloatParameter('a', 5.0, tip='Gabor filter width'),
    parameter.FloatParameter('b', 7.0, tip='Gabor filter depth'),
    parameter.IntParameter('n', 6, tip='Number of orientations'),
    parameter.IntParameter('t', 27, tip='Thresholding cutoff'),
    parameter.UbtParameter('d', 9,
                           tip='Diameter of structuring element for closing'),
    parameter.IntParameter('numEdgeIter', 9,
                           tip='Number of iterations for edge-linking'),
    parameter.IntParameter('boxSize', 10, tip='Line connection box'),
    parameter.BooleanParameter('trim', 1, tip='Trim')
    ],
                             tip='Connects the lines')
