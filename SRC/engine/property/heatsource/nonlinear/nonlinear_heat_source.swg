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

%module heatsource

%{
#include "engine/property/heatsource/nonlinear/nonlinear_heat_source.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%import "engine/symmmatrix.swg"

class NonlinearHeatSourceNoDeriv : public Property {
};

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

%pythoncode "engine/property/heatsource/nonlinear/nonlinear_heat_source.spy"

#endif // NONLINEAR_HEAT_SOURCE_SWG
