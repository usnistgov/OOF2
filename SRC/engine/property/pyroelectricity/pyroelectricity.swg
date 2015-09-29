// -*- C++ -*-
// $RCSfile: pyroelectricity.swg,v $
// $Revision: 1.6 $
// $Author: gdogan $
// $Date: 2010/04/02 22:19:51 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module piezoelectricity

%{
#include "engine/property/pyroelectricity/pyroelectricity.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"


 // Typemap to convert the enum value provided by the registered class
 // into a string, which is what the C property is expecting.  This
 // code could probably be generalized, if it turned out that there
 // were other C registered objects that needed enum parameters.

%typemap(python,in) std::string *coefficient_type (std::string s) {
  static PyObject *EnumBaseClass = 0;
  if(!EnumBaseClass) {
    PyObject *module = PyImport_ImportModule("ooflib.common.enum");
    EnumBaseClass = PyObject_GetAttrString(module, "EnumBase");
    Py_XDECREF(module);
    if(!EnumBaseClass) return 0;
  }
  if(PyObject_IsInstance($source, EnumBaseClass)) {
    PyObject *enum_name = PyObject_GetAttrString($source, "name");
    s = PyString_AsString(enum_name);
    Py_XDECREF(enum_name);
    $target = &s;
  }
  else {
    PyErr_SetString(PyExc_TypeError, "Type error in std::string *coefficient_type typemap, argument was not an enum.");
    return NULL;
  }
}


class PyroElectricity : public Property {
public:
  PyroElectricity(PyObject *reg, char *name,
		  double px, double py, double pz, double t0,
		  std::string *coefficient_type);
};


%typemap(python, in) std::string *coefficient_type {}

%pragma(python) include="pyroelectricity.spy"



