// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// This file contains the functions that must be defined when
// implementing a subclass of NonlinearHeatConductivity.  
//
// The heat equation solved by OOF2 is
//
//   (*)    div(J) + f = 0  (the static case)
// or
//   (**)   C dT/dt + div(J) + f = 0  (the time-dependent case)
//
// where J is the heat flux, C is heat capacity coefficient and div(.)
// is the divergence operator. We solve the equations (*) and (**) for
// the temperature field T.
//
// The nonlinear heat conductivity property specifies the heat flux
// function J in (*) & (**) as a function of the spatial coordinates
// x, y, time t, temperature T, and temperature gradient
// dT =(dT/dx, dT/dy, dT/dz)
//
//    J = ( J0(x,y,t,T,dT), J1(x,y,t,T,dT), J2(x,y,t,T,dT) )
//
// In the linear case, the heat flux is defined by J = -K dT,
// where K is the heat conductivity coefficient.
//
// A nonlinear heat conductivity property must define
//
//   DoubleVec nonlin_heat_flux(const Coord& pt,
// 		     	        double time, double temperature,
// 			        DoubleVec& temperature_gradient)
//
// where pt is the physical coordinate of the point where the flux is
// to be computed at the given time and temperature.
// temperature_gradient is a 3-vector containing the x, y, and z
// derivatives of the temperature.  The function returns a 3-vector
// containing the x, y, and z components of the heat flux.
//
// The nonlinear solver may require the definitions of the partial
// derivatives of the heat flux as well:
//
//   - the partial derivative of J with respect to temperature T
//
//        dJ/dT = ( dJ0/dT, dJ1/dT, dJ2/dT )
//
//   - the partial derivative of J with respect to the components
//     of the temperature gradient G = dT
//
//                | dJ0/dG0  dJ0/dG1  dJ0/dG2 |
//        dJ/dG = | dJ1/dG0  dJ1/dG1  dJ1/dG2 |
//                | dJ2/dG0  dJ2/dG1  dJ2/dG2 |
//      where
//          G = (G0 G1 G2) = ( dT/dx  dT/dy dT/dz )
//
// The partial derivative of heat flux with respect to temperature
// is defined by
//
//   DoubleVec nonlin_heat_flux_deriv_wrt_temperature(
//                      const Coord& pt, double time, double temperature,
// 			DoubleVec &temperature_gradient)
//
// The return value is a 3-vector containing the derivatives of the
// heat flux with respect to temperature,
//    (dJ0/dT, dJ1/dT, dJ2/dT)
//
// The partial derivative of heat flux with respect to temperature
// gradient is defined by
//
//   SmallMatrix nonlin_heat_flux_deriv_wrt_temperature_gradient(
//                           const Coord& pt, double time, double temperature,
// 			     DoubleVec &temperature_gradient)
//
// The return value is a 3x3 matrix storing the derivatives of the
// flux with respect to the temperature gradient:
//    dJdG(i,j) = dJ(i)/dG(j)
// with G defined above.



#include <oofconfig.h>
#include <math.h>
#include "%MODULENAME%.h"
#include "common/smallmatrix.h"


///////////////////////////////////////////////////////////////////////
//   FUNCTIONS CALLED BY NONLINEAR HEAT CONDUCTIVITY PROPERTY        //
///////////////////////////////////////////////////////////////////////

// The following function takes the spatial coordinate (pt), the time,
// the temperature, and the temperature gradient, and returns the
// corresponding heat flux value.

DoubleVec %CLASS%::nonlin_heat_flux(const Coord& pt, double time,
				    double temperature,
				    const DoubleVec &temperature_gradient)
const
{
  DoubleVec heatflux(3);
  
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT FLUX FUNCTIONS
  heatflux[0] = -atan(temperature_gradient[0]);
  heatflux[1] = -atan(temperature_gradient[1]);
  heatflux[2] =  0.0;
  // ========  END OF CHANGES =============================================

  return heatflux;
} // end of 'nonlin_heat_flux'


///////////////////////////////////////////////////////////////////////

// This function takes spatial coordinates (pt), time, temperature,
// and the temperature gradient, and returns the derivative of the
// heat flux with respect to the temperature.

DoubleVec %CLASS%::nonlin_heat_flux_deriv_wrt_temperature(
			  const Coord& pt, double time, double temperature,
			  const DoubleVec &temperature_gradient)
const
{
  DoubleVec heat_flux_deriv(3);

  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT FLUX DERIVATIVES
  heat_flux_deriv[0] = 0.0;
  heat_flux_deriv[1] = 0.0;
  heat_flux_deriv[2] = 0.0;
  // ========  END OF CHANGES =============================================

  return heat_flux_deriv;
} // end of 'nonlin_heat_flux_deriv_wrt_temperature'


// The following function takes the spatial coordinate pt, the time,
// the temperature and the temperature gradient, and returns the corresponding
// value of heat flux derivative with respect to the temperature gradient.

SmallMatrix %CLASS%::nonlin_heat_flux_deriv_wrt_temperature_gradient(
			     const Coord& pt, double time, double temperature,
			     const DoubleVec &temperature_gradient)
const
{
  SmallMatrix heat_flux_deriv(3);

  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT FLUX DERIVATIVES
  heat_flux_deriv(0,0) = -1.0 / (1.0 + pow(temperature_gradient[0], 2.0));
  heat_flux_deriv(0,1) =  0.0;
  heat_flux_deriv(0,2) =  0.0;

  heat_flux_deriv(1,0) =  0.0;
  heat_flux_deriv(1,1) = -1.0 / (1.0 + pow(temperature_gradient[1], 2.0));
  heat_flux_deriv(1,2) =  0.0;

  heat_flux_deriv(2,0) =  0.0;
  heat_flux_deriv(2,1) =  0.0;
  heat_flux_deriv(2,2) =  0.0;
  // ========  END OF CHANGES =============================================

  return heat_flux_deriv;
} // end of 'nonlin_heat_flux_deriv_wrt_temperature_gradient'
