// -*- C++ -*-
// $RCSfile: nonlinear_heat_conductivity_example.h,v $
// $Revision: 1.8 $
// $Author: langer $
// $Date: 2011-02-18 19:45:12 $

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


#include "engine/property/heatconductivity/nonlinear/nonlinear_heat_conductivity.h"
#include <string>
#include <vector>

class SmallMatrix;
class DoubleVec;


class %CLASS% : public NonlinearHeatConductivity {

private:
  double parameter1, parameter2;

public:
  %CLASS%(PyObject *registry, const std::string &name,
				   double param1, double param2)
    : NonlinearHeatConductivity( registry, name ),
      parameter1( param1 ), parameter2( param2 )
  {}
  
  virtual ~%CLASS%() {}

protected:

  virtual void nonlin_heat_flux(double x, double y, double z,
				double time, double temperature,
				const DoubleVec &temperature_gradient,
				DoubleVec &heat_flux) const;

  virtual void nonlin_heat_flux_deriv_wrt_temperature(
                                double x, double y, double z,
				double time, double temperature,
				const DoubleVec &temperature_gradient,
				DoubleVec &heat_flux_deriv) const;

  virtual void nonlin_heat_flux_deriv_wrt_temperature_gradient(
                                double x, double y, double z,
				double time, double temperature,
				const DoubleVec &temperature_gradient,
				SmallMatrix &heat_flux_deriv) const;
};

#endif	// %HEADER%
