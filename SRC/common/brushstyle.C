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

#include "common/brushstyle.h"
#include "common/cmicrostructure.h"
#include "common/geometry.h"
#include <math.h>
#include "printvec.h"

// TODO: Allow brush size to be specified in pixels as well as
// physical units?

void CircleBrush::getPixels(const CMicrostructure *ms,
			    const Coord &c, BoolArray &master,
			    BoolArray &selected, ICoord &offset)
{
  // Called by BrushSelection::start and BrushSelection::advance in
  // pixelselectioncourier.C.
  
  // selected is an array of pixels that are selected by the brush
  // when the brush is centered at point c.  Because selected will be
  // iterated over by BrushSelection (in pixelselectioncourier.C),
  // it's only as big as the brush and its position in the
  // Microstructure is determined by offset.  The array master keeps
  // track of all pixels that have been selected by this brush stoke,
  // to prevent pixels from being selected more than once.  master is
  // as large as the microstructure.
  
  // If r is smaller than max(psize(0)/2, psize(1)/2),
  // it returns the pixel position of the given mouse point.
  if (2.0*r<=ms->sizeOfPixels()(0) || 2.0*r<=ms->sizeOfPixels()(1)) {
    offset = ms->pixelFromPoint(c);
    selected.resize(ICoord(1,1));
    if (!master.get(offset)) {
      selected[ICoord(0,0)] = true;
      master[offset] = true;
    }
    return;
  }
  // If r is specified appropriately, it return a list of pixel
  // positions enclosed in the circle.
  const double cx = c(0);
  const double cy = c(1);
  const double rr = r*r;
  Coord ll = ms->physical2Pixel(Coord(cx-r, cy-r));
  Coord ur = ms->physical2Pixel(Coord(cx+r, cy+r));
  const int Xmin = int(ll(0)) - 1;
  const int Xmax = int(ur(0)) + 1;
  const int Ymin = int(ll(1)) - 1;
  const int Ymax = int(ur(1)) + 1;
  selected.resize(ICoord(Xmax-Xmin+1, Ymax-Ymin+1));
  selected.clear(false);
  offset = ICoord(Xmin, Ymin);
  for (int i=Xmin; i<=Xmax; i++) {
    for (int j=Ymin; j<=Ymax; j++) {
      double dx = (i+0.5)*ms->sizeOfPixels()(0) - cx;
      double dy = (j+0.5)*ms->sizeOfPixels()(1) - cy;
      if (dx*dx + dy*dy <= rr) {
	if (ms->contains(ICoord(i,j)))
	  if (!master.get(ICoord(i,j))) { 
	    selected[ICoord(i-Xmin, j-Ymin)] = true;
	    master[ICoord(i,j)] = true;
	  }
      }
    }
  }
}

void SquareBrush::getPixels(const CMicrostructure *ms,
			    const Coord &c, BoolArray &master,
			    BoolArray &selected, ICoord &offset)
{
  // TODO: Fix this.  It appears not to be working in some cases.
  // It's not working in 2.1.19 either.
  // It works on small.ppm if the pixels are 1x1 and the brush size is 10
  // It fails on small.ppm if the ms is 1x1 and the brush size is 0.1
  
  // If a radius is not a positive number, it returns a pixel position of
  // the given mouse point.
  if (2.0*size<=ms->sizeOfPixels()(0) || 2.0*size<=ms->sizeOfPixels()(1)) {
    offset = ms->pixelFromPoint(c);
    selected.resize(ICoord(1,1));
    if (!master.get(offset)) {
      selected[ICoord(0,0)] = true;
      master[offset] = true;
    }
    return;
  }
  // If a r is specified appropriately, it return a list of pixel
  // positions enclosed in the square.
  double cx = c(0);
  double cy = c(1);
  Coord ll = ms->physical2Pixel(Coord(cx-size, cy-size));
  Coord ur = ms->physical2Pixel(Coord(cx+size, cy+size));
  CRectangle rect = CRectangle(ll, ur);
  int Xmin = int(ll(0))-1;
  int Xmax = int(ur(0))+1;
  int Ymin = int(ll(1))-1;
  int Ymax = int(ur(1))+1;
  selected.resize(ICoord(Xmax-Xmin+1, Ymax-Ymin+1));
  selected.clear(false);
  offset = ICoord(Xmin, Ymin);
  for (int i=Xmin; i<=Xmax; i++) {
    for (int j=Ymin; j<=Ymax; j++) {
      double dx = (i+0.5)*ms->sizeOfPixels()(0);
      double dy = (j+0.5)*ms->sizeOfPixels()(1);
      if (rect.contains(Coord(dx, dy)))
	if (ms->contains(ICoord(i,j)))
	  if (!master.get(ICoord(i,j))) {
	    selected[ICoord(i-Xmin, j-Ymin)] = true;
	    master[ICoord(i,j)] = true;
	  }
    }
  }
}

