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

%feature("valuewrapper") DoubleVec;

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

  // Swig apparently expects the in-place arithmetic operators to
  // return a self reference.  I don't know why.  x=(y+=z) and
  // (x+=y)=z are not valid python.  But if they return void the
  // DoubleVec reference counting is incorrect, and a DoubleVec might
  // be deleted too soon.
  const DoubleVec& operator+=(const DoubleVec&);
  const DoubleVec& operator-=(const DoubleVec&);
  const DoubleVec& operator/=(double);
  const DoubleVec& operator*=(double);
  void axpy(double alpha, const DoubleVec& x); // self += alpha*x 

  DoubleVec operator+(const DoubleVec&) const;
  DoubleVec operator-(const DoubleVec&) const;
  DoubleVec operator/(double) const;
  double operator*(const DoubleVec&) const; // dot product
  DoubleVec operator*(double) const;
  
  double dot(const DoubleVec&);

  // Debugging routines
  const std::string str() const;
  const std::string addr() const;
  void verbose(bool);
  bool is_verbose() const;

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
    // if(self->is_verbose()) {
    //   dv->verbose(true);
    //   std::cerr << "DoubleVec.clone: src=" << self->addr()
    // 		<< "  dst=" << dv->addr() << std::endl;
    // }
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
  
  // void increment(int i, double v) { // TODO: Do we use this?  
  //   (*self)[i] += v;
  // }

  // %newobject __add__;
  // DoubleVec* __add__(const DoubleVec& other) {
  //   assert(self->size() == other.size());
  //   DoubleVec *result = new DoubleVec(*self);
  //   result->data += other.data;
  //   return result;
  // }

  // %newobject __sub__;
  // DoubleVec* __sub__(const DoubleVec& other) {
  //   DoubleVec *result = new DoubleVec(*self);
  //   result->data -= other.data;
  //   return result;
  // }

  // %newobject __truediv__;
  // DoubleVec *__truediv__(double factor) {
  //   DoubleVec* result = new DoubleVec(*self);
  //   result->data /= factor;
  //   return result;
  // }

  %newobject __rmul__;
  DoubleVec* __rmul__(double factor) {
    DoubleVec *result = new DoubleVec(*self);
    *result *= factor;
    return result;
  }

  // For some reason, swigging __iadd__, __isub__, and __itruediv__
  // doesn't work.  The reference count of the result is incorrect and
  // it's deleted too soon.  But swig knows what to do with
  // operator+=, etc.
  // TODO: Perhaps that was because it was returning *self instead of void?

  // void operator+=(const DoubleVec& other) {
  //   assert(0);
  //   std::cerr << "operator+=" << self->addr() << " " << other.addr() << std::endl;
  //   assert(self->size() == other.size());
  //   self->data += other.data;
  // }

  // void operator-=(const DoubleVec& other) {
  //   assert(self->size() == other.size());
  //   self->data -= other.data;
  // }

  // void operator/=(double factor) {
  //   self->data /= factor;
  // }

  // void operator*=(double factor) {
  //   self->data *= factor;
  // }

  // DoubleVec::__mul__, __rmul__, and __imul__ are defined in Python
  // (in doublevec.spy) so that they can check their argument type and
  // distinguish between vector*factor, factor*vector, and
  // vector*vector.  They call the methods c_mul, c_rmul, and c_imul
  // that are defined here.

  // %newobject c_mul;
  // DoubleVec* c_mul(double factor) {
  //   DoubleVec* result = new DoubleVec(*self);
  //   *result *= factor;
  //   return result;
  // }

  // %newobject c_rmul;
  // DoubleVec* c_rmul(double factor) {
  //   DoubleVec* result = new DoubleVec(*self);
  //   *result *= factor;
  //   return result;
  // }

  // DoubleVec* c_imul(double factor) {
  //   *self *= factor;
  //   return self;
  // }

  // bool __eq__(const DoubleVec &other) {
  //   assert(self->size() == other.size());
  //   return *self == other;
  // }

  // bool __ne__(const DoubleVec &other) {
  //   assert(self->size() == other.size());
  //   return *self != other;
  // }

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

// %pythoncode "common/doublevec.spy"

#endif // DOUBLEVEC_SWG
