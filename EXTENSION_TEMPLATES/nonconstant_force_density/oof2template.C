// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// This file contains the functions that are called by the nonconstant
// force density property.
//
// The user can change the functions given in the code below and
// specify other functional forms to define other nonconstant force
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
// The nonconstant force density function has the following form
//
//     f_i = f_i( x, y, z, t )
//
// f_i is a vector-valued function of the spatial coordinates x, y, z,
// time t. To be more explicit,
//
//              | f_0(x,y,z,t) |
//     f(.,U) = | f_1(x,y,z,t) |
//              | f_2(x,y,z,t) |
//
// The nonconstant force density is defined in the following function
//
//   void nonconst_force_density(double x, double y, double z,
//                               double time, DoubleVec &result)



#include <oofconfig.h>
#include <math.h>
#include "%MODULENAME%.h"


///////////////////////////////////////////////////////////////////////
//        FUNCTION CALLED BY NONCONSTANTFORCE DENSITY PROPERTY       //
///////////////////////////////////////////////////////////////////////


// The following function takes the spatial coordinate x,y,z and
// the time, and returns the corresponding force density value in 'result'.

void %CLASS%::nonconst_force_density(
                               double x, double y, double z,
			       double time, DoubleVec &result) const
{
  // ========  CHANGE THESE LINES FOR OTHER VARIABLE FORCE DENSITY FUNCTIONS

  double m = parameter1;
  double n = parameter2;

  double pi = M_PI;
  double Ux, Uxx, Uyy, Uyx, Vy, Vxx, Vyy, Vxy;

  // U(x,y) = sin(m*pi*x) * sin(n*pi*y)
  Ux  =  m*pi * cos(m*pi*x) * sin(n*pi*y);
  Uxx = -m*pi*m*pi * sin(m*pi*x) * sin(n*pi*y);
  Uyy = -n*pi*n*pi * sin(m*pi*x) * sin(n*pi*y);
  Uyx =  m*pi*n*pi * cos(m*pi*x) * cos(n*pi*y);

  // V(x,y) = x^2 + y^2
  Vy  =  2.0*y;
  Vxx =  2.0;
  Vyy =  2.0;
  Vxy =  0.0;

  result[0] = - ( (1.0 + 3.0*Ux*Ux)*Uxx + Uyy + Vxy );
  result[1] = - ( Vxx + (1.0 + 3.0*Vy*Vy)*Vyy + Uyx );
  result[2] = 0.0;

  // ========  END OF CHANGES ==============================================

} // end of '%CLASS%::nonconstant_force_density'

