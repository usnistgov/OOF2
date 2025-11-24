# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

from . import memorycheck
from .UTILS import file_utils

import math
import os
import unittest

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

    def checkPixel(self, ms, x, y, alpha, beta, gamma):
        orient, source = orientmapdata.getOrientationAtPoint(ms, iPoint(x, y))
        abg = orient.abg()
        self.assertAlmostEqual(math.degrees(abg.alpha()), alpha, 7)
        self.assertAlmostEqual(math.degrees(abg.beta()), beta, 7)
        self.assertAlmostEqual(math.degrees(abg.gamma()), gamma, 7)
        

    @memorycheck.check("orientmapMS")
    def OneOrientation(self):
        # orientmap0.tsl is 10x10 pixels with only one orientation,
        # which is 0,0,0.  
        self.readMap("orientmap0.tsl")
        ms = getMicrostructure("orientmapMS")
        self.assertEqual(ms.name(), "orientmapMS")
        self.assertEqual(microstructure.microStructures.nActual(), 1)
        # tslsimulator.py generated the data file, and it does strange
        # things with the pixel size, so that total physical
        # dimensions of the microstructure have weird off by one
        # divisior.
        self.assertAlmostEqual(
            (ms.size()-primitives.Point(10/9, 10/9)).norm2(), 0.0, 7)
        self.assertEqual(ms.sizeInPixels(), primitives.iPoint(10, 10))
        self.checkPixel(ms, 5, 5, 0.0, 0.0, 0.0)

    @memorycheck.check("orientmapMS")
    def TwoOrientations(self):
        # orientmap1.tsl is 100x100 pixels with two colors
        self.readMap("orientmap1.tsl")
        ms = getMicrostructure("orientmapMS")
        self.assertAlmostEqual(
            (ms.size()-primitives.Point(100/99, 100/99)).norm2(), 0.0, 7)
        self.checkPixel(ms, 25, 25, 10.0, 80.0, -100.0)
        self.checkPixel(ms, 65, 65, 0.0, 0.0, 0.0)

    @memorycheck.check("orientmapMS")
    def TwoOrientationsNotSquare(self):
        # orientmap3.tsl is 2x3 (almost) and 100x150 pixels with two colors
        self.readMap("orientmap3.tsl")
        ms = getMicrostructure("orientmapMS")
        self.assertAlmostEqual(
            (ms.size()-primitives.Point(2*100/99, 3*150/149)).norm2(), 0.0, 7)
        self.checkPixel(ms, 74, 101, 0.0, 0.0, 0.0)
        self.checkPixel(ms, 63, 24, 10., 80., -100.)
        self.checkPixel(ms, 37, 88, 10., 80., -100.)

test_set = [
    OOF_OrientationMapTest("OneOrientation"),
    OOF_OrientationMapTest("TwoOrientations"),
    OOF_OrientationMapTest("TwoOrientationsNotSquare")
]
    
