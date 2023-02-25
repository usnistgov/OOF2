# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
from ooflib.SWIG.image import oofimage
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import mainmenu
from ooflib.common.IO import microstructureIO
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.image.IO import imagemenu
import ooflib.common.microstructure

import sys
if config.use_skimage():
    import numpy
    import skimage

imgmenu = mainmenu.OOF.LoadData.addItem(oofmenu.OOFMenuItem('Image'))

# ImageData classes contain image data to be stored in OOF2 data
# files.

# TODO: If the internal representation of images is changed from
# 64-bit float to something else, then the toArray() methods in the
# ImageData subclasses will have to change.  Those classes should all
# call a single function that converts the numpy array to the correct
# format.  Should the user be able to choose the image representation?


class ImageData(registeredclass.RegisteredClass):
    registry = []
    tip = "Image data types."
    discussion = """<para>
    <classname>ImageData</classname> objects are used to store &image;
    pixels in &oof2; data files, as the <varname>pixels</varname>
    parameter in the <xref linkend='MenuItem-OOF.LoadData.Image.New'/>
    command.
    </para>"""

    
# RGBData8 is an old format, predating our use of numpy.  It should
# only be used to load old data files.  Also, it should have been
# called RGBData16.

class RGBData8(ImageData):
    def __init__(self, rgbvalues):
        self.rgbvalues = rgbvalues
    # RGBData8 has no toBytes method because it is only used to read
    # old data files, and cannot write new ones.
    def toArray(self, sizeInPixels):
        data = numpy.array(self.rgbvalues, dtype=numpy.dtype('H'))
        data = skimage.util.img_as_float64(data)
        data = data.reshape(sizeInPixels[1], sizeInPixels[0], 3)
        return data

registeredclass.Registration(
    'RGBData8',
    ImageData,
    RGBData8,
    ordering=100,
    params=[
    parameter.ListOfUnsignedShortsParameter('rgbvalues', tip="RGB values.")],
    tip="RGB image data.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/rgbdata8.xml')
)

#-----------

class NumpyRGB64(ImageData):
    def __init__(self, rgbdata):
        if type(rgbdata) == str:
            rgbdata = bytes.fromhex(rgbdata)
        self.rgbdata = rgbdata
    def toBytes(self, image):
        # Convert image to 64-bit float. This is a no-op if nothing
        # has to be done.
        img64 = skimage.img_as_float64(image)
        # Ensure that the output is little-endian
        if img64.dtype != numpy.dtype("<d"):
            img64 = img64.byteswap(inplace=(img64 is not image))
        self.rgbdata = img64.tobytes()
    def toArray(self, sizeInPixels):
        array = numpy.frombuffer(self.npdata, dtype=numpy.dtype('<d'))
        array = array.reshape(sizeInPixels[1], sizeInPixels[0], 3)
        return array
    def __repr__(self):
        return f"NumpyRGB64(rgbdata='{self.rgbdata.hex()}')"

registeredclass.Registration(
    'NumpyRGB64',
    ImageData,
    NumpyRGB64,
    ordering=2,
    params=[
        parameter.BytesParameter('npdata',
                                 tip='64 bit floats encoded as bytes')],
    tip="Numpy RGB image data stored as 8 byte floats.")

#-----------

class NumpyRGB16(ImageData):
    def __init__(self, rgbdata):
        if type(rgbdata) == str:
            rgbdata = bytes.fromhex(rgbdata)
        self.rgbdata = rgbdata
    def toBytes(self, image):
        # Convert data to 16 bit unsigned int. This is a no-op if
        # nothing has to be done.
        img16 = skimage.img_as_uint(image)
        # Ensure that the output is little-endian
        if img16.dtype != numpy.dtype("<H"):
            # Don't swap bytes in-place if img16 is image!
            img16 = img16.byteswap(inplace=(img16 is not image))
        self.rgbdata = img16.tobytes()
    def toArray(self, sizeInPixels):
        array = numpy.frombuffer(self.rgbdata, dtype=numpy.dtype("<H"))
        array = array.reshape(sizeInPixels[1], sizeInPixels[0], 3)
        return skimage.util.img_as_float64(array)
    def __repr__(self):
        return f"NumpyRGB16(rgbdata='{self.rgbdata.hex()}')"

registeredclass.Registration(
    'NumpyRGB16',
    ImageData,
    NumpyRGB16,
    ordering=1,
    params=[
        parameter.BytesParameter("rgbdata",
                                 tip='Image data stored as 16 bit ints')],
    tip="Numpy RGB image data stored as two byte ints.")


def _newImage(menuitem, name, microstructure, pixels):
    ms = ooflib.common.microstructure.microStructures[microstructure].getObject()
    if config.use_skimage():
        # Get bytes from the ImageData (pixels) arg. 
        image = oofimage.newImageFromNumpyData(
            name, pixels.toArray(ms.sizeInPixels()))
    else:
        image = oofimage.newImageFromData(name, ms.sizeInPixels(),
                                          list(pixels.values()))
    image.setSize(ms.size())
    imagemenu.loadImageIntoMS(image, microstructure)
    
imgmenu.addItem(oofmenu.OOFMenuItem(
    'New',
    callback=_newImage,
    params=[
    parameter.StringParameter('name', tip="Name for the Image."),
    whoville.WhoParameter('microstructure',whoville.getClass('Microstructure'),
                          tip=parameter.emptyTipString),
    parameter.RegisteredParameter('pixels', ImageData,
                                  tip=parameter.emptyTipString)],
    help="Load an Image.",
    discussion="<para>Load an &image; from a saved &micro;.</para>"
    ))

def writeImage(datafile, imagecontext):
    datafile.startCmd(mainmenu.OOF.LoadData.Image.New)
    datafile.argument('name', imagecontext.name())
    datafile.argument('microstructure', imagecontext.getMicrostructure().name())
    npimage = imagecontext.npImage()
    # Convert image to 16-bit ints.  This is a no-op if nothing has to
    # be done.
    img = skimage.util.img_as_uint(npimage)
    # Make sure image is little-endian
    if img.dtype != numpy.dtype("<H"):
        # Swap bytes to ensure little-endianness.  Do it in place only
        # if the previous conversion created a new object.
        img = img.byteswap(inplace=(img is not npimage))
    datafile.argument('pixels', NumpyRGB16(img.tobytes()))
    datafile.endCmd()

# TODO?  Allow the user to select the format for saved images?  This
# will probably have to be set as a global parameter, since images are
# saved as part of Microstructures, Skeletons, and Meshes.

###################

## Define a Microstructure IO PlugIn so that Images will be written to
## Microstructure data files.

def writeImageInMicrostructure(datafile, mscontext):
    for image in mscontext.getObject().getImageContexts():
        image.writeImage(datafile)

microstructureIO.registerMicrostructureIOPlugIn(writeImageInMicrostructure)

