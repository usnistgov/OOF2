# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Test suite for the menu commands under OOF.Image.*

# These functions assume that OOF.Microstructure commands work
# properly.  For proper regression testing, run microstructure_test
# first, then this one.

import os
import random
import sys
import unittest

from ooflib.SWIG.image import oofimage
from ooflib.common.IO.automatic import automatic
from ooflib.image import denoise
from ooflib.image import threshold

from . import memorycheck
from .UTILS.file_utils import reference_file

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Compare two image files. It's not possible to use filecmp.cmp
# because if the image format includes metadata, the files might
# differ even when the pixel data is identical.  Use skimage utilities
# instead.

import numpy
import skimage
from matplotlib import pyplot

def compare_image_files(imagefile0, imagefile1):
    image0 = oofimage.getNumpyData(imagefile0)
    image1 = oofimage.getNumpyData(imagefile1)

    if image0.shape != image1.shape:
        print(f"Image shapes don't agree: {image0.shape} {image1.shape}")
        return False
    compimg = skimage.util.compare_images(image0, image1, method="diff")
    diffnorm = numpy.linalg.norm(compimg)
    diffmax = compimg.max()
    if diffnorm > 0 or diffmax > 0:
        print(f"Image difference is nonzero: norm={diffnorm} max={diffmax}")
        return False
    return True

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class OOF_Image(unittest.TestCase):
    def setUp(self):
        global imagecontext
        from ooflib.image import imagecontext

    # OOF.File.Load.Image loads an image into a microstructure, but
    # the usual way to get them is to create a microstructure from an
    # image file.  There's also an OOF.File.Save.Image that needs testing.
    
    @memorycheck.check("rectangle.png")
    def Delete(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","rectangle.png"),
            microstructure_name="rectangle.png",
            height=automatic, width=automatic)
        OOF.Image.Delete(image="rectangle.png:rectangle.png")
        ms = getMicrostructure("rectangle.png")
        self.assertEqual(len(ms.imageNames()),0)
        self.assertEqual(len(ms.getImageContexts()), 0)

    @memorycheck.check("rectangle.png", "other")
    def Copy(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","rectangle.png"),
            microstructure_name="rectangle.png",
            height=automatic, width=automatic)
        OOF.Microstructure.New(name="other", width=150.0, height=121.0,
                               width_in_pixels=150, height_in_pixels=121)
        OOF.Image.Copy(image="rectangle.png:rectangle.png",
                       microstructure="other", name=automatic)
        ms_0 = getMicrostructure("rectangle.png")
        ms_1 = getMicrostructure("other")
        self.assertEqual(len(ms_1.imageNames()),1)
        self.assertTrue("rectangle.png" in ms_1.imageNames())
        # Ensure they're separate objects.
        self.assertNotEqual(id(ms_0.getImageContexts()[0]),
                            id(ms_1.getImageContexts()[0]))

    @memorycheck.check("rectangle.png")
    def Rename(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","rectangle.png"),
            microstructure_name="rectangle.png",
            height=automatic, width=automatic)
        ms_0 = getMicrostructure("rectangle.png")
        image_id = id(ms_0.getImageContexts()[0])
        OOF.Image.Rename(image="rectangle.png:rectangle.png",
                         name="newname")
        ms_0 = getMicrostructure("rectangle.png")
        image_id = id(ms_0.getImageContexts()[0])
        self.assertEqual(len(ms_0.imageNames()),1)
        self.assertTrue("newname" in ms_0.imageNames())
        self.assertEqual(image_id, id(ms_0.getImageContexts()[0]))

    # This test just checks that the groups are created and add up to
    # the right size.  Group operations are tested in more detail
    # elsewhere.
    @memorycheck.check("rectangle.png")
    def AutoGroup(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","rectangle.png"),
            microstructure_name="rectangle.png",
            height=automatic, width=automatic)
        OOF.Image.AutoGroup(image="rectangle.png:rectangle.png")
        ms = getMicrostructure("rectangle.png")
        self.assertEqual(ms.nGroups(), 7)
        self.assertEqual(ms.nCategories(), 7)
        # Check that the groups add up to the total size.
        size = 0
        for gname in ms.groupNames():
            size += len(ms.findGroup(gname))
        self.assertEqual(size, 121*150) # 121x150 is the size of the image.

    # Test for OOF.File.Load.Image, loading an RGB image into an
    # existing microstructure.
    @memorycheck.check("load_test")
    def Load(self):
        OOF.Microstructure.New(name="load_test",
                               width=150, height=121,
                               width_in_pixels=150, height_in_pixels=121)
        OOF.File.Load.Image(filename=reference_file("ms_data","rectangle.png"),
                            microstructure="load_test",
                            height=automatic, width=automatic)
        ms = getMicrostructure("load_test")
        ms_images = ms.imageNames()
        self.assertEqual(len(ms_images),1)
        self.assertTrue("rectangle.png" in ms_images)
        img = oofimage.getImage("load_test:rectangle.png")
        self.assertFalse(img.isGray())

    # Test for OOF.File.Load.Image, loading a grayscale image into an
    # existing microstructure.
    @memorycheck.check("gray")
    def LoadGray(self):
        OOF.Microstructure.New(name="gray",
                               width=100, height=100,
                               width_in_pixels=200, height_in_pixels=200)
        OOF.File.Load.Image(filename=reference_file("image_data",
                                                    "si3n4-small.png"),
                            microstructure="gray",
                            height=automatic, width=automatic)
        ms = getMicrostructure("gray")
        ms_images = ms.imageNames()
        self.assertEqual(len(ms_images), 1)
        self.assertTrue("si3n4-small.png" in ms_images)
        img = oofimage.getImage("gray:si3n4-small.png")
        self.assertTrue(img.isGray())

    # Check that images can be loaded from a microstructure file.
    @memorycheck.check("two_images")
    def LoadFromMS(self):
        OOF.File.Load.Data(
            filename=reference_file("image_data", "two_images.ms"))
        ms = getMicrostructure("two_images")
        ms_images = ms.imageNames()
        self.assertEqual(len(ms_images), 2)
        self.assertTrue("gray" in ms_images)
        self.assertTrue("small.png" in ms_images)
        img0 = oofimage.getImage("two_images:gray")
        img1 = oofimage.getImage("two_images:small.png")
        self.assertTrue(img0.isGray() and not img1.isGray())
        
    # Test for OOF.File.Save.Image
    @memorycheck.check("save_test")
    def Save(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","rectangle.png"),
            microstructure_name="save_test",
            height=automatic, width=automatic)
        # Save as png
        OOF.File.Save.Image(filename="image_save_test.png",
                            image="save_test:rectangle.png",
                            overwrite=False)
        self.assertTrue(
            compare_image_files(
                "image_save_test.png",
                reference_file("image_data", "saved_rectangle.png")))
        # Save as npy.  For testing, we need to ensure that the image
        # is little-endian, because the reference files are
        # little-endian.
        img = oofimage.getImage("save_test:rectangle.png")
        swapbytes = img.makeLittleEndian()
        OOF.File.Save.Image(filename="image_save_test.npy",
                            image="save_test:rectangle.png",
                            overwrite=False)
        self.assertTrue(
            compare_image_files(
                "image_save_test.npy",
                reference_file("image_data", "saved_rectangle.npy")))
        # And npz
        OOF.File.Save.Image(filename="image_save_test.npz",
                            image="save_test:rectangle.png",
                            overwrite=False)
        self.assertTrue(
            compare_image_files(
                "image_save_test.npz",
                reference_file("image_data", "saved_rectangle.npz")))
        if swapbytes:
            img.makeBigEndian()

        os.remove("image_save_test.png")
        os.remove("image_save_test.npy")
        os.remove("image_save_test.npz")

    # Test for OOF.File.Save.Image, with a grayscale image.  This
    # examines more cases than the same test for RGB images, because
    # the code for saving gray images is more complicated.  See
    # saveImage() in imagemenu.py.
    @memorycheck.check("gray")
    def SaveGray(self):
        # Load a gray scale image that is NOT restricted to 255
        # intensities.  This checks that formats that don't require 8
        # bit data aren't creating 8 bit data files.
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("image_data", "si3n4-blur.npy"),
            microstructure_name="gray",
            height=automatic, width=automatic)

        # Save in a bunch of standard image formats.  pdf, eps, and ps
        # are omitted because they might contain system dependent
        # metadata.
        for ext in ("png", "gif", "jpg", "ppm", "pgm", "tif", "tiff"):
            OOF.File.Save.Image(filename="image_save_test."+ext,
                                image="gray:si3n4-blur.npy",
                                overwrite=False)
            self.assertTrue(
                compare_image_files(
                    "image_save_test."+ext,
                    reference_file("image_data", "saved_gray."+ext)))

        # npy and npz are treated separately because they might depend
        # on endianness.
        img = oofimage.getImage("gray:si3n4-blur.npy")
        swapbytes = img.makeLittleEndian()
        for ext in ("npy", "npz"):
            OOF.File.Save.Image(filename="image_save_test."  +ext,
                                image="gray:si3n4-blur.npy",
                                overwrite=False)
            self.assertTrue(
                compare_image_files(
                    "image_save_test."+ext,
                    reference_file("image_data", "saved_gray."+ext)))
        if swapbytes:
            img.makeBigEndian()
            
        os.remove("image_save_test.gif")
        os.remove("image_save_test.jpg")
        os.remove("image_save_test.npy")
        os.remove("image_save_test.npz")
        os.remove("image_save_test.pgm")
        os.remove("image_save_test.png")
        os.remove("image_save_test.ppm")
        os.remove("image_save_test.tif")
        os.remove("image_save_test.tiff")        

    @memorycheck.check()
    def Modify(self):
        from ooflib.SWIG.common import crandom
        from ooflib.SWIG.image import oofimage
        global image_modify_args
        menuitem = OOF.Image.Modify
        for m in menuitem.items:
            try:
                test_list = image_modify_args[m.name]
            except KeyError:
                print("No test data for image modifier", m.name, file=sys.stderr)
            else:
                print(f"Testing {m.name}", file=sys.stderr)
                for (srcname, datafilename, argdict) in test_list:
                    imagename = argdict['image'] = f"imagemod_test:{srcname}"
                    OOF.Microstructure.Create_From_ImageFile(
                        filename=reference_file("image_data", srcname),
                        microstructure_name="imagemod_test",
                        height=automatic, width=automatic)
                    random.seed(17)
                    crandom.rndmseed(17)
                    m.callWithArgdict(argdict)

                    OOF.Microstructure.Create_From_ImageFile(
                        filename=reference_file("image_data", datafilename),
                        microstructure_name="comparison",
                        height=automatic, width=automatic)
                    im1 = imagecontext.imageContexts[imagename].getObject()
                    im2 = imagecontext.imageContexts[
                        "comparison:"+datafilename].getObject()
                    try:
                        self.assertTrue(im1.compare(im2, 1./65536.))
                    except:
                        # Save result for comparison.
                        ofilename = "modified_image.npz"
                        OOF.File.Save.Image(
                            filename=ofilename,
                            image=f"imagemod_test:{srcname}")
                        print(
f"""** Image comparison failed.
** Modified image saved in {os.path.join(os.getcwd(), ofilename)}
**      Reference image is {reference_file("image_data", datafilename)}""")
                        raise
                    
                    OOF.Microstructure.Delete(
                        microstructure="comparison")
                    OOF.Microstructure.Delete(
                        microstructure="imagemod_test")
                
    # Undo and Redo have the "Gray" test hard-coded.  
    @memorycheck.check("undo_test")
    def Undo(self):
        from ooflib.SWIG.image import oofimage
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("image_data","image_test.png"),
            microstructure_name="undo_test",
            height=automatic, width=automatic)
        image_context = imagecontext.imageContexts["undo_test:image_test.png"]
        im_0 = image_context.getObject()
        self.assertTrue(not oofimage.undoable("undo_test:image_test.png"))
        OOF.Image.Modify.Gray(image="undo_test:image_test.png")
        im_1 = image_context.getObject()
        self.assertNotEqual(id(im_0), id(im_1))
        self.assertTrue(oofimage.undoable("undo_test:image_test.png"))
        OOF.Image.Undo(image="undo_test:image_test.png")
        im_2 = image_context.getObject()
        self.assertNotEqual(id(im_2), id(im_1))
        self.assertEqual(id(im_0), id(im_2))

    @memorycheck.check("redo_test")
    def Redo(self):
        from ooflib.SWIG.image import oofimage
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("image_data","image_test.png"),
            microstructure_name="redo_test",
            height=automatic, width=automatic)
        image_context = imagecontext.imageContexts["redo_test:image_test.png"]
        OOF.Image.Modify.Gray(image="redo_test:image_test.png")
        im_0 = image_context.getObject()
        OOF.Image.Undo(image="redo_test:image_test.png")
        OOF.Image.Redo(image="redo_test:image_test.png")
        im_1 = image_context.getObject()
        self.assertEqual(id(im_0), id(im_1))
        
    def tearDown(self):
        pass


