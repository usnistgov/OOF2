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
#include <math.h>

#include "common/corientation.h"
#include "common/latticesystem.h"
#include "orientationmap/pixelselectioncouriero.h"

OrientationSelection::OrientationSelection(const OrientMap *ormap,
					   const COrientation *ornt,
					   const std::string &schoenflies,
					   double misor)
  : PixelSelectionCourier(ormap->getCMicrostructure()),
    orientation(ornt),
    symmetry(getLatticeSymmetry(schoenflies)),
    misorientation(M_PI*misor/180.),
    orientmap(ormap)
{}

OrientationSelection::~OrientationSelection() {
  // delete orientation;		// WHO OWNS THIS?
}

void OrientationSelection::start() {
  map_iter = orientmap->begin();
  if(outOfRange(map_iter.coord()))
     next();
}

ICoord OrientationSelection::currentPoint() const {
  return map_iter.coord();
}

void OrientationSelection::advance() {
  // Move to next pixel, unless at the end.
  if(!done_)
    ++map_iter;
  done_ = (map_iter == orientmap->end());
}

void OrientationSelection::next() {
  // Move to the next acceptable pixel.
  advance();
  while(!done_ && outOfRange(map_iter.coord()))
    advance();
}

bool OrientationSelection::outOfRange(const ICoord &pt) const {
  COrientABG localOr = (*orientmap)[pt];
  // std::cerr << "OrientationSelection::outOfRange: pt=" << pt
  // 	    << " localOr=" << localOr << " misorientation="
  // 	    <<  localOr.misorientation(*orientation, *symmetry)
  // 	    << " threshold=" << misorientation
  // 	    << std::endl;
  return localOr.misorientation(*orientation, *symmetry) > misorientation;
}

void OrientationSelection::print(std::ostream &os) const {
  os << "OrientationSelection()";
}
 
