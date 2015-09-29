/* -*- C++ -*-
 $RCSfile: timestep.h,v $
 $Revision: 1.2 $
 $Author: langer $
 $Date: 2014/09/27 21:41:37 $

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

#ifndef TIMESTEP_H
#define TIMESTEP_H

/*
This class takes time steps on an image. The available time steps are:
-Laplace step: Looks at the pixels right above, below, left, and right of each pixel to figure out the change in the pixels' intensity over time.
-Large Laplace step: Looks at all the pixels in a 5x5 mask around each pixel to find its' intensity change over time.
-Gaussian blur: Looks at the pixels in a 5x5 mask around each pixel while giving each pixel around the center a given weight to see the center pixels' change over time.
-Small Gaussian blur: Looks at the pixels in a 3x3 mask around each pixel while giving each pixel around the center a given weight to see the center pixels' change over time.

The laplacian functions have a changed array parameter, which based on a threshold given, updates the changed array to show which pixels have changed pask that threshold. If pixels change in the negative direction, they will never be set as an edge. 

*/

class TimeStepClass {
	public:
		TimeStepClass(double t);
		DoubleArray laplaceStep(DoubleArray gray, DoubleArray &changed, double threshold);
		DoubleArray largeLaplaceStep(DoubleArray gray, DoubleArray &changed, double threshold);
		DoubleArray gaussianBlur(DoubleArray gray, DoubleArray & change, double threshold);
		DoubleArray smallGaussianBlur(DoubleArray gray, DoubleArray & change, double threshold);
		DoubleArray antiGeometricTimeStep(DoubleArray gray, DoubleArray &changed, double threshold);

	private:
		double time;

};

#endif
