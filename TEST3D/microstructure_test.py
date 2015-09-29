# -*- python -*-
# $RCSfile: microstructure_test.py,v $
# $Revision: 1.2 $
# $Author: vrc $
# $Date: 2007/09/26 22:03:43 $

# Test suite for the menu commands under OOF.Microstructure.*

import unittest, os, filecmp

class OOF_Microstructure(unittest.TestCase):
    def setUp(self):
        global microstructure
        global ooferror
        from ooflib.common import microstructure
        from ooflib.SWIG.common import ooferror

    def New(self):
        from ooflib.common import primitives
        self.assertRaises(ooferror.ErrUserError,
                          OOF.Microstructure.New,
                          name="one", width=-1.0, height=-1.0,
                          width_in_pixels=10,
                          height_in_pixels=10)
        OOF.Microstructure.New(name="one", width=4.0, height=5.0, depth=6.0,
                               width_in_pixels=120, height_in_pixels=100, depth_in_pixels=120)
        ms = getMicrostructure("one")
        self.assertEqual(ms.name(), "one")
        labeltree_count=microstructure.microStructures.members.__len__()
        ms_and_proxies=microstructure.microStructures.nmembers
        # There should be one proxy in the tree.
        self.assertEqual(ms_and_proxies,3)
        # The labeltree object's len function counts the root and the proxy.
        self.assertEqual(labeltree_count,4)
        ms_count=microstructure.microStructures.nActual()
        # There should be only one non-proxy object.
        self.assertEqual(ms_count,1)
        self.assertEqual(ms.size(), primitives.Point(4.0,5.0,6.0))
        self.assertEqual(ms.sizeOfPixels(), (4.0/120, 5.0/100, 6.0/120))

    # "Delete" should be run only after "New" has succeeded.  Assumes
    # exactly one microstructure, named "one", has already been created.
    def Delete(self):
        ms_count=microstructure.microStructures.nActual()
        self.assertEqual(ms_count,1)
        self.assertRaises(KeyError,
                          OOF.Microstructure.Delete, microstructure="two")
        ms_count=microstructure.microStructures.nActual()
        self.assertEqual(ms_count,1)
        OOF.Microstructure.Delete(microstructure="one")
        labeltree_count=microstructure.microStructures.members.__len__()
        ms_and_proxies=microstructure.microStructures.nmembers
        # There should only be the proxy left.
        self.assertEqual(ms_and_proxies,2)
        # The labeltree object's len function counts the root and the proxy.
        self.assertEqual(labeltree_count,3)
        ms_count=microstructure.microStructures.nActual()
        # There should be only one non-proxy object.
        self.assertEqual(ms_count,0)

    # Creates a microstructure from the "small.ppm" file, which must
    # be in the ms_data directory below this script.
    def Create_From_ImageFile(self):
        from ooflib.image import oofimage3d
        from ooflib.common import primitives
        from ooflib.SWIG.common.IO import stringimage
        self.assertRaises(
            ooferror.ErrUserError, 
            OOF.Microstructure.Create_From_ImageFile,
            filename="nosuchfile", microstructure_name="nosuchfile",
            height=automatic, width=automatic, depth=automatic)
        self.assertRaises(
            ooferror.ErrUserError,
            OOF.Microstructure.Create_From_ImageFile,
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name="oops",
            height=-1.0, width=-1.0, depth=-1.0)
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name="slice.jpg.*",
            height=20.0, width=20.0, depth=20.0)
        ms = getMicrostructure("slice.jpg.*")
        self.assertEqual(ms.size(), primitives.Point(20.0, 20.0, 20.0))
        self.assertEqual(ms.sizeInPixels(), primitives.iPoint(100,100,100))
        self.assertEqual(ms.sizeOfPixels(), (20.0/100, 20.0/100, 20.0/100))
        ms_images = ms.imageNames()
        self.assertEqual(len(ms_images), 1)
        self.assert_("slice.jpg.*" in ms_images)
        img = oofimage3d.getImage("slice.jpg.*:slice.jpg.*")
