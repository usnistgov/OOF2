// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/activearea.h"
#include "common/array.h"
#include "common/burn.h"
#include "common/ccolor.h"
#include "common/cmicrostructure.h"
#include "common/pixelgroup.h"
#include "common/progress.h"
//#include "common/random.h"

#include <set>
#include <algorithm>

// Select a bunch of pixels by starting with one, and spreading
// outwards like a forest fire.  The selection spreads from one pixel
// to one of its neighbors if the difference between the pixel and the
// neighbor isn't too large, and if the difference between the
// original pixel where the fire started and the neighbor isn't too
// large.  What "too large" means and how the differences are computed
// is determined by the CPixelDifferentiator3 subclass that's passed
// in as an argument.


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// NbrList provides an easy of looping over neighboring
// pixels. NbrList[i] is the relative position of the i^th
// neighbor. The nearest neighbors come before the next nearest
// neighbors to make it possible to loop over only the nearest
// neighbors.

class NbrList {
private:
  ICoord nbr[8];
public:
  NbrList() {
    nbr[0] = ICoord( 0, -1);
    nbr[1] = ICoord(-1,  0);
    nbr[2] = ICoord( 1,  0);
    nbr[3] = ICoord( 0,  1);
    nbr[4] = ICoord(-1, -1);
    nbr[5] = ICoord( 1, -1);
    nbr[6] = ICoord(-1,  1);
    nbr[7] = ICoord( 1,  1);
  }
  const ICoord &operator[](int x) const { return nbr[x]; }
};

static NbrList neighbor;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::vector<ICoord> burn(CMicrostructure *ms,
			 const CPixelDifferentiator3 *pixdiff,
			 bool next_nearest,
			 const ICoord &seed, const ActiveArea *activeArea,
			 SimpleArray2D<bool> &alreadyDone)
{
  std::vector<ICoord> burned;	// pixels that have been burned
  std::vector<ICoord> activeSites; // sites whose neighbors have to be checked
  activeSites.reserve(ms->sizeInPixels()[0]*ms->sizeInPixels()[1]);
  int nnbrs = (next_nearest ? 8 : 4);
  
  // burn the first pixel
  burned.push_back(seed);
  activeSites.push_back(seed);
  while(activeSites.size() > 0) {
    // Remove the last site in the active list, burn its neighbors,
    // and add them to the list.
    const ICoord here = activeSites.back();
    activeSites.pop_back();

    // Loop over neighbors of the current point.
    for(unsigned int i=0; i< nnbrs; i++) {
      ICoord target = here + neighbor[i]; // candidate for burning
      if(activeArea->isActive(target)
	 && alreadyDone.contains(target) // target is w/in microstructure
	 && !alreadyDone[target]	 // target hasn't already been burned
	 && (*pixdiff)(target, here, seed)) // target meets burn criterion
	{
	  burned.push_back(target);
	  activeSites.push_back(target);
	  alreadyDone[target] = true;
	}
    }
  }
  return burned;
}


