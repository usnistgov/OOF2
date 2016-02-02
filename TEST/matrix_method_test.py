# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov. 

import unittest, os
import time
import sys

from UTILS import file_utils
fp_file_compare = file_utils.fp_file_compare
reference_file = file_utils.reference_file
datadir = 'matrix_data'

def loadMatrix(filename):
    matrix = sparsemat.SparseMat(0, 0)
    f = reference_file(datadir, filename)
    matrix.load(f)
    return matrix

def loadVector(filename):
    vector = doublevec.DoubleVec(0)
    f = reference_file(datadir, filename)
    vector.load(f)
    return vector

class IterativeMethods(unittest.TestCase):
    def setUp(self):
        global sparsemat
        global preconditioner
        global doublevec
        global matrixmethod
        from ooflib.SWIG.common import doublevec
        from ooflib.SWIG.engine import sparsemat
        from ooflib.engine import preconditioner
        from ooflib.engine import matrixmethod

        self.matrix = loadMatrix("spd.mtx")
        self.ref = loadVector("spd.vec")
        self.rhs = self.matrix * self.ref
        self.tolerance = 1.e-13
        self.max_iterations = 10000
    
    def CG(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.UnPreconditioner()
        solver = matrixmethod.ConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def CG_ILU(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUPreconditioner()
        solver = matrixmethod.ConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)

    def CG_ILUT(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUTPreconditioner()
        solver = matrixmethod.ConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def CG_Jacobi(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.JacobiPreconditioner()
        solver = matrixmethod.ConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def BiCGStab(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.UnPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def BiCGStab_ILU(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def BiCGStab_ILUT(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUTPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)

    def BiCGStab_Jacobi(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.JacobiPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)

    def BiCG(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.UnPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def BiCG_ILU(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def BiCG_ILUT(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUTPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)

    def BiCG_Jacobi(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.JacobiPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
class DirectMethods(unittest.TestCase):
    def setUp(self):
        global sparsemat
        global doublevec
        global matrixmethod
        from ooflib.SWIG.common import doublevec
        from ooflib.SWIG.engine import sparsemat
        from ooflib.engine import matrixmethod

        self.matrix = loadMatrix("spd.mtx")
        self.ref = loadVector("spd.vec")
        self.rhs = self.matrix * self.ref
        self.rhs = self.matrix * self.ref

    def SimplicialLLT(self):
        solution = doublevec.DoubleVec(0)
        solver = matrixmethod.SimplicialLLT()
        succ = solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def SimplicialLDLT(self):
        solution = doublevec.DoubleVec(0)
        solver = matrixmethod.SimplicialLDLT()
        succ = solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def SparseLU(self):
        solution = doublevec.DoubleVec(0)
        solver = matrixmethod.SparseLU()
        succ = solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)
    
    def SparseQR(self):
        solution = doublevec.DoubleVec(0)
        solver = matrixmethod.SparseQR()
        succ = solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 10)

def run_tests():

    iter_set = [
        IterativeMethods("CG"),
        IterativeMethods("CG_ILU"),
        IterativeMethods("CG_ILUT"),
        IterativeMethods("CG_Jacobi"),
        IterativeMethods("BiCG"),
        IterativeMethods("BiCG_ILU"),
        IterativeMethods("BiCG_ILUT"),
        IterativeMethods("BiCG_Jacobi"),
        IterativeMethods("BiCGStab"),
        IterativeMethods("BiCGStab_ILU"),
        IterativeMethods("BiCGStab_ILUT"),
        IterativeMethods("BiCGStab_Jacobi"),
    ]
    direct_set = [
        DirectMethods("SimplicialLLT"),
        DirectMethods("SimplicialLDLT"),
        DirectMethods("SparseLU"),
        DirectMethods("SparseQR"),
    ]
    test_set = iter_set + direct_set

    logan = unittest.TextTestRunner()
    for t in test_set:
        print >> sys.stderr, "\n *** Running test: %s\n" % t.id()
        res = logan.run(t)
        if not res.wasSuccessful():
            return 0
    return 1

if __name__ == "__main__":
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

