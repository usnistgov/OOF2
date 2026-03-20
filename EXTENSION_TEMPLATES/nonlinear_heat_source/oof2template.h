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
  // If there are parameters to be set by the user, they must be
  // stored here, passed in as arguments to the constructor below, and
  // initialized by the constructor.  They must also be listed in the
  // PropertyRegistration in %MODULENAME%.spy, and in the swig
  // declaration of the constructor in %MODULENAME%.swg.  There can be
  // any non-negative number of parameters.  Give them better names
  // than "parameter1" and "parameter2".
  double parameter1, parameter2;

public:
  %CLASS%(const std::string& name, PyObject* registration,
	  double param1, double param2)
    : NonlinearHeatSource(name, registration),
      parameter1(param1),
      parameter2(param2)
    {};

  virtual ~%CLASS%() {};

protected:

  virtual double nonlin_heat_source(
		    const Coord& pt, double time, double temperature) const;

  virtual double nonlin_heat_source_deriv_wrt_temperature(
		  const Coord& pt, double time, double temperature) const;

};

#endif	// %HEADER%
