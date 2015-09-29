/* -*- C++ -*-
 $RCSfile: mask.C,v $
 $Revision: 1.10 $
 $Author: langer $
 $Date: 2014/09/27 21:41:35 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */  

 
 #include "image/SEGMENTATION/mask.h"
 
Mask::Mask(int type) //M and N should be odd
  :maskArray(ICoord(1,1),0.0) // default array, just so something is assigned
{
	/* can reconstruct what the masks do by drawing out the masks assigned below. The only mask not assigned here is the newgabor mask, because it changes every time. The masks can be drawn out based on the coordicates, with the 0,0 being the left bottom corner */
	(*this).type = type;
	if (type == GAUSSIAN_MASK){
		maskArray = DoubleArray(ICoord(5,5));
		maskArray[ICoord(2,2)] = 15;
		maskArray[ICoord(0,0)] = 2;
		maskArray[ICoord(0,1)] = 4;
		maskArray[ICoord(0,2)] = 5;
		maskArray[ICoord(0,3)] = 4;
		maskArray[ICoord(0,4)] = 2;
		maskArray[ICoord(1,0)] = 4;
		maskArray[ICoord(1,1)] = 9;
		maskArray[ICoord(1,2)] = 12;
		maskArray[ICoord(1,3)] = 9;
		maskArray[ICoord(1,4)] = 4;
		maskArray[ICoord(2,0)] = 5;
		maskArray[ICoord(2,1)] = 12;
		maskArray[ICoord(2,3)] = 12;
		maskArray[ICoord(2,4)] = 5;
		maskArray[ICoord(3,0)] = 4;
		maskArray[ICoord(3,1)] = 9;
		maskArray[ICoord(3,2)] = 12;
		maskArray[ICoord(3,3)] = 9;
		maskArray[ICoord(3,4)] = 4;
		maskArray[ICoord(4,0)] = 2;
		maskArray[ICoord(4,1)] = 4;
		maskArray[ICoord(4,2)] = 5;
		maskArray[ICoord(4,3)] = 4;
		maskArray[ICoord(4,4)] = 2;
	}
	else if (type == SMALL_GAUSSIAN_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = 9;
		maskArray[ICoord(0,1)] = 12;
		maskArray[ICoord(0,2)] = 9;
		maskArray[ICoord(1,0)] = 12;
		maskArray[ICoord(1,1)] = 15;
		maskArray[ICoord(1,2)] = 12;
		maskArray[ICoord(2,0)] = 9;
		maskArray[ICoord(2,1)] = 12;
		maskArray[ICoord(2,2)] = 9;
		
	}
	else if (type == LAPLACE_MASK){
		maskArray = DoubleArray(ICoord(5,5));
		maskArray[ICoord(0,0)] = 1;
		maskArray[ICoord(0,1)] = 1;
		maskArray[ICoord(0,2)] = 1;
		maskArray[ICoord(0,3)] = 1;
		maskArray[ICoord(0,4)] = 1;
		maskArray[ICoord(1,0)] = 1;
		maskArray[ICoord(1,1)] = 1;
		maskArray[ICoord(1,2)] = 1;
		maskArray[ICoord(1,3)] = 1;
		maskArray[ICoord(1,4)] = 1;
		maskArray[ICoord(2,0)] = 1;
		maskArray[ICoord(2,1)] = 1;
		maskArray[ICoord(2,3)] = 1;
		maskArray[ICoord(2,4)] = 1;
		maskArray[ICoord(3,0)] = 1;
		maskArray[ICoord(3,1)] = 1;
		maskArray[ICoord(3,2)] = 1;
		maskArray[ICoord(3,3)] = 1;
		maskArray[ICoord(3,4)] = 1;
		maskArray[ICoord(4,0)] = 1;
		maskArray[ICoord(4,1)] = 1;
		maskArray[ICoord(4,2)] = 1;
		maskArray[ICoord(4,3)] = 1;
		maskArray[ICoord(4,4)] = 1;
		maskArray[ICoord(2,2)] = -24;
	}
	else if (type == SMALL_LAPLACE_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = 1;
		maskArray[ICoord(0,1)] = 1;
		maskArray[ICoord(0,2)] = 1;
		maskArray[ICoord(1,0)] = 1;
		maskArray[ICoord(1,1)] = -8;
		maskArray[ICoord(1,2)] = 1;
		maskArray[ICoord(2,0)] = 1;
		maskArray[ICoord(2,1)] = 1;
		maskArray[ICoord(2,2)] = 1;
	}
	else if (type == X_DERIVATIVE_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = 0;
		maskArray[ICoord(0,1)] = -.5;
		maskArray[ICoord(0,2)] = 0;
		maskArray[ICoord(1,0)] = 0;
		maskArray[ICoord(1,1)] = 0;
		maskArray[ICoord(1,2)] = 0;
		maskArray[ICoord(2,0)] = 0;
		maskArray[ICoord(2,1)] = .5;
		maskArray[ICoord(2,2)] = 0;
	}
	else if (type == Y_DERIVATIVE_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = 0;
		maskArray[ICoord(0,1)] = 0;
		maskArray[ICoord(0,2)] = 0;
		maskArray[ICoord(1,0)] = -.5;
		maskArray[ICoord(1,1)] = 0;
		maskArray[ICoord(1,2)] = .5;
		maskArray[ICoord(2,0)] = 0;
		maskArray[ICoord(2,1)] = 0;
		maskArray[ICoord(2,2)] = 0;
	}
	else if (type == YY_DERIVATIVE_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = 0;
		maskArray[ICoord(0,1)] = 0;
		maskArray[ICoord(0,2)] = 0;
		maskArray[ICoord(1,0)] = 1;
		maskArray[ICoord(1,1)] = -2;
		maskArray[ICoord(1,2)] = 1;
		maskArray[ICoord(2,0)] = 0;
		maskArray[ICoord(2,1)] = 0;
		maskArray[ICoord(2,2)] = 0;
	}
	else if (type == XX_DERIVATIVE_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = 0;
		maskArray[ICoord(0,1)] = 1;
		maskArray[ICoord(0,2)] = 0;
		maskArray[ICoord(1,0)] = 0;
		maskArray[ICoord(1,1)] = -2;
		maskArray[ICoord(1,2)] = 0;
		maskArray[ICoord(2,0)] = 0;
		maskArray[ICoord(2,1)] = 1;
		maskArray[ICoord(2,2)] = 0;
	}
	else if (type == XY_DERIVATIVE_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = .25;
		maskArray[ICoord(0,1)] = 0;
		maskArray[ICoord(0,2)] = -.25;
		maskArray[ICoord(1,0)] = 0;
		maskArray[ICoord(1,1)] = 0;
		maskArray[ICoord(1,2)] = 0;
		maskArray[ICoord(2,0)] = -.25;
		maskArray[ICoord(2,1)] = 0;
		maskArray[ICoord(2,2)] = .25;
	}
	else if (type == CANNY_X_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = -1;
		maskArray[ICoord(0,1)] = -2;
		maskArray[ICoord(0,2)] = -1;
		maskArray[ICoord(1,0)] = 0;
		maskArray[ICoord(1,1)] = 0;
		maskArray[ICoord(1,2)] = 0;
		maskArray[ICoord(2,0)] = 1;
		maskArray[ICoord(2,1)] = 2;
		maskArray[ICoord(2,2)] = 1;
	}
	else if (type == CANNY_Y_MASK){
		maskArray = DoubleArray(ICoord(3,3));
		maskArray[ICoord(0,0)] = 1;
		maskArray[ICoord(0,1)] = 0;
		maskArray[ICoord(0,2)] = -1;
		maskArray[ICoord(1,0)] = 2;
		maskArray[ICoord(1,1)] = 0;
		maskArray[ICoord(1,2)] = -2;
		maskArray[ICoord(2,0)] = 1;
		maskArray[ICoord(2,1)] = 0;
		maskArray[ICoord(2,2)] = -1;
	}
	width = (int)maskArray.size()(0)/2; // how many pixels to side of center pixel. 
}

