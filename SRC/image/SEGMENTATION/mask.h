 /* -*- C++ -*-
 $RCSfile: mask.h,v $
 $Revision: 1.5 $
 $Author: langer $
 $Date: 2014/09/27 21:41:35 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */  

 #include "common/doublearray.h"
 #include "common/coord.h"
 #include <oofconfig.h>
 
#ifndef MAKE_MASK_H
#define MAKE_MASK_H

/*
Create a square mask, where the center point represents the pixel being looked at. This mask can be 'scanned' over an image in order to perform operations on it, such as finding a derivative, or a gaussian of an image. Masks are assigned in the constructor, unless they are odd masks, in which case they can later be assigned just to the maskArray. Mask is applied in 'applyMask' function. 

*/

class Mask{
	private:
		int type;
		int width;
		bool pixelInBounds(ICoord pxl, ICoord size);
	public:
		DoubleArray maskArray;
		const static int GAUSSIAN_MASK = 1;
		const static int SMALL_GAUSSIAN_MASK = 2;
		const static int LAPLACE_MASK = 3;
		const static int SMALL_LAPLACE_MASK = 4;
		const static int X_DERIVATIVE_MASK = 5;
		const static int Y_DERIVATIVE_MASK = 6;
		const static int XX_DERIVATIVE_MASK = 7;
		const static int YY_DERIVATIVE_MASK = 8;
		const static int XY_DERIVATIVE_MASK = 9;
		const static int CANNY_X_MASK = 10;
		const static int CANNY_Y_MASK = 11;
		const static int UNASSIGNED = 100;
		Mask(int type);
		DoubleArray applyMask(DoubleArray array);
};


#endif
