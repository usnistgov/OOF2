from image import imagemodifier
from common import registeredclass
from common.IO import parameter
from SWIG.image.imagemanip import gray
from types import *

class grayModifier(imagemodifier.ImageModifier):
    def __init__(self):
        pass
    def __call__(self, image):
        gray.makeGray(image)

registeredclass.Registration('gray',
                             imagemodifier.ImageModifier,
                             grayModifier,
                             ordering=20.,
                             params=[],
                             tip='Converts the image to 256-color grayscale')
