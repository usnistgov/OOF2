// -*- C++ -*-
// $RCSfile: connectEdge.C,v $
// $Revision: 1.9 $
// $Author: langer $
// $Date: 2014/09/27 21:41:29 $

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
#include "common/array.h"
#include <iostream>
#include "image/GRAINBDY/imageops.h"
#include "image/GRAINBDY/close.h"
#include "image/GRAINBDY/skeletonize.h"
#include "common/doublearray.h"
#include "common/boolarray.h"

//bool isDiscontinuous(const Image &image, const ICoord pt);

bool isBroken(const BoolArray &image,ICoord pt) {
  // Is there a single pixel gap in a line at the given point?
  if (image[pt] || pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1)
    return false;
  
  int p1=image[ICoord(pt(0)-1,pt(1)+1)];
  int p2=image[ICoord(pt(0),pt(1)+1)];
  int p3=image[ICoord(pt(0)+1,pt(1)+1)];
  int p4=image[ICoord(pt(0)-1,pt(1))];
  int p6=image[ICoord(pt(0)+1,pt(1))];
  int p7=image[ICoord(pt(0)-1,pt(1)-1)];
  int p8=image[ICoord(pt(0),pt(1)-1)];
  int p9=image[ICoord(pt(0)+1,pt(1)-1)];

  int compNum=p1 + 2*p2 + 4*p3 + 8*p4 + 16*p6 + 32*p7 + 64*p8 + 128*p9;
/*  if ( 
      ((p1==0) && (p2==0) && (p3==1) && (p4==0) && (p6==0) && (p7==1) && (p8==0) && (p9==0))
      || ((p1==1) && (p2==0) && (p3==0) && (p4==0) && (p6==0) && (p7==0) && (p8==0) && (p9==1))
      || ((p1==0) && (p2==0) && (p3==0) && (p4==1) && (p6==1) && (p7==0) && (p8==0) && (p9==0))
      || ((p1==0) && (p2==1) && (p3==0) && (p4==0) && (p6==0) && (p7==0) && (p8==1) && (p9==0))
      || ((p1==0) && (p2==0) && (p3==1) && (p4==0) && (p6==0) && (p7==0) && (p8==1) && (p9==0))
      || ((p1==1) && (p2==0) && (p3==0) && (p4==0) && (p6==0) && (p7==0) && (p8==1) && (p9==0))
      || ((p1==0) && (p2==0) && (p3==0) && (p4==1) && (p6==0) && (p7==0) && (p8==0) && (p9==1))
      || ((p1==0) && (p2==0) && (p3==1) && (p4==1) && (p6==0) && (p7==0) && (p8==0) && (p9==0))
      || ((p1==1) && (p2==0) && (p3==0) && (p4==0) && (p6==1) && (p7==0) && (p8==0) && (p9==0))
      || ((p1==0) && (p2==1) && (p3==0) && (p4==0) && (p6==0) && (p7==1) && (p8==0) && (p9==0))
      || ((p1==0) && (p2==1) && (p3==0) && (p4==0) && (p6==0) && (p7==0) && (p8==0) && (p9==1))
      || ((p1==0) && (p2==0) && (p3==0) && (p4==0) && (p6==1) && (p7==1) && (p8==0) && (p9==0))
      )*/
  if(compNum==36 || compNum==129 || compNum==24 || compNum==66 || compNum==68
     || compNum==65 || compNum==136 || compNum==12 || compNum==17 || compNum==34
     || compNum==130 || compNum==48)
    return true;
  
  return false;
}

BoolArray closeLines(const BoolArray &image) {
  // Fill in single pixels gaps in lines.
  BoolArray temp=image;
  for (BoolArray::const_iterator i=image.begin(); i!=image.end(); ++i) {
    if (isBroken(image,i.coord())) {
      temp[i.coord()]=1;
    }
  }
  return temp;
}

bool isDiscontinuous(const BoolArray &image, const ICoord pt) { 
  //This function checks to see if a point is discontinuous. It does
  //so by checking the pixels surrounding the current pixel.

  if(image[pt]==0 || pt(0)==0 || pt(0)==image.width()-1 || pt(1)==0 || pt(1)==image.height()-1)
    return false;
  int p1=image[ICoord(pt(0)-1,pt(1)+1)];
  int p2=image[ICoord(pt(0),pt(1)+1)];
  int p3=image[ICoord(pt(0)+1,pt(1)+1)];
  int p4=image[ICoord(pt(0)-1,pt(1))];
  int p6=image[ICoord(pt(0)+1,pt(1))];
  int p7=image[ICoord(pt(0)-1,pt(1)-1)];
  int p8=image[ICoord(pt(0),pt(1)-1)];
  int p9=image[ICoord(pt(0)+1,pt(1)-1)];
  

  int numNonZero=0;
  
  for(int a=-1;a<=1;a++)
    for(int b=-1;b<=1;b++)
      numNonZero+=image[pt+ICoord(a,b)];
  if(numNonZero==1 || numNonZero==2)
    return true;
  
  int compVal=p1 + 2*p2 + 4*p3 + 8*p4 + 16*p6 + 32*p7 + 64*p8 + 128*p9;
  if(compVal==3 || compVal==6 || compVal==96 || compVal==192 || compVal==20
     || compVal==9 || compVal==40 || compVal==144)
    return true;
  return false;

  //  //3 pixel cases  *** CHECK may not be necessary
  //top left
/*  if ((p1==1) && (p3==0) && (p4==0) && (p6==0) && (p7==0) && (p8==0) && (p9==0) && (p2==1))
    return true; 
  //top right
  if ((p1==0) && (p3==1) && (p4==0) && (p6==0) && (p7==0) && (p8==0) && (p9==0) && (p2==1)) 
    return true; 
  //bottom left
  if ((p1==0) && (p3==0) && (p4==0) && (p6==0) && (p7==1) && (p8==1) && (p9==0) && (p2==0)) 
    return true; 
  //bottom right
  if ((p1==0) && (p3==0) && (p4==0) && (p6==0) && (p7==0) && (p8==1) && (p9==1) && (p2==0)) 
    return true; 
  //right top
  if ((p1==0) && (p3==1) && (p4==0) && (p6==1) && (p7==0) && (p8==0) && (p9==0) && (p2==0)) 
    return true; 
  //left top
  if ((p1==1) && (p3==0) && (p4==1) && (p6==0) && (p7==0) && (p8==0) && (p9==0) && (p2==0)) 
    return true; 
  //left bottom
  if ((p1==0) && (p3==0) && (p4==1) && (p6==0) && (p7==1) && (p8==0) && (p9==0) && (p2==0)) 
    return true; 
  //left bottom
  if ((p1==0) && (p3==0) && (p4==0) && (p6==1) && (p7==0) && (p8==0) && (p9==1) && (p2==0)) 
  return true;*/
}

