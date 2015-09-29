// -*- C++ -*-
// $RCSfile: segmenter.C,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:41:37 $

/* This software was produced by NIST, an agency of the U.S. government,
* and by statute is not subject to copyright in the United States.
* Recipients of this software assume all responsibilities associated
* with its operation, modification and maintenance. However, to
* facilitate maintenance we ask that before distributing modified
* versions of this software, you first contact the authors at
* oof_manager@nist.gov. 
*/


#include "image/SEGMENTATION/segmenter.h"
#include <math.h>
#include <iostream>
#include "image/oofimage.h"
#include "common/array.h"
#include "common/doublearray.h"
#include <cstdio>
#include "common/coord.h"
#include "common/boolarray.h"
#include "image/SEGMENTATION/canny.h"
#include "image/SEGMENTATION/fixborders.h"
#include <string>
#include "image/SEGMENTATION/classify.h"
#include "image/SEGMENTATION/skeletonize.h"

 


/*
Only draws straight lines so far. (like on same row or column)
*/


void doClassifying(DoubleArray & gray){
	ICoord size = gray.size();
	DoubleArray newgray = DoubleArray(size);
	ClassifyClass classif = ClassifyClass();
	newgray = classif.classifyRegions(gray);
	gray = newgray;

}



