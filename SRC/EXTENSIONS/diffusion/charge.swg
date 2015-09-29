// -*- C++ -*-
// $RCSfile: charge.swg,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:40:10 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module charge

%{
#include "EXTENSIONS/diffusion/charge.h"
%}

%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"
%extern "engine/symmmatrix.swg"

%pragma(python) include="charge.spy"

class IsoCurrent : public Property {
public:
  IsoCurrent(PyObject *reg, char *name, double kappa);
};

class AnisoCurrent : public Property {
public:
  AnisoCurrent(PyObject *reg, char *name, SymmMatrix3 *k);
};

