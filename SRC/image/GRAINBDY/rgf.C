// -*- C++ -*-
// $RCSfile: rgf.C,v $
// $Revision: 1.12 $
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

#include "rgf.h"

#include <math.h>
#include "mask.h"
#include "common/array.h"
#include "common/doublearray.h"

RealGF::RealGF(int a, int b, double phi)
  : MASK(3*b,3*b) 
{
  //This constructor defines the values in the mask using the Real Gabor Filter
//equations. 
  int M=maskArray.width(), N=maskArray.height();
  double phiR=phi*M_PI/180.; //phi in radians
  double omega=1./(double)(2.*a);
  double xP,yP,r,theta;
  int x,y;
  double inva2=1./(a*a), invb2=1./(b*b);
  double cosPhi=cos(phiR), sinPhi=sin(phiR);
  double weightedArea=0;

  DoubleArray weights(maskArray.width(),maskArray.height());
  DoubleArray funcVals(maskArray.width(),maskArray.height());

  for(DoubleArray::iterator i=weights.begin();i!=weights.end();++i) {
    x=i.coord()(0)-M/2; y=i.coord()(1)-N/2;
    xP=x*cosPhi+y*sinPhi;
    yP=y*cosPhi-x*sinPhi;
    weights[i]= exp(-M_PI*(xP*xP*inva2+yP*yP*invb2));
    weightedArea+=weights[i];
  }

  //double maskSum=0;
  
  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i){
    x=i.coord()(0)-M/2; y=i.coord()(1)-N/2;
    r=sqrt(float(x*x+y*y));
    theta=atan2(float(y),float(x));
    
    funcVals[i]=cos(2.*omega*M_PI*r*cos(theta-phiR));
    maskArray[i]=weights[i]*funcVals[i];
    //   if(y==0)
    //   std::cout<<x<<" "<<y<<" "<<maskArray[i]<<std::endl;
    //maskSum+=maskArray[i];
  }
  

  /*double subNum=maskSum/weightedArea;
  //double tempSum=0;
  
  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i) {
    maskArray[i]=weights[i]*(funcVals[i]-subNum);
    //tempSum+=maskArray[i];
  }*/

}
/*
DoubleArray RealGF::scaleRGFVals(const DoubleArray& image, int a, int b) {
  std::cout<<"SCALING"<<std::endl;
  DoubleArray newImage(image.width(),image.height());

  double maxSum=0,minSum=0;
  double inva2=1./(double)(a*a);
  double invb2=1./(double)(b*b);
  double omega=1./(double)(2*a);
//  std::cout<<omega<<" "<<inva2<<std::endl;
  for(int y=-maskArray.height()/2;y<=maskArray.height()/2;y++) {
    for(int temp=-maskArray.width()/2;temp<=maskArray.width()/2;temp++) {
      double theta=atan2(y,temp);
      double r=sqrt(temp*temp+y*y);
      if(temp<-a/2 || temp>a/2) {
	minSum+=exp(-M_PI*(temp*temp*inva2+y*y*invb2))*cos(2.*omega*M_PI*r*cos(theta));
      }
      else
        maxSum+=exp(-M_PI*(temp*temp*inva2+y*y*invb2))*cos(2.*omega*M_PI*r*cos(theta));
    } 
  } 
  double subNum=(maxSum+minSum); 
  std::cout<<maxSum<<" "<<minSum<<"="<<subNum<<std::endl; 
  // std::cout<<subNum<<std::endl;
  for(DoubleArray::const_iterator i=image.begin(); i!=image.end();++i) { 
    //   if(i.coord()(0)==10 && i.coord()(1)==71)
    //  std::cout<<image[i.coord()]<<" "<<image[i.coord()]-subNum<<std::endl;
    //   if(image[i.coord()]>3)
    //  std::cout<<"LARGE: "<<i.coord()(0)<<" "<<i.coord()(1)<<" "<<image[i.coord()]<<std::endl;
    newImage[i.coord()]=fabs(subNum-image[i.coord()]);
  }   
  return newImage; 
}  
*/ 
/*
void RealGF::define(int a,int b, double phiIn) {
  maskArray.resize(ICoord(3*a,3*b));
  phi=phiIn;
  double phiR=phi*M_PI/180.; //phi in radians
  double omega=1./(double)(2.*a);
  double x,y,xP,yP,r,theta;
  double inva2=1./(a*a), invb2=1./(b*b);
  double cosPhi=cos(phiR), sinPhi=sin(phiR);

  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i){
    x=i.coord()(0)-M/2; y=i.coord()(1)-N/2;
    xP=x*cosPhi+y*sinPhi; yP=y*cosPhi-x*sinPhi;
    r=sqrt(x*x+y*y);
    theta=atan2(y,x);
    maskArray[i]=exp(-M_PI*(xP*xP*inva2 + yP*yP*invb2))*cos(2.*omega*M_PI*r*cos(theta-phiR));
  }
}*/
