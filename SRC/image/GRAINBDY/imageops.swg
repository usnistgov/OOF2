// -*- C++ -*-
// $RCSfile: imageops.swg,v $
// $Revision: 1.23 $
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

#ifndef IMAGEOPS_SWG
#define IMAGEOPS_SWG

%module imageops
%include "common/typemaps.swg"
%extern "common/doublearray.swg"
%pragma(python) code="from ooflib.SWIG.common.doublearray import DoubleArrayPtr"
%extern "common/boolarray.swg"
%pragma(python) code="from ooflib.SWIG.common.boolarray import BoolArrayPtr"
%extern "common/intarray.swg"
%pragma(python) code="from ooflib.SWIG.common.intarray import IntArrayPtr"
%{
#include "image/GRAINBDY/hough.h"
#include "image/GRAINBDY/imageops.h"
#include "image/SEGMENTATION/imageops.h"
#include "image/GRAINBDY/close.h"
#include "image/GRAINBDY/skeletonize.h"
#include "image/GRAINBDY/connectEdge.h"
#include "image/GRAINBDY/histogram.h"
#include "image/GRAINBDY/hysteresis.h"
#include "image/GRAINBDY/nonmaxSuppression.h"
#include "image/GRAINBDY/compare.h"
#include "common/doublearray.h"
#include "common/boolarray.h"
#include "common/intarray.h"
#include "image/oofimage.h"
#include "common/coord.h"
%}

DoubleArray spread(DoubleArray,double);
DoubleArray spread2(DoubleArray,double);
void setFromInt(OOFImage,IntArray);
void setFromArray(OOFImage& colorImage,const DoubleArray& image);
BoolArray connecter(const DoubleArray&, double,double,  int,int, int,bool);

DoubleArray scaleArray(DoubleArray, double, double,int);
DoubleArray scaleArray2(DoubleArray, double, double);
DoubleArray scaleArray3(DoubleArray, double, double);

DoubleArray realGabor(DoubleArray,int,int,double);
DoubleArray imagGabor(DoubleArray,int,int,double);
DoubleArray modGabor(DoubleArray,int,int,double);
DoubleArray normGabor(DoubleArray,int,int,double);
DoubleArray newGabor(DoubleArray,int,int,double);

DoubleArray sobel(DoubleArray,int);
DoubleArray gaussSmooth(DoubleArray,double);
DoubleArray laplacian(DoubleArray);
DoubleArray laplacGauss(DoubleArray,double);
DoubleArray canny(DoubleArray,double);
DoubleArray nonmaxSuppress(DoubleArray,IntArray);

void applyRealGaborAngle(OOFImage,int,int,double);
void applyImagGaborAngle(OOFImage,int,int,double);
void applyModGaborAngle(OOFImage,int,int,double);

void applyRealGabor(OOFImage,int,int,int,double);
void applyImagGabor(OOFImage,int,int,int,double);
void applyModGabor(OOFImage,int,int,int,double);
void applyGabor(OOFImage,int,int,int,double,int);

//BoolArray close(BoolArray,int);
//BoolArray skeletonize(BoolArray);
BoolArray connect(DoubleArray, double,double,int,int,int,bool);
DoubleArray findLargerVals(DoubleArray,DoubleArray);
DoubleArray findLargerVals2(DoubleArray,DoubleArray,IntArray,int);
DoubleArray combineVals(DoubleArray,DoubleArray);
DoubleArray addNoise(DoubleArray,double);
BoolArray hysteresisThresh(DoubleArray,double,double);
void printHistogram(DoubleArray,int);
void compare(BoolArray,int);

BoolArray houghTrans(BoolArray);
#endif // IMAGEOPS_SWG
