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
			   double gx, double gy)
  : EqnProperty(nm, reg),
    g({gx, gy})
{
}

int ForceDensity::integration_order(const CSubProblem*, const Element *el) const
{
  return 0;
}

void ForceDensity::force_value(const FEMesh *mesh, const Element *element,
			       const Equation *eqn, const MasterPosition &x,
			       double time, void *data,
			       SmallSystem *eqndata) const
{
  eqndata->forceVector() += g;
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
    (*listdata)[0] = g[0];
    (*listdata)[1] = g[1];
  }
}
