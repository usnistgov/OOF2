// -*- C++ -*-
// $RCSfile: newGabor.h,v $
// $Revision: 1.2 $
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

#ifndef NEWGABOR_H
#define NEWGABOR_H

#include "mask.h"
#include "common/doublearray.h"

class NewGF : public MASK
{
public:
  NewGF(int a, int b, double phi); 
  virtual ~NewGF() {}
};

#endif //NEWGABOR_H
