# -*- python -*-

# This software was produced by NIST, an agency of the U.S. government,
# and by statute is not subject to copyright in the United States.
# Recipients of this software assume all responsibilities associated
# with its operation, modification and maintenance. However, to
# facilitate maintenance we ask that before distributing modified
# versions of this software, you first contact the authors at
# oof_manager@nist.gov.

from ooflib.SWIG.engine import cmatrixmethods
from ooflib.SWIG.engine import ooferror
from ooflib.engine import preconditioner
from ooflib.common import debug
from ooflib.common import registeredclass
from ooflib.common.IO import mainmenu
from ooflib.common.IO import oofmenu
from ooflib.common.IO import parameter
from ooflib.common.IO import xmlmenudump

import math

# Methods for solving SparseMat matrix equations.  Subclasses need to
# have a (Python) 'solveMatrix' method which takes four non-self arguments:
#   a SparseMat matrix
#   a DoubleVec rhs
#   a DoubleVec solution
# and returns a tuple containing the number of iterations taken and
# the final residual.

class MatrixMethod(registeredclass.RegisteredClass):
    registry = []
    def shortrepr(self):
        return self.__class__.__name__
    def solve(self, matrix, rhs, solution):
        return self.solveMatrix(matrix, rhs, solution)
    tip="Ways to solve a matrix equation."
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/matrixmethod.xml')
    xrefs=["Section-Tasks-Solver",
           "Section-Concepts-Mesh-Solvers"]

class PreconditionedMatrixMethod(MatrixMethod):
    def shortrepr(self):
        return "%s(%s)" % (self.__class__.__name__, 
                           self.preconditioner.shortrepr())

