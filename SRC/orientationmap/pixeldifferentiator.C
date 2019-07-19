// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "orientationmap/pixeldifferentiator.h"
#include "orientationmap/orientmapdata.h"
#include "common/latticesystem.h"
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
