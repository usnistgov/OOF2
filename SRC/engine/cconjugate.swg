// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CCONJUGATE_SWG
#define CCONJUGATE_SWG

%module(package="ooflib.SWIG.engine") cconjugate

%include "common/typemaps.swg"
%import "engine/equation.swg"
%import "engine/field.swg"
%import "engine/fieldindex.swg"

%{
#include <oofconfig.h>  
#include "engine/cconjugate.h"
#include "engine/equation.h"
#include "engine/field.h"
#include "engine/fieldindex.h"
  #include "engine/outputval.h"	// SWIGBUG
  #include "engine/flux.h"	// SWIGBUG
  #include "engine/node.h"	// SWIGBUG
%}

MAKE_LISTVEC_TYPEMAPS(CConjugatePair);

class CConjugatePair {
public:
  CConjugatePair(const Equation *eqn, const FieldIndex *eqncomp,
		 const Field *field, const FieldIndex *fieldcomp);
  const std::string &get_field_name();
  FieldIndex *get_field_component();
  Equation *get_equation();
  FieldIndex *get_equation_component();
};

%extend CConjugatePair {
  bool __eq__(CConjugatePair *other) {
    return *self == *other;
  }
};

#endif // CCONJUGATE_SWG
