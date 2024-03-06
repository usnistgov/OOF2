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

#include "engine/properties/forcedensity/nonlinear/nonlinear_force_density.h"
#include <string>

class SmallMatrix;
class DoubleVec;

class %CLASS% : public NonlinearForceDensity {

private:
  double parameter1, parameter2;

public:
  %CLASS%(PyObject *registry, const std::string &name,
	  double param1, double param2)
    : NonlinearForceDensity( registry, name ),
      parameter1( param1 ), parameter2( param2 ) {};
  virtual ~%CLASS%() {};

protected:

  virtual void nonlin_force_density(double x, double y, double z,
				    double time,
				    DoubleVec &displacement,
				    DoubleVec &result) const;

  virtual void nonlin_force_density_deriv(double x, double y, double z,
					  double time,
					  DoubleVec &displacement,
					  SmallMatrix &result) const;
};

#endif	// %HEADER%
