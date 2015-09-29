// -*- C++ -*-
// $RCSfile: fixborders.swg,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:35 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef FIX_BORDERS_SWG
#define FIX_BORDERS_SWG

%module fixborders
%include "common/typemaps.swg"
%extern "common/doublearray.swg"
%pragma(python) code="from oof2.SWIG.common.doublearray import DoubleArrayPtr"

%{
#include "image/SEGMENTATION/fixborders.h"
#include "common/doublearray.h"
%}

class Fixing{

}

%pragma(python) include="image/SEGMENTATION/fixborders.spy"
class FixBorders: public Fixing{
	public:
		FixBorders(int, bool);
		void touchBorders(DoubleArray, double );
		DoubleArray connectBorders(DoubleArray);
		DoubleArray deleteSmallClumps(DoubleArray, int);
		DoubleArray fix(DoubleArray);
		
};

class NoFix: public Fixing{
	public: 
		NoFix();
		DoubleArray fix(DoubleArray );
};


#endif
 
 
