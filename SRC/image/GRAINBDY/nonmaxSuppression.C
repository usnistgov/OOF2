// -*- C++ -*-
// $RCSfile: nonmaxSuppression.C,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:41:32 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modifed
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "image/oofimage.h"
#include "common/doublearray.h"
#include "common/intarray.h"

DoubleArray nonmaxSuppress(const DoubleArray& image,const IntArray& gradDirs) {
  DoubleArray newArray(image.size(),0.0);
  int w=image.width();
  int h=image.height();

  for(DoubleArray::const_iterator i=image.begin();i!=image.end();++i) {
    ICoord comp1, comp2;

    int x=i.coord()(0), y=i.coord()(1);
    if(gradDirs[i.coord()]==0) {
      comp1=ICoord(x-1,y); 
      comp2=ICoord(x+1,y);
    }
    else if(gradDirs[i.coord()]==2) {
      comp1=ICoord(x,y+1);
      comp2=ICoord(x,y-1);
    }
    else if(gradDirs[i.coord()]==3) {
      comp1=ICoord(x-1,y+1);
      comp2=ICoord(x+1,y-1);
    }
    else if(gradDirs[i.coord()]==1) {
      comp1=ICoord(x-1,y-1);
      comp2=ICoord(x+1,y+1);
    }
    if(comp1(0)>=0 && comp1(0)<w && comp1(1)>=0 && comp1(1)<h && 
       comp2(0)>=0 && comp2(0)<w && comp2(1)>=0 && comp2(1)<h && 
       (image[i]<image[comp1] || image[i]<image[comp2])) {
      newArray[i.coord()]=0;
    }
    else
      newArray[i.coord()]=image[i];
  }
  return newArray;
}
