/*
Kevin Chang
September 4, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

dilateNugget.C

Self-contianed dilation nugget.
 */
#include "image.h"
#include "common/array.h"

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "common/coord.h"
#include "imagemask.h"

/*----------*/

class dilateClass {
public:
  dilateClass(int din, const grayImage& sein);
  BWImage run(const BWImage & imagein);
private:
  int d;
  const grayImage se;  // Structuring element
  BWImage dilate(const BWImage & image, const grayImage & se);
};

/*----------*/

dilateClass::dilateClass(int din, const grayImage& sein) {
  d = din;
  for(grayImage::iterator i = array.begin(); i != array.end(); i++)
    se[i] = sein[i];
}

/*----------*/

BWImage dilateClass::run(const BWImage & imagein) {
  BWImage image;
  image = imagein;

  dilate(image, se);

  return image;
}

/*----------*/

BWImage dilateClass::dilate(const BWImage & image, const grayImage & se) {  // Opposite of erode.  Adds pixels to an area.  Background erodes.
  int w = image.query_width();
  int h = image.query_height();
  int sw = se.query_width();
  int sh = se.query_height();
  BWImage temp = image;

  for (int x = 0; x < w; x++) {
    for (int y = 0; y < h; y++) {  // For each pixel, in order
      ICoord here(x, y);
      if(image[here] == false) {  // If the pixel is black
	bool match = false;  // No match
	for (int a = -sw/2; a <= sw/2 && !match; a++) {  // For se width
	  for (int b = -sh/2; b <= sh/2 && !match ; b++) {  // For se height
	    if ((se[ICoord(a + sw/2, b + sh/2)] != -1) && (image[here+ICoord(a,b)] != 0)) {  // If the pixel the respective distance from 
	      match = true;                                                                  // "here" is a white pixel (checking with non-black)
	      temp[here] = true;  // Make pixel white
	    }
	  }
	}
      }
    }
  }
  return temp;
}
