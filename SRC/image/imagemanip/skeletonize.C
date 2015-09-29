/*
Kevin Chang
August 27, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

skeletonize.C

This file contains a function called by Python via SWIG to begin the skeletonization function.
*/

#include <oofconfig.h>

#include "image/oofimage.h"
#include "image/imagemanip/grayimage.h"
#include "image/imagemanip/bwimage.h"
#include <iostream>
#include "convertNugget.h"
#include "gaborNugget.h"
#include "skeletonNugget.h"
#include "bwimage.h"

void makeSkel(OOFImage &image, double a, double b, int n, int t) {
  grayImage gi = oof2gray(image);
  BWImage bwi = gray2bin(gi, t);
  skeletonClass sn = skeletonClass();
  //  skeletonClass sn();
  bwi = sn.run(bwi);
  gi = bin2gray(bwi);
  image.set(gi, &dbl2color);
  image.imageChanged();
}
