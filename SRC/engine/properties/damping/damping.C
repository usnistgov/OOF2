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

#include "engine/IO/propertyoutput.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/properties/damping/damping.h"
#include "engine/smallsystem.h"

IsotropicDampingProp::IsotropicDampingProp(const std::string &name,
					   PyObject *registration,
					   double coeff)
  : EqnProperty(name, registration),
    coeff(coeff)
{}

void IsotropicDampingProp::precompute(FEMesh *mesh) {
  displacement = Field::getField("Displacement");
  force_balance = Equation::getEquation("Force_Balance");
}

void IsotropicDampingProp::time_deriv_matrices(
					   const FEMesh *mesh,
					   const Element *element,
					   const ElementFuncNodeIterator &node,
					   const Equation *eqn,
					   const MasterPosition &mpos,
					   double time,
					   void*,
					   SmallSystem *eqndata)
  const
{
  // TODO: Check the check.   Are there any tests that use this property?
  if(*eqn != *force_balance)
    throw ErrProgrammingError("Unexpected equation!", __FILE__, __LINE__);
  double shapeFuncVal = node.shapefunction(mpos);
  for(IndexP component : *eqn->components()) {
    eqndata->damping_matrix_element(component, displacement, component, node)
      += coeff*shapeFuncVal;
  }
}

int IsotropicDampingProp::integration_order(const CSubProblem*,
					    const Element *el) 
  const 
{
  return el->shapefun_degree(); 
}

void IsotropicDampingProp::output(FEMesh *mesh,
				  const Element *element,
				  const PropertyOutput *output,
				  const MasterPosition &pos,
				  OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Material Constants:Mechanical:Damping") {
    ScalarOutputVal *sdata = dynamic_cast<ScalarOutputVal*>(data);
    *sdata = coeff;
  }
}
