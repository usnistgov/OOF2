// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/cdebug.h"
#include "common/chunkyvector.h"
#include "common/printvec.h"
#include "engine/dofmap.h"
#include "engine/sparsemat.h"

#include <unsupported/Eigen/SparseExtra>
#include <iostream>
#include <fstream>

// Construct by extraction from an existing matrix.
SparseMat::SparseMat(const SparseMat& source,
                     const DoFMap& rowmap,
                     const DoFMap& colmap) 
  : data(rowmap.range(), colmap.range())
{
  // rowmap[i] is the row of the submatrix corresponding to row i of
  // mat. If rowmap[i] == -1, then row i should not be included in the
  // submatrix. If rowmap[i] == rowmap[j], then rows i and j of mat are
  // added together in the submatrix. Likewise for columns.
  for(SparseMatConstIterator it=source.begin(); it<source.end(); ++it) {
    assert(it.row() < rowmap.domain());
    assert(it.col() < colmap.domain());
    int i = rowmap[it.row()];
    // DoFMap::range returns an unsigned int, so it's necessary to
    // cast it to int before comparing to i, which could be -1.
    assert(i < (int) rowmap.range());
    if(i >= 0) {
      int j = colmap[it.col()];
      assert(j < (int) colmap.range() && j >= -1);
      if(j >= 0) {
	// TODO: This calls SparseMatrix::coeffRef, which is
	// inefficient.  Use insertFromTriplets or
	// insertFromSortedTriplets instead.
	insert(i, j, it.value());
      }
    }
  }
  make_compressed();
}

void SparseMat::set_from_doublets(std::vector<std::vector<Doublet>> &doubs) {
  // Fill the Eigen::SparseMatrix efficiently, without allocating
  // extra space or doing too much extra work (hopefully).  Each entry
  // in doubs is a vector of Doublets for a single column of the
  // matrix.  It may have multiple entries for a row, which need to be
  // summed.

  // nnzcol is a vector of ints saying how many non-zero elements
  // are in each column of the matrix.
  Eigen::VectorXi nnzcol = Eigen::VectorXi::Zero(ncols());

  // For each column, find and sum the redundant entries and reserve
  // space in the Eigen::SparseMatrix for the resulting number of
  // rows.
  for(int c=0; c<ncols(); c++) { // Loop over columns
    std::vector<Doublet> *dvec = &doubs[c]; // Doublets in this column
    if(dvec->size() > 1) {
      // Sort the entries in the column by row number
      std::sort(dvec->begin(), dvec->end(),
		[](const Doublet &a, const Doublet &b) {
		  return a.row() < b.row();
		});
      // Look for adjacent entries with the same row number and add
      // them, while compressing the vector. 
      int nuniq = 1;		// number of unique rows found
      int latest = 0;		// index of latest unique row
      for(unsigned int k=1; k<dvec->size(); k++) { // loop over Doublets
	if((*dvec)[k].row() == (*dvec)[latest].row()) {
	  // Repeated row. Add this matrix element to the first one
	  // found for this row, and don't increment latest or nuniq.
	  (*dvec)[latest].value() += (*dvec)[k].value();
	}
	else {
	  // Found a new row number
	  (*dvec)[nuniq] = (*dvec)[k];
	  latest = nuniq;
	  ++nuniq;
	}
      }	// end loop over Doublets k
      
      // Truncate the vector of Doublets to its new length
      dvec->resize(nuniq, Doublet(-1,0));
      nnzcol[c] = nuniq;
    } // end if dvec->size() > 1

    else if(dvec->size() == 1)
      nnzcol[c] = 1;
    
  } // end loop over columns c

  // Reserve space in the matrix for each column
  data.reserve(nnzcol);

  // Insert values
  for(int c=0; c<ncols(); c++) {
    for(const Doublet &doub : doubs[c]) {
      // Because the matrix ordering is Eigen::ColMajor and the space
      // for each column is reserved, calling insert() is efficient.
      data.insert(doub.row(), c) = doub.value();
    }
  }
  // makeCompressed shouldn't have to move any values around.  The
  // only reason to call it here is to free some unnecessary vectors
  // and let the rest of Eigen know that the matrix is already
  // compressed.
  data.makeCompressed();
}

