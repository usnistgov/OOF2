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
#include "engine/properties/massdensity/massdensity.h"
#include "engine/smallsystem.h"


MassDensityProp::MassDensityProp(const std::string &name,
				 PyObject *registration,
				 double rho)
  : EqnProperty(name, registration), rho_(rho)
{}

void MassDensityProp::precompute(FEMesh *mesh) {
  disp = Field::getField("Displacement");
}

void MassDensityProp::second_time_deriv_matrix(const FEMesh *mesh,
					       const Element *lmnt,
					       const Equation *eqn,
					       const ElementFuncNodeIterator &eni,
					       const MasterPosition &mpos,
					       double time,
					       SmallSystem *eqdata) const {

  // Optional -- check that the equation is the right one.
  double shapeFuncVal = eni.shapefunction(mpos);
  for(IndexP component : *eqn->components()) {
    eqdata->mass_matrix_element(component, disp, component, eni)
      += rho_ * shapeFuncVal;
  }
}

int MassDensityProp::integration_order(const CSubProblem* subp,
				       const Element *el) const {
  return 2*el->shapefun_degree();
}

void MassDensityProp::output(FEMesh *mesh,
			     const Element *element,
			     const PropertyOutput *output,
			     const MasterPosition &pos,
			     OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Material Constants:Mechanical:Mass Density") {
    ScalarOutputVal *sdata = dynamic_cast<ScalarOutputVal*>(data);
    *sdata = rho_;
  }
}
