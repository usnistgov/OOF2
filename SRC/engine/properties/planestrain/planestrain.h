// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef STRESSFREESTRAIN_H
#define STRESSFREESTRAIN_H

#include <oofconfig.h>

#include "engine/property.h"
#include "engine/symmmatrix.h"
#include <string>

class Elasticity;
class Element;
class Flux;
class Material;
class OrientationPropBase;
class SmallSystem;
class SymmetricTensorFlux;

class PlaneStrain : public FluxProperty {
protected:
  Elasticity *elasticity;
  SymmetricTensorFlux *stress_flux;
public:
  PlaneStrain(PyObject *registry,
	      const std::string &nm, double ezz);
  virtual ~PlaneStrain() {}
  virtual void cross_reference(Material*);
  virtual void flux_offset(const FEMesh*, const Element*,
			   const Flux*, const MasterPosition&,
			   double time, SmallSystem*) const;

  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);

  virtual int integration_order(const CSubProblem*, const Element*) const;
private:
  double ezz_;
};

#endif
