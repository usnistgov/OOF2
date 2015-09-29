/* -*- C++ -*-
 $RCSfile: diffusionRHS.C,v $
 $Revision: 1.6 $
 $Author: langer $
 $Date: 2014/09/27 21:41:34 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */ 
 
#include "image/SEGMENTATION/diffusionRHS.h"
#include "image/SEGMENTATION/mask.h"
#include "image/SEGMENTATION/thresholding.h"

DiffusionRHS::DiffusionRHS(){
	time = 0;
}


AntiGeometric::AntiGeometric(double t) {
	time = t;
	type = ANTIGEOMETRIC;
}

/*
Takes ONE timestep via Anti-Geometric function.
Anti geometric equation: I(t + 1) = I(t) + dt*dI/dt
dI/dt = (Ix^2*Ixx + 2*IxIyIxy + Iy^2*Iyy)/(Ix^2+Iy^2)
*/
DoubleArray AntiGeometric::timestep(DoubleArray gray){
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
	for (DoubleArray::iterator i = gray.begin(); i !=gray.end(); ++i){
		center = i.coord();
		double change;
		double a = dx_mask[center]*dx_mask[center]*dxx_mask[center];
		double b = dx_mask[center]*dy_mask[center]*dxy_mask[center];
		double c = dy_mask[center]*dy_mask[center]*dyy_mask[center];
		double d = (dx_mask[center]*dx_mask[center]) + (dy_mask[center]*dy_mask[center]); /*math pow function not used because it often behaves badly with doubles and neg numbers? For some reason here. */
		if (d == 0) /* to avoid division by zero */
			change = 0;
		else 
			change = (a +2*b+c)/(d);
		newgray[center] = gray[center] + time*change; /* I(t + 1) = I(t) + dt*(dI/dt) */
	}
	return newgray;
}

/*
Returns the change between the timestep function, and the original function. Changed - original.
*/
DoubleArray AntiGeometric::change(DoubleArray g){
	DoubleArray changed = timestep(g);
	DoubleArray final = DoubleArray(g.size());
	for (DoubleArray::iterator i = g.begin(); i !=g.end(); ++i){
		ICoord c = i.coord();
		final[c] = changed[c] - g[c];
	}
	return final;
}

Geometric::Geometric(double t) {
	time = t;
	type = GEOMETRIC;
}

/*
Takes ONE timestep via Anti-Geometric function.
Anti geometric equation: I(t + 1) = I(t) + dt*dI/dt
dI/dt = (dx^2*dyy - 2dx*dy*dxy + dy^2*dxx)/(dx^2 + dy^2)
*/
DoubleArray Geometric::timestep(DoubleArray g){
	DoubleArray gray = DoubleArray(g);
	DoubleArray size = gray.size();
	ICoord center;
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
	for (DoubleArray::iterator i = gray.begin(); i !=gray.end(); ++i){
		center = i.coord();
		double change;
		double a = dx_mask[center]*dx_mask[center]*dyy_mask[center];
		double b = dx_mask[center]*dy_mask[center]*dxy_mask[center];
		double c = dy_mask[center]*dy_mask[center]*dxx_mask[center];
		double d = dx_mask[center]*dx_mask[center] + dy_mask[center]*dy_mask[center];
		if (d == 0) /* to avoid division by zero */
			change = 0;
		else 
			change = (a -2*b+c)/(d);
		newgray[center] = gray[center] + time*change; /* I(t + 1) = I(t) + dt*(dI/dt) */
	}
	return newgray;

}

/*
Returns the change between the timestep function, and the original function. Changed - original.
*/
DoubleArray Geometric::change(DoubleArray g){
	DoubleArray changed = timestep(g);
	DoubleArray final = DoubleArray(g.size());
	for (DoubleArray::iterator i = g.begin(); i !=g.end(); ++i){
		ICoord c = i.coord();
		final[c] = changed[c] - g[c];
	}
	return final;
}


LargeLaplace::LargeLaplace(double t) {
	time = t;
	type = LARGELAPLACE;
}