##        strimg = stringimage.StringImage(ms.sizeInPixels(), ms.size())
##         img.fillstringimage(strimg)
##         outfile = file('hexstringimage.dat','w')
##         print >> outfile, strimg.hexstringimage()
##         outfile.close()
##         assert filecmp.cmp('hexstringimage.dat',
##                            os.path.join('ms_data','smallppm.hex'))
##         os.remove("hexstringimage.dat")
        OOF.Microstructure.Delete(microstructure="slice.jpg.*")


    # Assumes no microstructures are present.  Requires "New" and "Delete".
    def Create_From_Image(self):
        from ooflib.common import primitives
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name=automatic,
            height=20.0, width=20.0, depth=20.0)
        OOF.Microstructure.Create_From_Image(
            name="new", width=automatic, height=automatic,
            image="slice.jpg.*:slice.jpg.*")
        ms_0 = getMicrostructure("slice.jpg.*")
        ms_1 = getMicrostructure("new")
        # Ensure images are separate objects.
        ms_1_image_id = id(ms_1.getImageContexts()[0])
        # Make sure the image wasn't copied in the source microstructure.
        self.assertEqual(len(ms_0.imageNames()), 1)
        # Make sure the newly constructed microstructure is the right size.
        self.assertEqual(ms_1.sizeInPixels(), primitives.iPoint(100,100,100))
        self.assertEqual(ms_1.size(), primitives.Point(20.0, 20.0, 20.0))
        self.assertEqual(ms_1.sizeOfPixels(), (20.0/100, 20.0/100, 20.0/100))
        OOF.Microstructure.Delete(microstructure="slice.jpg.*")
        # Ensure that after the originating microstructure has been
        # deleted, the derived one still has the same image.
        self.assert_("slice.jpg.*" in ms_1.imageNames())
        self.assertEqual(ms_1_image_id, id(ms_1.getImageContexts()[0]))
        OOF.Microstructure.Delete(microstructure="new")

    # Should be run after "New" and "Delete" are known to work.
    def Copy(self):
        start_ms_count = microstructure.microStructures.nActual()
        OOF.Microstructure.New(name="three", width=2.5, height=3.5, depth=4.5,
                               width_in_pixels=10, height_in_pixels=10,
                               depth_in_pixels=10)
        # Tests automatic name uniquification.
        OOF.Microstructure.Copy(microstructure="three", name="three")
        OOF.Microstructure.Copy(microstructure="three", name="four")
        ms_count = microstructure.microStructures.nActual()
        self.assertEqual(ms_count, start_ms_count + 3)
        name_list = microstructure.microStructures.keys()
        self.assert_(['three<2>'] in name_list)
        self.assert_(['four'] in name_list)
        OOF.Microstructure.Delete(microstructure="three<2>")
        ms_0 = getMicrostructure("three")
        ms_1 = getMicrostructure("four")
        self.assertEqual(ms_0.sizeInPixels(), ms_1.sizeInPixels())
        self.assertEqual(ms_0.areaOfPixels(), ms_1.areaOfPixels())
        self.assertEqual(ms_0.size(), ms_1.size())
        OOF.Microstructure.Delete(microstructure="three")
        OOF.Microstructure.Delete(microstructure="four")

    # Uses New, does not make assumptions about existing microstructures.
    def Rename(self):
        OOF.Microstructure.New(name="rename", width=2.5, height=3.5, depth=4.5,
                               width_in_pixels=10, height_in_pixels=10,
                               depth_in_pixels=10)
        ms_count = microstructure.microStructures.nActual()
        ms_0 = getMicrostructure("rename")
        OOF.Microstructure.Rename(microstructure="rename", name="newname")
        ms_1 = getMicrostructure("newname")
        self.assertEqual(id(ms_0),id(ms_1))
        new_ms_count = microstructure.microStructures.nActual()
        self.assertEqual(ms_count, new_ms_count)
        OOF.Microstructure.Delete(microstructure="newname")


    # Also test basic load and save.  This is currently only for the
    # MS itself -- as with "Copy", later versions should also test for
    # correct propagation of MS contents, like pixel groups.
    def Save(self):
        import filecmp, os
        OOF.Microstructure.New(name="save_test", width=2.5, height=3.5, depth=4.5,
                               width_in_pixels=10, height_in_pixels=10,
                               depth_in_pixels=10)
        OOF.File.Save.Microstructure(filename="ms_save_test",
                                     mode="w",
                                     format="ascii",
                                     microstructure="save_test")
        self.assert_(filecmp.cmp("ms_save_test",
                                 os.path.join("ms_data","saved_ms")))
        OOF.Microstructure.Delete(microstructure="save_test")
        os.remove("ms_save_test")

        
    def Load(self):
        from ooflib.common import primitives
        # The MS in this file is named "load_test", and is the same
        # as the "save_test" one, except for the name.
        OOF.File.Load.Data(filename=os.path.join("ms_data","saved_ms"))
        ms_0 = getMicrostructure("save_test")
        self.assertEqual(ms_0.sizeInPixels(), primitives.iPoint(10,10,10))
        self.assertEqual(ms_0.size(), primitives.Point(2.5, 3.5, 4.5))
        self.assertEqual(ms_0.sizeOfPixels(), (2.5/10, 3.5/10, 4.5/10))
        OOF.Microstructure.Delete(microstructure="save_test")


    def tearDown(self):
        pass


# Routine to do regression-type testing on the items in this file.
# Tests must be run in the order they appear in the list.  This
# routine will stop after the first failure.
def run_tests():
    test_set = [
        OOF_Microstructure("New"),
        OOF_Microstructure("Delete"),
        OOF_Microstructure("Create_From_ImageFile"),
        OOF_Microstructure("Create_From_Image"),
        OOF_Microstructure("Copy"),
        OOF_Microstructure("Rename"),
        OOF_Microstructure("Save"),
        OOF_Microstructure("Load")
        ]

    logan = unittest.TextTestRunner()
    print "running tests"
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
