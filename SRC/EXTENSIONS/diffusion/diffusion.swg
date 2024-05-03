// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module(package="ooflib.SWIG.EXTENSIONS.diffusion") diffusion

%{
#include "EXTENSIONS/diffusion/diffusion.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/symmmatrix.swg"

class IsoDiffusion : public FluxProperty {
public:
  IsoDiffusion(PyObject *reg, char *name, double kappa);
};

class AnisoDiffusion : public FluxProperty {
public:
  AnisoDiffusion(PyObject *reg, char *name, SymmMatrix3 *k);
};

class Mobility : public FluxProperty {
public:
  Mobility(PyObject *reg, char *name);
};


class AtomFluxJumpTest : public FluxProperty
{
public:
  AtomFluxJumpTest(PyObject *self, char*, double);
};

%pythoncode "diffusion.spy"
