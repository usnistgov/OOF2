// -*- C++ -*-
// $RCSfile: newGabor.C,v $
// $Revision: 1.3 $
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

#include "newGabor.h"

#include <math.h>
#include "mask.h"
#include "common/array.h"
#include "common/doublearray.h"

NewGF::NewGF(int a, int b, double phi)
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
    xP=x*cosPhi+y*sinPhi; yP=y*cosPhi-x*sinPhi;
    weights[i]= exp(-M_PI*(xP*xP*inva2+yP*yP*invb2));
    weightedArea+=weights[i];
  }

  double maskSum=0;
  
  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i){
    x=i.coord()(0)-M/2; y=i.coord()(1)-N/2;
    r=sqrt(float(x*x+y*y));
    theta=atan2(float(y),float(x));
    
    funcVals[i]=cos(2.*omega*M_PI*r*cos(theta-phiR));
    maskArray[i]=weights[i]*funcVals[i];
    maskSum+=maskArray[i];
  }
  

  double subNum=maskSum/weightedArea;
  
  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i) {
    maskArray[i]=weights[i]*(funcVals[i]-subNum);
  }

}
