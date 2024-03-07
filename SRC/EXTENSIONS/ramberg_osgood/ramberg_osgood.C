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
// as a separate predefined property and need nt be defined using
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
//    displacement_gradient[0][0] = dU_0/dx
//    displacement_gradient[0][1] = dU_0/dy
//  ( displacement_gradient[0][2] = dU_0/dz  in 3D )
//
//    displacement_gradient[1][0] = dU_1/dx
//    displacement_gradient[1][1] = dU_1/dy
//  ( displacement_gradient[1][2] = dU_1/dz  in 3D )
//
//  ( displacement_gradient[2][0] = dU_2/dx  in 3D )
//  ( displacement_gradient[2][1] = dU_2/dy  in 3D )
//  ( displacement_gradient[2][2] = dU_2/dz  in 3D )
//
// The output argument stress contains the components of the stress
//
//    stress[0][0] = S_00(.,U,dU)
//    stress[0][1] = S_01(.,U,dU)
//  ( stress[0][2] = S_02(.,U,dU)  in 3D )
//
//    stress[1][0] = S_10(.,U,dU)
//    stress[1][1] = S_11(.,U,dU)
//  ( stress[1][2] = S_12(.,U,dU)  in 3D )
//
//  ( stress[2][0] = S_20(.,U,dU)  in 3D )
//  ( stress[2][1] = S_21(.,U,dU)  in 3D )
//  ( stress[2][2] = S_22(.,U,dU)  in 3D )
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
// The partial derivative of stress with respect to displacement
// is defined in the following function
//
//   void nonlin_stress_deriv_wrt_displacement(double x, double y, double z,
//					  double time, double displacement[3],
//					  double displacement_gradient[3][3],
//					  double stress_deriv[3][3][3])
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
// is defined in the following function
//
//   void nonlin_stress_deriv_wrt_displacement_gradient(double x, double y, double z,
//					     double time, double displacement[3],
//					     double displacement_gradient[3][3],
//					     double stress_deriv[3][3][3][3])
//
// The arguments x, y, z, time, displacement, displacement_gradient
// are input to the function and the corresponding stress derivative
// is returned in the output argument stress_deriv.
// The components of the derivative are stored in the four-dim array
// as follows:
//
//    stress_deriv[0][0][0][0] = dS_00 / dG_00    (recall G_kl = dU_k/dx_l)
//    stress_deriv[0][0][0][1] = dS_00 / dG_01
//  ( stress_deriv[0][0][0][2] = dS_00 / dG_02  in 3D)
//
//    stress_deriv[0][0][1][0] = dS_00 / dG_10
//    stress_deriv[0][0][1][1] = dS_00 / dG_11
//    stress_deriv[0][0][1][2] = dS_00 / dG_12  in 3D)
//
//  ( stress_deriv[0][0][2][0] = dS_00 / dG_20  in 3D)
//  ( stress_deriv[0][0][2][1] = dS_00 / dG_21  in 3D)
//  ( stress_deriv[0][0][2][2] = dS_00 / dG_22  in 3D)
//
//
//    stress_deriv[0][1][0][0] = dS_01 / dG_00
//                         :
//  ( stress_deriv[0][1][2][2] = dS_01 / dG_22  in 3D)
//
//
//    stress_deriv[0][2][0][0] = dS_02 / dG_00
//                         :
//  ( stress_deriv[0][2][2][2] = dS_02 / dG_22  in 3D)
//
//
//
//    stress_deriv[1][0][0][0] = dS_10 / dG_00
//                         :
//                         :
//                         :
//  ( stress_deriv[2][2][2][2] = dS_22 / dG_22  in 3D)



#include <oofconfig.h>
#include <math.h>
#include "ramberg_osgood.h"
#include "common/doublevec.h"
#include "common/smallmatrix.h"
#include "engine/smalltensor.h"


// some helper functions

inline double SQR(double x){ return x*x; }
inline double CUBE(double x){ return x*x*x; }


// Helper function.  Takes the displacement gradient, computes the
// strain, and returns the R-O stress corresponding to that strain,
// along with the matrix of derviatives of the stress with respect to
// the *strain*.

// TODO: This helper function is expensive, and needs to be called for
// each invocation of the stress and stress_deriv functions, which is
// probably twice per gausspoint.  It really should only be done once,
// but 2x isn't so bad.  Should we add hooks for this sort of thing,
// or would that clutter the interface?

#define TOLERANCE 1.0e-10 // Sum of squares of the 9-component residual.
#define MAX_ITERS 1000

