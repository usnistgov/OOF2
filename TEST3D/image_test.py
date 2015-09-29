# -*- python -*-
# $RCSfile: image_test.py,v $
# $Revision: 1.2 $
# $Author: vrc $
# $Date: 2007/09/26 22:03:43 $

# Test suite for the menu commands under OOF.Image.*

# These functions make use of OOF.Microstructure commands as if they
# work -- for proper regression testing, run microstructure_test first,
# then this one.

import unittest, os

class OOF_Image(unittest.TestCase):
    def setUp(self):
        pass

    # OOF.File.Load.Image loads an image into a microstructure, but
    # the usual way to get them is to create a microstructure from an
    # image file.  There's also an OOF.File.Save.Image that needs testing.
    
    def Delete(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name="slice.jpg.*",
            height=automatic, width=automatic, depth=automatic)
        OOF.Image.Delete(image="slice.jpg.*:slice.jpg.*")
        ms = getMicrostructure("slice.jpg.*")
        self.assertEqual(len(ms.imageNames()),0)
        self.assertEqual(len(ms.getImageContexts()), 0)
        OOF.Microstructure.Delete(microstructure="slice.jpg.*")
        
    def Copy(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name="slice.jpg.*",
            height=automatic, width=automatic, depth=automatic)
        OOF.Microstructure.New(name="other", width=100.0,
                               height=100.0, depth=100.0,
                               width_in_pixels=100,
                               height_in_pixels=100,
                               depth_in_pixels=100)
        OOF.Image.Copy(image="slice.jpg.*:slice.jpg.*",
                       microstructure="other", name=automatic)
        ms_0 = getMicrostructure("slice.jpg.*")
        ms_1 = getMicrostructure("other")
        self.assertEqual(len(ms_1.imageNames()),1)
        self.assert_("slice.jpg.*" in ms_1.imageNames())
        # Ensure they're separate objects.
        self.assertNotEqual(id(ms_0.getImageContexts()[0]), id(ms_1.getImageContexts()[0]))
        OOF.Microstructure.Delete(microstructure="slice.jpg.*")
        OOF.Microstructure.Delete(microstructure="other")

    def Rename(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name="slice.jpg.*",
            height=automatic, width=automatic, depth=automatic)
        ms_0 = getMicrostructure("slice.jpg.*")
        image_id = id(ms_0.getImageContexts()[0])
        OOF.Image.Rename(image="slice.jpg.*:slice.jpg.*",
                         name="newname")
        ms_0 = getMicrostructure("slice.jpg.*")
        image_id = id(ms_0.getImageContexts()[0])
        self.assertEqual(len(ms_0.imageNames()),1)
        self.assert_("newname" in ms_0.imageNames())
        self.assertEqual(image_id, id(ms_0.getImageContexts()[0]))
        OOF.Microstructure.Delete(microstructure="slice.jpg.*")

    # This test just checks that the groups are created and add up to
    # the right size.  Group operations are tested in more detail
    # elsewhere.
    def AutoGroup(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","5color","slice*.tif"),
            microstructure_name="slice*.tif",
            height=automatic, width=automatic, depth=automatic)
        OOF.Image.AutoGroup(image="slice*.tif:slice*.tif")
        ms = getMicrostructure("slice*.tif")
        self.assertEqual(ms.nGroups(), 5)
        self.assertEqual(ms.nCategories(), 5)
        # Check that the groups add up to the total size.
        size = 0
        for gname in ms.groupNames():
            size += len(ms.findGroup(gname))
        self.assertEqual(size, 20*20*20)
        OOF.Microstructure.Delete(microstructure="slice*.tif")

    # Test for OOF.File.Image.Save, which is technically not in the
    # OOF.Image menu hierarchy.
    def Save(self):
        import filecmp, os
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","5color","slice*.tif"),
            microstructure_name="save_test",
            height=automatic, width=automatic, depth=automatic)
        OOF.File.Save.Image(filename="image_save_test_%i",
                            image="save_test:slice*.tif")
