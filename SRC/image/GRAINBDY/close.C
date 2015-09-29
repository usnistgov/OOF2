// -*- C++ -*-
// $RCSfile: close.C,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:41:28 $

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
#include <iostream>
#include "close.h"
#include "image/oofimage.h"
#include "common/array.h"
#include "common/doublearray.h"
#include "common/boolarray.h"

BoolArray dilate(const BoolArray & image, const DoubleArray & pattern) {
  // cout<<"DILATING"<<endl;
  int sw=pattern.width();
  int sh=pattern.height();
  BoolArray temp=image.clone();

  for(BoolArray::const_iterator i=image.begin(); i!=image.end(); ++i) {
    if(image[i.coord()]==0) {
      bool match=false;
      //for(int a=-sw/2;a<=sw/2 && !match;a++) {
      //for (int b=-sh/2;b<=sh/2 && !match ;b++) {
      for(DoubleArray::const_iterator j=pattern.begin(); j!=pattern.end() && !match; ++j) {
	//	  cout<<a+sw/2<<","<<b+sh/2<<" "<<i.coord()(0)+a<<","<<i.coord()(1)+b<<endl;
	if (pattern[j.coord()]!=-1) {
	  //if it is a white pixel
	  // int x=i.coord()(0)+a, y=i.coord()(1)+b;
	  if(image.contains(i.coord()+j.coord()-ICoord(sw/2,sh/2)) && image[i.coord()+j.coord()-ICoord(sw/2,sh/2)]!=0) {
	    match=true;
	    temp[i.coord()]=1;
	  }
	}	
      }
    }
  }
  
//cout<<"dilated"<<endl;
  return temp;
}

BoolArray erode(const BoolArray & image, const DoubleArray & pattern) {
  //cout<<"ERODING"<<endl;
  int sw=pattern.width();
  int sh=pattern.height();
  BoolArray temp=image.clone();
  
  for(BoolArray::const_iterator i=image.begin(); i!=image.end(); ++i) {
    if(image[i.coord()]==1) {
    //std::cerr<<"WORKING"<<endl;
      bool match=false;
    //  for (int a=-sw/2;a<=sw/2 && !match;a++) {
    //	for (int b=-sh/2;b<=sh/2 && !match ;b++) {
      for(DoubleArray::const_iterator j=pattern.begin(); j!=pattern.end() && !match; ++j) {
	if (pattern[j.coord()]!=-1) {
	    //	if is a black pixel
	  //int x=i.coord()(0)+a, y=i.coord()(1)+b;
	  if (image.contains(i.coord()+j.coord()-ICoord(sw/2,sh/2)) && image[i.coord()+j.coord()-ICoord(sw/2,sh/2)]==0) {
	    match=true;
	    temp[i.coord()]=0;
	  } 
	}
      }
    }
  }
  //cout<<"eroded"<<endl;
  return temp;
}

BoolArray close(const BoolArray& image,int n) {
//This sets the pattern used in erode and dilate to a diamond shape.
  if(n%2==0)
    n++;
  DoubleArray pattern(n,n);
  for(DoubleArray::iterator i=pattern.begin(); i!=pattern.end(); ++i) {
    pattern[i.coord()]=-1; 
  }
  
  for (int c=0;c<=n/2;c++) {
    for (int d=n/2-c;d<=n/2+c;d++) {
      pattern[ICoord(c,d)]=0;
      pattern[ICoord(n-1-c,d)]=0;
    }
  }
  
//   for (int e=0;e<n;e++) {
//     for (int f=0;f<n;f++) {
//       cout<<pattern[ICoord(e,f)]<<" ";
//     }
//     cout<<endl;
//   }
  return erode(dilate(image,pattern),pattern);

}
