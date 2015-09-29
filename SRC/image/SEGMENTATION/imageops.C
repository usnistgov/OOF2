// -*- C++ -*-
// $RCSfile: imageops.C,v $
// $Revision: 1.8 $
// $Author: langer $
// $Date: 2014/09/27 21:41:35 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "image/SEGMENTATION/imageops.h"
#include <iostream>
#include <math.h>
#include "image/oofimage.h"
#include "common/array.h"
#include "common/doublearray.h"
#include "common/boolarray.h"
#include "common/intarray.h"
#include "common/random.h"

/*
Sets an OOFImage from a DoubleArray. It turns out black and white even though the function is called gray2color.
*/
void setFromArray(OOFImage& colorImage,const DoubleArray& image) {
//Creates a color image from an array of doubles.
  colorImage.set(image,gray2color);
}

/*
Sets an OOFImage from a BoolArray. It turns out black and white even though the function is called gray2color.
*/
void setFromBoolArray(OOFImage& colorImage,const BoolArray& image) {
//Creates a color image from an array of doubles.
	DoubleArray grays = DoubleArray(image.size());
	for (DoubleArray::iterator i = grays.begin(); i != grays.end(); ++i){
		ICoord curr = i.coord();
		if (image[curr] == true)
			grays[curr] = 1;
		else
			grays[curr] = 0;
	}
	colorImage.set(grays,gray2color);
}

/*
Sets a DoubleArray from an OOFImage. Sets the values of all the pixels between 0-1 based on their intensity. 
*/
DoubleArray arrayFromImage(OOFImage& colorImage){
	return colorImage.convert(togray);
}


/*
Places all of the checked pixels (1s) on the old image to see if the borders match up.
*/
DoubleArray mountThresholdedImageOnOldImage(DoubleArray gray, DoubleArray newgray){
	ICoord size = gray.size();
	ICoord center;
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		center = i.coord();
		if (newgray[center] == 1)
			gray[center] = 1;
	
	}
	return gray;
}

/*
Draws a line from point 0 to point 1 in the specified color. Is another way to 'fix up' the image. Would be better replaced by a methond much like pixel selection but where the image is actually modified when pixels are selected. 
The line drawn here is a correct continuous line of one pixel in width. 
*/
void drawFixerLines(DoubleArray &gray, int x0, int y0, int x1, int y1, int color){
        if (y0 > y1){
		int temp = y0;
		y0 = y1;
		y1 = temp;
		temp = x0;
		x0 = x1;
		x1 = temp;
	}
	int dy = y1 - y0;
        int dx = x1 - x0;
        int stepx, stepy;
	int width = 1;
	ICoord size = gray.size();
        if (dy < 0) { dy = -dy;  stepy = -width; } else { stepy = width; }
        if (dx < 0) { dx = -dx;  stepx = -1; } else { stepx = 1; }
        dy <<= 1;
        dx <<= 1;
        y0 *= width;
        y1 *= width;
	if (pixelInBounds(ICoord(y0, x0), size))
	        gray[ICoord(y0, x0)] = color; 
        if (dx > dy) {
            int fraction = dy - (dx >> 1);
            while (x0 != x1) {
                if (fraction >= 0) {
                    y0 += stepy;
                    fraction -= dx;
                }
                x0 += stepx;
                fraction += dy;
                if (pixelInBounds(ICoord(y0, x0), size))
	      		gray[ICoord(y0, x0)] = color; 
            }
        } else {
            int fraction = dx - (dy >> 1);
            while (y0 != y1) {
                if (fraction >= 0) {
                    x0 += stepx;
                    fraction -= dy;
                }
                y0 += stepy;
                fraction += dx;
                if (pixelInBounds(ICoord(y0, x0), size))
	        	gray[ICoord(y0, x0)] = color;  
            }
        }
	
}

/*
Normalize the intensity of the image to range from 0 to 1 based on the minimum and maximum intensities of the pixels in the image. Used to make thresholding easier -> between 0 and 1 instead of random values.
Can be annoying when normalizing with negative and positive numbers and then thresholding, creating a spot in the middle where everything flips, might need to be noted somewhere. 
*/
DoubleArray normalizeImage(DoubleArray original){
	ICoord size = original.size();
	double min = original[ICoord(0,0)];
	double max = original[ICoord(0,0)];
	DoubleArray old = DoubleArray(original.size());
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();
		double a = original[curr];
		if (a > max)
			max = a;
		if (a < min)
			min = a;
	}
	double difference = max - min;
	double toadd = 0;
	if (min < 0){
		toadd = -1*min; // will be posisite amount to add
	}
	else
		toadd = -1*min; // will be negative amount to add so it will subtract

	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();

		original[curr] = (original[curr] + toadd)/difference;
	}
	for (DoubleArray::iterator i = original.begin();i !=original.end(); ++i){
		ICoord curr = i.coord();
		double a = original[curr];
		if (a > max)
			max = a;
		if (a < min)
			min = a;
	}
	return original;
}

