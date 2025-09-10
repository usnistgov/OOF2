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

import unittest, os
from . import memorycheck

from ooflib.SWIG.image import oofimage
from ooflib.common.IO.automatic import automatic

from ooflib.image import threshold

from .UTILS.file_utils import reference_file

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Compare two image files. It's not possible to use filecmp.cmp
# because if the image format includes metadata, the files might
# differ even if the pixel data is identical.  Use skimage utilities
# instead.

import numpy
import skimage
from matplotlib import pyplot

def compare_image_files(imagefile0, imagefile1):
    image0 = pyplot.imread(imagefile0)
    image1 = pyplot.imread(imagefile1)
    if image0.shape != image1.shape:
        print(f"Image shapes don't agree: {image0.shape} {image1.shape}")
        return False
    compimg = skimage.util.compare_images(image0, image1, method="diff")
    diffnorm = numpy.linalg.norm(compimg)
    diffmax = compimg.max()
    if diffnorm > 0 or diffmax > 0:
        print(f"Image difference is nonzero: norm={norm} max={max}")
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

    # Test for OOF.File.Image.Save, which is technically not in the
    # OOF.Image menu hierarchy.
    @memorycheck.check("save_test")
    def Save(self):
        import filecmp, os
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
            filecmp.cmp("image_save_test.npy",
                        reference_file("image_data", "saved_rectangle.npy")))
        # And npz
        OOF.File.Save.Image(filename="image_save_test.npz",
                            image="save_test:rectangle.png",
                            overwrite=False)
        self.assertTrue(
            filecmp.cmp("image_save_test.npz",
                        reference_file("image_data", "saved_rectangle.npz")))
        if swapbytes:
            img.makeBigEndian()
        os.remove("image_save_test.png")
        os.remove("image_save_test.npy")
        os.remove("image_save_test.npz")

    # Test for OOF.File.Image.Load, which is technically not in the
    # OOF.Image menu hierarchy.
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
        
    @memorycheck.check()
    def Modify(self):
        import filecmp, os, random
        from ooflib.SWIG.common import crandom
        from ooflib.SWIG.image import oofimage
        global image_modify_args
        menuitem = OOF.Image.Modify
        for m in menuitem.items:
            try:
                test_list = image_modify_args[m.name]
            except KeyError:
                print("No test data for image modifier ", m.name, file=sys.stderr)
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
                        # Tolerance is 1./256., which is the level of
                        # "quantization noise" for 8-bit color
                        # channels.  It seems that images are being
                        # converted to 8-bit when saved, and so tests
                        # can fail if the tolerance is lower than
                        # that.
                        ## TODO: Change format of reference files to
                        ## .npz, which doesn't have this problem.
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
# (assumed to be in the image_data directory), the name of a reference
# file containing the expected test result (also in image_data), and a
# dictionary of arguments to supply to the modifier menu item for the
# test.

# Commented-out entries in this list are modifications provided
# directly by ImageMagick.  These have proven to have some variability
# between different versions of the ImageMagick library, and so cannot
# be reliably tested here.  They're kept in and commented out so we'll
# know we didn't just forget. 

## TODO: Remove reference files for archived code, such as the Gabor
## modifier tests.

