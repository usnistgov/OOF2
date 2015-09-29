# -*- python -*-
# $RCSfile: skeleton_extra_test.py,v $
# $Revision: 1.27 $
# $Author: langer $
# $Date: 2013/10/21 15:11:58 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Test suite for skeleton menu command combinations which depend on
# the individual commands working.  These include a test of at least
# one skeleton modifier with pinned nodes, saving and loading of a
# skeleton with selections, groups, and boundaries, and tests of the
# commutativity of skeleton modification and selection changes.

# These tests are "extra" in the sense that they re-run menu items
# which have already been run, but they do so under more challenging
# circumstances than the initial test.

import unittest, os
import memorycheck
import UTILS.file_utils
reference_file = UTILS.file_utils.reference_file
fp_file_compare = UTILS.file_utils.fp_file_compare
UTILS.file_utils.generate = False

class OOF_Skeleton_Extra(unittest.TestCase):
    def setUp(self):
        global gfxmanager
        from ooflib.common.IO import gfxmanager
        global skeletoncontext
        from ooflib.engine import skeletoncontext
        global microstructure
        from ooflib.common import microstructure
        global cmicrostructure
        from ooflib.SWIG.common import cmicrostructure
        global cskeleton
        from ooflib.SWIG.engine import cskeleton
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","small.ppm"),
            microstructure_name="skeltest",
            height=20.0, width=20.0)
        OOF.Image.AutoGroup(image="skeltest:small.ppm")
        OOF.Skeleton.New(
            name="skelextra",
            microstructure="skeltest", 
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(left_right_periodicity=False,
                                           top_bottom_periodicity=False))
        OOF.Windows.Graphics.New()
        self.sk_context = skeletoncontext.skeletonContexts[
            "skeltest:skelextra"]
        self.e_selection = self.sk_context.elementselection
        self.s_selection = self.sk_context.segmentselection
        self.n_selection = self.sk_context.nodeselection
        #
        self.e_groups = self.sk_context.elementgroups
        self.s_groups = self.sk_context.segmentgroups
        self.n_groups = self.sk_context.nodegroups

    def tearDown(self):
        OOF.Graphics_1.File.Close()


    # Run a modifier with pinned nodes.
    @memorycheck.check("skeltest", "skelcomp")
    def PinnedModify(self):
        import os, random
        from ooflib.SWIG.common import crandom
        OOF.Graphics_1.Toolbox.Select_Node.Rectangle(
            skeleton="skeltest:skelextra",
            points=[Point(9.75,7.25), Point(10.25,12.75)],
            ctrl=0, shift=0)
        OOF.Skeleton.PinNodes.Pin_Node_Selection(
            skeleton="skeltest:skelextra")

        random.seed(17)
        crandom.rndmseed(17)
        OOF.Skeleton.Modify(
            skeleton="skeltest:skelextra",
            modifier=SnapNodes(targets=SnapAll(),
                               criterion=AverageEnergy(alpha=0.75)))
        OOF.File.Save.Skeleton(filename="skeleton_pinned_test",
                               mode="w", format="ascii",
                               skeleton="skeltest:skelextra")
        OOF.Skeleton.Delete(skeleton="skeltest:skelextra")
        OOF.File.Load.Data(filename="skeleton_pinned_test")
        OOF.File.Load.Data(filename=reference_file("skeleton_data",
                                                   "snapnodes_pinned"))
        sk1 = skeletoncontext.skeletonContexts[
            "skeltest:skelextra"].getObject()
        sk2 = skeletoncontext.skeletonContexts[
            "skelcomp:skelextra"].getObject()
        self.assertEqual(sk1.compare(sk2, 1.0e-13), 0)
        os.remove("skeleton_pinned_test")
        OOF.Skeleton.Delete(skeleton="skeltest:skelextra")

    # Save with nontrivial groups and pinned nodes.  Since no node
    # movement occurs, and selections are made unambiguously, direct
    # file comparison should still be OK.
    def enrich_skeleton(self):
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton="skeltest:skelextra", points=[Point(3.33, 4.95)],
            shift=0, ctrl=0)
        OOF.ElementGroup.New_Group(skeleton="skeltest:skelextra",
                                   name="eg")
        OOF.ElementGroup.Add_to_Group(skeleton="skeltest:skelextra",
                                      group="eg")

        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='skeltest:skelextra', points=[Point(1.37,3.25)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='skeltest:skelextra', points=[Point(1.38,1.46)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='skeltest:skelextra', points=[Point(4.18,1.29)],
            shift=1, ctrl=0)
        OOF.ElementGroup.New_Group(skeleton="skeltest:skelextra", name="ag")
        OOF.ElementGroup.Add_to_Group(skeleton="skeltest:skelextra",
                                      group="ag")
        OOF.Material.New(name='material', material_type='bulk')
        OOF.Material.New(name='material<2>', material_type='bulk')
        OOF.ElementGroup.Assign_Material(skeleton='skeltest:skelextra',
                                         group='eg', material='material')
        OOF.ElementGroup.Assign_Material(skeleton='skeltest:skelextra',
                                         group='ag', material='material<2>')

        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton="skeltest:skelextra", points=[Point(3.33, 4.95)],
            shift=0, ctrl=0)
        OOF.SegmentGroup.New_Group(skeleton="skeltest:skelextra",
                                   name="sg")
        OOF.SegmentGroup.Add_to_Group(skeleton="skeltest:skelextra",
                                      group="sg")

        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton="skeltest:skelextra", points=[Point(3.33, 4.95)],
            shift=0, ctrl=0)
        OOF.NodeGroup.New_Group(skeleton="skeltest:skelextra",
                                name="ng")
        OOF.NodeGroup.Add_to_Group(skeleton="skeltest:skelextra",
                                   group="ng")
        
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton="skeltest:skelextra", point=Point(3.33, 7.45))

    @memorycheck.check("skelcomp")
    def RichSave(self):
        self.enrich_skeleton()
        OOF.Microstructure.Rename(microstructure="skeltest",
                                  name="skelcomp")
        OOF.File.Save.Skeleton(filename="skeleton_rich_save",
                               mode="w", format="ascii",
                               skeleton="skelcomp:skelextra")
        self.assert_(fp_file_compare(
                'skeleton_rich_save',
                os.path.join('skeleton_data', 'rich_skeleton'),
                1.e-10))
        # Check abaqus output too.
        OOF.File.Save.Skeleton(filename="skeleton_abaqus_save",
                               mode="w", format="abaqus",
                               skeleton="skelcomp:skelextra")
        self.assert_(fp_file_compare(
            "skeleton_abaqus_save",
            os.path.join("skeleton_data", "abaqus_skeleton"),
            tolerance=1.e-10, ignoretime=True))
        OOF.Material.Delete(name="material")
        OOF.Material.Delete(name="material<2>")
        os.remove("skeleton_rich_save")
        os.remove("skeleton_abaqus_save")
        
    @memorycheck.check("skeltest", "skelcomp")
    def RichLoad(self):
        self.enrich_skeleton()
        OOF.File.Load.Data(filename=reference_file("skeleton_data",
                                                   "rich_skeleton"))
        from ooflib.engine import skeletoncontext
        skc1 = skeletoncontext.skeletonContexts["skeltest:skelextra"]
        skc2 = skeletoncontext.skeletonContexts["skelcomp:skelextra"]
        self.assertEqual(skc1.compare_groups(skc2), 0)
        OOF.Material.Delete(name="material")
        OOF.Material.Delete(name="material<2>")
        

    # Test commutativity of selection undo/redo operations and
    # modification undo/redo.  Just checks that the identities of the
    # selection objects and skeleton objects are correct -- they are
    # assumed, based on previous tests, to correctly convey state
    # information.
    @memorycheck.check("skeltest")
    def Commutativity(self):
        sel0 = self.sk_context.elementselection.currentSelection()
        sk1 = self.sk_context.getObject()
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton="skeltest:skelextra",
            points=[Point(3.75,3.75)], shift=0, ctrl=0)
        sel1 = self.sk_context.elementselection.currentSelection()
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton="skeltest:skelextra",
            points=[Point(3.75,3.75)], shift=0, ctrl=0)
        sel2 = self.sk_context.elementselection.currentSelection()
        OOF.Skeleton.Modify(
            skeleton="skeltest:skelextra",
            modifier=Refine(targets=CheckHomogeneity(threshold=0.9),
                            criterion=Unconditionally(),
                            degree=Bisection(rule_set="conservative")))
        sk2 = self.sk_context.getObject()

        OOF.Skeleton.Undo(skeleton="skeltest:skelextra")
        OOF.Graphics_1.Toolbox.Select_Element.Undo(
            skeleton="skeltest:skelextra")
        self.assertEqual(id(
            self.sk_context.elementselection.currentSelection()), id(sel1))
        self.assertEqual(id(self.sk_context.getObject()), id(sk1))

        # Undo, then redo in the opposite order.
        OOF.Skeleton.Redo(skeleton="skeltest:skelextra")
        OOF.Graphics_1.Toolbox.Select_Element.Redo(
            skeleton="skeltest:skelextra")
        OOF.Graphics_1.Toolbox.Select_Element.Undo(
            skeleton="skeltest:skelextra")
        OOF.Skeleton.Undo(skeleton="skeltest:skelextra")
        self.assertEqual(id(
            self.sk_context.elementselection.currentSelection()), id(sel1))
        self.assertEqual(id(self.sk_context.getObject()), id(sk1))


    # Special test for a bug in which the "selected" flag wasn't being
    # set correctly by undo/redo operations.
    @memorycheck.check("skeltest")
    def SelectionStateBug(self):
        # First, make a selection.
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton="skeltest:skelextra",
            points=[Point(3.75,3.75)], shift=0, ctrl=0)
        # Then modify the skeleton.
        OOF.Skeleton.Modify(
            skeleton="skeltest:skelextra",
            modifier=Refine(targets=CheckHomogeneity(threshold=0.9),
                            criterion=Unconditionally(),
                            degree=Bisection(rule_set="conservative")))
        # Then undo the modification...
        OOF.Skeleton.Undo(skeleton="skeltest:skelextra")
        # And undo and redo the selection...
        OOF.Graphics_1.Toolbox.Select_Element.Undo(
            skeleton="skeltest:skelextra")
        OOF.Graphics_1.Toolbox.Select_Element.Redo(
            skeleton="skeltest:skelextra")
        # Then redo the modification...
        OOF.Skeleton.Redo(skeleton="skeltest:skelextra")
        # Then count the selected elements.
        sk = self.sk_context.getObject()
        elist = [x for x in sk.elements if x.selected]
        # If selection-state is propagating correctly, there'll be
        # three of them.
        self.assertEqual(len(elist), 3)

    @memorycheck.check("skeltest")
    def SelectSegmentPixels(self):
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:skelextra', points=[Point(0.0272374,13.5525)],
            shift=0, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:skelextra', points=[Point(3.79377,20.0584)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:skelextra', points=[Point(19.1167,20.144)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:skelextra', points=[Point(20.144,18.8599)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:skelextra', points=[Point(14.323,0.0272374)],
            shift=1, ctrl=0)
        OOF.PixelSelection.Select_Segment_Pixels(
            microstructure='skeltest', skeleton='skeltest:skelextra')
        ms = microstructure.microStructures['skeltest']
        pixelselection = ms.getSelectionContext()
        self.assertEqual(pixelselection.size(), 97)

    @memorycheck.check("skeltest")
    def SelectElementPixels(self):
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='skeltest:skelextra', points=[Point(1.39689,18.5175)],
            shift=0, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='skeltest:skelextra', points=[Point(4.5642,15.607)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='skeltest:skelextra', points=[Point(6.19066,13.2957)],
            shift=1, ctrl=0)
        OOF.PixelSelection.Select_Element_Pixels(
            microstructure='skeltest', skeleton='skeltest:skelextra')
        ms = microstructure.microStructures['skeltest']
        pixelselection = ms.getSelectionContext()
        self.assertEqual(pixelselection.size(), 1159)



