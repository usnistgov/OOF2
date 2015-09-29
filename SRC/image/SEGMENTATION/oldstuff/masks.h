// -*- C++ -*-
// $RCSfile: masks.h,v $
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

#include <oofconfig.h>

#ifndef MASKS_H
#define MASKS_H


#include "common/array.h"
#include "common/coord.h"
#include "common/doublearray.h"

// TODO: Change MASK to Mask
// TODO: Derive Mask from Array<double>.

class MASKS {
public:
  MASKS(int M,int N); //M and N should be odd
  virtual ~MASKS() {}
  int width(); //Returns width of the mask
  int height(); //Returns height of the mask
  DoubleArray maskArrays; //Array that stores the values of the mask.
  virtual DoubleArray applyMasks(const DoubleArray& image); //Function that applies the mask to an image that is stored as an Array<double>
};

#endif //MASK_H
