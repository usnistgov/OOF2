// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef HEATCONDUCTIVITY_SWG
#define HEATCONDUCTIVITY_SWG

%module(package="ooflib.SWIG.engine.properties.heatconductivity") heatconductivity

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/properties/heatconductivity/heatconductivity.h"
%}

class IsoHeatConductivity : public Property {
public:
  IsoHeatConductivity(PyObject *reg, char *name, double kappa);
};

class AnisoHeatConductivity : public Property {
public:
  AnisoHeatConductivity(PyObject *reg, char *name, SymmMatrix3 *k);
};

%pythoncode "engine/properties/heatconductivity/heatconductivity.spy"

#endif // HEATCONDUCTIVITY_SWG
