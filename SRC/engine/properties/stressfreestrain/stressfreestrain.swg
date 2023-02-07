// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef STRESSFREESTRAIN_SWG
#define STRESSFREESTRAIN_SWG

%module(package="ooflib.SWIG.engine.properties.stressfreestrain") stressfreestrain

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"

%{
#include "engine/properties/stressfreestrain/stressfreestrain.h"
%}

class IsotropicStressFreeStrain : public Property {
public:
  IsotropicStressFreeStrain(PyObject *reg, char *name, double e);
};

class AnisotropicStressFreeStrain : public Property {
public:
  AnisotropicStressFreeStrain(PyObject *reg, char *name, SymmMatrix3 *e);
};

%pythoncode "engine/properties/stressfreestrain/stressfreestrain.spy"

#endif // STRESSFREESTRAIN_SWG
