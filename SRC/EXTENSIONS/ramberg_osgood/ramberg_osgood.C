// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

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

int CRambergOsgood::invert(SmallMatrix &displacement_gradient,
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

void CRambergOsgood::nonlin_stress(
                                     double x, double y, double z,
				     double time,
				     DoubleVec &displacement,
				     SmallMatrix &displacement_gradient,
				     SmallMatrix &stress) const
{
  SmallTensor4 stress_div;
  int res = this->invert(displacement_gradient, stress, stress_div);

  // Fills in the "stress" object.

} // end of 'CRambergOsgood::nonlinear_stress'


// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor derivative with respect to the displacement.

void CRambergOsgood::nonlin_stress_deriv_wrt_displacement(
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

} // end of 'CRambergOsgood::nonlinear_stress_deriv_wrt_displacement'


// The following function takes the spatial coordinate x,y,z, the time,
// the displacement, and the displacement gradient and returns the
// corresponding stress tensor derivative with respect to the displacement.
void CRambergOsgood::nonlin_stress_deriv_wrt_displacement_gradient(
                                         double x, double y, double z,
					 double time,
					 DoubleVec &displacement,
					 SmallMatrix &displacement_gradient,
		  			 SmallTensor4 &stress_deriv) const
{
  SmallTensor4 dsde;
  SmallMatrix stress(3);

  // std::cerr << "CRambergOsgood::nonlin_stress_deriv" << std::endl;

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

} // end of 'CRambergOsgood::nonlinear_stress_deriv_wrt_displacement_gradient'
