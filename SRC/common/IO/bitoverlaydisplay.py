# -*- python -*-

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
from ooflib.common.IO import bitmapdisplay
from ooflib.common.IO import display
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

# The BitmapOverlayDisplayMethod is used to display objects that have
# a getBitmap() method in their Who class.  getBitmap() can return
# None, in which case nothing is drawn.  The bitmap marks pixels to be
# drawn as an overlay on the topmost image in the display.  The pixels
# are drawn with a single color and transparency.


class BitmapOverlayDisplayMethod(display.DisplayMethod):
    def __init__(self, color):
        self.color = color
        display.DisplayMethod.__init__(self)
    def draw(self, gfxwindow):
        self.canvaslayer.removeAllItems()
        bitmap = self.who.resolve(gfxwindow).getBitmap()
        if bitmap is None or bitmap.empty():
            return
        bitmap.setColor(self.color)
        image = bitmap.makeCanvasImage(primitives.Point(0,0), bitmap.size())
        self.canvaslayer.addItem(image)

    def getTimeStamp(self, gfxwindow):
        return self.timestamp

bitmapOverlay = registeredclass.Registration(
    'BitmapOverlay',
    display.DisplayMethod,
    BitmapOverlayDisplayMethod,
    params=[color.TranslucentColorParameter('color', tip="Bitmap color.")],
    ordering=0,
    layerordering=display.SemiPlanar,
    whoclasses=('Pixel Selection', 'Active Area'),
    tip="Special bitmap display method for overlays.",
    discussion=xmlmenudump.loadFile(
        'DISCUSSIONS/common/reg/bitoverlaydisplay.xml'))

