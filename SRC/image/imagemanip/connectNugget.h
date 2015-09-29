/*
Kevin Chang
September 16, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

connectNugget.h

Self-contianed line connection nugget.
*/

#ifndef CONNECTNUGGET_H
#define CONNECTNUGGET_H

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "common/array.h"
#include "common/coord.h"
#include "image/imagemanip/imagemask.h"
#include "bwimage.h"
#include "skeletonNugget.h"
#include "closeNugget.h"

/*----------*/

class connectClass {
public:
  connectClass();
  BWImage run(const BWImage & imagein, int i, int d, int nei, int bs, bool trim);
private:
  int t;
  int d;
  BWImage imagein;
  //  int lineConnect;
  BWImage connectClass::connect(const BWImage & gabor, int t, int d, int numEdgeIter, int boxSize, bool trim);
  bool isDiscontinuous(const BWImage &image, const ICoord pt);
  BWImage getAndReduceDiscontinuities (BWImage connected1, const BWImage newThresh, int d, int boxSize);
  BWImage removeDeadLines(const BWImage & connected);
};

/*----------*/

#endif // CONNECTNUGGET_H
