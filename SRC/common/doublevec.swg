// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef DOUBLEVEC_SWG
#define DOUBLEVEC_SWG

%module(package="ooflib.SWIG.common") doublevec

%include "common/typemaps.swg"

%{
#include "common/doublevec.h"
%}

class DoubleVec {
public:
  DoubleVec(int size, double val=0);
  ~DoubleVec();
  
  int size() const;
  void resize(int size, double val=0);
  void zero();
  void unit();

  double norm() const;

  void axpy(double alpha, const DoubleVec& x);
  double dot(const DoubleVec&);

  const std::string str() const;
  const std::string addr() const;
  void verbose(bool);

  %newobject testIterator;
  static DoubleVec* testIterator(DoubleVec&);
};

%extend DoubleVec {
  %newobject __repr__;
  const std::string* __repr__() {
     return new std::string((*self).str());
  }

  void copy_inplace(DoubleVec *x) {
    *self = *x;
  }

  %newobject clone;
  DoubleVec *clone() {
    return new DoubleVec(*self);
  }

  void save(const char *filename) {
    save_vec(*self, std::string(filename));
  }

  void load(const char *filename) {
    load_vec(*self, std::string(filename));
  }

  int __len__() {
    return self->size();
  }

  %newobject __neg__;
  DoubleVec* __neg__() {
    DoubleVec *a = new DoubleVec(*self);
    *a *= -1.0;
    return a;
  }
  
  void increment(int i, double v) { // TODO: Do we use this?  
    (*self)[i] += v;
  }

  %newobject __add__;
  DoubleVec* __add__(const DoubleVec& other) {
    assert(self->size() == other.size());
    DoubleVec *result = new DoubleVec(*self);
    result->data += other.data;
    return result;
  }

  %newobject __sub__;
  DoubleVec* __sub__(const DoubleVec& other) {
    DoubleVec *result = new DoubleVec(*self);
    result->data -= other.data;
    return result;
  }

  %newobject __truediv__;
  DoubleVec *__truediv__(double factor) {
    DoubleVec* result = new DoubleVec(*self);
    result->data /= factor;
    return result;
  }

  // For some reason, swigging __iadd__, __isub__, and __itruediv__
  // doesn't work.  The reference count of the result is incorrect and
  // it's deleted too soon.  But swig knows what to do with
  // operator+=, etc.

  DoubleVec* operator+=(const DoubleVec& other) {
    assert(self->size() == other.size());
    self->data += other.data;
    return self;
  }

  DoubleVec* operator-=(const DoubleVec& other) {
    assert(self->size() == other.size());
    self->data -= other.data;
    return self;
  }

  DoubleVec* operator/=(double factor) {
    self->data /= factor;
    return self;
  }

  // DoubleVec::__mul__, __rmul__, and __imul__ are defined in Python
  // (in doublevec.spy) so that they can check their argument type and
  // distinguish between vector*factor, factor*vector, and
  // vector*vector.  They call the methods c_mul, c_rmul, and c_imul
  // that are defined here.

  %newobject c_mul;
  DoubleVec* c_mul(double factor) {
    DoubleVec* result = new DoubleVec(*self);
    *result *= factor;
    return result;
  }

  %newobject c_rmul;
  DoubleVec* c_rmul(double factor) {
    DoubleVec* result = new DoubleVec(*self);
    *result *= factor;
    return result;
  }

  DoubleVec* c_imul(double factor) {
    *self *= factor;
    return self;
  }

  %newobject __truediv__;
  DoubleVec* __truediv__(double factor) {
    DoubleVec* result = new DoubleVec(*self);
    *result *= 1./factor;
    return result;
  }
  
  DoubleVec* __itruediv__(double factor) {
    (*self) *= 1./factor;
    return self;
  }

  bool __eq__(const DoubleVec &other) {
    assert(self->size() == other.size());
    return *self == other;
  }

  bool __ne__(const DoubleVec &other) {
    assert(self->size() == other.size());
    return *self != other;
  }

  // Accessing individual items from python is highly discouraged but
  // is useful for testing and debugging.  Iteration in Python is not
  // supported, other than by using __getitem__() and __setitem__().
  double __getitem__(int i) {
    return (*self)[i];
  }
  void __setitem__(int i, double value) {
    (*self)[i] = value;
  }

  

};				// %extend DoubleVec

%pythoncode "common/doublevec.spy"

#endif // DOUBLEVEC_SWG
