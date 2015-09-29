// -*- C++ -*-
// $RCSfile: imageops.h,v $
// $Revision: 1.18 $
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


// Basic Image Operations

#include <oofconfig.h>

#ifndef IMAGEOPS_H
#define IMAGEOPS_H

class DoubleArray;
class BoolArray;
class IntArray;
#include "common/array.h"
class OOFImage;

DoubleArray spread(const DoubleArray&,double tolerance);
DoubleArray spread2(const DoubleArray&,double tolerance);

void setFromInt(OOFImage&,const IntArray&);
void setFromArray(OOFImage& colorImage,const DoubleArray& image);
BoolArray connecter(const DoubleArray& gabor, double initialThreshold,double threshDecrease,  int d,int numEdgeIter, int boxSize,bool trim);


DoubleArray scaleArray(const DoubleArray&, double min, double max,int lineColor); //Scales an array of doubles to fit between a min and max.
DoubleArray scaleArray2(const DoubleArray&, double min, double max);
DoubleArray scaleArray3(const DoubleArray&, double min, double max);

/****These functions apply the Gabor filters but don't modify the image***********/
DoubleArray realGabor(const DoubleArray&,int a,int b, double phi); //Applies the Real Gabor filter on an image.
DoubleArray imagGabor(const DoubleArray&,int a,int b, double phi); //Applies the Imaginary Gabor Filter on an image.
DoubleArray modGabor(const DoubleArray&,int a,int b, double phi); //Apples the modified Gabor Filter on an image.
DoubleArray normGabor(const DoubleArray&,int a,int b, double phi);
DoubleArray newGabor(const DoubleArray&,int a,int b, double phi);
/****************************************/

DoubleArray sobel(const DoubleArray&,int);
DoubleArray gaussSmooth(const DoubleArray&,double);
DoubleArray laplacian(const DoubleArray&);
DoubleArray laplacGauss(const DoubleArray&, double);
DoubleArray canny(const DoubleArray&, double);
//These functions apply the filter at a single angle and modify the image

void applyRealGaborAngle(OOFImage&,int,int,double);
void applyImagGaborAngle(OOFImage&,int,int,double);
void applyModGaborAngle(OOFImage&,int,int,double);

//These functions apply the filters at all angles (number is input by user) and modify the image
void applyRealGabor(OOFImage&,int,int,int,double);
void applyImagGabor(OOFImage&,int,int,int,double);
void applyModGabor(OOFImage&,int,int,int,double);
void applyGabor(OOFImage&,int,int,int,double,int);


//BoolArray threshold(const DoubleArray&,double tolerance); //Creates an array of bools after an image is thresholded.
//BoolArray closeImage(const BoolArray&,int);
//BoolArray skeletonizeImage(const BoolArray&);

DoubleArray findLargerVals(const DoubleArray&, const DoubleArray&);
DoubleArray findLargerVals2(const DoubleArray&,const DoubleArray&,IntArray&,int);
DoubleArray combineVals(const DoubleArray&, const DoubleArray&);
DoubleArray addNoise(const DoubleArray&, double);
#endif // IMAGEOPS_H
