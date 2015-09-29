// -*- C++ -*-
// $RCSfile: convertNugget.C,v $
// $Revision: 1.4 $
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
August 26, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

convertNugget.C

All image conversion functions are located within this file
*/

#include "convertNugget.h"

/*----------*/

BWImage gray2bin(const grayImage &image1, int tolerance) {
// This function converts a grayscale image to binary (black/white).  Any value above the tolerance
// value (passed in) is changed to white and any value under the tolerance is change to black.

  int color;  // The color of the current pixel
  int w = image1.width();  // Image width
  int h = image1.height();  // Image height
  BWImage newimage(w, h);  // Copies the image from the passed in (image1) to the function's image (image)
  for (int i = 0; i < w; i++) {  // For width
    for (int j = 0; j < h; j++) {  // For height (with above, array loop)
	if (image1[ICoord(i,j)] < (tolerance / 256.)) // If cell is under tolerance,
	    color = false;  // Make low pixels black
	else
	    color = true; // Make high pixels white

	newimage[ICoord(i,j)] = color;  // Cell takes new color as set above
    }
  }
  cout << "Image converted to binary." << endl;
  return newimage;
}

/*----------*/

grayImage bin2gray(const BWImage &image1) {
// This function converts a black and white (binary) image to grayscale
// It basically switches from a boolarray to an array<double>

  int w1 = image1.width();
  int h1 = image1.height();
  grayImage newimage(w1, h1);
  for (int x = 0; x < w1; x++)
    for(int y = 0; y < h1; y++)
      if(image1[ICoord(x,y)] == true)
	newimage[ICoord(x,y)] = 1.;
      else
	newimage[ICoord(x,y)] = 0.;
  cout << "Image converted to grayscale." << endl;
  return newimage;
}

/*----------*/

CColor dbl2color(double dbl) {
  CColor newcolor(dbl, dbl, dbl);
  return newcolor;
}

/*----------*/

double color2dbl(const CColor &color) {
  return color.gray();
}

/*----------*/

grayImage oof2gray(const OOFImage &image1) {
  grayImage newimage;
  newimage = image1.convert(color2dbl);
  return newimage;
}

/*----------*/

BWImage oof2bin(const OOFImage &image1) {
  grayImage intermediate;
  BWImage final;
  intermediate = oof2gray(image1);
  final = gray2bin(intermediate, 127);
  return final;
}

/*----------*/