void SparseMat::set_from_triplets(std::vector<Eigen::Triplet<double>>& tris) {
  // Initialize this sparse matrix from (row, col, value)
  // triplets. For triplets having the same row# and col#, add them
  // together.

  // This method is simple but involves some internal array
  // reallocation in Eigen and is expected to use more memory than
  // set_from_doublets.  The result of setFromTriplets is compressed.
  data.setFromTriplets(tris.begin(), tris.end());
}

bool SparseMat::is_nonempty_row(int i) const {
  assert(i >=0 && i <= nrows());
  Eigen::SparseVector<double> row = data.row(i);
  return row.nonZeros() != 0;
}

bool SparseMat::is_nonempty_col(int i) const {
  assert(i >= 0 && i <= ncols());
  Eigen::SparseVector<double> col = data.col(i);
  return col.nonZeros() != 0;
}

SparseMat SparseMat::lower() const {
  SparseMat tmp;
  tmp.data = data.triangularView<Eigen::Lower>();
  return tmp;
}

SparseMat SparseMat::unit_lower() const {
  SparseMat tmp;
  tmp.data = data.triangularView<Eigen::UnitLower>();
  return tmp;
}

SparseMat SparseMat::upper() const {
  SparseMat tmp;
  tmp.data = data.triangularView<Eigen::Upper>();
  return tmp;
}

SparseMat SparseMat::unit_upper() const {
  SparseMat tmp;
  tmp.data = data.triangularView<Eigen::UnitUpper>();
  return tmp;
}

SparseMat SparseMat::transpose() const {
  SparseMat tmp;
  tmp.data = data.transpose();
  return tmp;
}

SparseMat& SparseMat::operator*=(double scalar) {
  data *= scalar;
  return *this;
}

SparseMat& SparseMat::operator/=(double scalar) {
  data /= scalar;
  return *this;
}

SparseMat& SparseMat::operator+=(const SparseMat& other) {
  data += other.data;
  return *this;
}

SparseMat& SparseMat::operator-=(const SparseMat& other) {
  data -= other.data;
  return *this;
}

SparseMat SparseMat::operator*(double scalar) const {
  SparseMat tmp;
  tmp.data = data * scalar;
  return tmp;
}

SparseMat SparseMat::operator*(const SparseMat& other) const {
  SparseMat tmp;
  tmp.data = data * other.data;
  return tmp;
}

DoubleVec SparseMat::operator*(const DoubleVec& vec) const {
  DoubleVec tmp;
  tmp.data = data * vec.data;
  return tmp;
}

SparseMat& SparseMat::add(double scalar, const SparseMat& other) {
  data += other.data * scalar;
  return *this;
}

DoubleVec SparseMat::trans_mult(const DoubleVec& x) const {
  DoubleVec result = DoubleVec(data.cols(), 0.0);
  axpy_trans(1.0, x, result);
  return result;
}

void SparseMat::axpy(double alpha, const DoubleVec &x, DoubleVec &y) const {
  // adds alpha*M*x to y.
  y.data = data * x.data * alpha + y.data;
}

void SparseMat::axpy_trans(double alpha, const DoubleVec &x, DoubleVec &y) const {
  // adds alpha*transpose(M)*x to y.
  y.data = data.transpose() * x.data * alpha + y.data;
}

void SparseMat::solve_lower_triangle(const DoubleVec& rhs, DoubleVec& x) const {
  // Solve a lower triangular matrix. rhs and x can be the same
  // vector.
  assert(is_lower_triangular(true));
  x.data = data.triangularView<Eigen::Lower>().solve(rhs.data);
}

void SparseMat::solve_lower_triangle_unitd(const DoubleVec& rhs, DoubleVec& x)
  const
{
  // Solve a lower triangular matrix assuming that the diagonal
  // elements are 1.0.  rhs and x can be the same vector.
  assert(is_lower_triangular(false)); // false ==> no diagonal elements allowed
  x.data = data.triangularView<Eigen::UnitLower>().solve(rhs.data);
}

void SparseMat::solve_lower_triangle_trans(const DoubleVec& rhs, DoubleVec& x)
  const
{
  // Solve the transpose of a lower triangular matrix with explicitly
  // stored diagonal elements.  rhs and x can be the same vector.
  assert(is_lower_triangular(true));
  x.data = data.triangularView<Eigen::Lower>().transpose().solve(rhs.data);
}

