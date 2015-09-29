// -*- C++ -*-
// $RCSfile: igf.h,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:41:30 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
//Class that stores a Imaginary Gabor Filter and applies it to an image.

#ifndef IGF_H
#define IGF_H

#include "mask.h"

class ImagGF : public MASK
{
public:
  ImagGF(int a, int b, double phi); 
  virtual ~ImagGF() {}
//  void define(int a,int b, double phi);
};

#endif //IGF_H

