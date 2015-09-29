/* -*- C++ -*-
 $RCSfile: canny.C,v $
 $Revision: 1.10 $
 $Author: langer $
 $Date: 2014/09/27 21:41:34 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */ 

 #include "image/SEGMENTATION/canny.h"
 #include <math.h>
 #include "image/SEGMENTATION/mask.h"
 #include "image/SEGMENTATION/imageops.h"

CannyClass::CannyClass (ICoord s){
	size = s;
	return;
}

/*
Main function for Canny. 
*/
DoubleArray CannyClass::updateCannyArray(DoubleArray gray, double lowerThreshold, double upperThreshold){
	ICoord center;
	ICoord size = gray.size();
	DoubleArray newgray = DoubleArray(size);
	newgray = gray;
	DoubleArray gradient = DoubleArray(size); // strength of gradient at point
	DoubleArray angle = DoubleArray(size); // angle at which the gradient is going 
	DoubleArray final = DoubleArray(size); // what the thresholded image with edges traces looks like
	double min = 999;
	double max = -999;
	Mask Gx_Mask = Mask(Mask::CANNY_X_MASK);
	Mask Gy_Mask = Mask(Mask::CANNY_Y_MASK);
	DoubleArray Gx_array = Gx_Mask.applyMask(newgray); // X gradient
	DoubleArray Gy_array = Gy_Mask.applyMask(newgray); // Y gradient
	for (DoubleArray::iterator i = newgray.begin();i !=newgray.end(); ++i){
		center = i.coord();
		double Gx = Gx_array[center]; // Gradient in X for that point
		double Gy = Gy_array[center]; // Gradient in Y for that point
		double abs = sqrt(double(fabs(Gx)*fabs(Gx) + fabs(Gy)*fabs(Gy))); // The gradient for the point
		double thisAngle = (atan(double(double(Gy/Gx))/3.14)) * 180; // angle that there is change at for the point
		double newAngle = 0;
		/*  Now examine the angles, and average them out to be one of 4 directions   */
		if (((thisAngle <= 22.5) && (thisAngle > -22.5)) || (thisAngle >= 157.5) || (thisAngle <= -157.5))
			newAngle = 0;
		else if (((thisAngle > 22.5) && (thisAngle <= 67.5)) || ( (thisAngle <= -112.5) && (thisAngle > -157.5)))
			newAngle = 45;
		else if (((thisAngle > 67.5) && (thisAngle <= 112.5)) || ( (thisAngle <= -67.5) && (thisAngle > -112.5)))
			newAngle = 90;
		else if (((thisAngle > 112.5) && (thisAngle < 157.5)) || ( (thisAngle <= -22.5) && (thisAngle > -67.5)))
			newAngle = 135;
		gradient[center] = abs;
		angle[center] = newAngle;
		/* find the min and max angles for problemsolving */
		if (min > thisAngle)
			min = thisAngle;
		if (max < thisAngle)
			max = thisAngle;
		
	}
	for (DoubleArray::iterator i = final.begin(); i != final.end(); ++i){
		*i = 0;
	}
	
	/*   Set all the gradients to be between 0 and 1 */
	gradient = normalizeImage(gradient);
	
	/*
	Perform hysterisis thresholding. For each point that has gradient higher than upperThreshold, travel in perpendicular direction to the angle of that point while the next pixel has a gradient higher than the lowerThreshold, and has the same direction. 
	*/
	for (DoubleArray::iterator i = newgray.begin();i !=newgray.end(); ++i){
		center = i.coord();
		bool edgeEnd = false;
		if (gradient[center] >= upperThreshold){
			switch ((int)angle[center]){
				case 0:
					(*this).findEdge(edgeEnd, 0, 1, center, 0, lowerThreshold, gradient, angle, final);
					break;
				case 45:
					(*this).findEdge(edgeEnd, 1, 1, center, 45, lowerThreshold, gradient, angle, final);
					break;
				case 90:
					(*this).findEdge(edgeEnd,1, 0, center, 90, lowerThreshold, gradient, angle, final);
					break;
				case 135:
					(*this).findEdge(edgeEnd,1, -1, center, 135, lowerThreshold, gradient, angle, final);
					break;
				default:
					break;
			}	
		}
	}
	/* Canny often misses borders, so put a function to touch borders if they are up to two pixels away from an edge */
	(*this).touchBorders(final, lowerThreshold);
	return final;

}

