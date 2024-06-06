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

#include "engine/properties/heatsource/nonlinear/nonlinear_heat_source.h"
#include <string>

class %CLASS% : public NonlinearHeatSource {

private:
  double parameter1, parameter2;

public:
  %CLASS%(const std::string &name, PyObject *registration,
	  double param1, double param2)
    : NonlinearHeatSource(name, registration),
      parameter1(param1),
      parameter2(param2)
    {};

  virtual ~%CLASS%() {};

protected:

  virtual double nonlin_heat_source(double x, double y, double z,
				    double time, double temperature) const;

  virtual double nonlin_heat_source_deriv_wrt_temperature(
                                    double x, double y, double z,
				    double time, double temperature) const;

};

#endif	// %HEADER%
