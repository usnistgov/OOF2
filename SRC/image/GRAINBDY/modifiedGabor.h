// -*- C++ -*-
// $RCSfile: modifiedGabor.h,v $
// $Revision: 1.8 $
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

#ifndef MODIFIEDGABOR_H
#define MODIFIEDGABOR_H

#include "common/array.h"
#include "mask.h"
#include "common/doublearray.h"

class ModGabor : public MASK
{
private:
  DoubleArray weights;
  double weightedArea;
  DoubleArray findImageMeans(const DoubleArray& image) const;
public:
  ModGabor(int a,int b, double phi);
  virtual ~ModGabor() {}
  virtual DoubleArray applyMask(const DoubleArray& image);
  DoubleArray setImage(const DoubleArray& image);
};

#endif //MODIFIEDGABOR_H
