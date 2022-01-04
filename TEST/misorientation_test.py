# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest, os
import memorycheck

class OOF_Misorientation(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @memorycheck.check()
    def Oh(self):
        # Check that an orientation testAngle degrees off of the x
        # axis in the xy plane is testAngle degrees off of any
        # equivalent cubic ("Oh") orientation.
        testAngle = 5.0
        orient0 = Abg(alpha=0, beta=5., gamma=0)
        symOrient = []
        for axis in ((1, 0, 0), (0, 1, 0), (0, 0, 1),
                     (-1, 0, 0), (0, -1, 0), (0, 0, -1)):
            for angle in (0, 90, 180, -90):
                symOrient.append(Axis(angle=angle,
                                      x=axis[0], y=axis[1], z=axis[2]))
        for groupNo in range(221, 231):
            # Testing all of the space groups in the range 221-230 is
            # sort of silly because they all correspond to the same
            # point group (Oh, m-3m).
            spaceGroup = SpaceGroup(number=groupNo)
            for orient1 in symOrient:
                misor = orient1.misorientation(orient0,
                                               spaceGroup.schoenflies())
                self.assertAlmostEqual(misor, testAngle, 7)
                misor = orient0.misorientation(orient1,
                                               spaceGroup.schoenflies())
                self.assertAlmostEqual(misor, testAngle, 7)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=

test_set = [
    OOF_Misorientation("Oh")
]

