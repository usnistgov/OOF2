// -*- C++ -*-
// $RCSfile: masks.C,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:41:37 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */
#include <oofconfig.h>

#include <iostream>
#include "image/SEGMENTATION/masks.h"
#include "common/doublearray.h"

MASKS::MASKS(int M,int N) //M and N should be odd
  :maskArrays(ICoord(M+(1-M%2),N+(1-N%2)),0.0)
{
}

int MASKS::width() {
  return maskArrays.width();
}

int MASKS::height() {
  return maskArrays.height();
}

DoubleArray MASKS::applyMasks(const DoubleArray& image) {
//This applies the mask that is stored onto an array of doubles representing
//the image.
  DoubleArray newImage(image.size(),0.0);
  double tempSum=0;
  int startI,endI,startK,endK;
  int M=maskArrays.width(), N=maskArrays.height();

  for(int x=0;x<image.width();x++) {
    for(int y=0;y<image.height();y++) {
      startI=-M/2; endI=M/2;
      startK=-N/2; endK=N/2;
      if(x-M/2<0)
	startI=-x;
      if(y-N/2<0)
	startK=-y;
      if(x+M/2>=image.width())
	endI=image.width()-x-1;
      if(y+N/2>=image.height())
	endK=image.height()-y-1;
      for(int i=startI;i<=endI;i++) {
	for(int k=startK;k<=endK;k++) {
	  tempSum+=image[ICoord(x+i,y+k)]*maskArrays[ICoord(M/2+i,N/2+k)];
	  //If M and N aren't odd, will get segmentation fault
	}
      }
      newImage[ICoord(x,y)]=tempSum;
      //    if(tempSum<0)
      tempSum=0;
    }
  }
  return newImage;
}
