// -*- C++ -*-
// $RCSfile: edge3shapefunction.C,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:41:05 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "engine/ooferror.h"
#include "edge3shapefunction.h"

// Master element for the 3-noded edge element:
//
//     0----------1------------2
//  (-1,0)       (0,0)       (1,0)
// Here, the y-component of master-coord is totally trivial.


Edge3ShapeFunction::Edge3ShapeFunction(const MasterElement &mel)
  : ShapeFunction(3, mel)
{
  precompute(mel);
}

double Edge3ShapeFunction::value(ShapeFunctionIndex i,
				 const MasterCoord &mc) const
{
  if(i == 0)
    return 0.5*(mc(0)*mc(0) - mc(0));
  if(i == 1)
    return 1. - mc(0)*mc(0);
  if(i == 2)
    return 0.5*(mc(0)*mc(0) + mc(0));
  throw ErrBadIndex(i, __FILE__, __LINE__);
}

double Edge3ShapeFunction::masterderiv(ShapeFunctionIndex i, SpaceIndex j,
				       const MasterCoord &mc) const
{
  switch(i) {
  case 0:
    if(j == 0)
      return mc(0) - 0.5;
    if(j == 1)
      return 0.;
    break;
  case 1:
    if(j == 0)
      return -2.*mc(0);
    if(j == 1)
      return 0.;
    break;
  case 2:
    if(j == 0)
      return mc(0) + 0.5;
    if(j == 1)
      return 0.;
    break;
  default:
    throw ErrBadIndex(i, __FILE__, __LINE__);
  }
  throw ErrBadIndex(j, __FILE__, __LINE__);
}
