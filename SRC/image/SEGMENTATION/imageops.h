// -*- C++ -*-
// $RCSfile: imageops.h,v $
// $Revision: 1.6 $
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


// Basic Image Operations

#include <oofconfig.h>
#include "common/doublearray.h"
#include "image/oofimage.h"
#include "common/boolarray.h"

#ifndef IMAGEOP_H
#define IMAGEOP_H

/*
Groups together a bunch of operations performed on an image that do not need to be attached to a class. Might be better organized in the future.
All are further explained in the .C file.
*/

class DoubleArray;
class BoolArray;
class IntArray;
class OOFImage;
void setFromArray(OOFImage&,const DoubleArray&); //Creates a color image from an array of doubles
void setFromBoolArray(OOFImage& colorImage,const BoolArray& image);
DoubleArray arrayFromImage(OOFImage&);
static double togray(const CColor &color){ return color.getRed()*.2 + color.getGreen()*.5 + color.getBlue()*.3;};
DoubleArray mountThresholdedImageOnOldImage(DoubleArray gray, DoubleArray newgray);
void drawFixerLines(DoubleArray &gray, int x0, int y0, int x1, int y1, int color);
bool pixelInBounds(ICoord pxl, ICoord size);
DoubleArray normalizeImage(DoubleArray original);
void expand(int range, DoubleArray & image, int color);
void shrink(DoubleArray & image, int color);

#endif // IMAGEOPS_H

