/* -*- C++ -*-
 $RCSfile: diffusionRHS.h,v $
 $Revision: 1.7 $
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
#include "common/doublearray.h"
#include "common/coord.h" 

#ifndef DIFFUSION_RHS_H
#define DIFFUSION_RHS_H

/*
All of the ways to do diffusion decend from DiffusionRHS. This is done for SWIGGING. I have problems with when thresholding is done, the default timestep is always done, so this is why in constructors I specify what each diffusion step is. Then it can be 're-initialized' in the thresholding functions. If more diffusion methods are added, more const static int variables need to be added and thresholding.C needs to be changed. 

Summary of what the diffusion models are--
AntiGeometric: Diffuses across lines. For more information see paper by Manay and Yezzi: Anti-Geometric Diffusion for Adaptive Thresholding and Fast Segmentation. Works well for thresholding, bad for blurring.
Geometric: Diffuses along lines. Works bad for thresholding, good for blurring. 'opposite' or anti-geometric. 
LaPlace: Second derivative of each pixel. Mask is 3x3, with '-1's all around the center pixel, which is 8. 
LargeLaplace: A larger LaPlace, which I am not even sure how to name. It is a 5x5 mask, with '-1's all around the center pixel, which is 24.
Gaussian: Basic 'blurring' gaussian. Like a laplace, but it weighs pixels that are closer to center more. See mask.C for actual mask. This is a 3x3 mask.
LargeGaussian: Same as gaussian but a 5x5 mask.
*/

class DiffusionRHS {
	public:
		const static int ANTIGEOMETRIC = 1;
		const static int GEOMETRIC = 2;
		const static int LAPLACE = 3;
		const static int LARGELAPLACE = 4;
		const static int GAUSSIAN = 5;
		const static int LARGEGAUSSIAN = 6;
		const static int NOTYPE = 7;
		DiffusionRHS();
		double time;
		double type;
		virtual DoubleArray timestep(DoubleArray gray){ return gray;};
};

class AntiGeometric: public DiffusionRHS {
	public:
		AntiGeometric(double time);
		AntiGeometric(const AntiGeometric & other){ time = other.time;};
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
};

class Geometric: public DiffusionRHS {
	public:
		Geometric(double time);
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
};

class Laplace: public DiffusionRHS {
	public:
		Laplace(double time);
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
};

class LargeLaplace: public DiffusionRHS {
	public:
		LargeLaplace(double time);
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
};

class Gaussian: public DiffusionRHS {
	public:
		Gaussian();
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
};

class LargeGaussian: public DiffusionRHS {
	public:
		LargeGaussian();
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
};

class NoDiffusion: public DiffusionRHS {
	public:
		NoDiffusion(){ type = NOTYPE; };
		DoubleArray timestep(DoubleArray gray){ return gray;};
		DoubleArray change(DoubleArray g){ return g;};
};

#endif
