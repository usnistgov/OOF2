// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef %HEADER%
#define %HEADER%

#include "engine/properties/elasticity/nonlinear/general_nonlinear_elasticity.h"
#include <string>

class DoubleVec;
class SmallMatrix;
class SmallTensor3;
class SmallTensor4;

class %CLASS% : public GeneralNonlinearElasticity {

private:
  double parameter1, parameter2;

public:
  %CLASS%(const std::string &name, PyObject *registration,
	 double param1, double param2)
    : GeneralNonlinearElasticity(name, registration),
      parameter1(param1),
      parameter2(param2)
    {}
  
  virtual ~%CLASS%() {}

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

#endif // %HEADER%
