# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

# Test suite for the menu commands under OOF.Skeleton.*
# Namely, New, Simple, Delete, Copy, Rename, Modify, Undo,
# Redo, but not including PinNodes or Boundary, which are done in
# other files.  These basic commands, particularly modify, have
# variability in their results as the code evolves, so they've
# been separated out.

# This file assumes that microstructures, images, and pixel group
# menu items have all been tested and work.

import unittest, os
from . import memorycheck
from .UTILS.file_utils import reference_file

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

def getHomogIndex(msname, skelname, factor=0.5, minimumTileSize=5, bins=0):
    ms = getMicrostructure(msname)
    # If bins is non-zero, factor and minimumTileSize aren't used.  If
    # bins is zero, factor and minimumTileSize are used to create the
    # hierarchical tiling of pixel set boundaries.
    OOF.Microstructure.SetHomogeneityParameters(
        factor=factor, minimumTileSize=minimumTileSize,
        fixedSubdivision=bins)
    OOF.Microstructure.Recategorize(microstructure=msname)
    skelctxt = skeletoncontext.skeletonContexts[msname + ":" +skelname]
    homog = skelctxt.getObject().getHomogeneityIndex()
    # Reset the homogeneity parameters to keep this test from
    # affecting the results of future tests.
    OOF.Microstructure.ResetHomogeneityParameters()
    return homog

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class OOF_Skeleton(unittest.TestCase):
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

    @memorycheck.check("skeltest")
    def New(self):
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 0)
        from ooflib.common.IO import parameter
        self.assertRaises(
            parameter.ParameterMismatch,
            OOF.Skeleton.New,
            name="mis:punctuated", microstructure="skeltest",
            x_elements=8,y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        OOF.Skeleton.New(
            name="skeleton", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 1)
        skelctxt = skeletoncontext.skeletonContexts["skeltest:skeleton"]
        skel = skelctxt.getObject()
        self.assertEqual(skel.nnodes(), 81)
        self.assertEqual(skel.nelements(), 64)
        self.assertTrue(skel.sanity_check())
        
    @memorycheck.check("skeltest")
    def NewTri(self):
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 0)
        OOF.Skeleton.New(
            name="skeleton", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=TriSkeleton(arrangement="conservative",
                                          top_bottom_periodicity=False,
                                          left_right_periodicity=False))
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 1)
        skelctxt = skeletoncontext.skeletonContexts["skeltest:skeleton"]
        skel = skelctxt.getObject()
        self.assertEqual(skel.nnodes(), 81)
        self.assertEqual(skel.nelements(), 128)
        self.assertTrue(skel.sanity_check())

    @memorycheck.check("skeltest")
    def Delete(self):
        OOF.Skeleton.New(
            name="skeleton", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        OOF.Skeleton.Delete(skeleton="skeltest:skeleton")
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 0)

    @memorycheck.check("skeltest")
    def Simple(self):
        OOF.Skeleton.Simple(
            name="simple", microstructure="skeltest",
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 1)
        skelctxt = skeletoncontext.skeletonContexts["skeltest:simple"]
        skel = skelctxt.getObject()
        self.assertEqual(skel.nelements(), 22500)
        self.assertEqual(skel.nnodes(), 22801)
        # No sanity check here, because it takes too long.  The simple
        # skeleton uses the same code as the regular skeleton, so
        # checking shouldn't be necessary.

    @memorycheck.check("skeltest")
    def SimpleTri(self):
        OOF.Skeleton.Simple(
            name='simple', microstructure='skeltest',
            skeleton_geometry=TriSkeleton(arrangement='moderate',
                                          left_right_periodicity=False,
                                          top_bottom_periodicity=False))
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 1)
        skelctxt = skeletoncontext.skeletonContexts["skeltest:simple"]
        skel = skelctxt.getObject()
        self.assertEqual(skel.nelements(), 45000)
        self.assertEqual(skel.nnodes(), 22801)
        # No sanity check here, because it takes too long.  The simple
        # skeleton uses the same code as the regular skeleton, so
        # checking shouldn't be necessary.

    @memorycheck.check("skeltest")
    def Copy(self):
        OOF.Skeleton.New(
            name="skeleton", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        OOF.Skeleton.Copy(skeleton="skeltest:skeleton",
                          name="copy")
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 2)
        skelctxt = skeletoncontext.skeletonContexts["skeltest:copy"]
        skel = skelctxt.getObject()
        self.assertEqual(skel.nnodes(), 81)
        self.assertEqual(skel.nelements(), 64)
        self.assertTrue(skel.sanity_check())
        OOF.Skeleton.Delete(skeleton="skeltest:copy")

    @memorycheck.check("skeltest")
    def Rename(self):
        OOF.Skeleton.New(
            name="skeleton", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        OOF.Skeleton.Rename(skeleton="skeltest:skeleton",
                            name="rename")
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 1)
        skelctxt = skeletoncontext.skeletonContexts["skeltest:rename"]
        skel = skelctxt.getObject()
        self.assertEqual(skel.nnodes(), 81)
        self.assertEqual(skel.nelements(), 64)
        self.assertTrue(skel.sanity_check())

    @memorycheck.check("skeltest")
    def Save(self):
        import os, filecmp
        OOF.Skeleton.New(
            name="savetest", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        OOF.File.Save.Skeleton(filename="skeleton_save",
                               mode="w", format="ascii",
                               skeleton="skeltest:savetest")
        self.assertTrue(filecmp.cmp(reference_file("skeleton_data",
                                              "savetest"),
                                 "skeleton_save"))
        os.remove("skeleton_save")

    @memorycheck.check("skeltest")
    def Load(self):
        OOF.File.Load.Data(filename=reference_file("skeleton_data",
                                                 "savetest"))
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 1)
        self.assertTrue( ["skeltest", "savetest"] in
                         skeletoncontext.skeletonContexts.keys())
        skelctxt = skeletoncontext.skeletonContexts["skeltest:savetest"]
        skel = skelctxt.getObject()
        self.assertEqual(skel.nnodes(), 81)
        self.assertEqual(skel.nelements(), 64)
        self.assertTrue(skel.sanity_check())

    @memorycheck.check("skeltest")
    def Homogeneity(self):
        # Check that different binning schemes give the same
        # homogeneity.
        # Create a uniform NxN skeleton for each N in skelsizes
        skelsizes = (1, 2, 4, 10, 20)
        # Test each skeleton with an MxM tiling for each M in ntiles.
        ntiles = (2, 5, 10, 20, 100)
        # Skeleton geometries to test
        geometries = (QuadSkeleton(top_bottom_periodicity=False,
                                   left_right_periodicity=False),
                      TriSkeleton(arrangement='moderate',
                                  top_bottom_periodicity=False,
                                  left_right_periodicity=False))
        for geometry in geometries:
            for skelsize in skelsizes:
                OOF.Skeleton.New(
                    name='htest', microstructure='skeltest',
                    x_elements=skelsize, y_elements=skelsize,
                    skeleton_geometry=geometry)
                h0 = getHomogIndex("skeltest", "htest", bins=1)
                print("   bins=0, h=", h0, file=sys.stderr)
                for nbins in ntiles:
                    h = getHomogIndex("skeltest", "htest", bins=nbins)
                    print("   bins=", nbins, "h=", h, "delta=", \
                        h-h0, file=sys.stderr)
                    self.assertAlmostEqual(h, h0, 10)
                OOF.Skeleton.Delete(skeleton="skeltest:htest")
    #     self.testHomogeneityUniform(
    #         TriSkeleton(arrangement='moderate',
    #                     top_bottom_periodicity=False,
    #                     left_right_periodicity=False),
    #         skelsizes, ntiles)

    # def testHomogeneityUniform(self, skelgeom, skelsizes, ntiles):
    #     for skelsize in skelsizes:
    #         OOF.Skeleton.New(
    #             name="htest", microstructure="skeltest",
    #             x_elements=skelsize, y_elements=skelsize,
    #             skeleton_geometry=skelgeom)
    #         h0 = getHomogIndex("skeltest", "htest", bins=1)
    #         print >> sys.stderr, "Homogeneity Check: skelsize=", skelsize
    #         print >> sys.stderr, "  bins=0, h=", h0
    #         for bins in ntiles:
    #             h = getHomogIndex("skeltest", "htest", bins=bins)
    #             print >> sys.stderr, "  bins=", bins, "h=", h, "delta=", h-h0
    #             self.assertAlmostEqual(h, h0, 10);
    #         OOF.Skeleton.Delete(skeleton="skeltest:htest")
                    
        
    @memorycheck.check("skeltest")
    def doModify(self, registration, startfile, compfile, kwargs):
        import os, random
        from ooflib.SWIG.common import crandom
        # Loaded skeleton must be named "modtest".
        OOF.File.Load.Data(filename=reference_file("skeleton_data", startfile))
        mod = registration(**kwargs)
        random.seed(17)
        crandom.rndmseed(17)
        OOF.Skeleton.Modify(skeleton="skeltest:modtest", modifier=mod)
        skelc = skeletoncontext.skeletonContexts["skeltest:modtest"]
        self.assertTrue(skelc.getObject().sanity_check())
        # Saving and reloading the Skeleton guarantees that node
        # indices match up with the reference skeleton.  Nodes are
        # re-indexed when a skeleton is saved.
        OOF.File.Save.Skeleton(
            filename="skeleton_mod_test",
            mode="w", format="ascii",
            skeleton="skeltest:modtest")
        OOF.Skeleton.Delete(skeleton="skeltest:modtest")
        OOF.File.Load.Data(filename="skeleton_mod_test")
        # Saved skeleton is named "skelcomp:reference".
        OOF.File.Load.Data(
            filename=reference_file("skeleton_data",
                                  compfile))
        sk1 = skeletoncontext.skeletonContexts[
            "skeltest:modtest"].getObject()
        sk2 = skeletoncontext.skeletonContexts[
            "skelcomp:reference"].getObject()
        # Tolerance is 1.0e-13, 100x double-precision noise.
        ## After switching to Eigen 3.3.9 it was necessary to increase
        ## the tolerance to get the new calculations to "agree" with
        ## the old reference files for the Relax test.  
        ## TODO: Recompute the reference files.
        self.assertEqual(sk1.compare(sk2, 1.0e-6), 0)
        os.remove("skeleton_mod_test")
        OOF.Skeleton.Delete(skeleton="skeltest:modtest")
        OOF.Skeleton.Delete(skeleton="skelcomp:reference")
        OOF.Microstructure.Delete(microstructure="skelcomp")

    # This is a modify pass which may be considered preliminary -- the
    # only possible target is "AllNodes", because we do not yet know
    # that we can make selections, or pin nodes, or anything.
    def Modify(self):
        from ooflib.engine import skeletonmodifier
        for r in skeletonmodifier.SkeletonModifier.registry:
            try:
                mods = skel_modify_args[r.name()]
            except KeyError:
                print("No data for skeleton modifier %s." % r.name(), file=sys.stderr)
            else:
                print("Testing", r.name(), file=sys.stderr)
                for (startfile, compfile, kwargs) in mods:
                    self.doModify(r, startfile, compfile, kwargs)

    @memorycheck.check("skeltest")
    def Undo(self):
        from ooflib.engine import skeletoncontext
        OOF.Skeleton.New(
            name="undotest", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        sk_context = skeletoncontext.skeletonContexts["skeltest:undotest"]
        sk_0 = sk_context.getObject()
        self.assertTrue(not sk_context.undoable())
        OOF.Skeleton.Modify(skeleton="skeltest:undotest",
                            modifier=Refine(
            targets=CheckHomogeneity(threshold=0.9),
            criterion=Unconditionally(),
            degree=Trisection(rule_set="conservative")))
        sk_1 = sk_context.getObject()
        self.assertTrue(sk_context.undoable())
        self.assertNotEqual(id(sk_0),id(sk_1))
        OOF.Skeleton.Undo(skeleton="skeltest:undotest")
        sk_2 = sk_context.getObject()
        self.assertEqual(id(sk_0), id(sk_2))


    @memorycheck.check("skeltest")
    def Redo(self):
        from ooflib.engine import skeletoncontext
        OOF.Skeleton.New(
            name="redotest", microstructure="skeltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        sk_context = skeletoncontext.skeletonContexts["skeltest:redotest"]
        sk_0 = sk_context.getObject()
        OOF.Skeleton.Modify(skeleton="skeltest:redotest",
                            modifier=Refine(
            targets=CheckHomogeneity(threshold=0.9),
            criterion=Unconditionally(),
            degree=Trisection(rule_set="conservative")))
        sk_1 = sk_context.getObject()
        OOF.Skeleton.Undo(skeleton="skeltest:redotest")
        sk_2 = sk_context.getObject()
        OOF.Skeleton.Redo(skeleton="skeltest:redotest")
        self.assertEqual(id(sk_1),id(sk_context.getObject()))
        self.assertTrue(not sk_context.redoable())

    def tearDown(self):
         pass

# Extra tests that can't be in OOF_Skeleton for one reason or another.

class OOF_Skeleton_Special(unittest.TestCase):
    def setUp(self):
        global skeletoncontext
        from ooflib.engine import skeletoncontext
        global microstructure
        from ooflib.common import microstructure
        global imagecontext
        from ooflib.image import imagecontext

    def tearDown(self):
        pass

    # Now that skeletons are known to work, we can test if deleting a
    # microstructure which contains a skeleton does the right thing.
    # This test is pretty much redundant with the tests inserted by
    # the memorycheck decorator.

    def MS_Delete(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file("ms_data","small.ppm"),
            microstructure_name="deltest",
            height=20.0, width=20.0)
        OOF.Image.AutoGroup(image="deltest:small.ppm")
        OOF.Skeleton.New(
            name="skeleton", microstructure="deltest",
            x_elements=8, y_elements=8,
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 1)
        OOF.Microstructure.Delete(microstructure="deltest")
        self.assertEqual(microstructure.microStructures.nActual(), 0)
        self.assertEqual(skeletoncontext.skeletonContexts.nActual(), 0)
        self.assertEqual(imagecontext.imageContexts.nActual(), 0)
        self.assertEqual(cskeleton.get_globalNodeCount(), 0)
        self.assertEqual(cskeleton.get_globalElementCount(), 0)
        self.assertEqual(cmicrostructure.get_globalMicrostructureCount(), 0)

    # Check that round-off error isn't making nodes that should be on
    # a boundary appear to be off the boundary.  This can't be done as
    # part of the other tests, because it requires a special
    # Microstructure size.  (This bug was reported by Tobias Ziegler
    # in version 2.0.1.)
    
    @memorycheck.check("roundoff")
    def RoundOff(self):
        OOF.Microstructure.New(name='roundoff',
                               width=0.0067400000000000003, # magic number
                               height=0.0067400000000000003,
                               width_in_pixels=10, height_in_pixels=10)
        OOF.Skeleton.New(
            name='skeleton', microstructure='roundoff',
            x_elements=22, y_elements=22, # magic number
            skeleton_geometry=QuadSkeleton(top_bottom_periodicity=False,
                                           left_right_periodicity=False))
        skelctxt = skeletoncontext.skeletonContexts['roundoff:skeleton']
        skel = skelctxt.getObject()
        #  Node 512 on the top boundary should be able to move in x only.
        node = skel.getNode(512)
        print("x:", node.movable_x(), "y:", node.movable_y(), file=sys.stderr)
        self.assertTrue(node.movable_x() and not node.movable_y())
        # Node 367 on the right boundary should be able to move in y only.
        node = skel.getNode(367)
        self.assertTrue(node.movable_y() and not node.movable_x())

    @memorycheck.check("checkerboard.pgm")
    def CheckerBoard(self):
        OOF.Microstructure.Create_From_ImageFile(
            filename=reference_file('ms_data','checkerboard.pgm'),
            microstructure_name='checkerboard.pgm',
            height=20, width=10)
        OOF.Image.AutoGroup(
            image='checkerboard.pgm:checkerboard.pgm',
            name_template='%c')
        OOF.Skeleton.New(
            name='skeleton',
            microstructure='checkerboard.pgm',
            x_elements=3, y_elements=3,
            skeleton_geometry=TriSkeleton(
                arrangement='moderate',
                left_right_periodicity=False,top_bottom_periodicity=False))
        skelctxt = skeletoncontext.skeletonContexts['checkerboard.pgm:skeleton']
        skel = skelctxt.getObject()
        ms = skelctxt.getMicrostructure()
        for eidx in range(18):
            el = skel.getElement(eidx)
            homog = el.homogeneity(ms, False)
            self.assertAlmostEqual(homog, 0.5, 6)

    @memorycheck.check("mess")
    def MessyHomogeneity(self):
        # Check that different binning schemes give the same
        # homogeneity on a very inhomogeneous skeleton.
        OOF.File.Load.Data(
            filename=reference_file("skeleton_data", 'messyskel.dat'))
        ntiles = (2, 3, 4, 5, 10, 20, 50, 100)
        h0 = getHomogIndex("mess", "skeleton", bins=1)
        for nt in ntiles:
            h = getHomogIndex("mess", "skeleton", bins=nt)
            print("  nt=", nt, "h=", h, "delta=", h-h0, file=sys.stderr)
            self.assertAlmostEqual(h0, h, 2)
        # Check with automatic, hierarchical tiling
        factors = (0.1, 0.5, 0.7, 0.9)
        minTiles = (2, 5, 10, 20, 50, 100)
        for minTile in minTiles:
            for factor in factors:
                h = getHomogIndex("mess", "skeleton", factor=factor,
                                  minimumTileSize=minTile, bins=0)
                print("  factor=", factor, "minTile=", minTile, \
                    "h=", h, "delta=", h-h0, file=sys.stderr)
                self.assertAlmostEqual(h0, h, 2)

        
# Data for the skeleton modifier tests.  This is a dictionary indexed by
# skeleton modifier name, and for each modifier, there is a set of
# arguments to supply to the modifier menu item for the test, and the
# name of a file containing correct results for that test.
skel_modify_args = {}
def build_mod_args():
    global skel_modify_args
    skel_modify_args = {
        "Refine" :
        [
        ("modbase", "refine_1",
         { "targets" : CheckHomogeneity(threshold=0.9),
           "criterion" : Unconditionally(),
           "degree" : Trisection(rule_set="conservative"),
           "alpha" : 0.5
           }
         ),
        ("modbase", "refine_2",
         { "targets" : CheckHomogeneity(threshold=0.9),
           "criterion" : Unconditionally(),
           "degree" : Bisection(rule_set="conservative"),
           "alpha" : 0.5
           }
         ),
        ("modgroups","refine_3",
         {"targets" : CheckElementsInGroup(group='elementgroup'),
          "criterion" : Unconditionally(),
          "degree" : Bisection(rule_set="conservative"),
          "alpha" : 0.5
          }
         ),
        ("modgroups","refine_4",
         {"targets" : CheckAllElements(),
          "criterion" : Unconditionally(),
          "degree" : Bisection(rule_set="conservative"),
          "alpha" : 0.5
          }
         ),
        ("modgroups","refine_5",
         {"targets" : CheckAspectRatio(threshold=1.5),
          "criterion" : Unconditionally(),
          "degree" : Bisection(rule_set="conservative"),
          "alpha" : 0.5
          }
         ),
        ("modgroups","refine_6",
         {"targets" : CheckHeterogeneousEdges(threshold=1,
                                              choose_from=FromAllSegments()),
          "criterion" : Unconditionally(),
          "degree" : Bisection(rule_set="conservative"),
          "alpha" : 0.5
          }
         )
        ],
        "Relax" :
        [
        ("modbase", "relax",
         { "alpha" : 0.5,
           "gamma" : 0.5,
           "iterations" : 1
           }
         )
        ],
        "Snap Nodes" :
        [ ("modbase", "snapnodes",
           { "targets" : SnapAll(),
             "criterion" : AverageEnergy(alpha=1.)
             }
           )
          ],
        "Split Quads" :
        [ ("modbase", "splitquads",
           { "targets" : AllElements(),
             "criterion" : AverageEnergy(alpha=0.9),
             "split_how" : GeographicQ2T()
             }
           )
          ],
        "Anneal" :
        [
        ("modbase", "anneal",
         {"targets" : AllNodes(),
          "criterion" : AverageEnergy(alpha=0.6),
          "T" : 0.0,
          "delta" : 1.0,
          "iteration" : FixedIteration(iterations=5)            
          }
         ),
        ("modgroups", "anneal_2",
         {"targets" : NodesInGroup(group='nodegroup'),
          "criterion" : AverageEnergy(alpha=0.6),
          "T" : 0.0,
          "delta" : 1.0,
          "iteration" : FixedIteration(iterations=5)            
          }
         ),
        ("modgroups", "anneal_3",
         {"targets" : FiddleElementsInGroup(group='elementgroup'),
          "criterion" : AverageEnergy(alpha=0.6),
          "T" : 0.0,
          "delta" : 1.0,
          "iteration" : FixedIteration(iterations=5)            
          }
         ),
        ("modgroups", "anneal_4",
         {"targets" : FiddleHeterogeneousElements(threshold=0.95),
          "criterion" : AverageEnergy(alpha=0.6),
          "T" : 0.0,
          "delta" : 1.0,
          "iteration" : FixedIteration(iterations=5)            
          }
         )
        ],
        "Smooth" :
        [ ("modsecond", "smooth",
           {"targets" : AllNodes(),
            "criterion" : AverageEnergy(alpha=0.3),
            "T" : 0.0,
            "iteration" : FixedIteration(iterations=5)
            }
           )
          ],
        "Swap Edges" :
        [ ("modsecond", "swapedges",
           {"targets" : AllElements(),
            "criterion" : AverageEnergy(alpha=0.3)
            }
           )
          ],
        "Merge Triangles" :
        [ ("modsecond", "mergetriangles",
           {"targets" : AllElements(),
            "criterion" : AverageEnergy(alpha=0.3)
            }
           )
          ],
        "Rationalize" :
        [ ("modsecond", "rationalize",
           {"targets" : AllElements(),
            "criterion" : AverageEnergy(alpha=0.3),
            "method" : SpecificRationalization(
        rationalizers=[RemoveShortSide(ratio=5.0),
                       QuadSplit(angle=150),
                       RemoveBadTriangle(acute_angle=30,obtuse_angle=130)]),
            "iterations" : 3
            }
           )
          ],
        #For snaprefine_3 and snaprefine_5, if we used modgroups,
        #then there would be a difference in results between
        #32 and 64 bit machines.
        "Snap Refine" :
        [
        ("modbase", "snaprefine_1",
         { "targets" : CheckHomogeneity(threshold=0.9),
           "criterion" : Unconditionally(),
           "min_distance" : 0.01,
           }
         ),
        ("modgroups","snaprefine_2",
         {"targets" : CheckElementsInGroup(group='elementgroup'),
          "criterion" : Unconditionally(),
          "min_distance" : 1.0,
          }
         ),
        ("modgroups2","snaprefine_3",
         {"targets" : CheckAllElements(),
          "criterion" : Unconditionally(),
          "min_distance" : 1.0,
          }
         ),
        ("modgroups","snaprefine_4",
         {"targets" : CheckAspectRatio(threshold=1.5),
          "criterion" : Unconditionally(),
          "min_distance" : 0.01,
          }
         ),
        ("modgroups2","snaprefine_5",
         {"targets" : CheckHeterogeneousEdges(threshold=1,
                                              choose_from=FromAllSegments()),
          "criterion" : Unconditionally(),
          "min_distance" : 1.0,
          }
         )
        ],
        "Fix Illegal Elements" :
        [
            ("illegal_skeleton", "illegal_fixed", {})
        ]
    }

    # skel_modify_args = {
    #     "Relax" :
    #         [
    #         ("modbase", "relax",
    #          { "alpha" : 0.5,
    #            "gamma" : 0.5,
    #            "iterations" : 1
    #            }
    #          )
    #         ],
    # }

def initialize():
    build_mod_args()

skel_set = [
    OOF_Skeleton("New"),
    OOF_Skeleton("NewTri"),        
    OOF_Skeleton("Delete"),
    OOF_Skeleton("Simple"),
    OOF_Skeleton("SimpleTri"),
    OOF_Skeleton("Copy"),
    OOF_Skeleton("Rename"),
    OOF_Skeleton("Save"),
    OOF_Skeleton("Load"),
    OOF_Skeleton("Homogeneity"),
    OOF_Skeleton("Modify"),
    OOF_Skeleton("Undo"),
    OOF_Skeleton("Redo")
    ]

special_set = [
    OOF_Skeleton_Special("MS_Delete"),
    OOF_Skeleton_Special("RoundOff"),
    OOF_Skeleton_Special("CheckerBoard"),
    OOF_Skeleton_Special("MessyHomogeneity"),
    ]

test_set = skel_set + special_set
