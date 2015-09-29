# -*- python -*-
# $RCSfile: pixelinfodisplay.py,v $
# $Revision: 1.24 $
# $Author: langer $
# $Date: 2014/09/27 21:40:32 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import config
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import ghostgfxwindow
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump


class PixelInfoDisplay(display.DisplayMethod):
    def __init__(self, color, line_width=1, opacity=.3):
        self.color = color
        self.line_width = line_width
        self.opacity = opacity
        display.DisplayMethod.__init__(self)

    def draw(self, gfxwindow, device):
        toolbox = gfxwindow.getToolboxByName("Pixel_Info")
        pixel = toolbox.currentPixel()
        if pixel is not None:
            microstructure = toolbox.findMicrostructure()
            if microstructure is not None:
                self.drawPixel(device, pixel, microstructure)

#      n3_______________n2 ((i+1)*dx, (j+1)*dy)
#       |               |
#       |               |
#       |               |
#       |               dy
#       |     (i, j)    |
#       |               |
#       |               |
#       |               |
#       n0------dx------n1
# (i*dx, j*dy)
    def drawPixel(self, device, pixel, microstructure):
        if config.dimension() == 2:
            dx = microstructure.sizeOfPixels()[0]
            dy = microstructure.sizeOfPixels()[1]
            i = pixel.x
            j = pixel.y
            n0 = primitives.Point(i*dx, j*dy)
            n1 = primitives.Point((i+1)*dx, j*dy)
            n2 = primitives.Point((i+1)*dx, (j+1)*dy)
            n3 = primitives.Point(i*dx, (j+1)*dy)
            device.set_lineColor(self.color)
            device.set_lineWidth(self.line_width)
            device.draw_segment(primitives.Segment(n0, n1))
            device.draw_segment(primitives.Segment(n1, n2))
            device.draw_segment(primitives.Segment(n2, n3))
            device.draw_segment(primitives.Segment(n3, n0))
        elif config.dimension() == 3:
            device.set_lineColor(self.color)
            device.set_lineWidth(self.line_width)
            device.draw_voxel(pixel)

    def getTimeStamp(self, gfxwindow):
        toolbox = gfxwindow.getToolboxByName("Pixel_Info")
        return max(self.timestamp,
                   toolbox.getTimeStamp())

defaultPixelInfoColor = color.blue
if config.dimension() == 2:
    defaultLineWidth = 0
    widthRange = (0,10)
# In vtk, line widths of 0 cause errors
elif config.dimension() == 3:
    defaultLineWidth = 1
    widthRange = (1,10)

def _setDefaultPixelParams(menuitem, color, line_width): #, opacity):
    global defaultPixelInfoColor
    defaultPixelInfoColor = color
    global defaultLineWidth
    defaultLineWidth = line_width
##     global defaultOpacity
##     defaultOpacity = opacity


## if config.dimension() == 2:
pixelinfoparams = [color.ColorParameter('color', defaultPixelInfoColor,
                                        tip="Color for the queried pixel."),
                   parameter.IntRangeParameter('line_width', widthRange,
                                               defaultLineWidth,
                                               tip="Line width.")]
## elif config.dimension() == 3:
##     pixelinfoparams = [color.ColorParameter('color', defaultPixelInfoColor,
##                                             tip="Color for the queried pixel."),
##                        parameter.FloatRangeParameter('opacity', (0., 1., 0.01),
##                                                    defaultOpacity,
##                                                    tip="Tint Opacity.")]

mainmenu.gfxdefaultsmenu.Pixels.addItem(oofmenu.OOFMenuItem(
    "Pixel_Info",
    callback=_setDefaultPixelParams,
    ordering=2,
    params=pixelinfoparams,
    help="Set default parameters for the Pixel Info display.",
    discussion="""<para>

    Set default parameters for <link linkend="RegisteredClass-PixelInfoDisplay"><classname>PixelInfoDisplays</classname></link>.
    See <xref linkend="RegisteredClass-PixelInfoDisplay"/> for the details.
    This command may be placed in the &oof2rc; file to set a default value
    for all &oof2; sessions.

    </para>"""))

pixelInfoDisplay = registeredclass.Registration(
    'Pixel Info',
    display.DisplayMethod,
    PixelInfoDisplay,
    params=pixelinfoparams,
    ordering=2.70,
    layerordering=display.PointLike(0.5),
    whoclasses=('Image','Microstructure', 'Top Bitmap'),
    tip="Display a pixel that is being queried.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/pixelinfodisplay.xml')
    )

########################

# In order to have a single layer that displays pixel info for *both*
# Images and Microstructures, we create a new WhoClass that contains
# only a single WhoProxy object.  The proxy resolves to the topmost
# Image or Microstructure.  We can then create a predefined layer for
# the WhoClass.

from ooflib.common.IO import whoville

class TopBitmap(whoville.WhoProxyClass):
    def resolve(self, proxy, gfxwindow):
        return gfxwindow.topwho('Microstructure', 'Image')
    def getTimeStamp(self, proxy, gfxwindow):
        return gfxwindow.getLayerChangeTimeStamp()

TopBitmap('<top bitmap>')

whoville.WhoClass('Top Bitmap', ordering=20000, proxyClasses=['<top bitmap>'])

def predefinedPixelInfoLayer():
##     if config.dimension() == 2:
    return pixelInfoDisplay(color=defaultPixelInfoColor,
                            line_width=defaultLineWidth)
##     if config.dimension() == 3:
##         return pixelInfoDisplay(color=defaultPixelInfoColor,
##                                 opacity=defaultOpacity)

ghostgfxwindow.PredefinedLayer('Top Bitmap', '<top bitmap>',
                               predefinedPixelInfoLayer)
