// -*- C++ -*-
// $RCSfile: cpixelselection.C,v $
// $Revision: 1.18 $
// $Author: langer $
// $Date: 2014/09/27 21:40:19 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include <iostream>
using namespace std;

#include "common/activearea.h"
#include "common/cmicrostructure.h"
#include "common/cpixelselection.h"
#include "printvec.h"

CPixelSelection::CPixelSelection(const ICoord *pxlsize, const Coord *size,
				 CMicrostructure *ms)
  : pixset(pxlsize, ms),
    bitmap(size, pxlsize),
    isize_(*pxlsize),
    size_(*size)
{}

CPixelSelection::CPixelSelection(const CPixelSelection &other)
  : pixset(other.pixset),
    bitmap(&other.size(), &other.sizeInPixels()),
    isize_(other.sizeInPixels()),
    size_(other.size())
{
  bitmap.copy(&other.bitmap);
}

bool CPixelSelection::checkpixel(const ICoord *pixel) const {
  return bitmap.contains(pixel);
}

const ActiveArea *CPixelSelection::getActiveArea() const {
  return getCMicrostructure()->getActiveArea();
}

CMicrostructure *CPixelSelection::getCMicrostructure() const {
  return pixset.getCMicrostructure();
}

const std::vector<ICoord> *CPixelSelection::getActivePixels() const {
  // This returns a new'd vector which must be deleted.  The active
  // pixels are the ones *not* set in the bitmap, which is why the
  // argument to getPixels is 0.
  return getActiveArea()->getBitmap()->getPixels(0);
}

void CPixelSelection::clear() {
  if(getActiveArea()->getOverride())
    clearWithoutCheck();
  else {
    const std::vector<ICoord> *activepxls = getActivePixels();
    pixset.remove(activepxls);
    bitmap.reset(activepxls);
    delete activepxls;
  }
  ++timestamp;
}

void CPixelSelection::clearWithoutCheck() {
  pixset.clear();
  bitmap.clear();
  ++timestamp;
}

void CPixelSelection::invert() {
  if(getActiveArea()->getOverride())
    invertWithoutCheck();
  else {
    const std::vector<ICoord> *activepxls = getActivePixels();
    bitmap.toggle(activepxls);
    pixset.clear();
    pixset.setFromBitmap(bitmap);
  }
  ++timestamp;
};

void CPixelSelection::invertWithoutCheck() {
  bitmap.invert();
  pixset.clear();
  pixset.setFromBitmap(bitmap);
  ++timestamp;
};

void CPixelSelection::select(PixelSelectionCourier *selection) {
  const ActiveArea *activearea = getActiveArea();
  if(activearea->getOverride())
    selectWithoutCheck(selection);
  else {
    std::vector<ICoord> okpix;
    selection->start();
    while(!selection->done()) {
      ICoord pixel = selection->currentPoint();
      if(checkpixel(&pixel) && activearea->isActive(&pixel)) {
	bitmap.set(&pixel);
	okpix.push_back(pixel);
      }
      selection->next();
    }
    pixset.add(&okpix);
  }
  ++timestamp;
}

void CPixelSelection::unselect(PixelSelectionCourier *selection) {
  const ActiveArea *activearea = getActiveArea();
  if(activearea->getOverride())
    unselectWithoutCheck(selection);
  else {
    std::vector<ICoord> *pixels = new std::vector<ICoord>;
    selection->start();
    while(!selection->done()) {
      ICoord pixel = selection->currentPoint();
      if(checkpixel(&pixel) && activearea->isActive(&pixel)) {
	bitmap.reset(&pixel);
	pixels->push_back(pixel);
      }
      selection->next();
    }
    pixset.remove(pixels);
    delete pixels;
  }
  ++timestamp;
}

void CPixelSelection::toggle(PixelSelectionCourier *selection) {
  const ActiveArea *activearea = getActiveArea();
  if(activearea->getOverride())
    toggleWithoutCheck(selection);
  else {
    selection->start();
    while(!selection->done()) {
      ICoord pixel = selection->currentPoint();
      if(checkpixel(&pixel) && activearea->isActive(&pixel)) {
	bitmap.toggle(&pixel);
      }
      selection->next();
    }
    pixset.clear();
    pixset.setFromBitmap(bitmap);
  }
  ++timestamp;
}

void CPixelSelection::selectSelected(PixelSelectionCourier *selection) {
  const ActiveArea *activearea = getActiveArea();
  pixset.clear();
  selection->start();
  while(!selection->done()) {
    ICoord pixel = selection->currentPoint();
    if(bitmap.get(&pixel) && activearea->isActive(&pixel))
      pixset.add(pixel);
    selection->next();
  }
  bitmap.clear();
  bitmap.set(pixset.members());
  ++timestamp;
}

void CPixelSelection::selectWithoutCheck(PixelSelectionCourier *selection) {
  std::vector<ICoord> okpix;
  selection->start();
  while(!selection->done()) {
    ICoord pixel = selection->currentPoint();
    if(checkpixel(&pixel)) {
      bitmap.set(&pixel);
      okpix.push_back(pixel);
    }
    selection->next();
  }
  pixset.addWithoutCheck(&okpix);
  ++timestamp;
}

void CPixelSelection::unselectWithoutCheck(PixelSelectionCourier *selection) {
  std::vector<ICoord> *pixels = new std::vector<ICoord>;
  selection->start();
  while(!selection->done()) {
    ICoord pixel = selection->currentPoint();
    if(checkpixel(&pixel)) {
      bitmap.reset(&pixel);
      pixels->push_back(pixel);
    }
    selection->next();
  }
  pixset.removeWithoutCheck(pixels);
  delete pixels;
  ++timestamp;
}

void CPixelSelection::toggleWithoutCheck(PixelSelectionCourier *selection) {
  selection->start();
  while(!selection->done()) {
    ICoord pixel = selection->currentPoint();
    if(checkpixel(&pixel)) {
      bitmap.toggle(&pixel);
    }
    selection->next();
  }
  pixset.clear();
  pixset.setFromBitmap(bitmap);
  ++timestamp;
}

bool CPixelSelection::isSelected(const ICoord *pixel) const {
  return bitmap.get(pixel);
}

const std::vector<ICoord> *CPixelSelection::members() const {
  return pixset.members();
}

int CPixelSelection::len() const {
  return pixset.len();
}

void CPixelSelection::setFromGroup(const PixelSet *grp) {
  bitmap.set(grp->members());
  pixset.setFromBitmap(bitmap);
}
