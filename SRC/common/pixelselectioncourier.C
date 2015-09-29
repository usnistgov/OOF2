// -*- C++ -*-
// $RCSfile: pixelselectioncourier.C,v $
// $Revision: 1.19 $
// $Author: langer $
// $Date: 2014/09/27 21:40:26 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "common/ccolor.h"
#include "common/colordifference.h"
#include "common/cmicrostructure.h"
#include "common/pixelselectioncourier.h"
#include "common/printvec.h"
#if DIM==2
#include "common/brushstyle.h"
#endif
#include <math.h>
#include <iostream>
#include <iomanip>

PixelSelectionCourier::PixelSelectionCourier(const CMicrostructure *ms)
  : ms(ms),
    done_(false)
 {}

ICoord PixelSelectionCourier::pixelFromPoint(const Coord &pt) const {
  return ms->pixelFromPoint(pt);
}

//////////

PointSelection::PointSelection(const CMicrostructure *ms, const Coord *mp)
  : PixelSelectionCourier(ms),
    mousepoint(*mp) {}

ICoord PointSelection::currentPoint() const {
  return pixelFromPoint(mousepoint);
}

void PointSelection::next() {
  done_ = true;
}

//////////
#if DIM==2
BrushSelection::BrushSelection(const CMicrostructure *ms, BrushStyle *brush,
			       const std::vector<Coord> *points)
  : PixelSelectionCourier(ms),
    brush(brush),
    points(*points),
    master(ms->sizeInPixels()),
    offset(0, 0) {}

void BrushSelection::start() {
  pts_iter = points.begin();  // start from the first point
  brush->getPixels(ms, *pts_iter, master, selected, offset); // get pixels
  sel_iter = selected.begin();
  if (!*sel_iter) next();
}

ICoord BrushSelection::currentPoint() const {
  return sel_iter.coord() + offset;
}

void BrushSelection::advance() {
  if(sel_iter.done()) {  // if it's at the end of pixel array
    if (pts_iter == points.end()-1 ) {  // if it's also at the end of points
      done_ = true;
    }
    else {  // to the next point
      ++pts_iter;
      brush->getPixels(ms, *pts_iter, master, selected, offset);
      sel_iter.reset();
    }
  }
  else {
    ++sel_iter;
  }
}

void BrushSelection::next() {
  advance();
  while(!*sel_iter && !done_) 
    advance();
}
#endif

///////////

RectangleSelection::RectangleSelection(const CMicrostructure *ms,
				       const Coord *ll, const Coord *ur)
  : PixelSelectionCourier(ms),
    ll(pixelFromPoint(*ll)),
    ur(pixelFromPoint(*ur))
{
}

void RectangleSelection::start() {
  currentpt = ll;
}

ICoord RectangleSelection::currentPoint() const {
  return currentpt;
}

void RectangleSelection::next() {
  currentpt(0)++;
  if(currentpt(0) > ur(0)) {
    currentpt(0) = ll(0);
    currentpt(1)++;
  }
  if(currentpt(1) > ur(1))
    done_ = true;
}

//////////

CircleSelection::CircleSelection(const CMicrostructure *ms,
				 const Coord *c, const double r,
				 const Coord *ll, const Coord *ur)
  : PixelSelectionCourier(ms),
    center(*c),
    radius2(r*r),
    ll(pixelFromPoint(*ll)),
    ur(pixelFromPoint(*ur))
{
}

bool CircleSelection::interior() {
  double dx = (currentpt(0)+0.5)*ms->sizeOfPixels()(0) - center(0);
  double dy = (currentpt(1)+0.5)*ms->sizeOfPixels()(1) - center(1);
  return (dx*dx+dy*dy <= radius2);
}

void CircleSelection::start() {
  currentpt = ll;
  if (!interior()) next();
}

ICoord CircleSelection::currentPoint() const {
  return currentpt;
}

void CircleSelection::advance() {
  currentpt(0)++;
  if(currentpt(0) > ur(0)) {
    currentpt(0) = ll(0);
    currentpt(1)++;
  }
  if(currentpt(1) > ur(1))
    done_ = true;
}

