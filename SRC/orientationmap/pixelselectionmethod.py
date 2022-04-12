# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from ooflib.SWIG.common import latticesystem
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.image import pixelselectioncourieri
from ooflib.SWIG.orientationmap import orientmapdata
from ooflib.SWIG.orientationmap import pixeldifferentiatoro
from ooflib.SWIG.orientationmap import pixelselectioncouriero
from ooflib.common import debug
from ooflib.common import pixelselectionmethod
from ooflib.common.IO import parameter

class OrientationSelector(pixelselectionmethod.SelectionMethod):
    def __init__(self, lattice_symmetry, misorientation):
        self.lattice_symmetry = lattice_symmetry
        self.misorientation = misorientation
    def select(self, immidge, pointlist, selector):
        ms = immidge.getMicrostructure()
        orientationmap = orientmapdata.getOrientationMap(ms)
        if orientationmap is None:
            raise ooferror.ErrUserError(
                "The Microstructure has no orientation map.")
        pt = ms.pixelFromPoint(pointlist[0])
        orientation = orientationmap.angle(pt) # a swigged COrientABG
        selector(pixelselectioncouriero.OrientationSelection(
            orientationmap, orientation,
            self.lattice_symmetry.schoenflies(), self.misorientation))


pixelselectionmethod.PixelSelectionRegistration(
    'Orientation',
    OrientationSelector,
    ordering=1.1,
    events=['up'],
    params=[
        latticesystem.LatticeSymmetryParameter(
            'lattice_symmetry',
            tip="Assume the material at each point has this symmetry, making some orientations equivalent."),
        parameter.FloatRangeParameter(
            'misorientation', (0, 180, 1), 0,
            tip="Select orientations with misorientation less than this, relative to the selected pixel's orientation, in degrees.")
        ],
    whoclasses=['Microstructure'],
    tip="Select pixels whose orientation is within the given misorientation of the selected pixel's orientation.")

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## TODO: This method should be suppressed in the Pixel Selection
## Toolbox if the microstructure has no orientation map.  The best way
## to do that might be to make OrientationMap a WhoClass, and treat it
## like an Image.  Then the 'whoclasses' entry in the Registration
## would do what we need here.

# Burning with Orientations and burning with colors are similar and
# can use the same pixel selection courier.
BurnSelection = pixelselectioncourieri.BurnSelection

class OrientationBurn(pixelselectionmethod.SelectionMethod):
    def __init__(self, local_flammability, global_flammability,
                 lattice_symmetry, next_nearest):
        self.local_flammability = local_flammability
        self.global_flammability = global_flammability
        self.lattice_symmetry = lattice_symmetry
        self.next_nearest = next_nearest
    def select(self, immidge, points, selector):
        mspath = immidge.getParent().path()
        ms = immidge.getMicrostructure()
        orientationmap = orientmapdata.getOrientationMap(ms)
        if orientationmap is None:
            raise ooferror.ErrUserError(
                "The Microstructure has no orientation map.")
        startpt = ms.pixelFromPoint(points[0])
        selectionctxt = ms.pixelselection.getObject()
        if selectionctxt.checkpixel(startpt):
            od = pixeldifferentiatoro.OrientationDifferentiator(
                mspath,
                self.local_flammability,
                self.global_flammability,
                self.lattice_symmetry)
            selector(BurnSelection(ms, od.cobj, startpt, self.next_nearest))
            
pixelselectionmethod.PixelSelectionRegistration(
    'OrientationBurn',
    OrientationBurn,
    ordering=1.11,
    params=[
        parameter.FloatRangeParameter(
            'local_flammability',
            range=(0, 180., 0.1), value=10,
            tip="Maximum misorientation angle, in degrees, between neighboring pixels, across which a burn will extend."),
        parameter.FloatRangeParameter(
            'global_flammability',
            range=(0, 180., 0.1), value=10,
            tip="Misorientation, in degrees measured from initial point, beyond which a burn will not spread."),
        latticesystem.LatticeSymmetryParameter(
            'lattice_symmetry',
            tip="Assume that the material at each point has this symmetry, making some orientations equivalent."),
        parameter.BooleanParameter(
            'next_nearest', value=False,
            tip="Burn next-nearest neighbors?")
        ],
    whoclasses=['Microstructure', 'Image'],
    events=['up'],
    tip='Select a contiguous set of similarly oriented pixels, using a forest fire algorithm on an orientation map.')
