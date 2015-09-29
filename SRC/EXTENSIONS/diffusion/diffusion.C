// -*- C++ -*-
// $RCSfile: diffusion.C,v $
// $Revision: 1.23 $
// $Author: reida $
// $Date: 2012/01/19 21:22:17 $

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
#include "EXTENSIONS/diffusion/diffusion.h"
#include "engine/fieldindex.h"
#include "engine/material.h"
#include "engine/property/orientation/orientation.h"
#include "engine/smallsystem.h"
#include "engine/nodalequation.h"
#include "engine/outputval.h"
#include <iostream>
#include <fstream>
#include <string>

Diffusion::Diffusion(PyObject *reg, const std::string &nm)
  : FluxProperty(nm,reg)
{
  concentration = dynamic_cast<ScalarField*>(Field::getField("Concentration"));
  atom_flux = dynamic_cast<VectorFlux*>(Flux::getFlux("Atom_Flux"));
}


Mobility::Mobility(PyObject *reg, const std::string &nm) 
  : EqnProperty(nm,reg) {
  concentration = dynamic_cast<ScalarField*>(Field::getField("Concentration"));
}


int Diffusion::integration_order(const CSubProblem *subp,
					    const Element *el) const
{
#if DIM==2
  if(concentration->in_plane(subp))
    return el->dshapefun_degree();
#endif
  return el->shapefun_degree();
}


int Mobility::integration_order(const CSubProblem *subp, 
				const Element *el) const {
  return el->shapefun_degree();
}


void Diffusion::static_flux_value(const FEMesh  *mesh,
					 const Element *element,
					 const Flux    *flux,
					 const MasterPosition &pt,
					 double time,
					 SmallSystem *fluxdata) const
{
  // first evaluate the concentration gradient

  std::vector<double> fieldGradient(3);

  for (SpaceIndex i=0; i<DIM; ++i){
    OutputValue outputVal = element->outputFieldDeriv( mesh, *concentration, &i, pt );
    fieldGradient[i] = outputVal[0];
  }

#if DIM==2  // if plane-flux eqn, then dT/dz is kept as a separate out_of_plane field
  if ( !concentration->in_plane(mesh) ){
    OutputValue outputVal = element->outputField( mesh, *concentration->out_of_plane(), pt );
    fieldGradient[2] = outputVal[0];
  }
#endif

  // now compute the flux elements by the following summation
  //    flux_i = cond(i,j) * dT_j
  // where 'cond' is the conductivity tensor and dT_j is
  // jth component of the gradient of the concentration field

  const SymmMatrix3 cond( conductivitytensor( mesh, element, pt ) );

  for(VectorFieldIterator i; !i.end(); ++i)
    fluxdata->flux_vector_element( i ) -= cond( i.integer(), 0 ) * fieldGradient[0] +
                                          cond( i.integer(), 1 ) * fieldGradient[1] +
                                          cond( i.integer(), 2 ) * fieldGradient[2];

} // end of 'Diffusion::static_flux_value'

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Diffusion::flux_matrix(const FEMesh  *mesh,
			    const Element *el,
			    const ElementFuncNodeIterator &j,
			    const Flux    *flux,
			    const MasterPosition &pt,
			    double time,
			    SmallSystem *fluxdata)
  const
{
  // The atom flux matrix M_{ij} multiplies the vector of nodal
  // concentrations to give the vector atom current J at point pt.
  // M_{ij} = -D_{ik} grad_k N_j
  // J_i = -M_{ij} T_j
  // where N_j is the shapefunction at node j.
  // printf("flux");
  if (*flux != *atom_flux) {
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
    // in-plane concentration gradient contributions
    fluxdata->stiffness_matrix_element( i, concentration, j ) -=
                  cond(i.integer(), 0) * dsf0 + cond(i.integer(), 1) * dsf1;

    // out-of-plane concentration gradient contribution
    if(!concentration->in_plane(mesh))
      fluxdata->stiffness_matrix_element(i, concentration->out_of_plane(), j)
                                          -= cond(i.integer(), 2) * sf;

#elif DIM==3
    fluxdata->stiffness_matrix_element( i, concentration, j ) -=
                              cond( i.integer(), 0 ) * dsf0 +
                              cond( i.integer(), 1 ) * dsf1 +
                              cond( i.integer(), 2 ) * dsf2;
#endif

  }
} // end of 'Diffusion::flux_matrix'

