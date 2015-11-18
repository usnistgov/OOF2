/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <unsupported/Eigen/SparseExtra>
#include "doublevec.h"
#include <sstream>
#include <fstream>

DoubleVec& DoubleVec::operator+=(const DoubleVec& other) {
  data += other.data; 
  return *this;
}

DoubleVec& DoubleVec::operator-=(const DoubleVec& other) {
  data -= other.data;
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

void DoubleVec::scale(double alpha) {
  data *= alpha;
}

void DoubleVec::axpy(double alpha, const DoubleVec& x) {
  data += alpha * x.data;
}

DoubleVec DoubleVec::operator+(const DoubleVec& other) {
  DoubleVec rst;
  rst.data = data + other.data;
  return rst;
}

DoubleVec DoubleVec::operator-(const DoubleVec& other) {
  DoubleVec rst;
  rst.data = data - other.data;
  return rst;
}

DoubleVec DoubleVec::operator*(double alpha) {
  DoubleVec rst;
  rst.data = data * alpha;
  return rst;
}

DoubleVec DoubleVec::operator/(double alpha) {
  DoubleVec rst;
  rst.data = data / alpha;
  return rst;
}

// Friend method of DoubleVec, return the result of (scalar * vec)
DoubleVec operator*(double alpha, const DoubleVec& mat) {
  DoubleVec rst;
  rst.data = alpha * mat.data;
  return rst;
}

double DoubleVec::dot(const DoubleVec& other) {
  return data.dot(other.data); 
}

double DoubleVec::operator*(const DoubleVec& other) {
  return data.dot(other.data); 
}

const std::string DoubleVec::str() const {
  std::ostringstream os;
  os << data;
  return os.str();
}

std::ostream& operator<<(std::ostream& os, const DoubleVec& vec) {
  os << vec.data;  
  return os;
}

bool save_market_vec(const DoubleVec& vec, const std::string& filename) {
  return Eigen::saveMarketVector(vec.data, filename);
}

bool load_market_vec(DoubleVec& vec, const std::string& filename) {
  return Eigen::loadMarketVector(vec.data, filename);
}

bool save_vec(const DoubleVec& vec, const std::string& filename, int precision) {
  std::ofstream fs(filename); 
  // floatfield set to scientific
  fs.setf(std::ios::scientific, std::ios::floatfield);
  fs.precision(precision);

  int size = vec.size();
  fs << vec.size() << std::endl;
  for (int i = 0; i < size; i++) {
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
  int size;
  std::stringstream ss;
  ss << line;
  ss >> size;

  vec.resize(size);

  // read vector
  double val;
  for (int i = 0; i < size; i++) {
    fs >> val;
    vec.data[i] = val;
  }

  return true;
}

