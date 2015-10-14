
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

def loadMatrix(filename):
    matrix = sparsemat.SparseMat(0, 0)
    f = open(filename, 'r')

    for line in f:
        try:
            arr = line.split()
            i = int(arr[0])
            j = int(arr[1])
            val = float(arr[2])
        except:
            # Ignore lines that don't make sense.  They're
            # probably comments or blank lines.
            pass
        else:
            matrix.insert(i, j, val)

    f.close()
    return matrix

def loadVector(filename):
    vector = doublevec.DoubleVec(0)
    vector.load(filename)
    return vector

def run_precond_ILU(matrix, rhs):
    pcwrap = preconditioner.ILUPreconditioner()
    pc = pcwrap.create_preconditioner(matrix)
    rst = pc.solve(rhs)

def run_precond_IC(matrix, rhs):
    pcwrap = preconditioner.ICPreconditioner()
    pc = pcwrap.create_preconditioner(matrix)
    rst = pc.solve(rhs)

def run_precond_Jacobi(matrix, rhs):
    pcwrap = preconditioner.JacobiPreconditioner()
    pc = pcwrap.create_preconditioner(matrix)
    rst = pc.solve(rhs)

def run_CG(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.UnPreconditioner()
    solver = matrixmethod.ConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_CG_ILU(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ILUPreconditioner()
    solver = matrixmethod.ConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_CG_IC(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ICPreconditioner()
    solver = matrixmethod.ConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_CG_Jacobi(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.JacobiPreconditioner()
    solver = matrixmethod.ConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCG(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.UnPreconditioner()
    solver = matrixmethod.BiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCG_ILU(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ILUPreconditioner()
    solver = matrixmethod.BiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCG_IC(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ICPreconditioner()
    solver = matrixmethod.BiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCG_Jacobi(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.JacobiPreconditioner()
    solver = matrixmethod.BiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCGStab(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.UnPreconditioner()
    solver = matrixmethod.StabilizedBiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCGStab_ILU(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ILUPreconditioner()
    solver = matrixmethod.StabilizedBiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCGStab_IC(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ICPreconditioner()
    solver = matrixmethod.StabilizedBiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_BiCGStab_Jacobi(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.JacobiPreconditioner()
    solver = matrixmethod.StabilizedBiConjugateGradient(pc, tolerance, max_iterations)
    return solver.solveMatrix(matrix, rhs, solution)

def run_GMRES(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.UnPreconditioner()
    krylov_dim = 20
    solver = matrixmethod.GeneralizedMinResidual(pc, tolerance, max_iterations, krylov_dim)
    return solver.solveMatrix(matrix, rhs, solution)

def run_GMRES_ILU(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ILUPreconditioner()
    krylov_dim = 20
    solver = matrixmethod.GeneralizedMinResidual(pc, tolerance, max_iterations, krylov_dim)
    return solver.solveMatrix(matrix, rhs, solution)

def run_GMRES_IC(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.ICPreconditioner()
    krylov_dim = 20
    solver = matrixmethod.GeneralizedMinResidual(pc, tolerance, max_iterations, krylov_dim)
    return solver.solveMatrix(matrix, rhs, solution)

def run_GMRES_Jacobi(matrix, rhs, solution, max_iterations, tolerance):
    pc = preconditioner.JacobiPreconditioner()
    krylov_dim = 20
    solver = matrixmethod.GeneralizedMinResidual(pc, tolerance, max_iterations, krylov_dim)
    return solver.solveMatrix(matrix, rhs, solution)

def run_preconditioner(nruns, precond, matrix, rhs):
    if nruns < 1:
        return

    print "[========== %s ==========]" %(precond.__name__)
    for i in range(nruns):
        st = time.time()
        precond(matrix, rhs)
        et = time.time() - st
        RECORDS[precond.__name__].append(et)

   
    size = len(RECORDS[precond.__name__])
    if size > 0:
        tot = 0.0
        for t in RECORDS[precond.__name__]:
            tot += t
        print "%s seconds" %(tot / size)

def run_solver(nruns, solver, matrix, rhs, ref_solution, max_iterations, tolerance):
    if nruns < 1:
        return

    print "[========== %s ==========]" %(solver.__name__)

    for i in range(nruns):
        try:
            solution = doublevec.DoubleVec(rhs.size())
            st = time.time()
            nIters, residue = solver(matrix, rhs, solution, max_iterations, tolerance)
            et = time.time() - st
        except ooferror2.ErrConvergenceFailure:
            print "Failed to converge in %d steps" %max_iterations
        else:
            RECORDS[solver.__name__].append({ "iterations": nIters, "residue": residue, "time": et})
            print "%d iterations, %s residue, %s seconds" %(nIters, residue, et)
            print "relative deviation from result: %e" %(
                (solution - ref_solution).norm() / ref_solution.norm())

    size = len(RECORDS[solver.__name__])
    if size > 0:
        totTime = 0.0
        totIter = 0
        for r in RECORDS[solver.__name__]:
            totTime += r["time"]
            totIter += r["iterations"]
        print "average iterations %d, average time %s seconds" %(totIter / size, totTime / size)

def benchmark():

    print "Loading matrix and vectors ..."

    matA = loadMatrix("./data/matrix_17748-17748")
    vecRHS = loadVector("./data/rhs_17748")
    vecRef = loadVector("./data/rst_17748")

    tolerance = 1.e-13
    max_iterations = 10000
    benchmark_runs = 3

    vecRHS = matA * vecRef

    print "Matrix size: %d * %d" %(matA.nrows(), matA.ncols())
    print "Vector size: %d" %(vecRHS.size())
    print ""

    # Preconditioners
    preconds = [
        run_precond_ILU,
        run_precond_IC,
        run_precond_Jacobi,
    ]

    # Linear solvers with preconditioners
    solvers = [
        run_CG,
        run_CG_IC,
        run_CG_ILU,
        run_CG_Jacobi,
        run_BiCG,
        run_BiCG_IC,
        run_BiCG_ILU,
        run_BiCG_Jacobi,
        run_BiCGStab,
        run_BiCGStab_IC,
        run_BiCGStab_ILU,
        run_BiCGStab_Jacobi,
        run_GMRES,
        run_GMRES_IC,
        run_GMRES_ILU,
        run_GMRES_Jacobi,
    ]

    for pc in preconds:
        RECORDS[pc.__name__] = []    
    for fn in solvers:
        RECORDS[fn.__name__] = []    

    for pc in preconds:
        run_preconditioner(benchmark_runs, pc, matA, vecRHS)

    for fn in solvers:
        run_solver(benchmark_runs, fn, matA, vecRHS, vecRef, max_iterations, tolerance)

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
    from ooflib.SWIG.engine import preconditioner
    from ooflib.SWIG.engine import ooferror2
    from ooflib.engine import matrixmethod

    benchmark()

    OOF.File.Quit()

