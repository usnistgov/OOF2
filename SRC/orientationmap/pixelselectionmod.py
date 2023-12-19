# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

## Pixel selection modifiers make selections without mouse input.

## TODO: Make this work if the Microstructure has either an
## Orientation Property or OrientationMap. It currently requires an
## OrientationMap.

from ooflib.SWIG.common import latticesystem
from ooflib.SWIG.common import ooferror
from ooflib.SWIG.orientationmap import orientmapdata
from ooflib.SWIG.orientationmap import pixelselectioncouriero
from ooflib.common import debug
from ooflib.common import pixelselectionmod
from ooflib.common import registeredclass
from ooflib.common.IO import parameter
from ooflib.common.IO import whoville
from ooflib.common.IO import xmlmenudump
from ooflib.engine.IO import orientationmatrix

class OrientationRange(pixelselectionmod.SelectionModifier):
    def __init__(self, orientation, lattice_symmetry, misorientation):
        self.orientation = orientation
        self.lattice_symmetry = lattice_symmetry
        self.misorientation = misorientation
    def __call__(self, ms, selection):
        curselection = selection.getObject()
        orientationmap = orientmapdata.getOrientationMap(ms)
        if orientationmap is None:
            raise ooferror.PyErrUserError(
                "The Microstructure has no orientation map.")
        selection.start()
        selection.clearAndSelect(
            pixelselectioncouriero.OrientationSelection(
                orientationmap, self.orientation.corient,
                self.lattice_symmetry.schoenflies(), self.misorientation))

registeredclass.Registration(
    'Orientation Range',
    pixelselectionmod.SelectionModifier,
    OrientationRange,
    ordering=10,
    params=[
        parameter.ConvertibleRegisteredParameter(
            'orientation',
            orientationmatrix.Orientation,
            tip="Select orientations similar to this."),
        latticesystem.LatticeSymmetryParameter(
            'lattice_symmetry',
            tip="Assume the material at each point has this symmetry, making some orientations equivalent."),
        parameter.FloatRangeParameter(
            'misorientation', (0, 180, 1), 0,
            tip="Select orientations with misorientation less than this, relative to the given orientation, in degrees.")
    ],
    tip="Select all pixels whose orientation is in a given range.",
    discussion=xmlmenudump.loadFile(
        "DISCUSSIONS/orientationmap/reg/orientationrange.xml")
)
