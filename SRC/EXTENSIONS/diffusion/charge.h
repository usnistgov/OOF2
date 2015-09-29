// -*- C++ -*-
// $RCSfile: charge.h,v $
// $Revision: 1.2 $
// $Author: reida $
// $Date: 2012/03/26 20:54:17 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// atom conductivity property

#ifndef CHARGE_H
#define CHARGE_H


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

class Current : public FluxProperty {
public:
  Current(PyObject *registry, const std::string &name);
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
  ScalarField *voltage;
  VectorFlux  *charge_flux;
};


class IsoCurrent : public Current {
public:
  IsoCurrent(PyObject *registry,
		      const std::string &name, double K);
  virtual void cross_reference(Material*) {}
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const;
private:
  double K_;
};


class AnisoCurrent : public Current {
public:
  AnisoCurrent(PyObject *registry, const std::string &name, SymmMatrix3 *K);
  virtual void cross_reference(Material*); // finds Orientation
  virtual void precompute(FEMesh*);
  virtual const SymmMatrix3 conductivitytensor(const FEMesh*, const Element*,
					       const MasterPosition&) const;
private:
  SymmMatrix3 K_;
  OrientationPropBase *orientation;
};


#endif
