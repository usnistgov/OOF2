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

#include "common/latticesystem.h"
#include "common/tostring.h"
#include "orientationmap/orientmapdata.h"
#include "orientationmap/pixeldifferentiator.h"

#include <math.h>

COrientationDifferentiator3::COrientationDifferentiator3(
					       const OrientMap *om,
					       double lf,
					       double gf,
					       const std::string &schoenflies)
  : orientmap(om),
    local_flammability(lf),
    global_flammability(gf),
    lattice(getLatticeSymmetry(schoenflies))
{}

bool COrientationDifferentiator3::operator()(const ICoord &target,
					    const ICoord &local_reference,
					    const ICoord &global_reference)
  const
{
  const COrientABG &tgt = orientmap->angle(target);
  const COrientABG &lcl = orientmap->angle(local_reference);
  const COrientABG &gbl = orientmap->angle(global_reference);
  double degrees = 180./M_PI;
  return (degrees*tgt.misorientation(lcl, *lattice) < local_flammability &&
	  degrees*tgt.misorientation(gbl, *lattice) < global_flammability);
}
    
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

COrientationDifferentiator2::COrientationDifferentiator2(
					       const OrientMap *om,
					       double gf,
					       const std::string &schoenflies)
  : orientmap(om),
    misorientation(gf),
    lattice(getLatticeSymmetry(schoenflies))
{}

bool COrientationDifferentiator2::operator()(const ICoord &target,
					    const ICoord &global_reference)
  const
{
  const COrientABG &tgt = orientmap->angle(target);
  const COrientABG &gbl = orientmap->angle(global_reference);
  double degrees = 180./M_PI;
  return (degrees*tgt.misorientation(gbl, *lattice) < misorientation);
}
    
double COrientationDifferentiator2::distance2(const ICoord &p0,
					      const ICoord &p1)
  const
{
  const COrientABG &o0 = orientmap->angle(p0);
  const COrientABG &o1 = orientmap->angle(p1);
  double degrees = 180./M_PI;
  double misor = degrees*o0.misorientation(o1, *lattice);
  return misor*misor;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

OrientationPixelDistribution::OrientationPixelDistribution(
		   const ICoord &pixel,
		   const OrientMap *omap,
		   double sigma0,
		   const LatticeSymmetry *lat)
  : var0(sigma0*sigma0),
    variance(sigma0*sigma0),
    mean(omap->angle(pixel).axis()),
    lattice(lat),
    orientmap(omap)
{
  pxls.push_back(pixel);
}

OrientationPixelDistribution::OrientationPixelDistribution(
				   const std::set<ICoord> &pixels,
				   const OrientMap *omap,
				   double sigma0,
				   const LatticeSymmetry *lat)
  : var0(sigma0*sigma0),
    mean(0, 1.0, 0, 0),		// will be overwritten immediately
    lattice(lat),
    orientmap(omap)
{
  pxls.insert(pxls.begin(), pixels.begin(), pixels.end());
  
  auto iter = pixels.begin();
  mean = omap->angle(*iter).axis();
  int n = 1;
  ++iter;
  for( ; iter!=pixels.end(); ++iter, ++n) {
    mean = mean.weightedAverage(n, 1.0, omap->angle(*iter), *lattice);
  }
  findVariance();
}

PixelDistribution *OrientationPixelDistribution::clone(
					       const std::set<ICoord> &pxls) 
  const 
{
  OrientationPixelDistribution *newpd = new OrientationPixelDistribution(
					 pxls, orientmap, var0, lattice);
  return newpd;
}

void OrientationPixelDistribution::findVariance() {
  // The variance has to be recomputed from scratch each time a pixel
  // is added.  This is slow.  A faster approximate (wrong?) method
  // would be to pretend that the new point doesn't shift the
  // mean. Compute the new point's misorientation squared from the new
  // mean, and add it to the sum of the old misorientations squared
  // (without recomputing them).
  variance = 0;
  for(const ICoord &pixel : pxls) {
    double misorient = orientmap->angle(pixel).misorientation(mean, *lattice);
    variance += misorient*misorient;
  }
  double degrees = 180./M_PI;
  variance *= degrees*degrees/npts();
}

void OrientationPixelDistribution::add(const ICoord &pt) {
  mean = mean.weightedAverage(npts(), 1.0, orientmap->angle(pt), *lattice);
  pxls.push_back(pt);
  findVariance();
}

void OrientationPixelDistribution::merge(const PixelDistribution *othr) {
  int nOld = npts();
  const OrientationPixelDistribution *other =
    dynamic_cast<const OrientationPixelDistribution*>(othr);
  pxls.insert(pxls.end(), other->pxls.begin(), other->pxls.end());
  mean = mean.weightedAverage(nOld, other->npts(), other->mean, *lattice);
  findVariance();
}

double OrientationPixelDistribution::deviation2(const ICoord &pt) const {
  double misorient = mean.misorientation(orientmap->angle(pt), *lattice) *
    180./M_PI;
  return misorient*misorient;
}

double OrientationPixelDistribution::deviation2(const PixelDistribution *othr)
  const 
{
  const OrientationPixelDistribution *other =
    dynamic_cast<const OrientationPixelDistribution*>(othr);
  double misorient = mean.misorientation(other->mean, *lattice) * 180./M_PI;
  return misorient*misorient;
}

#ifdef DEBUG

std::string OrientationPixelDistribution::stats() const {
  return to_string(mean) + " +/- " + to_string(sqrt(variance));
}

std::string OrientationPixelDistribution::value(const ICoord &pt) const {
  return to_string(orientmap->angle(pt));
}

#endif // DEBUG

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

OrientationPixelDistFactory::OrientationPixelDistFactory(
				 const OrientMap *omap, double sigma0,
				 const std::string &latticename)
  : orientmap(omap),
    sigma0(sigma0),
    lattice(getLatticeSymmetry(latticename))
{}

PixelDistribution *OrientationPixelDistFactory::newDistribution(
							const ICoord &pt)
  const
{
  return new OrientationPixelDistribution(pt, orientmap, sigma0, lattice);
}
