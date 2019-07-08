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

// CPixelDifferentiator is the base class for objects that say whether
// or not pixels are different, used in the Burn algorithm. 

class CPixelDifferentiator {
public:
  virtual ~CPixelDifferentiator() {}
  // The first ICoord is the pixel being considered for selection.
  // The second is an immediate neighbor that has already been
  // selected, and the third is the pixel where the burn started.
  virtual bool operator()(const ICoord&, const ICoord&, const ICoord&) const=0;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// burn() selects a contiguous set of similar pixels, where "similar"
// is defined by the given CPixelDifferentiator.  The selected pixels
// are returned.  next_nearest should be true if diagonally adjacent
// pixels should be considered to be contiguous. seed is the location
// where the burn starts.  The burn is limited to the given
// ActiveArea, and only pixels not marked in alreadyDone will be
// burned.

std::vector<ICoord> burn(CMicrostructure *ms,
			 const CPixelDifferentiator *pixdiff,
			 bool next_nearest,
			 const ICoord &seed,
			 const ActiveArea *activeArea,
			 SimpleArray2D<bool> &alreadyDone);

// autograin() uses burn() to put every pixel in a pixel group by
// picking a random seed, starting a burn, grouping all the burned
// pixels, and repeating until all pixels in the CMicrostructure's
// ActiveArea have been burned.

const std::string *autograin(CMicrostructure*,
			     const CPixelDifferentiator*,
			     bool next_nearest,
			     const std::string &group_name_template);

#endif // BURNCOMMON_H
