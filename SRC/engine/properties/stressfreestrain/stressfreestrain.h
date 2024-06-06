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

class StressFreeStrain : public FluxProperty {
protected:
  Elasticity *elasticity;
  SymmetricTensorFlux *stress_flux;
  SymmMatrix3 stressfreestrain_;
public:
  StressFreeStrain(const std::string &nm, PyObject *registration);
  virtual ~StressFreeStrain() {}
  virtual void cross_reference(Material*) = 0;
  virtual const SymmMatrix3 stressfreestrain(const FEMesh*, const Element*,
					     const MasterPosition&) const = 0;

  virtual void flux_offset(const FEMesh*, const Element*,
			   const Flux*, const MasterPosition&,
			   double time, SmallSystem*) const;

  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);

  virtual int integration_order(const CSubProblem*, const Element*) const;
};

class IsotropicStressFreeStrain: public StressFreeStrain {
public:
  IsotropicStressFreeStrain(const std::string &name, PyObject *registration,
			    double e);
  virtual void cross_reference(Material*);
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 stressfreestrain(const FEMesh*, const Element*,
					     const MasterPosition&) const
  {
    return stressfreestrain_;
  }
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
private:
  double e_;
};

class AnisotropicStressFreeStrain: public StressFreeStrain {
public:
  AnisotropicStressFreeStrain(const std::string &nm, PyObject *registration,
			      SymmMatrix3 *e);
  virtual void cross_reference(Material*);
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 stressfreestrain(const FEMesh*, const Element*,
					     const MasterPosition&) const;
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
private:
  SymmMatrix3 e_;
  OrientationPropBase *orientation;
};

#endif
