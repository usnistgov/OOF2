// -*- C++ -*-
// $RCSfile: imageops.C,v $
// $Revision: 1.25 $
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
#include "imageops.h"
#include <iostream>
#include <math.h>

#include "image/oofimage.h" //This is where threshold is located
//#include "image/GRAINBDY/close.h"
//#include "image/GRAINBDY/skeletonize.h"
#include "image/oofimage.h"
#include "common/array.h"
#include "common/doublearray.h"
#include "common/boolarray.h"
#include "common/intarray.h"
#include "image/GRAINBDY/close.h"
#include "image/GRAINBDY/skeletonize.h"
#include "image/GRAINBDY/rgf.h"
#include "image/GRAINBDY/igf.h"
#include "image/GRAINBDY/newGabor.h"
#include "image/GRAINBDY/modifiedGabor.h"
#include "image/GRAINBDY/sobel.h"
#include "image/GRAINBDY/gaussSmooth.h"
#include "image/GRAINBDY/laplacian.h"
#include "image/GRAINBDY/laplacianGauss.h"
#include "image/GRAINBDY/nonmaxSuppression.h"
#include "image/GRAINBDY/connectEdge.h"
#include "common/random.h"
#include "image/oofimage.h"

// DoubleArray grayify(const OOFImage& image) {
// //Creates a gray image from a color image.
//   return image.convert(color2gray);
// }

DoubleArray spread(const DoubleArray& image1,double tolerance) {
  double color;  // The color of the current pixel
  int w = image1.width();  // Image width
  int h = image1.height();  // Image height
  DoubleArray newimage(w, h);  // Copies the image from the passed in (image1) to the function's image (image)
  for (DoubleArray::const_iterator i = image1.begin(); i != image1.end(); ++i) {  // For width
    if (image1[i]<=tolerance) // If cell is under tolerance,
      color = 0;  // Make low pixels black
    else
      color = (image1[i]-tolerance)/tolerance; // Make high pixels white
    newimage[i.coord()] = color;  // Cell takes new color as set above	
  }
  
  return newimage;
}

DoubleArray spread2(const DoubleArray& image1,double tolerance) {
  //double color;  // The color of the current pixel
//   int w = image1.width();  // Image width
//   int h = image1.height();  // Image height
  DoubleArray newimage(image1.size(),0.0);  // Copies the image from the passed in (image1) to the function's image (image)

  double minArr=100000., maxArr=0.;
  for (DoubleArray::const_iterator i = image1.begin(); i != image1.end(); ++i) {  // For width
    if (image1[i]>=tolerance) // If cell is over tolerance,
      newimage[i.coord()]=1;  // Make pixels white
    else {
      if(image1[i]<minArr)
	minArr=image1[i];
      else if(image1[i]>maxArr)
	maxArr=image1[i];
    }
  }
  double scaleFactor=.8/(maxArr-minArr);
  double shift=.8-maxArr*scaleFactor;
  
  for(DoubleArray::const_iterator j=image1.begin();j!=image1.end();++j) {
    if(newimage[j]<1)
      newimage[j.coord()]=image1[j]*scaleFactor+shift;
  }
  return newimage;
}


void setFromInt(OOFImage& colorImage,const IntArray& image) {
//Creates a color image from an array of doubles.
  colorImage.set(image,int2color);
}

void setFromArray1(OOFImage& colorImage,const DoubleArray& image) {
//Creates a color image from an array of doubles.
  colorImage.set(image,gray2color);
}


DoubleArray scaleArray(const DoubleArray& arr, double min, double max,int lineColor) {
//Scales the double values from applying a filter into values between the min
//and the max.
  double minArr=999999, maxArr=-999999;

  for(DoubleArray::const_iterator i=arr.begin();i!=arr.end();++i) {
    double val=0.;
    if(lineColor==2)//Detect both white and dark colored lines.
      val=fabs(arr[i]);
    else if(lineColor==1)//Detect only white lines.
      val=arr[i];
    else if(lineColor==0)//Detect only dark lines.
      val=-arr[i];
      
    if(val<minArr)
      minArr=val;
    if(val>maxArr)
      maxArr=val;
  }
  if(lineColor!=2)
    minArr=0;
  double scaleFactor=(max-min)/(maxArr-minArr);
  double shift=max-maxArr*scaleFactor;
  DoubleArray newArr(arr.width(),arr.height());
  for(DoubleArray::const_iterator j=arr.begin();j!=arr.end();++j) {
    if(lineColor==2)
      newArr[j.coord()]=fabs(arr[j])*scaleFactor+shift;
    else if(lineColor==1) {
      if(arr[j]>0)
	newArr[j.coord()]=arr[j]*scaleFactor+shift;
      else
	newArr[j.coord()]=0;
    }
    else {
      if(arr[j]<0)
	newArr[j.coord()]=-arr[j]*scaleFactor+shift;
      else
	newArr[j.coord()]=0;
    }
  }
  return newArr;    
}

