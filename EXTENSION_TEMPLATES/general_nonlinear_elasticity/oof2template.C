// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// This file contains the functions that are called by the general
// nonlinear elasticity property.
//
// The user can change the functions given in the code below and
// specify other functional forms to define other nonlinear stresses.
//
// Given certain elasticity (and possibly force density and mass
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
// In (*) and (**), S denotes the stress tensor (defined by specifying
// S_ij for i,j=0,1 or i,j=0,1,2), M is mass density and div(.)
// denotes the divergence operator. We solve the equations (*) and (**)
// for the displacement field U_n, n=0,1 or n=0,1,2.
//
// Now we describe the details of the general nonlinear elasticity
// property. Note that we do not consider the specific geometric
// nonlinear elasticity (or large-deformation elasticity or
// large-strain elasticity or finite-strain elasticity, which are
// the same). Geometric nonlinear elasticity is available in OOF
// as a separate predefined property and need not be defined using
// this file.
//
// In this file, our focus is on general nonlinearities that use
// a mapping from a displacement field U_n, n=0,1,2, and its spatial
// derivatives dU_kl, k,l=0,1,2, to the stress tensor. We assume 3D
// for the sake of presentation although the third components or
// z-components are not relevant for 2D experiments and should not
// be defined. The stress tensor has the following form
//
//     S_ij = S_ij( x, y, z, t, U_n, dU_kl ),
//
// S_ij is a matrix/array-valued function of the spatial coordinates
// x, y, z, time t, and the components of U and dU. To be more explicit,
//
//                |  S_00(.,U,dU)   S_01(.,U,dU)   S_02(.,U,dU)  |
//    S(.,U,dU) = |  S_10(.,U,dU)   S_11(.,U,dU)   S_12(.,U,dU)  |
//                |  S_20(.,U,dU)   S_21(.,U,dU)   S_22(.,U,dU)  |
//
// where we suppress the arguments x,y,z,time with "." for brevity and
//
//       U = ( U_0, U_1, U_2 )
//
// is a vector/array and
//
//          |  dU_00  dU_01  dU_02  |
//     dU = |  dU_10  dU_11  dU_12  |
//          |  dU_20  dU_21  dU_22  |
//
//          |  dU_0/dx   dU_0/dy   dU_0/dz  |
//     dU = |  dU_1/dx   dU_1/dy   dU_1/dz  |
//          |  dU_2/dx   dU_2/dy   dU_2/dz  |
//
// is the Jacobian or the matrix of spatial derivatives, represented
// by a 2D array.
//
// The nonlinear stress is defined in the following function
//
//   void nonlin_stress(double x, double y, double z,
//	 	        double time, double displacement[3],
//		        double displacement_gradient[3][3],
//		        double stress[3][3])
//
// The arguments x, y, z, time, displacement, displacement_gradient
// are input to the nonlin_stress function and the computed stress
// tensor is output in the argument stress.
// The argument displacement is an array of size 3 and it stores
// the components of the displacement field
//
//    displacement[0] = U_0 = x-component of displacement
//    displacement[1] = U_1 = y-component of displacement
//  ( displacement[2] = U_2 = z-component of displacement   in 3D )
//
// The argument displacement_gradient is a 3x3 array and it stores
// the spatial derivatives of the components of the displacement
// field in the following fashion
//
//    displacement_gradient(0,0) = dU_0/dx
//    displacement_gradient(0,1) = dU_0/dy
//  ( displacement_gradient(0,2) = dU_0/dz  in 3D )
//
//    displacement_gradient(1,0) = dU_1/dx
//    displacement_gradient(1,1) = dU_1/dy
//  ( displacement_gradient(1,2) = dU_1/dz  in 3D )
//
//  ( displacement_gradient(2,0) = dU_2/dx  in 3D )
//  ( displacement_gradient(2,1) = dU_2/dy  in 3D )
//  ( displacement_gradient(2,2) = dU_2/dz  in 3D )
//
// The output argument stress contains the components of the stress
//
//    stress(0,0) = S_00(.,U,dU)
//    stress(0,1) = S_01(.,U,dU)
//  ( stress(0,2) = S_02(.,U,dU)  in 3D )
//
//    stress(1,0) = S_10(.,U,dU)
//    stress(1,1) = S_11(.,U,dU)
//  ( stress(1,2) = S_12(.,U,dU)  in 3D )
//
//  ( stress(2,0) = S_20(.,U,dU)  in 3D )
//  ( stress(2,1) = S_21(.,U,dU)  in 3D )
//  ( stress(2,2) = S_22(.,U,dU)  in 3D )
//
// Currently the nonlinear solver requires the definitions
// of the derivatives of the stress tensor as well:
//
//   - the partial derivative of S with respect to
//     the components of the displacement U
//
//        dS/dU = { dS_ij/dU_n,  i,j,n=0,1,2 }
//
//   - the partial derivative of S with respect to
//     the spatial derivatives dU(k,l) = dU(k)/dx(l)
//     of the components U(k) of the displacement U
//
//        dS/dG = { dS_ij/dG_kl, i,j,k,l=0,1,2 }
//     where
//          G_kl = dU_kl = dU_k/dx_l   (x_l is one of x,y,z)
//
// The partial derivative of stress with respect to displacement is
// defined in the following function. It is necessary to define this
// function if Newton's method will be used as a nonlinear solver.
// Otherwise it is optional.
//
//   void nonlin_stress_deriv_wrt_displacement(double x, double y, double z,
//					  double time, DoubleVec &displacement,
//					  SmallMatrix &displacement_gradient,
//					  SmallTensor3 &stress_deriv)
//
// The arguments x, y, z, time, displacement, displacement_gradient
// are input to the function and the corresponding derivative of
// stress is returned in the output argument stress_deriv.
// The components of the partial derivative are stored in the array
// stress_deriv as follows:
//
//    stress_deriv[0][0][0] = dS_00 / dU_0
//    stress_deriv[0][0][1] = dS_00 / dU_1
//  ( stress_deriv[0][0][2] = dS_00 / dU_2  in 3D )
//
//    stress_deriv[0][1][0] = dS_01 / dU_0
//    stress_deriv[0][1][1] = dS_01 / dU_1
//  ( stress_deriv[0][1][2] = dS_01 / dU_2  in 3D )
//
//    stress_deriv[0][2][0] = dS_02 / dU_0
//    stress_deriv[0][2][1] = dS_02 / dU_1
//  ( stress_deriv[0][2][2] = dS_02 / dU_2  in 3D )
//
//    stress_deriv[1][0][0] = dS_10 / dU_0
//                       :
//                       :
//                       :
//  ( stress_deriv[2][2][2] = dS_22 / dU_2  in 3D )
//
// The partial derivative of stress with respect to displacement_gradient
// is defined in the following function. It is necessary to define this
// function if Newton's method will be used as a nonlinear solver.
// Otherwise it is optional.
//
//   void nonlin_stress_deriv_wrt_displacement_gradient(double x, double y, double z,
//					     double time, DoubleVec &displacement,
//					     SmallMatrix &displacement_gradient,
//					     SmallTensor4 &stress_deriv)
//
// The arguments x, y, z, time, displacement, displacement_gradient
// are input to the function and the corresponding stress derivative
// is returned in the output argument stress_deriv.
// The components of the derivative are stored in the four-dim array
// as follows:
//
//    stress_deriv(0,0,0,0) = dS_00 / dG_00    (recall G_kl = dU_k/dx_l)
//    stress_deriv(0,0,0,1) = dS_00 / dG_01
//  ( stress_deriv(0,0,0,2) = dS_00 / dG_02  in 3D)
//
//    stress_deriv(0,0,1,0) = dS_00 / dG_10
//    stress_deriv(0,0,1,1) = dS_00 / dG_11
//    stress_deriv(0,0,1,2) = dS_00 / dG_12  in 3D)
//
//  ( stress_deriv(0,0,2,0) = dS_00 / dG_20  in 3D)
//  ( stress_deriv(0,0,2,1) = dS_00 / dG_21  in 3D)
//  ( stress_deriv(0,0,2,2) = dS_00 / dG_22  in 3D)
//
//
//    stress_deriv(0,1,0,0) = dS_01 / dG_00
//                   :
//  ( stress_deriv(0,1,2,2) = dS_01 / dG_22  in 3D)
//
//
//    stress_deriv(0,2,0,0) = dS_02 / dG_00
//                   :
//  ( stress_deriv(0,2,2,2) = dS_02 / dG_22  in 3D)
//
//
//
//    stress_deriv(1,0,0,0) = dS_10 / dG_00
//                    :
//                    :
//                    :
//  ( stress_deriv(2,2,2,2) = dS_22 / dG_22  in 3D)



