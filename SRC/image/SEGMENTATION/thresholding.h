/* -*- C++ -*-
 $RCSfile: thresholding.h,v $
 $Revision: 1.11 $
 $Author: langer $
 $Date: 2014/09/27 21:41:36 $

 This software was produced by NIST, an agency of the U.S. government,
 and by statute is not subject to copyright in the United States.
 Recipients of this software assume all responsibilities associated
 with its operation, modification and maintenance. However, to
 facilitate maintenance we ask that before distributing modified
 versions of this software, you first contact the authors at
 oof_manager@nist.gov. */
#include <oofconfig.h>
#include "common/doublearray.h"
#include "common/boolarray.h"
#include "common/coord.h"
#include <stdio.h>
#include <typeinfo>
#include <iostream>
#include "image/SEGMENTATION/canny.h"
#include "image/SEGMENTATION/diffusionRHS.h"
 
#ifndef THRESHOLDING_H
#define THRESHOLDING_H

/*
Combination of different types of thresholding ideas. 
1. Simple thresholding. If change is above certain value, tag that as a border, if not, then it is background. Something can also be tagged as a border if it steadily grows through time. If the intensity decreases then automatically tagged as a non-border.
2. Canny Algorith: Uses combination of gradient and hysteresis thresholding. For more information see image/SEGMENTATION/canny.h
3. NewGabor: Uses a gabor filter and then hysteresis thresholding. For more information see image/SEGMENTATION/newgabor.h
4. ExperimentalThresholding: Attempt at region merging technique. Doesnt work currently. 
*/


struct area{ /* used in the region merging segmentation.. that doesnt work yet */
	std::vector<ICoord> members;
	std::vector<ICoord> neighbors;
	int size;
	double sum_intensities;
	double squared_sum_intensities;
	double mean_intensity;
	double squared_error;
	double color;
};


class Thresholding{
	public:
	void burn_nbrs(DoubleArray & image, std::vector<ICoord> &activesites, BoolArray &burned, int &nburnt, const ICoord & here, double startcolor, std::vector<ICoord> & all);
	std::vector<ICoord> burn(DoubleArray & image, BoolArray & burned, ICoord spark);
};

class NewGabor : public Thresholding{
	private:
		int a;
		int b;
		int numAngles;
		int line_color;
		double t1;
		double t2;
		DoubleArray newGabors(const DoubleArray& image,int a,int b,double phi);
		DoubleArray findLargerValss(const DoubleArray &arr1, const DoubleArray &arr2);
		DoubleArray scaleArrays(const DoubleArray& arr, double min, double max,int lineColor);
		BoolArray hysteresisThreshs(const DoubleArray& image, double T1, double T2);
	public:
		NewGabor(int a, int b, int numAngles, int line_color, double t1, double t2);
		DoubleArray threshold(DoubleArray original);
};


class Canny : public Thresholding{
	private:
		double lowerThreshold;
		double upperThreshold;
	public:
		Canny(double lowerThreshold, double upperThreshold);
		DoubleArray threshold(DoubleArray original);
};

class RegularThresholding : public Thresholding {
	private:
		double t;
		DiffusionRHS diff;
		int num;
		
	public:
		RegularThresholding(DiffusionRHS d, int n, double th);
		DoubleArray threshold(DoubleArray original);
		DoubleArray parse(DoubleArray original);	
};


class OddThresholding : public Thresholding {
	private:
		DiffusionRHS diff;
		double t;
		void setNeighbors(ICoord size, std::vector<ICoord> & array, ICoord curr);
		int findNeighbor(std::vector<area> all_areas, area here, std::vector<ICoord> neighbors);
	public:
		OddThresholding(DiffusionRHS d, double tr);
		DoubleArray threshold(DoubleArray original);
		DoubleArray parse(DoubleArray original);
};

class NoThresholding : public Thresholding {
	public:
		NoThresholding(){ return; };
		DoubleArray threshold (DoubleArray changed){ return changed;};
};

#endif
