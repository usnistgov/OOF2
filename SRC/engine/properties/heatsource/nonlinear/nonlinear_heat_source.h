// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef NONLINEAR_HEAT_SOURCE_H
#define NONLINEAR_HEAT_SOURCE_H


#include "common/coord.h"
#include "engine/property.h"
#include "engine/symmmatrix.h"
#include <string>

class Element;
class Material;
class FEMesh;
class OrientationPropBase;
class SmallSystem;
class ScalarField;
class VectorFlux;
class ElementNodeIterator;

class NonlinearHeatSource : public EqnProperty {
public:
  NonlinearHeatSource(const std::string &name, PyObject *registration);
  virtual ~NonlinearHeatSource() {}
  virtual void force_deriv_matrix(const FEMesh *mesh,
				  const Element *el,
				  const ElementFuncNodeIterator &j,
 				  const Equation *eqn,
				  const MasterPosition &pt,
				  double time, void*,
				  SmallSystem *eqndata ) const;
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return false; }
  virtual void force_value(const FEMesh*, const Element*,
			   const Equation*,
			   const MasterPosition&,
			   double time, void*,
			   SmallSystem *) const;
protected:
  ScalarField *temperature;
  VectorFlux  *heat_flux;

  virtual double nonlin_heat_source(
		    const Coord&, double time, double temperature) const = 0;
  virtual double nonlin_heat_source_deriv_wrt_temperature(
			  const Coord &pt, double time, double temperature)
    const = 0;
};


class TestNonlinearHeatSource : public NonlinearHeatSource {
public:
  TestNonlinearHeatSource(const std::string &name, PyObject *registration,
			  int testno)
    : NonlinearHeatSource(name, registration),
      testNo(testno)
  {}
  virtual ~TestNonlinearHeatSource() {}
protected:
  int testNo;
  virtual double nonlin_heat_source(
		    const Coord &pt, double time, double temperature) const;
  virtual double nonlin_heat_source_deriv_wrt_temperature(
		  const Coord &pt, double time, double temperature) const;

};

#endif
