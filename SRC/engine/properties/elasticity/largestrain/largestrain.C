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
#include "common/doublevec.h"
#include "common/smallmatrix.h"
#include "engine/cstrain.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/ooferror.h"
#include "engine/properties/elasticity/largestrain/largestrain.h"
#include "engine/properties/orientation/orientation.h"
#include "engine/smallsystem.h"
#include "engine/symmmatrix.h"

// TODO 2.1?  When using large strains, the Jacobian calculated in
// Element::jacobian should use Node::displaced_position, not
// Node::position.  This should be done for *all* Jacobian
// calculations if there are large strains, even if displacement isn't
// an active field or if LargeStrainElasticity isn't being used.  If
// displacement is active, the Jacobian for Newton's method needs to
// include a term for the derivative of the metric in the element
// integrals.  Using the displaced_position in Element::jacobian will
// also rotate Neumann boundary conditions correctly when they're
// specified in tangent/normal coordinates, but the integrals of those
// conditions over the boundary will lead to extra terms linear in the
// displacement, which will have to be included in the LHS when
// solving large strain elasticity problems.

CLargeStrainElasticity::CLargeStrainElasticity(const std::string &nm,
					       PyObject *registration)
  : Elasticity(nm, registration)
{}

bool CLargeStrainElasticity::is_symmetric_K(const CSubProblem*) const {
  return false;
}

// The function 'contract_C_dU_dF' the following sum necessary for
// the flux_matrix computation in geometric nonlinear elasticity:
//
//     \Sum_{m,n} C(i,j,m,n) dU(k)/dx(m) dF/dx(n),   i,j,k given
//
// where C is the elasticity modulus,
//       dU(k)/dx(m) is the deriv of mth component of displacement w.r.t. x(m) (x,y,z),
//       dF/dx(n) is the derivative of the shape function F w.r.t. x(n).
//
// The summation is over m,n=0,1 in 2D and m,n=0,1,2 in 3D.
// To save in the overhead of accessing C(i,j,m,n), we use the corresponding
// Voigt indices, i.e. (0,0) (0,1) (0,2)      0 5 4
//                     (1,0) (1,1) (1,2)  =>  5 1 3
//                     (2,0) (2,1) (2,2)      4 3 2

inline double contract_C_dU_dF(const Cijkl &C, 
			       const SmallMatrix &dU, 
			       const DoubleVec &dF,
			       int ij, int k, bool inplane)
{
  if ( inplane )
    return ( dU(k,0) * ( C(ij,0)*dF[0] + C(ij,5)*dF[1] ) +
	     dU(k,1) * ( C(ij,5)*dF[0] + C(ij,1)*dF[1] ) );
  else
    return ( dU(k,0) * ( C(ij,0)*dF[0] + C(ij,5)*dF[1] ) +
	     dU(k,1) * ( C(ij,5)*dF[0] + C(ij,1)*dF[1] ) +
	     dU(k,2) * ( C(ij,4)*dF[0] + C(ij,3)*dF[1] ) );

} // end of 'contract_C_dU_dF'


// The flux matrix for geometric nonlinear elasticity is
//
//  \Sum_l  C(i,j,k,l) dF/dx(l) + \Sum_{m,n} C(i,j,m,n) dU(k)/dx(m) dF/dx(n)
//
// where C is the elasticity modulus,
//       dU(k)/dx(m) is the deriv of mth component of displacement
//            w.r.t. x(m) (x,y,z),
//       dF/dx(n) is the derivative of the shape function F w.r.t. x(n).