##         OOF.File.Save.Image(filename=os.path.join("image_data",
##                                                   "saved_image_%i"),
##                             image="save_test:slice*.tif")
        for i in xrange(20):
            self.assert_(filecmp.cmp("image_save_test_"+str(i),
                                     os.path.join("image_data",
                                                  "saved_image_"+str(i))))
            os.remove("image_save_test_"+str(i))
        OOF.Microstructure.Delete(microstructure="save_test")

    # Test for OOF.File.Image.Load, which is technically not in the
    # OOF.Image menu hierarchy.
    def Load(self):
        OOF.Microstructure.New(name="load_test", width=100,
                               height=100, depth=100,
                               width_in_pixels=100,
                               height_in_pixels=100,
                               depth_in_pixels=100)
        OOF.File.Load.Image(filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
                            microstructure="load_test",
                            height=automatic, width=automatic, depth=automatic)
        ms = getMicrostructure("load_test")
        ms_images = ms.imageNames()
        self.assertEqual(len(ms_images),1)
        self.assert_("slice.jpg.*" in ms_images)
        OOF.Microstructure.Delete(microstructure="load_test")
                            
        
    def Modify(self):
        import filecmp, os, random
        from ooflib.SWIG.common import crandom
        from ooflib.image import oofimage3d
        global image_modify_args
        menuitem = OOF.Image.Modify
        for m in menuitem.items:
            try:
                test_list = image_modify_args[m.name]
            except KeyError:
                print "No test data for image modifier ", m.name
            else:
                for (datafilename, argdict) in test_list:
                    argdict['image']="imagemod_test:slice*.tif"
                    OOF.Microstructure.Create_From_ImageFile(
                        filename=os.path.join("ms_data","5color","slice*.tif"),
                        microstructure_name="imagemod_test",
                        height=automatic, width=automatic, depth=automatic)
                    random.seed(17)
                    crandom.rndmseed(17)
                    m.callWithArgdict(argdict)

##                     OOF.File.Save.Image(
##                         filename=os.path.join("image_data", datafilename[:-1]+"%i"),
##                         image="imagemod_test:slice*.tif")

                    OOF.Microstructure.Create_From_ImageFile(
                        filename=os.path.join("image_data", datafilename),
                        microstructure_name="comparison",
                        height=automatic, width=automatic, depth=automatic)
                    im1 = oofimage3d.imageContexts[
                        "imagemod_test:slice*.tif"].getObject()
                    im2 = oofimage3d.imageContexts[
                        "comparison:"+datafilename].getObject()
                    # Tolerance is 1./65535., which is the level of
                    # "quantization noise" for 16-bit color channels.
                    self.assert_(im1.compare(im2, 1./65535.))
                    
                    OOF.Microstructure.Delete(
                        microstructure="comparison")
                    OOF.Microstructure.Delete(
                        microstructure="imagemod_test")
                
    # Undo and Redo have the "Gray" test hard-coded.  They'd be a tad
    # more flexible if they just used the first test in the list.

    def Undo(self):
        from ooflib.image import oofimage3d
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name="undo_test",
            height=automatic, width=automatic, depth=automatic)
        image_context = oofimage3d.imageContexts["undo_test:slice.jpg.*"]
        im_0 = image_context.getObject()
        self.assert_(not oofimage3d.undoable("undo_test:slice.jpg.*"))
        OOF.Image.Modify.Gray(image="undo_test:slice.jpg.*")
        im_1 = image_context.getObject()
        self.assertNotEqual(id(im_0), id(im_1))
        self.assert_(oofimage3d.undoable("undo_test:slice.jpg.*"))
        OOF.Image.Undo(image="undo_test:slice.jpg.*")
        im_2 = image_context.getObject()
        self.assertNotEqual(id(im_2), id(im_1))
        self.assertEqual(id(im_0), id(im_2))
        OOF.Microstructure.Delete(microstructure="undo_test")
                     
    def Redo(self):
        from ooflib.image import oofimage3d
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name="redo_test",
            height=automatic, width=automatic, depth=automatic)
        image_context = oofimage3d.imageContexts["redo_test:slice.jpg.*"]
        OOF.Image.Modify.Gray(image="redo_test:slice.jpg.*")
        im_0 = image_context.getObject()
        OOF.Image.Undo(image="redo_test:slice.jpg.*")
        OOF.Image.Redo(image="redo_test:slice.jpg.*")
        im_1 = image_context.getObject()
        self.assertEqual(id(im_0), id(im_1))
        OOF.Microstructure.Delete(microstructure="redo_test")
        
    def tearDown(self):
        pass


# Data for the image modifier tests.  This is a dictionary indexed by
# image modifier name, and for each modifier, there is a set of
# arguments to supply to the modifier menu item for the test, and the
# name of a file containing correct results for that test.


