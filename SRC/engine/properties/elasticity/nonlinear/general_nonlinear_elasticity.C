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
#include "common/coord.h"
#include "common/doublevec.h"
#include "common/ooferror.h"
#include "common/smallmatrix.h"
#include "common/threadstate.h"
#include "common/trace.h"
#include "engine/IO/propertyoutput.h"
#include "engine/cnonlinearsolver.h"
#include "engine/cstrain.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/ooferror.h"
#include "engine/smallsystem.h"
#include "engine/smalltensor.h"
#include "general_nonlinear_elasticity.h"


GeneralNonlinearElasticityNoDeriv::GeneralNonlinearElasticityNoDeriv(
				     const std::string &nm,
				     PyObject *registration)
  : FluxProperty(nm, registration)
{
  displacement = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
  stress_flux = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}


int GeneralNonlinearElasticityNoDeriv::integration_order(
						 const CSubProblem *subp,
						 const Element *el) const
{
  if(displacement->in_plane(subp))
    return el->dshapefun_degree();
  return el->shapefun_degree();
}


void GeneralNonlinearElasticityNoDeriv::flux_value(const FEMesh  *mesh,
						   const Element *element,
						   const Flux *flux,
						   const MasterPosition &pt,
						   double time, void*, 
						   SmallSystem *fluxdata)
  const
{
  // first compute the displacement and its gradient at the given point
  DoubleVec dispVec(findDisplacement(mesh, element, pt));
  SmallMatrix dispGrad(findDisplacementGradient(mesh, element, pt));

  // compute the value of stress with the user-defined function
  Coord coord = element->from_master(pt);
  SmallMatrix stress = nonlin_stress(coord, time, dispVec, dispGrad);

  // now we can plug in the flux element values to fluxdata
  // TODO? Replace with
  //       fluxdata->fluxVector() -= stress;
  for(SymTensorIndex ij : symTensorIJComponents)
    fluxdata->flux_vector_element(ij) += stress(ij.row(), ij.col());

} // GeneralNonlinearElasticityNoDeriv::flux_value