DoubleArray scaleArray2(const DoubleArray& arr, double min, double max) {
//Scales the absolute values of double values into values between the min
//and the max.
  double minArr=999999, maxArr=-999999;
  for(DoubleArray::const_iterator i=arr.begin();i!=arr.end();++i) {
    if(fabs(arr[i])<minArr)
      minArr=fabs(arr[i]);
    if(fabs(arr[i])>maxArr)
      maxArr=fabs(arr[i]);
  }
  double scaleFactor=(max-min)/(maxArr-minArr);
  double shift=max-maxArr*scaleFactor;
  DoubleArray newArr(arr.width(),arr.height());
  for(DoubleArray::const_iterator j=arr.begin();j!=arr.end();++j) {
    newArr[j.coord()]=fabs(arr[j])*scaleFactor+shift;
  }
  return newArr;    
}

DoubleArray scaleArray3(const DoubleArray& arr, double min, double max) {
//Scales the double values into values between the min
//and the max.
  double minArr=999999, maxArr=-999999;
  for(DoubleArray::const_iterator i=arr.begin();i!=arr.end();++i) {
    if(arr[i]<minArr)
      minArr=arr[i];
    if(arr[i]>maxArr)
      maxArr=arr[i];
  }
  double scaleFactor=(max-min)/(maxArr-minArr);
  double shift=max-maxArr*scaleFactor;
  DoubleArray newArr(arr.width(),arr.height());
  for(DoubleArray::const_iterator j=arr.begin();j!=arr.end();++j) {
    newArr[j.coord()]=arr[j]*scaleFactor+shift;
  }
  return newArr;    
}

DoubleArray realGabor(const DoubleArray& image,int a,int b, double phi) {
//Applies the Real Gabor Filter to an image and returns raw data.
  RealGF realGaborMask(a,b,phi);
  return realGaborMask.applyMask(image);
//  DoubleArray temp(image.width(),image.height());
//  temp=realGaborMask.applyMask(image);
//  return realGaborMask.scaleRGFVals(temp,a,b);
}

DoubleArray imagGabor(const DoubleArray& image,int a,int b,double phi) {
//Applies the Imaginary Gabor Filter to an image and returns raw data.
  ImagGF imagGaborMask(a,b,phi);
  return imagGaborMask.applyMask(image);
}

DoubleArray modGabor(const DoubleArray& image, int a,int b,double phi) {
//Applies the modified Gabor Filter to an image and returns raw data.
  ModGabor modGaborMask(a,b,phi);
  return modGaborMask./*setImage(image)*/applyMask(image);
}

DoubleArray normGabor(const DoubleArray& image, int a,int b,double phi) {
//Using the results from the real and imaginary gabor filters, this function combines the two raw values into one image.
  DoubleArray arr1=realGabor(image,a,b,phi);
  DoubleArray arr2=imagGabor(image,a,b,phi);

  DoubleArray combined(arr1.width(),arr1.height());
  for(DoubleArray::iterator i=arr1.begin(); i!=arr1.end(); ++i) {
  //    if(arr1[i]>4.16786)
  //    cout<<arr1[i]<<" "<<i.coord()(0)<<","<<i.coord()(1)<<endl;
    combined[i.coord()]=sqrt(arr1[i]*arr1[i]+arr2[i]*arr2[i]);
    //  if(i.coord()(0)==14 && i.coord()(1)==64)
    //   cout<<arr1[i]<<" "<<combined[i.coord()]<<endl;
    //std::cout<<combined[i.coord()]<<" ";
  }
  // std::cout<<std::endl;
  
  return combined;
}

