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

#include "common/burn.h"
#include "common/ccolor.h"
#include "image/oofimage.h"
#include "image/pixeldifferentiator.h"

#include <set>
#include <algorithm>


CColorDifferentiator::CColorDifferentiator(const OOFImage *image,
					   double lf, double gf, bool l2)
  : image(image),
    local_flammability(lf),
    global_flammability(gf),
    useL2norm(l2)
{}

bool CColorDifferentiator::operator()(const ICoord &target,
				      const ICoord &local_reference,
				      const ICoord &global_reference)
  const
{
  const CColor trgt = (*image)[target];
  const CColor lcl = (*image)[local_reference];
  const CColor glbl = (*image)[global_reference];
  
  if(useL2norm) {
    double local_dist = L2dist2(trgt, lcl);
    double global_dist = L2dist2(trgt, glbl);
    return (local_dist < local_flammability*local_flammability &&
	    global_dist < global_flammability*global_flammability);
  }
  else {
    double local_dist = L1dist(trgt, lcl);
    double global_dist = L1dist(trgt, glbl);
    return local_dist < local_flammability && global_dist < global_flammability;
  }
}

