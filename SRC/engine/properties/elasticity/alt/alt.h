// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef ALTELASTICITY_H
#define ALTELASTICITY_H

// AltElasticity is just like Elasticity but defines static_flux_value
// instead of flux_matrix, for testing the numerical differentiation
// done in FluxProperty::flux_matrix.  This Property is not available to the
// casual OOF2 user.

// Most of the code in AltElasticity is copied from Elasticity and
// CIsoElasticityProp.  No attempt has been made to make AltElasticity
// part of the Elasticity class hierarchy.

#include "engine/property.h"
#include "engine/properties/elasticity/cijkl.h"
#include <string>

class CSubProblem;
class Element;
class ElementNodeIterator;
class FEMesh;
class Flux;
class Material;
class OutputVal;
class Position;
class PropertyOutput;
class SymmetricTensorFlux;
class TwoVectorField;
class SmallSystem;

class CAltElasticityProp : public FluxProperty {
private:
  Cijkl c_ijkl;
  TwoVectorField *displacement;
  SymmetricTensorFlux *stress_flux;
public:
  CAltElasticityProp(const std::string &name, PyObject *registration,
		     const Cijkl &c);
  virtual ~CAltElasticityProp() {}
  virtual void static_flux_value(const FEMesh*, const Element*,
				 const Flux*,
				 const MasterPosition&,
				 double time,
				 SmallSystem *) const;
  virtual int integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return true; }
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);

  virtual void geometricStrain(const FEMesh*, const Element*,
			       const MasterPosition&, SymmMatrix3*) const;

  const Cijkl cijkl(const FEMesh*, const Element*, const MasterPosition&) const
  {
    return c_ijkl;
  }

};

#endif // ALTELASTICITY
