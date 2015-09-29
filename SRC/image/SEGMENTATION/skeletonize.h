 /* -*- C++ -*-
 $RCSfile: skeletonize.h,v $
 $Revision: 1.8 $
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
#include <math.h>
#include "common/doublearray.h"
#include "image/oofimage.h"
#include "common/boolarray.h"

#ifndef SKELETONIZING_H
#define SKELETONIZING_H

/*
Skeletonizing is thinning lines (white) in an image until they are only one pixel wide. Minimal lines in order to preserve connectivity. This is useful so that there is minimal borders and they can be expanded upon. 
Decended from Skeletonizing for convenient Swigging. 
*/

class Skeletonizing{

};


class NoSkeletonize: public Skeletonizing{
	public:
	DoubleArray skeletonize(DoubleArray & a){ return a;};
	NoSkeletonize(){ };
};

class Skeletonize: public Skeletonizing{
	private:
		int numNonZeroTransitions(ICoord center, DoubleArray gray);
		int numBorderSides(ICoord center, DoubleArray list, int type);
		bool pixelInBounds(ICoord pxl, ICoord size);
		bool isDeletable(const BoolArray&,ICoord);
		bool satisfiesStep1(const BoolArray&,ICoord);
		bool satisfiesStep2(const BoolArray&,ICoord);
		bool isContour(const BoolArray &image,const ICoord pt);
		bool deleteLooseEnds;
		bool useMyVersion;
		int numSideEmpty(ICoord center, DoubleArray list, int type, int allSides);
	public:
		Skeletonize(bool a, bool b){ deleteLooseEnds = a; useMyVersion = b;};
		DoubleArray thinEdges(DoubleArray gray);
		DoubleArray skeletonize(DoubleArray&);
		DoubleArray deleteLeafs(DoubleArray gray);
		
};



#endif

 
