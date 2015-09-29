// -*- C++ -*-
// $RCSfile: quad4shapefunction.C,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:06 $

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
#include "quad4shapefunction.h"

//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//

// Master element for the four node quadrilateral:
//
//  (-1,1)   3--------------------2  (1,1)
//           |                    | 
//           |                    |
//           |                    |
//           |                    |
//           |                    |
//           |                    |
//           |                    |
//  (-1,-1)  0--------------------1  (1,-1)


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

Quad4ShapeFunction::Quad4ShapeFunction(const MasterElement &mel)
  : ShapeFunction(4, mel)
{
  precompute(mel);
}

double Quad4ShapeFunction::value(ShapeFunctionIndex i,
				      const MasterCoord &mc) const
{
  if(i == 0)
    return 0.25*(1. - mc(0))*(1. - mc(1));
  if(i == 1)
    return 0.25*(1. + mc(0))*(1. - mc(1));
  if(i == 2)
    return 0.25*(1. + mc(0))*(1. + mc(1));
  if(i == 3)
    return 0.25*(1. - mc(0))*(1. + mc(1));
  throw ErrBadIndex(i, __FILE__, __LINE__);
}

double Quad4ShapeFunction::masterderiv(ShapeFunctionIndex i, SpaceIndex j,
				       const MasterCoord &mc) const
{
  switch(i) {
  case 0:
    if(j == 0)
      return -0.25*(1. - mc(1));
    if(j == 1)
      return -0.25*(1. - mc(0));
    break;
  case 1:
    if(j == 0)
      return  0.25*(1. - mc(1));
    if(j == 1)
      return -0.25*(1. + mc(0));
    break;
  case 2:
    if(j == 0)
      return  0.25*(1. + mc(1));
    if(j == 1)
      return  0.25*(1. + mc(0));
    break;
  case 3:
    if(j == 0)
      return -0.25*(1. + mc(1));
    if(j == 1)
      return  0.25*(1. - mc(0));
    break;
  default:
    throw ErrBadIndex(i, __FILE__, __LINE__);
  }
  throw ErrBadIndex(j, __FILE__, __LINE__);
}

