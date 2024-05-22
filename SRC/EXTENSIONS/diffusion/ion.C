// -*- C++ -*-

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
#include "EXTENSIONS/diffusion/ion.h"
#include "engine/fieldindex.h"
#include "engine/material.h"
#include "engine/properties/orientation/orientation.h"
#include "engine/smallsystem.h"
#include "engine/nodalequation.h"
#include "engine/outputval.h"
#include <iostream>
#include <fstream>
#include <string>


IonDiffusion::IonDiffusion(PyObject *reg, const std::string &nm, double z)
  : FluxProperty(nm,reg)
{
  concentration = dynamic_cast<ScalarField*>(Field::getField("Concentration"));
  voltage = dynamic_cast<ScalarField*>(Field::getField("Voltage"));
  charge_flux = dynamic_cast<VectorFlux*>(Flux::getFlux("Charge_Flux"));
  atom_flux = dynamic_cast<VectorFlux*>(Flux::getFlux("Atom_Flux"));
  z_ = z;
}


int IonDiffusion::integration_order(const CSubProblem *subp,
				    const Element *el) const
{
  // Use the concentration field as the main source -- it appears in
  // both terms, whereas the voltage only appears in the
  // atom-flux-contributing term. 
  if(concentration->in_plane(subp))
    return el->dshapefun_degree();
  return el->shapefun_degree();
}


void IonDiffusion::cross_reference(Material *mat) {
  diffusion = dynamic_cast<Diffusion*>(mat->fetchProperty("Diffusion"));
}

