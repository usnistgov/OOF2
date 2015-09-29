# -*- python -*-
# $RCSfile: bitoverlaydisplay.py,v $
# $Revision: 1.29 $
# $Author: langer $
# $Date: 2011/02/03 20:18:51 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.common import config
from ooflib.SWIG.common import coord
from ooflib.common import color
from ooflib.common import debug
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

#####

class BitmapOverlayDisplayMethod(display.DisplayMethod):
    def __init__(self, color, tintOpacity, voxelOpacity=1.0):
        self.color = color
        self.tintOpacity = tintOpacity
        self.voxelOpacity = voxelOpacity
        display.DisplayMethod.__init__(self)
    def draw(self, gfxwindow, device):
        bitmap = self.who().resolve(gfxwindow).getBitmap()
        if bitmap is None or bitmap.empty():
            return
        bitmap.setColor(self.color)
        bitmap.setTintAlpha(self.tintOpacity)
        if device.has_alpha():
            if config.dimension() == 2:
                device.draw_alpha_image(bitmap, coord.Coord(0,0), bitmap.size())
            elif config.dimension() == 3:
                bitmap.setVoxelAlpha(self.voxelOpacity)
                device.draw_alpha_image(bitmap, coord.Coord(0,0,0), bitmap.size())
                

    def getTimeStamp(self, gfxwindow):
        return self.timestamp

if config.dimension()==2:
    bitoverlayparams=[color.ColorParameter('color', tip="Bitmap color."),
            parameter.FloatRangeParameter('tintOpacity', (0., 1., 0.01), 0.6,
                                          tip="Opacity of the overlay.")]
elif config.dimension()==3:
    bitoverlayparams=[color.ColorParameter('color', tip="Bitmap color."),
            parameter.FloatRangeParameter('tintOpacity', (0., 1., 0.01), 0.0,
                                          tip="Opacity of the tint."),
            parameter.FloatRangeParameter('voxelOpacity',
                                          (0., 1., 0.01), 0.2,
                                          tip="Opacity of the given region.")]
    

bitmapOverlay = registeredclass.Registration(
    'BitmapOverlay',
    display.DisplayMethod,
    BitmapOverlayDisplayMethod,
    params=bitoverlayparams,
    ordering=0,
    layerordering=display.SemiPlanar,
    whoclasses=('Pixel Selection', 'Active Area'),
    tip="Special bitmap display method for overlays.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/common/reg/bitoverlaydisplay.xml'))

