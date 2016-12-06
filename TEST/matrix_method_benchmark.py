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

RECORDS = {}

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

def run_CG(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.UnPreconditioner()
    solver = matrixmethod.ConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_CG_ILUT(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ILUTPreconditioner()
    solver = matrixmethod.ConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_CG_Jacobi(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.JacobiPreconditioner()
    solver = matrixmethod.ConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCGStab(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.UnPreconditioner()
    solver = matrixmethod.StabilizedBiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCGStab_ILUT(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ILUTPreconditioner()
    solver = matrixmethod.StabilizedBiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCGStab_Jacobi(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.JacobiPreconditioner()
    solver = matrixmethod.StabilizedBiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_SimplicialLLT(matrix, rhs, solution):
    solver = matrixmethod.SimplicialLLT()
    return solver.solveMatrix(matrix, rhs, solution)

def run_SimplicialLDLT(matrix, rhs, solution):
    solver = matrixmethod.SimplicialLDLT()
    return solver.solveMatrix(matrix, rhs, solution)

def run_SparseLU(matrix, rhs, solution):
    solver = matrixmethod.SparseLU()
    return solver.solveMatrix(matrix, rhs, solution)

def run_SparseQR(matrix, rhs, solution):
    solver = matrixmethod.SparseQR()
    return solver.solveMatrix(matrix, rhs, solution)

def run_iter_solver(nruns, solver, matrix, rhs, ref_solution, max_iterations, tolerance):
    if nruns < 1:
        return
    print "[========== %s ==========]" %(solver.__name__)

    for i in range(nruns):
        solution = doublevec.DoubleVec(rhs.size())
        st = time.time()
        nIters, residue = solver(matrix, rhs, solution, max_iterations, tolerance)
        et = time.time() - st
        RECORDS[solver.__name__].append({ "iterations": nIters, "residue": residue, "time": et})
        print "%d iterations, %s residue, %s seconds" %(nIters, residue, et)
        print "Relative deviation from result: %e" %(
            (solution - ref_solution).norm() / ref_solution.norm())

    size = len(RECORDS[solver.__name__])
    if size > 0:
        totTime = 0.0
        totIter = 0
        for r in RECORDS[solver.__name__]:
            totTime += r["time"]
            totIter += r["iterations"]
        print "Average iterations %d, average time %s seconds" %(totIter / size, totTime / size)
    print

def run_dir_solver(nruns, solver, matrix, rhs, ref_solution):
    if nruns < 1:
        return
    print "[========== %s ==========]" %(solver.__name__)

    for i in range(nruns):
        solution = doublevec.DoubleVec(rhs.size())
        st = time.time()
        solver(matrix, rhs, solution)
        et = time.time() - st
        RECORDS[solver.__name__].append({"time": et})
        print "%s seconds, relative deviation: %e" %(et,
            (solution-ref_solution).norm()/ref_solution.norm())

    size = len(RECORDS[solver.__name__])
    if size > 0:
        totTime = 0.0
        totIter = 0
        for r in RECORDS[solver.__name__]:
            totTime += r["time"]
        print "Average time %s seconds" %(totTime / size)
    print

def benchmark():
    print "Loading matrix and vectors ..."
    matA = loadMatrix("matrix_17748-17748")
    vecRef = loadVector("rst_17748")
    vecRHS = matA * vecRef

    print "Matrix size: %d * %d" %(matA.nrows(), matA.ncols())
    print "Number of nonzeros: %d" %(matA.nnonzeros())
    print ""

    tolerance = 1.e-13
    max_iterations = 10000
    benchmark_runs = 1

    # iterative matrix methods
    iter_solvers = [
        run_CG,
        #run_CG_ILUT,
        #run_CG_Jacobi,
        #run_BiCGStab,
        #run_BiCGStab_ILUT,
        #run_BiCGStab_Jacobi,
    ]

    # direct matrix methods
    dir_solvers = [
        #run_SimplicialLLT,
        #run_SimplicialLDLT,
        #run_SparseLU,
        #run_SparseQR,
    ]

    for fn in iter_solvers:
        RECORDS[fn.__name__] = []    
    for fn in iter_solvers:
        run_iter_solver(benchmark_runs, fn, matA, vecRHS, vecRef, max_iterations, tolerance)

    for fn in dir_solvers:
        RECORDS[fn.__name__] = []    
    for fn in dir_solvers:
        run_dir_solver(benchmark_runs, fn, matA, vecRHS, vecRef)

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

    global sparsemat
    global preconditioner
    global doublevec
    global matrixmethod
    global ooferror2
    from ooflib.SWIG.common import doublevec
    from ooflib.SWIG.engine import sparsemat
    from ooflib.SWIG.engine import ooferror2
    from ooflib.engine import preconditioner
    from ooflib.engine import matrixmethod

    benchmark()

    OOF.File.Quit()