class OOF_Skeleton_SmallBuffer(unittest.TestCase):
    def setUp(self):
        from ooflib.engine import skeletoncontext
        self.historysize = skeletoncontext.skeletonContexts.historysize
        OOF.Settings.UndoBuffer_Size.Skeleton(size=1)
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","triangle.png"), 
            microstructure_name='triangle', 
            height=automatic, 
            width=automatic)
        OOF.Windows.Graphics.New()
        OOF.Graphics_1.Toolbox.Pixel_Select.Burn(
            source='triangle:triangle.png', 
            local_flammability=0.10000000000000001, 
            global_flammability=0.20000000000000001, 
            color_space_norm='L1', 
            next_nearest=False, 
            points=[Point(72.9061,66.993)], shift=0, ctrl=0)
        OOF.PixelGroup.New(name='pixelgroup', microstructure='triangle')
        OOF.PixelGroup.AddSelection(microstructure='triangle', 
                                    group='pixelgroup')
        OOF.Graphics_1.Toolbox.Pixel_Select.Invert(
            source='triangle:triangle.png')
        OOF.PixelGroup.New(name='pixelgroup<2>', 
                           microstructure='triangle')
        OOF.PixelGroup.AddSelection(microstructure='triangle', 
                                    group='pixelgroup<2>')
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source='triangle:triangle.png')
        OOF.Skeleton.New(name='skeleton', 
                         microstructure='triangle', 
                         x_elements=3, y_elements=3, 
                         skeleton_geometry=TriSkeleton(
                arrangement='conservative',
                left_right_periodicity=False,
                top_bottom_periodicity=False))
        
    def tearDown(self):
        OOF.Graphics_1.File.Close()
        OOF.Settings.UndoBuffer_Size.Skeleton(size=self.historysize)
        
    @memorycheck.check("triangle")
    def Bufferbug(self):
        import os,random
        from ooflib.SWIG.common import crandom

        random.seed(17)
        crandom.rndmseed(17)
        
        OOF.Skeleton.Modify(skeleton='triangle:skeleton', 
                            modifier=Anneal(
                targets=AllNodes(),
                criterion=AverageEnergy(
                    alpha=0.94999999999999996),
                T=0.0,delta=1.0,
                iteration=FixedIteration(
                    iterations=20)))
        OOF.Skeleton.Modify(skeleton='triangle:skeleton', 
                            modifier=SwapEdges(
                targets=AllElements(),
                criterion=AverageEnergy(alpha=0.93650800000000001)))
        OOF.File.Save.Skeleton(filename="skeleton_bufferbug_test", 
                               mode='w', 
                               format='ascii', 
                               skeleton='triangle:skeleton')
        self.assert_(
            fp_file_compare(
                "skeleton_bufferbug_test",
                os.path.join("skeleton_data", "skeleton_bufferbug_ref"),
                1.e-10))
        os.remove("skeleton_bufferbug_test")
        



