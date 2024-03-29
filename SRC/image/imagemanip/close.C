// -*- C++ -*-

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
September 4, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

close.C

This file contains a function called by Python via SWIG to begin the closing function.
*/

#include <oofconfig.h>

#include "image/oofimage.h"
#include <iostream>
#include "convertNugget.h"
#include "gaborNugget.h"
#include "closeNugget.h"

void makeClosed(OOFImage &image, double a, double b, int n, int t, int d) {
  grayImage gi = oof2gray(image);
  gaborClass gn(a,b,n);
  gi = gn.run(gi);
  BWImage bwi = gray2bin(gi, t);
  closeClass cn(d);
  bwi = cn.run(bwi);
  gi = bin2gray(bwi);
  image.set(gi, &dbl2color);
  image.imageChanged();
}
