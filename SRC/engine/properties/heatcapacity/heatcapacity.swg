// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef HEATCAPACITY_SWG
#define HEATCAPACITY_SWG

%module(package="ooflib.SWIG.engine.properties.heatcapacity") heatcapacity

%{
#include "engine/properties/heatcapacity/heatcapacity.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"

class HeatCapacityProp : public Property {
public:
  HeatCapacityProp(PyObject *self, char *, double);
};

%pythoncode "engine/properties/heatcapacity/heatcapacity.spy"

#endif // HEATCAPACITY_SWG
