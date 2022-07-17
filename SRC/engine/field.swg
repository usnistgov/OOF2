// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef FIELD_SWG
#define FIELD_SWG

%module(package="ooflib.SWIG.engine") field

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/csubproblem.swg"
%import "engine/femesh.swg"
%import "engine/fieldindex.swg"
%import "engine/freedom.swg"
%import "engine/outputval.swg"
%import "engine/pointdata.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/coord.h"
#include "engine/field.h"
#include "engine/outputval.h"
#include "engine/pointdata.h"
int countFields();
typedef std::vector<CompoundField*> CompoundFieldVec;
%}


// %pragma(python) code="from ooflib.SWIG.engine.fieldindex import IteratorPPtr"
// %pragma(python) code="from ooflib.SWIG.engine.fieldindex import IndexPPtr"
// %pragma(python) code="from ooflib.SWIG.engine.outputval import ArithmeticOutputValuePtr"

// This fails because of the complicated Field virtual inheritance scheme.
// TODO PYTHON3? Try again with swig4, maybe.  Do we need this?
// %typemap(out) Field* {
//   $target = $source->pythonObject();
//   if(!$target)
//      return 0;
// }

// The CompoundFieldVec* typemap converts a std::vector of
// CompoundField*s to a Python list of CompoundFields.  It does *not*
// use the PythonExportable mechanism because the Field class uses too
// much virtual inheritance for PythonExportable to work properly.
// (TODO PYTHON3: Is that still true?)  The typemap instead extracts
// Field names and calls the Python getField function (defined in
// field.spy).

%typemap(out) CompoundFieldVec * {
  // typemap(out) CompoundFieldVec*
  static PyObject *getField = 0;
  if(!getField) {
    PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.field");
    getField = PyObject_GetAttrString(module, "getField");
    Py_XDECREF(module);
    if(!getField) return 0;
  }
  CompoundFieldVec::size_type sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<CompoundField*>::size_type i=0; i<sz; i++) {
    PyObject *fldobj = PyObject_CallFunction(getField, "(s)",
					     (*$1)[i]->name().c_str());
    Py_XDECREF(arg);
    arg = Py_BuildValue("O", fldobj);
    PyList_SET_ITEM($result, (Py_ssize_t) i, arg);
  }
}

%typemap(newfree) CompoundFieldVec * {
  // typemap(newfree) CompoundFieldVec*
  delete $1;
}

////////////////////////////

%nodefaultctor Field;
%nodefaultdtor Field;

class Field {
public:
  const std::string &name();
  int objectid();
  int index();

  int ndof();

  const std::string &classname(); 

  Field *time_derivative();

  void registerProperty(Property*);

  bool is_active(CSubProblem*);
  bool is_defined(CSubProblem*);

  double value(FEMesh*, PointData *n, int component);

  void setValueFromOutputValue(FEMesh*, PointData&, OutputValue*);

  IteratorP iterator(Planarity p);
  IndexP componenttype();
  IndexP getIndex(char *);	// convert from "x", "xy", etc.
  ArithmeticOutputValue newOutputValue();
  ArithmeticOutputValue output(FEMesh*, PointData&);
};

%extend Field {
  // TODO LATER: Get rid of setvalue, if possible.  Use
  // setValueFromOutputValue instead, since it sets all components.
  // setvalue is used in _loadFieldValues in meshIO.py, and also in
  // the field initialization code in fieldinit.py. And in
  // Dirichlet.__call__ and FloatBC.fixFloatTree in bdycondition.py.
  void setvalue(FEMesh *mesh, PointData *n, int component, double x) {
    (*self)(*n, component)->value(mesh) = x;
  }
  DegreeOfFreedom *dof(PointData *n, int component) {
    return (*self)(*n, component);
  }
  // iterator_all is used in situations in which it's not known if
  // we're iterating over a Field, Flux, or Equation.
  // Equation::iterator doesn't take an argument.
  IteratorP iterator_all() {
    return self->iterator(ALL_INDICES);
  }
};

%nodefaultctor CompoundField;
%nodefaultdtor CompoundField;

class CompoundField : public Field {
public:
  bool in_plane(FEMesh*);
  Field *out_of_plane();
  Field *out_of_plane_time_derivative(); 
};

int countFields();
CompoundField *getCompoundFieldByIndex(int);
int countCompoundFields();

class ScalarField : public CompoundField, public Field {
public:
  ScalarField(char *name);
  const std::string &classname();
};


class TwoVectorField : public CompoundField, public Field {
public:
  TwoVectorField(char *name);
  const std::string &classname();
};

class ThreeVectorField : public CompoundField, public Field {
public:
  ThreeVectorField(char *name);
  const std::string &classname();
};

class VectorFieldBase : public Field {
public:
  VectorFieldBase(char *name, int d);
  const std::string &classname();
};

class SymmetricTensorField : public Field {
public:
  SymmetricTensorField(char *name);
  const std::string &classname();
};

%pythoncode "engine/field.spy"

#endif // FIELD_SWG