void IonDiffusion::static_flux_value(const FEMesh  *mesh,
				     const Element *element,
				     const Flux    *flux,
				     const MasterPosition &pt,
				     double time,
				     SmallSystem *fluxdata) const
{
  // Find the concentration value at this point.
  double c = concentration->value(mesh, element, pt);

  const SymmMatrix3 cndct( diffusion->conductivitytensor( mesh, element, pt));

  std::vector<double> fieldGradient(3);
  
  if (*flux == *charge_flux ) {
    // For charge flux, the relevant gradient is the concentration.
    for (SpaceIndex i=0; i<DIM; ++i) {
      fieldGradient[i] = concentration->gradient(mesh, element, pt, i);
    }
    if (!concentration->in_plane(mesh) ) {
      fieldGradient[2] = concentration->out_of_plane()->value(
				      mesh, element, pt, ScalarFieldIndex());
    }
    for(IndexP i : *flux->components(ALL_INDICES)) {
      fluxdata->flux_vector_element(i) -= \
	z_*c*(cndct(i.integer(),0)*fieldGradient[0]+
	     cndct(i.integer(),1)*fieldGradient[1]+
	     cndct(i.integer(),2)*fieldGradient[2]);
    }
  }
  else if (*flux == *atom_flux ) {
    // For atom flux, the dependent field gradient is the voltage.
    for (SpaceIndex i=0; i<DIM; ++i) {
      fieldGradient[i] = voltage->gradient(mesh, element, pt, i);
    }
    if (!voltage->in_plane(mesh) ) {
      fieldGradient[2] = voltage->out_of_plane()->value(mesh, element, pt,
							ScalarFieldIndex());
    }
    for(IndexP i : *flux->components(ALL_INDICES)) {
      fluxdata->flux_vector_element(i) -=		\
	z_*c*(cndct(i.integer(),0)*fieldGradient[0]+
	     cndct(i.integer(),1)*fieldGradient[1]+
	     cndct(i.integer(),2)*fieldGradient[2]);
    }
  }
  else 
    throw ErrProgrammingError("Unexpected flux", __FILE__,__LINE__);


} // end of 'IonDiffusion::static_flux_value'

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void IonDiffusion::flux_matrix(const FEMesh  *mesh,
			       const Element *el,
			       const ElementFuncNodeIterator &j,
			       const Flux    *flux,
			       const MasterPosition &pt,
			       double time,
			       SmallSystem *fluxdata)
  const
{
  // The charge flux matrix M_{ij} multiplies the vector of nodal
  // field values (concentration and voltage) to give the vector
  // charge current J at point pt.  M_{ij} = -K_{ik} grad_k N_j J_i =
  // -M_{ij} T_j where N_j is the shapefunction at node j.
  // printf("flux");

  // fluxdata->stiffness_matrix_element( flux-comp, field, field-comp)

  double sf   = j.shapefunction( pt );
  double dsf0 = j.dshapefunction( 0, pt );
  double dsf1 = j.dshapefunction( 1, pt );

  // Same preliminaries as the flux-value case, find concentration
  // field value and conductivity tensor.
  double c = concentration->value(mesh, el, pt);
  const SymmMatrix3 cndct(diffusion->conductivitytensor( mesh, el, pt));
  std::vector<double> fieldGradient(3);

  if (*flux==*charge_flux) {

    // Still need to collect values of the concentration gradient.
    for (SpaceIndex i=0; i<DIM; ++i) {
      fieldGradient[i] = concentration->gradient(mesh, el, pt, i);
    }
    if (!concentration->in_plane(mesh) ) {
      fieldGradient[2] = concentration->out_of_plane()->value(
			      mesh, el, pt, ScalarFieldIndex());
    }

    // Now we have all the field data and shape functions, build the
    // matrix elements.
    for(IndexP i : *flux->components(ALL_INDICES)) {

      // First term, derivatives wrt field gradient.
      double t1 = z_*c*cndct(i.integer(),0)*dsf0 + 
	z_*c*cndct(i.integer(),1)*dsf1;

      
      // In 2D case with out-of-plane field, there's another piece.
      if(!concentration->in_plane(mesh)) {
	t1 += z_*c*cndct(i.integer(),2)*sf;
      }

      // Second term, derivative wrt concentration field.
      double t2 = z_*(cndct(i.integer(),0)*fieldGradient[0]+
		     cndct(i.integer(),1)*fieldGradient[1]+
		     cndct(i.integer(),2)*fieldGradient[2])*sf;

      fluxdata->stiffness_matrix_element( i, concentration, j) += t1;
      fluxdata->stiffness_matrix_element( i, concentration, j) += t2;
      
    }
  }
  else if (*flux==*atom_flux) {
    
    // For the atom_flux case, need the voltage derivatives.
    for (SpaceIndex i=0; i<DIM; ++i) {
      fieldGradient[i] = voltage->gradient(mesh, el, pt, i);
    }
    if (!voltage->in_plane(mesh) ) {
      fieldGradient[2] = voltage->out_of_plane()->value(mesh, el, pt,
							ScalarFieldIndex());
    }

    // Now (again) we have all the field data and shape functions,
    // build the matrix elements.
    for(IndexP i : *flux->components(ALL_INDICES)) {

      // First term, derivatives wrt field gradient.
      double t1 = z_*c*cndct(i.integer(),0)*dsf0 + 
	z_*c*cndct(i.integer(),1)*dsf1;

      
      // In 2D case with out-of-plane field, there's another piece.
      if(!voltage->in_plane(mesh)) {
	t1 += z_*c*cndct(i.integer(),2)*sf;
      }

      // Second term, derivative wrt concentration field.
      double t2 = z_*(cndct(i.integer(),0)*fieldGradient[0]+
		     cndct(i.integer(),1)*fieldGradient[1]+
		     cndct(i.integer(),2)*fieldGradient[2])*sf;

      fluxdata->stiffness_matrix_element( i, voltage, j) += t1;
      fluxdata->stiffness_matrix_element( i, concentration, j) += t2;
      
    }
  }
  else 
    throw ErrProgrammingError("Unexpected flux", __FILE__,__LINE__);

} // end of 'IonDiffusion::flux_matrix'


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

