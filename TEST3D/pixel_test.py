# -*- python -*-
# $RCSfile: pixel_test.py,v $
# $Revision: 1.2 $
# $Author: vrc $
# $Date: 2007/09/26 22:03:43 $

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@ctcms.nist.gov. 

# File for testing pixel grouping and selection operations on
# microstructures.  This includes re-running the Microstructure
# save/load and copy operations to ensure that they save/load/copy the
# pixel groups correctly.

# Need to be able to open a graphics window and make selections,
# also, of course.


import unittest, os

# Prerequisite for making toolbox selections is the existence of a
# graphics window.  These tests just open and close a graphics window.
class Graphics_Ops(unittest.TestCase):
    def setUp(self):
        global gfxmanager
        from ooflib.common.IO import gfxmanager

    # Opens a new graphics window, assuming that none are open (so
    # that the name will be "Graphics_1").
    def New(self):
        self.assertRaises(AttributeError,
                          OOF.Windows.__getattr__,
                          attr="Graphics_1")
        OOF.Windows.Graphics.New()
        self.assert_(hasattr(OOF.Windows.Graphics, "Graphics_1"))
        self.assert_(hasattr(OOF, "Graphics_1"))
        self.assertEqual(len(gfxmanager.gfxManager.windows), 1)

    # "Close" Assumes that a graphics window is open.  The "Close"
    # item is actually in OOF.Graphics_n, not in OOF.Windows.Graphics.
    def Close(self):
        # Find the graphics window.
        self.assert_(len(OOF.Windows.Graphics.items)==2)
        for item in OOF.Windows.Graphics.items:
            if item.name[:8]=="Graphics":
                item_name=item.name
                break
        self.assert_(item_name is not None)
        # Get the corresponding item from the OOF menu.
        gw_item = OOF.__getattr__(item_name)
        gw_item.File.Close()
        self.assert_(len(OOF.Windows.Graphics.items)==1)
        self.assert_(not hasattr(OOF.Windows.Graphics, item_name))

    def tearDown(self):
        pass