void Mobility::first_time_deriv_matrix(const FEMesh *mesh,
					const Element *lmnt,
					const Equation *eqn,
					const ElementFuncNodeIterator &eni,
					const MasterPosition &mpos,
					double time,
					SmallSystem *eqdata) const {

  double shapeFuncVal = eni.shapefunction( mpos );
  for(IteratorP eqncomp = eqn->iterator(); !eqncomp.end(); ++eqncomp) {
    // Kinetic coefficient is unity.
    eqdata->damping_matrix_element(eqncomp,concentration,eqncomp,eni) += \
      shapeFuncVal;
  }
}
					

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

IsoDiffusion::IsoDiffusion(PyObject *reg,
					 const std::string &nm,
					 double kppa)
  : Diffusion(reg, nm),
    D_(kppa)
{
}

void IsoDiffusion::precompute(FEMesh *mesh) {
  Diffusion::precompute(mesh);
  conductivitytensor_(0,0) = conductivitytensor_(1,1)
    = conductivitytensor_(2,2) = D_;
}

const SymmMatrix3
IsoDiffusion::conductivitytensor(const FEMesh*,
					const Element*,
					const MasterPosition&)
  const
{
  return conductivitytensor_;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

AnisoDiffusion::AnisoDiffusion(PyObject *reg,
					     const std::string &nm,
					     SymmMatrix3 *k)
  : Diffusion(reg,nm),
    D_(*k),
    orientation(0)
{}

void AnisoDiffusion::cross_reference(Material *mat) {
  orientation =
       dynamic_cast<OrientationPropBase*>(mat->fetchProperty("Orientation"));
}

void AnisoDiffusion::precompute(FEMesh *mesh) {
  Diffusion::precompute(mesh);
  if(orientation && orientation->constant_in_space())
    conductivitytensor_ = D_.transform(orientation->orientation());
}

const SymmMatrix3
AnisoDiffusion::conductivitytensor(const FEMesh *mesh,
					  const Element *el,
					  const MasterPosition &mpos)
  const
{
  if(orientation->constant_in_space())
    return conductivitytensor_;
  return D_.transform(orientation->orientation(mesh, el, mpos));
}



// Surface property -- stubbed for now.


AtomFluxJumpTest::AtomFluxJumpTest(PyObject *reg, const std::string &nm,
				 double coef) :
  EqnProperty(nm,reg),coef(coef) {}
// FluxProperty(nm,reg),coef(coef) {}


int AtomFluxJumpTest::integration_order(const CSubProblem* s,
				       const Element *el) const {
  return 0;
}

void AtomFluxJumpTest::begin_element(const CSubProblem *sp,
				    const Element *e) {
  std::cerr << "AtomFluxJumpTest::begin_element called." << std::endl;
  
  Coord increment, left_normal, right_normal;
  std::vector<const Node*> span;

  const InterfaceElement *ie = dynamic_cast<const InterfaceElement*>(e);
  
  span = ie->get_left_span();
  increment = span[1]->position()-span[0]->position();
  increment /= sqrt(norm2(increment));
  left_normal = Coord(-increment.y,increment.x);
  
  span = ie->get_right_span();
  increment = span[1]->position()-span[0]->position();
  increment /= sqrt(norm2(increment));
  right_normal = Coord(increment.y,-increment.x);

  e->setDataByName(new CoordElementData("left normal", left_normal));
  e->setDataByName(new CoordElementData("right normal", right_normal));

  std::cerr << "AtomFluxJumpTest: left normal :" << left_normal << std::endl;
  std::cerr << "AtomFluxJumpTest: right normal:" << right_normal << std::endl;
  
  std::cerr << "AtomFluxJumpTest: begin_element exiting." << std::endl;
}

void AtomFluxJumpTest::end_element(const CSubProblem *sp,
				  const Element *e) {
  std::cerr << "AtomFluxJumpTest::end_element called." << std::endl;

  // Delete the element-specific data.

  int ed = e->getIndexByName("left normal");
  ElementData *edp = e->getData(ed);
  e->delData(ed);
  delete edp;

  ed = e->getIndexByName("right normal");
  edp = e->getData(ed);
  e->delData(ed);
  delete edp;
}

void AtomFluxJumpTest::cross_reference(Material *m) {
  return;
}

void AtomFluxJumpTest::post_process(CSubProblem *sp,
				   const Element *e) const {}

// void AtomFluxJumpTest::flux_offset(const FEMesh *mesh,
// 				   const Element *element,
// 				   const Flux *flux,
// 				   const MasterPosition &pt,
// 				   double time,
// 				   SmallSystem *fluxdata) const {
//   std::cerr << "AtomFluxJumpTest::flux_offset called." << std::endl;
//   std::cerr << "Guasspoint is " << pt << std::endl;
//   const InterfaceElement *ie = dynamic_cast<const InterfaceElement*>(element);
//   if (ie->side()==LEFT) {
//     std::cerr << "Left-side case." << std::endl;
//     ElementData *ed = element->getDataByName("left normal");
//     const Coord &ln = dynamic_cast<CoordElementData*>(ed)->coord();
//     std::cerr << "Left normal is: " << ln << std::endl;
//     for(int i=0;i<DIM;++i) {
//       fluxdata->offset_vector_element(i) += ln(i);
//     }
//   }
//   else { 
//     std::cerr << "Right-side case." << std::endl;
//     ElementData *ed = element->getDataByName("right normal");
//     const Coord &rn = dynamic_cast<CoordElementData*>(ed)->coord();
//     std::cerr << "Right normal is: " << rn << std::endl;
//   }
// }

// void AtomFluxJumpTest::flux_matrix(const FEMesh *mesh,
// 				   const Element *element,
// 				   const ElementFuncNodeIterator &efi,
// 				   const Flux *flux,
// 				   const MasterPosition &pt,
// 				   double time,
// 				   SmallSystem *fluxdata) const {
  
//   // std::cerr << "AtomFluxJumpTest::flux_matrix called." << std::endl;

//   FuncNode *left,*right;

//   left = dynamic_cast<FuncNode*>(efi.leftnode());
//   right = dynamic_cast<FuncNode*>(efi.rightnode());


// }  




void AtomFluxJumpTest::force_deriv_matrix(const FEMesh* mesh,
					  const Element* element,
					  const Equation* eqn,
					  const ElementFuncNodeIterator &efi,
					  const MasterPosition& gpt,
					  double time, SmallSystem *eqndata) 
  const 
{
  std::cerr << "AtomFluxJumpTest::force_deriv_matrix called." << std::endl;
  
  FuncNode *left,*right;

  left = dynamic_cast<FuncNode*>(efi.leftnode());
  right = dynamic_cast<FuncNode*>(efi.rightnode());

  std::cerr << "Left: " << *left << std::endl; 

  std::cerr << "Right: " << *right << std::endl;

}

void AtomFluxJumpTest::force_value(const FEMesh* mesh, const Element* element,
				   const Equation* eqn,
				   const MasterPosition& gpt,
				   double time, SmallSystem *eqndata) const
{
  std::cerr << "AtomFluxJumpTest::force_value called." << std::endl;
  
  const InterfaceElement *ie = dynamic_cast<const InterfaceElement*>(element);
  if (ie->side()==LEFT) {
    eqndata->force_vector_element(0) -= 1.0;
  }
  else { // ie->side()!=LEFT, must be RIGHT
  }
}
