# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# File for testing pixel grouping and selection operations on
# microstructures.  This includes re-running the Microstructure
# save/load and copy operations to ensure that they save/load/copy the
# pixel groups correctly.

# Need to be able to open a graphics window and make selections,
# also, of course.

import unittest, os
from . import memorycheck
from .UTILS import file_utils
reference_file = file_utils.reference_file

from ooflib.common import color
from ooflib.common import microstructure
from ooflib.common import pixelselection
from ooflib.common.IO import gfxmanager
from ooflib.common.IO.reporter import messagemanager

def pixelSelectionCtxt(msname):
    return pixelselection.pixelselectionWhoClass[msname]

def pixelSelectionObj(msname):
    return pixelselection.pixelselectionWhoClass[msname].getObject()

def pixelSelectionSize(msname):
    return len(pixelSelectionObj(msname))

def pixelSelection(msname):
    return pixelSelectionObj(msname).members()

# Prerequisite for making toolbox selections is the existence of a
# graphics window.  These tests just open and close a graphics window.
class Graphics_Ops(unittest.TestCase):

    # Opens a new graphics window, assuming that none are open (so
    # that the name will be "Graphics_1").
    @memorycheck.check()
    def New(self):
        self.assertRaises(AttributeError,
                          OOF.Windows.__getattr__,
                          attr="Graphics_1")
        OOF.Windows.Graphics.New()
        self.assertTrue(hasattr(OOF.Windows.Graphics, "Graphics_1"))
        self.assertTrue(hasattr(OOF, "Graphics_1"))
        self.assertEqual(len(gfxmanager.gfxManager.windows), 1)

    # "Close" Assumes that a graphics window is open.  The "Close"
    # item is actually in OOF.Graphics_n, not in OOF.Windows.Graphics.
    @memorycheck.check()
    def Close(self):
        # Find the graphics window.
        self.assertTrue(len(OOF.Windows.Graphics.items)==2)
        for item in OOF.Windows.Graphics.items:
            if item.name[:8]=="Graphics":
                item_name=item.name
                break
        self.assertTrue(item_name is not None)
        # Get the corresponding item from the OOF menu.
        gw_item = OOF.__getattr__(item_name)
        gw_item.File.Close()
        self.assertTrue(len(OOF.Windows.Graphics.items)==1)
        self.assertTrue(not hasattr(OOF.Windows.Graphics, item_name))

    def tearDown(self):
        pass

# Tests of actual pixel selection operations.
# OOF.Toolbox.Pixel_Select items:
#   Point, Brush, Rectangle, Circle, Ellipse, Color, Burn.
# Selection modifiers from the same menu, Clear, Undo, Redo, Invert

