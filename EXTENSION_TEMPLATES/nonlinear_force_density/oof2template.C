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
// The user can change the functions given in the code below to define
// other nonlinear force densities.
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
// for i=0,1 (corresponding to x,y).  Other equations are possible by
// combining various material properties.  In (*) and (**), f is the
// force density function, S is the stress tensor, M is mass density
// and div(.) is the divergence operator. We solve the equations (*)
// and (**) for the displacement field U_n, n=0,1.
//
// The nonlinear force density function is a vector-valued function of
// the spatial coordinates x and y, time t, and the displacement field
// U.  It is computed by
//
//   DoubleVec nonlin_force_density(const Coord& pt, double time,
//                                  const DoubleVec& displacement)
//
// The displacement parameter and the return values are DoubleVecs of
// size 2, containing the x and y components of the displacement field
// and the force density respectively.
//
// The nonlinear solver may require the definition of the derivative
// of force density vector as well. The derivative is with respect
// to components of the displacement vector and results in a Hessian
// matrix:
//
//    df/dU = { df_i/dU_j,  i,j=0,1 }
//
// The partial derivative of force density with respect to displacement
// is computed by nonlin_force_density_deriv. It is necessary to define this
// function if Newton's method will be used as a nonlinear solver.
// Otherwise it is optional.  Its form is
//
//   SmallMatrix nonlin_force_density_deriv(const Coord& pt, double time,
//                                          const DoubleVec &displacement)
//
// The return value is a 2x2 matrix containing the partial derivatives with
//   result(i,j) = df_i/dU_j

#include <oofconfig.h>
#include <math.h>
#include "%MODULENAME%.h"
#include "common/smallmatrix.h"


///////////////////////////////////////////////////////////////////////
//        FUNCTIONS CALLED BY NONLINEAR FORCE DENSITY PROPERTY       //
///////////////////////////////////////////////////////////////////////

// Given the spatial coordinate pt, the time, and displacement,
// compute and return the force density.

DoubleVec %CLASS%::nonlin_force_density(const Coord& pt, double time,
					const DoubleVec& displacement)
const
{
  DoubleVec result(2);

  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR FORCE DENSITY FUNCTIONS
  double x = pt[0];
  double y = pt[1];
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
  // ========  END OF CHANGES ==============================================

  return result;
} // end of '%CLASS%::nonlin_force_density'


//////////////////////////////////////////////////////////////////////////

// The following function takes the spatial coordinate x,y,z, the time
// and the displacement, and returns the corresponding value of force density
// derivative in 'result'. The force density derivative is with respect to
// the components of the displacement field.
// Since force density function has DIM = 2,3 components and the displacement
// field has DIM = 2,3 components, the returned result is a 2x2 or 3x3 matrix.

SmallMatrix %CLASS%::nonlin_force_density_deriv(const Coord& pt, double time,
						const DoubleVec& displacement)
const
{
  SmallMatrix result(2);
  
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR FORCE DENSITY DERIVATIVES
  double exponent = parameter1;
  double coefficient = parameter2;

  result(0,0) = 1.0 - coefficient*exponent * pow(displacement[0], exponent-1.0);
  result(0,1) = 0.0;

  result(1,0) = 0.0;
  result(1,1) = 1.0 - coefficient*exponent*pow(displacement[1], exponent-1.0);

  // ========  END OF CHANGES ==============================================

  return result;
} // end of '%CLASS%::nonlin_force_density_deriv'
