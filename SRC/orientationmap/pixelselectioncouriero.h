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

#ifndef PIXELSELECTIONCOURIERO_H
#define PIXELSELECTIONCOURIERO_H

#include "common/pixelselectioncourier.h"
#include "orientationmap/orientmapdata.h"

class LatticeSymmetry;
class COrientation;

class OrientationSelection : public PixelSelectionCourier {
private:
  const COrientation *orientation;
  const LatticeSymmetry *symmetry;
  const double misorientation;
  ICoord currentPt;
  const OrientMap *orientmap;
  OrientMap::const_iterator map_iter;
  void advance();
  bool outOfRange(const ICoord&) const;
public:
  OrientationSelection(const OrientMap*, const COrientation*,
		       const std::string &ls, double);
  virtual ~OrientationSelection();
  virtual void start();
  virtual ICoord currentPoint() const;
  virtual void next();
  virtual void print(std::ostream&) const;
};

#endif // PIXELSELECTIONCOURIERO_H
