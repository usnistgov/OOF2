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
#include "Eigen/SparseCore"
#include <initializer_list>

#include "common/tostring.h"

class SparseMat;
class SmallMatrix;
template<typename VT, typename ET> class DoubleVecIterator;
enum class Precond;
template<typename Derived> class IterativeSolver;
template<typename Derived> class DirectSolver;

// TODO? Derive DoubleVec from Eigen::VectorXd, instead of wrapping it.

extern bool verboseVectors;

class DoubleVec {
public:			     // TODO: Make private when done debugging
  Eigen::VectorXd data;	     // N x 1 matrix
  mutable bool verbose_;     // TODO: remove when done debugging
  void verbose(bool flag) const { verbose_ = flag; }
  bool is_verbose() const { return verbose_; }

public:
  DoubleVec() : verbose_(verboseVectors) {} 
  DoubleVec(int size, double val=0)
    : verbose_(verboseVectors)
  { data.setConstant(size, val); }
  DoubleVec(const std::initializer_list<double> &v)
    : data({v}), verbose_(verboseVectors)
  {}
  DoubleVec(const DoubleVec&) = default;
  DoubleVec(DoubleVec&&) = default;
  DoubleVec& operator=(const DoubleVec&) = default;
  ~DoubleVec();

  std::string addr() const { return tostring(this); }
 
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

  // In-place operations, using no temporaries
  DoubleVec& operator+=(const DoubleVec&);
  DoubleVec& operator-=(const DoubleVec&);
  DoubleVec& operator*=(double);
  DoubleVec& operator/=(double);
  void axpy(double alpha, const DoubleVec& x);
  
  // Non-in-place, which may return a temporary object, although the
  // move constructor should make that cheap.
  DoubleVec operator+(const DoubleVec&) const;
  DoubleVec operator-(const DoubleVec&) const;
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

  friend DoubleVec* __isub__(const DoubleVec&);

  static DoubleVec* testIterator(DoubleVec&);
};

#endif // DOUBLEVEC_H
