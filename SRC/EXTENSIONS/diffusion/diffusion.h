// -*- C++ -*-
// $RCSfile: diffusion.h,v $
// $Revision: 1.11 $
// $Author: reida $
// $Date: 2011/09/13 21:26:53 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// atom conductivity property

#ifndef DIFFUSION_H
#define DIFFUSION_H


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

class Diffusion : public FluxProperty {
public:
  Diffusion(PyObject *registry, const std::string &name);
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
  virtual bool constant_in_space() const { return true; }
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const = 0;
protected:
  SymmMatrix3  conductivitytensor_;
  ScalarField *concentration;
  VectorFlux  *atom_flux;
};


class IsoDiffusion : public Diffusion {
public:
  IsoDiffusion(PyObject *registry,
		      const std::string &name, double D);
  virtual void cross_reference(Material*) {}
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const;
private:
  double D_;
};


class AnisoDiffusion : public Diffusion {
public:
  AnisoDiffusion(PyObject *registry, const std::string &name, SymmMatrix3 *D);
  virtual void cross_reference(Material*); // finds Orientation
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const;
private:
  SymmMatrix3 D_;
  OrientationPropBase *orientation;
};


class Mobility : public EqnProperty {
public:
  Mobility(PyObject *registry, const std::string &name);
  virtual void first_time_deriv_matrix(const FEMesh*, const Element*,
				       const Equation*, 
				       const ElementFuncNodeIterator&,
				       const MasterPosition&,
				       double time,
				       SmallSystem *) const;
  virtual void cross_reference(Material*) {}
  virtual int integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return true; }
  
protected:
  ScalarField *concentration;

};




class AtomFluxJumpTest : public EqnProperty 
{
private:
  double coef;
public:
  AtomFluxJumpTest(PyObject *reg, const std::string &name,
		  double coef);
  virtual ~AtomFluxJumpTest() {}
  virtual int integration_order(const CSubProblem*, const Element*) const;
  virtual bool constant_in_space() const { return true; }
  virtual void begin_element(const CSubProblem*, const Element*);
  virtual void end_element(const CSubProblem*, const Element*);
  virtual void cross_reference(Material*);
  virtual void post_process(CSubProblem*, const Element*) const;

  virtual void force_deriv_matrix(const FEMesh*, const Element*,
  				  const Equation*,
  				  const ElementFuncNodeIterator&,
  				  const MasterPosition&,
  				  double time, SmallSystem* ) const;
  virtual void force_value(const FEMesh*, const Element*,
  			   const Equation*, const MasterPosition&,
  			   double time, SmallSystem* ) const;
  

  // virtual void flux_offset(const FEMesh *mesh, const Element *element,
  //		   const Flux *flux, const MasterPosition &pt,
  //			   double time, SmallSystem *fluxdata) const;
  //virtual void flux_matrix(const FEMesh *mesh, const Element *el,
  //			   const ElementFuncNodeIterator &efi,
  //			   const Flux *flux, const MasterPosition &pt,
  //			   double time, SmallSystem *fluxdata) const;
};


#endif
