// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef RANK3TENSOR_SWG
#define RANK3TENSOR_SWG

%module(package="ooflib.SWIG.engine") rank3tensor
%include "common/typemaps.swg"

%{
#include "engine/rank3tensor.h"
%}

class Rank3Tensor {
public:
  Rank3Tensor();
  ~Rank3Tensor();
  int size();
  %addmethods {
    double get(int i, int j, int k) {
      double v =  (*self)(i, j, k);
      return v;
    }
    void set(int i, int j, int k, double val) {
      (*self)(i,j, k)=val;
    }
    // *= defined in Python only for scalars.
    Rank3Tensor __imul__(double x) {
      return (*self).operator*=(x);
    }
    bool equalp(Rank3Tensor &r) {
      return (*self).operator==(r);
    }
  } 
};

%pythoncode "engine/rank3tensor.spy"

#endif // RANK3TENSOR_SWG
