 // -*- C++ -*-
// $RCSfile: diffusionRHS.swg,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:41:34 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */


#ifndef DIFFUSION_RHS_SWG
#define DIFFUSION_RHS_SWG

%module diffusionRHS
%include "common/typemaps.swg"
%extern "common/doublearray.swg"
%pragma(python) code="from oof2.SWIG.common.doublearray import DoubleArrayPtr"

%{
#include "image/SEGMENTATION/diffusionRHS.h"
#include "common/doublearray.h"
#include "image/oofimage.h"
#include "common/coord.h"
%}

class DiffusionRHS {
	public:
		DiffusionRHS();
		virtual DoubleArray timestep(DoubleArray gray);
};

%pragma(python) include="image/SEGMENTATION/diffusionRHS.spy"

class AntiGeometric: public DiffusionRHS {
	public:
		AntiGeometric(double);
		DoubleArray timestep(DoubleArray);
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
}

class LargeLaplace: public DiffusionRHS {
	public:
		LargeLaplace(double time);
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
}

class Gaussian: public DiffusionRHS {
	public:
		Gaussian();
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
}

class LargeGaussian: public DiffusionRHS {
	public:
		LargeGaussian();
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
}

class NoDiffusion: public DiffusionRHS {
	public:
		NoDiffusion();
		DoubleArray timestep(DoubleArray gray);
		DoubleArray change(DoubleArray g);
};


#endif 

