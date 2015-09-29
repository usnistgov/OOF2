/*
Kevin Chang
September 4, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

closeNugget.C

Self-contianed image closing nugget.
*/

#include "common/array.h"

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "common/coord.h"
#include "imagemask.h"
#include "closeNugget.h"

/*----------*/

closeClass::closeClass() {
  d = 9;
}

/*----------*/

closeClass::closeClass(int din) {
  d = din;
}

/*----------*/

BWImage closeClass::run(const BWImage& imagein) {

  cout << "start closerun" << endl;

  BWImage image = close(imagein, d);  // Fills in the holes in the image left by thresholding     close.C
  /*
  ofstream gaborClosed("gaborClosed");
  closed.save(gaborClosed);
  gaborClosed.close();
  */

  return image;
}

/*----------*/

BWImage closeClass::close(BWImage image, int n) {

  cout << "close has begun" << endl;

  grayImage se(n,n);

  /*
  for (int a = 0; a < n; a++) {
    for (int b = 0; b < n; b++) {
      se[ICoord(a,b)] = -1; 
      cout << se[ICoord(a,b)] << " ";
    }
    cout << endl;
  }

  cout << "se has been initialized" << endl;

  for (int c = 0; c <= n/2; c++) {
    for (int d = n/2 - c; d <= n/2 + c; d++) {
      se[ICoord(c,d)] = 0;
      se[ICoord(n-1-c,d)] = 0;
      cout << se[ICoord(c,d)] << " ";
    }
    cout << endl;
  }

  cout << "se has been reinitialized" << endl;
  */

  //  BWImage closed = erode(dilate(image, se), se);

  // !!! IMPORTANT !!!
  // To make line closing stand-alone, erode MUST be fixed.
  // In the large algorithm, skeletonization makes it useless,
  // but without skeletonization, erosion is a necessary step.
  // !!! IMPORTANT !!!

  BWImage closed = dilate(image,se);

  //  cout << "closed has finished" << endl;

  return closed;
}

/*----------*/

BWImage closeClass::dilate(const BWImage& image, const grayImage& se) {  // Opposite of erode.  Adds pixels to an area.  Background erodes.
  int w = image.width();
  int h = image.height();
  int sw = se.width();
  int sh = se.height();
  BWImage temp(w,h);
  int newx;
  int newy;

  for (int k = 0; k < w; k++) {
    for (int c = 0; c < h; c++) {
      temp[ICoord(k,c)] = image[ICoord(k,c)];
    }
  }

  //  cout << "In dilate" << endl;

  for (int x = 0; x < w; x++) {
    for (int y = 0; y < h; y++) {  // For each pixel, in order
      ICoord here(x, y);
      if(image[here] == false) {  // If the pixel is black
	bool match = false;  // No match // This is the original location

	for (int a = -sw/2; a <= sw/2 && !match; a++) {  // For se width
	  for (int b = -sh/2; b <= sh/2 && !match ; b++) {  // For se height

	    if ((x + a < 0) || (x + a >= w))
	      newx = x - a;
	    else
	      newx = x + a;

	    if ((y + b < 0) || (y + b >= h))
	      newy = y - b;
	    else
	      newy = y + b;

	    /*
	    if (here(0) + a < 0)
	      newx = 0;
	    else if (here(0) + a >= w)
	      newx = w - 1;
	    else
	      newx = here(0) + a;

	    if (here(1) + b < 0)
	      newy = 0;
	    else if (here(1) + b >= h)
	      newy = h - 1;
	    else
	      newy = here(1) + b;
	    */

	    if (se[ICoord(a+sw/2, b+sh/2)] != -1) {
	      if (image[ICoord(newx,newy)] == true) {  // If the pixel is white
	        match = true;
  	        temp[here] = true;  // Make pixel white
	      }
	    }
	  }
	}
      }
    }
  }
  return temp;
}

/*----------*/

BWImage closeClass::erode(const BWImage& image, const grayImage& se) {  // Opposite of dilate.  Takes pixels off an area.  Background dilates.
  int w = image.width();
  int h = image.height();
  int sw = se.width();
  int sh = se.height();
  BWImage temp(w,h);
  int newx;
  int newy;

  for (int k = 0; k < w; k++) {
    for (int c = 0; c < h; c++) {
      temp[ICoord(k,c)] = image[ICoord(k,c)];
    }
  }

  for (int x = 0; x < w; x++) {
    for (int y = 0; y < h; y++) {
      ICoord here(x, y);
      if(image[here] == true) {  // If a white pixel
	bool match = false;
	for (int a = -sw/2; a <= sw/2 && !match; a++) {  // For se width
	  for (int b = -sh/2; b <= sh/2 && !match; b++) {  // For se height

	    //	    cout << "x, y, a, b, here: " << x << " " << y << " " << a << " " << b << " " << image[here] << endl;

	    if ((x + a < 0) || (x + a >= w))
	      newx = x - a;
	    else
	      newx = x + a;

	    if ((y + b < 0) || (y + b >= h))
	      newy = y - b;
	    else
	      newy = y + b;

	    //	    cout << "newx, newy: " << newx << " " << newy << endl;

	    if (se[ICoord(a + sw/2, b + sh/2)] != -1) {
	      if (image[ICoord(newx,newy)] == false) {  // If this is a black pixel // false
		match = true;
		temp[here] = false;  // Make pixel black // false
	      }
	    }
	  }
	}
      }
    }
  }
  return temp;
}

/*----------*/
