// -*- C++ -*-
/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef RAMBERGOSGOOD_SWG
#define RAMBERGOSGOOD_SWG

%module(package="ooflib.SWIG.EXTENSIONS.ramberg_osgood") ramberg_osgood

%{
#include "EXTENSIONS/ramberg_osgood/ramberg_osgood.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/nonlinear/general_nonlinear_elasticity.swg"
%import "engine/properties/elasticity/cijkl.swg"

// // Typemap for conversion between the parameter type
// // (IsotropicRank4Tensor) and the internal type, which is the swig'd Cijkl
// // object from engine/property/elasticity/cijkl.h"
// %typemap(python,in) Cijkl* {
//   PyObject *basevalue = PyObject_CallMethod($source,"to_base",NULL);
//   if(!basevalue) {
// //     acquirePyLock();  // TODO: Why was this line here?
//     restoreSignals;
//     return 0;
//   }
  
//   PyObject *c11_float = PyObject_GetAttrString(basevalue,"c11");
//   PyObject *c12_float = PyObject_GetAttrString(basevalue,"c12");

//   double c11 = PyFloat_AsDouble(c11_float);
//   double c12 = PyFloat_AsDouble(c12_float);

//   Py_DECREF(c11_float);
//   Py_DECREF(c12_float);

//   $target = new Cijkl;
//   (*$target)(0,0) = (*$target)(1,1) = (*$target)(2,2) = c11;
//   (*$target)(0,1) = (*$target)(0,2) = (*$target)(1,2) = c12;
//   (*$target)(3,3) = (*$target)(4,4) = (*$target)(5,5) = 0.5*(c11-c12);

// }

// %typemap(python,freearg) Cijkl* {
//   delete $source;
// }


class RambergOsgood : public GeneralNonlinearElasticity {
public:
  RambergOsgood(PyObject *reg, char *name, Cijkl &cijkl,
		double alpha, double s0, double n);
};


// %typemap(python,in) Cijkl* {}
// %typemap(Python,freearg) Cijkl* {}

%pythoncode "ramberg_osgood.spy"

#endif // RAMBERGOSGOOD_SWG
