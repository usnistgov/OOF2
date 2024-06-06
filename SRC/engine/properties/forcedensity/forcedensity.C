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
#include "common/ooferror.h"
#include "common/trace.h"
#include "engine/IO/propertyoutput.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/equation.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/indextypes.h"
#include "engine/material.h"
#include "engine/smallsystem.h"
#include "forcedensity.h"


ForceDensity::ForceDensity(const std::string &nm, PyObject *reg, 
			   double x, double y)
  : EqnProperty(nm, reg),
    gx(x),
    gy(y)
{}

int ForceDensity::integration_order(const CSubProblem*, const Element *el) const
{
  return el->shapefun_degree();
}

void ForceDensity::force_value(const FEMesh *mesh, const Element *element,
			       const Equation *eqn, const MasterPosition &x,
			       double time, SmallSystem *eqndata) const
{
  eqndata->force_vector_element(0) -= gx;
  eqndata->force_vector_element(1) -= gy;
}

void ForceDensity::output(FEMesh *mesh,
			  const Element *element,
			  const PropertyOutput *output,
			  const MasterPosition &pos,
			  OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Material Constants:Mechanical:Force Density F") {
    ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
    assert(listdata->size() == 2);
    (*listdata)[0] = gx;
    (*listdata)[1] = gy;
  }
}
