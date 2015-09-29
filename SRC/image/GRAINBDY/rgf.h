// -*- C++ -*-
// $RCSfile: rgf.h,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:41:32 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
//The class that stores a Real Gabor Filter and can apply it to an image.

#ifndef RGF_H
#define RGF_H

#include "mask.h"
#include "common/doublearray.h"

class RealGF : public MASK
{
public:
  RealGF(int a, int b, double phi); 
  virtual ~RealGF() {}
};

#endif //RGF_H
