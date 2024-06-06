// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONLINEAR_FORCE_DENSITY_SWG
#define NONLINEAR_FORCE_DENSITY_SWG

%module(package="ooflib.SWIG.engine.properties.forcedensity.nonlinear") nonlinear_force_density

%include "common/typemaps.swg"
%import "engine/property.swg"

%{
#include "engine/properties/forcedensity/nonlinear/nonlinear_force_density.h"
%}

%nodefaultctor NonlinearForceDensityNoDeriv;

class NonlinearForceDensityNoDeriv : public EqnProperty {
};

%nodefaultctor NonlinearForceDensity;

class NonlinearForceDensity : public NonlinearForceDensityNoDeriv {
};

class TestNonlinearForceDensityNoDeriv : public NonlinearForceDensityNoDeriv {
public:
  TestNonlinearForceDensityNoDeriv(std::string&, PyObject*, int testno);
};

class TestNonlinearForceDensity : public NonlinearForceDensity {
public:
  TestNonlinearForceDensity(std::string&, PyObject*, int testno);
};

%pythoncode "engine/properties/forcedensity/nonlinear/nonlinear_force_density.spy"

#endif // NONLINEAR_FORCE_DENSITY_SWG