class OOF_Skeleton_CyclicBoundary(unittest.TestCase):
    def setUp(self):
        OOF.Microstructure.New(name='skelextra', 
                               width=1.0, height=1.0, 
                               width_in_pixels=10, height_in_pixels=10)
        OOF.Skeleton.New(name='cycletest', microstructure='skelextra', 
                         x_elements=4, y_elements=4, 
                         skeleton_geometry=QuadSkeleton(
                left_right_periodicity=False,
                top_bottom_periodicity=False))
        OOF.Windows.Graphics.New()
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.353167420814,0.716515837104)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.258597285068,0.661764705882)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.263574660633,0.442760180995)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.383031674208,0.268552036199)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.621945701357,0.23371040724)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.771266968326,0.338235294118)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.761312217195,0.616968325792)], shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skelextra:cycletest', 
            points=[Point(0.592081447964,0.741402714932)], shift=1, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton='skelextra:cycletest',name='boundary', 
            constructor=EdgeFromSegments(group=selection,direction='Clockwise'))
        OOF.Graphics_1.Toolbox.Select_Segment.Clear(
            skeleton='skelextra:cycletest')
            
    def tearDown(self):
        OOF.Graphics_1.File.Close()

    @memorycheck.check("skelextra")
    def CycleSave(self):
        import os,filecmp
        OOF.File.Save.Skeleton(filename="skeleton_save",mode="w",
                               format="ascii",skeleton="skelextra:cycletest")
        self.assert_(filecmp.cmp(reference_file("skeleton_data",
                                                  "cycletest"),
                                   "skeleton_save"))
        os.remove("skeleton_save")



def run_tests():

    test_set = [
        OOF_Skeleton_Extra("PinnedModify"),
        OOF_Skeleton_Extra("RichSave"),
        OOF_Skeleton_Extra("RichLoad"),
        OOF_Skeleton_Extra("Commutativity"),
        OOF_Skeleton_Extra("SelectionStateBug"),
        OOF_Skeleton_Extra("SelectSegmentPixels"),
        OOF_Skeleton_Extra("SelectElementPixels")
        ]

    test_set += [
        OOF_Skeleton_SmallBuffer("Bufferbug")
        ]

    test_set += [
        OOF_Skeleton_CyclicBoundary("CycleSave")
        ]

    logan = unittest.TextTestRunner()
    for t in test_set:
        print >> sys.stderr, "\n *** Running test: %s\n" % t.id()
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
        import oof2
        sys.path.append(os.path.dirname(oof2.__file__))
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
