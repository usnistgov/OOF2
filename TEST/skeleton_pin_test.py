# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

# Test suite for pinning skeleton nodes.

import unittest
import sys
from . import memorycheck
from .UTILS import file_utils
from ooflib.engine import skeletoncontext

reference_file = file_utils.reference_file
fp_file_compare = file_utils.fp_file_compare

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Utility function

def verify(skeleton, expected):
    skelctxt = skeletoncontext.skeletonContexts["microstructure:skeleton"]
    pinnedobjs = skelctxt.pinnednodes.retrieve()
    actual = set(p.getIndex() for p in pinnedobjs)
    expected = set(expected)
    if expected == actual:
        return True
    print(f"Pinned node comparison failed.\nExpected {expected}\nGot {actual}",
          file=sys.stderr)
    return False
    

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Check that nodes can be pinned and unpinned

class OOF_Pin(unittest.TestCase):
    def setUp(self):
         OOF.Microstructure.New(
             name='microstructure',
             width=1, height=1,
             width_in_pixels=10, height_in_pixels=10)
         OOF.Skeleton.New(
             name='skeleton',
             microstructure='microstructure',
             x_elements=8, y_elements=8,
             skeleton_geometry=QuadSkeleton(left_right_periodicity=False,
                                            top_bottom_periodicity=False))
         OOF.Windows.Graphics.New()
         OOF.Material.New(name='material', material_type='bulk')
         OOF.Property.Copy(property='Color', new_name='instance')
         OOF.Property.Parametrize.Color.instance(
             color=TranslucentGray(value=0.6,alpha=1))
         OOF.Material.Add_Property(name='material', property='Color:instance')
         OOF.Graphics_1.Layer.New(
             category='Microstructure',
             what='microstructure',
             how=MicrostructureMaterialDisplay(
                 no_material=TranslucentGray(value=0.0,alpha=1.0),
                 no_color=RGBAColor(red=0.0,green=0.0,blue=1.0,alpha=1.0)))
         OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
             source='microstructure',
             points=[
                 Point(-0.0330572993188194,0.7951783090690527),
                 Point(0.487845599038333,0.4444370241752368)],
             shift=False, ctrl=False)
         OOF.Material.Assign(
             material='material',
             microstructure='microstructure', pixels=selection)

    def tearDown(self):
        OOF.Graphics_1.File.Close()
        OOF.Material.Delete(name="material")
        OOF.Property.Delete(property='Color:instance')

    def checkPinned(self, expected):
        skelctxt = skeletoncontext.skeletonContexts["microstructure:skeleton"]
        pinnedobjs = skelctxt.pinnednodes.retrieve()
        actual = set(p.getIndex() for p in pinnedobjs)
        expected = set(expected)
        self.assertEqual(expected, actual)
         
    @memorycheck.check("microstructure")
    def Pin(self):
        self.checkPinned([])
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.37, 0.36))
        self.checkPinned([30])
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.5,0.5))
        self.checkPinned([30, 40])

    @memorycheck.check("microstructure")
    def Unpin(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.37, 0.36))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.5,0.5))
        OOF.Graphics_1.Toolbox.Pin_Nodes.UnPin(
            skeleton='microstructure:skeleton',
            point=Point(0.37, 0.37))
        self.checkPinned([40])
        OOF.Graphics_1.Toolbox.Pin_Nodes.UnPin(
            skeleton='microstructure:skeleton',
            point=Point(0.5,0.5))
        self.checkPinned([])

    @memorycheck.check("microstructure")
    def UnpinAll(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.37, 0.36))
        OOF.Skeleton.PinNodes.UnpinAll(skeleton='microstructure:skeleton')
        self.checkPinned([])

    @memorycheck.check("microstructure")
    def Invert(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Invert(
            skeleton='microstructure:skeleton')
        self.assertTrue(verify("microstructure:skeleton",
                               range(81)))
        OOF.Graphics_1.Toolbox.Pin_Nodes.UnPin(
            skeleton='microstructure:skeleton',
            point=Point(0.5,0.5))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Invert(
            skeleton="microstructure:skeleton")
        self.checkPinned([40])
        
    @memorycheck.check("microstructure")
    def Selection(self):
        # Select four nodes
        OOF.Graphics_1.Toolbox.Select_Node.Rectangle(
            skeleton='microstructure:skeleton',
            points=[Point(0.2187124348871376,0.6666889274742885),
                    Point(0.42360090824095087,0.4444370241752368)],
            shift=False, ctrl=False)
        OOF.Skeleton.PinNodes.Pin_Node_Selection(
            skeleton='microstructure:skeleton')
        self.checkPinned([38, 39, 47, 48])
        # Unselect two nodes
        OOF.Graphics_1.Toolbox.Select_Node.Rectangle(
            skeleton='microstructure:skeleton',
            points=[Point(0.1944036329638038,0.6805796714304793),
                    Point(0.42360090824095087,0.5763990917590488)],
            shift=False, ctrl=True)
        OOF.Skeleton.PinNodes.UnPin_Node_Selection(
            skeleton='microstructure:skeleton')
        self.checkPinned([47, 48])

    @memorycheck.check("microstructure")
    def PinSelectedSegments(self):
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='microstructure:skeleton',
            points=[Point(-6.678242286641684e-05,0.5416722318685719)],
            shift=False, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='microstructure:skeleton',
            points=[Point(0.1229531187391478,0.5451449178576196)],
            shift=True, ctrl=False)
        OOF.Graphics_1.Toolbox.Select_Segment.Single_Segment(
            skeleton='microstructure:skeleton',
            points=[Point(0.008354481100574275,0.42707359422999847)],
            shift=True, ctrl=False)
        OOF.Skeleton.PinNodes.Pin_Selected_Segments(
            skeleton='microstructure:skeleton')
        self.checkPinned([27, 36, 37, 45, 46])

    @memorycheck.check("microstructure")
    def SelectedElements(self):
        # Select a square of four elements containing no boundary nodes
        OOF.Graphics_1.Toolbox.Select_Element.Rectangle(
            skeleton='microstructure:skeleton',
            points=[Point(0.10906237478295708,0.40623747829571233),
                    Point(0.4007679978629624,0.09022305329237323)],
            shift=False, ctrl=False)
        # Pin the external nodes of the selection
        OOF.Skeleton.PinNodes.Pin_Selected_Elements(
            skeleton='microstructure:skeleton',
            internal=False, boundary=True)
        self.assertTrue(verify("microstructure:skeleton",
                               [10, 11, 12, 19, 21, 28, 29, 30]))
        # Pin all nodes of the selection
        OOF.Graphics_1.Toolbox.Pin_Nodes.UnPinAll(
            skeleton='microstructure:skeleton')
        OOF.Skeleton.PinNodes.Pin_Selected_Elements(
            skeleton='microstructure:skeleton',
            internal=True, boundary=True)
        self.assertTrue(verify("microstructure:skeleton",
                               [10, 11, 12, 19, 20, 21, 28, 29, 30]))
        # Pin only the internal nodes
        OOF.Graphics_1.Toolbox.Pin_Nodes.UnPinAll(
            skeleton='microstructure:skeleton')
        OOF.Skeleton.PinNodes.Pin_Selected_Elements(
            skeleton='microstructure:skeleton',
            internal=True, boundary=False)
        self.checkPinned([20])

    @memorycheck.check("microstructure")
    def InternalBdys(self):
        OOF.Skeleton.PinNodes.Pin_Internal_Boundary_Nodes(
            skeleton='microstructure:skeleton')
        self.assertTrue(
            verify("microstructure:skeleton",
                   [40, 49, 54, 55, 56, 57, 58, 27, 28, 29, 30, 31]))

    #=--=##=--=##=--=##=--=#

    # Check that modified Skeletons get the correct pinned nodes from
    # their parent.  That is, check that the pinned nodes are
    # propagated properly to new child Skeletons.
    
    @memorycheck.check("microstructure")
    def NewSkeleton(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.12147722719380247,0.12494991318284998))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.24302123681047139,0.12147722719380238))
        self.checkPinned([10, 11])
        # Create a new Skeleton by refining all elements.
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckAllElements(),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.3))
        self.checkPinned([91, 92])
        # Create another new Skeleton by refining heterogenous elements
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckHomogeneity(threshold=0.9),
                            divider=TransitionPoints(minlength=0.01),
                            rules='Quick',
                            alpha=0.3))
        self.checkPinned([380, 381])

    @memorycheck.check("microstructure")
    def NewSkeletonDeputy(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.12147722719380247,0.12494991318284998))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.24302123681047139,0.12147722719380238))
        self.checkPinned([10, 11])
        # Create a new Skeleton by moving one node.
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.12842259917189783,0.256911980766662),
            destination=Point(0.1770402030185654,0.29511152664618645))
        self.checkPinned([10, 11])
        # Create another new Skeleton by Smoothing
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Smooth(targets=AllNodes(),
                            criterion=AverageEnergy(alpha=0.3),
                            T=0,
                            iteration=FixedIteration(iterations=5)))
        self.checkPinned([10, 11])
        # Create another new Skeleton by refining all elements,
        # checking that a non-deputy inherits correctly from a deputy.
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckAllElements(),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.3))
        self.checkPinned([91, 92])

    #=--=##=--=##=--=##=--=#

    # Check that pinned nodes are propagated correctly to parent
    # Skeletons.

    @memorycheck.check("microstructure")
    def Parent(self):
        # Create a non-deputy child Skeleton
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckAllElements(),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.3))
        # Pin nodes in the child
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.11800454120475479,0.12494991318284998))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.1770402030185654,0.1284225991718977))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.22565780686523296,0.1318952851609454))
        self.checkPinned([91, 169, 92])
        # Undo the Skeleton modification
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([10, 11])
        
    @memorycheck.check("microstructure")
    def ParentDeputy(self):
        # Create a deputy child Skeleton by moving one node
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.37498330439428335,0.6215440096166687),
            destination=Point(0.4270735942299986,0.5833444637371441))
        # Pin nodes in the child, including the moved node.
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin( # the moved node
            skeleton='microstructure:skeleton',
            point=Point(0.4201282222519032,0.5868171497261918))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.09022305329237335,0.1388406571390407))
        self.checkPinned([10, 48])
        # Undo the Skeleton modification
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        # The moved not is *not* pinned.
        self.checkPinned([10])
        
    #=--=##=--=##=--=##=--=#
        
    # Check that pinned nodes are propagated correctly to pre-existing
    # child Skeletons.

    @memorycheck.check("microstructure")
    def Child(self):
        # Create a non-deputy child
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckAllElements(),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.3))
        # Revert to the parent
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        # Pin nodes
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.11800454120475479,0.1318952851609454))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.24649392279951904,0.12147722719380238))
        self.checkPinned([10, 11])
        # Go back to the child
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([91, 92])
        
    @memorycheck.check("microstructure")
    def ChildDeputy(self):
        # Create a deputy child by moving a node
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.8750500868171497,0.8715774008281019),
            destination=Point(0.8299051689595298,0.847268598904768))
        # Revert to the parent
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        # Pin nodes, including the one that moved
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin( # this one moved
            skeleton='microstructure:skeleton',
            point=Point(0.8785227728061973,0.8715774008281019))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.13536797114999322,0.1318952851609454))
        self.checkPinned([10, 70])
        # Redo the Skeleton modification
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([10])

    # Create a sequence of modifications and check that pinning is
    # propagated from deputy to non-deputy as well as deputy to
    # deputy.  Make the initial pin in both deputy and non-deputy
    # skeletons.

    @memorycheck.check("microstructure")
    def Complicated(self):
        # Move a node
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.124,0.121),
            destination=Point(0.166,0.086))
        # Move a different node
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.256,0.246),
            destination=Point(0.309,0.197))
        # Select an element and refine it
        OOF.Graphics_1.Toolbox.Select_Element.Single_Element(
            skeleton='microstructure:skeleton',
            points=[Point(0.798,0.795)],
            shift=False, ctrl=False)
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckSelectedElements(),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.3))
        # Undo all three modifications
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        # Pin the first node that was moved
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.124,0.124))
        self.checkPinned([10])
        # Pin the second node that was moved
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.246,0.253))
        self.checkPinned([10, 20])
        # Pin a node of the refined element
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.750,0.760))
        self.checkPinned([10, 20, 60])
        # Pin a node uninvolved in the skeleton modifications
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.503,0.496))
        self.checkPinned([10, 20, 40, 60])
        # Redo the first node motion.
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        # The moved node is no longer pinned.
        self.checkPinned([20, 40, 60])
        # Redo the second node motion.
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([40, 60])
        # Redo the refinement
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([121, 141])
        # Unpin all nodes
        OOF.Graphics_1.Toolbox.Pin_Nodes.UnPinAll(
            skeleton='microstructure:skeleton')
        # Go back to the Skeleton with a single node moved
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        # Pin the same nodes as before.
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.159,0.093))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.246,0.246))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.496,0.499))
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.746,0.753))
        self.checkPinned([10, 20, 40, 60])
        # Revert to unmodified Skeleton, then redo each modification
        # and check that the expected nodes are pinned.
        OOF.Skeleton.Undo(skeleton="microstructure:skeleton")
        self.checkPinned([20, 40, 60])
        OOF.Skeleton.Redo(skeleton="microstructure:skeleton")
        self.checkPinned([10, 20, 40, 60])
        OOF.Skeleton.Redo(skeleton="microstructure:skeleton")
        self.checkPinned([10, 40, 60])
        OOF.Skeleton.Redo(skeleton="microstructure:skeleton")
        self.checkPinned([91, 121, 141])

    #=--=##=--=##=--=##=--=#
    
    # Pin, Refine, Undo pin, Undo refine, Redo pin, Redo refine
    @memorycheck.check("microstructure")
    def Commutivity1(self):
        # Base state has one node pinned, so that comparisons are
        # non-trivial.
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.116,0.751))
        self.checkPinned([55])
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
             skeleton='microstructure:skeleton',
             point=Point(0.237,0.744))
        self.checkPinned([55, 56])
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckHomogeneity(threshold=0.9),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.3))
        self.checkPinned([136, 137])
        OOF.Skeleton.PinNodes.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([136])
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([55])
        OOF.Skeleton.PinNodes.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([55, 56])
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([136, 137])

    # Pin, Move nodes, Undo pin, Undo modification, Redo pin, Redo
    # modification. Identical to Commutivity1, but the skeleton
    # modification creates a deputy Skeleton.
    @memorycheck.check("microstructure")
    def Commutivity2(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.116,0.751))
        self.checkPinned([55])
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
             skeleton='microstructure:skeleton',
             point=Point(0.237,0.744))
        self.checkPinned([55, 56])
        # create a deputy
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=SnapNodes(targets=SnapAll(),
                               criterion=AverageEnergy(alpha=0.7)))
        self.checkPinned([55, 56])
        OOF.Skeleton.PinNodes.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([55])
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([55])
        OOF.Skeleton.PinNodes.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([55, 56])
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([55, 56])

    # Refine, Pin, Undo refine, Undo pin, Redo refine, Redo pin.  Same
    # as Commutivity1, but the order of operations is reversed.
    @memorycheck.check("microstructure")
    def Commutivity3(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.116,0.751))
        self.checkPinned([55])
        # Refine
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=Refine(targets=CheckHomogeneity(threshold=0.9),
                            divider=Bisection(minlength=0),
                            rules='Quick',
                            alpha=0.3))
        self.checkPinned([136])
        # Pin a bunch of nodes, some not in the unrefined skeleton
        OOF.Graphics_1.Toolbox.Select_Node.Rectangle(
            skeleton='microstructure:skeleton',
            points=[Point(0.215,0.895), Point(0.399,0.729)],
            shift=False, ctrl=False)
        OOF.Skeleton.PinNodes.Pin_Node_Selection(
            skeleton='microstructure:skeleton')
        self.checkPinned([136,
                          137, 181, 138,
                          187, 192, 190,
                          146, 191, 147])
        # Undo the refinement
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([55, 56, 57, 65, 66])
        # Undo the pinning
        OOF.Skeleton.PinNodes.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([55])
        # Redo the refinement
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([136])
        # Redo the pinning
        OOF.Skeleton.PinNodes.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([136,
                          137, 181, 138,
                          187, 192, 190,
                          146, 191, 147])
        
    # Same as Commutivity3, but the Skeleton modification creates
    # a deputy skeleton.
    @memorycheck.check("microstructure")
    def Commutivity4(self):
        OOF.Graphics_1.Toolbox.Pin_Nodes.Pin(
            skeleton='microstructure:skeleton',
            point=Point(0.116,0.751))
        self.checkPinned([55])
        # Move some nodes
        OOF.Skeleton.Modify(
            skeleton='microstructure:skeleton',
            modifier=SnapNodes(targets=SnapAll(),
                               criterion=AverageEnergy(alpha=0.7)))
        self.checkPinned([55])
        # Pin multiple nodes, some of which have moved
        OOF.Graphics_1.Toolbox.Select_Node.Rectangle(
            skeleton='microstructure:skeleton',
            points=[Point(0.194,0.836), Point(0.434,0.579)],
            shift=False, ctrl=False)
        OOF.Skeleton.PinNodes.Pin_Node_Selection(
            skeleton='microstructure:skeleton')
        self.checkPinned([55, 47, 48, 56, 57])
        # Undo the skeleton modification
        OOF.Skeleton.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([55, 47, 48])
        # Undo the pinning
        OOF.Skeleton.PinNodes.Undo(skeleton='microstructure:skeleton')
        self.checkPinned([55])
        # Redo the skeleton modification
        OOF.Skeleton.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([55])
        # Redo the pinning
        OOF.Skeleton.PinNodes.Redo(skeleton='microstructure:skeleton')
        self.checkPinned([55, 47, 48, 56, 57])

    # Repeat Commutivity[1-4], but start with a deputy skeleton.
    # Since these call the other tests, they don't use the
    # memorycheck.check decorator.
    
    def Commutivity1D(self):
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.868,0.239),
            destination=Point(0.822,0.190))
        self.Commutivity1()

    # Same as Commutivity2, but starting with a deputy skeleton
    def Commutivity2D(self):
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.868,0.239),
            destination=Point(0.822,0.190))
        self.Commutivity2()

    # Same as Commutivity3, but starting with a deputy skeleton
    def Commutivity3D(self):
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.868,0.239),
            destination=Point(0.822,0.190))
        self.Commutivity3()
        
    # Same as Commutivit43, but starting with a deputy skeleton
    def Commutivity4D(self):
        OOF.Graphics_1.Toolbox.Move_Nodes.MoveNode(
            origin=Point(0.868,0.239),
            destination=Point(0.822,0.190))
        self.Commutivity4()
        
#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

test_set = [
    OOF_Pin("Pin"),
    OOF_Pin("Unpin"),
    OOF_Pin("UnpinAll"),
    OOF_Pin("Invert"),
    OOF_Pin("Selection"),
    OOF_Pin("PinSelectedSegments"),
    OOF_Pin("SelectedElements"),
    OOF_Pin("InternalBdys"),
    OOF_Pin("NewSkeleton"),
    OOF_Pin("NewSkeletonDeputy"),
    OOF_Pin("Parent"),
    OOF_Pin("ParentDeputy"),
    OOF_Pin("Child"),
    OOF_Pin("ChildDeputy"),
    OOF_Pin("Complicated"),
    OOF_Pin("Commutivity1"),
    OOF_Pin("Commutivity2"),
    OOF_Pin("Commutivity3"),
    OOF_Pin("Commutivity4"),
    OOF_Pin("Commutivity1D"),
    OOF_Pin("Commutivity2D"),
    OOF_Pin("Commutivity3D"),
    OOF_Pin("Commutivity4D")
]
