// -*- C++ -*-
// $RCSfile: surfacetest.C,v $
// $Revision: 1.5 $
// $Author: reida $
// $Date: 2011/08/11 21:40:36 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#include <oofconfig.h>
#include "surfacetest.h"
#include "engine/csubproblem.h"
#include "engine/linearizedsystem.h"
#include "engine/node.h"
#include "engine/element.h"
#include "engine/field.h"
#include "engine/material.h"
#include "engine/smallsystem.h"

ForceSurfaceTest::ForceSurfaceTest(PyObject *reg, const std::string &nm,
			     double coef)
  : EqnProperty(nm,reg),coef(coef)
{
}

int ForceSurfaceTest::integration_order(const CSubProblem*, 
				     const Element *el) const
{
  return 0;
}

// InterfaceElements can have split nodes.  The InterfaceElement class
// provides a get_nodelist2 function, which works similarly to the
// Element's get_nodelist() function.


//pElem must be an InterfaceElement

void ForceSurfaceTest::begin_element(const CSubProblem *pSubp, 
				  const Element *pElem) {
  
  std::cerr << "SFTest Begin-element called." << std::endl;
}

void ForceSurfaceTest::end_element(const CSubProblem* pSubp, const Element* pElem)
{}

void ForceSurfaceTest::cross_reference(Material* pMat)
{
  return;
}

void ForceSurfaceTest::post_process(CSubProblem* pSubp, 
				 const Element *pElem) const
{
}


void ForceSurfaceTest::force_value(const FEMesh *mesh, 
			      const Element *element,
			      const Equation *eqn, 
			      const MasterPosition &pt,
			      double time, SmallSystem *eqndata) const {
  
  std::cerr << "SFTest Force-value called." << std::endl;
}


void ForceSurfaceTest::force_deriv_matrix(const FEMesh *mesh, 
				     const Element *element,
				     const Equation *eqn, 
				     const ElementFuncNodeIterator&,
				     const MasterPosition &pt,
				     double time, 
				     SmallSystem *eqndata) const {
  std::cerr << "SFTest Force deriv called." << std::endl;
}



FluxSurfaceTest::FluxSurfaceTest(PyObject *reg, const std::string &nm,
				 double coef) :
  FluxProperty(nm,reg),coef(coef) {}

int FluxSurfaceTest::integration_order(const CSubProblem* s,
				       const Element *el) const {
  return 0;
}

void FluxSurfaceTest::begin_element(const CSubProblem *sp,
				    const Element *e) {
  std::cerr << "FluxSurfaceTest::begin_element called." << std::endl;
}

void FluxSurfaceTest::end_element(const CSubProblem *sp,
				  const Element *e) {
  std::cerr << "FluxSurfaceTest::end_element called." << std::endl;
}

void FluxSurfaceTest::cross_reference(Material *m) {
  return;
}

void FluxSurfaceTest::post_process(CSubProblem *sp,
				   const Element *e) const {}

void FluxSurfaceTest::static_flux_value(const FEMesh *mesh,
					const Element *element,
					const Flux *flux,
					const MasterPosition &pt,
					double time,
					SmallSystem *fluxdata) const {
  std::cerr << "FluxSurfaceTest::static_flux_value called." << std::endl;
}

void FluxSurfaceTest::flux_matrix(const FEMesh *mesh,
				  const Element *element,
				  const ElementFuncNodeIterator &efi,
				  const Flux *flux,
				  const MasterPosition &pt,
				  double time,
				  SmallSystem *fluxdata) const {
  std::cerr << "FluxSurfaceTest::flux_matrix called." << std::endl;
}
