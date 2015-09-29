/*
Kevin Chang
September 4, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

closeNugget.h

Self-contianed image closing nugget.
*/

#ifndef CLOSENUGGET_H
#define CLOSENUGGET_H

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "common/array.h"
#include "common/coord.h"
#include "image/imagemanip/imagemask.h"
#include "bwimage.h"

/*----------*/

class closeClass {
public:
  closeClass();
  closeClass(int din);
  BWImage run(const BWImage& imagein);
private:
  int d;
  BWImage close(BWImage image, int n);
  BWImage dilate(const BWImage& image, const grayImage& se);
  BWImage erode(const BWImage& image, const grayImage& se);
};

/*----------*/

#endif // CLOSENUGGET_H
