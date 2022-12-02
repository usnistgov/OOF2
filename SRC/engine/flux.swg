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

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/fieldindex.swg"
%import "engine/outputval.swg"
%import "engine/planarity.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/flux.h"
#include "engine/outputval.h"
typedef std::vector<Flux*> FluxVec;
%}

PYTHONEXPORTABLE(Flux);

%typemap(out) FluxVec * {
  // typemap(out) FluxVec*
  FluxVec::size_type sz = $1->size();
  // assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $result = PyList_New((Py_ssize_t) sz);
  for(FluxVec::size_type i=0; i<sz; i++) {
    PyObject *flux = (*$1)[i]->pythonObject();
    if(!flux)
      SWIG_fail;
    PyList_SET_ITEM($result, (Py_ssize_t) i, flux);
  }
}

%typemap(newfree) FluxVec * {
  // typemap(newfree) FluxVec*
  delete $1;
}

%nodefaultctor Flux;

class Flux {
public:
  int ndof();
  int divergence_dim();
  const std::string &name();
  int objectid();

  IteratorP iterator(Planarity p);
  IteratorP divergence_iterator();
  ArithmeticOutputValue newOutputValue();
};

ADD_REPR(Flux, repr);

%extend Flux {
  // iterator_all is used in situations in which it's not known if
  // we're iterating over a Field, Flux, or Equation.
  // Equation::iterator doesn't take an argument.
  IteratorP iterator_all() {
    return self->iterator(ALL_INDICES);
  }
  bool __eq__(Flux *other) {
    return self->objectid() == other->objectid();
  }
};
  
class VectorFlux : public Flux {
public:
  VectorFlux(char *name);
};

ADD_REPR(VectorFlux, repr);

class SymmetricTensorFlux : public Flux {
public:
  SymmetricTensorFlux(char *name, bool negate);
};

ADD_REPR(SymmetricTensorFlux, repr);

Flux *getFluxByIndex(int);
int countFluxes();

%pythoncode "engine/flux.spy"

#endif // FLUX_SWG