/*
Checks if the pixels is within the image bounds of the image. 
*/
bool pixelInBounds(ICoord pxl, ICoord size) {
  int xx = (pxl)(0);
  int yy = (pxl)(1);
  if ( (xx<0) || (xx>=size(0)) || (yy<0) || (yy>=size(1)) )
    return false;
  return true;
}

/*
Scans through the image and sets all of the pixels within a 'range' of each pixel to that pixels color, if the color of the pixels equals color. Similar to expand method of pixel selection. Is used in order to try to connect almost connecting pixels in a thresholded image. 
*/
void expand(int range, DoubleArray & image, int color){
	ICoord size = image.size();
	DoubleArray toAdd = DoubleArray(image.size());
	for (DoubleArray::iterator i = image.begin();i !=image.end(); ++i){
		ICoord c = i.coord();
		if (image[c] == color){
			for (int i = -range; i <= range; ++i){
				for (int j = -range; j <=range; ++j){
					ICoord a = c + ICoord(i, j);
					if (pixelInBounds(a, size) && image[a] != color) // if pixels around the center pixel are of a different color, they can be expanded onto
						toAdd[a] = .5; //tag the pixel for addition
				}
			}
		}
	}
	
	
	// merge the tagged pixels into the image.
	for (DoubleArray::iterator i = image.begin();i !=image.end(); ++i){
		ICoord c = i.coord();
		if (toAdd[c] == .5)
			image[c] = color;	
	}
}

/*
For each pixel of the given color in the image that is on the border, close in by 1 pixel. Does not preserve connectivity
*/
void shrink(DoubleArray & image, int color){
	ICoord size = image.size();
	DoubleArray toDelete = DoubleArray(image.size());
	for (DoubleArray::iterator i = image.begin();i !=image.end(); ++i){
		ICoord c = i.coord();
		if (image[c] == color){
			ICoord right = c + ICoord(0,1);
			ICoord rightdown = c + ICoord(-1,1);
			ICoord down = c + ICoord(-1,0);
			ICoord leftdown = c + ICoord(-1,-1);
			ICoord left = c + ICoord(0,-1);
			ICoord leftup = c + ICoord(1,-1);
			ICoord up = c + ICoord(1,0);
			ICoord rightup = c + ICoord(1, 1);
			/* for all the pixels around the center pixel */
			if (pixelInBounds(right, size) && image[right] != color){
				if (pixelInBounds(rightdown, size))
					toDelete[rightdown] = .5; // tag pixel for deletion. 
				if (pixelInBounds(rightup, size))
					toDelete[rightup] = .5;// tag pixel for deletion. 
			}	
			if (pixelInBounds(up, size) && image[up] != color){
				if (pixelInBounds(rightup, size))
					toDelete[rightup] = .5;// tag pixel for deletion. 
				if (pixelInBounds(leftup, size))
					toDelete[leftup] = .5;// tag pixel for deletion. 
			}
			if (pixelInBounds(left, size) && image[left] != color){
				if (pixelInBounds(leftdown, size))
					toDelete[leftdown] = .5;// tag pixel for deletion. 
				if (pixelInBounds(leftup, size))
					toDelete[leftup] = .5;// tag pixel for deletion. 
			}	
			if (pixelInBounds(down, size) && image[down] != color){
				if (pixelInBounds(rightdown, size))
					toDelete[rightdown] = .5;// tag pixel for deletion. 
				if (pixelInBounds(leftdown, size))
					toDelete[leftdown] =  .5;// tag pixel for deletion. 
			}
			
			if (pixelInBounds(rightup, size) && image[rightup] != color){
				if (pixelInBounds(right, size))
					toDelete[right] = .5;// tag pixel for deletion. 
				if (pixelInBounds(up, size))
					toDelete[up] = .5;// tag pixel for deletion. 
			}	
			if (pixelInBounds(leftup, size) && image[leftup] != color){
				if (pixelInBounds(up, size))
					toDelete[up] = .5;// tag pixel for deletion. 
				if (pixelInBounds(left, size))
					toDelete[left] = .5;// tag pixel for deletion. 
			}
			if (pixelInBounds(leftdown, size) && image[leftdown] != color){
				if (pixelInBounds(down, size))
					toDelete[down] = .5;// tag pixel for deletion. 
				if (pixelInBounds(left, size))
					toDelete[left] = .5;// tag pixel for deletion. 
			}	
			if (pixelInBounds(rightdown, size) && image[rightdown] != color){
				if (pixelInBounds(right, size))
					toDelete[right] = .5;// tag pixel for deletion. 
				if (pixelInBounds(down, size))
					toDelete[down] =  .5;// tag pixel for deletion. 
			}
			
		}
	}
	
	// delete the tagged pixels from the image
	for (DoubleArray::iterator i = image.begin();i !=image.end(); ++i){
		ICoord c = i.coord();
		if (toDelete[c] == .5)
			image[c] = 1-color; /* assign to opposite of given color. This works for binary image, and in case somebody puts in a non 0 or 1 value, this can produce some sort of result. 	*/
	}
}

