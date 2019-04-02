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
from ooflib.SWIG.orientationmap import orientmapdata
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
