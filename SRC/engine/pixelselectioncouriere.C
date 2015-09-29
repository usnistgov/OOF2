// -*- C++ -*-
// $RCSfile: pixelselectioncouriere.C,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2014/09/27 21:40:50 $

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
#include "common/coord.h"
#include "engine/cskeleton.h"
#include "engine/cskeleton.h"
#include "engine/pixelselectioncouriere.h"
#include "engine/material.h"

ElementSelection::ElementSelection(const CMicrostructure *ms,
				   const CSkeletonElement *element)
  : PixelSelectionCourier(ms),
    element(element),
    selected(0) {}

ElementSelection::~ElementSelection() {
  delete selected;
}

void ElementSelection::start() {
  selected = element->underlying_pixels(*ms);  // get the pixel vector
  sel_iter = selected->begin();
}

ICoord ElementSelection::currentPoint() const {
  return *sel_iter;
}

void ElementSelection::next() {
  if (sel_iter == selected->end()-1 )
    done_ = true;
  else
    ++sel_iter;
}

void ElementSelection::print(std::ostream &os) const {
  os << "ElementSelection()";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

SegmentSelection::SegmentSelection(const CMicrostructure *ms,
				   const Coord *n0, const Coord *n1)
  : PixelSelectionCourier(ms),
    n0(*n0),
    n1(*n1),
    selected(0) {}

SegmentSelection::~SegmentSelection() {
  delete selected;
}

void SegmentSelection::start() {
  bool dummy;
  selected = ms->segmentPixels(n0, n1, dummy);  // get the pixel array
  sel_iter = selected->begin();
}

ICoord SegmentSelection::currentPoint() const {
  return *sel_iter;
}

void SegmentSelection::next() {
  if(sel_iter == selected->end()-1 )
    done_ = true;
  else
    ++sel_iter;
}

void SegmentSelection::print(std::ostream &os) const {
  os << "SegmentSelection()";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

MaterialSelectionBase::MaterialSelectionBase(const CMicrostructure *ms)
  : PixelSelectionCourier(ms)
{
  const Array<PixelAttribute*> &mmap = getConstMaterialMap(ms);
  iter = mmap.begin();
  iterend = mmap.end();
}

void MaterialSelectionBase::start() {
  if(!ok(getMaterialFromPoint(ms, &iter.coord())))
    next();
}

ICoord MaterialSelectionBase::currentPoint() const {
  return iter.coord();
}

void MaterialSelectionBase::next() {
  if(!done_)
    ++iter;
  while(iter!=iterend && !ok(getMaterialFromPoint(ms, &iter.coord()))) {
    ++iter;
  }
  done_ = iter==iterend;
}

MaterialSelection::MaterialSelection(const CMicrostructure *ms,
				     const Material *mat)
  : MaterialSelectionBase(ms),
    material(mat)
{}

bool MaterialSelection::ok(const Material *mat) const {
  return mat == material;
}

void MaterialSelection::print(std::ostream &os) const {
  os << "MaterialSelection(" << material->name() << ")";
}

AnyMaterialSelection::AnyMaterialSelection(const CMicrostructure *ms)
  : MaterialSelectionBase(ms)
{}

bool AnyMaterialSelection::ok(const Material *mat) const {
  return mat != 0;
}

void AnyMaterialSelection::print(std::ostream &os) const {
  os << "AnyMaterialSelection()";
}

NoMaterialSelection::NoMaterialSelection(const CMicrostructure *ms)
  : MaterialSelectionBase(ms)
{}

bool NoMaterialSelection::ok(const Material *mat) const {
  return mat == 0;
}

void NoMaterialSelection::print(std::ostream &os) const {
  os << "NoMaterialSelection()";
}
