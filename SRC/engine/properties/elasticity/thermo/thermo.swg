// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ELASTICITY_THERMO_SWG
#define ELASTICITY_THERMO_SWG

%module(package="ooflib.SWIG.engine.properties.elasticity.thermo") thermo

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/properties/elasticity/cijkl.swg"
%import "engine/properties/elasticity/elasticity.swg"
#endif // NOSECONDIMPORTS

 //%pragma(python) code="from ooflib.SWIG.engine.property.elasticity.cijkl import CijklPtr"

%{
#include "engine/properties/elasticity/thermo/thermo.h"
%}

// // Typemap for conversion between the parameter type
// // (IsotropicModulus) and the internal type, which is the swig'd Cijkl
// // object from engine/properties/elasticity/cijkl.h"
// /// TODO: Why does this have an explicit typemap?  Elasticity
// /// doesn't.  This should use the same mechanism as Elasticity.

// %typemap(python,in) Cijkl * {
//   PyObject *basevalue = PyObject_CallMethod($source,(char*)"to_base",NULL);
  
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

// %typemap(python,freearg) Cijkl * {
//   delete $source;
// }

// %pragma(python) code="from ooflib.SWIG.engine.property.elasticity.elasticity import ElasticityPtr"

class ThermoElasticityProp : public Elasticity {
public:
  ThermoElasticityProp(PyObject *, char *, Cijkl &cijkl,
		       double t0, double dmudt);
};


%pythoncode "engine/properties/elasticity/thermo/thermo.spy"

#endif // ELASTICITY_THERMO_SWG
