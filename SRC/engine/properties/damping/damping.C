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

IsotropicDampingProp::IsotropicDampingProp(PyObject *registration,
					   const std::string &name,
					   double coeff)
  : EqnProperty(name, registration),
    coeff(coeff)
{}

void IsotropicDampingProp::precompute(FEMesh *mesh) {
  displacement = Field::getField("Displacement");
}

void IsotropicDampingProp::first_time_deriv_matrix(
			 const FEMesh *mesh,
			 const Element *lmnt,
			 const Equation *eqn,
			 const ElementFuncNodeIterator &eni,
			 const MasterPosition &mpos,
			 double time,
			 SmallSystem *eqndata)
  const
{
  double shapeFuncVal = eni.shapefunction(mpos);
  for(IndexP ell : displacement->components(IN_PLANE)) {
    for(IndexP eqncomp : eqn->components()) {
      eqndata->damping_matrix_element(eqncomp, displacement, ell, eni)
	+= coeff * shapeFuncVal;
    }
  }
}

int IsotropicDampingProp::integration_order(const CSubProblem*,
					    const Element*) 
  const 
{
  return 1;
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