DoubleArray newGabor(const DoubleArray& image,int a,int b,double phi) {
//Applies the Imaginary Gabor Filter to an image and returns raw data.
  NewGF newGaborMask(a,b,phi);
  return newGaborMask.applyMask(image);
}

DoubleArray sobel(const DoubleArray& image,int dir) {
  Sobel sobelMask(dir);
  return sobelMask.applyMask(image);
}

DoubleArray canny(const DoubleArray& image, double stdDev) {
  DoubleArray smoothed = gaussSmooth(image,stdDev);
  
  DoubleArray temp(image.size(),0.0);
  DoubleArray final(image.size(),0.0);
  IntArray gradDirs(image.size(),0);
  final=sobel(image,0);
  for(int a=1;a<4;a++) {
    temp = sobel(image,a);
    final=findLargerVals2(final,temp,gradDirs,a);
  }
  //final=nonmaxSuppress(final,gradDirs);
  return final;
}

DoubleArray gaussSmooth(const DoubleArray& image,double stdDev) {
  GaussSmooth gaussMask(stdDev);
  return gaussMask.applyMask(image);

}

DoubleArray laplacian(const DoubleArray& image) {
  Laplacian laplacianMask;
  return laplacianMask.applyMask(image);
}

DoubleArray laplacGauss(const DoubleArray& image, double stdDev) {
  LaplacianGauss lapGaussMask(stdDev);
  return lapGaussMask.applyMask(image);
}

void applyRealGaborAngle(OOFImage& image, int a,int b, double phi)
{//Applies the real Gabor filter at a given angle. 
   DoubleArray dbls(image.sizeInPixels(),0.0);
   dbls = grayify(image);
   dbls = realGabor(dbls,a,b,phi);
 //   dbls = scaleArray(dbls,0.0,1.0);
   dbls = scaleArray2(dbls,0.0,1.0);
   setFromArray1(image,dbls);
}

void applyImagGaborAngle(OOFImage& image, int a,int b, double phi)
{//Applies the imaginary Gabor filter at a given angle.  
   DoubleArray dbls(image.sizeInPixels(),0.0);
   dbls = grayify(image);
   dbls = imagGabor(dbls,a,b,phi);
   dbls = scaleArray2(dbls,0.0,1.0);
   setFromArray1(image,dbls);
}

void applyModGaborAngle(OOFImage& image, int a,int b, double phi)
{//Applies the modified gabor filter at a given angle. 
   DoubleArray dbls(image.sizeInPixels(),0.0);
   dbls = grayify(image);
   dbls = modGabor(dbls,a,b,phi);
   dbls = scaleArray2(dbls,0.0,1.0);
   setFromArray1(image,dbls);
}

void applyRealGabor(OOFImage& image,int a,int b,int numAngles, double T)
{
   DoubleArray dbls(image.sizeInPixels(),0.0);
   BoolArray bools(image.sizeInPixels(),false);
   DoubleArray old(image.sizeInPixels(),0.0);
   DoubleArray temp=grayify(image);

   for(int c=0;c<numAngles;c++) {
     double phi=180./numAngles*(double) c;
     dbls = realGabor(temp,a,b,phi);
     if(c!=0) {
       old=findLargerVals(dbls,old);
     }
     else
       old=dbls;
   }
   dbls = scaleArray2(old,0.0,1.0);
   bools = threshold(dbls,T);
   setFromBool(image,bools);  
}

void applyImagGabor(OOFImage& image,int a,int b,int numAngles, double T)
{
   DoubleArray dbls(image.sizeInPixels(),0.0);
   BoolArray bools(image.sizeInPixels(),false);
   DoubleArray old(image.sizeInPixels(),0.0);
   DoubleArray temp=grayify(image);

   for(int c=0;c<numAngles;c++) {
     double phi=180./numAngles*(double) c;
     dbls = imagGabor(temp,a,b,phi);
     if(c!=0) {
       old=findLargerVals(dbls,old);
     }
     else
       old=dbls;
   }
   dbls = scaleArray2(old,0.0,1.0);
   setFromArray1(image,dbls);
   bools = threshold(dbls,T);
   setFromBool(image,bools);  
}

