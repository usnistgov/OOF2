// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ORIENT_BURN_H
#define ORIENT_BURN_H

#include <oofconfig.h>

#include "common/cmicrostructure.h"
#include "common/pixelselectioncourier.h"
#include "image/burn.h"
#include "orientationmap/orientmapdata.h"

class OrientationBurner : public Burner<COrientABG, OrientMap> {
 public:
  double local_flammability;
  double global_flammability;
  const LatticeSystem *lattice;
  OrientationBurner(double lcl, double glbl, const std::string &ls, bool nn);
  virtual bool spread(const COrientABG &from, const COrientABG &to) const;
};

// Not sure why OrientationBurner and OrientBurnSelection have to be
// separate classes, except that that's how it's done in other pixel
// selection methods.

// TODO: BurnSelection (in pixelselectioncourieri.*) and this class
// should share code.

class OrientBurnSelection : public PixelSelectionCourier {
private:
  OrientationBurner *burner;
  OrientMap *orientmap;
  const ICoord spark;
  BoolArray selected;
  BoolArray::iterator sel_iter;
  void advance();
public:
  OrientBurnSelection(const CMicrostructure*, OrientationBurner*, OrientMap*,
		      const ICoord*);
  virtual ~OrientBurnSelection() {}
  virtual void start();
  virtual ICoord currentPoint() const;
  virtual void next();
  virtual void print(std::ostream &os) const;
};

#endif // ORIENT_BURN_H
