// -*- C++ -*-

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

#include <iostream>
#include <string>
#include "Eigen/Dense"
#include <initializer_list>

class SparseMat;
class SmallMatrix;
enum class Precond;
template<typename Derived> class IterativeSolver;
template<typename Derived> class DirectSolver;

// TODO? Derive DoubleVec from Eigen::VectorXd, instead of wrapping it.

class DoubleVec {
private:
  Eigen::VectorXd data;		// N x 1 matrix

public:
  DoubleVec() = default;
  DoubleVec(int size, double val=0) { data.setConstant(size, val); }
  DoubleVec(const std::initializer_list<double> &v) : data({v}) {}
  DoubleVec(const DoubleVec&) = default;
  DoubleVec(DoubleVec&&) = default;
  DoubleVec& operator=(const DoubleVec&) = default;
  ~DoubleVec() = default;

  /* Vector property methods */
  
  std::size_t size() const { return data.size(); }
  void resize(std::size_t size, double val=0) { data.setConstant(size, val); }
  void zero() { data.setZero(); }
  void clear() { zero(); }
  void unit() { data.setOnes(); }
  double& operator[](std::size_t index) { return data[index]; }
  double operator[](std::size_t index) const { return data[index]; }
  DoubleVec subvec(std::size_t start, std::size_t end) const;
  void subvec_copy(std::size_t, const DoubleVec&, std::size_t, std::size_t);

  typedef std::size_t size_type;

  bool operator==(const DoubleVec&) const;
  bool operator!=(const DoubleVec&) const;

  /* Arithmetic operations */

  // In-place operations, using no temporaries. Python and swig expect
  // these to return a self reference.
  DoubleVec& operator+=(const DoubleVec&);
  DoubleVec& operator-=(const DoubleVec&);
  DoubleVec& operator*=(double);
  DoubleVec& operator/=(double);
  void axpy(double alpha, const DoubleVec& x);
  
  // Not in-place. These may return a temporary object, although the
  // move constructor should make that cheap.
  DoubleVec operator+(const DoubleVec&) const;
  DoubleVec operator-(const DoubleVec&) const;
  DoubleVec operator-() const;
  DoubleVec operator*(double) const;
  DoubleVec operator/(double) const;
  friend DoubleVec operator*(double, const DoubleVec&);

  // Dot product
  double dot(const DoubleVec&) const;
  double operator*(const DoubleVec&) const;
  double norm() const { return data.norm(); }

  // Iterators
  typedef Eigen::VectorXd::iterator iterator;
  typedef Eigen::VectorXd::const_iterator const_iterator;
  iterator begin() { return data.begin(); }
  iterator end() { return data.end(); }
  const_iterator begin() const { return data.begin(); }
  const_iterator end() const { return data.end(); }

  /* Miscellaneous */

  const std::string str() const;

  friend SparseMat;
  friend SmallMatrix;
  template<typename Derived> friend class IterativeSolver;
  template<typename Derived> friend class DirectSolver;
  friend std::ostream& operator<<(std::ostream&, const DoubleVec&);
  friend bool save_market_vec(const DoubleVec&, const std::string&);
  friend bool load_market_vec(DoubleVec&, const std::string&);
  friend bool save_vec(const DoubleVec&, const std::string&);
  friend bool load_vec(DoubleVec&, const std::string&);

  static DoubleVec* testIterator(DoubleVec&);
};

#endif // DOUBLEVEC_H
