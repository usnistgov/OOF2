# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest, os
from . import memorycheck
from .UTILS import file_utils

# Tests for reading orientation maps and creating Microstructures from
# them.

## TODO: This just checks reading TSL files with the GenericReader.
## It should do more.

## TODO: polefigure_data should be renamed orientationmap_data or
## something like that, since the tests in polefigure_test.py are all
## commented out.

class OOF_OrientationMapTest(unittest.TestCase):
    def setUp(self):
        global microstructure
        global orientmapdata
        global primitives
        from ooflib.common import microstructure
        from ooflib.common import primitives
        from ooflib.SWIG.orientationmap import orientmapdata

    def readMap(self, filename):
        OOF.Microstructure.Create_From_OrientationMap_File(
            filename=file_utils.reference_file('polefigure_data', filename),
            reader=GenericReader(
                comment_character='#',
                separator=WhiteSpaceSeparator(),
                angle_column=1,
                angle_type=Bunge,
                angle_units='Radians',
                angle_offset=0,
                xy_column=4,
                scale_factor=1,
                flip_x=False,
                flip_y=True,
                groups=[]),
            microstructure='orientmapMS')

    @memorycheck.check("orientmapMS")
    def OneOrientation(self):
        # orientmap0.tsl is 10x10 with only one orientation, which is 0,0,0.
        self.readMap("orientmap0.tsl")
        ms = getMicrostructure("orientmapMS")
        self.assertEqual(ms.name(), "orientmapMS")
        self.assertEqual(microstructure.microStructures.nActual(), 1)
        self.assertAlmostEqual(
            (ms.size()-primitives.Point(10/9, 10/9)).norm2(), 0.0, 7)
        self.assertEqual(ms.sizeInPixels(), primitives.iPoint(10, 10))

        orient, source = orientmapdata.getOrientationAtPoint(ms, iPoint(5, 5))
        abg = orient.abg()
        self.assertEqual(abg.alpha(), 0.0)
        self.assertEqual(abg.beta(), 0.0)
        self.assertEqual(abg.gamma(), 0.0)
        

test_set = [
    OOF_OrientationMapTest("OneOrientation")
]
    
