# -*- python -*-
# $RCSfile: microstructuredisplay.py,v $
# $Revision: 1.28 $
# $Author: langer $
# $Date: 2014/09/27 21:40:58 $


# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# DisplayMethod for showing the Materials assigned to a Microstructure.

from ooflib.SWIG.common import coord
from ooflib.SWIG.common import config
from ooflib.SWIG.engine import material
if config.dimension() == 2:
    from ooflib.SWIG.engine import angle2color
    from ooflib.SWIG.engine import orientationimage
from ooflib.common import color
from ooflib.common import debug
from ooflib.common import primitives
from ooflib.common import registeredclass
from ooflib.common.IO import display
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

class MSMaterialDisplay(display.DisplayMethod):
    def getTimeStamp(self, gfxwindow):
        microstructure = self.who().getObject(gfxwindow)
        return max(display.DisplayMethod.getTimeStamp(self, gfxwindow),
                   material.getMaterialTimeStamp(microstructure))


class MicrostructureMaterialDisplay(MSMaterialDisplay):
    def __init__(self, no_material, no_color):
        self.no_material = no_material    # color if Material isn't assigned
        self.no_color = no_color    # color if Material has no ColorProperty
        MSMaterialDisplay.__init__(self)
    def draw(self, gfxwindow, device):
        microstructure = self.who().getObject(gfxwindow)
        # The draw_image() routine requires an object with a
        # .fillstringimage() function.  We can't simply give
        # Microstructure such a function, since it can be displayed in
        # many ways, so we construct a temporary object,
        # MaterialImage, just to pass to draw_image().
        matlimage = material.MaterialImage(microstructure, self.no_material,
                                           self.no_color)
        if config.dimension() == 2:
            device.draw_image(matlimage, coord.Coord(0,0), microstructure.size())
        if config.dimension() == 3:
            device.draw_image(matlimage, coord.Coord(0,0,0), microstructure.size())

registeredclass.Registration(
    'Material',
    display.DisplayMethod,
    MicrostructureMaterialDisplay,
    ordering=0,
    layerordering=display.Planar(0.4),
    params=[
    color.ColorParameter('no_material', color.black,
                         tip="Color to use if no material has been assigned to a pixel"),
    color.ColorParameter('no_color', color.blue,
                         tip="Color to use if the assigned material has no assigned color")
    ],
    whoclasses = ('Microstructure',),
    tip="Display the color of the Material assigned to each pixel.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/microstructuredisplay.xml')
    )

############################

if config.dimension() == 2:

    class OrientationDisplay(MSMaterialDisplay):
        def __init__(self, colorscheme, no_material=color.blue,
                     no_orientation=color.black):
            self.colorscheme = colorscheme
            self.no_orientation = no_orientation
            self.no_material = no_material
            MSMaterialDisplay.__init__(self)
        def draw(self, gfxwindow, device):
            msobj = self.who().getObject(gfxwindow)
            img = orientationimage.OrientationImage(msobj,
                                                    self.colorscheme,
                                                    self.no_material,
                                                    self.no_orientation)
            # Don't use OrientationImage.size() here, because
            # orientmapimage may be destroyed before drawing is
            # complete.  msobj.size() refers to an object that will be
            # persistent.
            device.draw_image(img, coord.Coord(0,0), msobj.size())

    registeredclass.Registration(
        'Orientation',
        display.DisplayMethod,
        OrientationDisplay,
        ordering=1,
        params=[parameter.RegisteredParameter('colorscheme',
                                              angle2color.Angle2Color,
                                     tip='Method for converting angles to colors.'),
                color.ColorParameter('no_material', color.blue,
                       tip="Color to use for pixels with no assigned Material"),
                color.ColorParameter('no_orientation', color.black,
                       tip='Color to use for pixels with no Orientation Property')],
        layerordering=display.Planar(0.6),
        whoclasses = ('Microstructure',),
        tip="Display the Orientation Property of pixels.",
        discussion=xmlmenudump.loadFile(
                     'DISCUSSIONS/engine/reg/orientationdisplay.xml'))
