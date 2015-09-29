/* -*- C++ -*-
 $RCSfile: classify.h,v $
 $Revision: 1.9 $
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
#include <stdio.h>
#include <math.h>
#include "common/doublearray.h"
#include "image/oofimage.h"
#include "common/boolarray.h"

#ifndef CLASSIFYING_H
#define CLASSIFYING_H

/*
Classifies the image by intensity. Groups together touching like colors. Changes each neighboring color to a different color, so that is easier seen. Done on a binary image. 

Uses the burn algorithm from pixel selection. Works fast and doesnt overflow. 
*/


class ClassifyClass {
	private:
		bool pixelInBounds(ICoord px1, ICoord size);
		void burn_nbrs(DoubleArray & image, std::vector<ICoord> &activesites, BoolArray &burned, int &nburnt, const ICoord & here, double startcolor, double changecolor);
		
	public:
		void burn(DoubleArray & image);
		ClassifyClass();
};

#endif
