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

  bool operator==(const DoubleVec&) const;
  bool operator!=(const DoubleVec&) const;

  void axpy(double alpha, const DoubleVec& x); // self += alpha*x

  DoubleVec operator+(const DoubleVec&) const;
  DoubleVec operator-(const DoubleVec&) const;
  DoubleVec operator/(double) const;
  double operator*(const DoubleVec&) const; // dot product
  DoubleVec operator*(double) const;
  
  double dot(const DoubleVec&);

  %newobject testIterator;
  static DoubleVec* testIterator(DoubleVec&);
};

%extend DoubleVec {
  //  %newobject __repr__;
  // TODO: Can __repr__ be done without copying a string?
  const std::string __repr__() {
    std::ostringstream os;
    if(self->size() > 0) {
      os << (*self)[0];
      for(int i=1; i<self->size(); i++) {
        os << " " << (*self)[i];
      }
      os << std::ends;
    }
    return std::string(os.str());
  }
  // The simpler __repr__ definition writes one vector element per
  // line, because that's what Eigen does.
  
  // %newobject __repr__;
  // const std::string* __repr__() {
  //    return new std::string((*self).str());
  // }


  void copy_inplace(DoubleVec *x) {
    *self = *x;
  }

  // TODO? Call this __copy__ instead of clone.  Then use copy.copy
  // to copy.
  %newobject clone;
  DoubleVec *clone() {
    DoubleVec* dv = new DoubleVec(*self);
    return dv;
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
  
  %newobject __rmul__;
  DoubleVec* __rmul__(double factor) {
    DoubleVec *result = new DoubleVec(*self);
    *result *= factor;
    return result;
  }

  void c_iadd(DoubleVec &other) {
    *self += other;
  }

  void c_isub(DoubleVec &other) {
    *self -= other;
  }

  void c_imul(double x) {
    *self *= x;
  }

  void c_idiv(double x) {
    *self /= x;
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
