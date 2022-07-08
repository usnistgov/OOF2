// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef CCONJUGATE_SWG
#define CCONJUGATE_SWG

%module cconjugate
%include "common/typemaps.swg"
%import "engine/equation.swg"
%import "engine/field.swg"
%import "engine/fieldindex.swg"

%{
#include "engine/cconjugate.h"
#include "engine/equation.h"
#include "engine/field.h"
%}

// %pragma(python) code="from ooflib.SWIG.engine.equation import EquationPtr"
// %pragma(python) code="from ooflib.SWIG.engine.field import FieldPtr"
// %pragma(python) code="from ooflib.SWIG.engine.fieldindex import FieldIndexPtr"

class CConjugatePair {
public:
  CConjugatePair(const Equation *eqn, const FieldIndex *eqncomp,
		 const Field *field, const FieldIndex *fieldcomp);
  Field *get_field();
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
