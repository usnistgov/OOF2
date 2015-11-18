/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef DOUBLEVEC_H
#define DOUBLEVEC_H

#include <Eigen/SparseCore>
#include <iostream>
#include <string>

class SparseMat;

class DoubleVec {
public:
  DoubleVec() = default;
  DoubleVec(int size, double val=0) { data.setConstant(size, val); }
  DoubleVec(const DoubleVec&) = default;
  DoubleVec& operator=(const DoubleVec&) = default;
  ~DoubleVec() = default;
  
  //TODO(lizhong): inline possible methods
  
  //TODO(lizhong): implement subscript operator

  /* Vector property methods */

  int size() const { return data.size(); }
  void resize(int size, double val=0) { data.setConstant(size, val); }
  void zero() { data.setZero(); }
  void unit() { data.setOnes(); }

  /* Arithmetic operations */

  double norm() const { return data.norm(); }

  // In-place operations, using no temporaries
  DoubleVec& operator+=(const DoubleVec&);
  DoubleVec& operator-=(const DoubleVec&);
  DoubleVec& operator*=(double);
  DoubleVec& operator/=(double);
  void axpy(double alpha, const DoubleVec& x);
  void scale(double alpha);
  
  // Non-in-place, which may return a temporary object.
  DoubleVec operator+(const DoubleVec&);
  DoubleVec operator-(const DoubleVec&);
  DoubleVec operator*(double);
  DoubleVec operator/(double);
  friend DoubleVec operator*(double, const DoubleVec&);

  // dot product
  double dot(const DoubleVec&);
  double operator*(const DoubleVec&);

  /* Miscellaneous */

  const std::string str() const;

  friend SparseMat;
  friend std::ostream& operator<<(std::ostream&, const DoubleVec&);
  friend bool save_market_vec(const DoubleVec&, const std::string&);
  friend bool load_market_vec(DoubleVec&, const std::string&);
  friend bool save_vec(const DoubleVec&, const std::string&, int precision=13);
  friend bool load_vec(DoubleVec&, const std::string&);

private:
  Eigen::VectorXd data; // N x 1 matrix
};

// TODO(lizhong): interators for doubelvec

#endif // DOUBLEVEC_H
