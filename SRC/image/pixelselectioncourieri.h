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

#ifndef PIXELSELECTIONCOURIERI_H
#define PIXELSELECTIONCOURIERI_H

#include "common/pixelselectioncourier.h"
class OOFImage;
class CColor;
class ColorDifference;
class CPixelDifferentiator3;

// Color Difference 
class ColorSelection : public PixelSelectionCourier {
private:
  OOFImage *image;
  const CColor *color;
  const ColorDifference *diff;
  BoolArray selected;
  BoolArray::iterator sel_iter;
  void advance();
public:
  ColorSelection(CMicrostructure *ms, OOFImage *immidge,
		 const CColor *color, const ColorDifference *diff);
  virtual ~ColorSelection();
  virtual void start();
  virtual ICoord currentPoint() const;
  virtual void next();
  virtual void print(std::ostream &os) const;
};

// Burn
class BurnSelection : public PixelSelectionCourier {
private:
  const CPixelDifferentiator3 *pixdiff;
  const ICoord spark;
  bool next_nearest;
  std::vector<ICoord> selected;
  std::vector<ICoord>::const_iterator sel_iter;
public:
  BurnSelection(CMicrostructure*,
		const CPixelDifferentiator3*,
		const ICoord*,
		bool);
  virtual ~BurnSelection() {}
  virtual void start();
  virtual ICoord currentPoint() const;
  virtual void next();
  virtual void print(std::ostream &os) const;
};

#endif // PIXELSELECTIONCOURIERI_H
