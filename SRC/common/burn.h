// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef BURNCOMMON_H
#define BURNCOMMON_H

#include <oofconfig.h>
#include <vector>

#include "common/array.h"

class ActiveArea;
class CMicrostructure;
class ICoord;

// CPixelDifferentiator3 is the base class for objects that say
// whether or not pixels are different, used in the Burn algorithm.
// The 3 is because its operator() takes 3 ICoord arguments.

class CPixelDifferentiator3 {
public:
  virtual ~CPixelDifferentiator3() {}
  // The first ICoord is the pixel being considered for selection.
  // The second is an immediate neighbor that has already been
  // selected, and the third is the pixel where the burn started.
  virtual bool operator()(const ICoord&, const ICoord&, const ICoord&) const=0;
};

// CPixelDifferentiator2 is used for burn-like algorithms that don't
// use a local comparison.  

// CPixelDifferentiator2 was added for use in an auto-grouping method
// (in burn.C) that was replaced by statgroups.C.  It's not currently
// used elsewhere, but it *could* be used by ColorSelection in
// image/pixelselectioncourieri.C, for example.

class CPixelDifferentiator2 {
public:
  virtual ~CPixelDifferentiator2() {}
  // The first ICoord is the pixel being considered for selection.
  // The second is the pixel where the burn started.
  virtual bool operator()(const ICoord&, const ICoord&) const = 0;
  // distance2 is the square of the distance between the pixel values
  // in pixel value space (color, orientation, etc).
  virtual double distance2(const ICoord&, const ICoord&) const = 0;
};


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// burn() selects a contiguous set of similar pixels, where "similar"
// is defined by the given CPixelDifferentiator3.  The selected pixels
// are returned.  next_nearest should be true if diagonally adjacent
// pixels should be considered to be contiguous. seed is the location
// where the burn starts.  The burn is limited to the given
// ActiveArea, and only pixels not marked in alreadyDone will be
// burned.

std::vector<ICoord> burn(CMicrostructure *ms,
			 const CPixelDifferentiator3 *pixdiff,
			 bool next_nearest,
			 const ICoord &seed,
			 const ActiveArea *activeArea,
			 SimpleArray2D<bool> &alreadyDone);


#endif // BURNCOMMON_H
