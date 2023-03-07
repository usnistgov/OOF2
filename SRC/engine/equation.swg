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

%include "common/typemaps.swg"
%import "engine/csubproblem.swg"
%import "engine/fieldindex.swg"
%import "engine/flux.swg"
%import "engine/nodalequation.swg"
%import "engine/planarity.swg"

%{
#include "engine/equation.h"
#include "engine/fieldindex.h"
#include "engine/flux.h"
#include "engine/node.h"
#include <vector>
typedef std::vector<Equation*> EquationVec;
typedef FieldIndex NewFieldIndex;
%}

PYTHONEXPORTABLE(Equation);
MAKE_LISTVEC_TYPEMAPS(Equation);

%nodefaultctor Equation;
%rename(c_components) Equation::components;

class Equation {
public:
  const std::string &name();
  int objectid();
  int dim();
  int ndof();			// same as dim()
  NodalEquation *nodaleqn(const FuncNode&, int);
  int is_active(const CSubProblem*);
  bool allow_boundary_conditions();
  static Equation *getEquation(const std::string&);
  ComponentsP components();
  NewFieldIndex *getIndex(const std::string&) const;
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
