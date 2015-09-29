// -*- C++ -*-
// $RCSfile: modifiedGabor.C,v $
// $Revision: 1.13 $
// $Author: langer $
// $Date: 2014/09/27 21:41:31 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "modifiedGabor.h"
#include <math.h>
#include "mask.h"
#include "common/doublearray.h"

//array.h is included in modifiedGabor.h

ModGabor::ModGabor(int a,int b,double phi2)
  : MASK(3*b,3*b), weights(ICoord(3*b,3*b),0.0) 
{
  int M=maskArray.width(), N=maskArray.height();
  double phi=phi2*M_PI/180.;
  weightedArea=0;
//  weights.resize(maskArray.size());
  double xP,yP;
  int x,y;

  for(DoubleArray::iterator i=weights.begin();i!=weights.end();++i) {
    x=i.coord()(0)-M/2; y=i.coord()(1)-N/2;
    xP=x*cos(phi)+y*sin(phi); yP=y*cos(phi)-x*sin(phi);
    weights[i]= exp(-M_PI*(xP*xP/a/a+yP*yP/b/b));

  //    std::cout<<weights[i]<<" ";
  //  if(i.coord()(0)==weights.width()-1)
  //    std::cout<<std::endl;

    weightedArea+=weights[i];
  }

//  std::cout<<weightedArea<<std::endl<<std::endl;

  double gabSum=0;
  double omega=1./(double)(2.*a);
  double r,theta;
  DoubleArray funcVals(maskArray.size(),0.0);
  
  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i){
    x=i.coord()(0)-M/2; y=i.coord()(1)-N/2;
    //xP=x*cos(phi)+y*sin(phi); yP=y*cos(phi)-x*sin(phi);
    r=sqrt(float(x*x+y*y));
    theta=atan2(float(y),float(x));
    funcVals[i]=cos(2.*omega*M_PI*r*cos(theta-phi));
    maskArray[i]=weights[i]*funcVals[i];

  //    std::cout<<maskArray[i]<<" ";
  //  if(i.coord()(0)==maskArray.width()-1)
  //    std::cout<<std::endl;

  //    gabSum+=maskArray[i]*weights[i];
    gabSum+=weights[i]*maskArray[i];
  }  
 
 /* double subNum=gabSum/(M*M);
  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i) {
    maskArray[i]-=subNum; 
  }*/  
//  std::cout<<std::endl;

  double gabMean=gabSum/weightedArea;
  
  //std::cout<<gabMean<<std::endl;  
  for(DoubleArray::iterator i=maskArray.begin();i!=maskArray.end();++i) { 

    //maskArray[i]-=gabMean;
    maskArray[i]=weights[i]*(funcVals[i]-gabMean);
    //     maskArray[i]-=.113984;

    // std::cout<<maskArray[i]<<" ";

     //    if(i.coord()(0)==maskArray.width()-1)
     //  std::cout<<std::endl;
   }
 //   std::cout<<std::endl<<"----------------------------"<<std::endl;
}


DoubleArray ModGabor::findImageMeans(const DoubleArray& image) const {
  //This function finds the weighted mean of an array centered at every point (x,y) on the image.
  int startI, endI, startK, endK;
  DoubleArray meanImage(image.size(),0.0);
  double tempSum=0;
  
  int M=maskArray.width(), N=maskArray.height();
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
	  tempSum+=image[ICoord(x+i,y+k)]*weights[ICoord(i+M/2,k+N/2)];
	}
      }
      meanImage[ICoord(x,y)]=tempSum/weightedArea;
      tempSum=0;
    }
  }
  return meanImage;
}

DoubleArray ModGabor::applyMask(const DoubleArray& image) {
//  DoubleArray image(image1.width(),image1.height());
//  image=setImage(image1);
  DoubleArray newImage(image.size(),0.0);

  DoubleArray meanImage(image.size(),0.0);
  meanImage=findImageMeans(image);
  double tempSum=0;
  int startI,endI,startK,endK;
  int M=maskArray.width(), N=maskArray.height();

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
      if(y+M/2>=image.height())
	endK=image.height()-y-1;
      for(int i=startI;i<=endI;i++) {
	for(int k=startK;k<=endK;k++) {
	  tempSum+=(image[ICoord(x+i,y+k)]-meanImage[ICoord(x,y)])*maskArray[ICoord(M/2+i,N/2+k)];
	  //If M and N aren't odd, M/2+i and N/2+k will go out of bounds at end.
	}
      }
      newImage[ICoord(x,y)]=fabs(tempSum);
      tempSum=0;
    }
  }

  return newImage;
}

DoubleArray ModGabor::setImage(const DoubleArray& image) {
  DoubleArray newImage(image.size(),0.0);
  DoubleArray meanImage(image.size(),0.0);
  meanImage=findImageMeans(image);
  
  for(int x=0;x<image.width();x++) {
    for(int y=0;y<image.height();y++) {
       newImage[ICoord(x,y)]=image[ICoord(x,y)]-meanImage[ICoord(x,y)];
    }
  }

  return newImage;
}

