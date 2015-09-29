# -*- python -*-
# $RCSfile: imageIO.py,v $
# $Revision: 1.16 $
# $Author: langer $
# $Date: 2010/12/13 21:52:12 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import config
if config.dimension() == 2:
    from ooflib.SWIG.image import oofimage
elif config.dimension() == 3:
    from ooflib.SWIG.image import oofimage3d as oofimage
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


imgmenu = mainmenu.OOF.LoadData.addItem(oofmenu.OOFMenuItem('Image'))


class ImageData(registeredclass.RegisteredClass):
    registry = []
    tip = "Image data types."
    discussion = """<para>
    <classname>ImageData</classname> objects are used to store &image;
    pixels in &oof2; data files, as the <varname>pixels</varname>
    parameter in the <xref linkend='MenuItem-OOF.LoadData.Image.New'/>
    command.
    </para>"""

class RGBData8(ImageData):
    def __init__(self, rgbvalues):
        self.rgbvalues = rgbvalues
    def values(self):
        return self.rgbvalues

registeredclass.Registration(
    'RGBData8',
    ImageData,
    RGBData8,
    ordering=0,
    params=[
    parameter.ListOfUnsignedShortsParameter('rgbvalues', tip="RGB values.")],
    tip="RGB image data.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/rgbdata8.xml'))



class GrayData8(ImageData):
    def __init__(self, grayvalues):
        self.grayvalues = grayvalues
    def values(self):
        return self.grayvalues

registeredclass.Registration(
    'GrayData8',
    ImageData,
    GrayData8,
    ordering=1,
    params=[
    parameter.ListOfUnsignedShortsParameter('grayvalues', tip="Gray values.")],
    tip="Gray image data.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/image/reg/graydata8.xml'))


def _newImage(menuitem, name, microstructure, pixels):
    ms = ooflib.common.microstructure.microStructures[microstructure].getObject()
    image = oofimage.newImageFromData(name, ms.sizeInPixels(), pixels.values())
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
    datafile.argument('pixels', RGBData8(imagecontext.getObject().getPixels()))
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