void SparseMat::solve_lower_triangle_trans_unitd(const DoubleVec& rhs,
						 DoubleVec& x)
  const
{
  // Solve a lower triangular matrix assuming that the diagonal
  // elements are 1.0.  rhs and x can be the same vector.
  assert(is_lower_triangular(false)); // false ==> no diagonal elements allowed
  x.data = data.triangularView<Eigen::UnitLower>().transpose().solve(rhs.data);
}

void SparseMat::solve_upper_triangle(const DoubleVec& rhs, DoubleVec& x) const {
  // Solve an upper triangular matrix with explicit diagonal elements.
  // rhs and x can be the same vector.
  assert(is_upper_triangular(true));
  x.data = data.triangularView<Eigen::Upper>().solve(rhs.data);
}

void SparseMat::solve_upper_triangle_trans(const DoubleVec& rhs, DoubleVec& x)
  const
{
  // Solve the transpose of an upper triangular matrix with explicit
  // diagonal elements.  rhs and x can be the same vector.
  assert(is_upper_triangular(true));
  x.data = data.triangularView<Eigen::Upper>().transpose().solve(rhs.data);
}

void SparseMat::tile(int i, int j, const SparseMat &other) {
  // TODO OPT: Don't use coeffRef for each entry.  Add other to this,
  // offset by i rows and j columns.  Or insertFromTriplets,
  // insertFromSortedTriplets, or set_from_doublets.  This could
  // significant.
  assert(i + other.nrows() <= nrows());
  assert(j + other.ncols() <= ncols());

  for(SparseMatConstIterator it=other.begin(); it<other.end(); ++it) {
    int ii = it.row() + i;
    int jj = it.col() + j;
    data.coeffRef(ii,jj) += it.value();
  }
}

// The Eigen sparse matrix does not need to be compressed for
// the iterators to work, but looping over its elements is more
// efficient if it's compressed.

SparseMatIterator SparseMat::begin() {
  return SparseMatIterator(data);
}

SparseMatIterator SparseMat::end() {
  SparseMatIterator it(data);
  it.to_end();
  return it;
}

SparseMatConstIterator SparseMat::begin() const {
  return SparseMatConstIterator(data);
}

SparseMat::const_iterator SparseMat::end() const {
  SparseMatConstIterator it(data);
  it.to_end();
  return it;
}

bool SparseMat::is_lower_triangular(bool diag) const {
  if (diag) {			// diagonal elements allowed
    for(auto it=begin(); it<end(); ++it) {
      if(it.row() < it.col())
	return false;
    }
  }
  else {
    for(auto it=begin(); it<end(); ++it) {
      if(it.row() <= it.col())
	return false;
    }
  }
  return true;
}

bool SparseMat::is_upper_triangular(bool diag) const {
  if (diag) {			// diagonal elements allowed
    for(auto it=begin(); it<end(); ++it) {
      if(it.row() > it.col())
	return false;
    }
  }
  else {
    for(auto it=begin(); it<end(); ++it) {
      if(it.row() >= it.col())
	return false;
    }
  }
  return true;
}

bool SparseMat::is_symmetric(double tolerance) const {
  assert(data.isCompressed());  
  if (data.rows() != data.cols())
    return false;
  for(auto it=begin(); it<end(); ++it) {
    double e1 = it.value();
    if(it.row() != it.col()) {
      double e2 = data.coeff(it.col(), it.row());
      if(fabs(e1-e2) > 0.5*tolerance*(fabs(e1) + fabs(e2))) {
	return false;
      }
    }
  }
  return true;
}

const std::string SparseMat::str() const {
  std::ostringstream os;
  os << *this;
  return os.str();
}

SparseMat identityMatrix(int size) {
  // make an identity matrix
  SparseMat mat(size, size);
  mat.reserve(size);
  for (int i = 0; i < size; ++i)
    mat.insert(i, i, 1);
  return mat;
}

std::ostream& operator<<(std::ostream& os, const SparseMat& mat) {
  os << mat.nrows() << " " << mat.ncols() << " " << mat.nnonzeros()
     << std::endl;
  for(SparseMatConstIterator it=mat.begin(); it<mat.end(); ++it)
    os << it.row() << " " << it.col() << " " << it.value() << std::endl;
  return os;
}

std::ostream& operator<<(std::ostream& os, const Doublet& doub) {
  os << "(" << doub.row() << ", " << doub.value() << ")";
  return os;
}

