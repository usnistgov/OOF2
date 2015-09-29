// -*- C++ -*-
// $RCSfile: mask.h,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:41:31 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef MASK_H
#define MASK_H


#include "common/array.h"
#include "common/coord.h"
#include "common/doublearray.h"

// TODO: Change MASK to Mask
// TODO: Derive Mask from Array<double>.

class MASK {
public:
  MASK(int M,int N); //M and N should be odd
  virtual ~MASK() {}
  int width(); //Returns width of the mask
  int height(); //Returns height of the mask
  DoubleArray maskArray; //Array that stores the values of the mask.
  virtual DoubleArray applyMask(const DoubleArray& image); //Function that applies the mask to an image that is stored as an Array<double>
};

#endif //MASK_H
