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
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def CG_ILU(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUPreconditioner()
        solver = matrixmethod.ConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)

    def CG_ILUT(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUTPreconditioner()
        solver = matrixmethod.ConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def CG_Jacobi(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.JacobiPreconditioner()
        solver = matrixmethod.ConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def BiCGStab(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.UnPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def BiCGStab_ILU(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def BiCGStab_ILUT(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUTPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)

    def BiCGStab_Jacobi(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.JacobiPreconditioner()
        solver = matrixmethod.StabilizedBiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)

    def BiCG(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.UnPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def BiCG_ILU(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def BiCG_ILUT(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.ILUTPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)

    def BiCG_Jacobi(self):
        solution = doublevec.DoubleVec(0)
        pc = preconditioner.JacobiPreconditioner()
        solver = matrixmethod.BiConjugateGradient(pc, self.tolerance, self.max_iterations)
        solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
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
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def SimplicialLDLT(self):
        solution = doublevec.DoubleVec(0)
        solver = matrixmethod.SimplicialLDLT()
        succ = solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def SparseLU(self):
        solution = doublevec.DoubleVec(0)
        solver = matrixmethod.SparseLU()
        succ = solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)
    
    def SparseQR(self):
        solution = doublevec.DoubleVec(0)
        solver = matrixmethod.SparseQR()
        succ = solver.solveMatrix(self.matrix, self.rhs, solution)
        self.assertAlmostEqual(self.ref.norm(), solution.norm(), 9)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#


class BCTest(unittest.TestCase):
    # Tests using a matrix and RHS that made TwoFloats in
    # boundary_condition_test.py fail after upgrading to Eigen 3.3.9
    # from 3.2.  Other preconditioned CG solvers failed too.
    def setUp(self):
        global doublevec
        global matrixmethod
        global preconditioner
        global sparsemat
        from ooflib.SWIG.common import doublevec
        from ooflib.SWIG.engine import sparsemat
        from ooflib.engine import matrixmethod
        from ooflib.engine import preconditioner
        self.tolerance = 1.e-13
        self.max_iterations = 10000

    def solve(self, solver):
        matrix = loadMatrix("bctest.mtx")
        self.assert_(matrix.is_symmetric(1.e-12))
        rhs = loadVector("bctest.rhs")
        solution = doublevec.DoubleVec(0)
        solver.solveMatrix(matrix, rhs, solution)
        ref = loadVector("bctest.sol")
        diff = solution - ref
        self.assertAlmostEqual(diff.norm(), 0.0, 9)
        resid = matrix*solution - rhs
        self.assertAlmostEqual(resid.norm(), 0.0, 9)
    def CG0(self):
        self.solve(
            matrixmethod.ConjugateGradient(
                preconditioner.UnPreconditioner(),
                self.tolerance, self.max_iterations))
    # ILU(T) is not guaranteed to work with CG, and doesn't in this
    # case, using Eigen 3.3.9.  It did work with Eigen 3.2.91.  Also,
    # Eigen only provides ILUT, not ILU, so OOF2's ILU is the same as
    # ILUT.
    # def CG_ILU(self):
    #     self.solve(
    #         matrixmethod.ConjugateGradient(
    #             preconditioner.ILUPreconditioner(),
    #             self.tolerance, self.max_iterations))
    # def CG_ILUT(self):
    #     self.solve(
    #         matrixmethod.ConjugateGradient(
    #             preconditioner.ILUTPreconditioner(),
    #             self.tolerance, self.max_iterations))
    def CG_Jacobi(self):
        self.solve(
            matrixmethod.ConjugateGradient(
                preconditioner.JacobiPreconditioner(),
                self.tolerance, self.max_iterations))
    def CG_IC(self):
        self.solve(
            matrixmethod.ConjugateGradient(
                preconditioner.ICPreconditioner(),
                self.tolerance, self.max_iterations))

    def BiCG0(self):
        self.solve(
            matrixmethod.BiConjugateGradient(
                preconditioner.UnPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCG_ILU(self):
        self.solve(
            matrixmethod.BiConjugateGradient(
                preconditioner.ILUPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCG_ILUT(self):
        self.solve(
            matrixmethod.BiConjugateGradient(
                preconditioner.ILUTPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCG_Jacobi(self):
        self.solve(
            matrixmethod.BiConjugateGradient(
                preconditioner.JacobiPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCG_IC(self):
        self.solve(
            matrixmethod.BiConjugateGradient(
                preconditioner.ICPreconditioner(),
                self.tolerance, self.max_iterations))
        
    def BiCGStab0(self):
        self.solve(
            matrixmethod.StabilizedBiConjugateGradient(
                preconditioner.UnPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCGStab_ILU(self):
        self.solve(
            matrixmethod.StabilizedBiConjugateGradient(
                preconditioner.ILUPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCGStab_ILUT(self):
        self.solve(
            matrixmethod.StabilizedBiConjugateGradient(
                preconditioner.ILUTPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCGStab_Jacobi(self):
        self.solve(
            matrixmethod.StabilizedBiConjugateGradient(
                preconditioner.JacobiPreconditioner(),
                self.tolerance, self.max_iterations))
    def BiCGStab_IC(self):
        self.solve(
            matrixmethod.StabilizedBiConjugateGradient(
                preconditioner.ICPreconditioner(),
                self.tolerance, self.max_iterations))

    def SimplicialLDLT(self):
        self.solve(matrixmethod.SimplicialLDLT())
    def SimplicialLLT(self):
        self.solve(matrixmethod.SimplicialLLT())
    def SparseLU(self):
        self.solve(matrixmethod.SparseLU())
    def SparseQR(self):
        self.solve(matrixmethod.SparseQR())

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

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

bc_set = [
    BCTest("CG0"),
    # BCTest("CG_ILU"), # doesn't converge
    # BCTest("CG_ILUT"), # doesn't converge
        BCTest("CG_Jacobi"),
    BCTest("CG_IC"),
    BCTest("BiCG0"),      
    BCTest("BiCG_ILU"), 
    BCTest("BiCG_ILUT"),
    BCTest("BiCG_Jacobi"),
    BCTest("BiCG_IC"),
    BCTest("BiCGStab0"),      
    BCTest("BiCGStab_ILU"), 
    BCTest("BiCGStab_ILUT"),
    BCTest("BiCGStab_Jacobi"),
    BCTest("BiCGStab_IC"),
    BCTest("SimplicialLDLT"),
    BCTest("SimplicialLLT"),
    BCTest("SparseLU"),
    BCTest("SparseQR")
]

test_set = iter_set + direct_set + bc_set