#include <oofconfig.h>
#include <math.h>
#include "%MODULENAME%.h"
#include "common/doublevec.h"
#include "common/smallmatrix.h"
#include "engine/smalltensor.h"


///////////////////////////////////////////////////////////////////////
//        FUNCTIONS CALLED BY NONLINEAR ELASTICITY PROPERTY          //
///////////////////////////////////////////////////////////////////////


// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor.

void %CLASS%::nonlin_stress(
			   double x, double y, double z,
			   double time, DoubleVec &displacement,
			   SmallMatrix &displacement_gradient,
			   SmallMatrix &stress) const
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR STRESS FUNCTIONS

  double exponent = parameter1; // exponent is a parameter input by the user
  double coefficient = parameter2; // nonlinear coefficient is by the user

  stress(0,0) = displacement_gradient(0,0)
                 + coefficient * pow( displacement_gradient(0,0), exponent );
  stress(0,1) = displacement_gradient(0,1) + displacement_gradient(1,0);
  stress(0,2) = 0.0;

  stress(1,0) = displacement_gradient(0,1) + displacement_gradient(1,0);
  stress(1,1) = displacement_gradient(1,1)
                 + coefficient * pow( displacement_gradient(1,1), exponent );
  stress(1,2) = 0.0;

  stress(2,0) = 0.0;
  stress(2,1) = 0.0;
  stress(2,2) = 0.0;

  // ========  END OF CHANGES =============================================

} // end of '%CLASS%::nonlinear_stress'


