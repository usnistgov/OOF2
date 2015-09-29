// -*- C++ -*-
// $RCSfile: convertNugget.h,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:39 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

/*
Kevin Chang
August 26, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

convertNugget.h

This file contains functions used to manipulate an image between
various types, including bwImage (binary), grayImage (monochrome),
and OOFImage (color).
*/

#include <oofconfig.h>

#ifndef CONVERTNUGGET_H
#define CONVERTNUGGET_H

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "image/oofimage.h"
#include "common/array.h"

#include "common/coord.h"
#include "imagemask.h"

#include "grayimage.h"
#include "bwimage.h"

BWImage gray2bin(const grayImage &image1, int tolerance);
grayImage bin2gray(const BWImage &image1);
// OOFImage gray2oof(const grayImage &image1);
grayImage oof2gray(const OOFImage &image1);
// OOFImage bin2oof(const BWImage &image1);
BWImage oof2bin(const OOFImage &image1);
double color2dbl(const CColor &color);
CColor dbl2color(double dbl);

#endif // CONVERTNUGGET_H
