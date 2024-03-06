// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// This file contains the functions that are called by the nonlinear
// force density property.
//
// The user can change the functions given in the code below and
// specify other functional forms to define other nonlinear force
// densities.
//
// Given certain elasticity and force density (and possibly mass
// density) properties, the equation that is solved by OOF is
//
//   (*)    div(S_i) + f_i = 0  (the static case)
// or
//            d^2
//   (**)  -M --- U_i + div(S_i) + f_i = 0  (the time-dependent case)
//            dt^2
//
// for i=0,1 or i=0,1,2 (corresponding to x,y,z coordinates respectively).
// Other equations are possible by combining various material properties.
// In (*) and (**), f denotes the force density function (defined by
// specifying f_i for i=0,1 or i=0,1,2), S denotes the stress tensor
// (defined by specifying S_ij for i,j=0,1 or i,j=0,1,2), M is mass density
// and div(.) denotes the divergence operator. We solve the equations (*)
// and (**) for the displacement field U_n, n=0,1 or n=0,1,2.
//
// Now we describe the details of the nonlinear force density property.
//
// The nonlinear force density function has the following form
//
//     f_i = f_i( x, y, z, t, U_n )
//
// f_i is a vector-valued function of the spatial coordinates x, y, z,
// time t, and the components of the displacement field U.
// To be more explicit,
//
//              | f_0(.,U) |
//     f(.,U) = | f_1(.,U) |
//              | f_2(.,U) |
//
// where we suppress the arguments x,y,z,time with "." for brevity and
//
//       U = ( U_0, U_1, U_2 )
//
// is a vector/array.
//
// The nonlinear force density is defined in the following function
//
//   void nonlin_force_density(double x, double y, double z, double time,
//                             DoubleVec &displacement, DoubleVec &result)
//
// The arguments x, y, z, time and displacement are input to
// the nonlin_force_density function and the computed force density
// vector is output in the argument result.
// The argument displacement is of type DoubleVec and it stores
// the components of the displacement field
//
//    displacement[0] = U_0 = x-component of displacement
//    displacement[1] = U_1 = y-component of displacement
//  ( displacement[2] = U_2 = z-component of displacement   in 3D )
//
// The output argument result contains the components of the force
// density vector
//
//    result[0] = f_0(.,U)
//    result[1] = f_1(.,U)
//  ( result[2] = f_2(.,U)   in 3D )
//
// The nonlinear solver may require the definition of the derivative
// of force density vector as well. The derivative is with respect
// to components of the displacement vector and results in a Hessian
// matrix:
//
//    df/dU = { df_i/dU_j,  i,j=0,1,(2) }
//
// The partial derivative of force density with respect to displacement
// is defined in the following function. It is necessary to define this
// function if Newton's method will be used as a nonlinear solver.
// Otherwise it is optional.
//
//   void nonlin_force_density_deriv(double x, double y, double z,
//                                   double time, DoubleVec &displacement,
//                                   SmallMatrix &result)
//
// The arguments x, y, z, time, and displacement are input to
// the function and the corresponding derivative of force density
// is returned in the output argument result.
// The components of the partial derivative are stored in the array
// result as follows:
//
//    result(0,0) = df_0 / dU_0
//    result(0,1) = df_0 / dU_1
//    result(0,2) = df_0 / dU_2
//
//    result(1,0) = df_1 / dU_0
//    result(1,1) = df_1 / dU_1
//    result(1,2) = df_1 / dU_2
//
//    result(2,0) = df_2 / dU_0
//    result(2,1) = df_2 / dU_1
//    result(2,2) = df_2 / dU_2



#include <oofconfig.h>
#include <math.h>
#include "%MODULENAME%.h"
#include "common/smallmatrix.h"


///////////////////////////////////////////////////////////////////////
//        FUNCTIONS CALLED BY NONLINEAR FORCE DENSITY PROPERTY       //
///////////////////////////////////////////////////////////////////////


// The following function takes the spatial coordinate x,y,z, the time and
// displacement, and returns the corresponding force density value in 'result'.

void %CLASS%::nonlin_force_density(
                          double x, double y, double z, double time,
			  DoubleVec &displacement,
			  DoubleVec &result) const
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR FORCE DENSITY FUNCTIONS

  double exponent = parameter1; // user input parameters
  double coefficient = parameter2;

  double pi = M_PI, uex0, uex1, f0, f1;
  double m0 = 2.0, n0 = 3.0, m1 = 1.0, n1 = 2.0;

  uex0 = sin(m0*pi*x) * sin(n0*pi*y);
  uex1 = sin(m1*pi*x) * sin(n1*pi*y);

  f0 = (m0*m0 + n0*n0)*pi*pi*uex0 - uex0 + coefficient*pow(uex0, exponent);
  f1 = (m1*m1 + n1*n1)*pi*pi*uex1 - uex1 + coefficient*pow(uex1, exponent);

  result[0] = displacement[0] - coefficient*pow(displacement[0], exponent) + f0;
  result[1] = displacement[1] - coefficient*pow(displacement[1], exponent) + f1;
  result[2] = 0.0;

  // ========  END OF CHANGES ==============================================

} // end of '%CLASS%::nonlin_force_density'


//////////////////////////////////////////////////////////////////////////

// The following function takes the spatial coordinate x,y,z, the time
// and the displacement, and returns the corresponding value of force density
// derivative in 'result'. The force density derivative is with respect to
// the components of the displacement field.
// Since force density function has DIM = 2,3 components and the displacement
// field has DIM = 2,3 components, the returned result is a 2x2 or 3x3 matrix.

void %CLASS%::nonlin_force_density_deriv(
                                double x, double y, double z, double time,
				DoubleVec &displacement,
				SmallMatrix &result) const
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR FORCE DENSITY DERIVATIVES
  double exponent = parameter1;
  double coefficient = parameter2;

  result(0,0) = 1.0 - coefficient*exponent * pow(displacement[0], exponent-1.0);
  result(0,1) = 0.0;
  result(0,2) = 0.0;

  result(1,0) = 0.0;
  result(1,1) = 1.0 - coefficient*exponent*pow(displacement[1], exponent-1.0);
  result(1,2) = 0.0;

  result(2,0) = result(2,1) = result(2,2) = 0.0;

  // ========  END OF CHANGES ==============================================

} // end of '%CLASS%::nonlin_force_density_deriv'
