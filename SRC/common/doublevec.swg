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
  void scale(double alpha);
  double dot(const DoubleVec&);

  const std::string str() const;
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
  // TODO PYTHON3: Check that allocated vector is cleaned up properly.
  DoubleVec *clone() {
    return new DoubleVec(*self);
  }

  // Increment the entry at index i by the amount v.
  // Do not use this too much.
  void increment(int i, double v) {
    (*self)[i] += v;
  }

  void save(const char *filename) {
    save_vec(*self, std::string(filename));
  }

  void load(const char *filename) {
    load_vec(*self, std::string(filename));
  }
};

%pythoncode "common/doublevec.spy"

#endif // DOUBLEVEC_SWG
