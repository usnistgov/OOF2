// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef FLUX_SWG
#define FLUX_SWG

%module(package="ooflib.SWIG.engine") flux

%include "common/typemaps.swg"
%import "engine/fieldindex.swg"
%import "engine/outputval.swg"
%import "engine/planarity.swg"

%{
#include "engine/flux.h"
#include "engine/outputval.h"
typedef FieldIndex NewFieldIndex;
%}

PYTHONEXPORTABLE(Flux);
MAKE_LISTVEC_TYPEMAPS(Flux);

%nodefaultctor Flux;
%rename(c_components) Flux::components;
%rename(c_divergenceComponents) Flux::divergenceComponents;
%rename(c_outOfPlaneComponents) Flux::outOfPlaneComponents;

class Flux {
public:
  int ndof();
  int divergence_dim();
  const std::string &name();
  int objectid();
  ArithmeticOutputValue newOutputValue();
  const Components* components(Planarity) const;
  const Components* divergenceComponents() const;
  const Components* outOfPlaneComponents() const;
  NewFieldIndex *getIndex(const std::string&) const;
};

ADD_REPR(Flux, repr);

%extend Flux {
  bool __eq__(Flux *other) {
    return self->objectid() == other->objectid();
  }
};

%pythonappend VectorFlux::VectorFlux %{
  finishConstruction(self)
%}
  
class VectorFlux : public Flux {
public:
  VectorFlux(char *name);
};

ADD_REPR(VectorFlux, repr);

%pythonappend SymmetricTensorFlux::SymmetricTensorFlux %{
  finishConstruction(self)
%}

class SymmetricTensorFlux : public Flux {
public:
  SymmetricTensorFlux(char *name, bool negate);
};

ADD_REPR(SymmetricTensorFlux, repr);

Flux *getFluxByIndex(int);
int countFluxes();

%pythoncode "engine/flux.spy"

#endif // FLUX_SWG
