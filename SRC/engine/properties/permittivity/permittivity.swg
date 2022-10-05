// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef PERMITTIVITY_SWG
#define PERMITTIVITY_SWG

%module(package="ooflib.SWIG.engine.properties.permittivity") permittivity

%{
#include "engine/properties/permittivity/permittivity.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
#endif // NOSECONDIMPORTS

class IsoDielectricPermittivity : public Property {
public:
  IsoDielectricPermittivity(PyObject *reg, char *name, double epsilon);
};

class AnisoDielectricPermittivity : public Property {
public:
  AnisoDielectricPermittivity(PyObject *reg, char *name, SymmMatrix3 *k);
};

class ChargeDensity : public Property {
public:
  ChargeDensity(PyObject *reg, char *name, double qdot);
  double rho();
};

%pythoncode "engine/properties/permittivity/permittivity.spy"

#endif // PERMITTIVITY_SWG
