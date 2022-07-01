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

// TODO PYTHON3: Can two swig files contribute to the same module?
// The module line in heatsource.swg is the same as this one.  Or does
// that module have a different path?
%module heatsource

%{
#include "engine/property/heatsource/nonconstant/nonconstant_heat_source.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%import "engine/symmmatrix.swg"

class NonconstantHeatSource : public Property {
};


class TestNonconstantHeatSource : public NonconstantHeatSource {
public:
  TestNonconstantHeatSource(PyObject *reg, char *name, int testno);
};

%pythoncode "nonconstant_heat_source.spy"

#endif // NONCONSTANT_HEAT_SOURCE_SWG
