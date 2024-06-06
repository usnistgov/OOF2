// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONLINEAR_HEAT_SOURCE_SWG
#define NONLINEAR_HEAT_SOURCE_SWG

%module(package="ooflib.SWIG.engine.properties.heatsource.nonlinear") nonlinear_heat_source

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"

%{
#include "engine/properties/heatsource/nonlinear/nonlinear_heat_source.h"
%}

%nodefaultctor NonlinearHeatSourceNoDeriv;

class NonlinearHeatSourceNoDeriv : public EqnProperty {
};

%nodefaultctor NonlinearHeatSource;

class NonlinearHeatSource : public NonlinearHeatSourceNoDeriv {
};

class TestNonlinearHeatSourceNoDeriv : public NonlinearHeatSourceNoDeriv {
public:
  TestNonlinearHeatSourceNoDeriv(std::string &name, PyObject *reg, int testno);
};

class TestNonlinearHeatSource : public NonlinearHeatSource {
public:
  TestNonlinearHeatSource(std::string &name, PyObject *reg, int testno);
};

%pythoncode "engine/properties/heatsource/nonlinear/nonlinear_heat_source.spy"

#endif // NONLINEAR_HEAT_SOURCE_SWG