void CircleSelection::next() {
  // Move to the next slot
  advance();
  // Check if it's a valid point
  while (!interior() && !done())
    advance();
}

//////////

EllipseSelection::EllipseSelection(const CMicrostructure *ms,
				   const Coord *ll, const Coord *ur)
  : PixelSelectionCourier(ms),
    ll(pixelFromPoint(*ll)),
    ur(pixelFromPoint(*ur)),
    center(Coord(0.5*((*ll)(0)+(*ur)(0)), 0.5*((*ll)(1)+(*ur)(1)))),
    aa( 1.0/(0.5*((*ur)(0)-(*ll)(0))*0.5*((*ur)(0)-(*ll)(0))) ),
    bb( 1.0/(0.5*((*ur)(1)-(*ll)(1))*0.5*((*ur)(1)-(*ll)(1))) ) {}

bool EllipseSelection::interior() {
  double dx = (currentpt(0)+0.5)*ms->sizeOfPixels()(0) - center(0);
  double dy = (currentpt(1)+0.5)*ms->sizeOfPixels()(1) - center(1);
  if (dx*dx*aa + dy*dy*bb <= 1.0) return true;
  return false;
}

void EllipseSelection::start() {
  currentpt = ll;
  if (!interior()) next();
}

ICoord EllipseSelection::currentPoint() const {
  return currentpt;
}

void EllipseSelection::advance() {
  currentpt(0)++;
  if(currentpt(0) > ur(0)) {
    currentpt(0) = ll(0);
    currentpt(1)++;
  }
  if(currentpt(1) > ur(1))
    done_ = true;
}

void EllipseSelection::next() {
  // Move to the next slot
  advance();
  // Check if it's a valid point
  while (!interior() && !done_)
    advance();
}

//////////

GroupSelection::GroupSelection(const CMicrostructure *ms,
			       const PixelSet *group)
  : PixelSelectionCourier(ms),
    pgroup(group)
{
}
    
void GroupSelection::start() {
  pxl_iter = pgroup->members()->begin();
  if(pgroup->members()->size() == 0)
    done_ = true;
}

ICoord GroupSelection::currentPoint() const {
  return *pxl_iter;
}

void GroupSelection::next() {
  if (pxl_iter == pgroup->members()->end()-1)
    done_ = true;
  else
    ++pxl_iter;
}

/////////

IntersectSelection::IntersectSelection(const CMicrostructure *ms,
				       const PixelSet *selpix,
				       const PixelSet *grppix)
  : PixelSelectionCourier(ms),
    selpix(selpix),
    grppix(grppix)
{}

void IntersectSelection::start() {
  sel_iter = selpix->members()->begin();
  grp_iter = grppix->members()->begin();
  if(selpix->members()->size() == 0 || grppix->members()->size() == 0)
    done_ = true;
  else if (!(*sel_iter == *grp_iter))
    next();
}
  
ICoord IntersectSelection::currentPoint() const {
  return *sel_iter;
}

void IntersectSelection::advance() {
  if ( (sel_iter == selpix->members()->end()-1) ||
       (grp_iter == grppix->members()->end()-1) ) {
    done_ = true;
  }
  else {
    if (*sel_iter == *grp_iter) {
      ++sel_iter;
      ++grp_iter;
    }
    else if (*sel_iter < *grp_iter)
      ++sel_iter;
    else if (*grp_iter < *sel_iter)
      ++grp_iter;
  }
}

void IntersectSelection::next() {
  advance();
  while (!(*sel_iter == *grp_iter) && !done_) {
    advance();
  }
}


#ifndef DIM_3
DespeckleSelection::DespeckleSelection(const CMicrostructure *ms,
				       const PixelSet *group,
				       const int neighbors)  
  : PixelSelectionCourier(ms),
    pgroup(group),
    neighbors(neighbors),
    selected(ms->sizeInPixels(), false),
    sel_iter(selected.begin()) {}

void DespeckleSelection::start() {
  pgroup->despeckle(neighbors, selected);  // get the pixel array
  if (!*sel_iter) next();
}

ICoord DespeckleSelection::currentPoint() const {
  return sel_iter.coord();
}

void DespeckleSelection::advance() {
  if(sel_iter.done()) // if it's at the end of pixel array
    done_ = true;
  else
    ++sel_iter;
}

