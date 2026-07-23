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
class Coord;
class DoubleVec;
class Element;
class FEMesh;
class Flux;
class MasterPosition;
class SmallMatrix;
class SmallSystem;
class SmallTensor3;
class SmallTensor4;
class SymmetricTensorFlux;
class TwoVectorField;

class GeneralNonlinearElasticity : public FluxProperty {
public:
  GeneralNonlinearElasticity(const std::string &name, PyObject *registration);
  virtual ~GeneralNonlinearElasticity() {}
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return false; }
  virtual void flux_value(const FEMesh*, const Element*, const Flux*,
			  const MasterPosition&, double time,  void*,
			  SmallSystem*) const;
  virtual void flux_matrix(const FEMesh *mesh,
			   const Element *element,
			   const ElementFuncNodeIterator &nu,
			   const Flux *flux,
			   const MasterPosition &x,
			   double time, void*, 
			   SmallSystem *fluxmtx) const;
protected:
  TwoVectorField *displacement;
  SymmetricTensorFlux *stress_flux;

  virtual SmallMatrix nonlin_stress(const Coord &pt, double time,
				    const DoubleVec &displacement,
				    const SmallMatrix &dispGrad) const = 0;
  virtual SmallTensor3 nonlin_stress_deriv_wrt_displacement(
			    const Coord &pt, double time,
			    const DoubleVec &displacement,
			    const SmallMatrix &dispGrad) const = 0;
  virtual SmallTensor4 nonlin_stress_deriv_wrt_displacement_gradient(
			     const Coord &pt, double time,
			     const DoubleVec &displacement,
			     const SmallMatrix &dispGrad) const = 0;

}; // GeneralNonlinearElasticity

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

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
  virtual SmallMatrix nonlin_stress(const Coord &pt, double time,
			     const DoubleVec &displacement,
			     const SmallMatrix &dispGrad) const;
  virtual SmallTensor3 nonlin_stress_deriv_wrt_displacement(
                             const Coord &pt, double time,
			     const DoubleVec &displacement,
			     const SmallMatrix &dispGrad) const;
  virtual SmallTensor4 nonlin_stress_deriv_wrt_displacement_gradient(
                             const Coord &pt, double time,
			     const DoubleVec &displacement,
			     const SmallMatrix &dispGrad) const;

}; // TestGeneralNonlinearElasticity

#endif