image_modify_args = {
    "Gray" : [ ("image_test.png", "gray.npz", {}) ],
    "Flip" : [ ("image_test.png", "flip_x.npz", {"axis" : "x"}),
               ("image_test.png", "flip_y.npz", {"axis" : "y"}),
               ("image_test.png", "flip_xy.npz", {"axis" : "xy"})],
    "Fade" : [ ("image_test.png", "fade.npz", {"factor" : 0.3}) ],
    "Dim"  : [ ("image_test.png", "dim.npz", {"factor" : 0.7}) ],
    "Blur" : [ ("image_test.png", "blur.npz", {"radius" : 3.0, "sigma" : 3.0})],
    "Contrast" : [ ("escher.ppm", "contrast.npz", {"radius" : 5.0 }) ],

                     # "Despeckle" : [ ("despeckle", {})],
                     # "Edge" : [ ("edge", {"radius" : 0.0})],
                     # "Enhance" : [ ("enhance", {})],
                     # "Equalize" : [ ("equalize", {})],
                     # "MedianFilter" : [ ("median",
                     #                     {"radius" : 1.0}) ],
                     # "Negate" : [("negate", {})],
                     # "Normalize" : [("normalize", {})],
                     # "ReduceNoise" : [("reduce_noise",
                     #                   {"radius" : 1.0})],
                     # "Sharpen" : [("sharpen", {"radius" : 1.0,
                     #                           "sigma" : 3.0})],
    "Reilluminate" : [("cb_grad.png",
                       "reilluminate.npz", {"radius" : 5})],

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
             average=threshold.LocalMean())}),
        ("cb_grad.png", "thresh_local20_mean.npz",
         {"method" : threshold.LocalThreshold(
             radius=20,
             average=threshold.LocalMean())}),
        ("cb_grad.png", "thresh_local20_median.npz",
         {"method" :
          threshold.LocalThreshold(
             radius=20,
             average=threshold.LocalMedian())}),
        ("cb_grad.png", "thresh_local20_gaussian.npz",
         {"method" :
          threshold.LocalThreshold(
              radius=20,
              average=threshold.LocalGaussian(sigma=automatic))}),
        ("cb_grad.png", "thresh_isodata.npz",
         {"method" : threshold.IsoDataThreshold()}),
        ("cb_grad.png", "thresh_otsu.npz",
         {"method" : threshold.OtsuThreshold()}),
        ("cb_grad.png", "thresh_triangle.npz",
         {"method" : threshold.TriangleThreshold(nbins=256)}),
        ("cb_grad.png", "thresh_yen.npz",
         {"method" : threshold.YenThreshold(nbins=256)}),
        
        
    ],

                     "CloseImage" : [("closeimage.png", {"n" : 7})],
                     "Connect_Edges" : [("connect_edges.png",
                                         {"Threshold" : 0.5,
                                          "d" : 7,
                                          "n" : 9,
                                          "B" : 5,
                                          "trimYN" : 0,
                                          "t" : 0.5})],
                     "SkeletonizeImage" : [("skeletonize.png", {})],
                     "FullEdgeDetection" : [("fulledgedetection.png",
                                             {"a": 3,
                                              "b": 3,
                                              "numAngles" : 6,
                                              "Threshold" : 0.5,
                                              "Line_color" : 2,
                                              "d" : 7,
                                              "n" : 9,
                                              "B" : 5,
                                              "trimYN" : 0,
                                              "t" : 0.5})],
                     "HysteresisThreshold" : [("hysteresisthreshold.png",
                                               {"T1" : 0.5, "T2" : 0.5})],
                     "ImaginaryGabor" : [("imaginarygabor.png",
                                          {"a" : 3, "b" : 3,
                                           "numAngles" : 6,
                                           "Threshold" : 0.5} )],
                     "ModifiedGabor" : [("modifiedgabor.png",
                                         {"a" : 3, "b" : 3,
                                          "numAngles" : 6,
                                          "Threshold" : 0.5} )],
                     "NewGabor" : [("newgabor.png",
                                    {"a" : 3, "b" : 3,
                                     "numAngles" : 4,
                                     "Threshold" : 0.5,
                                     "Line_color" : 2 } )],
                     "NormalGabor" : [("normalgabor.png",
                                       {"a" : 3, "b" : 3,
                                        "numAngles" : 6,
                                        "Threshold" : 0.5} )],
                     "RealGabor" : [("realgabor.png",
                                     {"a" : 3, "b" : 3,
                                      "numAngles" : 6,
                                      "Threshold" : 0.5} )],
                     "Add_Gaussian_Noise" : [("add_gaussian_noise.png",
                                              {"Standard_deviation" : 0.2})],
                     "Canny" : [("canny.png", {"stdDev" : 1.0})],
                     "GaussianSmoothing" : [("gaussiansmoothing.png",
                                             {"stdDev" : 1.0})],
                     "LaplacianFilter" : [("laplacianfilter.png", {})],
                     "LaplacianGaussFilter" : [("laplaciangaussfilter.png",
                                                {"stdDev" : 1.0})],
                     "Sobel" : [("sobel.png", {})],
                     "SpreadDataValues" : [("spreaddatavalues.png",
                                            {"T" : 0.3})],
                     "SpreadDataValues2" : [("spreaddatavalues2.png",
                                             {"T" : 0.3})]
                     }

# image_modify_args = {
#     "Fade" : [ ("image_test.png", "fade.png", {"factor" : 0.3}) ],
#     }

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

test_set = [
    OOF_Image("Save"),
    OOF_Image("Load"),
    OOF_Image("Undo"),
    OOF_Image("Redo"),
    OOF_Image("Delete"),
    OOF_Image("Copy"),
    OOF_Image("Rename"),
    OOF_Image("AutoGroup"),
    OOF_Image("Modify")
]

