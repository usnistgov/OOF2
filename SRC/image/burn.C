// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// OLD BURN MACHINERY

#include <oofconfig.h>

#include "common/boolarray.h"
#include "common/ccolor.h"
#include "common/cmicrostructure.h"
#include "image/burn.h"
#include "image/oofimage.h"
#include <vector>

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

BurnerBase::Nbr BurnerBase::neighbor;

BurnerBase::Nbr::Nbr() {
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
    double global_dist = L2dist2(startvalue, to);
    return local_dist < local_flammability*local_flammability &&
      global_dist < global_flammability*global_flammability;
  }
  else {
    double local_dist = L1dist(from, to);
    double global_dist = L1dist(startvalue, to);
    return local_dist < local_flammability && global_dist < global_flammability;
  }
}
