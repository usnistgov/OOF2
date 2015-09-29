// -*- C++ -*-
// $RCSfile: ion.h,v $
// $Revision: 1.3 $
// $Author: reida $
// $Date: 2012/03/28 18:43:33 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// atom conductivity property

#ifndef ION_H
#define ION_H


#include "common/coord.h"
#include "engine/property.h"
#include "engine/symmmatrix.h"
#include "EXTENSIONS/diffusion/diffusion.h"
#include <string>

class Element;
class Material;
class FEMesh;
class OrientationPropBase;
class SmallSystem;
class ScalarField;
class VectorFlux;
class ElementNodeIterator;


// This property is the coupling between diffusion and current for an
// ion in an electrolyte.  It needs a diffusion coefficient, which it
// gets from the Diffusion property in the material.  Its actual
// arguments are the charge.  In principle, this property also
// dependson the temperature.  For now, we fold all the stuff into the
// "z" parameter, but this isn't really right.

class IonDiffusion : public FluxProperty {
public:
  IonDiffusion(PyObject *registry, const std::string &name, double z);
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
  virtual void cross_reference(Material*);
  virtual int  integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return true; }
  virtual void precompute(FEMesh*) {}

private:
  Diffusion *diffusion; // Property from which we get the conductivity.
  ScalarField *voltage,*concentration;
  VectorFlux  *charge_flux,*atom_flux;
  double z_;
};

#endif