BoolArray getAndReduceDiscontinuities (const BoolArray& connected1, const BoolArray newThresh, int d, int halfsize) {

  BoolArray connected=connected1.clone();
  int w = connected.width();
  int h = connected.height();
  int size=halfsize*2+1; //make size odd
  BoolArray box(ICoord(size,size),false);//	make small box	
  CloserClass cl = CloserClass();
  // int halfsize = size/2;
  Skeletonizing skel = Skeletonizing();
  for(BoolArray::iterator pt=connected.begin();pt!=connected.end();++pt) {    
    int a=pt.coord()(0), b=pt.coord()(1);
    if (connected[pt]==1 && isDiscontinuous(connected,pt.coord())) {
      for (int c=-halfsize;c<=halfsize;c++) {
	for (int d=-halfsize;d<=halfsize;d++) {
	  // TODO: Use if.. else to avoid extra computation
	  if(a+c>=0 && a+c<w && b+d>=0 && b+d<h) {
	    if ( (abs(c)<size/4) && (abs(d)<size/4) && box[ICoord(c+halfsize,d+halfsize)]==0)
	      box[ICoord(c+halfsize,d+halfsize)]=newThresh[ICoord(a+c,b+d)];
	    else
	      box[ICoord(c+halfsize,d+halfsize)]=connected[ICoord(a+c,b+d)];
	  }
	}
      }
      box=skel.skeletonize(cl.close(box,size/4));
      
      for (int g=-halfsize;g<=halfsize;g++) {
	for (int h2=-halfsize;h2<=halfsize;h2++) {
	  if(a+g>=0 && a+g<w && b+h2>=0 && b+h2<h) {
	    if (connected[ICoord(g+a,h2+b)]==0) {
	      connected[ICoord(g+a,h2+b)]=box[ICoord(g+halfsize,h2+halfsize)];
	    }
	  }
	}
      }
    }
  }

  return skel.skeletonize(cl.close(connected,d));
}

BoolArray removeDeadLines(const BoolArray & connected) {
  BoolArray temp=connected.clone();
  int numRemoved=-1;
  while (numRemoved!=0) { 
    numRemoved=0;
    for (int a = 1; a < connected.width()-1; a++) {
      for (int b = 1; b < connected.height()-1; b++) {
	if ( (temp[ICoord(a,b)]==1) && isDiscontinuous(temp,ICoord(a,b))) {
	  temp[ICoord(a,b)]=0;
	  numRemoved++;
	}
      }
    }
  }
  
  return temp;
}

BoolArray connect(const DoubleArray& gabor, double initialThreshold,double threshDecrease,  int d,int numEdgeIter, int boxSize,bool trim) {
  Skeletonizing skel = Skeletonizing();
  CloserClass cl = CloserClass();
  BoolArray threshed=threshold(gabor,initialThreshold);
  BoolArray connected=skel.skeletonize(cl.close(threshed,d));

  double curThresh=initialThreshold;
  for (int a=0;a<numEdgeIter;a++) {
    //   std::cout<<curThresh<<std::endl;
    threshed=threshold(gabor,curThresh);
    BoolArray temp=skel.skeletonize(cl.close(threshed,d));
    
    //   std::cout<<"Done skeletonizing"<<std::endl;
    connected=getAndReduceDiscontinuities(connected,temp,d,boxSize);
 //    std::cout<<"Done connection"<<std::endl;
    //std::cout<<a<<std::endl;
    curThresh-=threshDecrease*curThresh/100.;
  }
  
  if (trim)
    connected=removeDeadLines(connected);
  return connected;
}

void removeNoisePoints(double tol, BoolArray & image, DoubleArray minMaxRatio) {
  int w=image.width();
  int h=image.height();
  for (int a=0;a<w;a++) {
    for (int b=0;b<h;b++) {
      if ( (image[ICoord(a,b)]==1) && (minMaxRatio[ICoord(a,b)]>tol)) {
      //	std::cout<<"Noise removed at "<<a<<" "<<h-1-b<<std::endl;
	image[ICoord(a,b)]=0;
      }
    }
  }
}
