// -*- C++ -*-
// $RCSfile: edge2shapefunction.C,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2010/12/06 04:11:48 $

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
#include "edge2shapefunction.h"

// Master element for the 2-noded edge element:
//
//     0----------------------1
//  (-1,0)                  (1,0)
// Here, the y-component of master-coord is totally trivial.


Edge2ShapeFunction::Edge2ShapeFunction(const MasterElement &mel)
  : ShapeFunction(2, mel)
{
  precompute(mel);
}

double Edge2ShapeFunction::value(ShapeFunctionIndex i,
				 const MasterCoord &mc) const
{
  if(i == 0)
    return 0.5*(1. - mc(0));
  if(i == 1)
    return 0.5*(1. + mc(0));
  throw ErrBadIndex(i, __FILE__, __LINE__);
}

double Edge2ShapeFunction::masterderiv(ShapeFunctionIndex i, SpaceIndex j,
				       const MasterCoord &mc) const
{
  switch(i) {
  case 0:
    if(j == 0)
      return -0.5;
    if(j == 1)
      return 0.;
    break;
  case 1:
    if(j == 0)
      return  0.5;
    if(j == 1)
      return 0.;
    break;
  default:
    throw ErrBadIndex(i, __FILE__, __LINE__);
  }
  throw ErrBadIndex(j, __FILE__, __LINE__);
}

// TODO: Implement realderiv somehow.  This is complicated by the fact
// that we don't necessarily know the orientation of the element.
// Even if you make it along the line of the element, it's not
// obviously right, because the deformed element may curve...
