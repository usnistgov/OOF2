// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONCONSTANT_FORCE_DENSITY_SWG
#define NONCONSTANT_FORCE_DENSITY_SWG

%module(package="ooflib.SWIG.engine.properties.forcedensity.nonconstant") nonconstant_force_density

%include "common/typemaps.swg"
%import "engine/property.swg"

%{
#include "engine/properties/forcedensity/nonconstant/nonconstant_force_density.h"
%}

%nodefaultctor NonconstantForceDensity;

class NonconstantForceDensity : public Property {
};

class TestNonconstantForceDensity : public Property {
public:
  TestNonconstantForceDensity(PyObject *reg, char *name, int testno);
};

%pythoncode "engine/properties/forcedensity/nonconstant/nonconstant_force_density.spy"

#endif // NONCONSTANT_FORCE_DENSITY_SWG
