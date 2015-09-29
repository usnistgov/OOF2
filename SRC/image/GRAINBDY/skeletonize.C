// -*- C++ -*-
// $RCSfile: skeletonize.C,v $
// $Revision: 1.7 $
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

#include <math.h>

#include "skeletonize.h"
#include "common/array.h"
#include "common/boolarray.h"

bool isContour(const BoolArray &image,const ICoord pt) {
  if(image[pt]==1 && (pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1))
    return true;
  if (image[pt]==1) {  // If the point is white
    for (int a = -1; a <= 1; a++) {  // Twice
      for (int b = -1; b <= 1; b++) {  // Twice
	if (image[pt+ICoord(a,b)] == 0)
	  return true;  // Returns true if any of the points surrounding the white one is black
      }
    }
  }
  return false;
}

bool isDeletable(const BoolArray& image,ICoord pt) {
  //check 0-1 transitions
//  if(pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1)
//    return false;

  int numTrans=0;
  int xChange[9]={-1,0,1,1,1,0,-1,-1,-1};
  int yChange[9]={1,1,1,0,-1,-1,-1,0,1};

  for(int a=0;a<8;a++) {
    bool pixVal1,pixVal2;
    //int newX1=pt(0)+xChange[a], newY1=pt(1)+yChange[a];
    //int newX2=pt(0)+xChange[a+1],newY2=pt(1)+yChange[a+1];

    if(image.contains(pt+ICoord(xChange[a],yChange[a])))
      pixVal1=image[pt+ICoord(xChange[a],yChange[a])];
    else
      pixVal1=0;
    
    if(image.contains(pt+ICoord(xChange[a+1],yChange[a+1])))
      pixVal2=image[pt+ICoord(xChange[a+1],yChange[a+1])];
    else
      pixVal2=0;
    if(pixVal1==0 && pixVal2==1)
      numTrans++;
  }
 
  if (numTrans!=1)
    return false;

  //check nonzero neighbors
  int numNonzero=0;
  for (int a=-1;a<=1;a++) {
    for (int b=-1;b<=1;b++) {
      if(image.contains(pt+ICoord(a,b)) && (a!=0 || b!=0) && image[pt+ICoord(a,b)])
	numNonzero++;
    }
  }

  if ((numNonzero<2) || (numNonzero>6))
    return false;

  return true;
}

bool satisfiesStep1(const BoolArray &image,ICoord pt) {
//  if(pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1)
//    return false;
  int p2=0,p4=0,p6=0,p8=0;
  if(pt(1)+1<image.height())
    p2=int(image[ICoord(pt(0),pt(1)+1)]);
  if(pt(0)+1<image.width())
    p4=int(image[ICoord(pt(0)+1,pt(1))]);
  if(pt(1)-1>=0)
    p6=int(image[ICoord(pt(0),pt(1)-1)]);
  if(pt(0)-1>=0)
    p8=int(image[ICoord(pt(0)-1,pt(1))]);
  if ((p2*p4*p6==0)&&(p4*p6*p8==0)) {
    return true;
  }    
  else {
    return false;
  }
}

bool satisfiesStep2(const BoolArray &image,ICoord pt) {
//  if(pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1)
//    return false;

  int p2=0,p4=0,p6=0,p8=0;
  if(pt(1)+1<image.height())
    p2=image[ICoord(pt(0),pt(1)+1)];
  if(pt(0)+1<image.width())
    p4=image[ICoord(pt(0)+1,pt(1))];
  if(pt(1)-1>=0)
    p6=image[ICoord(pt(0),pt(1)-1)];
  if(pt(0)-1>=0)
    p8=image[ICoord(pt(0)-1,pt(1))];
  if ((p2*p4*p8==0)&&(p2*p6*p8==0))
    return true;
  else
    return false;
}

BoolArray skeletonize(const BoolArray &image) {
    std::cout << "here" << std::endl;
  int w=image.width();
  int h=image.height();
  BoolArray flag(ICoord(w,h),false);
  for(BoolArray::iterator i=flag.begin();i!=flag.end(); ++i)
    flag[i]=0;
  BoolArray deleted = image.clone();

  int step=1;
  bool stop=false;

  while (!stop) {
    int numChanged=0;
    for (int a = 0; a < w; a++) {
      for (int b = 0; b < h; b++) {
	if (/*deleted[ICoord(a,b)]*/isContour(deleted,ICoord(a,b)) && isDeletable(deleted,ICoord(a,b))) {
	  if (step == 1) {
	    if (satisfiesStep1(deleted,ICoord(a,b))) {
              flag[ICoord(a,b)]=1;
 	      numChanged++;
	    }
	  }
	  else {
	    if (satisfiesStep2(deleted,ICoord(a,b))) {  
	      flag[ICoord(a,b)]=1;  // Marks point for deletion
  	      numChanged++;
	    }
	  }
	}
      }
    }
    std::cout << "middle " << std::endl;

    //remove flagged points
    for (int c = 0; c < w; c++) {
      for (int d = 0; d < h; d++) {
	if (flag[ICoord(c,d)]==1) {
	  flag[ICoord(c,d)]=0;
	  deleted[ICoord(c,d)]=0;
	}
      }
    }
    step *= -1;
    if (numChanged==0)
      stop=true;
  }
  std::cout << " ending" << std::endl;
  return deleted;
}

