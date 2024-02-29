/*
Kevin Chang
August 27, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

skeletonNugget.h

The class contained in this file is a self-contained unit that can apply a
skeletonization algorithm to a Gabor-ized image.
*/

#ifndef SKELETONNUGGET_H
#define SKELETONNUGGET_H

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "common/array.h"
#include "common/coord.h"
#include "image/imagemanip/imagemask.h"
#include "bwimage.h"

/*----------*/

class skeletonClass {
public: 
  skeletonClass();
  BWImage run(const BWImage & imagein);
private:
  bool isContour(const BWImage &image,ICoord pt);
  bool isDeletable(const BWImage &image,ICoord pt);
  bool satisfiesStep1(const BWImage &image, ICoord pt);
  bool satisfiesStep2(const BWImage &image, ICoord pt);
  BWImage skeletonize(const BWImage &image);
};

/*----------*/

#endif // SKELETONNUGGET_H
