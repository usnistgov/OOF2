// -*- C++ -*-
// $RCSfile: gray.C,v $
// $Revision: 1.4 $
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

gray.C

This file contains a function called by Python via SWIG to begin the OOF to grayscale conversion.
*/

#include <oofconfig.h>

#include "image/oofimage.h"
#include <iostream>
#include "convertNugget.h"

void makeGray(OOFImage &image) {
  grayImage gi = oof2gray(image);
  image.set(gi, &dbl2color);
  image.imageChanged();
}
