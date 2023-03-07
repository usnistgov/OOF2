// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef PLANESTRAIN_SWG
#define PLANESTRAIN_SWG

%module(package="ooflib.SWIG.engine.properties.planestrain") planestrain

%{
#include "engine/properties/planestrain/planestrain.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"

class PlaneStrain : public Property {
public:
  PlaneStrain(PyObject *reg, char *name, double e);
};

%pythoncode "engine/properties/planestrain/planestrain.spy"

#endif // PLANESTRAIN_SWG
