// -*- C++ -*-
// $RCSfile: laplacian.C,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:41:30 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "laplacian.h"

#include <math.h>
#include "mask.h"
#include "common/array.h"
#include "common/doublearray.h"

Laplacian::Laplacian()
  : MASK(3,3)
{
  maskArray[ICoord(0,0)]=0;
  maskArray[ICoord(0,1)]=1;
  maskArray[ICoord(0,2)]=0;
  maskArray[ICoord(1,0)]=1;
  maskArray[ICoord(1,1)]=-4;
  maskArray[ICoord(1,2)]=1;
  maskArray[ICoord(2,0)]=0;
  maskArray[ICoord(2,1)]=1;
  maskArray[ICoord(2,2)]=0;
}
