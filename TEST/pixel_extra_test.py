# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# These tests are "extra" in the sense that they re-run menu items
# which have already been run, but they do so under more challenging
# circumstances than the initial test, or because they rely on other
# features that weren't tested at the time that the first tests were
# run.

import unittest, os
import memorycheck
from UTILS.file_utils import reference_file

class OOF_Pixel_Extra(unittest.TestCase):
    def setUp(self):
        global microstructure
        from ooflib.common import microstructure
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","small.ppm"),
            microstructure_name="skeltest",
            height=20.0, width=20.0)
        OOF.Image.AutoGroup(image="skeltest:small.ppm")

    @memorycheck.check("skeltest")
    def SelectMaterialPixels(self):
        OOF.Material.New(name='material')
        OOF.Material.Assign(
            material='material', microstructure='skeltest', pixels='#000000')
        OOF.Material.New(name='otherstuff')
        OOF.Material.Assign(
            material='otherstuff', microstructure='skeltest', pixels='#f80000')
        ms = microstructure.microStructures['skeltest']
        pixelselection = ms.getSelectionContext()
        self.assertEqual(pixelselection.size(), 0)
        # Select pixels with either material.
        OOF.PixelSelection.Select_Material(
            microstructure='skeltest', material='<Any>')
        self.assertEqual(pixelselection.size(), 2955)
        # Select pixels with no material.
        OOF.PixelSelection.Clear(microstructure='skeltest')
        OOF.PixelSelection.Select_Material(
            microstructure='skeltest', material='<None>')
        self.assertEqual(pixelselection.size(), 19545)
        # Select pixels with a specified material.
        OOF.PixelSelection.Clear(microstructure='skeltest')
        OOF.PixelSelection.Select_Material(
            microstructure='skeltest', material='material')
        self.assertEqual(pixelselection.size(), 2585)
        # Try again with no materials assigned.  This test is
        # important because it ensures that the iterators are looking
        # at every pixel.
        OOF.Material.Remove(microstructure='skeltest', pixels=all)
        OOF.PixelSelection.Clear(microstructure='skeltest')
        OOF.PixelSelection.Select_Material(
            microstructure='skeltest', material='<Any>')
        self.assertEqual(pixelselection.size(), 0)
        OOF.PixelSelection.Clear(microstructure='skeltest')
        OOF.PixelSelection.Select_Material(
            microstructure='skeltest', material='<None>')
        self.assertEqual(pixelselection.size(), 22500)
        OOF.PixelSelection.Clear(microstructure='skeltest')
        OOF.PixelSelection.Select_Material(
            microstructure='skeltest', material='material')
        self.assertEqual(pixelselection.size(), 0)
        
        OOF.Material.Delete(name="material")
        OOF.Material.Delete(name="otherstuff")

test_set = [
    OOF_Pixel_Extra("SelectMaterialPixels")
]
