// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CSTRAIN_SWG
#define CSTRAIN_SWG

%module cstrain

%include "common/typemaps.swg"
%import "engine/IO/propertyoutput.swg"

 // %pragma(python) code="from ooflib.SWIG.engine.IO.propertyoutput import PropertyOutputValInitPtr"
  
%{
#include "engine/cstrain.h"
#include "engine/IO/propertyoutput.h"
%}


class POInitGeometricStrain : public PropertyOutputValInit {
public:
  POInitGeometricStrain();
};

%typemap(in, numinputs=0) SymmMatrix3 *OUT (SymmMatrix3 *tmp) {
  // typemap(in, numinputs=0) SymmMatrix3 *OUT
  // TODO PYTHON3: Why use new?  Just make tmp a SymmMatrix3, not a
  // pointer, and set $1 = &tmp.
  tmp = new SymmMatrix3();
  $1 = tmp;
}

%typemap(python,argout) SymmMatrix3 *OUT {
  // typemap(python, argout) SymmMatrix3 *OUT
  FETCH_CLASS(ooflib.SWIG.engine.symmatrix, SymmMatrix3);
  // static PyObject *symmMatrix3Class = 0;
  // static PyObject *pyOne;
  // if(!symmMatrix3Class) {
  //   PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.symmmatrix");
  //   symmMatrix3Class = PyObject_GetAttrString(module, "SymmMatrix3Ptr");
  //   Py_XDECREF(module);
  //   if(!symmMatrix3Class) return 0;
  //   pyOne = PyInt_FromLong(1);
  // }
  char _stemp[128];
  SWIG_MakePtr(_stemp, (char*)($source), "_SymmMatrix3_p");
  PyObject *swigthis = Py_BuildValue("(s)", _stemp);
  PyObject *mtx = PyObject_CallObject(symmMatrix3Class, swigthis);
  Py_XDECREF(swigthis);
  PyObject_SetAttrString(mtx, "thisown", pyOne);
  $target = mtx;
}

void findGeometricStrain(FEMesh*, Element*, MasterPosition&, SymmMatrix3 *OUT,
			 bool);

%pythoncode "engine/cstrain.spy"

#endif // CSTRAIN_SWG
