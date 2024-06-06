// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// heat conductivity property

#ifndef HEATCONDUCTIVITY_H
#define HEATCONDUCTIVITY_H


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

class HeatConductivity : public FluxProperty {
public:
  HeatConductivity(const std::string &name, PyObject *registration);
  virtual void flux_matrix(const FEMesh*, const Element*,
			   const ElementFuncNodeIterator&,
			   const Flux*,
			   const MasterPosition&,
			   double time,
			   SmallSystem *) const;
  virtual void static_flux_value(const FEMesh*, const Element*,
				 const Flux*,
				 const MasterPosition&,
				 double time,
				 SmallSystem *) const;
  virtual void cross_reference(Material*) = 0;
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const = 0;
protected:
  SymmMatrix3  conductivitytensor_;
  ScalarField *temperature;
  VectorFlux  *heat_flux;
};


class IsoHeatConductivity : public HeatConductivity {
public:
  IsoHeatConductivity(const std::string &name, PyObject *registration,
		      double kappa);
  virtual void cross_reference(Material*) {}
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const;
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
private:
  double kappa_;
};


class AnisoHeatConductivity : public HeatConductivity {
public:
  AnisoHeatConductivity(const std::string &name, PyObject *registration,
			SymmMatrix3 *kappa);
  virtual void cross_reference(Material*); // finds Orientation
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const;
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
private:
  SymmMatrix3 kappa_;
  OrientationPropBase *orientation;
};

#endif
