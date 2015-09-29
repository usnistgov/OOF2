/*
Kevin Chang
September 4, 2002
Senior Research Project
Torrence

Center for Theoretical and Computational Materials Science
National Institute of Standards and Technology

skeletonNugget.C

File contains a self-contained skeletonization class
*/

#include "image/oofimage.h"
#include "common/array.h"

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "common/coord.h"
#include "imagemask.h"
#include "skeletonNugget.h"

/*----------*/

skeletonClass::skeletonClass() {
}

/*----------*/

BWImage skeletonClass::run(const BWImage & imagein) {

  //  cout << "Run begins" << endl;

  int w = imagein.width();
  int h = imagein.height();

  /*
  BWImage image(w,h);
  for (int a = 0; a < w; a++)
    for (int b = 0; b < h; b++)
      image[ICoord(a,b)] = imagein[ICoord(a,b)];
  */

  BWImage skeleton(w,h);
  skeleton = skeletonize(imagein);

  /*
  ofstream gaborSkel("gaborSkel");
  skeleton.save(gaborSkel);
  gaborSkel.close();
  cout << "Intermediate step: Skeletonized gabor image saved to file: gaborSkel" << endl;
  */

  cout << "Run ends" << endl;

  return skeleton;
}

/*----------*/

bool skeletonClass::isContour(const BWImage &image, ICoord pt) {
  int llxa;
  int llyb;

  //  cout << "isContour begin" << endl;

  if (image[pt] == 1) {  // If the point is white
    for (int a = -1; a <= 1; a++) {
      for (int b = -1; b <= 1; b++) {
	llxa = pt(0) + a;
	llyb = pt(1) + b;

        if (llxa < 0)
          llxa *= -1;
	if (llyb < 0)
	  llyb *= -1;
        if(llxa >= image.width())
          llxa -= image.width();
        if(llyb >= image.height())
          llyb -= image.height();

	if (image[ICoord(llxa, llyb)] == 0)
	  return true;  // Returns true if any of the points surrounding the white one is black
      }
    }
  }
  return false;
}

/*----------*/

bool skeletonClass::isDeletable(const BWImage &image, ICoord pt) {  //check 0-1 transitions; basically, this function implements the Zhang and Suen algorithm
  int numTrans = 0;
  int xneg = pt(0) - 1;
  int xpos = pt(0) + 1;
  int yneg = pt(1) - 1;
  int ypos = pt(1) + 1;
  int h = image.height();
  int w = image.width();
  int newx;
  int newy;

  if (xneg < 0)
    xneg = 0;
  if (yneg < 0)
    yneg = 0;
  if (xpos >= w)
    xpos = w - 1;
  if (ypos >= h)
    ypos = h - 1;

  //  cout << "flag2" << endl;

  if (image[ICoord(pt(0), ypos)] == false && (image[ICoord(xpos, ypos)] == true))
    numTrans++;
  if (image[ICoord(xpos, ypos)] == false && (image[ICoord(xpos, pt(1))] == true))
    numTrans++;
  if (image[ICoord(xpos, pt(1))] == false && (image[ICoord(xpos, yneg)] == true))
    numTrans++;
  if (image[ICoord(xpos, yneg)] == false && (image[ICoord(pt(0), yneg)] == true))
    numTrans++;
  if (image[ICoord(pt(0), yneg)] == false && (image[ICoord(xneg, yneg)] == true))
    numTrans++;
  if (image[ICoord(xneg, yneg)] == false && (image[ICoord(xneg, pt(1))] == true))
    numTrans++;
  if (image[ICoord(xneg, pt(1))] == false && (image[ICoord(xneg, ypos)] == true))
    numTrans++;
  if (image[ICoord(xneg, ypos)] == false && (image[ICoord(pt(0), ypos)] == true))
    numTrans++;
/*-------------------------------------------------------------------------------------------*/
/* Increase numTrans if any two points adjacent to the point are also adjacent to each other */
/*-------------------------------------------------------------------------------------------*/

  //  cout << "flag3; numTrans: " << numTrans << endl;

  if (numTrans != 1)
    return false;  // Return false (not deletable) unless there is exactly one "triangle"

  //check nonzero neighbors   (AND,(?)) check the number of points adjacent to the point that are white
  int numNonzero = -1;

  //  cout << "flag4; image width: " << image.width() << ", image height: " << image.height() << endl;

  for (int a = -1; a <= 1; a++) {
    for (int b = -1; b <= 1; b++) {
      if (pt(0) + a < 0)
	newx = 0;
      else if (pt(0) + a >= w)
	newx = w - 1;
      else
	newx = pt(0) + a;

      if (pt(1) + b < 0)
	newy = 0;
      else if (pt(1) + b >= h)
	newy = h - 1;
      else
	newy = pt(1) + b;

      //      cout << ICoord(newx,newy) << endl;

      if (image[ICoord(newx,newy)] == true)
        numNonzero++;
    }
  }

  //  cout << "isDeletable end" << endl;

  if ((numNonzero < 2) || (numNonzero > 6))  // The Zhang and Suen algorithm uses this method in skeletonization; basically, if not between
     return false;                           // 2 and 6, it is 1 or 7 and thus an endpoint and thus not deletable.

  return true;
}

