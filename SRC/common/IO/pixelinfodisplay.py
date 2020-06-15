# -*- python -*-


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import config
from ooflib.SWIG.common.IO.OOFCANVAS import oofcanvas
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

    def draw(self, gfxwindow, canvaslayer):
        canvaslayer.removeAllItems()
        toolbox = gfxwindow.getToolboxByName("Pixel_Info")
        microstructure = toolbox.findMicrostructure()
        if microstructure is not None:
            pixel = toolbox.currentPixel()
            if pixel is not None:
                self.drawPixel(canvaslayer, pixel, microstructure)
                for plugIn in toolbox.plugIns:
                    plugIn.draw(self, canvaslayer, pixel, microstructure)

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

    def getNodes(self, pixel, microstructure):
        # This returns all four nodes even though PixelInfoDisplay
        # only needs two of them, because some plug-ins might want all
        # four.
        dx = microstructure.sizeOfPixels()[0]
        dy = microstructure.sizeOfPixels()[1]
        i = pixel.x
        j = pixel.y
        n0 = primitives.Point(i*dx, j*dy)
        n1 = primitives.Point((i+1)*dx, j*dy)
        n2 = primitives.Point((i+1)*dx, (j+1)*dy)
        n3 = primitives.Point(i*dx, (j+1)*dy)
        return n0, n1, n2, n3
            
    def drawPixel(self, canvaslayer, pixel, microstructure):
        n0, n1, n2, n3 = self.getNodes(pixel, microstructure)
        rect = oofcanvas.CanvasRectangle(n0.x, n0.y, n2.x, n2.y)
        rect.setLineColor(color.canvasColor(self.color))
        rect.setLineWidthInPixels()
        rect.setLineWidth(self.line_width)
        canvaslayer.addItem(rect)
        
    def getTimeStamp(self, gfxwindow):
        toolbox = gfxwindow.getToolboxByName("Pixel_Info")
        return max(self.timestamp,
                   toolbox.getTimeStamp())

defaultPixelInfoColor = color.blue
defaultLineWidth = 2
widthRange = (0, 10, 0.2)

def _setDefaultPixelParams(menuitem, color, line_width): #, opacity):
    global defaultPixelInfoColor
    defaultPixelInfoColor = color
    global defaultLineWidth
    defaultLineWidth = line_width

pixelinfoparams = [
    color.ColorParameter(
        'color', defaultPixelInfoColor,
        tip="Color for the queried pixel."),
    parameter.FloatRangeParameter(
        'line_width', widthRange,
        defaultLineWidth,
        tip="Line width in screen pixels.")]

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
    return pixelInfoDisplay(color=defaultPixelInfoColor,
                            line_width=defaultLineWidth)

ghostgfxwindow.PredefinedLayer('Top Bitmap', '<top bitmap>',
                               predefinedPixelInfoLayer)
