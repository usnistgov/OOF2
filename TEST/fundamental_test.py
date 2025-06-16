# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest, os, sys
from ooflib.common import debug, utils
from ooflib.SWIG.common import cdebug

# For reasons that I don't completely understand, file_utils needs to
# be imported with an absolute path name, or else the modules imported
# here and in regression.py will have different __name__'s.  That
# means that the second import (this one) will re-run the commands in
# the file, and reset file_utils.referencedir.
from oof2.TEST.UTILS.file_utils import reference_file

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Class for tests that generate Exceptions.


class ExcTestCase(unittest.TestCase):

    def assertOOFRaises(self, expectation, cmd, *args, **kwargs):
        # expectation is the expected exception.  It can be an
        # Exception subclass or an instance of one.
        try:
            cmd(*args, **kwargs)
        except Exception as exc:
            # Find the root cause of the caught exception, if it's a
            # PyOOFError.  The root cause might not also be a
            # PyOOFError.
            exc = exc.rootCause()
            # exc is an instance of PyOOFError or Exception.  Since
            # PyOOFError is a subclass of Exception, the order of the
            # comparisons below is important.
            if isinstance(exc, ooferror.PyOOFError):
                # exc is a PyOOFError object. expectation must be a
                # PyOOFError object or class.
                if isinstance(expectation, type):
                    # expectation is a class. exc must be an instance
                    # of it.
                    if not isinstance(exc, expectation):
                        self.fail()
                else:
                    # excpectation is a PyOOFError instance. exc must
                    # equal it.  PyOOFError instances can be compared
                    # directly.
                    self.assertEqual(exc, expectation)
            else:
                # exc is a generic non-OOF Exception.
                if isinstance(expectation, type):
                    # expectation is a class.  exc should be an
                    # instance of it.
                    if not isinstance(exc, expectation):
                        self.fail()
                else:
                    # expectation is an instance. exc must equal it.
                    # Standard Python exceptions can't be compared
                    # directly with __eq__ (WTF?).  For example, this is
                    # False:
                    #   NameError("abc") == NameError("abc")
                    self.assertEqual(type(exc), type(expectation))
                    self.assertEqual(exc.args, expectation.args)
        else:
            # No exception was raised, although we were expecting one.
            self.fail()

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class OOF_Fundamental(ExcTestCase):
    def setUp(self):
        global allWorkers, allWorkerCores
        from ooflib.common.worker import allWorkers, allWorkerCores
        from ooflib.common import utils

    def DoubleVec(self):
        from ooflib.SWIG.common.doublevec import DoubleVec
        size = 10
        a = DoubleVec(size)
        b = DoubleVec(size)
        
        # setting and getting
        for i in range(size):
            a[i] = i 
        for i in range(size):
            self.assertEqual(a[i], i)
        for i in range(size):
            b[i] = -i
            
        # iteration in C++.
        # iteration over a DoubleVec in python is not supported.
        vec = DoubleVec.testIterator(a) # returns 7*a
        self.assertEqual(len(vec), size)
        for i in range(size):
            self.assertEqual(vec[i], 7*i)
        
        # cloning
        c = a.clone()
        for i in range(size):
            self.assertEqual(a[i], c[i])
            
        # equality
        self.assertTrue(a == c)
        self.assertEqual(a, c)
        self.assertTrue(b != c)
        self.assertNotEqual(b, c)

        # in-place operations on a single entry
        c = a.clone()
        c[1] += 5
        self.assertEqual(c[1], 6)
        c[2] -= 4
        self.assertEqual(c[2], -2)
        c[3] *= 5
        self.assertEqual(c[3], 15)
        c[4] /= -1
        self.assertEqual(c[4], -4)
        
        # addition
        c = a + b
        self.assertEqual(len(c), size)
        for i in range(size):
            self.assertEqual(c[i], 0)

        # in-place addition
        d = a.clone()
        self.assertEqual(len(d), len(a))
        d += b 
        self.assertEqual(len(d), len(b))
        self.assertTrue(a+b == d)

        # subtraction
        c = a - b
        self.assertEqual(len(c), size)
        for i in range(size):
            self.assertEqual(c[i], 2*i)

        # in-place subtraction
        d = a.clone()
        d -= b
        self.assertTrue(d == c)

        # multiplication
        d = a*2                 # __mul__
        for i in range(size):
            self.assertEqual(d[i], 2*i)
        e = 2*a                 # __rmul__
        self.assertEqual(e, d)
        e *= 0.5                # __imul__
        self.assertEqual(e, a)

        # division
        print("divide")
        d = a/2.
        for i in range(size):
            self.assertEqual(d[i], a[i]/2)
        d /= 2.
        for i in range(size):
            self.assertEqual(d[i], a[i]/4)
        
        # dot product
        self.assertEqual(a*b, -285)
            
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

    def WorkerException00(self):
        # Check that errors raised in python are handled correctly
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        self.assertRaises(ooferror.PyErrPyProgrammingError,
                          OOF.Help.Debug.Error.PyError2)
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

    def WorkerExceptionZero(self):
        # Check for a properly handled divide by zero error
        ## TODO: Fix this!  Is the worker not being removed?
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)
        self.assertRaises(ZeroDivisionError, OOF.Help.Debug.Error.DivideByZero)
        self.assertEqual(len(allWorkers), 0)
        self.assertEqual(len(allWorkerCores), 0)

    def ScriptException0(self):
        # Check that an exception thrown by a script halts the
        # execution of the script.  The script sets teststring to
        # "ok", raises an exception by using an undefined variable,
        # and then sets teststring to "not ok".  If the exception is
        # not handled properly, lines following the error will be
        # read, and teststring will be set to "not ok".
        self.assertOOFRaises(
            NameError("name 'y' is not defined"),
            OOF.File.Load.Script,
            filename = reference_file("fundamental_data", "pyerror.py"))
        self.assertEqual(utils.OOFeval('teststring'), "ok")

    def ScriptException1(self):
        # This script is similar, but it raises the exception by
        # running a menu command, OOF.Help.Debug.Error.CError.  The
        # command throws an ErrProgrammingError from C++.
        self.assertOOFRaises(
            PyErrProgrammingError(
                "Somebody made a mistake!",
                # The file name given here needs to be the same as
                # the file name referred to by __FILE__ when oof2 was
                # compiled.
                cdebug.sourcePathPrefix() + "OOF2/SRC/common/cdebug.C",
                # The line number here is fake, so that the test won't
                # break if cdebug.C is altered.  See throwException()
                # in cdebug.C.
                124),
            OOF.File.Load.Script,
            filename=reference_file("fundamental_data", "errorcmd.py"))
        self.assertEqual(utils.OOFeval('teststring'), "ok")

    def ScriptException2(self):
        # This script is the same, but it calls the first script using
        # a nested menu command.  teststring and/or another test will
        # not be "ok" if lines following the error are being
        # processed.
        self.assertOOFRaises(
            PyErrProgrammingError(
                "Somebody made a mistake!",
                cdebug.sourcePathPrefix() + "OOF2/SRC/common/cdebug.C",
                124),
            OOF.File.Load.Script,
            filename=reference_file("fundamental_data", "nestederror.py"))
        self.assertTrue(utils.OOFeval('teststring')=="ok" and
                        utils.OOFeval('anothertest')=="ok")

    def ScriptSyntaxErr0(self):
        self.assertOOFRaises(SyntaxError,
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
        # This test runs a script that attempts to load the faulty
        # syntexerror.py script used by ScriptSyntaxErr0.  Nothing in
        # syntaxerror.py should be evaluated, but everything in
        # nestedsyntaxerr.py that comes *before* it imports
        # syntaxerror.py should be evaluated.  nestedsyntaxerr.py sets
        # teststring="ok" before loading syntaxerror.py and "not ok"
        # afterwards.
        self.assertOOFRaises(SyntaxError,
                             OOF.File.Load.Script,
                             filename=reference_file("fundamental_data",
                                                     "nestedsyntaxerr.py"))
        self.assertRaises(NameError, utils.OOFeval, "bandersnatch")
        self.assertRaises(NameError, utils.OOFeval, "borogoves")
        self.assertEqual(utils.OOFeval('teststring'), 'ok')

    def ScriptFuncDef(self):
        OOF.File.Load.Script(filename=reference_file("fundamental_data",
                                                     "funcdef.py"))
        self.assertEqual(utils.OOFeval('tart'), 6.28)
        self.assertEqual(utils.OOFeval('pie'), 3.14)
                                                     

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
        # Make sure that the shuffle algorithm does what it used to
        # do. When we relied on methods provide by the system or by
        # Python, the implementation sometimes changed, which broke
        # other tests.
        from ooflib.SWIG.common import crandom
        crandom.rndmseed(137)
        r = list(range(50))
        expected = [6, 5, 30, 37, 10, 11, 43, 32, 41, 1, 20, 33, 13, 35, 28, 38, 18, 17, 2, 36, 22, 9, 3, 48, 15, 25, 40, 21, 31, 26, 42, 49, 16, 4, 46, 27, 24, 34, 45, 14, 47, 23, 44, 7, 12, 29, 19, 0, 8, 39]
        # To ensure that shuffle, implemented in C++, isn't
        # mishandling reference counts, count the references to one
        # element of the list before and after shuffling.
        val = 40                # anything in the list
        refcount = sys.getrefcount(val)
        crandom.shuffle(r)
        self.assertEqual(len(r), 50)
        self.assertEqual(len(set(r)), 50) # no duplicate entries
        self.assertEqual(r, expected)
        self.assertEqual(refcount, sys.getrefcount(val))
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
        self.assertEqual(len(r), 50)
        self.assertEqual(len(set(r)), 50)
        self.assertEqual(r, expected2)

test_set = [ 
    OOF_Fundamental("OrderedDict"),
    OOF_Fundamental("Ordered_Set"),
    OOF_Fundamental("WorkerCleanup"),
    OOF_Fundamental("WorkerException0"),
    OOF_Fundamental("WorkerException00"),
    OOF_Fundamental("WorkerException1"),
    OOF_Fundamental("WorkerException2"),
    OOF_Fundamental("WorkerException3"),
    # OOF_Fundamental("WorkerExceptionZero"),
    OOF_Fundamental("ScriptException0"),
    OOF_Fundamental("ScriptException1"),
    OOF_Fundamental("ScriptException2"),
    OOF_Fundamental("ScriptSyntaxErr0"),
    OOF_Fundamental("ScriptSyntaxErr1"),
    OOF_Fundamental("RandomNumbers"),
    OOF_Fundamental("Shuffle"),
    OOF_Fundamental("ScriptFuncDef"),
    OOF_Fundamental("DoubleVec")
]

# test_set = [
#     OOF_Fundamental("ScriptSyntaxErr0")
# ]
