// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef THERMALEXPANSION_SWG
#define THERMALEXPANSION_SWG

%module(package="ooflib.SWIG.engine.properties.thermalexpansion") thermalexpansion

%{
#include "engine/properties/thermalexpansion/thermalexpansion.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
#endif // NOSECONDIMPORTS

 //%pragma(python) code="from ooflib.SWIG.engine.symmmatrix import SymmMatrix3Ptr"



class IsotropicThermalExpansion : public Property {
public:
  IsotropicThermalExpansion(PyObject *reg, char *name, double alpha, double t0);
};


class AnisotropicThermalExpansion : public Property {
public:
  AnisotropicThermalExpansion(PyObject *registry, char *name, SymmMatrix3 *alpha, double t0);
};

%pythoncode "engine/properties/thermalexpansion/thermalexpansion.spy"

#endif // THERMALEXPANSION_SWG
