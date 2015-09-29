// -*- C++ -*-
// $RCSfile: imageops.swg,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:41:35 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef IMAGEOPSESE_SWG
#define IMAGEOPSESE_SWG

%module imageops
%include "common/typemaps.swg"
%include "common/typemaps.swg"
%extern "common/doublearray.swg"
%pragma(python) code="from oof2.SWIG.common.doublearray import DoubleArrayPtr"
%extern "common/boolarray.swg"
%pragma(python) code="from oof2.SWIG.common.boolarray import BoolArrayPtr"
%extern "common/intarray.swg"
%pragma(python) code="from oof2.SWIG.common.intarray import IntArrayPtr"
%{
#include "image/SEGMENTATION/imageops.h"
#include "common/doublearray.h"
#include "common/boolarray.h"
#include "common/intarray.h"
#include "image/oofimage.h"
#include "common/coord.h"
%}

void setFromArray(OOFImage,DoubleArray);
DoubleArray arrayFromImage(OOFImage);
DoubleArray mountThresholdedImageOnOldImage(DoubleArray, DoubleArray);
void drawFixerLines(DoubleArray, int, int, int, int, int);
DoubleArray normalizeImage(DoubleArray);
void expand(int, DoubleArray, int);
void shrink(DoubleArray, int);
void setFromBoolArray(OOFImage& colorImage,const BoolArray& image);
#endif 