//////////////////////////////////////////////////////////////////////////

// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor derivative with respect to the displacement.

void %CLASS%::nonlin_stress_deriv_wrt_displacement(
                                         double x, double y, double z,
					 double time, DoubleVec &displacement,
					 SmallMatrix &displacement_gradient,
					 SmallTensor3 &stress_deriv) const
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR STRESS DERIVATIVES

  for (int i = 0; i < 3; i++) {
    stress_deriv(i,0,0) = stress_deriv(i,0,1) = stress_deriv(i,0,2) = 0.0;
    stress_deriv(i,1,0) = stress_deriv(i,1,1) = stress_deriv(i,1,2) = 0.0;
    stress_deriv(i,2,0) = stress_deriv(i,2,1) = stress_deriv(i,2,2) = 0.0;
  }

  // ========  END OF CHANGES =============================================

} // end of '%CLASS%::nonlinear_stress_deriv_wrt_displacement'


//////////////////////////////////////////////////////////////////////////

// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor derivative with respect to the displacement.

void %CLASS%::nonlin_stress_deriv_wrt_displacement_gradient(
                                         double x, double y, double z,
					 double time, DoubleVec &displacement,
					 SmallMatrix &displacement_gradient,
					 SmallTensor4 &stress_deriv) const
{
  // ========  CHANGE THESE LINES FOR OTHER NONLINEAR STRESS DERIVATIVES

  double exponent = parameter1;
  double coefficient = parameter2;

  for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++) {
      stress_deriv(i,j,0,0) = stress_deriv(i,j,0,1) = stress_deriv(i,j,0,2) = 0.0;
      stress_deriv(i,j,1,0) = stress_deriv(i,j,1,1) = stress_deriv(i,j,1,2) = 0.0;
      stress_deriv(i,j,2,0) = stress_deriv(i,j,2,1) = stress_deriv(i,j,2,2) = 0.0;
    }

  stress_deriv(0,0,0,0) = 1.0 + coefficient * exponent
                                   * pow( displacement_gradient(0,0), exponent-1.0 );
  stress_deriv(0,1,0,1) = 1.0;
  stress_deriv(0,1,1,0) = 1.0;
  stress_deriv(1,1,1,1) = 1.0 + coefficient * exponent
                                   * pow( displacement_gradient(1,1), exponent-1.0 );
  stress_deriv(1,0,0,1) = 1.0;
  stress_deriv(1,0,1,0) = 1.0;

  // ========  END OF CHANGES ==============================================

} // end of '%CLASS%::nonlinear_stress_deriv_wrt_displacement_gradient'
