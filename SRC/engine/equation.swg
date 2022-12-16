// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef EQUATION_SWG
#define EQUATION_SWG

%module(package="ooflib.SWIG.engine") equation

%feature("valuewrapper") IteratorP;
%feature("valuewrapper") IndexP;

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/csubproblem.swg"
%import "engine/fieldindex.swg"
%import "engine/flux.swg"
%import "engine/nodalequation.swg"
%import "engine/planarity.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/equation.h"
#include "engine/fieldindex.h"
#include "engine/flux.h"
#include <vector>
typedef std::vector<Equation*> EquationVec;
%}

PYTHONEXPORTABLE(Equation);

// %typemap(out) EquationVec * {
//   // typemap(out) EquationVec*
//   EquationVec::size_type sz = $1->size();
//   // assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
//   $result = PyList_New((Py_ssize_t) sz);
//   for(std::vector<Equation*>::size_type i=0; i<sz; i++) {
//     // pythonObject() returns a new reference and PyList_SET_ITEM steals it.
//     PyObject *eqn = (*$1)[i]->pythonObject();
//     if(!eqn)
//       SWIG_fail;
//     PyList_SET_ITEM($result, (Py_ssize_t) i, eqn);
//   }
// }

// %typemap(newfree) EquationVec * {
//   // typemap(newfree) EquationVec*
//   delete $1;
// }

%nodefaultctor Equation;

class Equation {
public:
  const std::string &name();
  int objectid();
  int dim();
  int ndof();			// same as dim()
  NodalEquation *nodaleqn(const FuncNode&, int);
  // IteratorP iterator();
  IndexP getIndex(char*);
  int is_active(const CSubProblem*);
  bool allow_boundary_conditions();
  static Equation *getEquation(const std::string&);
};

%extend Equation {
  bool __eq__(Equation *other) {
    return self->objectid() == other->objectid();
  }
};

%nodefaultctor FluxEquation;

class FluxEquation : public Equation {
public:
  const std::string &fluxname();
  Flux *flux();
};

// Natural equations don't require a flux.
class NaturalEquation : public Equation {
public:
  NaturalEquation(char *name, int dim);
};

class DivergenceEquation : public FluxEquation {
public:
  DivergenceEquation(char *name, Flux &flux, int dim);
};

class PlaneFluxEquation : public FluxEquation {
public:
  PlaneFluxEquation(char *name, Flux &flux, int dim);
};

int countEquations();
Equation *getEquationByIndex(int);

%pythoncode "engine/equation.spy"

#endif // EQUATION_SWG
