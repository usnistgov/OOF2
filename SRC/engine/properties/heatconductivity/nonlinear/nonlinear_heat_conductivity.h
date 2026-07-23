// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONLINEAR_HEAT_CONDUCTIVITY_H
#define NONLINEAR_HEAT_CONDUCTIVITY_H


#include "common/coord.h"
#include "engine/property.h"
#include "engine/symmmatrix.h"
#include <string>

class DoubleVec;
class Element;
class Material;
class FEMesh;
class OrientationPropBase;
class SmallSystem;
class ScalarField;
class VectorFlux;
class ElementNodeIterator;


class NonlinearHeatConductivity : public FluxProperty {
public:
  NonlinearHeatConductivity(const std::string &name, PyObject *registration);
  virtual ~NonlinearHeatConductivity() {}
  virtual void flux_matrix(const FEMesh*, const Element*,
			   const ElementFuncNodeIterator&,
			   const Flux*,
			   const MasterPosition&,
			   double time, void*,
			   SmallSystem*) const;
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return false; }
  // virtual bool is_symmetric_K(const CSubProblem*) const { return false; }
  virtual void flux_value(const FEMesh*, const Element*, const Flux*,
			  const MasterPosition&, double time, void*,
			  SmallSystem*) const;

protected:
  ScalarField *temperature;
  VectorFlux  *heat_flux;

  virtual DoubleVec nonlin_heat_flux_deriv_wrt_temperature(
				   const Coord &pt, double time,
				   double temperature,
				   const DoubleVec &temperature_gradient)
    const = 0;

  virtual SmallMatrix nonlin_heat_flux_deriv_wrt_temperature_gradient(
				      const Coord &pt, double time,
				      double temperature,
				      const DoubleVec &temperature_gradient)
    const = 0;
  virtual DoubleVec nonlin_heat_flux(const Coord &pt, double time,
				     double temperature,
				     const DoubleVec &temperature_gradient)
    const = 0;
}; 

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


class TestNonlinearHeatConductivity : public NonlinearHeatConductivity {

public:
  TestNonlinearHeatConductivity(const std::string &name, PyObject *registration,
				int testno)
    : NonlinearHeatConductivity(name, registration),
      testNo(testno)
  {}
  virtual ~TestNonlinearHeatConductivity() {}

protected:
  int testNo;
  virtual DoubleVec nonlin_heat_flux(const Coord &pt,
				double time, double temperature,
				const DoubleVec &temperature_gradient) const;
  virtual DoubleVec nonlin_heat_flux_deriv_wrt_temperature(
                                const Coord &pt,
				double time, double temperature,
				const DoubleVec &temperature_gradient) const;
  virtual SmallMatrix nonlin_heat_flux_deriv_wrt_temperature_gradient(
                                const Coord &pt,
				double time, double temperature,
				const DoubleVec &temperature_gradient) const;
};

#endif