/*
This has a funny way of dealing with edges. In case of a Gaussian blur, divides by the sum of all of the numbers in the mask by definition. Might prove harsh on edges. In all other cases, divides by 8 no matter what, so that can equalize at edges. Also, when one of the pixels needed in the mask calculation is off the bounds of the image, the center pixel value is substituted, so that there is less difference. This doesnt pick up as many stray lines on edges, but also proves to often not pick up enough lines. 
*/
DoubleArray Mask::applyMask(DoubleArray array){
	ICoord size = array.size();
	DoubleArray newarray = DoubleArray(size);
	width = (int)maskArray.size()(0)/2; /* in case the maskArray was edited */
	for (DoubleArray::iterator i = array.begin();i !=array.end(); ++i){
		ICoord curr = i.coord();
		double num = 0;
		double c = 0;
		int d = 1;
		for (int i = -width; i <= width; ++i){ // scans through the mask
			for (int j = -width; j <= width; ++j){
				ICoord a = ICoord(i,j);
				if (pixelInBounds(curr + a, size)){
					num = num + array[curr+a]*maskArray[ICoord(i + width, j + width)];
					c = c + maskArray[ICoord(i + width, j + width)];
				}
				else{
					num = num + array[curr]*maskArray[ICoord(i + width, j + width)]; /* if pixel needed for mask is out of the image, then substitute the center pixel */
					d = d + 1; /* count number of pixels out of bounds */
				}
			}
		}
		if (type == GAUSSIAN_MASK)
			newarray[curr] = num/159;
		else if (type == SMALL_GAUSSIAN_MASK)
			newarray[curr] = num/99;
		else
			newarray[curr] = num/8;
	}
	return newarray;
}

/*
Check if pixel is in bounds. 
*/
bool Mask::pixelInBounds(ICoord pxl, ICoord size) {
  int xx = (pxl)(0);
  int yy = (pxl)(1);
  if ( (xx<0) || (xx>=size(0)) || (yy<0) || (yy>=size(1)) )
    return false;
  return true;
}

