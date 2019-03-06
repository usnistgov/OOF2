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

#include "common/smallmatrix.h"
#include <string.h>

SmallMatrix::SmallMatrix(int size) : data(size, size) {
  data.setZero(size, size);
}

SmallMatrix::SmallMatrix(int rows, int cols) : data(rows, cols) {
  data.setZero(rows, cols);
}

void SmallMatrix::resize(int rows, int cols) {
  data.resize(rows, cols);
  data.setZero(rows, cols);
}

double& SmallMatrix::operator()(int row, int col) {
  assert(row >= 0 && col >= 0 && row < data.rows() && col < data.cols());
  return data.coeffRef(row, col);
}

const double &SmallMatrix::operator()(int row, int col) const 
{
  assert(row >= 0 && col >= 0 && row < data.rows() && col < data.cols());
  return data.coeffRef(row, col);
}

SmallMatrix& SmallMatrix::operator+=(const SmallMatrix &other) {
  data += other.data;
  return *this;
}

SmallMatrix& SmallMatrix::operator-=(const SmallMatrix &other) {
  data -= other.data;
  return *this;
}

SmallMatrix& SmallMatrix::operator*=(double x) {
  data *= x;
  return *this;
}

SmallMatrix SmallMatrix::operator+(const SmallMatrix &other) const {
  SmallMatrix tmp;
  tmp.data = data + other.data;
  return tmp;
}

SmallMatrix SmallMatrix::operator-(const SmallMatrix &other) const {
  SmallMatrix tmp;
  tmp.data = data - other.data;
  return tmp;
}

// Matrix * scalar
SmallMatrix SmallMatrix::operator*(double x) const {
  SmallMatrix tmp;
  tmp.data = data * x;
  return tmp;
}

// Matrix * Matrix
SmallMatrix SmallMatrix::operator*(const SmallMatrix& other) const {
  SmallMatrix tmp;
  tmp.data = data * other.data;
  return tmp;
}

// Matrix * vector
DoubleVec SmallMatrix::operator*(const DoubleVec& other) const {
  DoubleVec tmp;
  tmp.data = data * other.data;
  return tmp;
}

// In-place transposition. Only works for square matrices.
void SmallMatrix::transpose() {
  data.transposeInPlace();
}

int SmallMatrix::solve(SmallMatrix &rhs) const {
  // This routine modifies the contents both of the "host" matrix
  // and the passed-in rhs.  
  rhs.data = data.fullPivLu().solve(rhs.data);

  //TODO(lizhong): remove return value
  return 0;
}

int SmallMatrix::symmetric_invert() {
  data = data.inverse();

  //TODO(lizhong): remove return value
  return 0;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// SmallMatrix3x3::SmallMatrix3x3(double a00, double a01, double a02,
// 			       double a10, double a11, double a12,
// 			       double a20, double a21, double a22)
//   : SmallMatrix(3, 3)
// {
//   data <<
//     a00, a01, a02,
//     a10, a11, a12,
//     a20, a21, a22;
// }


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream& operator<<(std::ostream &os, const SmallMatrix& mat) {
  // for(int i=0; i<mat.rows(); i++) {
  //   for(int j=0; j<mat.cols(); j++) 
  //     os << " " << mat(i,j);
  //   os << std::endl;
  // }

  os << "[";
  for(int i=0; i<mat.rows(); i++) {
    if(i > 0)
      os << ", ";
    os << "[";
    for(int j=0; j<mat.cols(); j++) {
      if(j > 0)
	os << ", ";
      os << mat(i, j);
    }
    os << "]";
  }
  os << "]";
  return os;
}
