// -*- C++ -*-
// $RCSfile: boolarray.h,v $
// $Revision: 1.12 $
// $Author: langer $
// $Date: 2014/05/29 14:38:02 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef BOOLARRAY_H
#define BOOLARRAY_H

#include "common/array.h"
#include <vector>
#include <iostream>

class BoolArray : public Array<bool> {
public:
  BoolArray() {}
#if DIM == 2
  BoolArray(int w, int h) : Array<bool>(w, h) {}
#elif DIM == 3
  BoolArray(int w, int h, int d): Array<bool>(w, h, d) {}
#endif
  BoolArray(const ICoord &size, bool x=false) : Array<bool>(size, x) {}
  BoolArray(const ICoord &size, ArrayData<bool> *dptr)
    : Array<bool>(size, dptr)
  {}
  BoolArray(const Array<bool> &other) : Array<bool>(other) {}

  virtual ~BoolArray() {}
  BoolArray clone() const;
  BoolArray subarray(const ICoord &crnr0, const ICoord &crnr1);
  const BoolArray subarray(const ICoord &crnr0, const ICoord &crnr1) const;
  virtual void clear(const bool&);
  void set(const ICoord &pxl) { (*this)[pxl] = true; }
  void reset(const ICoord &pxl) { (*this)[pxl] = false; }
  bool get(const ICoord &pxl) const { return (*this)[pxl]; }
  void toggle(const ICoord &pxl) { (*this)[pxl] ^= 1; }
  // pointer versions to keep SWIG happy
  void set(const ICoord *pxl) { (*this)[*pxl] = true; }
  void reset(const ICoord *pxl) { (*this)[*pxl] = false; }
  bool get(const ICoord *pxl) { return (*this)[*pxl]; }
  void toggle(const ICoord *pxl) { (*this)[*pxl] ^= 1; }
  void invert();
  int nset() const;
  bool empty() const;
  std::vector<ICoord> *pixels(bool) const; // returns new'd vector
};


#endif // BOOLARRAY_H
