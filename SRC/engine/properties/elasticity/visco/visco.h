// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#include <oofconfig.h>

#ifndef ISOELASTICITY_H
#define ISOELASTICITY_H

#include <oofconfig.h>
#include "engine/properties/elasticity/cijkl.h"
#include "engine/property.h"
#include <string>

class CSubProblem;
class Element;
class ElementFuncNodeIterator;
class Flux;
class FEMesh;
class MasterPosition;
class SmallSystem;
class TwoVectorField;
class SymmetricTensorFlux;

// TODO: Add all symmetries.

class CViscoElasticity : public FluxProperty {
private:
  Cijkl g_ijkl;
  TwoVectorField *displacement;
  SymmetricTensorFlux *stress_flux;
public:
  CViscoElasticity(const std::string &name, PyObject *registration, Cijkl &g);
  virtual ~CViscoElasticity() {}
  virtual void flux_matrix(const FEMesh *mesh,
			   const Element *element,
			   const ElementFuncNodeIterator &nu,
			   const Flux *flux,
			   const MasterPosition &x,
			   double time,
			   SmallSystem *fluxmtx) const;
  virtual int integration_order(const CSubProblem*, const Element*) const;
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
};

#endif
