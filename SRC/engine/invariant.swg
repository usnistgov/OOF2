// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef INVARIANT_SWG
#define INVARIANT_SWG

%module(package="ooflib.SWIG.engine") invariant

%include "common/typemaps.swg"

%{
#include "engine/invariant.h"
#include "common/ooferror.h"
%}

%nodefaultctor Invariant;

class Invariant {
public:
  %addmethods{
    double __call__(ArithmeticOutputVal &ov) {
      return (*self)(ov);
    }
  }
};

class Magnitude : public Invariant {
public:
  Magnitude();
};

class MatrixTrace : public Invariant {
public:
  MatrixTrace();
};

class SecondInvariant : public Invariant {
public:
  SecondInvariant();
};

class Determinant : public Invariant {
public:
  Determinant();
};

class Deviator : public Invariant {
public:
  Deviator();
};

class VonMises : public Invariant {
public:
  VonMises();
};

%typemap(in) EigenValueRank* (EigenValueRank rank) {
  // $input is a Python EigenValueRank, which is a subclass of
  // enum.Enum and defined in invariant.spy.  We're converting it to a
  // C++ EigenValueRank, which is just an enum defined in invariant.h.
  // This routine relies on the order in which the Python
  // EigenValueRank values were listed in the class definition.

  // TODO PYTHON3: Can we just swig the C++ enum now?  Or do we lose its
  // text representation?
  
  int indx = PyLong_AsLong(PyObject_CallMethod($input, (char*) "index", NULL));
  switch(indx) {
  case 0:
    rank = MAX_EIGENVALUE;
    break;
  case 1:
    rank = MID_EIGENVALUE;
    break;
  case 2:
    rank = MIN_EIGENVALUE;
    break;
  default:
    PyErr_SetString(PyExc_TypeError,
		    "in '$symname', bad EigenValueRank");
    SWIG_fail;
  }
  $1 = &rank;
}

class Eigenvalue : public Invariant {
public:
  Eigenvalue(EigenValueRank*);
};

%pythoncode "engine/invariant.spy"

#endif // INVARIANT_SWG