void CLargeStrainElasticity::flux_matrix(const FEMesh  *mesh,
					 const Element *element,
					 const ElementFuncNodeIterator &node,
					 const Flux    *flux,
					 const MasterPosition &pt,
					 double time,
					 SmallSystem *fluxmtx) const
{
  int (*ij2voigt)(int,int) = &SymTensorIndex::ij2voigt; // shorter func name
  SmallMatrix dU(3);	// gradient of displacement
  double Fval;		// the value of the shape function (for node)
  DoubleVec dF(3);	// and its derivative at the given pt
  bool inplane = false;	// needed both in 2D & 3D versions regardless,
			// passed to contract_C_dU_dF

  // in 2D, check if it is an in-plane eqn or a plane-flux eqn.
  static CompoundField *displacement =
    dynamic_cast<CompoundField*>(Field::getField("Displacement"));
  inplane = displacement->in_plane( mesh );

  // check for unexpected flux, flux should be a stress flux
  if (*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  // evaluate the shape function and its gradient (of node) at the given pt
  Fval  = node.shapefunction( pt );     // value of the shape function
  dF[0] = node.dshapefunction( 0, pt ); // x-deriv of the shape function
  dF[1] = node.dshapefunction( 1, pt ); // y-deriv of the shape function

  computeDisplacementGradient( mesh, element, pt, dU );

  const Cijkl CC = cijkl( mesh, element, pt ); // elasticity modulus

  // add the flux contributions to stiffness matrix element

  for (SymTensorIndex ij_iter : symTensorIJComponents) {
    int k0, k1, k2, ij = ij_iter.integer();
    double nonlinear_part; // to store the sum from the nonlinear terms

    // TODO: Use tensor iterators for k0, k1, k2.

    // sum CC(i,j,k,l)*dF(l),  k=0   over l=0,1, then add to stiffness_mtx
    k0 = ij2voigt( 0,0 );
    k1 = ij2voigt( 0,1 );
    nonlinear_part = contract_C_dU_dF(CC, dU, dF, ij, 0, inplane ); // at ij, k=0
    fluxmtx->stiffness_matrix_element( ij_iter, displacement,
				       VectorFieldIndex(0), node )
      -= CC( ij,k0 ) * dF[0] + CC( ij,k1 ) * dF[1]
      + nonlinear_part;


    // sum CC(i,j,k,l)*dF(l),  k=1   over l=0,1, then add to stiffness_mtx
    k0 = ij2voigt( 1,0 );
    k1 = ij2voigt( 1,1 );
    nonlinear_part = contract_C_dU_dF( CC, dU, dF, ij, 1, inplane ); // at ij, k=1
    fluxmtx->stiffness_matrix_element( ij_iter, displacement,
				       VectorFieldIndex(1), node )
      -= CC( ij,k0 ) * dF[0] + CC( ij,k1 ) * dF[1]
      + nonlinear_part;


    if ( !inplane ) // now contributions from z-deriv of displacement field
    {
      Field *disp_z_deriv = displacement->out_of_plane();
      for(IndexP k_iter : *disp_z_deriv->components(ALL_INDICES)) {
	double diag_factor = ( k_iter.integer()==2 ? 1.0 : 0.5 );

	k2 = ij2voigt( 2, k_iter.integer() );

	fluxmtx->stiffness_matrix_element( ij_iter, disp_z_deriv, k_iter, node )
 	             -= diag_factor * Fval * CC( ij,k2 );
      }
    } // end of 'if (!inplane)'
  } // end of loop over ij

} // end of 'CLargeStrainElasticity::flux_matrix'

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void CLargeStrainElasticity::geometricStrain(const FEMesh *mesh,
					     const Element *element,
					     const MasterPosition &pos,
					     SymmMatrix3 *strain)
  const
{
  findGeometricStrain(mesh, element, pos, strain, true);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CIsoLargeStrainElasticity::CIsoLargeStrainElasticity(const std::string &name,
						     PyObject *registration,
						     PyObject *self,
						     const Cijkl &c)
  : PythonNative<Property>(self),
    CLargeStrainElasticity(name, registration),
    c_ijkl(c)
{}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CAnisoLargeStrainElasticity::CAnisoLargeStrainElasticity(const std::string &nm,
							 PyObject *registration,
							 PyObject *self,
							 const Cijkl &c)
  : PythonNative<Property>(self),
    CLargeStrainElasticity(nm, registration),
    orientation(0),
    crystal_cijkl_(c)
{}


// TODO: These functions are identical to their counterparts in
// CAnisoElasticity.  We could probably use multiple inheritance to
// remove the redundancy.

void CAnisoLargeStrainElasticity::cross_reference(Material *mat) {
  try {
    orientation = 
      dynamic_cast<OrientationPropBase*>(mat->fetchProperty("Orientation"));
  }
  catch (ErrNoSuchProperty&) {
    orientation = 0;
    throw;
  }
}

void CAnisoLargeStrainElasticity::precompute(FEMesh *mesh) {
  Elasticity::precompute(mesh);
  if(orientation && orientation->constant_in_space())
    lab_cijkl = crystal_cijkl().transform(orientation->orientation());
}

const Cijkl CAnisoLargeStrainElasticity::cijkl(const FEMesh *mesh,
					       const Element *el,
					       const MasterPosition &mpos)
  const
{
  if(orientation->constant_in_space())
    return lab_cijkl;
  return crystal_cijkl().transform(orientation->orientation(mesh, el, mpos));
}

const Cijkl &CAnisoLargeStrainElasticity::crystal_cijkl() const {
  return crystal_cijkl_;
}
