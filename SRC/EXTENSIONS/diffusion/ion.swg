// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module(package="ooflib.SWIG.EXTENSIONS.diffusion") ion

%{
#include "EXTENSIONS/diffusion/ion.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"
#endif // NOSECONDIMPORTS
   
class IonDiffusion : public Property {
public:
  IonDiffusion(PyObject *reg, char *name, double z);
};

%pythoncode "ion.spy"

