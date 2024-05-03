// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONLINEAR_HEAT_CONDUCTIVITY_SWG
#define NONLINEAR_HEAT_CONDUCTIVITY_SWG

%module(package="ooflib.SWIG.engine.properties.heatconductivity.nonlinear") nonlinear_heat_conductivity

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"

%{
#include "engine/properties/heatconductivity/nonlinear/nonlinear_heat_conductivity.h"
%}

%nodefaultctor NonlinearHeatConductivityNoDeriv;

class NonlinearHeatConductivityNoDeriv : public FluxProperty {
};

%nodefaultctor NonlinearHeatConductivity;

class NonlinearHeatConductivity : public NonlinearHeatConductivityNoDeriv {
};

class TestNonlinearHeatConductivityNoDeriv : public NonlinearHeatConductivityNoDeriv {
public:
  TestNonlinearHeatConductivityNoDeriv(PyObject *reg, char *name, int testno);
};

class TestNonlinearHeatConductivity : public NonlinearHeatConductivity {
public:
  TestNonlinearHeatConductivity(PyObject *reg, char *name, int testno);
};

%pythoncode "engine/properties/heatconductivity/nonlinear/nonlinear_heat_conductivity.spy"

#endif // NONLINEAR_HEAT_CONDUCTIVITY_SWG
