// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef RAMBERGOSGOOD_H
#define RAMBERGOSGOOD_H

#include "engine/properties/elasticity/cijkl.h"
#include "engine/properties/elasticity/nonlinear/general_nonlinear_elasticity.h"
#include <string>

class Doublevec;
class SmallMatrix;
class SmallTensor4;

class CRambergOsgood
  : public GeneralNonlinearElasticity, virtual public PythonNative<Property>
{

private:
  int invert(const SmallMatrix &ein, SmallMatrix &sout, SmallTensor4 &dsde) const;
  Cijkl cijkl;
  double alpha;
  double s0;
  double n;

public:
  CRambergOsgood(const std::string &name, PyObject *registration,
		 PyObject *self, 
		const Cijkl &cijkl, double alpha, double s0, double n)
    : GeneralNonlinearElasticity(name, registration),
      PythonNative<Property>(self),
      cijkl(cijkl),
      alpha(alpha),
      s0(s0),
      n(n)
  {}
  virtual ~CRambergOsgood() {};

protected:
  virtual SmallMatrix nonlin_stress(const Coord &pt, double time,
				    const DoubleVec &displacement,
				    const SmallMatrix &displacement_gradient)
    const;

  virtual SmallTensor3 nonlin_stress_deriv_wrt_displacement(
				    const Coord &pt, double time,
				    const DoubleVec &displacement,
				    const SmallMatrix &displacement_gradient)
    const;

  virtual SmallTensor4 nonlin_stress_deriv_wrt_displacement_gradient(
				     const Coord &pt, double time,
				     const DoubleVec &displacement,
				     const SmallMatrix &displacement_gradient)
    const;
};

#endif	// RAMBERGOSGOOD_H