/*----------*/

bool skeletonClass::satisfiesStep1(const BWImage &image, ICoord pt) {

  //  cout << "ss1 begin" << endl;

  int p2, p4, p6, p8;

  if (pt(1) + 1 >= image.height())
    p2 = image[ICoord(pt(0),pt(1)-1)];
  else
    p2 = image[ICoord(pt(0),pt(1)+1)];

  if (pt(0) + 1 >= image.width())
    p4 = image[ICoord(pt(0)-1,pt(1))];
  else
    p4 = image[ICoord(pt(0)+1,pt(1))];

  if (pt(1) - 1 < 0)
    p6 = image[ICoord(pt(0),pt(1)+1)];
  else
    p6 = image[ICoord(pt(0),pt(1)-1)];

  if (pt(0) - 1 < 0)
    p8 = image[ICoord(pt(0)+1,pt(1))];
  else
    p8 = image[ICoord(pt(0)-1,pt(1))];

  //  cout << "ss1 end" << endl;

  if ((p2 * p4 * p6 == 0) && (p4 * p6 * p8 == 0))  // Also part of the Zhang and Suen thinning (skeletonization) algorithm
    return true;
  else
    return false;
}

/*----------*/

bool skeletonClass::satisfiesStep2(const BWImage &image, ICoord pt) {
  int p2, p4, p6, p8;

  //  cout << "ss2 begin" << endl;

  if (pt(1) + 1 >= image.height())
    p2 = image[ICoord(pt(0),pt(1)-1)];
  else
    p2 = image[ICoord(pt(0),pt(1)+1)];

  if (pt(0) + 1 >= image.width())
    p4 = image[ICoord(pt(0)-1,pt(1))];
  else
    p4 = image[ICoord(pt(0)+1,pt(1))];

  if (pt(1) - 1 < 0)
    p6 = image[ICoord(pt(0),pt(1)+1)];
  else
    p6 = image[ICoord(pt(0),pt(1)-1)];

  if (pt(0) - 1 < 0)
    p8 = image[ICoord(pt(0)+1,pt(1))];
  else
    p8 = image[ICoord(pt(0)-1,pt(1))];

  //  cout << "ss2 end" << endl;

  if ((p2 * p4 * p8 == 0) && (p2 * p6 * p8 == 0))  // Also part of the Zhang and Suen thinning (skeletonization) algorithm
    return true;
  else
    return false;
}

/*----------*/

BWImage skeletonClass::skeletonize(const BWImage &image) {

  cout << "Start skeletonize" << endl;

  int w = image.width();
  int h = image.height();
  BWImage flag(w,h);

  BWImage deleted(w,h);
  for (int m = 0; m < w; m++)
    for (int n = 0; n < h; n++)
      deleted[ICoord(m,n)] = image[ICoord(m,n)];

  //  cout << "Initializations done" << endl;

  int step = 1;
  bool stop = false;
  while (!stop) {
    int numChanged = 0;

    for (int a = 0; a < w; a++) {
      for (int b = 0; b < h; b++) {

	//	cout << a << ", " << b << endl;
	//	cout << image.width() << ", " << image.height() << endl;

	if (isContour(deleted,ICoord(a,b)) && isDeletable(deleted,ICoord(a,b))) {  // If the pixel is isolated and deletable

	  //	  cout << "isContour, isDeletable passed" << endl;

	  if (((step == 1) && (satisfiesStep1(deleted,ICoord(a,b))))
	   || ((step == -1) && (satisfiesStep2(deleted,ICoord(a,b))))) {  // Zhang and Suen algorithm-related
              flag[ICoord(a,b)] = 1;  // Marks point for deletion
	      numChanged++;
	  }
	}
      }
    }

    //    cout << "First major loop over" << endl;

    //remove flagged points
    for (int c = 0; c < w; c++) {
      for (int d = 0; d < h; d++) {
	if (flag[ICoord(c,d)] == 1)
	  deleted[ICoord(c,d)] = 0;
      }
    }
    step *= -1;
    //      cout << numChanged << endl;
    if (numChanged == 0)
      stop=true;
  }

  cout << "skeletonize finished" << endl;

  return deleted;
}
