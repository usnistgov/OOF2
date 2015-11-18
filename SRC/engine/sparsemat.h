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
#include <Eigen/SparseCore>
#include <sstream>

/* SparseMat class wraps Eigen's SparseMatrix */

class SparseMatIterator;

class SparseMat {
public:
  typedef Eigen::SparseMatrix<double, Eigen::RowMajor> ESMat;
  typedef ESMat::InnerIterator InnerIter;

  SparseMat() = default;
  SparseMat(unsigned int nr, unsigned int nc) : data(nr, nc) {}
  //SparseMat(const SparseMat&, const DoFMap&, const DoFMap&);
  SparseMat(const SparseMat&) = default;
  SparseMat(SparseMat&&) = default; // move constructor
  SparseMat& operator=(const SparseMat&) = default;
  SparseMat& operator=(SparseMat&&) = default; // move assignment
  ~SparseMat() = default;
  SparseMat clone() const { return *this; }

  // TODO(lizhong): inline possible methods

  /* Matrix property methods */

  int nrows() const { return data.rows(); }
  int ncols() const { return data.cols(); }
  int nnonzeros() const { return data.nonZeros(); }
  void resize(int nr, int nc) { data.resize(nr, nc); }
  void reserve(int size) { data.reserve(size); }
  void insert(int ir, int ic, double val) { data.insert(ir, ic) = val; }
  bool empty() const { return data.nonZeros() == 0; }
  double coeff(int ir, int ic) { return data.coeff(ir, ic); }
  double& coeff_ref(int ir, int ic) { return data.coeffRef(ir, ic); }
  void make_compressed() { data.makeCompressed(); }
  bool is_compressed() { return data.isCompressed(); }
  bool is_nonempty_row(unsigned int) const;
  bool is_nonempty_col(unsigned int) const;

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

  /* Iterators */

  friend class SparseMatIterator;
  typedef SparseMatIterator iterator;
  iterator begin();
  iterator end();

  /*
  typedef SparseMatConstIterator const_iterator;
  const_iterator begin() const;
  const_iterator end() const;

  typedef SparseMatIterator iterator;
  iterator begin();
  iterator end();
  */

  /* Debugging routines. */

  bool is_lower_triangular(bool diag) const;
  bool is_upper_triangular(bool diag) const;
  bool is_symmetric(double tolerance) const;
  /*
  bool unique_indices() const;
  DoubleVec inefficient_get_column(unsigned int) const;

  //void merge(const std::vector<SparseMat>& ms);
  //void tile(unsigned int i, unsigned int j, const SparseMat &other);
  */

  const std::string str() const;

  friend std::ostream& operator<<(std::ostream&, const SparseMat&);
  friend bool save_market_mat(const SparseMat& mat, const std::string& filename, int sym = 0);
  friend bool load_market_mat(SparseMat& mat, const std::string& filename);

private:
  // Eigen's sparse matrix 
  ESMat data;
};

bool save_mat(const SparseMat& mat, const std::string& filename, int precision=13, int sym = 0);
bool load_mat(SparseMat& mat, const std::string& filename);

//TODO(lizhong): implement const iterator

class SparseMatIterator {
private:
  SparseMat& mat;

  // This iterator is implemented based on the storage scheme of compressed
  // sparse matricis (row or column major) in Eigen.
  // The compressed sparse matrix consist of three compact arrays:
  // - Values: stores the coefficient values of the non-zeros.
  // - InnerIndices: stores the row (resp. column) indices of the non-zeros.
  // - OuterStarts: stores for each column (resp. row) the index of the
  //                first non-zero in the previous two arrays.

  double* val_ptr;    // pointer of the Values array
  int* in_ptr;        // pointer of the InnerIndices array 
  int* out_ptr;       // pointer of the OuterStarts array
  int  in_idx;        // current index in the InnerIndices
  int  out_idx;       // current index in the OuterIndeces

public:
  SparseMatIterator(SparseMat&);

  int row() const;
  int col() const;
  double& value() const;
  bool done() const;

  SparseMatIterator& operator++();
  double& operator*() const;

  bool operator==(const SparseMatIterator&) const;
  bool operator!=(const SparseMatIterator&) const;

  /*
  bool operator<(const SparseMatIterator&) const;
  bool operator>=(const SparseMatIterator&) const;
  bool operator==(const SparseMatConstIterator&) const;
  bool operator!=(const SparseMatConstIterator&) const;
  bool operator<(const SparseMatConstIterator&) const;
  bool operator>=(const SparseMatConstIterator&) const;
  */

  /* Debug */

  // print the three compact arrays.
  void print_indices() {
    for (int i = 0; i <= mat.data.nonZeros(); i++) {
        std::cout << val_ptr[i] << ", ";
    }
    std::cout << std::endl;
    for (int i = 0; i <= mat.data.nonZeros(); i++) {
        std::cout << in_ptr[i] << ", ";
    }
    std::cout << std::endl;
    for (int i = 0; i <= mat.data.outerSize(); i++) {
        std::cout << out_ptr[i] << ", ";
    }
    std::cout << std::endl;
  }

  friend class SparseMat;
  //friend class SparseMatConstIterator;
  friend std::ostream& operator<<(std::ostream&, const SparseMatIterator&);

private:
  void to_end();
};

#endif // SPARSEMAT_H_
