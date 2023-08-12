// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef GENERAL_NONLINEAR_ELASTICITY_SWG
#define GENERAL_NONLINEAR_ELASTICITY_SWG

%module(package="ooflib.SWIG.engine.properties.elasticity.nonlinear") general_nonlinear_elasticity

%{
#include "engine/properties/elasticity/nonlinear/general_nonlinear_elasticity.h"
%}

%include "common/typemaps.swg"
%import "engine/property.swg"

%nodefaultctor GeneralNonlinearElasticityNoDeriv;

class GeneralNonlinearElasticityNoDeriv : public Property {
};

%nodefaultctor GeneralNonlinearElasticity;

class GeneralNonlinearElasticity : public GeneralNonlinearElasticityNoDeriv {
};

class TestGeneralNonlinearElasticityNoDeriv
  : public GeneralNonlinearElasticityNoDeriv
{
public:
  TestGeneralNonlinearElasticityNoDeriv(PyObject *reg, char *name, int testno);
};

class TestGeneralNonlinearElasticity : public GeneralNonlinearElasticity {
public:
  TestGeneralNonlinearElasticity(PyObject *reg, char *name, int testno);
};

%pythoncode "engine/properties/elasticity/nonlinear/general_nonlinear_elasticity.spy"

#endif // GENERAL_NONLINEAR_ELASTICITY_SWG
