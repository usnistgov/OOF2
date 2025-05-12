// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <unsupported/Eigen/SparseExtra>
#include "common/doublevec.h"
#include <sstream>
#include <fstream>

// bool verboseVectors = false;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// TODO: Remove this section after debugging is complete.  All methods
// should be defined inline in doublevec.h.

// int DoubleVec::idcount_ = 0;
  
DoubleVec::~DoubleVec() {
  // if(verbose_)
  //   std::cerr << "DoubleVec DESTRUCTOR: size=" << size()
  // 	      << " addr=" << addr() << std::endl;
}

DoubleVec::DoubleVec()
  // : verbose_(verboseVectors),
  //   id_(idcount_++)
{
  // if(verbose_)
  //   std::cerr << "DoubleVec null constructor: size=" << size()
  // 	      << " addr=" << addr() << std::endl;
}

DoubleVec::DoubleVec(int size, double val)
  // : verbose_(verboseVectors),
  //   id_(idcount_++)
{
  data.setConstant(size, val);
}

DoubleVec::DoubleVec(const std::initializer_list<double> &vals)
  : data({vals}) //,
    // verbose_(verboseVectors),
    // id_(idcount_++)
{}

DoubleVec::DoubleVec(const DoubleVec &other)
  : data(other.data) //,
    // verbose_(other.verbose_)
{
  // id_ = ++idcount_;
  // if(verbose_)
  //   std::cerr << "DoubleVec copy constructor: src=" << other.addr()
  // 	      << " dst=" << addr() << std::endl;
}

DoubleVec::DoubleVec(DoubleVec &&other)
  : data(std::move(other.data)) //,
    // verbose_(other.verbose_)
{
  // id_ = other.id_;
  other.data.resize(0);
  // if(verbose_)
  //   std::cerr << "DoubleVec move constructor: src=" << other.addr()
  // 	      << " dst=" << addr() << std::endl;
}

// This is not quite the same syntax as Python.  x=y in Python usually
// does not create a new object, just a new reference to an old
// object, meaning that x=y;y+=z will leave x set to y+z.  What do we
// want DoubleVec::operator= to do in Python?
DoubleVec& DoubleVec::operator=(const DoubleVec &other) {
  data = other.data;
  // verbose_ = other.is_verbose();
  // if(verbose_)
  //   std::cerr << "DoubleVec::operator=: src=" << other.addr()
  // 	      << "dst=" << addr() << std::endl;
  return *this;
}

// std::string DoubleVec::addr() const {
//   return tostring(this) + "(" + tostring(id_) + ")";
// }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//



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

bool DoubleVec::operator==(const DoubleVec& other) const {
  return data == other.data;
}

bool DoubleVec::operator!=(const DoubleVec& other) const {
  return data != other.data;
}

const DoubleVec& DoubleVec::operator+=(const DoubleVec& other) {
  // std::cerr << "DoubleVec::operator+=: this=" << addr()
  // 	    << " other=" << other.addr() << std::endl;
  assert(other.size() == size());
  data += other.data;
  return *this;
}

const DoubleVec& DoubleVec::operator-=(const DoubleVec& other) {
  assert(other.size() == size());
  data -= other.data;
  assert(other.size() == size());
  return *this;
}

const DoubleVec& DoubleVec::operator*=(double alpha) {
  data *= alpha;
  return *this;
}

const DoubleVec&  DoubleVec::operator/=(double alpha) {
  data /= alpha;
  return *this;
}

void DoubleVec::axpy(double alpha, const DoubleVec& x) {
  assert(x.size() == size());
  // TODO: Check to see if Eigen does this in one loop or two.
  data += alpha * x.data;
}

DoubleVec DoubleVec::operator+(const DoubleVec& other) const {
  // std::cerr << "DoubleVec::operator+: copying" << std::endl;
  DoubleVec result(*this);
  // std::cerr << "DoubleVec::operator+: this=" << addr()
  // 	    << " other=" << other.addr()
  // 	    << " result=" << result.addr() << std::endl;
  result.data += other.data;
  // std::cerr << "DoubleVec::operator+: done" << std::endl;
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
