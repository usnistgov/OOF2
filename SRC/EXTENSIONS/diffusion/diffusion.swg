// -*- C++ -*-
// $RCSfile: diffusion.swg,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2014/09/27 21:40:11 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module diffusion

%{
#include "EXTENSIONS/diffusion/diffusion.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%extern "engine/symmmatrix.swg"

%pragma(python) include="diffusion.spy"

class IsoDiffusion : public Property {
public:
  IsoDiffusion(PyObject *reg, char *name, double kappa);
};

class AnisoDiffusion : public Property {
public:
  AnisoDiffusion(PyObject *reg, char *name, SymmMatrix3 *k);
};

class Mobility : public Property {
public:
  Mobility(PyObject *reg, char *name);
};


class AtomFluxJumpTest : public Property
{
public:
  AtomFluxJumpTest(PyObject *self, char*, double);
};
