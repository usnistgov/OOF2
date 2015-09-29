// -*- C++ -*-
// $RCSfile: charge.C,v $
// $Revision: 1.1 $
// $Author: reida $
// $Date: 2012/03/26 19:29:02 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// atom conductivity
#include <stdio.h>
#include <oofconfig.h>
#include "common/coord.h"
#include "common/tostring.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "EXTENSIONS/diffusion/charge.h"
#include "engine/fieldindex.h"
#include "engine/material.h"
#include "engine/property/orientation/orientation.h"
#include "engine/smallsystem.h"
#include "engine/nodalequation.h"
#include "engine/outputval.h"
#include <iostream>
#include <fstream>
#include <string>

Current::Current(PyObject *reg, const std::string &nm)
  : FluxProperty(nm,reg)
{
  voltage = dynamic_cast<ScalarField*>(Field::getField("Voltage"));
  charge_flux = dynamic_cast<VectorFlux*>(Flux::getFlux("Charge_Flux"));
}


int Current::integration_order(const CSubProblem *subp,
			       const Element *el) const
{
#if DIM==2
  if(voltage->in_plane(subp))
    return el->dshapefun_degree();
#endif
  return el->shapefun_degree();
}



void Current::static_flux_value(const FEMesh  *mesh,
				const Element *element,
				const Flux    *flux,
				const MasterPosition &pt,
				double time,
				SmallSystem *fluxdata) const
{
  // first evaluate the voltage gradient

  std::vector<double> fieldGradient(3);

  for (SpaceIndex i=0; i<DIM; ++i){
    OutputValue outputVal = element->outputFieldDeriv( mesh, *voltage, &i, pt );
    fieldGradient[i] = outputVal[0];
  }

#if DIM==2  // if plane-flux eqn, then dT/dz is kept as a separate out_of_plane field
  if ( !voltage->in_plane(mesh) ){
    OutputValue outputVal = element->outputField( mesh, *voltage->out_of_plane(), pt );
    fieldGradient[2] = outputVal[0];
  }
#endif

  // now compute the flux elements by the following summation
  //    flux_i = cond(i,j) * dT_j
  // where 'cond' is the conductivity tensor and dT_j is
  // jth component of the gradient of the voltage field

  const SymmMatrix3 cond( conductivitytensor( mesh, element, pt ) );

  for(VectorFieldIterator i; !i.end(); ++i)
    fluxdata->flux_vector_element( i ) -= cond( i.integer(), 0 ) * fieldGradient[0] +
                                          cond( i.integer(), 1 ) * fieldGradient[1] +
                                          cond( i.integer(), 2 ) * fieldGradient[2];

} // end of 'Current::static_flux_value'

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Current::flux_matrix(const FEMesh  *mesh,
			  const Element *el,
			  const ElementFuncNodeIterator &j,
			  const Flux    *flux,
			  const MasterPosition &pt,
			  double time,
			  SmallSystem *fluxdata)
  const
{
  // The charge flux matrix M_{ij} multiplies the vector of nodal
  // voltages to give the vector charge current J at point pt.
  // M_{ij} = -K_{ik} grad_k N_j
  // J_i = -M_{ij} T_j
  // where N_j is the shapefunction at node j.
  // printf("flux");
  if (*flux != *charge_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  double sf   = j.shapefunction( pt );
  double dsf0 = j.dshapefunction( 0, pt );
  double dsf1 = j.dshapefunction( 1, pt );
#if DIM==3
  double dsf2 = j.dshapefunction( 2, pt );
#endif

  const SymmMatrix3 cond( conductivitytensor( mesh, el, pt ) );

  // Loop over flux components.  Loop over all components, even if
  // the flux is in-plane, because the out-of-plane components of
  // the flux matrix are used to construct the constraint equation.

  for(VectorFieldIterator i; !i.end(); ++i){
#if DIM==2
    // in-plane voltage gradient contributions
    fluxdata->stiffness_matrix_element( i, voltage, j ) -=
                  cond(i.integer(), 0) * dsf0 + cond(i.integer(), 1) * dsf1;

    // out-of-plane voltage gradient contribution
    if(!voltage->in_plane(mesh))
      fluxdata->stiffness_matrix_element(i, voltage->out_of_plane(), j)
                                          -= cond(i.integer(), 2) * sf;

#elif DIM==3
    fluxdata->stiffness_matrix_element( i, voltage, j ) -=
                              cond( i.integer(), 0 ) * dsf0 +
                              cond( i.integer(), 1 ) * dsf1 +
                              cond( i.integer(), 2 ) * dsf2;
#endif

  }
} // end of 'Charge::flux_matrix'


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

IsoCurrent::IsoCurrent(PyObject *reg,
		       const std::string &nm,
		       double kppa)
  : Current(reg, nm),
    K_(kppa)
{
}

void IsoCurrent::precompute(FEMesh *mesh) {
  Current::precompute(mesh);
  conductivitytensor_(0,0) = conductivitytensor_(1,1)
    = conductivitytensor_(2,2) = K_;
}

const SymmMatrix3
IsoCurrent::conductivitytensor(const FEMesh*,
					const Element*,
					const MasterPosition&)
  const
{
  return conductivitytensor_;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

AnisoCurrent::AnisoCurrent(PyObject *reg,
			   const std::string &nm,
			   SymmMatrix3 *k)
  : Current(reg,nm),
    K_(*k),
    orientation(0)
{}

void AnisoCurrent::cross_reference(Material *mat) {
  orientation =
    dynamic_cast<OrientationPropBase*>(mat->fetchProperty("Orientation"));
}

void AnisoCurrent::precompute(FEMesh *mesh) {
  Current::precompute(mesh);
  if(orientation && orientation->constant_in_space())
    conductivitytensor_ = K_.transform(orientation->orientation());
}

const SymmMatrix3
AnisoCurrent::conductivitytensor(const FEMesh *mesh,
				 const Element *el,
				 const MasterPosition &mpos)
  const
{
  if(orientation->constant_in_space())
    return conductivitytensor_;
  return K_.transform(orientation->orientation(mesh, el, mpos));
}

