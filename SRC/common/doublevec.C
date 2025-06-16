// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "common/doublevec.h"
#include <sstream>
#include <fstream>

// for saveMarketVector and loadMarketVector
#include <unsupported/Eigen/SparseExtra> 


DoubleVec DoubleVec::subvec(std::size_t start, std::size_t end) const {
  // Extract the n coeffs in the range [start : end-1]
  assert(start<=end && end<=data.size());
  DoubleVec part;
  part.data = data.segment(start, end-start);
  return part;
}

void DoubleVec::subvec_copy(std::size_t toPos, const DoubleVec& other,
			    std::size_t pos, std::size_t size) {
  // Copy other's [pos, pos+size) to this [toPos, toPos+size)
  assert(pos >= 0 && pos + size <= other.data.size());
  assert(toPos >= 0 && toPos + size <= data.size());
  data.segment(toPos, size) = other.data.segment(pos, size);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

bool DoubleVec::operator==(const DoubleVec& other) const {
  return data == other.data;
}

bool DoubleVec::operator!=(const DoubleVec& other) const {
  return data != other.data;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

DoubleVec& DoubleVec::operator+=(const DoubleVec& other) {
  assert(other.size() == size());
  data += other.data;
  return *this;
}

DoubleVec& DoubleVec::operator-=(const DoubleVec& other) {
  assert(other.size() == size());
  data -= other.data;
  assert(other.size() == size());
  return *this;
}

DoubleVec& DoubleVec::operator*=(double alpha) {
  data *= alpha;
  return *this;
}

DoubleVec& DoubleVec::operator/=(double alpha) {
  data /= alpha;
  return *this;
}

void DoubleVec::axpy(double alpha, const DoubleVec& x) {
  assert(x.size() == size());
  // TODO: Check to see if Eigen does this in one loop or two.
  data += alpha * x.data;
}

DoubleVec DoubleVec::operator+(const DoubleVec& other) const {
  DoubleVec result(*this);
  result.data += other.data;
  return result;
}

DoubleVec DoubleVec::operator-(const DoubleVec& other) const {
  DoubleVec result(*this);
  result.data -= other.data;
  return result;
}

// Unary -
DoubleVec DoubleVec::operator-() const {
  DoubleVec result(*this);
  result *= -1;
  return result;
}

DoubleVec DoubleVec::operator*(double alpha) const {
  DoubleVec result(*this);
  result.data *= alpha;
  return result;
}

DoubleVec DoubleVec::operator/(double alpha) const {
  DoubleVec result(*this);
  result.data /= alpha;
  return result;
}

// Friend method of DoubleVec, return the result of (scalar * vec)
DoubleVec operator*(double alpha, const DoubleVec& mat) {
  DoubleVec result;
  result.data = alpha * mat.data;
  return result;
}

double DoubleVec::dot(const DoubleVec& other) const {
  return data.dot(other.data); 
}

double DoubleVec::operator*(const DoubleVec& other) const {
  return data.dot(other.data); 
}

const std::string DoubleVec::str() const {
  std::ostringstream os;
  os << data;
  return os.str();
}

std::ostream& operator<<(std::ostream& os, const DoubleVec& vec) {
  bool notfirst = false;
  for(double x : vec) {
    if(notfirst)
      os << " ";
    else
      notfirst = true;
    os << x;
  }
  return os;
}

// TODO: Eigen 3.4.90 documentation says to use saveMarketDense and
// loadMarketDense instead of saveMarketVector and loadMarketVector,
// but it doesn't compile that way.  Perhaps because we're using
// version 3.4.0?

bool save_market_vec(const DoubleVec& vec, const std::string& filename) {
  return Eigen::saveMarketVector(vec.data, filename);
}

bool load_market_vec(DoubleVec& vec, const std::string& filename) {
  return Eigen::loadMarketVector(vec.data, filename);
}

bool save_vec(const DoubleVec& vec, const std::string& filename) {
  int precision = 13;
  std::ofstream fs(filename); 
  // floatfield set to scientific
  fs.setf(std::ios::scientific, std::ios::floatfield);
  fs.precision(precision);

  std::size_t size = vec.size();
  fs << vec.size() << std::endl;
  for (std::size_t i = 0; i < size; i++) {
    fs << vec.data[i] << std::endl;
  }
  return true;
}

bool load_vec(DoubleVec& vec, const std::string& filename) {
  std::ifstream fs(filename);
  std::string line;
  
  // Ignore the comments at the begining of file
  while (!fs.eof()) {
    std::getline(fs, line);
    // '#' is the comment flag
    if (line[0] != '#')
      break;
  }

  // extract vector size info
  std::size_t size;
  std::stringstream ss;
  ss << line;
  ss >> size;

  vec.resize(size);

  // read vector
  double val;
  for (std::size_t i = 0; i < size; i++) {
    fs >> val;
    vec.data[i] = val;
  }

  return true;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// For testing iteration

// static
DoubleVec* DoubleVec::testIterator(DoubleVec &vec) {
  DoubleVec *result = new DoubleVec(vec.size(), 0.0);

  // traditional for loop
  for(int i=0; i<vec.size(); ++i) {
    (*result)[i] = vec[i];
  }
  
  // range-base for loop
  int i = 0;
  for(double x : vec) {
    (*result)[i++] += 2*x;
  }
  
  // STL-like for loop
  auto itr = result->data.begin();
  auto itv = vec.data.begin();
  for(; itr<result->data.end() && itv < vec.data.end(); ++itr, ++itv) {
    *itr += 4*(*itv);
  }
  return result;
    
}
