/* -*- C++ -*-
 $RCSfile: timestep.C,v $
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

 #include "image/SEGMENTATION/timestep.h"
 #include "image/SEGMENTATION/classify.h"
 #include "image/SEGMENTATION/mask.h"
 
TimeStepClass::TimeStepClass (double t) {
	time = t;
	return;
}
 
 DoubleArray TimeStepClass::largeLaplaceStep(DoubleArray gray, DoubleArray &changed, double threshold){
	DoubleArray changes = DoubleArray(gray.size());
	DoubleArray newgray = DoubleArray(gray.size());
	ICoord center;
	Mask mask = Mask(Mask::LAPLACE_MASK);
	changes = mask.applyMask(gray);
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		center = i.coord();
		newgray[center] = gray[center] + time*changes[center];
		if (changes[center] > threshold &&  changed[center] > -1){
			changed[center] = 1;
		}
		if (changes[center] < 0 && changed[center] < 1)
			changed[center] = -1;
	}
	return newgray;

}

 DoubleArray TimeStepClass::laplaceStep(DoubleArray gray, DoubleArray &changed, double threshold){
	DoubleArray changes = DoubleArray(gray.size());
	DoubleArray newgray = DoubleArray(gray.size());
	ICoord center;
	Mask mask = Mask(Mask::SMALL_LAPLACE_MASK);
	changes = mask.applyMask(gray);
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		center = i.coord();
		newgray[center] = gray[center] + time*changes[center];
		if (changes[center] > threshold &&  changed[center] > -1){
			changed[center] = 1;
		}
		if (changes[center] < 0 && changed[center] < 1)
			changed[center] = -1;
	}
	return newgray;

}

DoubleArray TimeStepClass::gaussianBlur(DoubleArray gray, DoubleArray & change, double threshold){
	DoubleArray changes = DoubleArray(gray.size());
	Mask mask = Mask(Mask::GAUSSIAN_MASK);
	changes = mask.applyMask(gray);
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		ICoord center = i.coord();
		double c = gray[center] - changes[center];
		if (c > threshold && change[center] > -1)
			change[center] = 1;
		else if (c < 0 && change[center] < 1)
			change[center] = -1;
	}
	return changes;
}

DoubleArray TimeStepClass::smallGaussianBlur(DoubleArray gray, DoubleArray & change, double threshold){
	DoubleArray changes = DoubleArray(gray.size());
	Mask mask = Mask(Mask::SMALL_GAUSSIAN_MASK);
	changes = mask.applyMask(gray);
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		ICoord center = i.coord();
		double c = gray[center] - changes[center];
		if (c > threshold && change[center] > -1)
			change[center] = 1;
		else if (c < 0 && change[center] < 1)
			change[center] = -1;
	}
	return changes;
}

DoubleArray TimeStepClass::antiGeometricTimeStep(DoubleArray gray, DoubleArray &changed, double threshold){
	ICoord center;
	ICoord size = gray.size();
	DoubleArray newgray = DoubleArray(size);
	Mask dxmask = Mask(Mask::X_DERIVATIVE_MASK);
	Mask dymask = Mask(Mask::Y_DERIVATIVE_MASK);
	Mask dxxmask = Mask(Mask::XX_DERIVATIVE_MASK);
	Mask dyymask = Mask(Mask::YY_DERIVATIVE_MASK);
	Mask dxymask = Mask(Mask::XY_DERIVATIVE_MASK);
	DoubleArray dx_mask = dxmask.applyMask(gray);
	DoubleArray dy_mask = dymask.applyMask(gray);
	DoubleArray dxx_mask = dxxmask.applyMask(gray);
	DoubleArray dyy_mask = dyymask.applyMask(gray);
	DoubleArray dxy_mask = dxymask.applyMask(gray);
	double change;
	for (DoubleArray::iterator i = gray.begin(); i !=gray.end(); ++i){
		center = i.coord();
		double a = dx_mask[center]*dx_mask[center]*dxx_mask[center];
		double b = dx_mask[center]*dy_mask[center]*dxy_mask[center];
		double c = dy_mask[center]*dy_mask[center]*dyy_mask[center];
		double d = (dx_mask[center]*dx_mask[center]) + (dy_mask[center]*dy_mask[center]);
		
		if (d == 0)
			change = 0;
		else 
			change = (a +2*b+c)/(d);
		if (change > threshold && changed[center] != .01)
			changed[center] = 1;
		if (change < -.01)
			changed[center] = .01;

		newgray[center] = gray[center] + time*change;
	}

	return newgray;
}