class Direct_Pixel_Selection(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("image_data","image_test.png"),
            microstructure_name=automatic,
            height=automatic, width=automatic)
        OOF.Windows.Graphics.New()

    def tearDown(self):
        OOF.Graphics_1.File.Close()

    # Direct selection operations -- these are toolbox ops in the
    # graphics window.
    # Select circle, rectangle, ellipse, point.
    @memorycheck.check("image_test.png")
    def Circle(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="image_test.png:image_test.png",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0, ctrl=0)
        # Size should be 2000 pixels.
        self.assertEqual(pixelSelectionSize('image_test.png'), 2000)

    # Makes and clears a selection.  Uses the circle selector, so
    # that one should be tested first.
    @memorycheck.check("image_test.png")
    def Clear(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="image_test.png:image_test.png",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0, ctrl=0)
        self.assertNotEqual(pixelSelectionSize('image_test.png'), 0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source="image_test.png:image_test.png")
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)

    # Remining direct selection methods --
    # Point, Brush, Rectangle, Ellipse, Color, Burn.

    @memorycheck.check("image_test.png")
    def Point(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="image_test.png:image_test.png",
            points=[Point(52.0, 70.0)], shift=0, ctrl=0)
        # Size should be 1 pixel, of course.
        self.assertEqual(pixelSelectionSize('image_test.png'), 1)
        self.assertEqual(pixelSelection('image_test.png'), [iPoint(52,70)])

    # Brush points were recorded from an actual user session.
    @memorycheck.check("image_test.png")
    def Brush(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='image_test.png:image_test.png',
            style=CircleBrush(radius=2.0),
            points=[Point(19.12,61.2829), Point(19.642,61.2829),
                    Point(20.1639,61.2829), Point(21.2078,61.2829),
                    Point(21.7298,60.761), Point(22.2518,60.761),
                    Point(22.7737,60.761), Point(23.2957,60.761), 
                    Point(23.8176,60.761), Point(24.3396,60.761), 
                    Point(24.8616,60.761), Point(25.3835,60.761), 
                    Point(25.9055,60.761), Point(26.4275,60.761), 
                    Point(26.9494,60.761), Point(27.4714,60.761), 
                    Point(27.9933,60.761), Point(28.5153,60.761), 
                    Point(29.0373,60.761), Point(29.0373,60.239), 
                    Point(29.5592,60.239), Point(30.0812,60.239), 
                    Point(30.6031,60.239), Point(31.1251,60.239), 
                    Point(31.6471,60.239), Point(32.169,60.239), 
                    Point(32.691,60.239), Point(33.2129,60.239), 
                    Point(33.7349,60.239), Point(34.2569,60.239), 
                    Point(34.7788,60.239), Point(35.3008,60.239), 
                    Point(35.8227,60.239), Point(36.3447,60.239), 
                    Point(36.8667,60.239), Point(37.3886,60.239), 
                    Point(37.9106,60.239), Point(38.4325,60.239), 
                    Point(38.9545,60.239), Point(39.4765,60.239), 
                    Point(39.9984,60.239)], shift=0, ctrl=0)
        self.assertEqual(pixelSelectionSize('image_test.png'), 99)


    @memorycheck.check("image_test.png")
    def Rectangle(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='image_test.png:image_test.png',
            points=[Point(23.3,57.0), Point(123.0,24.75)],
            shift=0, ctrl=0)
        self.assertEqual(pixelSelectionSize('image_test.png'), 3434)
        
    @memorycheck.check("image_test.png")
    def Ellipse(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse(
            source='image_test.png:image_test.png',
            points=[Point(23.3,57.0), Point(123.0,24.75)],
            shift=0, ctrl=0)
        self.assertEqual(pixelSelectionSize('image_test.png'), 2526)

    @memorycheck.check("image_test.png")
    def Color(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Color(
            source='image_test.png:image_test.png',
            range=DeltaRGB(delta_red=0.3, delta_green=0.3, delta_blue=0.3),
            points=[Point(14.7,62.1)], shift=0, ctrl=0)
        self.assertEqual(pixelSelectionSize('image_test.png'), 4204)

    @memorycheck.check("image_test.png")
    def Burn(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Burn(
            source='image_test.png:image_test.png',
            local_flammability=0.1,global_flammability=0.2,
            color_space_norm="L1", next_nearest=False,
            points=[Point(14.7,62.1)], shift=0, ctrl=0)
        self.assertEqual(pixelSelectionSize('image_test.png'), 4195)


    # Then, mechanical ones -- Undo, Redo, Invert.

    @memorycheck.check("image_test.png")
    def Undo(self):
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        self.assertTrue(not pixelSelectionCtxt('image_test.png').undoable())
        ps_0_id = id(pixelSelectionObj('image_test.png'))
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="image_test.png:image_test.png",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0, ctrl=0)
        self.assertTrue(pixelSelectionCtxt('image_test.png').undoable())
        ps_1_id = id(pixelSelectionObj('image_test.png'))
        self.assertNotEqual(ps_0_id, ps_1_id)
        OOF.Graphics_1.Toolbox.Pixel_Select.Undo(
            source="image_test.png:image_test.png")
        ps_2_id = id(pixelSelectionObj('image_test.png'))
        self.assertEqual(ps_0_id, ps_2_id)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)

    @memorycheck.check("image_test.png")
    def Redo(self):
         ps = pixelSelectionCtxt('image_test.png')
         ps_0_id = id(ps.getObject())
         OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
             source="image_test.png:image_test.png",
             points=[Point(66.2,55.0), Point(87.6,41.8)],
             shift=0, ctrl=0)
         ps_1_id = id(ps.getObject())
         OOF.Graphics_1.Toolbox.Pixel_Select.Undo(
             source="image_test.png:image_test.png")
         self.assertTrue(ps.redoable())
         OOF.Graphics_1.Toolbox.Pixel_Select.Redo(
             source="image_test.png:image_test.png")
         self.assertEqual(id(ps.getObject()), ps_1_id)
         self.assertTrue(not ps.redoable())

    @memorycheck.check("image_test.png")
    def Clear(self):
        ps = pixelSelectionCtxt("image_test.png")
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
             source="image_test.png:image_test.png",
             points=[Point(66.2,55.0), Point(87.6,41.8)],
             shift=0, ctrl=0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source="image_test.png:image_test.png")
        ps_1_id = id(ps.getObject())
        self.assertEqual(ps.getObject().len(), 0)
        self.assertNotEqual(ps_0_id, ps_1_id)

    @memorycheck.check("image_test.png")
    def Invert(self):
         OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
             source="image_test.png:image_test.png",
             points=[Point(66.2,55.0), Point(87.6,41.8)],
             shift=0, ctrl=0)
         OOF.Graphics_1.Toolbox.Pixel_Select.Invert(
             source="image_test.png:image_test.png")
         self.assertEqual(pixelSelectionSize('image_test.png'), 16166)

    # Tests for selections in which the initial and/or final mouse
    # points are outside the bounds of the Microstructure.
    
    @memorycheck.check("image_test.png")
    def ExoPoint(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source='image_test.png:image_test.png',
            points=[Point(-5.8, 61.0)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source='image_test.png:image_test.png',
            points=[Point(74.,132.)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source='image_test.png:image_test.png',
            points=[Point(157.,57.)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source='image_test.png:image_test.png',
            points=[Point(74.,-10.)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)

    @memorycheck.check("image_test.png")
    def ExoBrush(self):
        # Path starts and ends inside, but crosses the image
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='image_test.png:image_test.png',
            style=CircleBrush(radius=10),
            points=[Point(-12.14420000000001,104.544),
                    Point(-11.515000000000011,104.544),
                    Point(-5.8522000000000105,105.8024),
                    Point(2.3273999999999906,107.69),
                    Point(10.506999999999993,110.836),
                    Point(17.428199999999993,113.982),
                    Point(24.349399999999996,117.128),
                    Point(34.416599999999995,120.9032),
                    Point(44.483799999999995,124.6784),
                    Point(47.629799999999996,126.566),
                    Point(49.517399999999995,128.4536)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 737)
        # Path starts and ends outside on the left, without touching
        # the image
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='image_test.png:image_test.png',
            style=CircleBrush(radius=10),
            points=[Point(-14.031800000000011,94.4768),
                    Point(-14.031800000000011,94.4768),
                    Point(-14.031800000000011,94.4768),
                    Point(-14.031800000000011,93.8476),
                    Point(-14.031800000000011,91.3308),
                    Point(-13.402600000000012,88.814),
                    Point(-12.773400000000011,85.668),
                    Point(-12.14420000000001,83.15119999999999),
                    Point(-11.515000000000011,80.6344),
                    Point(-11.515000000000011,79.376),
                    Point(-11.515000000000011,78.1176),
                    Point(-11.515000000000011,78.1176),
                    Point(-11.515000000000011,77.48839999999998),
                    Point(-11.515000000000011,77.48839999999998),
                    Point(-11.515000000000011,77.48839999999998),
                    Point(-11.515000000000011,77.48839999999998),
                    Point(-11.515000000000011,77.48839999999998),
                    Point(-11.515000000000011,76.85919999999999),
                    Point(-11.515000000000011,76.85919999999999),
                    Point(-11.515000000000011,76.85919999999999),
                    Point(-11.515000000000011,76.85919999999999),
                    Point(-10.88580000000001,76.85919999999999)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        # Path starts and ends outside on the right, without touching
        # the image
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='image_test.png:image_test.png',
            style=CircleBrush(radius=10),
            points=[Point(166.5486,93.8476),
                    Point(166.5486,93.2184),
                    Point(166.5486,92.5892),
                    Point(165.9194,91.3308),
                    Point(165.9194,88.814),
                    Point(165.9194,85.0388),
                    Point(165.9194,83.15119999999999),
                    Point(165.9194,81.8928),
                    Point(165.9194,80.6344),
                    Point(165.9194,79.376),
                    Point(165.9194,79.376),
                    Point(165.9194,79.376),
                    Point(165.9194,79.376)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        # Path starts outside and ends inside
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='image_test.png:image_test.png',
            style=CircleBrush(radius=10),
            points=[Point(79.0898,141.0376),
                    Point(79.0898,141.0376),
                    Point(78.4606,140.4084),
                    Point(78.4606,138.5208),
                    Point(78.4606,134.7456),
                    Point(78.4606,130.34120000000001),
                    Point(78.4606,127.8244),
                    Point(78.4606,124.6784),
                    Point(78.4606,121.5324),
                    Point(78.4606,117.128),
                    Point(79.0898,113.982),
                    Point(79.0898,110.836),
                    Point(79.0898,110.2068),
                    Point(79.0898,110.2068),
                    Point(79.0898,109.5776),
                    Point(79.0898,108.94839999999999),
                    Point(79.0898,107.69),
                    Point(79.0898,106.4316),
                    Point(79.0898,105.8024),
                    Point(79.0898,105.8024),
                    Point(79.0898,105.8024),
                    Point(79.0898,105.8024),
                    Point(79.0898,105.8024),
                    Point(76.57300000000001,105.8024)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 498)
        # Path starts inside and ends outside
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='image_test.png:image_test.png',
            style=CircleBrush(radius=10),
            points=[Point(83.4942,12.05159999999998),
                    Point(83.4942,12.05159999999998),
                    Point(83.4942,9.53479999999999),
                    Point(83.4942,5.759599999999978),
                    Point(83.4942,-0.5324000000000098),
                    Point(83.4942,-6.195200000000014),
                    Point(83.4942,-13.116400000000013),
                    Point(83.4942,-18.779200000000017),
                    Point(84.1234,-24.44200000000002),
                    Point(84.1234,-25.700400000000016),
                    Point(84.1234,-25.700400000000016),
                    Point(84.1234,-25.700400000000016),
                    Point(84.1234,-25.700400000000016),
                    Point(84.1234,-25.700400000000016)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 394)

    @memorycheck.check("image_test.png")
    def ExoRectangle(self):
        # Fully out of bounds on the left
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='image_test.png:image_test.png',
            points=[Point(-18.,85.), Point(-7.,49.)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        # Fully out of bounds on the right
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='image_test.png:image_test.png',
            points=[Point(157.,86.), Point(166.,40.)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        # Crossing from top to bottom
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='image_test.png:image_test.png',
            points=[Point(97.33,131.60), Point(125.02,-14.37)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 3509)
        # Starting outside, ending outside, enclosing a corner
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='image_test.png:image_test.png',
            points=[Point(131.31,132.85), Point(165.29,96.36)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 475)
        # Starting outside, ending inside
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='image_test.png:image_test.png',
            points=[Point(158.99,48.54), Point(109.92,66.16)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 779)

    @memorycheck.check("image_test.png")
    def ExoCircle(self):
        # Fully out of bounds on the top
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source='image_test.png:image_test.png',
            points=[Point(68.39,142.92), Point(76.57,133.48)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        # Center out of bounds on the top, mouse release in bounds
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source='image_test.png:image_test.png',
            points=[Point(74.0562,132.858), Point(76.57300000000001,110.2068)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 302)
        # Center in bounds, but mouse release out of bounds
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source='image_test.png:image_test.png',
            points=[Point(140.12,10.16), Point(156.48,-6.19)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 969)
        # Center and release out of bounds, but circle partly in bounds
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source='image_test.png:image_test.png',
            points=[Point(-7.11,61.12), Point(-10.25,40.99)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 367)

    @memorycheck.check("image_test.png")
    def ExoEllipse(self):
        # Fully out of bounds below
        OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse(
            source='image_test.png:image_test.png',
            points=[Point(43.85,-6.82), Point(111.17,-26.32)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 0)
        # Crossing from outside on the left to outside on the right
        OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse(
            source='image_test.png:image_test.png',
            points=[Point(-10.25,69.30), Point(157.11,44.76)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 3088)
        # Mouse points out of bounds, ellipse grazing an edge
        OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse(
            source='image_test.png:image_test.png',
            points=[Point(33.15,128.45), Point(92.93,117.75)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('image_test.png'), 126)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Test a subset of the pixel selection operations for non-square
# pixels.

class NonSquare(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data", "small.ppm"),
            microstructure_name=automatic,
            height=2., width=1.618)
        OOF.Windows.Graphics.New()
              
    def tearDown(self):
        OOF.Graphics_1.File.Close()

    @memorycheck.check("small.ppm")
    def Point(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source='small.ppm:small.ppm',
            points=[Point(0.3895,1.65173)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('small.ppm'), 1)
        self.assertEqual(pixelSelection('small.ppm'), [iPoint(36,123)])

    @memorycheck.check("small.ppm")
    def Brush(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='small.ppm:small.ppm',
            style=CircleBrush(radius=0.1),
            points=[Point(-0.17900000000000002,1.0832),
                    Point(-0.17900000000000002,1.0832),
                    Point(-0.17900000000000002,1.0832),
                    Point(-0.17206666666666667,1.0901333333333332),
                    Point(-0.17206666666666667,1.0901333333333332),
                    Point(-0.17206666666666667,1.0901333333333332),
                    Point(-0.16513333333333335,1.0901333333333332),
                    Point(-0.1582,1.0970666666666666),
                    Point(-0.1512666666666667,1.104),
                    Point(-0.14433333333333337,1.1109333333333333),
                    Point(-0.13046666666666668,1.1178666666666666),
                    Point(-0.11660000000000001,1.1248),
                    Point(-0.10273333333333334,1.1317333333333333),
                    Point(-0.09580000000000001,1.1386666666666665),
                    Point(-0.08193333333333334,1.1456),
                    Point(-0.06806666666666668,1.1456),
                    Point(-0.04726666666666668,1.1525333333333334),
                    Point(-0.026466666666666677,1.1525333333333334),
                    Point(-0.005666666666666674,1.1594666666666666),
                    Point(0.028999999999999995,1.1594666666666666),
                    Point(0.0498,1.1663999999999999),
                    Point(0.09833333333333333,1.1663999999999999),
                    Point(0.133,1.1663999999999999),
                    Point(0.1746,1.1663999999999999),
                    Point(0.22313333333333332,1.1663999999999999),
                    Point(0.2786,1.1663999999999999),
                    Point(0.3340666666666667,1.1594666666666666),
                    Point(0.36873333333333336,1.1525333333333334),
                    Point(0.4103333333333333,1.1456),
                    Point(0.43806666666666666,1.1386666666666665),
                    Point(0.47273333333333334,1.1317333333333333),
                    Point(0.5004666666666667,1.1178666666666666),
                    Point(0.549,1.0970666666666666),
                    Point(0.5836666666666667,1.0762666666666667),
                    Point(0.6183333333333334,1.0554666666666668),
                    Point(0.653,1.0277333333333334),
                    Point(0.6807333333333333,1.0138666666666667),
                    Point(0.6876666666666666,1.0069333333333332)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('small.ppm'), 1122)

    @memorycheck.check("small.ppm")
    def Rectangle(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='small.ppm:small.ppm',
            points=[Point(0.2647333333333333,0.6741333333333333),
                    Point(0.7847333333333334,0.23039999999999994)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('small.ppm'), 1666)

    @memorycheck.check("small.ppm")
    def Circle(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source='small.ppm:small.ppm',
            points=[Point(0.7500666666666667,1.1802666666666668),
                    Point(0.9164666666666668,1.0277333333333334)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('small.ppm'), 1099)
        # Both positions out of bounds
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source='small.ppm:small.ppm',
            points=[Point(1.7346000000000001,0.5978666666666665),
                    Point(1.8039333333333334,0.8058666666666665)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('small.ppm'), 188)

    @memorycheck.check('small.ppm')
    def Ellipse(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse(
            source='small.ppm:small.ppm',
            points=[Point(0.29246666666666665,1.5477333333333334),
                    Point(0.48660000000000003,0.6949333333333332)],
            shift=False, ctrl=False)
        self.assertEqual(pixelSelectionSize('small.ppm'), 909)


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Pixel group creation and manipulation tests.

# OOF.PixelGroup:
# New Rename Copy Delete Meshable AddSelection RemoveSelection Clear
# Query

# These tests use the "small.ppm" image, which autogroups
# cleanly, rather than the more difficult image_test.png.

class Pixel_Groups(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","small.ppm"),
            microstructure_name=automatic,
            height=10., width=automatic) # pixels are not 1x1 in physical units
        OOF.Windows.Graphics.New()

    @memorycheck.check("small.ppm")
    def New(self):
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        ms = microstructure.getMicrostructure("small.ppm")
        groups = ms.groupNames()
        self.assertEqual(len(groups),1)
        self.assertTrue("test" in groups)

    @memorycheck.check("small.ppm")
    def Delete(self):
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        ms = microstructure.getMicrostructure("small.ppm")
        OOF.PixelGroup.Delete(microstructure="small.ppm", group="test")
        groups = ms.groupNames()
        self.assertEqual(len(groups),0)

    # Uses "circle" selection.  Clear the selection before measuring
    # the size of the group.
    @memorycheck.check("small.ppm")
    def AddSelection(self):
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        ms = microstructure.getMicrostructure("small.ppm")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelGroup.AddSelection(
            microstructure="small.ppm", group="test")
        ps = pixelselection.pixelselectionWhoClass['small.ppm']
        sel_size = ps.getObject().len()
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source="small.ppm:small.ppm")
        group = ms.findGroup("test")
        self.assertEqual(len(group), sel_size)
        
    @memorycheck.check("small.ppm")
    def RemoveSelection(self):
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        ms = microstructure.getMicrostructure("small.ppm")
        ps = pixelselection.pixelselectionWhoClass['small.ppm']
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        sel_large = ps.getObject().len()
        OOF.PixelGroup.AddSelection(
            microstructure="small.ppm", group="test")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(80.0,41.5)],
            shift=0,ctrl=0)
        sel_small = ps.getObject().len()
        OOF.PixelGroup.RemoveSelection(
            microstructure="small.ppm", group="test")
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source="small.ppm:small.ppm")
        group = ms.findGroup("test")
        self.assertEqual(len(group), sel_large-sel_small)

    @memorycheck.check("small.ppm")
    def Copy(self):
        ms = microstructure.getMicrostructure("small.ppm")
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelGroup.AddSelection(
            microstructure="small.ppm", group="test")
        group = ms.findGroup("test")
        initial_group_size = len(group)
        OOF.PixelGroup.Copy(microstructure="small.ppm",
                            group="test", name="testcopy")
        OOF.PixelGroup.Delete(microstructure="small.ppm", group="test")
        self.assertEqual(ms.nGroups(), 1)
        group = ms.findGroup("testcopy")
        self.assertEqual(len(group), initial_group_size) 
        
    @memorycheck.check("small.ppm")
    def Rename(self):
        ms = microstructure.getMicrostructure("small.ppm")
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelGroup.AddSelection(
            microstructure="small.ppm", group="test")
        group = ms.findGroup("test")
        initial_group_size = len(group)
        OOF.PixelGroup.Rename(microstructure="small.ppm",
                              group="test", new_name="testrename")
        group = ms.findGroup("testrename")
        self.assertEqual(len(group), initial_group_size)
        # Still only one group.
        self.assertEqual(ms.nGroups(), 1)
        self.assertTrue( not "test" in ms.groupNames())
        
    @memorycheck.check("small.ppm")
    def AutoGroup(self):
        def colordiff(c1,c2):
            return (c1.red-c2.red)**2 + \
                   (c1.green-c2.green)**2 + \
                   (c1.blue-c2.blue)**2
        # Dictionary of nearest pure colors and sizes of the
        # corresponding groups, which will not have exactly this
        # color, but will be closer to it than to any other color (in
        # colordiff measure).
        expected_sizes = {color.magenta : 2404,
                          color.RGBColor(1.0,1.0,1.0) : 4781,
                          color.RGBColor(0.0,0.0,0.0) : 2585,
                          color.blue : 2947,
                          color.green : 4795,
                          color.cyan : 1001,
                          color.yellow : 3617,
                          color.red : 370 }

        OOF.Image.AutoGroup(image="small.ppm:small.ppm", name_template='%c')
        ms = microstructure.getMicrostructure("small.ppm")
        groups = ms.groupNames()
        self.assertEqual(len(groups), 8)
        for name in groups:
#             rgb = eval(name)
            rgb = color.rgb_from_hex(name)
            key = None
            diff = None
            for c in expected_sizes.keys():
                cdiff = colordiff(rgb,c)
                if (diff is None) or (cdiff < diff):
                    key = c
                    diff = cdiff
            self.assertEqual(len(ms.findGroup(name)), expected_sizes[key])

    # TODO: tests for the statistical auto group

    @memorycheck.check("small.ppm")
    def Query(self):
        OOF.Image.AutoGroup(image='small.ppm:small.ppm', name_template='%c')
        # Query the small red group at the top of small.ppm
        OOF.PixelGroup.Query(
            microstructure='small.ppm',
            group='#f80000',
            units='Physical',
            contiguous=False)
        lines = messagemanager.latest(9)
        # Dump lines to a file so as to use fp_file_compare.
        phile = open("test.dat", "w")
        for line in lines:
            print(line, file=phile)
        phile.close()
        self.assertTrue(file_utils.fp_file_compare(
            'test.dat',
            os.path.join('ms_data', 'pixelinfo1.dat'),
            1.e-6))
        file_utils.remove('test.dat')
        # Query the red group again, using fractional units.
        OOF.PixelGroup.Query(
            microstructure='small.ppm',
            group='#f80000',
            units='Fractional',
            contiguous=False)
        lines = messagemanager.latest(9)
        phile = open("test.dat", "w")
        for line in lines:
            print(line, file=phile)
        phile.close()
        self.assertTrue(file_utils.fp_file_compare(
            'test.dat',
            os.path.join('ms_data', 'pixelinfo2.dat'),
            1.e-6))
        file_utils.remove('test.dat')
        # Query the red group again, using pixel units.
        OOF.PixelGroup.Query(
            microstructure='small.ppm',
            group='#f80000',
            units='Pixel',
            contiguous=False)
        lines = messagemanager.latest(9)
        phile = open("test.dat", "w")
        for line in lines:
            print(line, file=phile)
        phile.close()
        self.assertTrue(file_utils.fp_file_compare(
            'test.dat',
            os.path.join('ms_data', 'pixelinfo3.dat'),
            1.e-6))
        file_utils.remove('test.dat')
        # Make a new group by combining two others
        OOF.PixelGroup.New(
            name='doublegroup',
            microstructure='small.ppm')
        # Select the yellow group
        OOF.PixelSelection.Select_Group(
            microstructure='small.ppm',
            group='#f8fc00')
        # Also select the red group
        OOF.PixelSelection.Add_Group(
            microstructure='small.ppm',
            group='#f80000')
        # Put the selection in a new group
        OOF.PixelGroup.AddSelection(
            microstructure='small.ppm',
            group='doublegroup')
        # Query it in physical units
        OOF.PixelGroup.Query(
            microstructure='small.ppm',
            group='doublegroup',
            units='Pixel',
            contiguous=False)
        lines = messagemanager.latest(9)
        phile = open("test.dat", "w")
        for line in lines:
            print(line, file=phile)
        phile.close()
        self.assertTrue(file_utils.fp_file_compare(
            'test.dat',
            os.path.join('ms_data', 'pixelinfo4.dat'),
            1.e-6))
        file_utils.remove('test.dat')
        # Query it again, but use contiguous=True.
        OOF.PixelGroup.Query(
            microstructure='small.ppm',
            group='doublegroup',
            units='Pixel',
            contiguous=True)
        lines = messagemanager.latest(20)
        phile = open("test.dat", "w")
        for line in lines:
            print(line, file=phile)
        phile.close()
        self.assertTrue(file_utils.fp_file_compare(
            'test.dat',
            os.path.join('ms_data', 'pixelinfo5.dat'),
            1.e-6))
        file_utils.remove('test.dat')
    
    # Meshable may be better tested at skel-mod time.
        
    def tearDown(self):
        OOF.Graphics_1.File.Close()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Pixel selection modifers.
# OOF.PixelSelection:
# Undo Redo Clear Invert Select_Group Add_Group Unselect_Group
# Intersect_Group Despeckle Elkcepsed Expand Shrink Color_Range Copy

## Tests for Select_Element_Pixels and Select_Segment_Pixels are in
## skeleton_extra_test.py, the test for Select_Material is in
## pixel_extra_test.py.

class Selection_Modify(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","small.ppm"),
            microstructure_name=automatic,
            height=automatic, width=automatic)
        OOF.Windows.Graphics.New()

    # A lot of the obvious checks are already done in the undo test in
    # Direct_Pixel_Selection.
    @memorycheck.check("small.ppm")
    def Undo(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        ps_1_id = id(ps.getObject())
        OOF.PixelSelection.Undo(microstructure="small.ppm")
        ps_2_id = id(ps.getObject())
        self.assertEqual(ps_2_id, ps_0_id)
        self.assertNotEqual(ps_2_id, ps_1_id)

    @memorycheck.check("small.ppm")
    def Redo(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        ps_1_id = id(ps.getObject())
        OOF.PixelSelection.Undo(microstructure="small.ppm")
        OOF.PixelSelection.Redo(microstructure="small.ppm")
        ps_2_id = id(ps.getObject())
        self.assertTrue(not ps.redoable())
        self.assertEqual(ps_2_id, ps_1_id)
        self.assertNotEqual(ps_2_id, ps_0_id)

    @memorycheck.check("small.ppm")
    def Clear(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelSelection.Clear(microstructure="small.ppm")
        ps_1_id = id(ps.getObject())
        self.assertEqual(ps.getObject().len(), 0)
        self.assertNotEqual(ps_0_id, ps_1_id)

    @memorycheck.check("small.ppm")
    def Invert(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelSelection.Invert(microstructure="small.ppm")
        self.assertEqual(ps.getObject().len(), 20500)

    @memorycheck.check("small.ppm")
    def Copy(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        OOF.Microstructure.Copy(microstructure="small.ppm", name="copy")
        copy_ps = pixelselection.pixelselectionWhoClass["copy"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        self.assertEqual(copy_ps.getObject().len(), 0)
        OOF.PixelSelection.Copy(microstructure="copy",
                                source="small.ppm")
        self.assertEqual(copy_ps.getObject().len(),
                         ps.getObject().len())
        OOF.Microstructure.Delete(microstructure="copy")

    @memorycheck.check("small.ppm")
    def Select_Group(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        OOF.PixelGroup.AddSelection(microstructure="small.ppm", group="test")
        OOF.PixelSelection.Undo(microstructure="small.ppm")
        OOF.PixelSelection.Select_Group(microstructure="small.ppm", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(), 2000)

    @memorycheck.check("small.ppm")
    def Add_Group(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        OOF.PixelGroup.AddSelection(microstructure="small.ppm", group="test")
        OOF.PixelSelection.Undo(microstructure="small.ppm")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(57.0,84.0), Point(67.0, 70.0)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelSelection.Add_Group(microstructure="small.ppm", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(), 2690)
        
    @memorycheck.check("small.ppm")
    def Unselect_Group(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        OOF.PixelGroup.AddSelection(microstructure="small.ppm", group="test")
        OOF.PixelSelection.Undo(microstructure="small.ppm")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(57.0,84.0), Point(67.0, 70.0)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelSelection.Unselect_Group(
            microstructure="small.ppm", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(), 690)
        
    @memorycheck.check("small.ppm")
    def Intersect_Group(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.PixelGroup.New(name="test", microstructure="small.ppm")
        OOF.PixelGroup.AddSelection(microstructure="small.ppm", group="test")
        OOF.PixelSelection.Undo(microstructure="small.ppm")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(57.0,84.0), Point(67.0, 70.0)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelSelection.Intersect_Group(
            microstructure="small.ppm", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(), 238)

    # Helper function, to make a selection suitable for use
    # by the Despeckle, Ekcepsed, Expand, and Shrink tests.
    
    def select_helper(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(36.0, 81.0), Point(47.5,72.0)],
            shift=0,ctrl=0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="small.ppm:small.ppm",
            points=[Point(37.0, 64.5)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="small.ppm:small.ppm",
            points=[Point(53.0, 81.0)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="small.ppm:small.ppm",
            points=[Point(36.0, 81.0)],
            shift=0, ctrl=1)
            
        
        
    @memorycheck.check("small.ppm")
    def Despeckle(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Despeckle(microstructure="small.ppm",
                                     neighbors=8)
        self.assertEqual(ps.getObject().len(), 682)


    @memorycheck.check("small.ppm")
    def Elkcepsed(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Elkcepsed(microstructure="small.ppm",
                                     neighbors=3)
        self.assertEqual(ps.getObject().len(), 679)

    @memorycheck.check("small.ppm")
    def Expand(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Expand(microstructure="small.ppm",
                                     radius=1.0)
        self.assertEqual(ps.getObject().len(), 773)

    @memorycheck.check("small.ppm")
    def Shrink(self): # You can't disintegrate me!!
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Shrink(microstructure="small.ppm",
                                     radius=1.0)
        self.assertEqual(ps.getObject().len(), 595)


    # Color range is a selector, not really a modifer, but there you go.
    @memorycheck.check("small.ppm")
    def Color_Range(self):
        ps = pixelselection.pixelselectionWhoClass["small.ppm"]
        OOF.PixelSelection.Color_Range(
            microstructure="small.ppm", image="small.ppm:small.ppm",
            reference=RGBColor(red=0.0,green=0.0,blue=0.0),
            range=DeltaRGB(delta_red=1.0,delta_green=0.0,delta_blue=1.0))
        self.assertEqual(ps.getObject().len(), 8306)
           

    # Element and segment ops can't be tested until skeletons exist.

    # Rich_MS_Copy is a test of the microstructure copying process now
    # that nontrivial groups and selections can be made -- these
    # should survive the copy process.  The magic numbers come from
    # the autogroup and circle-selection tests, also in this file.
    @memorycheck.check("small.ppm")
    def Rich_MS_Copy(self):
        OOF.Image.AutoGroup(image="small.ppm:small.ppm")
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="small.ppm:small.ppm",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0,ctrl=0)
        OOF.Microstructure.Copy(microstructure="small.ppm",
                                name="copy")

        # Essentially a re-run of the autogroup test.
        def colordiff(c1,c2):
            return (c1.red-c2.red)**2 + \
                   (c1.green-c2.green)**2 + \
                   (c1.blue-c2.blue)**2
        # Dictionary of nearest pure colors and sizes of the
        # corresponding groups, which will not have exactly this
        # color, but will be closer to it than to any other color (in
        # colordiff measure).
        expected_sizes = {color.magenta : 2404,
                          color.RGBColor(1.0,1.0,1.0) : 4781,
                          color.RGBColor(0.0,0.0,0.0) : 2585,
                          color.blue : 2947,
                          color.green : 4795,
                          color.cyan : 1001,
                          color.yellow : 3617,
                          color.red : 370 }
        ms = microstructure.getMicrostructure("copy")
        groups = ms.groupNames()
        self.assertEqual(len(groups), 8)
        for name in groups:
#            rgb = eval(name)
            rgb = color.rgb_from_hex(name)
            key = None
            diff = None
            for c in expected_sizes.keys():
                cdiff = colordiff(rgb,c)
                if (diff is None) or (cdiff < diff):
                    key = c
                    diff = cdiff
            self.assertEqual(len(ms.findGroup(name)), expected_sizes[key])
        ps = pixelselection.pixelselectionWhoClass["copy"]
        # Selection should *not* be copied.
        self.assertEqual(ps.getObject().len(), 0)
        OOF.Microstructure.Delete(microstructure="copy")
        

    def tearDown(self):
        OOF.Graphics_1.File.Close()
    
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#
    
test_set = [
    Graphics_Ops("New"),
    Graphics_Ops("Close"),
    Direct_Pixel_Selection("Circle"),
    Direct_Pixel_Selection("Clear"),
    Direct_Pixel_Selection("Point"),
    Direct_Pixel_Selection("Brush"),
    Direct_Pixel_Selection("Rectangle"),
    Direct_Pixel_Selection("Ellipse"),
    Direct_Pixel_Selection("Color"),
    Direct_Pixel_Selection("Burn"),
    Direct_Pixel_Selection("Undo"),
    Direct_Pixel_Selection("Redo"),
    Direct_Pixel_Selection("Clear"),
    Direct_Pixel_Selection("Invert"),
    Direct_Pixel_Selection("ExoPoint"),
    Direct_Pixel_Selection("ExoBrush"),
    Direct_Pixel_Selection("ExoRectangle"),
    Direct_Pixel_Selection("ExoCircle"),
    Direct_Pixel_Selection("ExoEllipse"),
    NonSquare("Point"),
    NonSquare("Brush"),
    NonSquare("Rectangle"),
    NonSquare("Circle"),
    NonSquare("Ellipse"),
    Pixel_Groups("AutoGroup"),
    Pixel_Groups("New"),
    Pixel_Groups("Delete"),
    Pixel_Groups("AddSelection"),
    Pixel_Groups("RemoveSelection"),
    Pixel_Groups("Copy"),
    Pixel_Groups("Rename"),
    Selection_Modify("Undo"),
    Selection_Modify("Redo"),
    Selection_Modify("Clear"),
    Selection_Modify("Invert"),
    Selection_Modify("Copy"),
    Selection_Modify("Select_Group"),
    Selection_Modify("Add_Group"),
    Selection_Modify("Unselect_Group"),
    Selection_Modify("Intersect_Group"),
    Selection_Modify("Despeckle"),
    Selection_Modify("Elkcepsed"),
    Selection_Modify("Expand"),
    Selection_Modify("Shrink"),
    Selection_Modify("Color_Range"),
    Selection_Modify("Rich_MS_Copy"),
    Pixel_Groups("Query"),      # Should be after modifier tests.
]
