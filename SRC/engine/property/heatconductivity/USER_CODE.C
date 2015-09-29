// -*- C++ -*-
// $RCSfile: USER_CODE.C,v $
// $Revision: 1.9 $
// $Author: langer $
// $Date: 2014/09/27 21:41:14 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */



// This file contains the functions that are called by the following
// material properties nonlinear heat flux property,
//
// The user can change the functions given below and specify other
// functional forms to define other nonlinear heat fluxes.
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
// Now we describe the details of the nonlinear heat conductivity
// property.
//
// The nonlinear heat conductivity property specifies the heat flux
// function J in (*) & (**) as a function of the spatial coordinates
// x, y, z, time t, temperature T and temperature gradient
// dT =(dT/dx, dT/dy, dT/dz)
//
//    J = ( J0, J1, J2 )
//
//    J = ( J0(x,y,z,t,T,dT), J1(x,y,z,t,T,dT), J2(x,y,z,t,T,dT) )
//
// The z component J2 of J is not relevant for 2D experiments
// (and should not be defined). Similarly the spatial coordinate
// z is not relevant in 2D experiments.
//
// In the linear case, the heat flux is defined by J = -K dT,
// where K is the heat conductivity coefficient and this can
// be done through the user interface for material property
// definitions.
//
// The nonlinear heat flux is defined in the following function
//
//   void nonlin_heat_flux(double x, double y, double z,
// 		     	   double time, double temperature,
// 			   double temperature_gradient[3],
// 		 	   double heat_flux[3])
//
// The arguments x, y, z, time, temperature, temperature_gradient
// are input to the nonlin_heat_flux function and the computed
// heat flux vector is output in the argument heat_flux.
// The argument temperature_gradient is an array of size 3
// and it stores the values of the temperature gradient
// in the following fashion:
//
//    temperature_gradient[0] = dT/dx
//    temperature_gradient[1] = dT/dy
//  ( temperature_gradient[2] = dT/dz  in 3D )
//
// The output argument heat_flux contains the components of
// the heat flux vector:
//
//    heat_flux[0] = J0
//    heat_flux[1] = J1
//  ( heat_flux[2] = J2  in 3D )
//
// Currently the nonlinear solver requires the definitions
// of the derivatives of the heat flux as well:
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
// is defined in the following function
//
//   void nonlin_heat_flux_deriv_wrt_temperature(double x, double y, double z,
// 					      double time, double temperature,
// 					      double temperature_gradient[3],
// 					      double heat_flux_deriv[3])
//
// The arguments x, y, z, time, temperature, temperature_gradient
// are input to the function and the corresponding heat flux
// derivative is returned in the output argument heat_flux_deriv.
// The components of the partial derivative are stored in the array
// heat_flux_deriv as follows:
//
//    heat_flux_deriv[0] = dJ0/dT
//    heat_flux_deriv[1] = dJ1/dT
//  ( heat_flux_deriv[2] = dJ2/dT  in 3D )
//
// The partial derivative of heat flux with respect to temperature
// gradient is defined in the following function
//
//   void nonlin_heat_flux_deriv_wrt_temperature_gradient(
//                                            double x, double y, double z,
// 					      double time, double temperature,
// 					      double temperature_gradient[3],
// 					      double heat_flux_deriv[3][3])
//
// The arguments x, y, z, time, temperature, temperature_gradient
// are input to the function and the corresponding heat flux
// derivative is returned in the output argument heat_flux_deriv.
// The components of the derivative are stored in the two-dim array
// as follows:
//
//    heat_flux_deriv[0][0] = dJ0/dG0
//    heat_flux_deriv[0][1] = dJ0/dG1
//  ( heat_flux_deriv[0][2] = dJ0/dG2  in 3D )
//
//    heat_flux_deriv[1][0] = dJ1/dG0
//    heat_flux_deriv[1][1] = dJ1/dG1
//  ( heat_flux_deriv[1][2] = dJ1/dG2  in 3D )
//
//  ( heat_flux_deriv[2][0] = dJ2/dG0  in 3D )
//  ( heat_flux_deriv[2][1] = dJ2/dG1  in 3D )
//  ( heat_flux_deriv[2][2] = dJ2/dG2  in 3D )
//
// (recall G = (G0 G1 G2) = (dT/dx dT/dy dT/dz))



