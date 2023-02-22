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

if config.use_skimage():
    import numpy

imgmenu = mainmenu.OOF.LoadData.addItem(oofmenu.OOFMenuItem('Image'))

# class NumpyArrayParameter(parameter.Parameter):
#     types = (numpy.ndarray,)
#     def binaryRepr(self, datafile, value):
#         shape = value.shape
#         shapeFmt = ">" + "i"*len(shape)
#         dt = value.dtype.str # string representation of dtype
#         return (struct.pack(structIntFmt, len(shape)) + # no. of dims
#                 struct.pack(shapeFmt, *shape) +         # dims
#                 struct.pack(structIntFmt, len(dt)) +    # no. chars in type str
#                 bytes(dt, "UTF-8") +                    # type str
#                 value.tobytes())                        # array data
#     def binaryRead(self, parser):
#         b = parser.getBytes(parameter.structIntSize)
#         (ndims,) = struct.unpack(parameter.structIntFmt, b)
#         shapeFmt = ">" + "i"*ndims
#         b = parser.getBytes(struct.calcsize(shapeFmt))
#         shape = struct.unpack(shapeFmt, b)
#         b = parser.getBytes(parameter.structIntSize)
#         (ndtype,) = struct.unpack(parameter.structIntFmt, b)
#         dtypename = parser.getBytes(ndtype).decode()
#         dtype = numpy.dtype(dtypename)
#         n = dtype.itemsize      # no. bytes per array entry
#         for d in shape:
#             n *= d
#         b = parser.getBytes(n)
#         array = numpy.frombuffer(b, dtype)
#         array.reshape(shape)
#         return array
#     def valueDesc(self):
#         return "A numpy array (numpy.ndarray)."
#     ## TODO: How does this get written in an ascii data file?
                


# ImageData classes contain image data to be stored in OOF2 data
# files.

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
# only be used to load old data files.

class RGBData8(ImageData):
    def __init__(self, rgbvalues):
        self.rgbvalues = rgbvalues
    def values(self):
        return self.rgbvalues
    def getArray(self, nrows, ncols):
        data = numpy.array(self.rgbvalues, dtype=dtype('>f8'))
        data.reshape(nrows, ncols, 3)
        return data

registeredclass.Registration(
    'RGBData8',
    ImageData,
    RGBData8,
    ordering=0,
    params=[
    parameter.ListOfUnsignedShortsParameter('rgbvalues', tip="RGB values.")],
    tip="RGB image data.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/rgbdata8.xml')
)

# # GrayData8 is an old format, predating our use of numpy.  It should
# # only be used to load old data files.

# class GrayData8(ImageData):
#     depth = 1
#     def __init__(self, grayvalues):
#         self.grayvalues = grayvalues
#     def values(self):
#         return self.grayvalues
#     def getArray(self, shape):
#         data = numpy.array(self.grayvalues, dtype=dtype('>f8'))
        
# registeredclass.Registration(
#     'GrayData8',
#     ImageData,
#     GrayData8,
#     ordering=1,
#     params=[
#     parameter.ListOfUnsignedShortsParameter('grayvalues', tip="Gray values.")],
#     tip="Gray image data.",
#     discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/graydata8.xml'))

class NumpyRGB64(ImageData):
    def __init__(self, npdata):
        self.npdata = npdata
    def values(self):
        return self.npdata
    def getArray(self, nrows, ncols):
        array = numpy.frombuffer(self.npdata, dtype=numpy.dtype('>f8'))
        array.reshape(nrows, ncols, 3)
        return array
    def __repr__(self):
        return self.nbdata.tobytes()

registeredclass.Registration(
    'NumpyRGB64',
    ImageData,
    NumpyRGB64,
    ordering=2,
    params=[
        parameter.BytesParameter('npdata',
                                 tip='64 bit floats encoded as bytes')],
    tip="Numpy image data for an RGB image")

# class NumpyGray64(ImageData):
#     def __init__(self, npdata):
#         self.npdata = npdata
#     def values(self):
#         return self.npdata
#     def getArray(self, nrows, ncols):
#         array = numpy.frombuffer(self.npdata, dtype=numpy.dtype('>f8'))
#         array.reshape(nrows, ncols)
#         return array

# registeredclass.Registration(
#     'NumpyGray64',
#     ImageData,
#     ordering=3,
#     params=[
#         parameter.BytesParameter('npdata',
#                                  tip='64 bit floats encoded as bytes')],
#     tip = "Numpy image data for a gray scale image")
    
    
    
## TODO NUMPY: Rewrite _newImage and writeImage.
##
## They should transfer data directly to and from from the numpy
## object, using numpy.ndarray.tobytes and numpy.frombuffer.
## Do they have to care about endianness?

## Existing files use the ListOfUnsignedShortsParameter, which stores
## shorts, not doubles.  So keep the old versions, but create a new 
## ImageData classes that stores doubles.  Those commands can copy the data
## in binary.  Does that make sense for ascii & script data files?
## Yes-- image.data.tobytes() writes a bytes object that has an ascii
## repr.

def _newImage(menuitem, name, microstructure, pixels):
    ms = ooflib.common.microstructure.microStructures[microstructure].getObject()
    if config.use_skimage():
        #* Get bytes from the ImageData (pixels) arg.  The old
        #  non-numpy subclasses will have to convert the data.  Numpy
        #  subclasses just return it.
        pixelparam = menuitem.get_arg("pixels")
        image = oofimage.newImageFromNumpyData(name, pixelparam.getArray())
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
    datafile.argument('pixels', NumpyRGB64(npimage.tobytes()))
    datafile.endCmd()

# TODO LATER: Allow different image depths, and find a way to store
# only gray values if the image is gray.

###################

## Define a Microstructure IO PlugIn so that Images will be written to
## Microstructure data files.

def writeImageInMicrostructure(datafile, mscontext):
    for image in mscontext.getObject().getImageContexts():
        image.writeImage(datafile)

microstructureIO.registerMicrostructureIOPlugIn(writeImageInMicrostructure)

