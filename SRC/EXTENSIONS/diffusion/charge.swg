// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef EXTENSION_CHARGE_SWG
#define EXTENSION_CHARGE_SWG

// TODO PYTHON3: Check this
%module(package="ooflib.SWIG.EXTENSIONS.diffusion") charge

%{
#include "EXTENSIONS/diffusion/charge.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
 //%include "engine/propertyhdr.swg"
%import "engine/symmmatrix.swg"
#endif // NOSECONDIMPORTS

class IsoCurrent : public Property {
public:
  IsoCurrent(PyObject *reg, char *name, double kappa);
};

class AnisoCurrent : public Property {
public:
  AnisoCurrent(PyObject *reg, char *name, SymmMatrix3 *k);
};

%pythoncode "charge.spy"

#endif // EXTENSION_CHARGE_SWG
