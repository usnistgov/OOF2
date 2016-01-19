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

%module cmatrixmethods
%include "engine/typemaps.swg"

%{
#include "engine/cmatrixmethods.h"
typedef CG<Precond::Uncond> CG_Unpre;
typedef CG<Precond::Diag> CG_Diag;
typedef CG<Precond::ILUT> CG_ILUT;
typedef BiCGStab<Precond::Uncond> BiCGStab_Unpre;
typedef BiCGStab<Precond::Diag> BiCGStab_Diag;
typedef BiCGStab<Precond::ILUT> BiCGStab_ILUT;
%}

class CG_Unpre{
public:
  CG_Unpre();
  ~CG_Unpre();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
  int info() const;
};

class CG_Diag {
public:
  CG_Diag();
  ~CG_Diag();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
  int info() const;
};

class CG_ILUT{
public:
  CG_ILUT();
  ~CG_ILUT();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
  int info() const;
};

class BiCGStab_Unpre {
public:
  BiCGStab_Unpre();
  ~BiCGStab_Unpre();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
  int info() const;
};

class BiCGStab_Diag {
public:
  BiCGStab_Diag();
  ~BiCGStab_Diag();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
  int info() const;
};

class BiCGStab_ILUT {
public:
  BiCGStab_ILUT();
  ~BiCGStab_ILUT();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  void set_max_iterations(int iters);
  int max_iterations() const;
  void set_tolerance(double tol);
  double tolerance() const;
  int iterations() const;
  double error() const;
  int info() const;
};

class SimplicialLLT {
public:
  SimplicialLLT();
  ~SimplicialLLT();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  int info();
};

class SimplicialLDLT {
public:
  SimplicialLDLT();
  ~SimplicialLDLT();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  int info();
};

class SparseLU {
public:
  SparseLU();
  ~SparseLU();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  int info();
};

class SparseQR {
public:
  SparseQR();
  ~SparseQR();
  void solve(const SparseMat& m, const DoubleVec& rhs, DoubleVec& x);
  int info();
};

%typemap(python, argout) int INOUT {
  // typemap(python, argout) int INOUT
  if(!$target || $target == Py_None) {
    $target = PyList_New(0);
  }
  PyList_Append($target, PyInt_FromLong($source));
 }

%typemap(python, argout) double INOUT {
  // typemap(python, argout) double INOUT
  if(!$target || $target == Py_None) {
    $target = PyList_New(0);
  }
  PyList_Append($target, PyFloat_FromDouble($source));
 }

void solveCG(const SparseMat&, const DoubleVec&,
  int, int INOUT, double INOUT, DoubleVec&);

void solveBiCG(const SparseMat&, const DoubleVec&,
  int, int INOUT, double INOUT, DoubleVec&);

void solveBiCGStab(const SparseMat&, const DoubleVec&,
  int, int INOUT, double INOUT, DoubleVec&);

void solveGMRes(const SparseMat&, const DoubleVec&,
  int, int INOUT, int, double INOUT, DoubleVec&);

void solveDirect(const SparseMat&, const DoubleVec &rhs, DoubleVec &x);


#endif
