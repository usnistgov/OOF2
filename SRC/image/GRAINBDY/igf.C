// -*- C++ -*-
// $RCSfile: igf.C,v $
// $Revision: 1.6 $
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

#include "igf.h"

#include <math.h>
#include "mask.h"
#include "common/array.h"
#include "common/doublearray.h"

ImagGF::ImagGF(int a, int b, double phi)
  : MASK(3*b,3*b) {
//This constructor defines the values in the mask using the equation for the
//Imaginary Gabor Filter.
  int M=maskArray.width(), N=maskArray.height();
  double phiR=phi*M_PI/180.; //phi in radians
  double omega=1./(double)(2.*a);
  double xP,yP,r,theta;
  int x,y;
  double inva2=1./(a*a), invb2=1./(b*b);
  double cosPhi=cos(phiR), sinPhi=sin(phiR);

  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i){
    x=i.coord()(0)-M/2; y=i.coord()(1)-N/2;
    xP=x*cosPhi+y*sinPhi; yP=y*cosPhi-x*sinPhi;
    r=sqrt(float(x*x+y*y));
    theta=atan2(float(y),float(x));
    maskArray[i]=exp(-M_PI*(xP*xP*inva2 + yP*yP*invb2))*sin(2.*omega*M_PI*r*cos(theta-phiR));

    //std::cerr<<maskArray[i]<<" ";
    //if(i.coord()(0)==maskArray.width()-1)
      //    std::cerr<<endl;
  }
  //std::cerr<<endl<<endl;
}
/*
void ImagGF::define(int a,int b,double phiIn) {
  maskArray.resize(ICoord(3*a,3*b));
  phi=phiIn;
  double omega=1/(double)(2.*a);
  
  double x,y,xP,yP,r,theta;
  for(DoubleArray::iterator i=maskArray.begin(); i!=maskArray.end();++i){
    x=i.coord()(0); y=i.coord()(1);
    xP=x*cos(phi)+y*sin(phi); yP=y*cos(phi)-x*sin(phi);
    r=sqrt(x*x+y*y);
    theta=atan2(y,x);
    maskArray[i]=exp(-M_PI*(xP*xP/a/a + yP*yP/b/b))*sin(2.*omega*M_PI*r*cos(theta-phi));
  }  
}
*/
