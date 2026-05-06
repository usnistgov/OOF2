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
enum class Precond;
template <typename Derived> class IterativeSolver;
template <typename Derived> class DirectSolver;
template <typename MATRIX> class SparseMatIterator;

// TODO: Documentation for Eigen::BiCGSTAB says its more efficient for
// row-major sparse matrix format, and can be multithreaded with
// openMP.  Is there a reason for using ColMajor here?

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
  typedef SparseMatIterator<ESMat> iterator;
  typedef SparseMatIterator<const ESMat> const_iterator;
  SparseMatIterator<ESMat> begin();
  SparseMatIterator<ESMat> end();
  SparseMatIterator<const ESMat> begin() const;
  SparseMatIterator<const ESMat> end() const;

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

// MATRIX is an Eigen sparse matrix class. It should be either ESMat
// or const ESMat.

template <typename MATRIX>
class SparseMatIterator {
protected:
  MATRIX& mat;
  typename MATRIX::InnerIterator inneriter; // iterator for the inner loop
  int outer;			// index for the outer loop
  bool done;
public:
  SparseMatIterator(MATRIX& m)
    : mat(m),
      inneriter(m, 0),
      outer(0),
      done(m.nonZeros() == 0)
  {
    if(!done) {
      // Find the first non-empty row
      inneriter = typename MATRIX::InnerIterator(mat, outer);
      while(!inneriter) {
	inneriter = typename MATRIX::InnerIterator(mat, ++outer);
      }
    }
  }
  
  SparseMatIterator(const SparseMatIterator<MATRIX>&) = default;
  
  bool operator==(const SparseMatIterator<MATRIX>& other) const {
    // Iterators are equal if they're both done, or both point to the
    // same entry.  Comparing iterators from different matrices is
    // undefined.
    return ((done && other.done) ||
	    (outer == other.outer and inneriter == other.inneriter));
  }

  bool operator!=(const SparseMatIterator<MATRIX>& other) const {
    return !this->operator==(other);
  }

  bool operator<(const SparseMatIterator<MATRIX>& other) const {
    if(other.done)
      return !done;
    return (outer < other.outer ||
	    (outer == other.outer && inneriter < other.inneriter));
  }
  
  SparseMatIterator<MATRIX>& operator++() {
    ++inneriter;		// increment the Eigen InnerIterator
    // If we're done with this inner row/col, find the next non-empty one.
    while(outer < mat.outerSize()-1 && !inneriter) {
      inneriter = typename MATRIX::InnerIterator(mat, ++outer);
    }
    done = not bool(inneriter);
    return *this;
  }
  
  void to_end() {
    outer = mat.outerSize();
    done = true;
  }

  int row() const { return inneriter.row(); }
  int col() const { return inneriter.col(); }
  double value() const { return inneriter.value(); }
  double operator*() const { return inneriter.value(); }

  // If MATRIX is a const type, these methods will never be used, so
  // it doesn't matter that MATRIX::InnerIterator::valueRef is a
  // non-const method.
  double& operator*() { return inneriter.valueRef(); }
  double& value() { return inneriter.valueRef(); }
};

template class SparseMatIterator<ESMat>;
template class SparseMatIterator<const ESMat>;

#endif // SPARSEMAT_H_
