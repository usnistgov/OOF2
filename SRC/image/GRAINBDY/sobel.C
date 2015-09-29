// -*- C++ -*-
// $RCSfile: sobel.C,v $
// $Revision: 1.6 $
// $Author: langer $
// $Date: 2014/09/27 21:41:32 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "sobel.h"

#include <math.h>
#include "mask.h"
#include "common/array.h"
#include "common/doublearray.h"

Sobel::Sobel(int dir)
  : MASK(3,3)
{
  if(dir==0) { //Vertical
    maskArray[ICoord(0,0)]=-1;
    maskArray[ICoord(0,1)]=-2;
    maskArray[ICoord(0,2)]=-1;
    maskArray[ICoord(1,0)]=0;
    maskArray[ICoord(1,1)]=0;
    maskArray[ICoord(1,2)]=0;
    maskArray[ICoord(2,0)]=1;
    maskArray[ICoord(2,1)]=2;
    maskArray[ICoord(2,2)]=1;
  }
  else if(dir==2){ //Horizontal
    maskArray[ICoord(0,0)]=-1;
    maskArray[ICoord(1,0)]=-2;
    maskArray[ICoord(2,0)]=-1;
    maskArray[ICoord(0,1)]=0;
    maskArray[ICoord(1,1)]=0;
    maskArray[ICoord(2,1)]=0;
    maskArray[ICoord(0,2)]=1;
    maskArray[ICoord(1,2)]=2;
    maskArray[ICoord(2,2)]=1;
  }
  else if(dir==3){ //Diagonal bottom left to top right
    maskArray[ICoord(0,0)]=0;
    maskArray[ICoord(1,0)]=1;
    maskArray[ICoord(2,0)]=2;
    maskArray[ICoord(0,1)]=-1;
    maskArray[ICoord(1,1)]=0;
    maskArray[ICoord(2,1)]=1;
    maskArray[ICoord(0,2)]=-2;
    maskArray[ICoord(1,2)]=-1;
    maskArray[ICoord(2,2)]=0;
  }
  else if(dir==1){ //Diagonal top left to bottom right
    maskArray[ICoord(0,0)]=-2;
    maskArray[ICoord(1,0)]=-1;
    maskArray[ICoord(2,0)]=0;
    maskArray[ICoord(0,1)]=-1;
    maskArray[ICoord(1,1)]=0;
    maskArray[ICoord(2,1)]=1;
    maskArray[ICoord(0,2)]=0;
    maskArray[ICoord(1,2)]=1;
    maskArray[ICoord(2,2)]=2;
  }
}
