// -*- C++ -*-
/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef RAMBERGOSGOOD_SWG
#define RAMBERGOSGOOD_SWG

%module(package="ooflib.SWIG.EXTENSIONS.ramberg_osgood") ramberg_osgood

%include "common/typemaps.swg"
%import "engine/properties/elasticity/nonlinear/general_nonlinear_elasticity.swg"
%import "engine/properties/elasticity/cijkl.swg"

%{
#include "EXTENSIONS/ramberg_osgood/ramberg_osgood.h"
#include "engine/properties/elasticity/cijkl.h"
#include "engine/properties/elasticity/elasticity.h"
%}

class CRambergOsgood : public GeneralNonlinearElasticity {
public:
  CRambergOsgood(PyObject *reg, PyObject *self, const std::string &name,
		 Cijkl &cijkl, double alpha, double s0, double n);
  ~CRambergOsgood();
};

%pythoncode "ramberg_osgood.spy"

#endif // RAMBERGOSGOOD_SWG
