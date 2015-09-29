#include "image.h"
#include "/common/array.h"

#include <stdio.h>
#include <iostream.h>
#include <fstream.h>
#include <math.h>

#include "/common/coord.h"
#include "imagemask.h"

bool isContour(const Image &image,ICoord pt) {
  if (image[pt]==255) {  // If the point is white
    for (int a = -1; a <= 1; a++) {  // Twice
      for (int b = -1; b <= 1; b++) {  // Twice
	if (image[ICoord(pt.x+a,pt.y+b)] == 0)
	  return true;  // Returns true if any of the points surrounding the white one is black
      }
    }
  }
  return false;
}

bool isDeletable(const Image &image,ICoord pt) {  //check 0-1 transitions; basically, this function implements the Zhang and Suen algorithm

  int numTrans=0;
  if ((image[ICoord(pt.x,pt.y+1)]==0) && (image[ICoord(pt.x+1,pt.y+1)]==255))
    numTrans++;
  if ((image[ICoord(pt.x+1,pt.y+1)]==0) && (image[ICoord(pt.x+1,pt.y)]==255))
    numTrans++;
  if ((image[ICoord(pt.x+1,pt.y)]==0) && (image[ICoord(pt.x+1,pt.y-1)]==255))
    numTrans++;
  if ((image[ICoord(pt.x+1,pt.y-1)]==0) && (image[ICoord(pt.x,pt.y-1)]==255))
    numTrans++;
  if ((image[ICoord(pt.x,pt.y-1)]==0) && (image[ICoord(pt.x-1,pt.y-1)]==255))
    numTrans++;
  if ((image[ICoord(pt.x-1,pt.y-1)]==0) && (image[ICoord(pt.x-1,pt.y)]==255))
    numTrans++;
  if ((image[ICoord(pt.x-1,pt.y)]==0) && (image[ICoord(pt.x-1,pt.y+1)]==255))
    numTrans++;
  if ((image[ICoord(pt.x-1,pt.y+1)]==0) && (image[ICoord(pt.x,pt.y+1)]==255))
    numTrans++;
/*-------------------------------------------------------------------------------------------*/
/* Increase numTrans if any two points adjacent to the point are also adjacent to each other */
/*-------------------------------------------------------------------------------------------*/

  if (numTrans!=1)
    return false;  // Return false (not deletable) unless there is exactly one "triangle"

  //check nonzero neighbors   (AND,(?)) check the number of points adjacent to the point that are white
  int numNonzero=-1;
  for (int a=-1;a<=1;a++) {
    for (int b=-1;b<=1;b++) {
      if (image[ICoord(pt.x+a,pt.y+b)]==255)
        numNonzero++;
    }
  }

  if ((numNonzero < 2) || (numNonzero > 6))  // The Zhang and Suen algorithm uses this method in skeletonization; basically, if not between
                                             // 2 and 6, it is 1 or 7 and thus an endpoint and thus not deletable.
     return false;

  return true;
}

bool satisfiesStep1(const Image &image,ICoord pt) {
  int p2=image[ICoord(pt.x,pt.y+1)];
  int p4=image[ICoord(pt.x+1,pt.y)];
  int p6=image[ICoord(pt.x,pt.y-1)];
  int p8=image[ICoord(pt.x-1,pt.y)];
  if ((p2*p4*p6==0)&&(p4*p6*p8==0))  // Also part of the Zhang and Suen thinning (skeletonization) algorithm
    return true;
  else
    return false;
}

bool satisfiesStep2(const Image &image,ICoord pt) {
  int p2=image[ICoord(pt.x,pt.y+1)];
  int p4=image[ICoord(pt.x+1,pt.y)];
  int p6=image[ICoord(pt.x,pt.y-1)];
  int p8=image[ICoord(pt.x-1,pt.y)];
  if ((p2*p4*p8==0)&&(p2*p6*p8==0))  // Also part of the Zhang and Suen thinning (skeletonization) algorithm
    return true;
  else
    return false;
}

Image skeletonize(const Image &image) {
  int w=image.query_width();
  int h=image.query_height();
  Image flag(w,h);

  Image deleted = image;

  int step=1;
  bool stop=false;
  while (!stop) {
    int numChanged=0;

    for (int a = 0; a < w; a++) {
      for (int b = 0; b < h; b++) {
	if (isContour(deleted,ICoord(a,b)) && isDeletable(deleted,ICoord(a,b))) {  // If the pixel is isolated and deletable
	  if (step == 1) {
	    if (satisfiesStep1(deleted,ICoord(a,b))) {  // Zhang and Suen algorithm-related
              flag[ICoord(a,b)]=1;
	      numChanged++;
	    }
	  }
	  else {
	    if (satisfiesStep2(deleted,ICoord(a,b))) {  // Zhang and Suen algorithm-related
	      flag[ICoord(a,b)]=1;  // Marks point for deletion
	      numChanged++;
	    }
	  }
	}
      }
    }

    //remove flagged points
    for (int c = 0; c < w; c++) {
      for (int d = 0; d < h; d++) {
	if (flag[ICoord(c,d)]==1)
	  deleted[ICoord(c,d)]=0;
      }
    }
    step *= -1;
    //  cout<<numChanged<<endl;
    if (numChanged==0)
      stop=true;
  }
  return deleted;
}
