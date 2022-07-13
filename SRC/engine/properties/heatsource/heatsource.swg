// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef HEATSOURCE_SWG
#define HEATSOURCE_SWG

%module heatsource

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/properties/heatsource/heatsource.h"
%}

class HeatSourceProp : public Property {
public:
  HeatSourceProp(PyObject *reg, char *name, double qdot);
};

%pythoncode "engine/properties/heatsource/heatsource.spy"

#endif	// HEATSOURCE_SWG