static int mapping[3][3] = { { 0, 5, 4 }, { 8, 1, 3 }, { 7, 6, 2 }};

int RambergOsgood::invert(SmallMatrix &displacement_gradient,
			  SmallMatrix &s, SmallTensor4 &dsde) const {

  //  std::cerr << "Entering invert." << std::endl;

  double c11 = (this->cijkl)(0,0);
  double c12 = (this->cijkl)(0,1);

  double coefa = 1.0/(c11-c12);
  double coefb = c12/((c11-c12)*(c11+2.0*c12));

  double coefc = (this->alpha)*(3.0/2.0);

  SmallMatrix deds = SmallMatrix(9);
  SmallMatrix rhs = SmallMatrix(9,1);

  // Use STL vectors to get bounds-checking for free.
  std::vector<double> dxidsj = std::vector<double>(9);
  std::vector<double> strain_value = std::vector<double>(9);
  std::vector<double> strain_target = std::vector<double>(9);
  std::vector<double> stress_value = std::vector<double>(9);

  for(int i=0;i<3;++i) {
    for(int j=0;j<3;++j) {
      strain_target[mapping[i][j]] = 0.5*(displacement_gradient(i,j) +
					  displacement_gradient(j,i));
    }
  }

//   std::cerr << "Strain at input:" << std::endl;
//   for(int i=0;i<9;++i) {
//     std::cerr << strain_target[i] << " ";
//   }
//   std::cerr << std::endl;

  stress_value.clear();
  stress_value.resize(9,0.0);

  // TODO: Come up with a starting guess for the stress.  At the
  // moment, it's always starting from zero, which is rather wasteful
  // of cycles.

  int icount=0;
  int retcode=0;

//   std::cerr << "Entering the loop." << std::endl;
  do {
    double sqxis0,pn1_sqxis0,pn2_sqxi,trs,xi,resid;

    // Take the trace of the stress, it's a handy thing.
    trs = stress_value[0]+stress_value[1]+stress_value[2];

    // Compute xi from the current stress.
    xi = 0.0;
    double xi2=0.0;
    for(int i=0;i<9;++i)
      xi2 += SQR(stress_value[i]);
    xi = (3.0/2.0)*(xi2-(1.0/3.0)*SQR(trs));

    // Also these convenient quantities.
    sqxis0 = sqrt(xi)/this->s0;
    pn1_sqxis0 = pow(sqxis0,this->n-1.0);
    pn2_sqxi   = 0.5*pow(xi,(this->n-3.0)/2.0)/pow(s0,this->n-1.0);

    // And dxidsj.
    for(int j=0;j<9;++j) {
      dxidsj[j] = 3.0*stress_value[j];
      if (j<3) dxidsj[j] -= trs;
    }

    // std::cerr << "Computed convenience quantities." << std::endl;

    // Compute the actual R-O strain for this stress.
    for(int i=0;i<9;++i) {
      strain_value[i] = coefa*stress_value[i];
      if (i<3) strain_value[i] -= coefb*trs;
      double sig = stress_value[i];
      if (i<3) sig -= (1.0/3.0)*trs;
      strain_value[i] += coefc*pn1_sqxis0*sig;
    }

//     std::cerr << "Computed R-O strain." << std::endl;
//     for(int i=0;i<9;++i) {
//       std::cerr << strain_value[i] << " ";
//     }
//     std::cerr << std::endl;

    // Residual.
    resid = 0.0;
    for(int i=0;i<9;++i) {
      resid += SQR(strain_value[i]-strain_target[i]);
    }

    //    std::cerr << "Computed residual.  It's " << resid << std::endl;

    // Build the linear system.
    deds.clear();
    rhs.clear();
    for(int i=0;i<9;++i) {
      double sig = stress_value[i];
      if(i<3) sig -= (1.0/3.0)*trs;
      deds(i,i) += coefa + coefc*pn1_sqxis0;
      for(int j=0;j<9;++j) {
	if ((i<3)&&(j<3)) deds(i,j) -= coefb + (1.0/3.0)*coefc*pn1_sqxis0;
	deds(i,j) += coefc*pn2_sqxi*(this->n-1.0)*sig*dxidsj[j];
      }
      rhs(i,0) = strain_target[i]-strain_value[i];
    }

//     std::cerr << "Built linear system." << std::endl;

    // Check if we're done -- it's important to break out with the
    // matrix freshly built, since the solver mangles it.
    if (resid < TOLERANCE) break;

//     std::cerr << "DEDS:" << std::endl;
//     std::cerr << deds << std::endl;

    // Solve the linear system.
    icount++;
    retcode = deds.solve(rhs);

    if (retcode==0) {
      for(int i=0;i<9;++i)
	stress_value[i] += rhs(i,0);
    }
    else
      break;

//     std::cerr << "Solved linear system." << std::endl;

  } while (icount < MAX_ITERS);

  // std::cerr << "Broke out of the loop." << std::endl;
  // We're out.
  if ((icount==MAX_ITERS)||(retcode!=0)) {
//     std::cerr << "Bad retcode or iterations, failing." << std::endl;
//     std::cerr << "Retcode: " << retcode << std::endl;
//     std::cerr << "Iterations: " << icount << std::endl;
//     exit(-256);
    return -1;
  }

  // std::cerr << "Building the stress return value." << std::endl;
  // Build the stress return value.
  for(int i=0;i<3;++i) {
    for(int j=0;j<3;++j) {
      s(i,j)=stress_value[mapping[i][j]];
    }
  }

  // std::cerr << "Constructing inverse." << std::endl;
  SmallMatrix inverse = SmallMatrix(9);
  inverse.clear();
  for(int i=0;i<9;++i) inverse(i,i)=1.0;
  retcode = deds.solve(inverse);
  // std::cerr << "Solved for inverse, retcode is " << retcode << std::endl;
  if (retcode!=0) {
//     std::cerr << "Bad retcode, failing." << std::endl;
    return -2;
  }

  // The "inverse" matrix now contains dsde, but in the nine-index
  // form.  Convert to the full form.
  for(int i=0;i<3;++i)
    for(int j=0;j<3;++j)
      for(int k=0;k<3;++k)
	for(int l=0;l<3;++l)
	  dsde(i,j,k,l) = inverse(mapping[i][j],mapping[k][l]);

//   std::cerr << "Exiting successfully." << std::endl;
//   std::cerr << "Stress is: ";
//   for(int i=0;i<9;++i) {
//     std::cerr << stress_value[i] << " ";
//   }
//   std::cerr << std::endl;
  return 0; // Indicate success.
}

