// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CMATRIXMETHODS_SWG
#define CMATRIXMETHODS_SWG

%module(package="ooflib.SWIG.engine") cmatrixmethods

%include "common/typemaps.swg"

%{
#include "engine/cmatrixmethods.h"
typedef CG<Precond::Uncond> CG_Unpre;
typedef CG<Precond::Diag> CG_Diag;
typedef CG<Precond::ILUT> CG_ILUT;
typedef CG<Precond::IC> CG_IC;
typedef BiCGStab<Precond::Uncond> BiCGStab_Unpre;
typedef BiCGStab<Precond::Diag> BiCGStab_Diag;
typedef BiCGStab<Precond::ILUT> BiCGStab_ILUT;
typedef BiCGStab<Precond::IC> BiCGStab_IC;
typedef GMRES<Precond::Uncond> GMRES_Unpre;
typedef GMRES<Precond::Diag> GMRES_Diag;
typedef GMRES<Precond::ILUT> GMRES_ILUT;
typedef GMRES<Precond::IC> GMRES_IC;
%}

enum Info {
  // From Eigen/src/Core/util/Constants.h:
  // enum ComputationInfo {
  //   /** Computation was successful. */
  //   Success = 0,
  //   /** The provided data did not satisfy the prerequisites. */
  //   NumericalIssue = 1,
  //   /** Iterative procedure did not converge. */
  //   NoConvergence = 2,
  //   /** The inputs are invalid, or the algorithm has been improperly called.
  //    * When assertions are enabled, such errors trigger an assert. */
  //   InvalidInput = 3
  // };
  SUCCESS = Eigen::Success,
  NUMERICAL = Eigen::NumericalIssue,
  NOCONVERG = Eigen::NoConvergence,
  INVALID_INPUT = Eigen::InvalidInput
};

class CG_Unpre{
public:
  CG_Unpre();
  ~CG_Unpre();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class CG_Diag {
public:
  CG_Diag();
  ~CG_Diag();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class CG_ILUT {
public:
  CG_ILUT();
  ~CG_ILUT();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class CG_IC {
public:
  CG_IC();
  ~CG_IC();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class BiCGStab_Unpre {
public:
  BiCGStab_Unpre();
  ~BiCGStab_Unpre();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class BiCGStab_Diag {
public:
  BiCGStab_Diag();
  ~BiCGStab_Diag();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class BiCGStab_ILUT {
public:
  BiCGStab_ILUT();
  ~BiCGStab_ILUT();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class BiCGStab_IC {
public:
  BiCGStab_IC();
  ~BiCGStab_IC();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class GMRES_Unpre{
public:
  GMRES_Unpre();
  ~GMRES_Unpre();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class GMRES_Diag {
public:
  GMRES_Diag();
  ~GMRES_Diag();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class GMRES_ILUT {
public:
  GMRES_ILUT();
  ~GMRES_ILUT();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class GMRES_IC {
public:
  GMRES_IC();
  ~GMRES_IC();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
};

class SimplicialLLT {
public:
  SimplicialLLT();
  ~SimplicialLLT();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
};

class SimplicialLDLT {
public:
  SimplicialLDLT();
  ~SimplicialLDLT();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
};

class SparseLU {
public:
  SparseLU();
  ~SparseLU();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
};

class SparseQR {
public:
  SparseQR();
  ~SparseQR();
  int solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
};

#endif
