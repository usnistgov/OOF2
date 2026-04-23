// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef SPARSEMAT_H
#define SPARSEMAT_H

#include <oofconfig.h>
#include <sstream>
#include "Eigen/SparseCore"
#include "common/doublevec.h"

class DoFMap;
class SparseMatIterator;
class SparseMatConstIterator;
enum class Precond;
template<typename Derived> class IterativeSolver;
template<typename Derived> class DirectSolver;

typedef Eigen::SparseMatrix<double, Eigen::ColMajor> ESMat;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Doublet contains a row index and matrix element.  It's used when
// constructing the SparseMat.  It's basically the same as
// Eigen::Triplet<double>, but allows the value to be altered and
// doesn't contain the column index.

class Doublet {
private:
  int row_;
  double val_;
public:
  Doublet(int r, double x) : row_(r), val_(x) {}
  double value() const { return val_; }
  double &value() { return val_; }
  int row() const { return row_; }
};

std::ostream &operator<<(std::ostream& os, const Doublet& t);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// SparseMat class wraps Eigen's SparseMatrix

// TODO: Why not derive SparseMat from Eigen::SparseMatrix?

class SparseMat {
private:
  ESMat data;   // Eigen's sparse matrix 

public:
  SparseMat() = default;
  SparseMat(unsigned int nr, unsigned int nc) : data(nr, nc) {}
  SparseMat(const SparseMat&, const DoFMap&, const DoFMap&);
  SparseMat(const SparseMat&) = default;
  SparseMat(SparseMat&&) = default; // move constructor
  SparseMat& operator=(const SparseMat&) = default;
  SparseMat& operator=(SparseMat&&) = default; // move assignment
  ~SparseMat() = default;
  SparseMat clone() const { return *this; }
  void set_from_doublets(std::vector<std::vector<Doublet>>&); // efficient way
  void set_from_triplets(std::vector<Eigen::Triplet<double>>&); // old way

  // TODO(lizhong): inline possible methods

  /* Matrix property methods */

  int nrows() const { return data.rows(); }
  int ncols() const { return data.cols(); }
  int nnonzeros() const { return data.nonZeros(); }
  void resize(int nr, int nc) { data.resize(nr, nc); }
  void reserve(int size) { data.reserve(size); }
  void insert(int ir, int ic, double val) { data.coeffRef(ir, ic) += val; }
  bool empty() const { return data.nonZeros() == 0; }
  double coeff(int ir, int ic) { return data.coeff(ir, ic); }
  double& coeff_ref(int ir, int ic) { return data.coeffRef(ir, ic); }
  void make_compressed() { data.makeCompressed(); }
  bool is_compressed() const { return data.isCompressed(); }
  bool is_nonempty_row(int) const;
  bool is_nonempty_col(int) const;

  SparseMat lower() const;
  SparseMat unit_lower() const;
  SparseMat upper() const;
  SparseMat unit_upper() const;

  /* Arithmetic operations */

  double norm() const { return data.norm(); }
  SparseMat transpose() const;

  SparseMat& operator*=(double);
  SparseMat& operator/=(double);

  SparseMat& operator+=(const SparseMat&);
  SparseMat& operator-=(const SparseMat&);
  SparseMat operator*(double scalar) const;
  SparseMat operator*(const SparseMat&) const;
  DoubleVec operator*(const DoubleVec&) const;

  SparseMat &add(double, const SparseMat&); // scale and add
  DoubleVec trans_mult(const DoubleVec&) const;

  // In-place matrix vector multiplication, ala blas.
  void axpy(double alpha, const DoubleVec &x, DoubleVec &y) const;
  void axpy_trans(double alpha, const DoubleVec &x, DoubleVec &y) const;

  // Triangular solvers.
  void solve_lower_triangle(const DoubleVec&, DoubleVec&) const;
  void solve_lower_triangle_unitd(const DoubleVec&, DoubleVec&) const;
  void solve_lower_triangle_trans(const DoubleVec&, DoubleVec&) const;
  void solve_lower_triangle_trans_unitd(const DoubleVec&, DoubleVec&) const;
  void solve_upper_triangle(const DoubleVec&, DoubleVec&) const;
  void solve_upper_triangle_trans(const DoubleVec&, DoubleVec&) const;

  void tile(int, int, const SparseMat&);

  /* Iterators */
  typedef SparseMatIterator iterator;
  typedef SparseMatConstIterator const_iterator;
  SparseMatIterator begin();
  SparseMatIterator end();
  SparseMatConstIterator begin() const;
  SparseMatConstIterator end() const;

  /* Debugging routines. */

  bool is_lower_triangular(bool diag) const;
  bool is_upper_triangular(bool diag) const;
  bool is_symmetric(double tolerance) const;

  const std::string str() const;

  template<typename Derived> friend class IterativeSolver;
  template<typename Derived> friend class DirectSolver;
  friend std::ostream& operator<<(std::ostream&, const SparseMat&);
  friend bool load_market_mat(SparseMat& mat, const std::string& filename);
  friend bool save_market_mat(const SparseMat&, const std::string&, int);
};				// SparseMat

SparseMat identityMatrix(int);
bool save_mat(const SparseMat& mat, const std::string& filename,
              int precision=13, int sym = 0);
bool load_mat(SparseMat& mat, const std::string& filename);
bool save_market_mat(const SparseMat& mat, const std::string& filename,
		     int sym = 0);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class SMIteratorBase {
protected:
  ESMat& mat;
  ESMat::InnerIterator iter;	// iterator for the inner loop
  int outer;			// index for the outer loop
  bool done;
public:
  SMIteratorBase(ESMat&);
  SMIteratorBase(const SMIteratorBase&) = default;
  void operator++();
  int row() const { return iter.row(); }
  int col() const { return iter.col(); }
  bool operator==(const SMIteratorBase&) const;
  bool operator!=(const SMIteratorBase&) const;
  bool operator<(const SMIteratorBase&) const;
  void to_end();
};

class SparseMatIterator : public SMIteratorBase {
public:
  SparseMatIterator(ESMat& m) : SMIteratorBase(m) {}
  SparseMatIterator& operator++();
  double value() const { return iter.value(); }
  double& value() { return iter.valueRef(); }
  double& operator*() { return iter.valueRef(); }
  double operator*() const { return iter.value(); }
};

class SparseMatConstIterator : public SMIteratorBase {
public:
  SparseMatConstIterator(const ESMat& m)
    : SMIteratorBase(const_cast<ESMat&>(m)) // ugly
  {}
  SparseMatConstIterator& operator++();
  double value() const { return iter.value(); }
  double operator*() const { return iter.value(); }
};

#endif // SPARSEMAT_H_