void GeneralNonlinearElasticity::flux_matrix(
				     const FEMesh *mesh,
				     const Element *element,
				     const ElementFuncNodeIterator &node,
				     const Flux *flux,
				     const MasterPosition &pt,
				     double time, void*, 
				     SmallSystem *fluxmtx)
  const
{
  // check for unexpected flux, should be stress flux
  if (*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  // first compute the displacement and its gradient at the given point
  DoubleVec dispVec(findDisplacement(mesh, element, pt));
  SmallMatrix dispGrad(findDisplacementGradient(mesh, element, pt));

  // evaluate the value of flux derivatives with the given pt, time,
  // displacement etc
  Coord coord = element->from_master(pt);
  // the derivative of the stress flux mapping w.r.t. displacement field
  SmallTensor3 stressDeriv1 = nonlin_stress_deriv_wrt_displacement(
					   coord, time, dispVec, dispGrad);
  // the derivative of the stress flux mapping w.r.t. displacement gradient
  SmallTensor4 stressDeriv2 =  nonlin_stress_deriv_wrt_displacement_gradient(
					   coord, time, dispVec, dispGrad);

  // evaluate the shape function and its gradient at the given node j
  double shapeFuncVal   = node.shapefunction(pt);
  double shapeFuncGrad0 = node.dshapefunction(0, pt);
  double shapeFuncGrad1 = node.dshapefunction(1, pt);

  // finally add the contributions to the stiffness matrix element
  for (SymTensorIndex ij : symTensorIJComponents) {
    int i = ij.row();
    int j = ij.col();

    for(IndexP k : *displacement->components(ALL_INDICES)) {
      fluxmtx->stiffness_matrix_element(ij, displacement, k, node) +=
	stressDeriv1(i,j,k) * shapeFuncVal +
	stressDeriv2(i,j,k,0) * shapeFuncGrad0 +
	stressDeriv2(i,j,k,1) * shapeFuncGrad1;
    } // End of kay loop.

    if (!displacement->in_plane(mesh)) {
      Field *disp_z_deriv = displacement->out_of_plane();
      for(IndexP ko : *disp_z_deriv->components(ALL_INDICES)) {
	fluxmtx->stiffness_matrix_element(ij, disp_z_deriv, ko, node) +=
	  stressDeriv2(i,j,ko,2) * shapeFuncVal;
      }
    }

  } // end of loop over ij

} // end of 'GeneralNonlinearElasticity::flux_matrix'


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


inline double SQR(double x) { return x*x; }
inline double CUBE(double x) { return x*x*x; }


SmallMatrix nonlin_stress_1(const Coord &pt, double time,
			    const DoubleVec &displacement,
			    const SmallMatrix &dispGrad)
{
  SmallMatrix stress(3);
  stress(0,0) = dispGrad(0,0) + CUBE(dispGrad(0,0));
  stress(0,1) = dispGrad(0,1) + dispGrad(1,0);
  stress(0,2) = 0.0;

  stress(1,0) = dispGrad(0,1) + dispGrad(1,0);
  stress(1,1) = dispGrad(1,1) + CUBE(dispGrad(1,1));
  stress(1,2) = 0.0;

  stress(2,0) = 0.0;
  stress(2,1) = 0.0;
  stress(2,2) = 0.0;

  return stress;
}


SmallTensor3 nonlin_stress_deriv_wrt_displacement_1(
				    const Coord &pt, double time,
				    const DoubleVec &displacement,
				    const SmallMatrix &dispGrad)
{
  return SmallTensor3();
}


SmallTensor4 nonlin_stress_deriv_wrt_displacement_gradient_1(
                                        const Coord &pt, double time,
					const DoubleVec &displacement,
					const SmallMatrix &dispGrad)
{
  SmallTensor4 stress_deriv;
  stress_deriv(0,0,0,0) = 1.0 + 3.0 * SQR(dispGrad(0,0));
  stress_deriv(0,1,0,1) = 1.0;
  stress_deriv(0,1,1,0) = 1.0;
  stress_deriv(1,1,1,1) = 1.0 + 3.0 * SQR(dispGrad(1,1));
  stress_deriv(1,0,0,1) = 1.0;
  stress_deriv(1,0,1,0) = 1.0;
  return stress_deriv;
}


SmallMatrix nonlin_stress_2(const Coord &pt, double time,
			    const DoubleVec &displacement,
			    const SmallMatrix &dispGrad)
{
  SmallMatrix stress(3);
  stress(0,0) = dispGrad(0,0) + CUBE(dispGrad(0,0)) +
                 (dispGrad(0,2) + dispGrad(2,0) + dispGrad(2,2))/20.0;
  stress(0,1) = dispGrad(0,1);
  stress(0,2) = dispGrad(0,0)/20.0 + atan(dispGrad(0,2) + dispGrad(2,0));

  stress(1,0) = dispGrad(1,0);
  stress(1,1) = dispGrad(1,1) + CUBE(dispGrad(1,1)) +
 	         (dispGrad(1,2) + dispGrad(2,1) + dispGrad(2,2))/20.0;
  stress(1,2) = dispGrad(1,1)/20.0 + atan(dispGrad(1,2) + dispGrad(2,1));

  stress(2,0) = dispGrad(0,0)/20.0 + atan(dispGrad(0,2) + dispGrad(2,0));
  stress(2,1) = dispGrad(1,1)/20.0 + atan(dispGrad(1,2) + dispGrad(2,1));
  stress(2,2) = (dispGrad(0,0) + dispGrad(1,1))/20.0 + atan(dispGrad(2,2));
  return stress;
}


SmallTensor3 nonlin_stress_deriv_wrt_displacement_2(
					    const Coord &pt, double time,
					    const DoubleVec &displacement,
					    const SmallMatrix &dispGrad)
{
  return SmallTensor3();
}


SmallTensor4 nonlin_stress_deriv_wrt_displacement_gradient_2(
                                        const Coord &pt, double time,
					const DoubleVec &u,
					const SmallMatrix &du)
{
  SmallTensor4 s;

  s(0,0,0,0) = 1.0 + 3.0 * SQR(du(0,0));
  s(1,1,1,1) = 1.0 + 3.0 * SQR(du(1,1));
  s(2,2,2,2) = 1.0 / (1.0 + SQR(du(2,2)));

  s(0,1,0,1) = s(1,0,1,0) = 1.0;

  s(0,2,0,2) = s(0,2,2,0) = s(2,0,0,2) = s(2,0,2,0)
                = 1.0 / (1.0 + SQR(du(0,2) + du(2,0)));

  s(1,2,1,2) = s(1,2,2,1) = s(2,1,1,2) = s(2,1,2,1)
                = 1.0 / (1.0 + SQR(du(1,2) + du(2,1)));

  s(0,0,0,2) = s(0,0,2,0) = s(0,0,2,2) = s(0,2,0,0)
             = s(1,1,1,2) = s(1,1,2,1) = s(1,1,2,2)
             = s(1,2,1,1) = s(2,0,0,0) = s(2,1,1,1)
             = s(2,2,0,0) = s(2,2,1,1) = 1.0/20.0;

  return s;
} 

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

SmallMatrix TestGeneralNonlinearElasticityNoDeriv::nonlin_stress(
                                        const Coord &pt, double time,
					const DoubleVec &displacement,
					const SmallMatrix &dispGrad)
  const
{
  switch (testNo) {
  case 1:
    return nonlin_stress_1(pt, time, displacement, dispGrad);
  case 2:
    return nonlin_stress_2(pt, time, displacement, dispGrad);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
}


SmallMatrix TestGeneralNonlinearElasticity::nonlin_stress(
                                        const Coord &pt, double time,
					const DoubleVec &displacement,
					const SmallMatrix &dispGrad)
  const
{
  switch (testNo) {
  case 1:
    return nonlin_stress_1(pt, time, displacement, dispGrad);
  case 2:
    return nonlin_stress_2(pt, time, displacement, dispGrad);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
} 


SmallTensor3
TestGeneralNonlinearElasticity::nonlin_stress_deriv_wrt_displacement(
                                        const Coord &pt, double time,
					const DoubleVec &displacement,
					const SmallMatrix &dispGrad)
  const
{
  switch (testNo) {
  case 1:
    return nonlin_stress_deriv_wrt_displacement_1(pt, time,
						  displacement, dispGrad);
  case 2:
    return nonlin_stress_deriv_wrt_displacement_2(pt, time,
						  displacement, dispGrad);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
} 


SmallTensor4
TestGeneralNonlinearElasticity::nonlin_stress_deriv_wrt_displacement_gradient(
                                        const Coord &pt, double time,
					const DoubleVec &displacement,
					const SmallMatrix &dispGrad)
  const
{
  switch (testNo) {
    case 1:
      return nonlin_stress_deriv_wrt_displacement_gradient_1(
						     pt, time,
						     displacement, dispGrad);
    case 2:
      return nonlin_stress_deriv_wrt_displacement_gradient_2(
						     pt, time,
						     displacement, dispGrad);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
}