class SymmetricMatrixMethodParam(parameter.RegisteredParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        super(SymmetricMatrixMethodParam, self).__init__(
            name, MatrixMethod, value=value, default=default, tip=tip)

class AsymmetricMatrixMethodParam(parameter.RegisteredParameter):
    def __init__(self, name, value=None, default=None, tip=None):
        super(AsymmetricMatrixMethodParam, self).__init__(
            name, MatrixMethod, value=value, default=default, tip=tip)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

_check_symmetry = False #debug.debug()

## The routines in cmatrixmethods return the number of iterations and
## the residual.

## TODO: Use Eigen's solveWithGuess() method instead of solve() in
## cases where we have a previous solution (non-linear solvers?
## plasticity?)

class ConjugateGradient(PreconditionedMatrixMethod):
    solver_map = {
        preconditioner.UnPreconditioner : cmatrixmethods.CG_Unpre,
        preconditioner.JacobiPreconditioner : cmatrixmethods.CG_Diag,
        preconditioner.ICPreconditioner : cmatrixmethods.CG_IC,
        preconditioner.ILUPreconditioner : cmatrixmethods.CG_ILUT,
        preconditioner.ILUTPreconditioner : cmatrixmethods.CG_ILUT
    }
    def __init__(self, preconditioner, tolerance, max_iterations):
        self.preconditioner = preconditioner
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.solver = self.solver_map[type(preconditioner)]()
        self.solver.set_max_iterations(max_iterations)
        self.solver.set_tolerance(tolerance)
    def solveMatrix(self, matrix, rhs, solution):
        if _check_symmetry:
            import sys
            import subprocess, os
            if (matrix.nrows()!=matrix.ncols() or
                not matrix.is_symmetric(1.e-12)): # can be very slow
                raise ooferror.PyErrPyProgrammingError(
                    "%dx%d CG matrix is not symmetric!" %
                    (matrix.nrows(), matrix.ncols()))
        # added to try to debug memory usage
        #subprocess.check_output(["oof2",'os.getpid()'])
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NOCONVERG:
                raise ooferror.PyErrConvergenceFailure(
                    "CG", self.solver.iterations())
        return self.solver.iterations(), self.solver.error()

registeredclass.Registration(
    "CG",
    MatrixMethod,
    ConjugateGradient,
    ordering=1,
    symmetricOnly=True,
    params=[
        preconditioner.PreconditionerParameter(
            "preconditioner",
            preconditioner.Preconditioner,
            tip="Black magic for making the matrix more easily solvable."),
        parameter.FloatParameter(
            "tolerance", 1.e-13,
            tip="Largest acceptable relative error in the matrix solution."),
        parameter.IntParameter(
            "max_iterations", 1000,
            tip="Maximum number of iterations to perform.")],
    tip="Conjugate Gradient method for iteratively solving symmetric matrices.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/cg.xml')
    )

def check_symmetry(menuitem, state):
    global _check_symmetry
    _check_symmetry = state

mainmenu.debugmenu.addItem(
    oofmenu.CheckOOFMenuItem(
        'Check_CG_symmetry',
        debug.debug(),
        callback=check_symmetry,
        help='Verify matrix symmetry before using Conjugate Gradient.',
        discussion="<para>For debugging.  Slow.</para>"))


#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class StabilizedBiConjugateGradient(PreconditionedMatrixMethod):
    solver_map = {
        preconditioner.UnPreconditioner : cmatrixmethods.BiCGStab_Unpre,
        preconditioner.JacobiPreconditioner : cmatrixmethods.BiCGStab_Diag,
        preconditioner.ILUTPreconditioner : cmatrixmethods.BiCGStab_ILUT,
        preconditioner.ILUPreconditioner : cmatrixmethods.BiCGStab_ILUT,
        preconditioner.ICPreconditioner : cmatrixmethods.BiCGStab_IC
    }
    def __init__(self, preconditioner, tolerance, max_iterations):
        self.preconditioner = preconditioner
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.solver = self.solver_map[type(preconditioner)]()
        self.solver.set_max_iterations(max_iterations)
        self.solver.set_tolerance(tolerance)
    def solveMatrix(self, matrix, rhs, solution):
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NOCONVERG:
                raise ooferror.PyErrConvergenceFailure(
                    "StabilizedBiConjugateGradient", self.solver.iterations())
        return self.solver.iterations(), self.solver.error()

registeredclass.Registration(
    "BiCGStab",
    MatrixMethod,
    StabilizedBiConjugateGradient,
    ordering=2.1,
    symmetricOnly=False,
    params=[
        preconditioner.PreconditionerParameter(
            "preconditioner",
            preconditioner.Preconditioner,
            tip="Black magic for making the matrix more easily solvable."),
        parameter.FloatParameter(
            "tolerance", 1.e-13,
            tip="Largest acceptable relative error in the matrix solution."),
        parameter.IntParameter(
            "max_iterations", 1000,
            tip="Maximum number of iterations to perform.")],
    tip="Stabilized bi-conjugate gradient method for iteratively solving non-symmetric matrices.",
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/bicgstab.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

class GMRES(PreconditionedMatrixMethod):
    solver_map = {
        preconditioner.UnPreconditioner : cmatrixmethods.GMRES_Unpre,
        preconditioner.JacobiPreconditioner : cmatrixmethods.GMRES_Diag,
        preconditioner.ILUTPreconditioner : cmatrixmethods.GMRES_ILUT,
        preconditioner.ILUPreconditioner : cmatrixmethods.GMRES_ILUT,
        preconditioner.ICPreconditioner : cmatrixmethods.GMRES_IC
    }
    def __init__(self, preconditioner, tolerance, max_iterations):
        self.preconditioner = preconditioner
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.solver = self.solver_map[type(preconditioner)]()
        self.solver.set_max_iterations(max_iterations)
        self.solver.set_tolerance(tolerance)
    def solveMatrix(self, matrix, rhs, solution):
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NOCONVERG:
                raise ooferror.PyErrConvergenceFailure(
                    "GMRES", self.solver.iterations())
        return self.solver.iterations(), self.solver.error()

registeredclass.Registration(
    "GMRES",
    MatrixMethod,
    GMRES,
    ordering=2.1,
    symmetricOnly=False,
    params=[
        preconditioner.PreconditionerParameter(
            "preconditioner",
            preconditioner.Preconditioner,
            tip="Black magic for making the matrix more easily solvable."),
        parameter.FloatParameter(
            "tolerance", 1.e-13,
            tip="Largest acceptable relative error in the matrix solution."),
        parameter.IntParameter(
            "max_iterations", 1000,
            tip="Maximum number of iterations to perform.")],
    tip="Generalized Mean Residuial method for iteratively solving non-symmetric matrices.",
#    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/gmres.xml')
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

## Preserve this method for backward compitability, which actually
## inherts BiCGStab.
class BiConjugateGradient(StabilizedBiConjugateGradient):
    def __init__(self, preconditioner, tolerance, max_iterations):
        StabilizedBiConjugateGradient.__init__(
            self, preconditioner, tolerance, max_iterations)

registeredclass.Registration(
    "BiCG",
    MatrixMethod,
    BiConjugateGradient,
    ordering=2.2,
    symmetricOnly=False,
    secret=True,
    params=[
        preconditioner.PreconditionerParameter(
            "preconditioner",
            preconditioner.Preconditioner,
            tip="Black magic for making the matrix more easily solvable."),
        parameter.FloatParameter(
            "tolerance", 1.e-13,
            tip="Largest acceptable relative error in the matrix solution."),
        parameter.IntParameter(
            "max_iterations", 1000,
            tip="Maximum number of iterations to perform.")],
    tip="Actually the same as BiCGStab.  Preserved for backwards compatibility.",
    discussion="""<para>
    This method is kept for backwards compatibility, but
    <xref linkend="RegisteredClass-BiCBStab"/> is used instead.
    </para>"""
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# Direct linear solvers 

## Preserve this method for backward compitability, which actually
## calls SparseLU. 
class DirectMatrixSolver(MatrixMethod):
    def __init__(self):
        self.solver = cmatrixmethods.SparseLU()
    def solveMatrix(self, matrix, rhs, solution):
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NUMERICAL:
                raise ooferror.PyErrPyProgrammingError(
                    "The provided data did not satisfy the prerequisites.")
            elif succ == cmatrixmethods.INVALID_INPUT:
                raise ooferror.PyErrPyProgrammingError(
                    "The inputs are invalid, or the algorithm has been improperly called.")
        return (1, 0)

class SimplicialLLT(MatrixMethod):
    def __init__(self):
        self.solver = cmatrixmethods.SimplicialLLT()
    def solveMatrix(self, matrix, rhs, solution):
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NUMERICAL:
                raise ooferror.PyErrPyProgrammingError(
                    "The provided data did not satisfy the prerequisites.")
            elif succ == cmatrixmethods.INVALID_INPUT:
                raise ooferror.PyErrPyProgrammingError(
                    "The inputs are invalid, or the algorithm has been improperly called.")
        return (1, 0)

class SimplicialLDLT(MatrixMethod):
    def __init__(self):
        self.solver = cmatrixmethods.SimplicialLDLT()
    def solveMatrix(self, matrix, rhs, solution):
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NUMERICAL:
                raise ooferror.PyErrPyProgrammingError(
                    "The provided data did not satisfy the prerequisites.")
            elif succ == cmatrixmethods.INVALID_INPUT:
                raise ooferror.PyErrPyProgrammingError(
                    "The inputs are invalid, or the algorithm has been improperly called.")
        return (1, 0)

class SparseLU(MatrixMethod):
    def __init__(self):
        self.solver = cmatrixmethods.SparseLU()
    def solveMatrix(self, matrix, rhs, solution):
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NUMERICAL:
                raise ooferror.PyErrPyProgrammingError(
                    "The provided data did not satisfy the prerequisites.")
            elif succ == cmatrixmethods.INVALID_INPUT:
                raise ooferror.PyErrPyProgrammingError(
                    "The inputs are invalid, or the algorithm has been improperly called.")
        return (1, 0)

class SparseQR(MatrixMethod):
    def __init__(self):
        self.solver = cmatrixmethods.SparseQR()
    def solveMatrix(self, matrix, rhs, solution):
        succ = self.solver.solve(matrix, rhs, solution)
        if succ != cmatrixmethods.SUCCESS: 
            if succ == cmatrixmethods.NUMERICAL:
                raise ooferror.PyErrPyProgrammingError(
                    "The provided data did not satisfy the prerequisites.")
            elif succ == cmatrixmethods.INVALID_INPUT:
                raise ooferror.PyErrPyProgrammingError(
                    "The inputs are invalid, or the algorithm has been improperly called.")
        return (1, 0)

registeredclass.Registration(
    "DirectMatrixSolver",
    MatrixMethod,
    DirectMatrixSolver,
    ordering=204,
    symmetricOnly=True,
    secret=True,        # so that it won't be used in new computations
    tip="An obsolete matrix solver preserved for compitability."
    # no discussion is necessary -- secret registrations aren't in the manual
)

registeredclass.Registration(
    "SimplicialLLT",
    MatrixMethod,
    SimplicialLLT,
    ordering=201,
    symmetricOnly=True,
    tip="A direct sparse matrix solver using LL^T Cholesky factorizations for sparse positive definite matrices.",
    discussion="""
    <para>This routine is provided by <ulink
    url="https://eigen.tuxfamily.org" role="external">Eigen</ulink>.
    See <ulink
    url="https://eigen.tuxfamily.org/dox/classEigen_1_1SimplicialLLT.html"
    role="external"/>.
    </para>"""
)

registeredclass.Registration(
    "SimplicialLDLT",
    MatrixMethod,
    SimplicialLDLT,
    ordering=200,
    symmetricOnly=True,
    tip="A direct sparse matrix solver using LDL^T Cholesky factorizations for sparse positive definite matrices. Recommended for very sparse and not too large problems.",
    discussion="""<para>This routine is provided by <ulink
    url="https://eigen.tuxfamily.org" role="external">Eigen</ulink>.
    See <ulink url="https://eigen.tuxfamily.org/dox/classEigen_1_1SimplicialLDLT.html"
    role="external"/>.
    </para>"""
)

registeredclass.Registration(
    "SparseLU",
    MatrixMethod,
    SparseLU,
    ordering=202,
    symmetricOnly=False,
    tip="A direct sparse matrix solver using LU factorizations for square matrices.",
    discussion="""<para>
    This routine is provided by <ulink
    url="https://eigen.tuxfamily.org" role="external">Eigen</ulink>.
    See <ulink
    url="https://eigen.tuxfamily.org/dox/classEigen_1_1SparseLU.html"
    role="external"/>.
    </para>"""
)

registeredclass.Registration(
    "SparseQR",
    MatrixMethod,
    SparseQR,
    ordering=203,
    symmetricOnly=False,
    tip="A direct sparse matrix solver using QR factorizations for any type of matrices.",
    discussion="""<para>
    This routine is provided by <ulink
    url="https://eigen.tuxfamily.org" role="external">Eigen</ulink>.
    See <ulink
    url="https://eigen.tuxfamily.org/dox/classEigen_1_1SparseQR.html"
    role="external"/>.
    </para>"""
)

#=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=##=--=#

# BasicMatrixMethod is used when setting solver parameters in Basic
# mode.  It only requires the user to choose between Iterative and
# Direct.

class BasicMatrixMethod(registeredclass.RegisteredClass):
    registry = []
    tip="Simple methods for solving matrix equations."
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/basicmatrix.xml')

class BasicDirect(BasicMatrixMethod):
    def shortrepr(self):
        return "Direct"
    def resolve_symmetric(self, existingSolver):
        if isinstance(existingSolver, SimplicialLDLT):
            return existingSolver
        return SimplicialLDLT()
    def resolve_asymmetric(self, existingSolver):
        if isinstance(existingSolver, SparseQR):
            return existingSolver
        return SparseQR()

class BasicIterative(BasicMatrixMethod):
    def __init__(self, tolerance, max_iterations):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
    def resolve_symmetric(self, existingSolver):
        if (isinstance(existingSolver, ConjugateGradient) and
            existingSolver.tolerance == self.tolerance and
            existingSolver.max_iterations == self.max_iterations and
            isinstance(existingSolver.preconditioner,
                       preconditioner.ICPreconditioner)):
            return existingSolver
        return ConjugateGradient(
            preconditioner=preconditioner.ICPreconditioner(),
            tolerance=self.tolerance,
            max_iterations=self.max_iterations)
    def resolve_asymmetric(self, subproblemcontext, existingSolver):
        if (isinstance(existingSolver, StabilizedBiConjugateGradient) and
            existingSolver.tolerance == self.tolerance and
            existingSolver.max_iterations == self.max_iterations and
            isinstance(existingSolver.preconditioner,
                       preconditioner.ILUTPreconditioner
                       )):
            return existingSolver
        return StabilizedBiConjugateGradient(
            preconditioner=preconditioner.ILUTPreconditioner(),
            tolerance=self.tolerance,
            max_iterations=self.max_iterations)
    def shortrepr(self):
        return "Iterative"

registeredclass.Registration(
    'Iterative',
    BasicMatrixMethod,
    BasicIterative,
    ordering=0,
    params=[
        parameter.FloatParameter(
            "tolerance", 1.e-13,
            tip="Largest acceptable relative error in the matrix solution."),
        parameter.IntParameter(
            "max_iterations", 1000,
            tip="Maximum number of iterations to perform.")],
    tip='Solve matrix equations approximately and iteratively, without using exta memory.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/basiciterative.xml')
    )

registeredclass.Registration(
    'Direct',
    BasicMatrixMethod,
    BasicDirect,
    ordering=1,
    tip='Solve matrix equations with a direct method.  Not recommended for large problems.',
    discussion=xmlmenudump.loadFile('DISCUSSIONS/engine/reg/basicdirect.xml'))

