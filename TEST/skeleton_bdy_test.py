# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 


# Test suite for skeleton boundary construction, modification, and
# deletion.  This test should follow the more basic skeleton_test
# tests.

import unittest, os
from . import memorycheck
from .UTILS.file_utils import reference_file

# Utility to extract tuples of node indices from an edge boundary, for
# comparison.
def nodesFromEdgeBdy(skelctxt, bdyname):
    edges = skelctxt.edgeboundaries[bdyname].current_boundary().edges
    nodepairs = [e.get_nodes() for e in edges] # list of lists
    indices = [(n0.index, n1.index) for (n0, n1) in nodepairs]
    return indices
    

class Skeleton_Boundary(unittest.TestCase):
    def setUp(self):
        global skeletoncontext
        from ooflib.engine import skeletoncontext
        global cskeleton
        from ooflib.SWIG.engine import cskeleton
        global cmicrostructure
        from ooflib.SWIG.common import cmicrostructure
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","small.ppm"),
            microstructure_name="skeltest",
            height=20.0, width=20.0)
        OOF.Image.AutoGroup(image="skeltest:small.ppm")
        OOF.Skeleton.New(
            name="bdytest",
            microstructure="skeltest", 
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))

        # Need a graphics window so we can do the direct selection.
        OOF.Windows.Graphics.New()
        self.sk_context = skeletoncontext.skeletonContexts[
            "skeltest:bdytest"]

    def tearDown(self):
        OOF.Graphics_1.File.Close()

    # Check that the default boundaries exist and are the right size.
    # As with most tests, this could do more, i.e. ensure edges are
    # exterior, check that indices are as expected, etc.
    @memorycheck.check("skeltest")
    def Defaults(self):
        default_edges = ["top", "bottom", "left", "right"]
        self.assertEqual(len(self.sk_context.edgeboundaries), 4)
        for e in self.sk_context.edgeboundaries.keys(): 
            self.assertTrue(e in default_edges)
            default_edges.remove(e)
            
        default_points = ["topleft", "topright", "bottomleft", "bottomright"]
        self.assertEqual(len(self.sk_context.pointboundaries), 4)
        for p in self.sk_context.pointboundaries.keys():
            self.assertTrue(p in default_points)
            default_points.remove(p)

        for e in self.sk_context.edgeboundaries.values():
            self.assertEqual(e.current_size(), 8)

        for p in self.sk_context.pointboundaries.values():
            self.assertEqual(p.current_size(), 1)


    @memorycheck.check("skeltest")
    def Construct_Edge_from_Elements(self):
        # Create bdy from selected elements
        OOF.Graphics_1.Toolbox.Select_Element.Rectangle(
            skeleton="skeltest:bdytest",
            points=[Point(4.5,8.5), Point(14.0,4.0)],
            shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test",
            constructor=EdgeFromElements(group=selection,
                                         direction="Clockwise"))
        self.assertTrue("test" in self.sk_context.edgeboundaries.keys())
        test_bdy = self.sk_context.edgeboundaries["test"]
        self.assertEqual(test_bdy.current_size(), 8)
        # Create bdy from element group
        OOF.ElementGroup.New_Group(skeleton='skeltest:bdytest',name='egroup')
        OOF.ElementGroup.Add_to_Group(skeleton='skeltest:bdytest',
                                      group='egroup')
        OOF.Skeleton.Boundary.Construct(
            skeleton='skeltest:bdytest', name='test2',
            constructor=EdgeFromElements(group='egroup',
                                         direction='Clockwise'))
        self.assertTrue("test2" in self.sk_context.edgeboundaries.keys())
        test_bdy = self.sk_context.edgeboundaries["test2"]
        self.assertEqual(test_bdy.current_size(), 8)

    @memorycheck.check("skeltest")
    def Construct_Edge_from_Segments(self):
        # Create bdy from selected segments
        OOF.Graphics_1.Toolbox.Select_Segment.Rectangle(
            skeleton="skeltest:bdytest",
            points=[Point(4.5,8.5), Point(14.0,4.0)],
            shift=0, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton="skeltest:bdytest",
            points=[Point(7.5,6.25)],
            shift=0, ctrl=1)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton="skeltest:bdytest",
            points=[Point(10.0,6.25)],
            shift=0, ctrl=1)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test",
            constructor=EdgeFromSegments(group=selection,
                                         direction="Clockwise"))
        self.assertTrue("test" in self.sk_context.edgeboundaries.keys())
        test_bdy = self.sk_context.edgeboundaries["test"]
        self.assertEqual(test_bdy.current_size(), 8)
        # Create bdy from segment group
        OOF.SegmentGroup.New_Group(skeleton='skeltest:bdytest', name="sgroup")
        OOF.SegmentGroup.Add_to_Group(skeleton='skeltest:bdytest',
                                      group='sgroup')
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test2",
            constructor=EdgeFromSegments(group='sgroup',
                                         direction="Clockwise"))
        self.assertTrue("test2" in self.sk_context.edgeboundaries.keys())
        test_bdy = self.sk_context.edgeboundaries["test2"]
        self.assertEqual(test_bdy.current_size(), 8)

    @memorycheck.check("skeltest")
    def Construct_Edge_from_Nodes(self):
        OOF.Graphics_1.Toolbox.Select_Node.Rectangle(
            skeleton="skeltest:bdytest",
            points=[Point(3.75,3.75), Point(11.25,11.25)],
            shift=0, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton="skeltest:bdytest",
            points=[Point(7.5,7.5)],
            shift=0, ctrl=1)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test",
            constructor=EdgeFromNodes(group=selection,
                                      direction="Clockwise"))
        self.assertTrue("test" in self.sk_context.edgeboundaries.keys())
        test_bdy = self.sk_context.edgeboundaries["test"]
        self.assertEqual(test_bdy.current_size(), 8)
        OOF.NodeGroup.New_Group(skeleton='skeltest:bdytest', name='ngroup')
        OOF.NodeGroup.Add_to_Group(skeleton='skeltest:bdytest', group='ngroup')
        OOF.Skeleton.Boundary.Construct(
            skeleton='skeltest:bdytest', name='test2',
            constructor=EdgeFromNodes(group='ngroup', direction="Clockwise"))
        self.assertTrue("test2" in self.sk_context.edgeboundaries.keys())
        test_bdy = self.sk_context.edgeboundaries["test2"]
        self.assertEqual(test_bdy.current_size(), 8)

    @memorycheck.check("skeltest")
    def Construct_Edge_from_Nodes2(self):
        # A configuration that failed with an earlier version of
        # segments_from_seg_aggregate.
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='skeltest:bdytest',
            points=[Point(8.509333333333332,13.258666666666667)],
            shift=True, ctrl=False)
        OOF.Skeleton.Modify(
            skeleton='skeltest:bdytest',
            modifier=SplitQuads(targets=SelectedElements(),
                                criterion=AverageEnergy(alpha=1),
                                split_how=TrialAndErrorQ2T()))
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(2.269333333333333,12.357333333333333)],
            shift=True, ctrl=False)        
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(4.696,12.773333333333333)],
            shift=True, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(7.677333333333333,12.703999999999999)],
            shift=True, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(9.965333333333332,12.565333333333331)],
            shift=True, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(12.253333333333332,12.565333333333331)],
            shift=True, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(7.607999999999999,14.783999999999999)],
            shift=True, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(4.834666666666666,14.853333333333332)],
            shift=True, ctrl=False)
        OOF.Skeleton.Boundary.Construct(
            skeleton='skeltest:bdytest',
            name='boundary',
            constructor=EdgeFromNodes(group=selection,
                                      direction='Left to right'))
        self.assertTrue("boundary" in self.sk_context.edgeboundaries)
        bdy = self.sk_context.edgeboundaries["boundary"]
        self.assertEqual(bdy.current_size(), 6)
        self.assertEqual(nodesFromEdgeBdy(self.sk_context, "boundary"),
                         [(127, 128), (128, 137), (137, 138), (138, 129),
                          (129, 130), (130, 131)])
        OOF.Skeleton.Boundary.Construct(
            skeleton='skeltest:bdytest',
            name='boundary2',
            constructor=EdgeFromNodes(group=selection,
                                      direction='Right to left'))
        self.assertTrue("boundary2" in self.sk_context.edgeboundaries)
        bdy2 = self.sk_context.edgeboundaries["boundary2"]
        self.assertEqual(bdy2.current_size(), 6)
        self.assertEqual(nodesFromEdgeBdy(self.sk_context, "boundary2"),
                         [(131, 130), (130, 129), (129, 138), (138, 137),
                          (137, 128), (128, 127)])
        # Make the node set unsequenceable by unselecting a critical
        # node, leaving a set that has more than one possible path.
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(2.4079999999999995,12.495999999999999)],
            shift=False, ctrl=True)
        self.assertRaises(ooferror.PyErrUserError,
                          OOF.Skeleton.Boundary.Construct,
                          skeleton='skeltest:bdytest',
                          name='boundary3',
                          constructor=EdgeFromNodes(group=selection,
                                                    direction='Right to left'))
        self.assertTrue("boundary3" not in self.sk_context.edgeboundaries)
        # Make it differently unsequenceable by reselecting the
        # previously unselected node, and selecting other that are not
        # connected to the first set.
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(4.834666666666666,14.853333333333332)],
            shift=True, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(7.191999999999999,5.215999999999999)],
            shift=False, ctrl=True)
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton='skeltest:bdytest',
            points=[Point(7.469333333333332,2.5120000000000005)],
            shift=False, ctrl=True)
        self.assertRaises(ooferror.PyErrUserError,
                          OOF.Skeleton.Boundary.Construct,
                          skeleton='skeltest:bdytest',
                          name='boundary3',
                          constructor=EdgeFromNodes(group=selection,
                                                    direction='Right to left'))
        self.assertTrue("boundary3" not in self.sk_context.edgeboundaries)
    @memorycheck.check("skeltest")
    def Construct_Point_from_Elements(self):
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton="skeltest:bdytest",
            points=[Point(3.75,3.75)],
            shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test",
            constructor=PointFromElements(group=selection))
        self.assertTrue("test" in self.sk_context.pointboundaries.keys())
        test_bdy = self.sk_context.pointboundaries["test"]
        self.assertEqual(test_bdy.current_size(), 4)
        OOF.ElementGroup.New_Group(skeleton='skeltest:bdytest', name='egroup')
        OOF.ElementGroup.Add_to_Group(skeleton='skeltest:bdytest',
                                      group='egroup')
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test2",
            constructor=PointFromElements(group='egroup'))
        self.assertTrue("test2" in self.sk_context.pointboundaries.keys())
        test_bdy = self.sk_context.pointboundaries["test2"]
        self.assertEqual(test_bdy.current_size(), 4)


    @memorycheck.check("skeltest")
    def Construct_Point_from_Segments(self):
        OOF.Graphics_1.Toolbox.Select_Segment.Rectangle(
            skeleton="skeltest:bdytest",
            points=[Point(4.5,8.5), Point(14.0,4.0)],
            shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test",
            constructor=PointFromSegments(group=selection))
        self.assertTrue("test" in self.sk_context.pointboundaries.keys())
        test_bdy = self.sk_context.pointboundaries["test"]
        self.assertEqual(test_bdy.current_size(), 8)
        OOF.SegmentGroup.New_Group(skeleton='skeltest:bdytest', name='sgroup')
        OOF.SegmentGroup.Add_to_Group(skeleton='skeltest:bdytest',
                                      group='sgroup')
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test2",
            constructor=PointFromSegments(group='sgroup'))
        self.assertTrue("test2" in self.sk_context.pointboundaries.keys())
        test_bdy = self.sk_context.pointboundaries["test2"]
        self.assertEqual(test_bdy.current_size(), 8)
        
        
    @memorycheck.check("skeltest")
    def Construct_Point_from_Nodes(self):
        OOF.Graphics_1.Toolbox.Select_Node.Rectangle(
            skeleton="skeltest:bdytest",
            points=[Point(3.75,3.75), Point(11.25,11.25)],
            shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test",
            constructor=PointFromNodes(group=selection))
        self.assertTrue("test" in self.sk_context.pointboundaries.keys())
        test_bdy = self.sk_context.pointboundaries["test"]
        self.assertEqual(test_bdy.current_size(), 9)
        OOF.NodeGroup.New_Group(skeleton='skeltest:bdytest', name='ngroup')
        OOF.NodeGroup.Add_to_Group(skeleton='skeltest:bdytest', group='ngroup')
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test2",
            constructor=PointFromNodes(group='ngroup'))
        self.assertTrue("test2" in self.sk_context.pointboundaries.keys())
        test_bdy = self.sk_context.pointboundaries["test2"]
        self.assertEqual(test_bdy.current_size(), 9)

    # For deletion, do two, one for edge and one for point.
    @memorycheck.check("skeltest")
    def Delete(self):
        OOF.Skeleton.Boundary.Delete(skeleton="skeltest:bdytest",
                                     boundary="top")
        self.assertEqual(len(self.sk_context.edgeboundaries), 3)
        self.assertTrue(not "top" in self.sk_context.edgeboundaries.keys())
        OOF.Skeleton.Boundary.Delete(skeleton="skeltest:bdytest",
                                     boundary="topright")
        self.assertEqual(len(self.sk_context.pointboundaries), 3)
        self.assertTrue(not "topright" in self.sk_context.pointboundaries.keys())

    @memorycheck.check("skeltest")
    def Rename(self):
        bdy0 = self.sk_context.edgeboundaries["top"]
        OOF.Skeleton.Boundary.Rename(skeleton="skeltest:bdytest",
                                     boundary="top", name="test")
        self.assertEqual(len(self.sk_context.edgeboundaries), 4)
        self.assertTrue("test" in self.sk_context.edgeboundaries.keys())
        bdy1 = self.sk_context.edgeboundaries["test"]
        self.assertEqual(id(bdy0),id(bdy1))
        
    # "Modify" does not (yet) test direction reversal for edge boundaries.
    @memorycheck.check("skeltest")
    def Modify(self):
        OOF.Graphics_1.Toolbox.Select_Segment.Rectangle(
            skeleton="skeltest:bdytest",
            points=[Point(3.75,3.75), Point(11.25,6.25)],
            shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test",
            constructor=EdgeFromSegments(group=selection,
                                         direction="Left to right"))
        bdy0 = self.sk_context.edgeboundaries["test"]
        OOF.Graphics_1.Toolbox.Select_Segment.Rectangle(
            skeleton="skeltest:bdytest",
            points=[Point(8.75,3.75), Point(18.75,6.25)],
            shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Modify(
            skeleton="skeltest:bdytest", boundary="test",
            modifier=AddSegments(group=selection))
        bdy1 = self.sk_context.edgeboundaries["test"]
        self.assertEqual(id(bdy1), id(bdy0))
        self.assertEqual(bdy1.current_size(), 5)
        OOF.Graphics_1.Toolbox.Select_Segment.Undo(
            skeleton="skeltest:bdytest")
        OOF.Skeleton.Boundary.Modify(
            skeleton="skeltest:bdytest", boundary="test",
            modifier=RemoveSegments(group=selection))
        bdy2 = self.sk_context.edgeboundaries["test"]
        self.assertEqual(id(bdy2), id(bdy0))
        self.assertEqual(bdy2.current_size(), 3)
        
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton="skeltest:bdytest",
            points=[Point(5.25,5.25)], shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton="skeltest:bdytest", name="test2",
            constructor=PointFromNodes(group=selection))
        bdy0 = self.sk_context.pointboundaries["test2"]
        OOF.Graphics_1.Toolbox.Select_Node.Single_Node(
            skeleton="skeltest:bdytest",
            points=[Point(7.25,7.25)], shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Modify(
            skeleton="skeltest:bdytest", boundary="test2",
            modifier=AddNodes(group=selection))
        bdy1 = self.sk_context.pointboundaries["test2"]
        self.assertEqual(id(bdy1),id(bdy0))
        self.assertEqual(bdy1.current_size(), 2)
        OOF.Graphics_1.Toolbox.Select_Node.Undo(
            skeleton="skeltest:bdytest")
        OOF.Skeleton.Boundary.Modify(
            skeleton="skeltest:bdytest", boundary="test2",
            modifier=RemoveNodes(group=selection))
        bdy2 = self.sk_context.pointboundaries["test2"]
        self.assertEqual(id(bdy2),id(bdy0))
        self.assertEqual(bdy2.current_size(), 1)

    @memorycheck.check("skeltest")
    def Modify2(self):
        # Build a new boundary and refine the skeleton, then remove a
        # segment from the boundary.

        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:bdytest',
            points=[Point(0.729257641921,12.5458515284)], shift=0, ctrl=0)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:bdytest',
            points=[Point(3.51528384279,12.4497816594)], shift=1, ctrl=0)
        OOF.Skeleton.Boundary.Construct(
            skeleton='skeltest:bdytest',
            name='boundary',
            constructor=EdgeFromSegments(group=selection,
                                         direction='Left to right'))
        test_bdy = self.sk_context.edgeboundaries["boundary"]
        self.assertEqual(test_bdy.current_size(), 2)
        OOF.Skeleton.Modify(
            skeleton='skeltest:bdytest', 
            modifier=Refine(targets=CheckAllElements(),
                            divider=Bisection(minlength=0.0),
                            rules='Quick',
                            alpha=0.3))
        self.assertEqual(test_bdy.current_size(), 4)
        # Select a refined segment and remove it from the boundary
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='skeltest:bdytest',
            points=[Point(0.248908296943,12.7379912664)], shift=0, ctrl=0)
        OOF.Skeleton.Boundary.Modify(
            skeleton='skeltest:bdytest',
            boundary='boundary',
            modifier=RemoveSegments(group=selection))
        self.assertEqual(test_bdy.current_size(), 3)
        # Undo the refinement
        OOF.Skeleton.Undo(skeleton='skeltest:bdytest')
        self.assertEqual(test_bdy.current_size(), 1)
        # Redo it.
        OOF.Skeleton.Redo(skeleton='skeltest:bdytest')
        self.assertEqual(test_bdy.current_size(), 3)

test_set = [
    Skeleton_Boundary("Defaults"),
    Skeleton_Boundary("Construct_Edge_from_Elements"),
    Skeleton_Boundary("Construct_Edge_from_Segments"),
    Skeleton_Boundary("Construct_Edge_from_Nodes"),
    Skeleton_Boundary("Construct_Edge_from_Nodes2"),
    Skeleton_Boundary("Construct_Point_from_Elements"),
    Skeleton_Boundary("Construct_Point_from_Segments"),
    Skeleton_Boundary("Construct_Point_from_Nodes"),
    Skeleton_Boundary("Delete"),
    Skeleton_Boundary("Rename"),
    Skeleton_Boundary("Modify"),
    Skeleton_Boundary("Modify2")
]