# Tests of actual pixel selection operations.
# OOF.Toolbox.Pixel_Select items:
#   Point, Brush, Rectangle, Circle, Ellipse, Color, Burn.
# Selection modifiers from the same menu, Clear, Undo, Redo, Invert
class Direct_Pixel_Selection(unittest.TestCase):
    def setUp(self):
        global gfxmanager
        global pixelselection
        from ooflib.common.IO import gfxmanager
        from ooflib.common import pixelselection
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name=automatic,
            height=automatic, width=automatic, depth=automatic)
        OOF.Windows.Graphics.New()

    # Direct selection operations -- these are toolbox ops in the
    # graphics window.
    # Select circle, rectangle, ellipse, point.
    def Circle(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Circle(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0), Point(87.6,41.8)],
            shift=0, ctrl=0)
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        # Size should be 2000 pixels.
        self.assertEqual(ps.getObject().len(), 2000)

    # Makes and clears a selection.  Uses the circle selector, so
    # that one should be tested first.
    def Clear(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0, ctrl=0)
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        self.assertNotEqual(ps.getObject().len(), 0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source="slice.jpg.*:slice.jpg.*")
        self.assertEqual(ps.getObject().len(), 0)

    # Remining direct selection methods --
    # Point, Brush, Rectangle, Ellipse, Color, Burn.

    def Point(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(52.0, 70.0,60.0)], shift=0, ctrl=0)
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        # Size should be 1 pixel, of course.
        self.assertEqual(ps.getObject().len(), 1)
        psi = ps.getObject()
        self.assertEqual(psi.members(), [iPoint(52,70,60)])

    # Brush points were recorded from an actual user session.
    def Brush(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Brush(
            source='slice.jpg.*:slice.jpg.*',
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
        ps =  pixelselection.pixelselectionWhoClass['slice.jpg.*']
        self.assertEqual(ps.getObject().len(), 94)


    def Rectangle(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Rectangle(
            source='slice.jpg.*:slice.jpg.*',
            points=[Point(23.3,57.0), Point(123.0,24.75)],
            shift=0, ctrl=0)
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        self.assertEqual(ps.getObject().len(), 3434)
        
    def Ellipse(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Ellipse(
            source='slice.jpg.*:slice.jpg.*',
            points=[Point(23.3,57.0), Point(123.0,24.75)],
            shift=0, ctrl=0)
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        self.assertEqual(ps.getObject().len(), 2526)

    def Color(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Color(
            source='slice.jpg.*:slice.jpg.*',
            range=DeltaRGB(delta_red=0.3, delta_green=0.3, delta_blue=0.3),
            points=[Point(14.7,62.1)], shift=0, ctrl=0)
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        self.assertEqual(ps.getObject().len(), 330982)

    def Burn(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Burn(
            source='slice.jpg.*:slice.jpg.*',
            local_flammability=0.1,global_flammability=0.2,
            color_space_norm="L1", next_nearest=False,
            points=[Point(14.7,62.1)], shift=0, ctrl=0)
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        self.assertEqual(ps.getObject().len(), 333914)


    # Then, mechanical ones -- Undo, Redo, Invert.

    def Undo(self):
        ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
        self.assertEqual(ps.getObject().len(), 0)
        self.assert_(not ps.undoable())
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0, 44.0)],
            shift=0, ctrl=0)
        self.assert_(ps.undoable())
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        OOF.Graphics_1.Toolbox.Pixel_Select.Undo(
            source="slice.jpg.*:slice.jpg.*")
        ps_2_id = id(ps.getObject())
        self.assertEqual(ps_0_id, ps_2_id)
        self.assertEqual(ps.getObject().len(), 0)

    def Redo(self):
         ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
         ps_0_id = id(ps.getObject())
         OOF.Graphics_1.Toolbox.Pixel_Select.Point(
             source="slice.jpg.*:slice.jpg.*",
             points=[Point(66.0,55.0,44.0)],
             shift=0, ctrl=0)
         ps_1_id = id(ps.getObject())
         OOF.Graphics_1.Toolbox.Pixel_Select.Undo(
             source="slice.jpg.*:slice.jpg.*")
         self.assert_(ps.redoable())
         OOF.Graphics_1.Toolbox.Pixel_Select.Redo(
             source="slice.jpg.*:slice.jpg.*")
         self.assertEqual(id(ps.getObject()), ps_1_id)
         self.assert_(not ps.redoable())


    def Invert(self):
         OOF.Graphics_1.Toolbox.Pixel_Select.Point(
             source="slice.jpg.*:slice.jpg.*",
             points=[Point(66,55,44)],
             shift=0, ctrl=0)
         ps = pixelselection.pixelselectionWhoClass['slice.jpg.*']
         print ps.getObject().len()
         OOF.Graphics_1.Toolbox.Pixel_Select.Invert(
             source="slice.jpg.*:slice.jpg.*")
         # Magic number is total minus circle-selected number.
         print ps.getObject().len()
         self.assertEqual(ps.getObject().len(), 999999)
         

         
    def tearDown(self):
        OOF.Graphics_1.File.Close()
        OOF.Microstructure.Delete(microstructure="slice.jpg.*")
        

# Then pixel group creation/manipulation options.

# OOF.PixelGroup:
# New Rename Copy Delete Meshable AddSelection RemoveSelection Clear
# Query

# Pixel group creation/manipulation -- assume that selections are
# possible.  Also should test the autogroup from the image menu.
# These tests use the "small.ppm.*" image, which autogroups reasonably
# cleanly, rather than the more difficult slice.jpg.*.
class Pixel_Groups(unittest.TestCase):
    def setUp(self):
        global microstructure
        global gfxmanager
        global pixelselection
        from ooflib.common import microstructure
        from ooflib.common.IO import gfxmanager
        from ooflib.common import pixelselection
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","5color","slice*.tif"),
            microstructure_name=automatic,
            height=automatic, width=automatic, depth=automatic)
        OOF.Windows.Graphics.New()

    def AutoGroup(self):
        from ooflib.common import color
        def colordiff(c1,c2):
            return (c1.red-c2.red)**2 + \
                   (c1.green-c2.green)**2 + \
                   (c1.blue-c2.blue)**2
        # Dictionary of nearest pure colors and sizes of the
        # corresponding groups, which will not have exactly this
        # color, but will be closer to it than to any other color (in
        # colordiff measure).
        expected_sizes = {color.RGBColor(1.0,1.0,1.0) : 2385,
                          color.blue : 1205,
                          color.green : 1020,
                          color.yellow : 2313,
                          color.red : 1077 }

        OOF.Image.AutoGroup(image="slice*.tif:slice*.tif")
        ms = microstructure.getMicrostructure("slice*.tif")
        groups = ms.groupNames()
        self.assertEqual(len(groups), 5)
        for name in groups:
            rgb = eval(name)
            key = None
            diff = None
            for c in expected_sizes.keys():
                cdiff = colordiff(rgb,c)
                if (diff is None) or (cdiff < diff):
                    key = c
                    diff = cdiff
            self.assertEqual(len(ms.findGroup(name)), expected_sizes[key])
        
                            
    def New(self):
        OOF.PixelGroup.New(name="test", microstructure="slice*.tif")
        ms = microstructure.getMicrostructure("slice*.tif")
        groups = ms.groupNames()
        self.assertEqual(len(groups),1)
        self.assert_("test" in groups)

    def Delete(self):
        OOF.PixelGroup.New(name="test", microstructure="slice*.tif")
        ms = microstructure.getMicrostructure("slice*.tif")
        OOF.PixelGroup.Delete(microstructure="slice*.tif", group="test")
        groups = ms.groupNames()
        self.assertEqual(len(groups),0)

    # Uses "circle" selection.  Clear the selection before measuring
    # the size of the group.
    def AddSelection(self):
        OOF.PixelGroup.New(name="test", microstructure="slice*.tif")
        ms = microstructure.getMicrostructure("slice*.tif")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice*.tif:slice*.tif",
            points=[Point(15.0,15.0,15.0)],
            shift=0,ctrl=0)
        OOF.PixelGroup.AddSelection(
            microstructure="slice*.tif", group="test")
        ps = pixelselection.pixelselectionWhoClass['slice*.tif']
        sel_size = ps.getObject().len()
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source="slice*.tif:slice*.tif")
        group = ms.findGroup("test")
        self.assertEqual(len(group), sel_size)
        
    def RemoveSelection(self):
        OOF.PixelGroup.New(name="test", microstructure="slice*.tif")
        ms = microstructure.getMicrostructure("slice*.tif")
        ps = pixelselection.pixelselectionWhoClass['slice*.tif']
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice*.tif:slice*.tif",
            points=[Point(15.0,15.0,15.0)],
            shift=0,ctrl=0)
        sel_large = ps.getObject().len()
        OOF.PixelGroup.AddSelection(
            microstructure="slice*.tif", group="test")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice*.tif:slice*.tif",
            points=[Point(15.0,15.0,15.0)],
            shift=0,ctrl=0)
        sel_small = ps.getObject().len()
        OOF.PixelGroup.RemoveSelection(
            microstructure="slice*.tif", group="test")
        OOF.Graphics_1.Toolbox.Pixel_Select.Clear(
            source="slice*.tif:slice*.tif")
        group = ms.findGroup("test")
        self.assertEqual(len(group), sel_large-sel_small)

    def Copy(self):
        ms = microstructure.getMicrostructure("slice*.tif")
        OOF.PixelGroup.New(name="test", microstructure="slice*.tif")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice*.tif:slice*.tif",
            points=[Point(15.0,15.0,15.0)],
            shift=0,ctrl=0)
        OOF.PixelGroup.AddSelection(
            microstructure="slice*.tif", group="test")
        group = ms.findGroup("test")
        initial_group_size = len(group)
        OOF.PixelGroup.Copy(microstructure="slice*.tif",
                            group="test", name="testcopy")
        OOF.PixelGroup.Delete(microstructure="slice*.tif", group="test")
        self.assertEqual(ms.nGroups(), 1)
        group = ms.findGroup("testcopy")
        self.assertEqual(len(group), initial_group_size) 
        
    def Rename(self):
        ms = microstructure.getMicrostructure("slice*.tif")
        OOF.PixelGroup.New(name="test", microstructure="slice*.tif")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice*.tif:slice*.tif",
            points=[Point(15.0,15.0,15.0)],
            shift=0,ctrl=0)
        OOF.PixelGroup.AddSelection(
            microstructure="slice*.tif", group="test")
        group = ms.findGroup("test")
        initial_group_size = len(group)
        OOF.PixelGroup.Rename(microstructure="slice*.tif",
                              group="test", new_name="testrename")
        group = ms.findGroup("testrename")
        self.assertEqual(len(group), initial_group_size)
        # Still only one group.
        self.assertEqual(ms.nGroups(), 1)
        self.assert_( not "test" in ms.groupNames())
        

    # Meshable may be better tested at skel-mod time.
    # Query is just weird -- writes to stdout!
    
    def tearDown(self):
        OOF.Graphics_1.File.Close()
        OOF.Microstructure.Delete(microstructure="slice*.tif")


