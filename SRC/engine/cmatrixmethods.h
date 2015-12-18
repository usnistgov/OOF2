/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Swiggable C++ Wrappers for the low level Eigen's matrix solvers.

#ifndef CMATRIXMETHODS_H
#define CMATRIXMETHODS_H

#include <oofconfig.h>
#include <Eigen/IterativeLinearSolvers>
#include <Eigen/SparseCholesky>
#include <Eigen/SparseLU>
#include <Eigen/SparseQR>
#include "engine/sparsemat.h"

enum class Precond {Uncond=1, Diag=2, ILUT=3};

template<Precond P> class CG;
template<Precond P> class BiCGStab;
class SimplicialLLT;

namespace internal {
// Iterative solver traits

template<typename Derived> struct IterSolverTrait;

template<> struct IterSolverTrait<CG<Precond::Uncond>> {
  typedef Eigen::ConjugateGradient< ESMat,
    Eigen::Lower | Eigen::Upper,
    Eigen::IdentityPreconditioner > Type;
};

template<> struct IterSolverTrait<CG<Precond::Diag>> {
  typedef Eigen::ConjugateGradient< ESMat,
    Eigen::Lower | Eigen::Upper,
    Eigen::DiagonalPreconditioner<double> > Type;
};

template<> struct IterSolverTrait<CG<Precond::ILUT>> {
  typedef Eigen::ConjugateGradient< ESMat,
    Eigen::Lower | Eigen::Upper,
    Eigen::IncompleteLUT<double> > Type;
};

template<> struct IterSolverTrait<BiCGStab<Precond::Uncond>> {
  typedef Eigen::BiCGSTAB< ESMat, Eigen::IdentityPreconditioner > Type;
};

template<> struct IterSolverTrait<BiCGStab<Precond::Diag>> {
  typedef Eigen::BiCGSTAB< ESMat, Eigen::DiagonalPreconditioner<double> > Type;
};

template<> struct IterSolverTrait<BiCGStab<Precond::ILUT>> {
  typedef Eigen::BiCGSTAB< ESMat, Eigen::IncompleteLUT<double> > Type;
};

// Direct sovler traits

template<typename Derived> struct DirectSolverTrait;

template<> struct DirectSolverTrait<SimplicialLLT> {
  typedef Eigen::SimplicialLLT<ESMat> Type;
};
} // end namespace internal

// Iterative solvers

template<typename Derived>
class IterativeSolver {
private:
  typename internal::IterSolverTrait<Derived>::Type solver_;
public:
  void analyze_pattern(const SparseMat& m);
  void factorize(const SparseMat& m);
  void compute(const SparseMat& m);
  DoubleVec solve(const DoubleVec& rhs);
  DoubleVec solve(const SparseMat& m, const DoubleVec& rhs);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
  int info() const;
};

template<Precond P>
class CG : public IterativeSolver<CG<P>> {
  friend class IterativeSolver<CG<P>>;
};
template class CG<Precond::Uncond>;
template class CG<Precond::Diag>;
template class CG<Precond::ILUT>;

template <Precond P>
class BiCGStab : public IterativeSolver<BiCGStab<P>> {
  friend class IterativeSolver<BiCGStab<P>>;
};
template class BiCGStab<Precond::Uncond>;
template class BiCGStab<Precond::Diag>;
template class BiCGStab<Precond::ILUT>;

// Direct solvers

template <typename Derived> class DirectSolver {
protected:
  typename internal::DirectSolverTrait<Derived>::Type solver_;
public:
  void analyze_pattern(const SparseMat& m);
  void factorize(const SparseMat& m);
  void compute(const SparseMat& m);
  DoubleVec solve(const DoubleVec& rhs);
  DoubleVec solve(const SparseMat& m, const DoubleVec& rhs);
  int info();
};

class SimplicialLLT : public DirectSolver<SimplicialLLT> {
  friend class DirectSolver<SimplicialLLT>;
};

void solveCG(const SparseMat&, const DoubleVec &rhs,
  int precond_id, int &maxiter, double &tolerance,
  DoubleVec &x);

void solveBiCG(const SparseMat&, const DoubleVec &rhs,
  int precond_id, int &maxiter, double &tolerance,
  DoubleVec &x);

void solveBiCGStab(const SparseMat&, const DoubleVec &rhs,
  int precond_id, int &maxiter, double &tolerance,
  DoubleVec &x);

void solveGMRes(const SparseMat&, const DoubleVec &rhs,
  int precond_id, int &maxiter, int krylov_dim,
  double &tolerance, DoubleVec &x);

void solveDirect(const SparseMat&, const DoubleVec &rhs, DoubleVec &x);

#endif // CMATRIXMETHODS_H
