/* -*- C++ -*-
 $RCSfile: fixborders.h,v $
 $Revision: 1.8 $
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
#include "common/boolarray.h"
#include "image/oofimage.h"
#include "common/coord.h"

#ifndef FIX_BORDERS_H
#define FIX_BORDERS_H 

/*
This class encompases all of the functions dealing with attempting to connect non-connected edges after thresholding, and deleting 'clumps' that are not connected to the actual edges. 

All decend from Fixing class for swigging purposes. 
*/


class Fixing {

};

class FixBorders: public Fixing{
	private:
		bool pixelInBounds(ICoord pxl, ICoord size);
		void burn_nbrs(DoubleArray & image, std::vector<ICoord> &activesites, BoolArray &burned, int &nburnt, const ICoord & here, double startcolor, std::vector<ICoord> & all);
		std::vector<ICoord> burn(DoubleArray & image, BoolArray & burned, ICoord spark);
		int numClump;
		int connectNeighbors;
		DoubleArray classified;
	public:
		FixBorders(int numClump, bool connectNeighbors);
		FixBorders();
		void touchBorders(DoubleArray &final, double lowerThreshold);
		DoubleArray connectBorders(DoubleArray gray);
		DoubleArray deleteSmallClumps(DoubleArray gray, int threshold);
		DoubleArray fix(DoubleArray original);
		
};

class NoFix: public Fixing{
	public:
	NoFix();
	DoubleArray fix(DoubleArray a){ return a;};

};

#endif
