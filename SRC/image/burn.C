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
#include "common/boolarray.h"
#include "common/ccolor.h"
#include "common/cmicrostructure.h"
#include "image/burn.h"
#include "image/oofimage.h"
#include <vector>

template <class BURNABLE, class IMAGE>
void Burner<BURNABLE, IMAGE>::burn(const IMAGE &image, const ICoord *spark,
				   BoolArray &burned)
{
  // Initialize the data structures.
  int nburnt = 0;
  startcolor = image[spark];
  std::vector<ICoord> activesites; // sites whose neighbors have to be checked
  activesites.reserve(image.sizeInPixels()(0)*image.sizeInPixels()(1));

  // burn the first pixel
  burned[*spark] = true;
  nburnt++;
  activesites.push_back(*spark);

  while(activesites.size() > 0) {
    // Remove the last site in the active list, burn its neighbors,
    // and add them to the list.
    int n = activesites.size() - 1;
    const ICoord here = activesites[n];
    activesites.pop_back();
    burn_nbrs(image, activesites, burned, nburnt, here);
  }
}

template <class BURNABLE, class IMAGE>
void Burner<BURNABLE, IMAGE>::burn_nbrs(const IMAGE &image,
				 std::vector<ICoord> &activesites,
				 BoolArray &burned, int &nburnt,
				 const ICoord &here) {
  // Burn neighboring pixels and put them in the active list.
  const ActiveArea *aa = image.getCMicrostructure()->getActiveArea();
  int nbrmax = (next_nearest? 8 : 4);
  BURNABLE thiscolor(image[here]);
  for(int i=0; i<nbrmax; i++) {
    ICoord target = here + neighbor[i];
    if(aa->isActive(&target) && burned.contains(target) && !burned[target]
       && spread(thiscolor, image[target])) {
      burned[target] = true;
      nburnt++;
      activesites.push_back(target);
    }
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

template <class BURNABLE, class IMAGE>
typename Burner<BURNABLE, IMAGE>::Nbr Burner<BURNABLE, IMAGE>::neighbor;

template <class BURNABLE, class IMAGE>
Burner<BURNABLE, IMAGE>::Nbr::Nbr() {
  // don't change the order here without changing Burner::burn_nbrs(),
  // or the nearest neighbor/next nearest neighbor distinction will be
  // screwed up.
  nbr[0] = ICoord( 0, -1);
  nbr[1] = ICoord(-1,  0);
  nbr[2] = ICoord( 1,  0);
  nbr[3] = ICoord( 0,  1);
  nbr[4] = ICoord(-1, -1);
  nbr[5] = ICoord( 1, -1);
  nbr[6] = ICoord(-1,  1);
  nbr[7] = ICoord( 1,  1);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// I'm not sure why we have to force instantiation of this template,
// because it's used explicitly in burn.h, but apparently it's
// necessary:
template class Burner<CColor, OOFImage>;

bool BasicBurner::spread(const CColor &from, const CColor &to) const {
  if(useL2norm) {
    double local_dist = L2dist2(from, to);
    double global_dist = L2dist2(startcolor, to);
    return local_dist < local_flammability*local_flammability &&
      global_dist < global_flammability*global_flammability;
  }
  else {
    double local_dist = L1dist(from, to);
    double global_dist = L1dist(startcolor, to);
    return local_dist < local_flammability && global_dist < global_flammability;
  }
}
