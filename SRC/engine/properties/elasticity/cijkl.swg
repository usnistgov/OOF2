// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CIJKL_SWG
#define CIJKL_SWG

%module(package="ooflib.SWIG.engine.properties.elasticity") cijkl

%include "common/typemaps.swg"
%import "engine/symmmatrix.swg"

%{
#include "engine/properties/elasticity/cijkl.h"
%}

class Cijkl {
public:
  Cijkl();
  void clear();
};

%extend Cijkl {
  double get(int i, int j, int k, int l) {
    return (*self)(i, j, k, l);
  }
  double getvoigt(int i, int j) {
    return (*self)(i, j);
  }
  void set(int i, int j, int k, int l, double val) {
    (*self)(i, j, k, l) = val;
  }
  void setvoigt(int i, int j, double val) {
    (*self)(i, j) = val;
  }
  SymmMatrix3 __mul__(SymmMatrix3 &other) {
    return (*self)*other;
  }
}

%pythoncode "engine/properties/elasticity/cijkl.spy"

#endif // CIJKL_SWIG