#include <oofconfig.h>
#include <math.h>


// some helper functions

inline double SQR(double x){ return x*x; }
inline double CUBE(double x){ return x*x*x; }


///////////////////////////////////////////////////////////////////////
//        FUNCTIONS CALLED BY NONLINEAR HEAT FLUX PROPERTY           //
///////////////////////////////////////////////////////////////////////


// The following function takes the spatial coordinate x,y,z, the time,
// the temperature, and the temperature gradient, and returns the
// corresponding heat flux value.

void nonlin_heat_flux(double x, double y, double z,
		      double time, double temperature,
		      double temperature_gradient[3],
		      double heat_flux[3])
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT FLUX FUNCTIONS

  heat_flux[0] = temperature_gradient[0] + CUBE( temperature_gradient[0] ) / 3.0;
  heat_flux[1] = temperature_gradient[1];

  // double rho = 0.1;
  // heat_flux[0] = -temperature_gradient[0] - 0.5*rho * SQR( temperature_gradient[0] );
  // heat_flux[1] = -temperature_gradient[1] - 0.5*rho * SQR( temperature_gradient[1] );
#if DIM==3
  heat_flux[2] = 0.0;
#endif

  // ========  END OF CHANGES =============================================

} // end of 'nonlin_heat_flux'


// The following function takes the spatial coordinate x,y,z, the time,
// the temperature and the temperature gradient, and returns the corresponding
// value of heat flux derivative with respect to the temperature.

void nonlin_heat_flux_deriv_wrt_temperature(double x, double y, double z,
					    double time, double temperature,
					    double temperature_gradient[3],
					    double heat_flux_deriv[3])
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT FLUX DERIVATIVES

  heat_flux_deriv[0] = 0.0;
  heat_flux_deriv[1] = 0.0;
#if DIM==3
  heat_flux_deriv[2] = 0.0;
#endif

  // ========  END OF CHANGES =============================================

} // end of 'nonlin_heat_flux_deriv_wrt_temperature'


// The following function takes the spatial coordinate x,y,z, the time,
// the temperature and the temperature gradient, and returns the corresponding
// value of heat flux derivative with respect to the temperature gradient.

void nonlin_heat_flux_deriv_wrt_temperature_gradient(double x, double y, double z,
						     double time, double temperature,
						     double temperature_gradient[3],
						     double heat_flux_deriv[3][3])
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR HEAT FLUX DERIVATIVES

  heat_flux_deriv[0][0] = 1.0 + SQR( temperature_gradient[0] );
  heat_flux_deriv[0][1] = 0.0;
  heat_flux_deriv[1][0] = 0.0;
  heat_flux_deriv[1][1] = 1.0;

  // double rho = 0.1;
  // heat_flux_deriv[0][0] = -1.0 - rho * temperature_gradient[0];
  // heat_flux_deriv[0][1] =  0.0;
  // heat_flux_deriv[1][0] =  0.0;
  // heat_flux_deriv[1][1] = -1.0 - rho * temperature_gradient[1];

#if DIM==3
  heat_flux_deriv[0][2] = 0.0;
  heat_flux_deriv[1][2] = 0.0;
  heat_flux_deriv[2][0] = 0.0;
  heat_flux_deriv[2][1] = 0.0;
  heat_flux_deriv[2][2] = 0.0;
#endif

  // ========  END OF CHANGES =============================================

} // end of 'nonlin_heat_flux_deriv_wrt_temperature_gradient'