void applyModGabor(OOFImage& image,int a,int b,int numAngles, double T)
{
   DoubleArray dbls(image.sizeInPixels(),0.0);
   BoolArray bools(image.sizeInPixels(),false);
   DoubleArray old(image.sizeInPixels(),0.0);
   DoubleArray temp=grayify(image);

   for(int c=0;c<numAngles;c++) {
     double phi=180./numAngles*(double) c;
     dbls = modGabor(temp,a,b,phi);
     if(c!=0) {
       old=findLargerVals(dbls,old);
     }
     else
       old=dbls;
   }
   dbls = scaleArray2(old,0.0,1.0);
   bools = threshold(dbls,T);
   setFromBool(image,bools);  
}

void applyGabor(OOFImage& image,int a,int b,int numAngles, double T,int lineClr)
{//Combination of the real and imaginary gabor filters.
   DoubleArray real(image.sizeInPixels(),0.0);
   DoubleArray imag(image.sizeInPixels(),0.0);
   DoubleArray old(image.sizeInPixels(),0.0);

   BoolArray bools(image.sizeInPixels(),false);
   DoubleArray temp=grayify(image);

   for(int c=0;c<numAngles;c++) {
     double phi=180./numAngles*(double) c;
     real = realGabor(temp,a,b,phi);
     imag = imagGabor(temp,a,b,phi);
     if(c!=0) {
       old=findLargerVals(real,old);
       old=findLargerVals(imag,old);
     }
     else
       old=findLargerVals(real,imag);
   }
   old = scaleArray(old,0.0,1.0,lineClr);
   bools = threshold(old,T);
   setFromBool(image,bools);  
}

/*BoolArray  closeImage(const BoolArray& image,int n) {
  CloserClass cl = CloserClass();
  return cl.close(image,n);
}

BoolArray skeletonizeImage(const BoolArray& image) {
  Skeletonizing skel = Skeletonizing();
  return skel.skeletonize(image);
}*/



BoolArray connecter(const DoubleArray& gabor, double initialThreshold,double threshDecrease,  int d,int numEdgeIter, int boxSize,bool trim) {
	return connect(gabor, initialThreshold, threshDecrease, d, numEdgeIter, boxSize, trim);
}

DoubleArray findLargerVals(const DoubleArray &arr1, const DoubleArray &arr2) {
  //Both arrays must be the same size, or it will go out of bounds.
  DoubleArray newArr(arr1.width(),arr1.height());
  for(DoubleArray::const_iterator i=arr1.begin(); i!=arr1.end(); ++i) {
    if(fabs(arr1[i])>=fabs(arr2[i]))
      newArr[i.coord()]=arr1[i];
    else
      newArr[i.coord()]=arr2[i];
  }
  return newArr;
}

DoubleArray findLargerVals2(const DoubleArray &arr1, const DoubleArray &arr2,
			   IntArray& gradDirs, int curDir) {
  DoubleArray newArr(arr1.width(),arr1.height());
  for(DoubleArray::const_iterator i=arr1.begin(); i!=arr1.end(); ++i) {
    if(fabs(arr1[i])>=fabs(arr2[i]))
      newArr[i.coord()]=arr1[i];
    else {
      newArr[i.coord()]=arr2[i];
      gradDirs[i.coord()]=curDir;
    }
  }
  return newArr;
}

DoubleArray combineVals(const DoubleArray &arr1, const DoubleArray &arr2) {
  //Both arrays must be the same size, or it will go out of bounds.
  DoubleArray newArr(arr1.width(),arr1.height());
  for(DoubleArray::const_iterator i=arr1.begin(); i!=arr1.end(); ++i) {
    newArr[i.coord()]=fabs(arr1[i])+fabs(arr2[i]);
  }
  return newArr;
}

DoubleArray addNoise(const DoubleArray& image, double s) {
  DoubleArray final(image.width(),image.height());
  // rndmseed(1);

  for(DoubleArray::const_iterator i=image.begin(); i!=image.end(); ++i) {
    final[i.coord()]=image[i]+s*gasdev();
    if(final[i]>1)
      final[i.coord()]=1;
    else if(final[i]<0)
      final[i.coord()]=0;
  }
  return final;
}


