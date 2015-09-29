// -*- C++ -*-
// $RCSfile: close.h,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:41:28 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/array.h"
#include "common/boolarray.h"
#include "common/doublearray.h"

#ifndef CLOSERS_H
#define CLOSERS_H


class DoubleArray;
class BoolArray;

class CloserClass{
	public:
	BoolArray dilate(const BoolArray & image, const DoubleArray & pattern);
	BoolArray erode(const BoolArray&, const DoubleArray&);
	BoolArray close(const BoolArray&,int);
};

#endif //CLOSE_H
