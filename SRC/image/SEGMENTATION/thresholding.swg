// -*- C++ -*-
// $RCSfile: thresholding.swg,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:41:36 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef THRESHOLDING_SWG
#define THRESHOLDING_SWG

%module thresholding
%include "common/typemaps.swg"
%extern "common/doublearray.swg"
%pragma(python) code="from oof2.SWIG.common.doublearray import DoubleArrayPtr"
%{
#include "image/SEGMENTATION/thresholding.h"
#include "common/doublearray.h"
%}

class Thresholding{

};

%pragma(python) include="image/SEGMENTATION/thresholding.spy"

class Canny : public Thresholding{
	public:
		Canny(double lowerThreshold, double upperThreshold);
		DoubleArray threshold(DoubleArray original);
};

class RegularThresholding : public Thresholding {
	public:
		RegularThresholding(DiffusionRHS d, int n, double th);
		DoubleArray threshold(DoubleArray original);
		DoubleArray parse(DoubleArray original);
};

class NewGabor : public Thresholding{
	public:
		NewGabor(int a, int b, int numAngles, int line_color, double t1, double t2);
		DoubleArray threshold(DoubleArray original);
}

class OddThresholding : public Thresholding {
	public:
		OddThresholding(DiffusionRHS d, double tr);
		DoubleArray threshold(DoubleArray original);
		DoubleArray parse(DoubleArray original);
};

class NoThresholding : public Thresholding {
	public:
		NoThresholding();
		DoubleArray threshold (DoubleArray original);
};
#endif
 
