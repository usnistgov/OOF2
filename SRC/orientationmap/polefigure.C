// -*- C++ -*-
// $RCSfile: polefigure.C,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2012/04/24 19:53:48 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/cmicrostructure.h"
#include "common/direction.h"
#include "common/pixelgroup.h"
#include "common/smallmatrix.h"
#include "engine/crystalsymmetry.h"
#include "engine/material.h"
#include "orientationmap/orientmapdata.h"
#include "orientationmap/orientmapproperty.h"
#include "orientationmap/polefigure.h"

#include <math.h>
#include <limits>

PoleFigure::PoleFigure(const CMicrostructure *ms,
		       const PixelSet *pixset,
		       const AnisoCrystalSymmetry *symmetry,
		       const CDirection *pole,
		       int nBins,
		       bool hemisphere)
  : nBins(nBins),
    totalCounts(0),
    counts(nBins, nBins),
    minVal(std::numeric_limits<double>::max()),
    maxVal(-std::numeric_limits<double>::max())
{
  const RotationSet *rotations = getEquivalentRotations(*symmetry);

  rProj = hemisphere? sqrt(2.) : 2; // radius of projection
  binSize = 2*rProj/nBins;

  if(pixset != 0) {		// Hack. See _makePoleFigure in polefigure.spy
    // Loop over pixels
    const std::vector<ICoord> *pxls = pixset->members();
    for(std::vector<ICoord>::const_iterator i=pxls->begin(); i<pxls->end(); ++i)
      totalCounts += processPixel(*i, rotations, pole, ms);
  }
  else {			// pixset==0 ==> Use all pixels
    const Array<PixelAttribute*> &matlmap = getConstMaterialMap(ms);
    for(Array<PixelAttribute*>::const_iterator ij=matlmap.begin();
	ij!=matlmap.end(); ++ij)
      {
	totalCounts += processPixel(ij.coord(), rotations, pole, ms); 
      }
  }

  // Normalization is that a uniform distribution has a density of one
  // everywhere (Multiples of Random Distribution).  The area of the
  // projection is pi*rProj^2.
  double factor = M_PI*rProj*rProj/totalCounts;
  for(int i=0; i<nBins; i++)
    for(int j=0; j<nBins; j++)
      if(inside(i, j)) {
	  double v = counts(i, j) * factor;
	  counts(i,j) = v;
	  if(v > maxVal)
	    maxVal = v;
	  if(v < minVal)
	    minVal = v;
	}
}

bool PoleFigure::inside(int i, int j) const {
  int ii = 2*i - nBins;		// twice the distance from the center
  int jj = 2*j - nBins;
  return (i >= 0 && i < nBins && j >= 0 && j < nBins 
	  && ii*ii + jj*jj <= nBins*nBins);
}

int PoleFigure::processPixel(const ICoord &ij, const RotationSet *rotations,
			     const CDirection *pole,
			     const CMicrostructure *ms)
{
  int ndone = 0;
  // Get the orientation at this pixel
  const Material *matl = getMaterialFromPoint(ms, &ij);
  if(!matl)
    return 0;
  const OrientationPropBase *orientationProp = 
    dynamic_cast<OrientationPropBase*>(matl->fetchProperty("Orientation"));
  if(orientationProp) {
    const COrientation *orient = orientationProp->orientation(ms, ij);
    CUnitVectorDirection rpole = orient->rotation()*(*pole);
    // Loop over equivalent directions from the crystal symmetry
    for(int d=0; d<rotations->size(); d++) {
      const SmallMatrix *rot = (*rotations)[d];
      CUnitVectorDirection dir = (*rot)*rpole;
      double theta = dir.theta();
      double phi = dir.phi();
      // Equal area projection
      double r = 2*sin(theta/2.);
      double x = rProj + r*cos(phi);
      double y = rProj + r*sin(phi);
      // Bin
      int ix = x/binSize + 0.5;
      int iy = y/binSize + 0.5;
      if(inside(ix, iy))
	counts(ix, iy) += 1.0;
      ++ndone;
    }	// end loop over equivalent directions
  }	// end if orientationProp
  return ndone;
}

