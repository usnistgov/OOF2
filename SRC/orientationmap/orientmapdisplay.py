# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import coord
from ooflib.SWIG.engine import angle2color
from ooflib.SWIG.engine import orientationimage
from ooflib.SWIG.orientationmap import orientmapdata
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump
from ooflib.engine.IO import microstructuredisplay

class OrientationMapDisplay(display.DisplayMethod):
    def __init__(self, colorscheme):
        self.colorscheme = colorscheme
        display.DisplayMethod.__init__(self)
    def draw(self, gfxwindow):
        msobj = self.who.getObject(gfxwindow)
        data = orientmapdata.getOrientationMap(msobj)
        if data is not None:
            orientimage = orientmapdata.OrientMapImage(data, self.colorscheme)
            image = orientimage.makeCanvasImage(primitives.Point(0,0),
                                                msobj.size())
            self.canvaslayer.addItem(image)
    def getTimeStamp(self, gfxwindow):
        msobj = self.who.getObject(gfxwindow)
        return max(display.DisplayMethod.getTimeStamp(self, gfxwindow),
                   orientmapdata.getOrientationMapTimestamp(msobj))

registeredclass.Registration(
    'Orientation Map',
    display.DisplayMethod,
    OrientationMapDisplay,
    ordering=2,
    params=[parameter.RegisteredParameter('colorscheme',
                                          angle2color.Angle2Color,
                                tip='Method for converting angles to colors.')
            ],
    layerordering=display.Planar(0.5),
    whoclasses = ('Microstructure',),
    tip="Display a Microstructure's Orientation Map, whether or not it's used by Material Properties.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/orientationmap/reg/orientationmapdisplay.xml'))
