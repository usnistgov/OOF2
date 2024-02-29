/*
Kevin Chang
August 26, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

imagemask.h

The class contained in this file provides helper functions for application of
the Gabor Wavelet Filter, for which the main functions are in gaborNugget.

Defines a class of image masks, rectangular arrays of values that can be
convoluted onto an image
*/

#ifndef IMAGEMASK_H
#define IMAGEMASK_H

class ImageMask;

#include "common/array.h"
#include "image/oofimage.h"
#include "image/imagemanip/grayimage.h"

#include <iostream.h>
#include <fstream.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

class ImageMask : public Array<double>
{
private:
  double mean;
  double weightedMean;
  double weightSum;
  Array<double> weight;
public:
  ImageMask();
  ImageMask(int w, int h);
  double getMaskValue(const grayImage &image, ICoord cc);
  void output();
  void define();
  grayImage applyMask(const grayImage &image, double n);
  grayImage applyMaskArray(const grayImage &image, double n);
  void loadMask(ifstream &file);
  void saveMask(ofstream &file);
  void makeRealGabor(double a, double b, double w, double phi);
  void makeImagGabor(double a, double b, double w, double phi);
};

#endif // IMAGEMASK_H
