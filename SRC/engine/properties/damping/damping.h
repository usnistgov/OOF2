// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef DAMPING_H
#define DAMPING_H

#include <oofconfig.h>

#include "engine/property.h"

class IsotropicDampingProp : public EqnProperty {
private:
  double coeff;
  Field *displacement;
  Equation *force_balance;
public:
  IsotropicDampingProp(const std::string&, PyObject*, double);
  virtual ~IsotropicDampingProp() {}
  virtual void precompute(FEMesh*);
  virtual void time_deriv_matrices(const FEMesh*,
				   const Element*,
				   const ElementFuncNodeIterator&,
				   const Equation*,
				   const MasterPosition&,
				   double time,
				   void*, 
				   SmallSystem*) const;
  virtual int integration_order(const CSubProblem*, const Element*) const;
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*);
};

// TODO: Add asymmetries?

#endif
