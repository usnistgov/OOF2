// -*- C++ -*-
// $RCSfile: skeletonize.swg,v $
// $Revision: 1.8 $
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


#ifndef SKELETONIZE_SEGMENTED_SWG
#define SKELETONIZE_SEGMENTED_SWG

%module skeletonize
%include "common/typemaps.swg"
%extern "common/doublearray.swg"
%pragma(python) code="from oof2.SWIG.common.doublearray import DoubleArrayPtr"
%{
#include "image/SEGMENTATION/skeletonize.h"
#include "common/doublearray.h"
%}
class Skeletonizing{

};
%pragma(python) include="image/SEGMENTATION/skeletonize.spy"

class NoSkeletonize: public Skeletonizing{
	public:
		NoSkeletonize();
		DoubleArray skeletonize(DoubleArray & a){ return a;};
};

class Skeletonize: public Skeletonizing{
	public:
  		Skeletonize(bool, bool);
  		DoubleArray thinEdges(DoubleArray gray);
 		DoubleArray skeletonize(DoubleArray&);
 		DoubleArray deleteLeafs(DoubleArray gray);
		
};

#endif 

