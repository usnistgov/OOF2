/*
Kevin Chang
September 4, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

erodeNugget.C

Self-contianed erosion nugget.
 */

#include "image/image.h"
#include "common/array.h"

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "common/coord.h"
#include "imagemask.h"

/*----------*/

class erodeClass {
public:
  erodeClass(int din, const grayImage& sein);
  BWImage run(const BWImage& imagein);
private:
  int d;
  const grayImage se;  // Structuring element
  BWImage erode(const BWImage& image, const grayImage& se);
};

/*----------*/

BWImage erodeClass::run(const BWImage& imagein) {
  BWImage image;
  image = imagein;

  erode(image, se);

  return image;
}

/*----------*/

erodeClass::erodeClass(int din, const grayImage& sein) {
  d = din;
  for(grayImage::iterator i = array.begin(); i != array.end(); i++)
    se[i] = sein[i];
}

/*----------*/

BWImage erodeClass::erode(const BWImage& image, const grayImage& se) {  // Opposite of dilate.  Takes pixels off an area.  Background dilates.
  int w = image.query_width();
  int h = image.query_height();
  int sw = se.query_width();
  int sh = se.query_height();
  BWImage temp = image;

  for (int x = 0; x < w; x++) {
    for (int y = 0; y < h; y++) {
      ICoord here(x, y);
      if(image[here] == true) {  // If a white pixel
	bool match = false;
	for (int a = -sw/2; a <= sw/2 && !match; a++) {  // For se width
	  for (int b = -sh/2; b <= sh/2 && !match; b++) {  // For se height
	    if ((se[ICoord(a + sw/2, b + sh/2)] != -1) && (image[here+ICoord(a,b)] == 0)) {  // If this is a black pixel
	      match = true;
	      temp[here] = false;  // Make pixel black
	    }
	  }
	}
      }
    }
  }

  return temp;
}
