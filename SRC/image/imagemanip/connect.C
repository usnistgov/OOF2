// -*- C++ -*-
// $RCSfile: connect.C,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:38 $

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
September 16, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

connect.C

This file contains a function called by Python via SWIG to begin the connection function.
*/

#include <oofconfig.h>

#include "image/oofimage.h"
#include <iostream>
#include "image/imagemanip/grayimage.h"
#include "image/imagemanip/bwimage.h"
#include "bwimage.h"
#include "convertNugget.h"
#include "gaborNugget.h"
#include "closeNugget.h"
#include "skeletonNugget.h"
#include "connectNugget.h"

void makeConnected(OOFImage &image, double a, double b, int n, int t, int d, int numEdgeIter, int boxSize, bool trim) {
  grayImage gi = oof2gray(image);
  ///  gaborClass gn(a,b,n);
  ///  gi = gn.run(gi);
  BWImage bwi = gray2bin(gi, t);
  ///  closeClass cln(d);
  ///  bwi = cln.run(bwi);

  ///  int w = bwi.width();
  ///  int h = bwi.height();  
  /////  BWImage bwi2(w,h);
  /////  BWImage skeli(w,h);

  /////  for (int a = 0; a < w; a++)
  /////    for (int b = 0; b < h; b++)
  /////      bwi2[ICoord(a,b)] = bwi[ICoord(a,b)];

  ///  skeletonClass sn = skeletonClass();
  ///  skeli = sn.run(bwi2);

  /////  cout << "pre-wh" << endl;

  /////  w = skeli.width();
  /////  h = skeli.height();  

  /////  cout << "pre-bwi3" << endl;

  /////  BWImage bwi3(w,h);

  /////  cout << "bwi3 created" << endl;

  /////  for (int c = 0; c < w; c++)
  /////    for (int d = 0; d < h; d++)
  /////      bwi3[ICoord(c,d)] = skeli[ICoord(c,d)];

  /////  cout << "bwi3 initialized" << endl;

  connectClass con = connectClass();

  cout << "con created" << endl;

  //////////  bwi3 = con.run(bwi3, t, d, numEdgeIter, boxSize, trim);
  bwi = con.run(bwi, t, d, numEdgeIter, boxSize, trim);

  cout << "connected" << endl;

  //////////  gi = bin2gray(bwi3);
  gi = bin2gray(bwi);

  image.set(gi, &dbl2color);
  image.imageChanged();
}
