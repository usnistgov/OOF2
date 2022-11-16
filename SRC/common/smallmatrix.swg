// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */


#ifndef SMALLMATRIX_SWG
#define SMALLMATRIX_SWG

%module(package="ooflib.SWIG.common") smallmatrix

%include "common/typemaps.swg"

%{
#include "common/smallmatrix.h"
%}

class SmallMatrix {
public:
  SmallMatrix(int, int);
  ~SmallMatrix();
  void clear();
  int solve(SmallMatrix &);
  void scale(double);
  void madd(SmallMatrix&);
  void msub(SmallMatrix&);
};

%extend SmallMatrix {
  double getitem(int i, int j) {
    return (*self)(i,j);
  }
  void setitem(int i, int j, double v) {
    (*self)(i,j)=v;
  }
  %newobject copy;
  SmallMatrix *copy() {
    return new SmallMatrix(*self);
  }
    // The rest of the arithmetic operators are defined in
    // smallmatrix.spy.  We used to do them here, like this:
    //     SmallMatrix __add__(const SmallMatrix &x) {
    //       return self->operator+(x);
    //     }
    // The trouble with that is that returning a SmallMatrix rather
    // than a SmallMatrix* causes swig to generate an extra copy
    // constuctor call:
    //     _result = new SmallMatrix (SmallMatrix___add__(_arg0,*_arg1));
    // By using copy() (which returns a SmallMatrix*) and swigged
    // in-place arithmetic operations we avoid the extra copy.

    // In swig4, Setting the "optimal" option on the out typemap would
    // eliminate the copy, but that doesn't work if we have an
    // %exception typemap.

  // Matrix multiplication is *not* done the same way, because we
  // don't have an in-place C++ matrix multiplication operator.
  %newobject mmult;
  SmallMatrix *mmult(SmallMatrix &other) {
    // With luck, C++ will optimize away the copy constructor here.
    return new SmallMatrix((*self)*other);
  }
};

%pythoncode "common/smallmatrix.spy"

#endif
