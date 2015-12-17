/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#include <oofconfig.h>
#include <iostream>

#include "common/doublevec.h"
#include "common/printvec.h"	// for debugging
#include "common/smallmatrix.h"
#include "engine/SparseLib++/bicg.h"
#include "engine/SparseLib++/bicgstab.h"
//#include "engine/SparseLib++/cg.h"
#include "engine/SparseLib++/gmres.h"
#include "engine/cmatrixmethods.h"
#include "engine/ooferror.h"
#include "engine/preconditioner.h"
#include "engine/sparsemat.h"

// TODO(lizhong)
#include <Eigen/SparseCore>
#include <Eigen/IterativeLinearSolvers>
#include <typeinfo> // RTTI, temporary
#include "engine/diagpre.h"
#include "engine/ilupre.h"

// TODO(lizhong): comment
// CG, BiCG, BiCGStab and GMRES are just wrappers for the IML++
// template routines.  The wrappers are necessary because we can't
// swig the templates.

// On exit, these routines set maxiter and tolerance to the actual
// number of iterations and the residual.  The swigged versions then
// return those values as a tuple to Python, so that solution
// statistics can be accumulated by SolverStats.

void solveCG(const SparseMat &A, const DoubleVec &rhs,
	    const PreconditionerBase &pc, int &maxiter, double &tolerance,
	    DoubleVec &x)
{
  if (typeid(pc) == typeid(UnconditionerCore)) {
    CG<Precond::Uncond> slv; 
    slv.set_max_iterations(maxiter);
    slv.set_tolerance(tolerance);
    x = slv.solve(A, rhs); 
    maxiter = slv.iterations();
    tolerance = slv.error();
    if (slv.info() != Eigen::Success) {
      throw std::string("CG failed to converge");
    }
  }
  else if (typeid(pc) == typeid(DiagPreconditionerCore)) {
    CG<Precond::Diag> slv; 
    slv.set_max_iterations(maxiter);
    slv.set_tolerance(tolerance);
    slv.compute(A);
    x = slv.solve(rhs);
    maxiter = slv.iterations();
    tolerance = slv.error();
    if (slv.info() != Eigen::Success) {
      throw std::string("CG failed to converge");
    }
  }
  else if (typeid(pc) == typeid(ILUPreconditionerCore)) {
    CG<Precond::ILUT> slv; 
    slv.set_max_iterations(maxiter);
    slv.set_tolerance(tolerance);
    slv.compute(A);
    x = slv.solve(rhs);
    maxiter = slv.iterations();
    tolerance = slv.error();
    if (slv.info() != Eigen::Success) {
      throw std::string("CG failed to converge");
    }
  }
  else {
    std::stringstream ss;
    ss << "CG No preconditioner " << typeid(pc).name();
    throw ss.str();
  }
}

void solveBiCG(const SparseMat &A, const DoubleVec &rhs,
	      const PreconditionerBase &pc, int &maxiter, double &tolerance,
	      DoubleVec &x)
{
  if (typeid(pc) == typeid(UnconditionerCore)) {
    BiCGStab<Precond::Uncond> slv; 
    slv.set_max_iterations(maxiter);
    slv.set_tolerance(tolerance);
    x = slv.solve(A, rhs); 
    maxiter = slv.iterations();
    tolerance = slv.error();
    if (slv.info() != Eigen::Success) {
      throw std::string("BiCG failed to converge");
    }
  }
  else if (typeid(pc) == typeid(DiagPreconditionerCore)) {
    BiCGStab<Precond::Diag> slv; 
    slv.set_max_iterations(maxiter);
    slv.set_tolerance(tolerance);
    slv.compute(A);
    x = slv.solve(rhs);
    maxiter = slv.iterations();
    tolerance = slv.error();
    if (slv.info() != Eigen::Success) {
      throw std::string("BiCG failed to converge");
    }
  }
  else if (typeid(pc) == typeid(ILUPreconditionerCore)) {
    BiCGStab<Precond::ILUT> slv; 
    slv.set_max_iterations(maxiter);
    slv.set_tolerance(tolerance);
    slv.compute(A);
    x = slv.solve(rhs);
    maxiter = slv.iterations();
    tolerance = slv.error();
    if (slv.info() != Eigen::Success) {
      throw std::string("BiCG failed to converge");
    }
  }
  else {
    std::stringstream ss;
    ss << "BiCG No preconditioner " << typeid(pc).name();
    throw ss.str();
  }

  //BiCG(A, x, rhs, pc, maxiter, tolerance);
}