# Data for the image modifier tests.  This is a dictionary indexed by
# image modifier name. The values are lists of test specifications,
# which are tuples containing the name of the source image file
# (assumed to be in the TEST/image_data directory), the name of a
# reference file containing the expected test result (also in
# image_data), and a dictionary of arguments to supply to the modifier
# menu item for the test.

image_modify_args = {
    "Gray" : [
        ("image_test.png", "gray.npz", {}),
        ("gray.npz", "gray.npz", {}),
        ("grayarrow.png", "grayarrow.npz", {})],
    
    "Flip" : [("image_test.png", "flip_x.npz", {"axis" : "x"}),
              ("image_test.png", "flip_y.npz", {"axis" : "y"}),
              ("image_test.png", "flip_xy.npz", {"axis" : "xy"}),
              ("grayarrow.png", "flip_gray.npz", {"axis": "x"})],

    # The tests for Normalize use the reference files for the Fade and
    # Dim tests as a starting point. 
    "Fade" : [("image_test.png", "fade.npz", {"factor" : 0.3}),
              ("grayarrow.png", "fade_gray.npz", {"factor" : 0.5})],
    "Dim"  : [("image_test.png", "dim.npz", {"factor" : 0.7}),
              ("grayarrow.png", "dim_gray.npz", {"factor" : 0.7})],
    "Normalize" : [("fade.npz", "normalize.npz", {}),
                   ("fade_gray.npz", "normalize_gray.npz", {}),
                   ("dim.npz", "normalize.npz", {}),
                   ("dim_gray.npz", "normalize_gray.npz", {}),],
    
    # The tests for Sharpen use the reference files for Blur as a
    # starting point.
    "Blur" : [("image_test.png", "blur.npz", {"radius" : 3, "sigma" : 3}),
              ("grayarrow.png", "blur_gray.npz", {"radius" : 3, "sigma":1.5})],
    "Sharpen" : [
        ("blur.npz", "sharpen_rgb.npz",
         {"radius":3, "amount":3, "mode":'RGB'}),
        ("blur.npz", "sharpen_hsv.npz",
         {"radius":3, "amount":3, "mode":'HSV'}),
        ("blur_gray.npz", "sharpen_gray.npz",
         {"radius":3, "amount":4, "mode":'RGB'}),
        ("blur_gray.npz", "sharpen_gray.npz",
         {"radius":3, "amount":4, "mode":'HSV'}),],
    
    "Contrast" : [
        ("escher.ppm", "contrast_rgb.npz", {"radius" : 5, "mode" : "RGB"}),
        ("escher.ppm", "contrast_hsv.npz", {"radius" : 5, "mode" : "HSV"}),
        ("si3n4-small.png", "contrast_gray.npz", {"radius":5, "mode":"RGB"}),
        ("si3n4-small.png", "contrast_gray.npz", {"radius":5, "mode":"HSV"})],
    
    "Equalize" : [("escher.ppm", "equalize.npz", {}),
                  ("si3n4-small.png", "equalize_gray.npz", {})],
    
    "Negate" : [("image_test.png", "negate.npz", {}),
                ("grayarrow.png", "negate_gray.npz", {})],

    "Reilluminate" : [
        ("cb_grad.png", "reilluminate.npz", {"radius" : 5}),
        ("color_gradient_checker.png", "reilluminate_color.npz", {"radius":15})
    ],
    
    # Threshold converts images to grayscale so these tests don't use
    # any rgb images.
    "Threshold" : [
        ("cb_grad.png", "thresh_manual0.npz",
         {"method" : threshold.ManualThreshold(value=0.0)}),
        ("cb_grad.png", "thresh_manual3.npz",
         {"method" : threshold.ManualThreshold(value=0.3)}),
        ("cb_grad.png", "thresh_manual5.npz",
         {"method" : threshold.ManualThreshold(value=0.5)}),
        ("cb_grad.png", "thresh_manual7.npz",
         {"method" : threshold.ManualThreshold(value=0.7)}),
        ("cb_grad.png", "thresh_manual1.npz",
         {"method" :  threshold.ManualThreshold(value=1.0)}),
        ("cb_grad.png", "thresh_mean.npz",
         {"method" : threshold.MeanThreshold()}),
        ("cb_grad.png", "thresh_minimum.npz",
         {"method" : threshold.MinimumThreshold()}),
        ("cb_grad.png", "thresh_entropy.npz",
         {"method" : threshold.MinimumEntropyThreshold(tolerance=automatic)}),
        ("cb_grad.png", "thresh_local10_mean.npz",
         {"method" : threshold.LocalThreshold(
             radius=10,
             average=threshold.LocalMean(),
             offset=0)}),
        ("cb_grad.png", "thresh_local20_mean.npz",
         {"method" : threshold.LocalThreshold(
             radius=20,
             average=threshold.LocalMean(),
             offset=0)}),
        ("cb_grad.png", "thresh_local20_median.npz",
         {"method" :
          threshold.LocalThreshold(
             radius=20,
             average=threshold.LocalMedian(),
             offset=0)}),
        ("cb_grad.png", "thresh_local20_gaussian.npz",
         {"method" :
          threshold.LocalThreshold(
              radius=20,
              average=threshold.LocalGaussian(sigma=automatic),
              offset=0)}),
        ("cb_grad.png", "thresh_isodata.npz",
         {"method" : threshold.IsoDataThreshold()}),
        ("cb_grad.png", "thresh_otsu.npz",
         {"method" : threshold.OtsuThreshold()}),
        ("cb_grad.png", "thresh_triangle.npz",
         {"method" : threshold.TriangleThreshold(nbins=256)}),
        ("cb_grad.png", "thresh_yen.npz",
         {"method" : threshold.YenThreshold(nbins=256)}),
    ],

    "MedianFilter" : [
        ("image_test.png", "medianfilter.npz", {"radius" : 5}),
        ("image_test_noisy.png", "medianfilter2.npz", {"radius" : 5}),
        ("si3n4-small-noisy.png","medianfilter3.npz", {"radius" : 4})
    ],

    "Edge" : [
        ("image_test.png", "edge_rgb.npz", {"mode":"RGB"}),
        ("image_test.png", "edge_hsv.npz", {"mode":"HSV"}),
        ("si3n4-small.png", "edge2.npz", {"mode":"HSV"})
    ],
    
    "Denoise" : [
        ("image_test_noisy.png", "denoise_tv.npz",
         {"method" : denoise.TotalVariation(
             weight=0.1,eps=0.0002,max_iterations=200)}),
        ("si3n4-small.png", "denoise_tv2.npz",
         {"method" : denoise.TotalVariation(
             weight=0.5,eps=0.002,max_iterations=200)}),
        ("image_test_noisy.png", "denoise_nlm.npz",
         {"method" : denoise.NonlocalMeans(
             patch_size=7,patch_distance=11,h=0.1,sigma=automatic)}),
        ("si3n4-small.png", "denoise_nlm2.npz",
         {"method" : denoise.NonlocalMeans(
             patch_size=7,patch_distance=5,h=0.1,sigma=automatic)})
    ],
    
    "AddNoise":  [
        ("image_test.png", "noisy.npz", {"sigma" : 0.1, "seed" : 17}),
        ("si3n4-small.png", "noisy_gray.npz", {"sigma" : 0.1, "seed" : 137})
    ],
}   # image_modify_args

# image_modify_args = {
#     "Fade" : [ ("image_test.png", "fade.png", {"factor" : 0.3}) ],
#     }

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

test_set = [
    OOF_Image("Load"),
    OOF_Image("LoadGray"),
    OOF_Image("LoadFromMS"),
    OOF_Image("Save"),
    OOF_Image("SaveGray"),
    OOF_Image("Undo"),
    OOF_Image("Redo"),
    OOF_Image("Delete"),
    OOF_Image("Copy"),
    OOF_Image("Rename"),
    OOF_Image("AutoGroup"),
    OOF_Image("Modify")
]

# test_set = [
#     OOF_Image("SaveGray")
#     ]

    
