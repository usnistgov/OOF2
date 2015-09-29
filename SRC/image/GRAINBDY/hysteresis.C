// -*- C++ -*-
// $RCSfile: hysteresis.C,v $
// $Revision: 1.6 $
// $Author: langer $
// $Date: 2014/09/27 21:41:30 $

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
#include "common/boolarray.h"

/*
This is a modified threshold function developed by Canny and used in his Canny 
operator. There are two thresholds, T1 and T2, where T1<T2, used to select more
edge points while limiting noise. First, a normal threshold is performed using
T2 such that a new BoolArray stores the definite edge pixels. Next, all the
points not already included as an edge pixel are examined again. If the point's
value is over T1 and adjacent to an accepted edge pixel, then it too is added.
This process keeps looping through until there are no more possible edge points
to add.
*/


BoolArray hysteresisThresh(const DoubleArray& image, double T1, double T2)
{//T1 is the lower threshold and T2 is the higher threshold

  BoolArray newimage(image.width(),image.height());

  for (DoubleArray::const_iterator i = image.begin(); i != image.end(); ++i) {
    newimage[i.coord()] = image[i]>=T2;
  }
  
//  std::cout<<image[ICoord(296,20)]<<" "<<newimage[ICoord(296,20)]<<std::endl;
  int xChange[8]= {-1,0,1,1,1,0,-1,-1}, yChange[8]={1,1,1,0,-1,-1,-1,0};

  bool changed=1;
  while(changed) {
    changed=0;
    for (DoubleArray::const_iterator i = image.begin(); i != image.end(); ++i) {
      if(!newimage[i.coord()] && image[i]>=T1) {
	int x=i.coord()(0), y=i.coord()(1);
      	for(int dir=0;dir<8;dir++) {
	  int newX=x+xChange[dir], newY=y+yChange[dir];
	  if(newX>=0 && newX<image.width() && newY>=0 && newY<image.height() 
	     && newimage[ICoord(newX,newY)]) {
	    if(i.coord()(0)==296 && i.coord()(1)==20)
	      std::cout<<newX<<" "<<newY<<"="<<newimage[ICoord(newX,newY)]<<std::endl;
	    newimage[i.coord()]=1;
	    changed=1;
	    break;
	  }
	}
      }
    }
  }
  std::cout<<image[ICoord(296,20)]<<" "<<newimage[ICoord(296,20)]<<std::endl;
  return newimage;
}
