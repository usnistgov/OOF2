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

%include "common/typemaps.swg"
%import "engine/csubproblem.swg"
%import "engine/femesh.swg"
%import "engine/fieldindex.swg"
%import "engine/freedom.swg"
%import "engine/outputval.swg"
%import "engine/planarity.swg"
%import "engine/pointdata.swg"

%{
#include "common/coord.h"
#include "engine/field.h"
#include "engine/outputval.h"
#include "engine/pointdata.h"
  #include "engine/flux.h"	// SWIGBUG
  #include "engine/node.h"	// SWIGBUG
  #include "engine/property.h"	// SWIGBUG?
int countFields();
typedef std::vector<CompoundField*> CompoundFieldVec;
typedef FieldIndex NewFieldIndex;
%}

// Typemap to convert a std::vector of CompoundField*s to a Python
// list of CompoundFields.  It does *not* use the PythonExportable
// mechanism because the Field class uses too much virtual inheritance
// for PythonExportable to work properly.  The typemap instead
// extracts Field names and call the Python getField function (defined
// in field.spy).

// ** Do not use MAKE_LISTVEC_TYPEMAPS for CompoundField! **

// There is no typemap for Field*.  Field objects should never be
// returned from C++ to Python.  Use getField() instead.

// TODO PYTHON3 LATER: If Field had a swigged __eq__ method that
// compared objectid()s, would it be safe to return Fields from Python
// to C++?  The reason for not doing that was that two separately
// swigged instances of the same field don't compare equal, so we
// ensure than there is only one instance of a given Field in C++.  Is
// there some subtle reason that just providing __eq__ (and maybe also
// __hash__ and __lt__) doesn't work?

%typemap(out) std::vector<CompoundField*> * {
  // typemap(out) std::vector<CompoundField*>*
  static PyObject *getField = 0;
  if(!getField) {
    PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.field");
    getField = PyObject_GetAttrString(module, "getField");
    Py_XDECREF(module);
    if(!getField)
      SWIG_fail;
  }
  std::vector<CompoundField*>::size_type sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<CompoundField*>::size_type i=0; i<sz; i++) {
    PyObject *fldobj = PyObject_CallFunction(getField, "(s)",
					     (*$1)[i]->name().c_str());
    PyList_SET_ITEM($result, (Py_ssize_t) i, fldobj);
  }
}

%typemap(newfree) CompoundFieldVec * {
  // typemap(newfree) CompoundFieldVec*
  delete $1;
}

////////////////////////////

%nodefaultctor Field;
%nodefaultdtor Field;

%rename(c_time_derivative) Field::time_derivative;
%rename(c_components) Field::components;
%rename(c_outOfPlaneComponents) Field::outOfPlaneComponents;

class Field {
public:
  const std::string &name();
  int objectid();
  int index();

  int ndof();

  const std::string &classname();

  // The time_derivative, out_of_plane, and
  // out_of_plane_time_derivative parts of a Field cannot be returned
  // from C++ to Python in the usual way, because swig would create a
  // separate object each time, and we want all the Field objects to
  // be singletons in Python (one for Temperature, one for
  // Displacement, etc).  So there are separate Python definitions of
  // those methods in field.spy that retrieve cached singleton objects
  // from a dictionary.  To create that dictionary, the newField
  // function in problem.py calls Field.c_time_derivative, etc.
  // c_time_derivative should not be used anywhere else.
  Field *time_derivative(); // renamed to c_time_derivative

  ComponentsP components(Planarity p);
  ComponentsP outOfPlaneComponents();

  void registerProperty(Property*);

  bool is_active(CSubProblem*);
  bool is_defined(CSubProblem*);

  double value(FEMesh*, PointData *n, int component);

  void setValueFromOutputValue(FEMesh*, PointData&, OutputValue*);

  NewFieldIndex *getIndex(const std::string&) const;
  
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
};

%nodefaultctor CompoundField;
%nodefaultdtor CompoundField;

%rename(c_out_of_plane) CompoundField::out_of_plane();
%rename(c_out_of_plane_time_derivative) CompoundField::out_of_plane_time_derivative();

class CompoundField : public Field {
public:
  bool in_plane(FEMesh*);

  // See comment above re Field::time_derivative.
  Field *out_of_plane();		 // renamed to c_out_of_plane
  Field *out_of_plane_time_derivative(); // to c_out_of_plane_time_derivative
};

int countFields();
CompoundField *getCompoundFieldByIndex(int);
int countCompoundFields();

%pythonappend ScalarField::ScalarField %{
  finishCompoundFieldConstruction(self)
%}

class ScalarField : public CompoundField, public Field {
public:
  ScalarField(char *name);
  const std::string &classname();
};


%pythonappend TwoVectorField::TwoVectorField %{
  finishCompoundFieldConstruction(self)
%}

class TwoVectorField : public CompoundField, public Field {
public:
  TwoVectorField(char *name);
  const std::string &classname();
};

// ThreeVectorField and SymmetricTensorField aren't CompoundFields.

class ThreeVectorField : public Field {
public:
  ThreeVectorField(char *name);
  const std::string &classname();
};

class SymmetricTensorField : public Field {
public:
  SymmetricTensorField(char *name);
  const std::string &classname();
};

void testIterators();

%pythoncode "engine/field.spy"

#endif // FIELD_SWG
