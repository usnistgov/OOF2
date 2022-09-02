# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest, os

# For reasons that I don't completely understand, file_utils needs to
# be imported with an absolute path name, or else the modules imported
# here and in regression.py will have different __name__'s.  That
# means that the second import (this one) will re-run the commands in
# the file, and reset file_utils.referencedir.
from oof2.TEST.UTILS.file_utils import reference_file

class OOF_Fundamental(unittest.TestCase):
    def setUp(self):
        global allWorkers, allWorkerCores
        from ooflib.common.worker import allWorkers, allWorkerCores
        from ooflib.common import utils
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
        self.assertTrue(3 in os1)
        self.assertTrue(5 not in os1)
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

    def WorkerCleanup(self):
        # Check that worker is destroyed after successful completion
        # of its task.
        from ooflib.SWIG.common import ooferror
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        OOF.Help.Debug.NoOp()
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)

    def WorkerException0(self):
        # Check that a worker is destroyed if its task raises an
        # exception in Python.
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        self.assertRaises(RuntimeError, OOF.Help.Debug.Error.PyError)
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        
    def WorkerException1(self):
        # Check that a worker is destroyed if its task raises an
        # exception in C++.
        from ooflib.SWIG.common import ooferror
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        self.assertRaises(ooferror.PyErrProgrammingError,
                          OOF.Help.Debug.Error.CError)
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)

    def WorkerException2(self):
        # Check that a worker is destroyed if its task raises a Python
        # exception by calling a Python function from C++.
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        self.assertRaises(AttributeError, OOF.Help.Debug.Error.CPyError)
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)

    def WorkerException3(self):
        # Check that a worker is destroyed if its task calls a C++
        # function that calls a Python function that calls a C++
        # function that throws an exception.
        from ooflib.SWIG.common import ooferror
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        self.assertRaises(ooferror.PyErrProgrammingError,
                          OOF.Help.Debug.Error.CPyCError)
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)

    def ScriptException0(self):
        # Check that an exception thrown by a script halts the
        # execution of the script.  The script sets teststring to
        # "ok", raises an exception by using an undefined variable,
        # and then sets teststring to "not ok".  If the exception is
        # not handled properly, lines following the error will be
        # read, and teststring will be set to "not ok".
        #
        # The script contains a NameError, but loadscript() in
        # mainmenu.py converts it into a PyErrUserError.
        self.assertRaises(ooferror.PyErrUserError,
                          OOF.File.Load.Script,
                          filename = reference_file("fundamental_data",
                                                    "pyerror.py"))
        self.assertEqual(utils.OOFeval('teststring'), "ok")

    def ScriptException1(self):
        # This script is similar, but it raises the exception by
        # running a menu command.  The exception is an
        # ErrProgrammingError.
        self.assertRaises(ooferror.PyErrUserError,
                          OOF.File.Load.Script,
                          filename=reference_file("fundamental_data",
                                                  "errorcmd.py"))
        self.assertEqual(utils.OOFeval('teststring'), "ok")

    def ScriptException2(self):
        # This script is the same, but it calls the first script using
        # a nested menu command.  teststring and/or another test will
        # not be "ok" if lines following the error are being
        # processed.
        self.assertRaises(ooferror.PyErrUserError,
                          OOF.File.Load.Script,
                          filename=reference_file("fundamental_data",
                                                  "nestederror.py"))
        self.assertTrue(utils.OOFeval('teststring')=="ok" and
                        utils.OOFeval('anothertest')=="ok")

    def ScriptSyntaxErr0(self):
        self.assertRaises(SyntaxError,
                          OOF.File.Load.Script,
                          filename=reference_file("fundamental_data",
                                                  "syntaxerror.py"))
        # syntaxerror.py tries to define 'bandersnatch' before the
        # line containing the syntax error, and 'borogoves' after it.
        # Neither should be defined, because none of the file should
        # have actually been evaluated.
        self.assertRaises(NameError, utils.OOFeval, "bandersnatch")
        self.assertRaises(NameError, utils.OOFeval, "borogoves")

    def ScriptSyntaxErr1(self):
        self.assertRaises(ooferror.PyErrUserError,
                          OOF.File.Load.Script,
                          filename=reference_file("fundamental_data",
                                                  "nestedsyntaxerr.py"))
        self.assertRaises(NameError, utils.OOFeval, "bandersnatch")
        self.assertRaises(NameError, utils.OOFeval, "borogoves")
        self.assertEqual(utils.OOFeval('teststring'), 'ok')

    def RandomNumbers(self):
        # Check to be sure that the random numbers are reproducible
        # from machine to machine when the generator has been seeded.
        # If they're not reproducible, many of the subsequent tests
        # will fail.
        from ooflib.SWIG.common import crandom
        crandom.rndmseed(17)
        r = [crandom.irndm() for x in range(10)]
        expected = [1227918265, 3978157, 263514239, 1969574147, 1833982879,
                    488658959, 231688945, 1043863911, 1421669753, 1942003127]
        self.assertEqual(r, expected)
        crandom.rndmseed(17)
        r = [crandom.irndm() for x in range(10)]
        expected = [1227918265, 3978157, 263514239, 1969574147, 1833982879,
                    488658959, 231688945, 1043863911, 1421669753, 1942003127]
        self.assertEqual(r, expected)
        crandom.rndmseed(137)
        r = [crandom.irndm() for x in range(10)]
        expected = [171676246, 1227563367, 950914861, 1789575326, 941409949,
                    491970794, 2006468446, 837991916, 696662892, 1224152791]
        self.assertEqual(r, expected)

    def Shuffle(self):
        from ooflib.SWIG.common import crandom
        crandom.rndmseed(137)
        r = list(range(50))
        crandom.shuffle(r)
        expected = [6, 5, 30, 37, 10, 11, 43, 32, 41, 1, 20, 33, 13, 35, 28, 38, 18, 17, 2, 36, 22, 9, 3, 48, 15, 25, 40, 21, 31, 26, 42, 49, 16, 4, 46, 27, 24, 34, 45, 14, 47, 23, 44, 7, 12, 29, 19, 0, 8, 39]
        self.assertEqual(r, expected)
        self.assertEqual(len(r), 50)
        self.assertEqual(len(set(r)), 50)
        # Repeat with same seed
        crandom.rndmseed(137)
        r = list(range(50))
        crandom.shuffle(r)
        self.assertEqual(r, expected)
        # Repeat with different seed
        crandom.rndmseed(1778)
        r = list(range(50))
        crandom.shuffle(r)
        expected2 = [10, 20, 42, 23, 36, 25, 2, 30, 17, 32, 34, 49, 13, 21, 33, 47, 35, 46, 24, 5, 28, 0, 29, 22, 38, 27, 26, 4, 40, 16, 3, 19, 14, 37, 39, 1, 44, 48, 6, 11, 7, 18, 31, 9, 8, 45, 15, 12, 43, 41]
        self.assertEqual(r, expected2)
        self.assertEqual(len(r), 50)
        self.assertEqual(len(set(r)), 50)
        
        
test_set = [
    OOF_Fundamental("OrderedDict"),
    OOF_Fundamental("Ordered_Set"),
    OOF_Fundamental("WorkerCleanup"),
    OOF_Fundamental("WorkerException0"),
    OOF_Fundamental("WorkerException1"),
    OOF_Fundamental("WorkerException2"),
    OOF_Fundamental("WorkerException3"),
    OOF_Fundamental("ScriptException0"),
    OOF_Fundamental("ScriptException1"),
    OOF_Fundamental("ScriptException2"),
    OOF_Fundamental("ScriptSyntaxErr0"),
    OOF_Fundamental("ScriptSyntaxErr1"),
    OOF_Fundamental("RandomNumbers"),
    OOF_Fundamental("Shuffle")
]
