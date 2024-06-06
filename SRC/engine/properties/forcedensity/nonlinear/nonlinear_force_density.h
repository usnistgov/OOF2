// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONLINEAR_FORCE_DENSITY_H
#define NONLINEAR_FORCE_DENSITY_H

#include <oofconfig.h>
#include "engine/property.h"
#include "engine/smallsystem.h"
#include <string>

class CSubProblem;
class Element;
class Equation;
class Flux;
class Material;
class FEMesh;
class Position;
class TwoVectorField;
class SymmetricTensorFlux;
class ElementNodeIterator;
class SmallMatrix;
class DoubleVec;


class NonlinearForceDensityNoDeriv : public EqnProperty {
public:
  NonlinearForceDensityNoDeriv(const std::string &name, PyObject *reg);
  virtual ~NonlinearForceDensityNoDeriv() {}
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return false; }
  virtual void precompute(FEMesh*);
  virtual void force_value(
		   const FEMesh*, const Element*, const Equation*,
		   const MasterPosition&, double time, SmallSystem*) const;
protected:
  TwoVectorField *displacement;
  SymmetricTensorFlux *stress_flux;

  virtual void nonlin_force_density(double x, double y, double z, double time,
				    DoubleVec &displacement,
				    DoubleVec &result) const = 0;
}; // NonlinearForceDensityNoDeriv


class NonlinearForceDensity : public NonlinearForceDensityNoDeriv {
public:
  NonlinearForceDensity(const std::string &name, PyObject *reg)
    : NonlinearForceDensityNoDeriv(name, reg)
  {}
  virtual ~NonlinearForceDensity() {}
  virtual void force_deriv_matrix(const FEMesh *mesh,
				  const Element  *element,
				  const Equation *eqn,
				  const ElementFuncNodeIterator &node,
				  const MasterPosition &point,	double time,
				  SmallSystem *eqndata) const;
protected:
  virtual void nonlin_force_density_deriv(double x, double y, double z,
					  double time,
					  DoubleVec &displacement,
					  SmallMatrix &result) const = 0;
};


class TestNonlinearForceDensityNoDeriv : public NonlinearForceDensityNoDeriv {
public:
  TestNonlinearForceDensityNoDeriv(const std::string &name,
				   PyObject *registration,
				   int testno)
    : NonlinearForceDensityNoDeriv(name, registration),
      testNo(testno)
  {}
  virtual ~TestNonlinearForceDensityNoDeriv() {}
protected:
  int testNo;
  virtual void nonlin_force_density(double x, double y, double z, double time,
				    DoubleVec &displacement,
				    DoubleVec &result) const;
}; // TestNonlinearForceDensityNoDeriv


class TestNonlinearForceDensity : public NonlinearForceDensity {
public:
  TestNonlinearForceDensity(const std::string &name, PyObject *registration, 
			    int testno)
    : NonlinearForceDensity(name, registration),
      testNo(testno)
  {}
  virtual ~TestNonlinearForceDensity() {}
protected:
  int testNo;
  virtual void nonlin_force_density(double x, double y, double z, double time,
				    DoubleVec &displacement,
				    DoubleVec &result) const;
  virtual void nonlin_force_density_deriv(double x, double y, double z, double time,
					  DoubleVec &displacement,
					  SmallMatrix &result) const;
}; // TestNonlinearForceDensity

#endif
