// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONCONSTANT_HEAT_SOURCE_SWG
#define NONCONSTANT_HEAT_SOURCE_SWG

%module(package="ooflib.SWIG.engine.properties.heatsource.nonconstant") nonconstant_heat_source

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"

%{
#include "engine/properties/heatsource/nonconstant/nonconstant_heat_source.h"
%}

%nodefaultctor NonconstantHeatSource;

class NonconstantHeatSource : public EqnProperty {
};


class TestNonconstantHeatSource : public NonconstantHeatSource {
public:
  TestNonconstantHeatSource(PyObject *reg, char *name, int testno);
};

%pythoncode "engine/properties/heatsource/nonconstant/nonconstant_heat_source.spy"

#endif // NONCONSTANT_HEAT_SOURCE_SWG