bool save_market_mat(const SparseMat& mat, const std::string& filename, int sym) {
  return Eigen::saveMarket(mat.data, filename, sym);
}

bool load_market_mat(SparseMat& mat, const std::string& filename) {
  return Eigen::loadMarket(mat.data, filename);
}

bool save_mat(const SparseMat& mat, const std::string& filename,
	      int precision, int sym)
{
  //TODO(lizhong): support symmetric matrix

  // Note: matrix needs to be compressed
  assert(mat.is_compressed());

  std::ofstream fs(filename);

  // floatfield set to scientific
  fs.setf(std::ios::scientific, std::ios::floatfield);
  fs.precision(precision);

  // save matrix row by row 

  fs << mat.nrows() << " " << mat.ncols() << " "
     << mat.nnonzeros() << std::endl;

  typedef std::tuple<int, int, double> Tri;
  std::vector<Tri> coeffs;
  coeffs.reserve(mat.nnonzeros());
  for(auto it=mat.begin(); it<mat.end(); ++it) {
    coeffs.emplace_back(it.row(), it.col(), it.value());
  }
  std::sort(coeffs.begin(), coeffs.end(),
	    [](const Tri& a, const Tri&b) -> bool {
	      return ((std::get<0>(a) < std::get<0>(b)) ||
		      (std::get<0>(a) == std::get<0>(b) &&
		       std::get<1>(a) < std::get<1>(b)));
		}
	    );
  for(auto& tri: coeffs)
    fs << std::get<0>(tri) << " " << std::get<1>(tri) << " " << std::get<2>(tri)
       << std::endl;

  return true;
}

bool load_mat(SparseMat& mat, const std::string& filename) {
  std::ifstream fs(filename);
  std::string line;
  
  // Ignore the comments at the begining of file
  while (!fs.eof()) {
    std::getline(fs, line);
    // '#' is the comment flag
    if (line[0] != '#')
      break;
  }
  // extract matrix size info
  int nr, nc, nnz;
  std::stringstream ss;
  ss << line;
  ss >> nr >> nc >> nnz;

  mat.resize(nr, nc);

  // read matrix elements
  std::vector<Eigen::Triplet<double>> trips;
  trips.reserve(nnz);
  int r, c;
  double val;
  int idebug = 0;
  for (int i = 0; i < nnz; i++) {
    fs >> r >> c >> val;
    assert(0 <= r && r < nr && 0 <= c && c < nc);
    trips.emplace_back(r, c, val);
  }
  mat.set_from_triplets(trips);
  return true;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

SMIteratorBase::SMIteratorBase(ESMat &m)
  : mat(m),
    inneriter(m, 0),
    outer(0),
    done(m.nonZeros() == 0)
{
  if(!done) {
    // Find the first non-empty row
    inneriter = ESMat::InnerIterator(mat, outer);
    while(!inneriter) {
      inneriter = ESMat::InnerIterator(mat, ++outer);
    }
  }
}

void SMIteratorBase::operator++() {
  ++inneriter;			// increment the Eigen InnerIterator
  // If we're done with this inner row/col, find the next non-empty one.
  while(outer < mat.outerSize()-1 && !inneriter) {
    inneriter = ESMat::InnerIterator(mat, ++outer);
  }
  done = not bool(inneriter);
}

SparseMatIterator& SparseMatIterator::operator++() {
  this->SMIteratorBase::operator++();
  return *this;
}

SparseMatConstIterator& SparseMatConstIterator::operator++() {
  this->SMIteratorBase::operator++();
  return *this;
}

void SMIteratorBase::to_end() {
  outer = mat.outerSize();
  done = true;
}

bool SMIteratorBase::operator==(const SMIteratorBase& other) const {
  // Iterators are equal if they're both done, or both point to the
  // same entry.  Comparing iterators from different matrices is
  // undefined.
  return ((done && other.done) ||
	  (outer == other.outer and inneriter == other.inneriter));
}

bool SMIteratorBase::operator!=(const SMIteratorBase& other) const {
  return !this->operator==(other);
}

bool SMIteratorBase::operator<(const SMIteratorBase& other) const {
  if(other.done)
    return !done;
  return (outer < other.outer ||
	  (outer == other.outer && inneriter < other.inneriter));
}