///////////////////////////////////////////////////////////////////////
//        FUNCTIONS CALLED BY NONLINEAR ELASTICITY PROPERTY          //
///////////////////////////////////////////////////////////////////////



// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor.

void RambergOsgood::nonlin_stress(
                                     double x, double y, double z,
				     double time,
				     DoubleVec &displacement,
				     SmallMatrix &displacement_gradient,
				     SmallMatrix &stress) const
{
  SmallTensor4 stress_div;
  int res = this->invert(displacement_gradient, stress, stress_div);

  // Fills in the "stress" object.

} // end of 'RambergOsgood::nonlinear_stress'


// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor derivative with respect to the displacement.

void RambergOsgood::nonlin_stress_deriv_wrt_displacement(
                                         double x, double y, double z,
					 double time,
					 DoubleVec &displacement,
					 SmallMatrix &displacement_gradient,
					 SmallTensor3 &stress_deriv) const
{
  for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
      for (int k = 0; k < 3; k++)
	stress_deriv(i,j,k) = 0.0;

} // end of 'RambergOsgood::nonlinear_stress_deriv_wrt_displacement'


// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor derivative with respect to the displacement.
void RambergOsgood::nonlin_stress_deriv_wrt_displacement_gradient(
                                         double x, double y, double z,
					 double time,
					 DoubleVec &displacement,
					 SmallMatrix &displacement_gradient,
		  			 SmallTensor4 &stress_deriv) const
{
  SmallTensor4 dsde;
  SmallMatrix stress(3);

  // std::cerr << "RambergOsgood::nonlin_stress_deriv" << std::endl;

  int res = this->invert(displacement_gradient, stress, dsde);

  // std::cerr << "Back from invert, retcode is " << res << std::endl;

  // Invert fills in dsde, but we want derivs wrt displacement
  // gradients.  Convert, even though they're probably the same.

  for(int i=0;i<3;++i) {
    for(int j=0;j<3;++j) {
      for(int k=0;k<3;++k) {
	for(int l=0;l<3;++l) {
	  stress_deriv(i,j,k,l) = 0.5*(dsde(i,j,k,l)+dsde(i,j,l,k));
	  // std::cerr << i << " " << j << " " << k << " " << l << " " << stress_deriv[i][j][k][l] << std::endl;

	}
      }
    }
  }

} // end of 'RambergOsgood::nonlinear_stress_deriv_wrt_displacement_gradient'
