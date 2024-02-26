// -*- C++ -*-
// $RCSfile: nonlinear_heat_source_example.C,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2011-02-17 22:44:47 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */



// The user can change the functions given below and specify other
// functional forms to define other nonlinear heat sources.
//
// Given certain heat conductivity and heat source properties,
// the equation that is solved by OOF is
//
//   (*)    div(J) + f = 0  (the static case)
// or
//   (**)   C dT/dt + div(J) + f = 0  (the time-dependent case)
//
// where J is the heat flux (= -K gradient(T) in the linear case),
// C is heat capacity coefficient and div(.) denotes the divergence
// operator. We solve the equations (*) and (**) for the temperature
// field T.
//
// The heat source function f is specified as a function of
// the spatial coordinates x, y, z, time t, and temperature T,
//
//      f = f(x,y,z,t,T)
//
// The third variable z is not relevant for 2D experiments.
// The definition of f is done in the following function
//
//   double nonlin_heat_source(double x, double y, double z,
// 			       double time, double temperature)
//
// This returns the computed value of the heat source function.
//
// In order to use Newton's method to solve the resulting equation,
// we also need to specify the first partial derivative df/dT of
// the source function f with respect to the temperature variable T.
// This is done in the following function
//
//   double nonlin_heat_source_deriv_wrt_temperature(double x, double y, double z,
// 	 					  double time, double temperature)
//
// This returns the value of the partial derivative with respect
// to temperature.
//
// The definition of the derivative function is optional if
// Newton's method is not used to solve the equation
// (for example, if Picard iterations are used).



#include <oofconfig.h>
#include <math.h>
#include "%MODULENAME%.h"


///////////////////////////////////////////////////////////////////////
//        FUNCTIONS CALLED BY NONLINEAR HEAT SOURCE PROPERTY         //
///////////////////////////////////////////////////////////////////////


// The following function takes the spatial coordinates x,y,z, the time
// and temperature, and returns the corresponding heat source value.

double %CLASS%::nonlin_heat_source(
                                double x, double y, double z,
				double time, double temperature) const
{
  double source_value;

  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT SOURCE FUNCTIONS

  double c1 = parameter1;
  double c2 = parameter2;

  source_value = c1 * exp( c2*temperature );

  // ========  END OF CHANGES =============================================

  return source_value;

} // end of '%CLASS%::nonlin_heat_source'


///////////////////////////////////////////////////////////////////////

// The following function takes the spatial coordinates x,y,z, the time
// and the temperature, and returns the corresponding value of heat source
// derivative with respect to the temperature field.

double %CLASS%::nonlin_heat_source_deriv_wrt_temperature(
                                double x, double y, double z,
				double time, double temperature) const
{
  double source_deriv_value;

  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT SOURCE DERIVATIVES

  double c1 = parameter1;
  double c2 = parameter2;

  source_deriv_value = c1*c2 * exp( c2*temperature );


  // ========  END OF CHANGES =============================================

  return source_deriv_value;

} // end of '%CLASS%::nonlin_heat_source_deriv_wrt_temperature'


