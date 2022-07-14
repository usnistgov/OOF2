// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MASTERCOORD_SWG
#define MASTERCOORD_SWG

%module(package="ooflib.SWIG.engine") mastercoord

%include "common/typemaps.swg"

%{
#include "engine/mastercoord.h"
%}

%typemap(in) MasterCoord *Point (MasterCoord mc) {
  // typemap(in) MasterCoord *Point
  PyObject *xobj = PySequence_GetItem($input, 0);
  PyObject *yobj = PySequence_GetItem($input, 1);
  if(!xobj || !yobj) {
    PyErr_SetString(
	    PyExc_TypeError,
	    "in method '$symname'.  Argument must have 0 and 1 components.");
    SWIG_fail;
  }

  mc(0) = PyFloat_AsDouble(xobj);
  mc(1) = PyFloat_AsDouble(yobj);
  Py_XDECREF(xobj);
  Py_XDECREF(yobj);
  $1 = &mc;
}

%nodefaultctor MasterPosition;

class MasterPosition {
public:
  MasterCoord mastercoord();
};

class MasterCoord : public MasterPosition {
public:
  MasterCoord(double x1, double x2);
  ~MasterCoord();
};

%extend MasterCoord {
  double __getitem__(int i) {
    return (*self)(i);
  }
  MasterCoord __add__(MasterCoord &other) {
    return *self + other;
  }
  MasterCoord __sub__(MasterCoord &other) {
    return *self - other;
  }
  MasterCoord __mul__(double a) {
    return a*(*self);
  }
  MasterCoord __div__(double a) {
    return *self/a;
  }
};

MAKE_LISTVEC_TYPEMAPS(MasterCoord);

%pythoncode "engine/mastercoord.spy"

#endif // MASTERCOORD_SWG