void solveBiCGStab(const SparseMat &A, const DoubleVec &rhs,
		  const PreconditionerBase &pc, int &maxiter, double &tolerance,
		  DoubleVec &x)
{
  BiCGSTAB(A, x, rhs, pc, maxiter, tolerance);
}

void solveGMRes(const SparseMat &A, const DoubleVec &rhs,
	       const PreconditionerBase &pc, int &maxiter, int krylov_dim,
	       double &tolerance, DoubleVec &x)
{
  SmallMatrix H(krylov_dim+1, krylov_dim+1);
  GMRES(A, x, rhs, pc, H, krylov_dim, maxiter, tolerance);
}

void solveDirect(const SparseMat &A, const DoubleVec &rhs, DoubleVec &x) {
  SimplicialLLT slv;
  x = slv.solve(A, rhs);
  if (slv.info() != Eigen::Success) {
    throw ErrUserError( "Direct matrix solver failed.");
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// IterativeSolver class methods

template<typename Derived>
void IterativeSolver<Derived>::analyze_pattern(const SparseMat& m) {
  solver_.analyzePattern(m.data);
}

template<typename Derived>
void IterativeSolver<Derived>::factorize(const SparseMat& m) {
  solver_.factorize(m.data);
}

template<typename Derived>
void IterativeSolver<Derived>::compute(const SparseMat& m) {
  solver_.compute(m.data);
}

template<typename Derived>
DoubleVec IterativeSolver<Derived>::solve(const DoubleVec& rhs) {
  DoubleVec x;
  x.data = solver_.solve(rhs.data);
  return x;
}

template<typename Derived>
DoubleVec IterativeSolver<Derived>::solve(
  const SparseMat& m, const DoubleVec& rhs) {
  DoubleVec x;
  solver_.compute(m.data);
  x.data = solver_.solve(rhs.data);
  return x;
}

template<typename Derived>
void IterativeSolver<Derived>::set_max_iterations(int iters) {
  solver_.setMaxIterations(iters);
}

template<typename Derived>
int IterativeSolver<Derived>::max_iterations() const {
  return solver_.maxIterations();
}

template<typename Derived>
void IterativeSolver<Derived>::set_tolerance(double tol) {
  solver_.setTolerance(tol);
}

template<typename Derived>
double IterativeSolver<Derived>::tolerance() const {
  return solver_.tolerance();
}

template<typename Derived>
int IterativeSolver<Derived>::iterations() const {
  return solver_.iterations();
}

template<typename Derived>
double IterativeSolver<Derived>::error() const {
  return solver_.error();
}

template<typename Derived>
int IterativeSolver<Derived>::info() const {
  // TODO(lizhong): return type
  return solver_.info();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// DirectSolver class methods

template <typename Derived>
void DirectSolver<Derived>::analyze_pattern(const SparseMat& m) {
  solver_.analyzePattern(m.data);
}

template <typename Derived>
void DirectSolver<Derived>::factorize(const SparseMat& m) {
  solver_.factorize(m.data);
}

template <typename Derived>
void DirectSolver<Derived>::compute(const SparseMat& m) {
  solver_.compute(m.data);
}

template <typename Derived>
DoubleVec DirectSolver<Derived>::solve(const DoubleVec& rhs) {
  DoubleVec x;
  x.data = solver_.solve(rhs.data);
  return x;
}

template <typename Derived>
DoubleVec DirectSolver<Derived>::solve(const SparseMat& m,
  const DoubleVec& rhs) {
  DoubleVec x;
  solver_.compute(m.data);
  x.data = solver_.solve(rhs.data);
  return x;
}

template <typename Derived>
int DirectSolver<Derived>::info() {
  // TODO(lizhong): return type
  return solver_.info();
}
