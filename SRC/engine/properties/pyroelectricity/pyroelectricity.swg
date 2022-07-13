// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef PYROELECTRICITY_SWG
#define PYROELECTRICITY_SWG

%module pyroelectricity

%{
#include "engine/properties/pyroelectricity/pyroelectricity.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%include "engine/property.swg"
#endif // NOSECONDIMPORTS

 // Typemap to convert the enum value provided by the registered class
 // into a string, which is what the C property is expecting.  This
 // code could probably be generalized, if it turned out that there
 // were other C registered objects that needed enum parameters.

%typemap(in) std::string *coefficient_type (std::string s) {
  // static PyObject *EnumBaseClass = 0;
  // if(!EnumBaseClass) {
  //   PyObject *module = PyImport_ImportModule("ooflib.common.enum");
  //   EnumBaseClass = PyObject_GetAttrString(module, "EnumBase");
  //   Py_XDECREF(module);
  //   if(!EnumBaseClass)
  //     SWIG_fail;
  // }
  FETCH_CLASS(ooflib.common.enum, EnumBase);
  if(PyObject_IsInstance($input, EnumBaseClass)) {
    // TODO PYTHON3: I'm not at all sure that this is correct.
    PyObject *enum_name = PyObject_GetAttrString($input, "name");
    PyObject *ustr = PyUnicode_AsEncodedString(enum_name, "UTF-8", "replace");
    s.assign(PyBytes_AsString(ustr));
    $1 = &s;
  }
  else {
    PyErr_SetString(
	    PyExc_TypeError,
	    "Type error in std::string *coefficient_type typemap,"
	    " argument was not an enum.");
    SWIG_fail;
  }
}


class PyroElectricity : public Property {
public:
  PyroElectricity(PyObject *reg, char *name,
		  double px, double py, double pz, double t0,
		  std::string *coefficient_type);
};


%typemap(python, in) std::string *coefficient_type {}

%pythoncode "engine/properties/pyroelectricity/pyroelectricity.spy"

#endif // PYROELECTRICITY_SWG
