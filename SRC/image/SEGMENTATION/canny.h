/* -*- C++ -*-
 $RCSfile: canny.h,v $
 $Revision: 1.5 $
 $Author: langer $
 $Date: 2014/09/27 21:41:34 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */ 

#include <oofconfig.h>
#include <stdio.h>
#include <math.h>
#include "common/doublearray.h"
#include "image/oofimage.h"

#ifndef CANNY_ALGORITHM_H
#define CANNY_ALGORITHM_H

/*
Uses the Canny algorithm in order to find the edges in an image. 
Is usually passed an image that has been blurred through a gaussian blur.  

How canny algorithm works:
Applies filters in four directions to detect horizontal, vertical and diagonal edges of blurred image. For each pixel in result, the filter gives the magnitude of change: intensity. Also the direction fo change is found from teh filters. In the hysterisis thresholding, an edge starts at the condition that its magnitude is higher than T1, and continues as long as the edge points in the same direction and the next pixels' magnitude is greater than T2. 

Status of it:
Produces lines that are very thick. Need to do one of those 'delete smaller peaks' on it, but when I tried it, it picked up too many different lines,and basically split each thick line into 3-4 smaller lines. Can be attempted again?
*/


class CannyClass {
	private:
		ICoord size;
	public:
		void suppressMax(DoubleArray & final, DoubleArray angle, DoubleArray gradient);
		CannyClass(ICoord s);
		void findEdge(bool &edgeEnd, int colShift, int rowShift, ICoord center, int dir, double lowerThreshold, DoubleArray gradient, DoubleArray edgeDir, DoubleArray &final);
		void touchBorders(DoubleArray &final, double lowerThreshold);
		DoubleArray updateCannyArray(DoubleArray gray,  double lowerThreshold, double upperThreshold);
		bool pixelInBounds(ICoord pxl);
		
};

#endif
