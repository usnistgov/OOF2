/*
Kevin Chang
August 26, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

gaborNugget.h

The class contained in this file is a self-contained unit that can apply the
Gabor Wavelet Filter to various types of images given the requisite inputs.
*/

#ifndef GABORNUGGET_H
#define GABORNUGGET_H

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

// #include "image.h"
#include "common/array.h"
#include "common/coord.h"
#include "image/imagemanip/imagemask.h"

/*----------*/

class gaborClass {
public:
  gaborClass(double ain, double bin, int nin);
  grayImage run(const grayImage & imagein);
private:
  double a;
  double b;
  int n;
  grayImage rawToImage(const grayImage &rawMaskedImage, double low, double high);
  grayImage getMax(grayImage image[], int numImages);
  grayImage applyRealGabor(int a, int b, const grayImage & image, int n);
  grayImage gabor(int a, int b, grayImage image, int n);
};

#endif // GABORNUGGET_H

/*----------*/
