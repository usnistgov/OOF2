// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef GENERAL_NONLINEAR_ELASTICITY_H
#define GENERAL_NONLINEAR_ELASTICITY_H

#include <oofconfig.h>
#include "engine/property.h"
#include <string>

class CSubProblem;
class DoubleVec;
class Element;
class ElementNodeIterator;
class FEMesh;
class Flux;
class Material;
class OutputVal;
class Position;
class PropertyOutput;
class SmallMatrix;
class SmallTensor3;
class SmallTensor4;
class SmallSystem;
class SymmetricTensorFlux;
class TwoVectorField;



class GeneralNonlinearElasticityNoDeriv : public FluxProperty {
public:
  GeneralNonlinearElasticityNoDeriv(const std::string &name,
				    PyObject *registration);
  virtual ~GeneralNonlinearElasticityNoDeriv() {}
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return false; }
  virtual void static_flux_value(const FEMesh*, const Element*,
				 const Flux*,
				 const MasterPosition&,
				 double time,
				 SmallSystem *) const;
protected:
  TwoVectorField *displacement;
  SymmetricTensorFlux *stress_flux;

  virtual void nonlin_stress(double x, double y, double z,
			     double time, DoubleVec &displacement,
			     SmallMatrix &dispGrad,
			     SmallMatrix &stress) const = 0;

}; // GeneralNonlinearElasticityNoDeriv


class GeneralNonlinearElasticity : public GeneralNonlinearElasticityNoDeriv {
public:
  GeneralNonlinearElasticity(const std::string &name, PyObject *registration)
    : GeneralNonlinearElasticityNoDeriv(name, registration)
  {};
  virtual ~GeneralNonlinearElasticity() {}
  virtual void flux_matrix(const FEMesh *mesh,
			   const Element *element,
			   const ElementFuncNodeIterator &nu,
			   const Flux *flux,
			   const MasterPosition &x,
			   double time,
			   SmallSystem *fluxmtx) const;
protected:
  virtual void nonlin_stress_deriv_wrt_displacement(
                             double x, double y, double z,
			     double time, DoubleVec &displacement,
			     SmallMatrix &dispGrad,
			     SmallTensor3 &stress_deriv) const = 0;

  virtual void nonlin_stress_deriv_wrt_displacement_gradient(
                             double x, double y, double z,
			     double time, DoubleVec &displacement,
			     SmallMatrix &dispGrad,
			     SmallTensor4 &stress_deriv) const = 0;

}; // GeneralNonlinearElasticity

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


class TestGeneralNonlinearElasticityNoDeriv : public GeneralNonlinearElasticityNoDeriv {

public:
  TestGeneralNonlinearElasticityNoDeriv(const std::string &name,
					PyObject *registration,
					int testno)
    : GeneralNonlinearElasticityNoDeriv(name, registration),
      testNo(testno)
  {};
  virtual ~TestGeneralNonlinearElasticityNoDeriv() {}

protected:
  int testNo;
  virtual void nonlin_stress(double x, double y, double z, double time,
			     DoubleVec &displacement,
			     SmallMatrix &dispGrad,
			     SmallMatrix &stress) const;
}; // TestGeneralNonlinearElasticityNoDeriv


class TestGeneralNonlinearElasticity : public GeneralNonlinearElasticity{

public:
  TestGeneralNonlinearElasticity(const std::string &name,
				 PyObject *registration,
				 int testno)
    : GeneralNonlinearElasticity(name, registration),
      testNo(testno)
  {};
  virtual ~TestGeneralNonlinearElasticity() {};

protected:
  int testNo;
  virtual void nonlin_stress(double x, double y, double z, double time,
			     DoubleVec &displacement,
			     SmallMatrix &dispGrad,
			     SmallMatrix &stress) const;
  virtual void nonlin_stress_deriv_wrt_displacement(
                             double x, double y, double z, double time,
			     DoubleVec &displacement,
			     SmallMatrix &dispGrad,
			     SmallTensor3 &stress_deriv) const;
  virtual void nonlin_stress_deriv_wrt_displacement_gradient(
                             double x, double y, double z, double time,
			     DoubleVec &displacement,
			     SmallMatrix &dispGrad,
			     SmallTensor4 &stress_deriv) const;

}; // TestGeneralNonlinearElasticity

#endif
