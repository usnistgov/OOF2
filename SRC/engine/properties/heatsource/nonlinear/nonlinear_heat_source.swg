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

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/properties/heatsource/nonlinear/nonlinear_heat_source.h"
%}

%nodefaultctor NonlinearHeatSourceNoDeriv;

class NonlinearHeatSourceNoDeriv : public Property {
};

%nodefaultctor NonlinearHeatSource;

class NonlinearHeatSource : public NonlinearHeatSourceNoDeriv {
};

class TestNonlinearHeatSourceNoDeriv : public NonlinearHeatSourceNoDeriv {
public:
  TestNonlinearHeatSourceNoDeriv(PyObject *reg, char *name, int testno);
};

class TestNonlinearHeatSource : public NonlinearHeatSource {
public:
  TestNonlinearHeatSource(PyObject *reg, char *name, int testno);
};

%pythoncode "engine/properties/heatsource/nonlinear/nonlinear_heat_source.spy"

#endif // NONLINEAR_HEAT_SOURCE_SWG