# Then pixel selection modifers.
# OOF.PixelSelection:
# Undo Redo Clear Invert Select_Group Add_Group Unselect_Group
# Intersect_Group Despeckle Elkcepsed Expand Shrink Color_Range Copy

## Tests for Select_Element_Pixels and Select_Segment_Pixels are in
## skeleton_extra_test.py, the test for Select_Material is in
## pixel_extra_test.py.

class Selection_Modify(unittest.TestCase):
    def setUp(self):
        global microstructure
        global gfxmanager
        global pixelselection
        from ooflib.common import microstructure
        from ooflib.common.IO import gfxmanager
        from ooflib.common import pixelselection
        OOF.Microstructure.Create_From_ImageFile(
            filename=os.path.join("ms_data","jpeg","slice.jpg.*"),
            microstructure_name=automatic,
            height=automatic, width=automatic, depth=automatic)
        OOF.Windows.Graphics.New()

    # A lot of the obvious checks are already done in the undo test in
    # Direct_Pixel_Selection.
    def Undo(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        ps_1_id = id(ps.getObject())
        OOF.PixelSelection.Undo(microstructure="slice.jpg.*")
        ps_2_id = id(ps.getObject())
        self.assertEqual(ps_2_id, ps_0_id)
        self.assertNotEqual(ps_2_id, ps_1_id)

    def Redo(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        ps_1_id = id(ps.getObject())
        OOF.PixelSelection.Undo(microstructure="slice.jpg.*")
        OOF.PixelSelection.Redo(microstructure="slice.jpg.*")
        ps_2_id = id(ps.getObject())
        self.assert_(not ps.redoable())
        self.assertEqual(ps_2_id, ps_1_id)
        self.assertNotEqual(ps_2_id, ps_0_id)

    def Clear(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        ps_0_id = id(ps.getObject())
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        OOF.PixelSelection.Clear(microstructure="slice.jpg.*")
        ps_1_id = id(ps.getObject())
        self.assertEqual(ps.getObject().len(), 0)
        self.assertNotEqual(ps_0_id, ps_1_id)

    def Invert(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        OOF.PixelSelection.Invert(microstructure="slice.jpg.*")
        self.assertEqual(ps.getObject().len(), 999999)

    def Copy(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        OOF.Microstructure.Copy(microstructure="slice.jpg.*", name="copy")
        copy_ps = pixelselection.pixelselectionWhoClass["copy"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        self.assertEqual(copy_ps.getObject().len(), 0)
        OOF.PixelSelection.Copy(microstructure="copy",
                                source="slice.jpg.*")
        self.assertEqual(copy_ps.getObject().len(),
                         ps.getObject().len())
        OOF.Microstructure.Delete(microstructure="copy")

    def Select_Group(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelGroup.New(name="test", microstructure="slice.jpg.*")
        OOF.PixelGroup.AddSelection(microstructure="slice.jpg.*", group="test")
        OOF.PixelSelection.Undo(microstructure="slice.jpg.*")
        OOF.PixelSelection.Select_Group(microstructure="slice.jpg.*", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(), 1)

    def Add_Group(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        OOF.PixelGroup.New(name="test", microstructure="slice.jpg.*")
        OOF.PixelGroup.AddSelection(microstructure="slice.jpg.*", group="test")
        OOF.PixelSelection.Undo(microstructure="slice.jpg.*")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(57.0,84.0,99.0)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelSelection.Add_Group(microstructure="slice.jpg.*", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(), 2)
        
    def Unselect_Group(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        OOF.PixelGroup.New(name="test", microstructure="slice.jpg.*")
        OOF.PixelGroup.AddSelection(microstructure="slice.jpg.*", group="test")
        OOF.PixelSelection.Undo(microstructure="slice.jpg.*")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(57.0,84.0,99.0)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelSelection.Unselect_Group(
            microstructure="slice.jpg.*", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(),1)
        
    def Intersect_Group(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        OOF.PixelGroup.New(name="test", microstructure="slice.jpg.*")
        OOF.PixelGroup.AddSelection(microstructure="slice.jpg.*", group="test")
        OOF.PixelSelection.Undo(microstructure="slice.jpg.*")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(57.0,84.0), Point(67.0, 70.0)],
            shift=0,ctrl=0)
        ps_0_id = id(ps.getObject())
        OOF.PixelSelection.Intersect_Group(
            microstructure="slice.jpg.*", group="test")
        ps_1_id = id(ps.getObject())
        self.assertNotEqual(ps_0_id, ps_1_id)
        self.assertEqual(ps.getObject().len(), 238)

    # Helper function, to make a selection suitable for use
    # by the Despeckle, Ekcepsed, Expand, and Shrink tests.
    
    def select_helper(self):
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(36.0, 81.0), Point(47.5,72.0)],
            shift=0,ctrl=0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(37.0, 64.5)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(53.0, 81.0)],
            shift=1, ctrl=0)
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(36.0, 81.0)],
            shift=0, ctrl=1)
            
        
        
    def Despeckle(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Despeckle(microstructure="slice.jpg.*",
                                     neighbors=8)
        self.assertEqual(ps.getObject().len(), 682)


    def Elkcepsed(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Elkcepsed(microstructure="slice.jpg.*",
                                     neighbors=3)
        self.assertEqual(ps.getObject().len(), 679)

    def Expand(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Expand(microstructure="slice.jpg.*",
                                     radius=1.0)
        self.assertEqual(ps.getObject().len(), 773)

    def Shrink(self): # You can't disintegrate me!!
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        self.select_helper()
        self.assertEqual(ps.getObject().len(), 681)
        OOF.PixelSelection.Shrink(microstructure="slice.jpg.*",
                                     radius=1.0)
        self.assertEqual(ps.getObject().len(), 595)


    # Color range is a selector, not really a modifer, but there you go.
    def Color_Range(self):
        ps = pixelselection.pixelselectionWhoClass["slice.jpg.*"]
        OOF.PixelSelection.Color_Range(
            microstructure="slice.jpg.*", image="slice.jpg.*:slice.jpg.*",
            reference=RGBColor(red=0.0,green=0.0,blue=0.0),
            range=DeltaRGB(delta_red=1.0,delta_green=0.0,delta_blue=1.0))
        self.assertEqual(ps.getObject().len(), 8306)
           


    # Element and segment ops can't be tested until skeletons exist.

    # Rich_MS_Copy is a test of the microstructure copying process now
    # that nontrivial groups and selections can be made -- these
    # should survive the copy process.  The magic numbers come from
    # the autogroup and circle-selection tests, also in this file.
    def Rich_MS_Copy(self):
        from ooflib.common import color
        OOF.Image.AutoGroup(image="slice.jpg.*:slice.jpg.*")
        OOF.Graphics_1.Toolbox.Pixel_Select.Point(
            source="slice.jpg.*:slice.jpg.*",
            points=[Point(66.0,55.0,44.0)],
            shift=0,ctrl=0)
        OOF.Microstructure.Copy(microstructure="slice.jpg.*",
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
            rgb = eval(name)
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
        OOF.Microstructure.Delete(microstructure="slice.jpg.*")


    

    
# Routine to do regression-type testing on the items in this file.
# Tests must be run in the order they appear in the list.  This
# routine will stop after the first failure.
def run_tests():
    test_set = [
        Graphics_Ops("New"),
        Graphics_Ops("Close"),
        #Direct_Pixel_Selection("Circle"),
        Direct_Pixel_Selection("Clear"),
        Direct_Pixel_Selection("Point"),
        #Direct_Pixel_Selection("Brush"),
        #Direct_Pixel_Selection("Rectangle"),
        #Direct_Pixel_Selection("Ellipse"),
        Direct_Pixel_Selection("Color"),
        Direct_Pixel_Selection("Burn"),
        Direct_Pixel_Selection("Undo"),
        Direct_Pixel_Selection("Redo"),
        Direct_Pixel_Selection("Invert"),
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
        #Selection_Modify("Intersect_Group"),
        #Selection_Modify("Despeckle"),
        #Selection_Modify("Elkcepsed"),
        #Selection_Modify("Expand"),
        #Selection_Modify("Shrink"),
        #Selection_Modify("Color_Range"),
        #Selection_Modify("Rich_MS_Copy")
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
