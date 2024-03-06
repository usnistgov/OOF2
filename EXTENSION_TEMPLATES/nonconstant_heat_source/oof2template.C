// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// This file contains the functions that are called by
// nonconstant heat source property.
//
// The user can change the functions given below and specify other
// functional forms to define other nonconstant heat sources.
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
// Nonconstant heat source property specifies the heat source
// function f in (*), (**) as/ a function of the spatial coordinates
// x, y, z and time t,
//
//      f = f(x,y,z,t)
//
// The third variable z is not relevant for 2D experiments.
// The definition of f is done in the following function:
//
//   double nonconst_heat_source(double x, double y, double z, double time)
//
// This returns the value of the heat source function.



#include <oofconfig.h>
#include <math.h>
#include "%MODULENAME%.h"


///////////////////////////////////////////////////////////////////////
//        FUNCTION CALLED BY NONCONSTANT HEAT SOURCE PROPERTY        //
///////////////////////////////////////////////////////////////////////


// The following function takes the spatial coordinate x,y,z and
// the time, and returns the corresponding heat source value.

double %CLASS%::nonconst_heat_source(
                               double x, double y, double z, double time) const
{
  double source_value;

  // ========  CHANGE THESE LINES FOR OTHER NONCONSTANT HEAT SOURCE FUNCTIONS

  double m = parameter1;
  double n = parameter2;

  double Ux, Uy, Uxx, Uyy, pi=M_PI;

  Ux  = m*pi * cos(m*pi*x) * sin(n*pi*y);
  Uy  = n*pi * sin(m*pi*x) * cos(n*pi*y);

  Uxx = -m*m*pi*pi * sin(m*pi*x) * sin(n*pi*y);
  Uyy = -n*n*pi*pi * sin(m*pi*x) * sin(n*pi*y);

  source_value = Uxx / (1.0 + Ux*Ux) + Uyy / (1.0 + Uy*Uy);

  // ========  END OF CHANGES =============================================

  return source_value;

} // end of '%CLASS%::nonconstant_heat_source'