/*
Takes ONE timestep with following mask.
Mask is '-1's in 5x5 around each center point, with the center point at 24 each time.
*/
DoubleArray LargeLaplace::timestep(DoubleArray gray){
	DoubleArray changes = DoubleArray(gray.size());
	DoubleArray newgray = DoubleArray(gray.size());
	ICoord center;
	Mask mask = Mask(Mask::LAPLACE_MASK);
	changes = mask.applyMask(gray);
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		center = i.coord();
		newgray[center] = gray[center] + time*changes[center]; /* I(t + 1) = I(t) + dt*(dI/dt) */
	}
	return newgray;
}

/*
Returns the change between the timestep function, and the original function. Changed - original.
*/
DoubleArray LargeLaplace::change(DoubleArray g){
	DoubleArray changed = timestep(g);
	DoubleArray final = DoubleArray(g.size());
	for (DoubleArray::iterator i = g.begin(); i !=g.end(); ++i){
		ICoord c = i.coord();
		final[c] = changed[c] - g[c];
	}
	return final;
}

Laplace::Laplace(double t) {
	time = t;
	type = LAPLACE;
}


/*
Takes ONE timestep with second derivative -> laplace.
Mask is '-1's in 3x3 around each center point, with the center point at 8 each time.
*/
DoubleArray Laplace::timestep(DoubleArray gray){
	DoubleArray changes = DoubleArray(gray.size());
	DoubleArray newgray = DoubleArray(gray.size());
	ICoord center;
	Mask mask = Mask(Mask::SMALL_LAPLACE_MASK);
	changes = mask.applyMask(gray);
	for (DoubleArray::iterator i = gray.begin();i !=gray.end(); ++i){
		center = i.coord();
		newgray[center] = gray[center] + time*changes[center]; /* I(t + 1) = I(t) + dt*(dI/dt) */
	}
	return newgray;
}

/*
Returns the change between the timestep function, and the original function. Changed - original.
*/
DoubleArray Laplace::change(DoubleArray g){
	DoubleArray changed = timestep(g);
	DoubleArray final = DoubleArray(g.size());
	for (DoubleArray::iterator i = g.begin(); i !=g.end(); ++i){
		ICoord c = i.coord();
		final[c] = changed[c] - g[c];
	}
	return final;
}

LargeGaussian::LargeGaussian() {
	type = LARGEGAUSSIAN;
}

/*
convolving the image with a Gaussian or normal distribution -> http://en.wikipedia.org/wiki/Gaussian_blur.
This is a 5x5 mask.
See mask.C for more information. 
*/
DoubleArray LargeGaussian::timestep(DoubleArray gray){
	DoubleArray changes = DoubleArray(gray.size());
	Mask mask = Mask(Mask::GAUSSIAN_MASK);
	changes = mask.applyMask(gray);
	return changes;
}

/*
Returns the change between the timestep function, and the original function. Changed - original.
*/
DoubleArray LargeGaussian::change(DoubleArray g){
	DoubleArray changed = timestep(g);
	DoubleArray final = DoubleArray(g.size());
	for (DoubleArray::iterator i = g.begin(); i !=g.end(); ++i){
		ICoord c = i.coord();
		final[c] = changed[c] - g[c];
	}
	return final;
}

Gaussian::Gaussian() {
	type = GAUSSIAN;
}

/*
convolving the image with a Gaussian or normal distribution -> http://en.wikipedia.org/wiki/Gaussian_blur.
Applies a smaller mask than largeGaussian-> 3x3.
See mask.C for more information. 
*/
DoubleArray Gaussian::timestep(DoubleArray gray){
	DoubleArray changes = DoubleArray(gray.size());
	Mask mask = Mask(Mask::SMALL_GAUSSIAN_MASK);
	changes = mask.applyMask(gray);
	return changes;
}

/*
Returns the change between the timestep function, and the original function. Changed - original.
*/
DoubleArray Gaussian::change(DoubleArray g){
	DoubleArray changed = timestep(g);
	DoubleArray final = DoubleArray(g.size());
	for (DoubleArray::iterator i = g.begin(); i !=g.end(); ++i){
		ICoord c = i.coord();
		final[c] = changed[c] - g[c];
	}
	return final;
}
