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

%module field

%include "engine/typemaps.swg"
%import "engine/freedom.swg"
%import "engine/csubproblem.swg"
%import "engine/femesh.swg"
%import "engine/pointdata.swg"

%{
#include "common/coord.h"
#include "common/ooferror.h"
#include "common/pythonlock.h"
#include "engine/field.h"
#include "engine/pointdata.h"
  int countFields();
typedef double (*INITFUNC)(const Coord &position, int dof, void *clientdata);
%}
%import "engine/fieldindex.swg"
%pragma(python) code="from ooflib.SWIG.engine.fieldindex import IteratorPPtr"
%pragma(python) code="from ooflib.SWIG.engine.fieldindex import IndexPPtr"
%import "engine/outputval.swg"
%pragma(python) code="from ooflib.SWIG.engine.outputval import ArithmeticOutputValuePtr"

// This fails because of the complicated Field virtual inheritance scheme.
// TODO PYTHON3? Try again with swig4, maybe.  Do we need this?
// %typemap(out) Field* {
//   $target = $source->pythonObject();
//   if(!$target)
//      return 0;
// }

class Field {
    public:
  %readonly
  const string &name();
  int objectid();
  int index();
  %readwrite

  int ndof();

  const string &classname(); 

  Field *time_derivative();

  void registerProperty(Property*);

  bool is_active(CSubProblem*);
  bool is_defined(CSubProblem*);

  // void initialize(CSubProblem *subproblem, INITFUNC f, void *clientdata);
  double value(FEMesh*, PointData *n, int component);

  void setValueFromOutputValue(FEMesh*, PointData&, OutputValue*);

  %addmethods {
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
  }
  IteratorP iterator(Planarity p);
  %addmethods {
    // iterator_all is used in situations in which it's not known if
    // we're iterating over a Field, Flux, or Equation.
    // Equation::iterator doesn't take an argument.
    IteratorP iterator_all() {
      return self->iterator(ALL_INDICES);
    }
  }
  IndexP componenttype();
  IndexP getIndex(char *);	// convert from "x", "xy", etc.
  ArithmeticOutputValue newOutputValue();
  ArithmeticOutputValue output(FEMesh*, PointData&);
};


class CompoundField : public Field {
public:
  //   Field *time_derivative();
#ifndef DIM_3
  bool in_plane(FEMesh*);
  Field *out_of_plane();
  Field *out_of_plane_time_derivative(); 
#endif
};

int countFields();
CompoundField *getCompoundFieldByIndex(int);
int countCompoundFields();

class ScalarField : public CompoundField, public Field {
public:
  ScalarField(char *name);
  const string &classname();
};

class TwoVectorField : public CompoundField, public Field {
public:
  TwoVectorField(char *name);
  const string &classname();
};

class ThreeVectorField : public CompoundField, public Field {
public:
  ThreeVectorField(char *name);
  const string &classname();
};

class VectorFieldBase : public Field {
public:
  VectorFieldBase(char *name, int d);
  const string &classname();
};

class SymmetricTensorField : public Field {
public:
  SymmetricTensorField(char *name);
  const string &classname();
}

%pythoncode "engine/field.spy"

#endif // FIELD_SWG
