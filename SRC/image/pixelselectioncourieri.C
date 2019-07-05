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
#include "common/cmicrostructure.h"
#include "image/pixelselectioncourieri.h"
#include "image/oofimage.h"

ColorSelection::ColorSelection(CMicrostructure *ms, OOFImage *immidge,
			       const CColor *color,
			       const ColorDifference *diff)
  : PixelSelectionCourier(ms),
    image(immidge),
    color(color->clone()),
    diff(diff->clone()),
    selected(ms->sizeInPixels(), false),
    sel_iter(selected.begin()) {}

ColorSelection::~ColorSelection() {
  delete color;
  delete diff;
}

void ColorSelection::start() {
  image->getColorPoints(*color, *diff, selected);  // get the pixel array
  if (!*sel_iter) next();
}

ICoord ColorSelection::currentPoint() const {
  return sel_iter.coord();
}

void ColorSelection::advance() {
  if(sel_iter.done()) // if it's at the end of pixel array
    done_ = true;
  else
    ++sel_iter;
}

void ColorSelection::next() {
  advance();
  while(!*sel_iter && !done_) 
    advance();
}

void ColorSelection::print(std::ostream &os) const {
  os << "ColorSelection()";
}

//////////


BurnSelection::BurnSelection(CMicrostructure *ms,
			     const CPixelDifferentiator *pixdiff,
			     const ICoord *pt,
			     bool next_nearest)
  : PixelSelectionCourier(ms),
    pixdiff(pixdiff),
    spark(*pt),
    next_nearest(next_nearest)
{
  sel_iter = selected.begin();
}

void BurnSelection::start() {
  SimpleArray2D<bool> alreadyDone(ms->sizeInPixels());
  selected = burn(ms, pixdiff, next_nearest, spark,
		  ms->getActiveArea(),
		  alreadyDone);
  sel_iter = selected.begin();
  done_ = (sel_iter == selected.end());
}

ICoord BurnSelection::currentPoint() const {
  return *sel_iter;
}

void BurnSelection::next() {
  ++sel_iter;
  done_ = (sel_iter == selected.end());
}

void BurnSelection::print(std::ostream &os) const {
  os << "BurnSelection()";
}

