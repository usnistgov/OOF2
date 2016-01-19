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
#include "common/smallmatrix.h"
#include "engine/cmatrixmethods.h"
#include "engine/ooferror.h"
#include "engine/sparsemat.h"

#include <Eigen/SparseCore>
#include <Eigen/IterativeLinearSolvers>
#include <typeinfo> // RTTI, temporary

// TODO(lizhong): comment
// CG, BiCG, BiCGStab and GMRES are just wrappers for the IML++
// template routines.  The wrappers are necessary because we can't
// swig the templates.

// On exit, these routines set maxiter and tolerance to the actual
// number of iterations and the residual.  The swigged versions then
// return those values as a tuple to Python, so that solution
// statistics can be accumulated by SolverStats.

void solveCG(const SparseMat &A, const DoubleVec &rhs,
	    int precond_id, int &maxiter, double &tolerance,
	    DoubleVec &x)
{
  if (precond_id == (int)Precond::Uncond){
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
  else if (precond_id == (int)Precond::Diag) {
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
  else if (precond_id == (int)Precond::ILUT) {
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
    ss << "CG No preconditioner " << precond_id;
    throw ss.str();
  }
}

void solveBiCG(const SparseMat &A, const DoubleVec &rhs,
	      int precond_id, int &maxiter, double &tolerance,
	      DoubleVec &x)
{
  //BiCG(A, x, rhs, pc, maxiter, tolerance);
  solveBiCGStab(A, rhs, precond_id, maxiter, tolerance, x);
}

void solveBiCGStab(const SparseMat &A, const DoubleVec &rhs,
		  int precond_id, int &maxiter, double &tolerance,
		  DoubleVec &x)
{
  //BiCGSTAB(A, x, rhs, pc, maxiter, tolerance);

  if (precond_id == (int)Precond::Uncond){
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
  else if (precond_id == (int)Precond::Diag) {
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
  else if (precond_id == (int)Precond::ILUT) {
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
    ss << "BiCG No preconditioner " << precond_id;
    throw ss.str();
  }
}

void solveGMRes(const SparseMat &A, const DoubleVec &rhs,
	       int precond_id, int &maxiter, int krylov_dim,
	       double &tolerance, DoubleVec &x)
{
  //SmallMatrix H(krylov_dim+1, krylov_dim+1);
  //GMRES(A, x, rhs, pc, H, krylov_dim, maxiter, tolerance);
}

void solveDirect(const SparseMat &A, const DoubleVec &rhs, DoubleVec &x) {
  SimplicialLLT slv;
  x = slv.solve(A, rhs);
  if (slv.info() != Eigen::Success) {
    throw ErrUserError( "Direct matrix solver failed.");
  }
}

