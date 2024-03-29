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
  int invert(SmallMatrix &ein, SmallMatrix &sout,
	     SmallTensor4 &dsde) const;
  Cijkl cijkl;
  double alpha;
  double s0;
  double n;

public:
  CRambergOsgood(PyObject *registry, PyObject *self, const std::string &name,
		const Cijkl &cijkl, double alpha, double s0, double n)
    : GeneralNonlinearElasticity(registry, name),
      PythonNative<Property>(self),
      cijkl(cijkl),
      alpha(alpha),
      s0(s0),
      n(n)
  {}
  virtual ~CRambergOsgood() {};

protected:
  virtual void nonlin_stress(double x, double y, double z,
			     double time, DoubleVec &displacement,
			     SmallMatrix &displacement_gradient,
			     SmallMatrix &stress) const;

  virtual void nonlin_stress_deriv_wrt_displacement(
                             double x, double y, double z,
			     double time, DoubleVec &displacement,
			     SmallMatrix &displacement_gradient,
			     SmallTensor3 &stress_deriv) const;

  virtual void nonlin_stress_deriv_wrt_displacement_gradient(
                             double x, double y, double z,
			     double time, DoubleVec &displacement,
			     SmallMatrix &displacement_gradient,
			     SmallTensor4 &stress_deriv) const;
};

#endif	// RAMBERGOSGOOD_H
