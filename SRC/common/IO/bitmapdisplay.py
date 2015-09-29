# -*- python -*-
# $RCSfile: bitmapdisplay.py,v $
# $Revision: 1.17 $
# $Author: langer $
# $Date: 2014/09/27 21:40:30 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.common import debug
from ooflib.common.IO import display
from ooflib.common.IO import xmlmenudump
from ooflib.SWIG.common import coord
from ooflib.SWIG.common import config
from ooflib.common import registeredclass
##import weakref

class BitmapDisplayMethod(display.DisplayMethod):
    def __init__(self):
        self.bitmapobject = None
        display.DisplayMethod.__init__(self)
    def draw(self, gfxwindow, device):
        bitmapobj = self.who().getObject(gfxwindow)
        if config.dimension() == 2:
            device.draw_image(bitmapobj, coord.Coord(0,0), bitmapobj.size())
        if config.dimension() == 3:
            device.draw_image(bitmapobj, coord.Coord(0,0,0), bitmapobj.size())

bitmapDisplay = registeredclass.Registration(
    'Bitmap',
    display.DisplayMethod,
    BitmapDisplayMethod,
    ordering=-100,
    layerordering=display.Planar,
    params=[],
    whoclasses = ('Image',),
    tip="Display an Image as a bitmap.",
    discussion = xmlmenudump.loadFile('DISCUSSIONS/common/reg/bitmapdisplay.xml')
    )