/*
This is me trying to write supression of max. It doesnt work, but here for reference. This doesnt use the angles very well from how Canny max supression is supposed to work, I tried that and it didnt work well. 
*/
void CannyClass::suppressMax(DoubleArray & final, DoubleArray angle, DoubleArray gradient){
	for (DoubleArray::iterator i = final.begin(); i !=final.end(); ++i){
		ICoord center = i.coord();
		if (final[center] == 1){
			int dir = (int)(angle[center]);
			if (dir == 135){
				ICoord a = center + ICoord(1,0);
				ICoord b = center + ICoord(-1, 0);
				if (pixelInBounds(a) && pixelInBounds(b)){
					if (final[a] == 1 && final[b] == 1)
						final[center] = 0;
				}
			}
			else if (dir == 90){
				ICoord a = center + ICoord(-1,1);
				ICoord b = center + ICoord(1, 1);
				if (pixelInBounds(a) && final[a] == 1 && (pixelInBounds(b) && final[b] == 1))
					final[center] = 0;
			}
			else if (dir == 45){
				ICoord a = center + ICoord(0,1);
				ICoord b = center + ICoord(0, -1);
				if (pixelInBounds(a) && final[a] == 1 && (pixelInBounds(b) && final[b] == 1))
					final[center] = 0;
			
			}
			else if (dir == 0){
				ICoord a = center + ICoord(1,-1);
				ICoord b = center + ICoord(-1, -1);
				if (pixelInBounds(a) && final[a] == 1 && (pixelInBounds(b) && final[b] == 1))
					final[center] = 0;
			}
		}
	}

}

/*
If an edge approaches within two pixels of the end of the image, then the pixels in between are set to 1. This is because Canny doesnt work very well around edges, and this often helps out. Can be deleted in theory. 
*/
void CannyClass::touchBorders(DoubleArray &final, double lowerThreshold){
	ICoord size = final.size();
	ICoord r;
	ICoord l;
	for (int i = 0; i < size(0); ++i){
		r = ICoord(i, 0);
		l = ICoord(i, size(1)-1);
		if (final[r] == 0 && final[ICoord(i, 1)] == 1)
			final[r] = 1;
		if (final[l] == 0 && final[ICoord(i, size(1)-2)] == 1)
			final[l] = 1;
		if (final[r] == 0 && final[ICoord(i, 2)] == 1)
			final[r] = 1;
		if (final[l] == 0 && final[ICoord(i, size(1)-3)] == 1)
			final[l] = 1;
	}
	
	for (int i = 0; i < size(1); ++i){
		r = ICoord(0, i);
		l = ICoord(size(0)-1, i);
		if (final[r] == 0 && final[ICoord(1, i)] == 1)
			final[r] = 1;
		if (final[l] == 0 && final[ICoord(size(0)-2, i)] == 1)
			final[l] = 1;
		if (final[r] == 0 && final[ICoord(2, i)] == 1)
			final[r] = 1;
		if (final[l] == 0 && final[ICoord(size(0)-3, i)] == 1)
			final[l] = 1;
	}
}

/*
Follows the edge until the next pixel either doesnt have a high enough gradient or points in the wrong direction. 
*/
void CannyClass::findEdge(bool &edgeEnd, int colShift, int rowShift, ICoord center, int dir, double lowerThreshold, DoubleArray gradient, DoubleArray edgeDir, DoubleArray &final){
	ICoord size = gradient.size();
	int W = size(0);
	int H = size(1);
	int newCol = center(0);
	int newRow = center(1);
	int col = center(0);
	int row = center(1);

	/* Finds what the next pixel should be */
	if (colShift < 0) {
		if (col > 0)
			newCol = col + colShift;
		else
			edgeEnd = true;
	} 
	else if (col < W - 1) {
		newCol = col + colShift;
	}
	else
		edgeEnd = true;
	if (rowShift < 0) {
		if (row > 0)
			newRow = row + rowShift;
		else
			edgeEnd = true;
	}
	else if (row < H - 1) {
		newRow = row + rowShift;
	}
	else
		edgeEnd = true;

	/* Directions dont always point correctly, so to find more edges this is here */
	if (!edgeEnd && (gradient[ICoord(newCol, newRow)] > lowerThreshold))
		final[center] = 1;
	while (!edgeEnd && (edgeDir[ICoord(newCol, newRow)] == dir) && (gradient[ICoord(newCol, newRow)] >= lowerThreshold)){	
		final[ICoord(newCol, newRow)] = 1;
		if (colShift < 0) {
			if (newCol > 0)
				newCol = newCol + colShift;
			else
				edgeEnd = true;	
		} else if (newCol < W - 1) {
			newCol = newCol + colShift;
		} else
			edgeEnd = true;
		if (rowShift < 0) {
			if (newRow > 0)
				newRow = newRow + rowShift;
			else
				edgeEnd = true;
		} 
		else if (newRow < H - 1) {
			newRow = newRow + rowShift;
		} 
		else
			edgeEnd = true;
	}
	return;
}

/* Returns true if the pixel is in bounds of the image */
bool CannyClass::pixelInBounds(ICoord pxl) {
  int xx = (pxl)(0);
  int yy = (pxl)(1);
  if ( (xx<0) || (xx>=size(0)) || (yy<0) || (yy>=size(1)) )
    return false;
  return true;
}