image_modify_args = {"Gray" : [ ("gray*", {}) ],
                     "Flip" : [ ("flip_x*", {"axis" : "x"}),
                                ("flip_y*", {"axis" : "y"}),
                                ("flip_xy*", {"axis" : "xy"}),
                                ("flip_yz*", {"axis" : "yz"}),
                                ("flip_xz*", {"axis" : "xz"}),
                                ("flip_xyz*", {"axis" : "xyz"})],
                     "Fade" : [ ("fade*", {"factor" : 0.3}) ],
                     "Dim"  : [ ("dim*", {"factor" : 0.7}) ],
                     "Blur" : [ ("blur*", {"radius" : 1.0,
                                          "sigma" : 3.0} ) ],
                     # Contrast ? 
                     # "Despeckle" : [ ("despeckle", {})],
                     # "Edge" : [ ("edge", {"radius" : 0.0})],
                     # "Enhance" : [ ("enhance", {})],
                     # "Equalize" : [ ("equalize", {})],
                     "MedianFilter" : [ ("median*",
                                         {"radius" : 1}) ],
                     "Negate" : [("negate*", {})],
                     "Normalize" : [("normalize*", {})],
                     # "ReduceNoise" : [("reduce_noise",
                     #                   {"radius" : 1.0})],
                     # "Sharpen" : [("sharpen", {"radius" : 1.0,
                     #                           "sigma" : 3.0})],
##                      "Reilluminate" : [("reilluminate", {"radius" : 10})],
                     "ThresholdImage" : [("threshold*", {"T" : 0.5})],


## METHODS NOT PART OF REGULAR IMAGE.MODIFY MENU
##                      "Add_Gaussian_Noise" : [("add_gaussian_noise",
##                                               {"Standard_deviation" : 0.2})],
##                      "Canny" : [("canny", {"stdDev" : 1.0})],
##                      "GaussianSmoothing" : [("gaussiansmoothing",
##                                              {"stdDev" : 1.0})],
##                      "LaplacianFilter" : [("laplacianfilter", {})],
##                      "LaplacianGaussFilter" : [("laplaciangaussfilter",
##                                                 {"stdDev" : 1.0})],
##                      "Sobel" : [("sobel", {})],
##                      "SpreadDataValues" : [("spreaddatavalues", {"T" : 0.3})],
##                      "SpreadDataValues2" : [("spreaddatavalues2",
##                                              {"T" : 0.3})]
##                      "Add_Gaussian_Noise" : [("add_gaussian_noise",
##                                               {"Standard_deviation" : 0.2})],
##                      "Canny" : [("canny", {"stdDev" : 1.0})],
##                      "GaussianSmoothing" : [("gaussiansmoothing",
##                                              {"stdDev" : 1.0})],
##                      "LaplacianFilter" : [("laplacianfilter", {})],
##                      "LaplacianGaussFilter" : [("laplaciangaussfilter",
##                                                 {"stdDev" : 1.0})],
##                      "Sobel" : [("sobel", {})],
##                      "SpreadDataValues" : [("spreaddatavalues", {"T" : 0.3})],
##                      "SpreadDataValues2" : [("spreaddatavalues2",
##                                              {"T" : 0.3})]
                     }

# Routine to do regression-type testing on the items in this file.
# Tests must be run in the order they appear in the list.  This
# routine will stop after the first failure.
def run_tests():
    test_set =  [OOF_Image("Undo"),
                OOF_Image("Redo"),
                OOF_Image("Delete"),
                OOF_Image("Copy"),
                OOF_Image("Rename"),
                OOF_Image("Save"),
                OOF_Image("Load"),
                OOF_Image("AutoGroup"),
                OOF_Image("Modify")
                ]



    logan = unittest.TextTestRunner()
    for t in test_set:
        print "\n *** Running test: %s\n" % t.id()
        res = logan.run(t)
        if not res.wasSuccessful():
            return 0
    return 1


###################################################################
# The code below this line should be common to all testing files. #
###################################################################

if __name__=="__main__":
    # If directly run, then start oof, and run the local tests, then quit.
    import sys
    try:
        import oof3d
        sys.path.append(os.path.dirname(oof3d.__file__))
        from ooflib.common import oof
    except ImportError:
        print "OOF is not correctly installed on this system."
        sys.exit(4)
    sys.argv.append("--text")
    sys.argv.append("--quiet")
    sys.argv.append("--seed=17")
    oof.run(no_interp=1)
    
    success = run_tests()

    OOF.File.Quit()
    
    if success:
        print "All tests passed."
    else:
        print "Test failure."
