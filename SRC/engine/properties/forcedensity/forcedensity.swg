// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef FORCEDENSITY_SWG
#define FORCEDENSITY_SWG

%module(package="ooflib.SWIG.engine.properties.forcedensity") forcedensity

%include "common/typemaps.swg"
%import "engine/property.swg"

%{
#include "engine/properties/forcedensity/forcedensity.h"
%}

class ForceDensity : public Property {
public:
  ForceDensity(PyObject *self, char *, double, double);
  double fdensity_x();
  double fdensity_y();
};

%pythoncode "engine/properties/forcedensity/forcedensity.spy"

#endif // FORCEDENSITY_SWG
