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
#include "common/random.h"

#include <set>
#include <algorithm>

// This is yet another refactoring of the algorithm in image/burn.h.
// If this is done correctly, that file should be able to use this
// one.



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
			 const CPixelDifferentiator *pixdiff,
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

    // Loop over neighbors
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

#include <random>

const std::string *autograin(CMicrostructure *ms,
			     const CPixelDifferentiator *pixdiff,
			     bool next_nearest,
			     const std::string &name_template)
{
  ICoord mssize(ms->sizeInPixels());
  const ActiveArea *activeArea = ms->getActiveArea();

  Progress *progress =
    dynamic_cast<DefiniteProgress*>(findProgress("AutoGrain"));
  
  // alreadyDone[pixel] is true if the pixel is already in a grain
  SimpleArray2D<bool> alreadyDone(mssize);
  int ngroups = 0;		// number of pixel groups created
  int npix = 0;			// number of pixels checked

  // shuffledPix is a list of all possible starting points for the
  // burn algorithm.  It's randomized to prevent bias.
  std::vector<ICoord> shuffledPix;
  shuffledPix.reserve(mssize[0]*mssize[1]);
  for(unsigned int i=0; i<mssize[0]; i++)
    for(unsigned int j=0; j<mssize[1]; j++) {
      ICoord pix(i, j);
      if(activeArea->isActive(pix)) {
	shuffledPix.push_back(pix);
      }
    }
  OOFRandomNumberGenerator r;
  oofshuffle(shuffledPix.begin(), shuffledPix.end(), r);
  
  std::string groupname;
  
  for(const ICoord seed : shuffledPix) {
    if(progress->stopped())
      break;
    if(!alreadyDone[seed]) {
      std::vector<ICoord> grain = burn(ms, pixdiff, next_nearest,
				       seed, activeArea, alreadyDone);
      assert(grain.size() > 0);
      npix += grain.size();
      
      // Construct a name for the pixel group
      groupname = name_template;
      std::string::size_type pos = groupname.find("%n", 0);
      if(pos != std::string::npos)
	groupname = groupname.replace(pos, 2, to_string(ngroups));
      ngroups++;

      // Create the pixel group
      bool newness = false;
      PixelGroup *grp = ms->getGroup(groupname, &newness);
      // Add pixels to the group. No need to check the active area --
      // we only burned active pixels.
      grp->addWithoutCheck(&grain);

      progress->setFraction(float(npix)/(mssize[0]*mssize[1]));
    } // end if seed hasn't already been put in a group
  }   // end loop over seed pixels

  if(!progress->stopped())
    return new std::string(groupname);
  return new std::string("");
} // end autograin()