void DespeckleSelection::next() {
  advance();
  while(!*sel_iter && !done_) 
    advance();
}

/////////

ElkcepsedSelection::ElkcepsedSelection(const CMicrostructure *ms,
				       const PixelSet *group,
				       const int neighbors)  
  : PixelSelectionCourier(ms),
    pgroup(group),
    neighbors(neighbors),
    selected(ms->sizeInPixels(), false),
    sel_iter(selected.begin()) {}

void ElkcepsedSelection::start() {
  pgroup->elkcepsed(neighbors, selected);  // get the pixel array
  if (!*sel_iter) next();
}

ICoord ElkcepsedSelection::currentPoint() const {
  return sel_iter.coord();
}

void ElkcepsedSelection::advance() {
  if(sel_iter.done()) // if it's at the end of pixel array
    done_ = true;
  else
    ++sel_iter;
}

void ElkcepsedSelection::next() {
  advance();
  while(!*sel_iter && !done_) 
    advance();
}

//////////

ExpandSelection::ExpandSelection(const CMicrostructure *ms,
				 const PixelSet *group,
				 const double radius)  
  : PixelSelectionCourier(ms),
    pgroup(group),
    radius(radius),
    selected(ms->sizeInPixels(), false),
    sel_iter(selected.begin()) {}

void ExpandSelection::start() {
  pgroup->expand(radius, selected);  // get the pixel array
  if (!*sel_iter) next();
}

ICoord ExpandSelection::currentPoint() const {
  return sel_iter.coord();
}

void ExpandSelection::advance() {
  if(sel_iter.done()) // if it's at the end of pixel array
    done_ = true;
  else
    ++sel_iter;
}

void ExpandSelection::next() {
  advance();
  while(!*sel_iter && !done_) 
    advance();
}

//////////

ShrinkSelection::ShrinkSelection(const CMicrostructure *ms,
				 const PixelSet *group,
				 const double radius)  
  : PixelSelectionCourier(ms),
    pgroup(group),
    radius(radius),
    selected(ms->sizeInPixels(), false),
    sel_iter(selected.begin()) {}

void ShrinkSelection::start() {
  pgroup->shrink(radius, selected);  // get the pixel array
  if (!*sel_iter) next();
}

ICoord ShrinkSelection::currentPoint() const {
  return sel_iter.coord();
}

void ShrinkSelection::advance() {
  if(sel_iter.done()) // if it's at the end of pixel array
    done_ = true;
  else
    ++sel_iter;
}

void ShrinkSelection::next() {
  advance();
  while(!*sel_iter && !done_) 
    advance();
}
#endif // DIM_3
/////////

// Output here is just for debugging, so it is sort of skeletal in spots.

std::ostream &operator<<(std::ostream &os, const PixelSelectionCourier &psc) {
  psc.print(os);
  return os;
}

void PointSelection::print(std::ostream &os) const {
  os << "PointSelection(" << mousepoint << ")";
}

#if DIM==2
void BrushSelection::print(std::ostream &os) const {
  os << "BrushSelection()";
}
#endif

void RectangleSelection::print(std::ostream &os) const {
  os << "RectangleSelection(" << ll << ", " << ur << ")";
}

void CircleSelection::print(std::ostream &os) const {
  os << "CircleSelection(" << center << ", " << sqrt(radius2) << ")";
}

void EllipseSelection::print(std::ostream &os) const {
  os << "EllipseSelection(" << ll << ", " << ur << ")";
}

void GroupSelection::print(std::ostream &os) const {
  os << "GroupSelection(" << pgroup->len() << ")";
}

void IntersectSelection::print(std::ostream &os) const {
  os << "IntersectSelection()";
}

#ifndef DIM_3
void DespeckleSelection::print(std::ostream &os) const {
  os << "DespeckleSelection()";
}

void ElkcepsedSelection::print(std::ostream &os) const {
  os << "ElkcepsedSelection()";
}

void ExpandSelection::print(std::ostream &os) const {
  os << "ExpandSelection()";
}

void ShrinkSelection::print(std::ostream &os) const {
  os << "ShrinkSelection()";
}
#endif // DIM_3
