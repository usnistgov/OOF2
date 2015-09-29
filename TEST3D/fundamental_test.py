# -*- python -*-
# $RCSfile: fundamental_test.py,v $
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

# This is nearly the same as 2d version.

import unittest, os

class OOF_Fundamental(unittest.TestCase):
    def OrderedDict(self):
        from ooflib.common.utils import OrderedDict
        od = OrderedDict();
        od['a'] = 'hey'
        od['c'] = 'sea'
        od['b'] = 'bee'
        od['d'] = 'dee'
        vals = []
        for key,val in od.items():
            vals.append(val)
        self.assertEqual(vals, ['hey', 'sea', 'bee', 'dee'])
        od.reorder(['a', 'b', 'c'])
        vals = []
        for key,val in od.items():
            vals.append(val)
        self.assertEqual(vals, ['hey', 'bee', 'sea', 'dee'])
        
    def Ordered_Set(self):
        from ooflib.common.utils import OrderedSet
        os1 = OrderedSet([1,3,2,4])
        self.assertEqual([x for x in os1], [1,3,2,4])
        os1.add(1)
        self.assertEqual([x for x in os1], [1,3,2,4])
        self.assert_(3 in os1)
        self.assert_(5 not in os1)
        os1.discard(3)
        self.assertEqual([x for x in os1], [1,2,4])
        os1.discard(3)
        self.assertEqual([x for x in os1], [1,2,4])
        self.assertRaises(KeyError, os1.remove, 3)
        os2 = OrderedSet([4,2,7,1])
        union1 = os1 | os2
        self.assertEqual([x for x in union1], [1,2,4,7])
        union2 = os2 | os1
        self.assertEqual([x for x in union2], [4,2,7,1])
        inter1 = os1 & os2
        self.assertEqual([x for x in inter1], [1,2,4])
        inter2 = os2 & os1
        self.assertEqual([x for x in inter2], [4,2,1])
        self.assertEqual(os1, OrderedSet([1,2,4]))
        self.assertNotEqual(os1, os2)

def run_tests():
    test_set = [
        OOF_Fundamental("OrderedDict"),
        OOF_Fundamental("Ordered_Set")
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
