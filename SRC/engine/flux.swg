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
#endif // NOSECONDIMPORTS

%{
#include "engine/flux.h"
#include "engine/outputval.h"
#include <vector>
typedef std::vector<Flux*> FluxVec;
%}

// %pragma(python) code="from ooflib.SWIG.engine.fieldindex import IteratorPPtr"
// %pragma(python) code="from ooflib.SWIG.engine.fieldindex import IndexPPtr"
// %pragma(python) code="from ooflib.SWIG.engine.outputval import ArithmeticOutputValuePtr"

%typemap(out) Flux* {
  // typemap(out) Flux*
  $result = $1->pythonObject();
  if(!$result)
    SWIG_fail;
}

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
  const string &name();
  int objectid();

  IteratorP iterator(Planarity p);
  IteratorP divergence_iterator();
  IndexP componenttype();
  ArithmeticOutputValue newOutputValue();
};

%extend Flux {
  // iterator_all is used in situations in which it's not known if
  // we're iterating over a Field, Flux, or Equation.
  // Equation::iterator doesn't take an argument.
  IteratorP iterator_all() {
    return self->iterator(ALL_INDICES);
  }
};
  
class VectorFlux : public Flux {
public:
  VectorFlux(char *name);
};

class SymmetricTensorFlux : public Flux {
public:
  SymmetricTensorFlux(char *name, bool negate);
};

Flux *getFluxByIndex(int);
int countFluxes();

%pythoncode "engine/flux.spy"

#endif // FLUX_SWG
