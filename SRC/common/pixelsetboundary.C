// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modifed
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/pixelsetboundary.h"
#include "common/cmicrostructure.h"
#include "common/geometry.h"
#include "common/printvec.h"
#include <limits>
#include <map>
#include <math.h>
#include <assert.h>

static const ICoord iRight(1, 0);
static const ICoord iUp(0, 1);
static const ICoord iLeft(-1, 0);
static const ICoord iDown(0, -1);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// A PixelSetBoundary is a bunch of line segments that form the
// perimeter of a bunch of pixels.  It's used when computing the
// intersection of a pixel set and a finite element.  There are two
// things that it has to do:
//  (1) be able to construct itself efficiently from a set of pixels.
//  (2) be able to compute the area of its intersection with a convex
//  polygon.

// A PixelSetBoundary is stored as a bunch of loops, each defined by a
// set of segments.  Since it's a loop, only the start points of the
// segments are stored.

// The intersection area is computed by clipping each loop with the
// lines that define the sides of the intersecting element.  The sides
// are handled one at a time.  Clipping a loop with one line produces
// a new loop, which is clipped by the next line.  Treating the
// element sides as infinite lines and clipping with each in turn only
// works because the element is assumed to be convex.

// The initial loops in the PixelSetBoundary are instances of
// PixelBdyLoop, which stores its segment ends as ICoords (in the
// pixel coordinate system).  Using ICoords makes the construction of
// loops from pixels robust.  On the other hand, the clipped loops are
// ClippedPixelBdyLoop instances, using Coords because the clipped
// points aren't generally at integer coordinates.

// Clipping a loop by a line entails finding which points are to be
// retained (those on the left side of the clipping line).  New points
// are created by interpolating along the loop segments that cross the
// clipping line.  New points created when the pixel loop leaves the
// clipping region (crosses the line from left to right) are connected
// to the last point in the clipping region and directly to the next
// new point, which is created when the pixel loop re-enters the
// clipping region (crosses the line from right to left).  The line
// connecting the two new points is a segment of the clipping line.
// The resulting loop may contain multiple overlapping collinear
// segments along the clipping line, but they will go in both
// directions and cancel each other out, and their net contribution to
// the loop area will be correct.

// A fundamental difference between this method and the earlier
// methods that we tried is that this one works with one element edge
// at a time, and only has to decide which points are on which side of
// a line, not which points are inside the element.  As such, there's
// never any ambiguity about how new points should be connected.  The
// only possible connection is along the clipping line.

// The big advantage of this method is that it doesn't require us to
// determine the order of intersection points along the element
// perimeter.  Round-off error in that calculation was what caused
// errors in the previous version of
// CSkeletonElement::categoryAreas().  Like r3d, this method is robust
// to round-off error.

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Some geometric utilities

// Is the given point to the left of the given line?

int countleft = 0;		// debugging

template <class COORD>
bool leftside(const COORD &pt, const Line &line) {
  ++countleft;			// debugging
  return cross(line.second - line.first, pt - line.first) > 0.0;
}

// Return the intersection point of the segment (a0, a1) and the line
// through (b0, b1).  The intersection is known to exist -- a0 and a1
// are on different sides of the line.

Coord intersection(const Coord &a0, const Coord &a1,
		   const Coord &b0, const Coord &b1)
{
  double denom = cross(a1-a0, b1-b0);
  assert(denom != 0); // because the segment and line are known to intersect
  double alpha = cross(b0-a0, b1-b0)/denom;
  if(alpha < 0.0)
    return a0;
  if(alpha > 1.0)
    return a1;
  return a0 + alpha*(a1-a0);
}

// This version takes ICoord arguments for the segment.

Coord intersection(const ICoord &a0, const ICoord &a1,
		   const Coord &b0, const Coord &b1)
{
  double denom = cross(a1-a0, b1-b0);
  assert(denom != 0); // because the segment and line are known to intersect
  double alpha = cross(b0-a0, b1-b0)/denom;
  if(alpha < 0.0)
    return Coord(a0(0), a0(1));
  if(alpha > 1.0)
    return Coord(a1(0), a1(1));
  return a0 + (a1-a0)*alpha;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

PixelSetBoundary::PixelSetBoundary(const CMicrostructure* ms, int nx, int ny)
  :  subBdys(nx*ny),
     microstructure(ms),
     nbinsx(nx), nbinsy(ny)
{
}

void PixelSetBoundary::add_pixel(const ICoord &px) {
  // Find which bin the pixel contributes to.
  ICoord mssize = microstructure->sizeInPixels();
  int ix = (px(0)/(double) mssize(0))*nbinsx;
  if(ix >= nbinsx) ix = nbinsx-1;
  int iy = (px(1)/(double) mssize(1))*nbinsy;
  if(iy >= nbinsy) ix = nbinsy-1;
  // Add to the bin.
  subBdys[iy*nbinsx + ix].add_pixel(px);
}

// find_boundary is called by CMicrostructure::categorize() after it
// has called add_pixel for each pixel in the microstructure.

void PixelSetBoundary::find_boundary() {
  for(PixelSetSubBoundary &psb : subBdys)
    psb.find_boundary(microstructure);
}

double PixelSetBoundary::clippedArea(const LineList &lines,
				     const CRectangle &bbox)
  const
{
#ifdef DEBUG
  for(const Line &line : lines)
    assert(line.first != line.second);
#endif // DEBUG
  double area = 0.0;
  for(const PixelSetSubBoundary &subbdy : subBdys) {
    area += subbdy.clippedArea(lines, bbox);
  }
  // Convert back to physical units
  Coord pxlsize = microstructure->sizeOfPixels();
  return area * pxlsize[0] * pxlsize[1];
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

PixelSetSubBoundary::~PixelSetSubBoundary() {
  for(std::vector<PixelBdyLoop*>::iterator i=loopset.begin(); i<loopset.end();
      ++i)
    delete *i;
}

// Add the boundary segments for this pixel to the map of all pixel
// segments.
void PixelSetSubBoundary::add_pixel(const ICoord &px) {
  // Pixel boundary segments are actually just stored as ICoords,
  // which are the left or bottom endpoint of the segment.  The
  // direction of the segment is implied by which SegSet it's in.

  // Insert the L->R segment along the bottom of the pixel unless the
  // R->L one is already present.
  SegSet::iterator old = segmentsRL.find(px);
  if(old == segmentsRL.end())
    segmentsLR.insert(px);
  else
    segmentsRL.erase(old);

  // Insert the R->L segment along the top of the pixel unless the
  // L->R is already present.
  ICoord rl = px + iUp;
  old = segmentsLR.find(rl);
  if(old == segmentsLR.end())
    segmentsRL.insert(rl);
  else
    segmentsLR.erase(old);

  // Insert the U->D segment along the left edge unless the D->U is
  // already present.
  old = segmentsDU.find(px);
  if(old == segmentsDU.end())
    segmentsUD.insert(px);
  else
    segmentsDU.erase(old);

  // Insert the D->U segment along the right edge ...
  ICoord ud = px + iRight;
  old = segmentsUD.find(ud);
  if(old == segmentsUD.end())
    segmentsDU.insert(ud);
  else
    segmentsUD.erase(old);
}


typedef std::pair<ICoord, ICoord> DirectedSeg; // start point, direction

void PixelSetSubBoundary::find_boundary(const CMicrostructure *microstructure) {
  CoordMap cm;
  // After all calls to add_pixel(), the remaining segments are all
  // boundary segments.  Put them in a more convenient map for making
  // connections.  The map key is the starting point of the segment,
  // and the stored value is a pair (DirectedSeg) containing the
  // segment's direction and the pointer to the segment itself.
  for(SegSet::iterator i=segmentsLR.begin(); i!=segmentsLR.end(); ++i)
    cm.insert(DirectedSeg(*i, iRight));
  for(SegSet::iterator i=segmentsDU.begin(); i!=segmentsDU.end(); ++i)
    cm.insert(DirectedSeg(*i, iUp));
  for(SegSet::iterator i=segmentsRL.begin(); i!=segmentsRL.end(); ++i)
    cm.insert(DirectedSeg(*i+iRight, iLeft));
  for(SegSet::iterator i=segmentsUD.begin(); i!=segmentsUD.end(); ++i)
    cm.insert(DirectedSeg(*i+iUp, iDown));

  // There must be at least one segment in each direction.  Find
  // loops, removing segments from the sets, until the sets are empty.
  while(!cm.empty()) {
    loopset.push_back(find_loop(cm));
  }
  assert(cm.empty());

  // Clean up.  Combine colinear contiguous segments and compute
  // bounding boxes. 
  for(std::vector<PixelBdyLoop*>::iterator loop=loopset.begin();
      loop!=loopset.end(); ++loop)
    {
      (*loop)->clean(microstructure);
    }

  segmentsLR.clear();
  segmentsRL.clear();
  segmentsUD.clear();
  segmentsDU.clear();
}

typedef std::pair<CoordMap::iterator, CoordMap::iterator> CoordMapRange;

// Finds a loop in the passed-in coordinate map, and returns it.
// Removes the relevant segments from the cm, also, which is why it's
// a reference and not const.

PixelBdyLoop *PixelSetSubBoundary::find_loop(CoordMap &cm) {
  PixelBdyLoop *loop = new PixelBdyLoop();
  assert(!cm.empty());
  CoordMap::iterator current = cm.begin();

  bool done = false;
  while(!done) {
    ICoord here = (*current).first;
    ICoord direction = (*current).second;
    loop->add_point(here);
    ICoord next = here + direction; // endpoint of the current segment

    cm.erase(current);

    // Look for a segment starting at the end point of this one.
    int n = cm.count(next);
    if(n == 0)
      done = true;
    else if(n == 1) {
      current = cm.lower_bound(next);
    }
    else {
      // There is more than one choice of outgoing segment from the
      // current point.  This can happen only if two pixels in the set
      // touch at a corner, and the other two pixels at the corner are
      // not in the set, checkerboard style. Because the pixels in the
      // set are always on the left of the boundary, we know that
      // there are only two possible situations:  
      // A: The pixels are in the NE and SW corners. The incoming
      //    segments are vertical, and the outgoing segments are
      //    horizontal.  If we come in from the S we go out to the W.
      //    If we come in from the N we go out to the E.
      // B: The pixels are in the NW and SE corners.  The incoming
      //    segments are horizontal and the outgoing segments are
      //    vertical.  If we come in from the E we go out to the S.
      //    If we come in from the W we go out to the N.

      CoordMapRange range = cm.equal_range(next); // possible outgoing segs
      ICoord outgoing = (direction == iUp ? iLeft : // desired outgoing dir
			 (direction == iDown ? iRight :
			  (direction == iRight ? iUp :
			   iDown)));
      for(CoordMap::iterator i=range.first; i!=range.second; i++) {
	if((*i).second == outgoing) {
	  current = i;
	  break;
	}
      }	// loop over outgoing segments
    } // more than one outgoing segment
  } // while !done
  assert(loop->size() >= 4);
  assert(loop->closed());
  return loop;
}

double PixelSetSubBoundary::clippedArea(const LineList &lines,
					const CRectangle &bbox)
  const
{
  double area = 0.0;
  for(PixelBdyLoop *loop : loopset) {
    area += loop->clippedArea(lines, bbox);
  }
  return area;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

template <class CTYPE, class RTYPE>
PxlBdyLoopBase<CTYPE, RTYPE>::PxlBdyLoopBase(const std::vector<CTYPE> &oloop,
					     const RTYPE *rect)
  : loop(oloop),
    bounds(nullptr)
{
  if(rect != nullptr)
    bounds = new CRectangle(*rect);
}

template <class CTYPE, class RTYPE>
PxlBdyLoopBase<CTYPE, RTYPE>::PxlBdyLoopBase(
				     const PxlBdyLoopBase<CTYPE, RTYPE> &other)
  : loop(other.loop)
{
  if(other.bounds)
    bounds = new RTYPE(*other.bounds);
  else
    bounds = nullptr;
}

template <class CTYPE, class RTYPE>
PxlBdyLoopBase<CTYPE, RTYPE>::PxlBdyLoopBase(
				     PxlBdyLoopBase<CTYPE, RTYPE> &&other)
  : loop(std::move(other.loop)),
    bounds(other.bounds)
{
  other.bounds = nullptr;
}

template <class CTYPE, class RTYPE>
PxlBdyLoopBase<CTYPE, RTYPE> &PxlBdyLoopBase<CTYPE, RTYPE>::operator=(
				      const PxlBdyLoopBase<CTYPE, RTYPE> &other)
{
  loop = other.loop;
  if(other.bounds)
    bounds = new RTYPE(*other.bounds);
  else
    bounds = nullptr;
  return *this;
}

double PixelBdyLoop::clippedArea(const LineList &lines, const CRectangle &bbox)
  const
{
  // If there are no clipping lines, return the area of the loop.  If
  // there are lines, clip with the first one, creating new loops, and
  // call clippedArea() on those loops with the remaining lines.
  assert(!lines.empty());
  assert(bounds != nullptr);
  if(!bbox.intersects(*bounds)) {
    return 0.0;
  }
  ClippedPixelBdyLoop curloop(clip(lines[0]));
  for(unsigned int i=1; i<lines.size(); i++) {
    if(curloop.size() == 0) {
      return 0.0;
    }
    ClippedPixelBdyLoop newloop = curloop.clip(lines[i]);
    curloop = newloop;
  }
  return curloop.areaInPixelUnits();
}

template <class CTYPE, class RTYPE>
double PxlBdyLoopBase<CTYPE, RTYPE>::areaInPixelUnits() const {
  if(loop.size() < 3)
    return 0.0;
  CTYPE pt0 = loop[0];
  double sum = 0.0;
  for(unsigned int i=2; i<loop.size(); i++) {
    sum += cross(loop[i-1]-pt0, loop[i]-pt0);
  }
  return 0.5*sum;
}

template <class CTYPE, class RTYPE>
ClippedPixelBdyLoop PxlBdyLoopBase<CTYPE, RTYPE>::clip(const Line &line)
  const
{
  // Return the loop formed by clipping by the given line.

  assert(line.first != line.second);
  // If the loop is empty, its bounding box won't be set, so check
  // that first.
  if(loop.empty()) {
    return ClippedPixelBdyLoop(); // empty loop
  }

  // Count the number of bounding box corners to the left of the
  // clipping line.
  unsigned int nbbleft = 0;
  for(unsigned int i=0; i<4; i++) {
    if(leftside((*bounds)[i], line))
      nbbleft++;
  }
  
  // If nbbleft==0, all of the pixels are to the right of the line (or
  // on it), and the entire loop is clipped away.  Return an empty
  // loop.
  if(nbbleft == 0) {
    return ClippedPixelBdyLoop(); // empty loop
  }
  if(nbbleft == 4) {
    // All of the pixels are to the left of the line, so they're all
    // retained. Don't do anything other than to convert the
    // PixelBdyLoop to a ClippedPixelBdyLoop.

    // TODO: Avoid a copy here by by returning *this if the derived
    // class is ClippedPixelBdyLoop, and returning
    // ClippedPixelBdyLoop(this) if the derived class is PixelBdyLoop.
    return ClippedPixelBdyLoop(this);
  }

  // The line cuts through the loop's bounding box. Actually clip the
  // loop.
  unsigned int n = size();
  bool keepprev = leftside(loop.back(), line);
  unsigned int iprev = n - 1;
  ClippedPixelBdyLoop newloop;
  newloop.reserve(loop.size());
  for(unsigned int i=0; i<n; i++) {
    bool keepthis = leftside(loop[i], line);
    if(keepthis) {
      if(!keepprev) {
	// We're keeping this point, but not the previous one, so add
	// the point where the previous segment intersects the
	// clipping line.
	newloop.add(intersection(loop[iprev], loop[i],
				  line.first, line.second));
      }
      newloop.add(loop[i]);	// keep this point
    }
    else {			// !keepthis
      if(keepprev) {
	// We kept the previous point but we're not keeping this one,
	// so add the point where the previous segment intersects the
	// clipping line.
	newloop.add(intersection(loop[iprev], loop[i],
				  line.first, line.second));
      }
    }
    keepprev = keepthis;
    iprev = i;
  } // end loop over points i

  return newloop;
}

template <class CTYPE, class RTYPE>
std::ostream &operator<<(std::ostream &os,
			 const PxlBdyLoopBase<CTYPE, RTYPE> &pbl)
{
  os << pbl.data;
  return os;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void PixelBdyLoop::add_point(const ICoord &pbs) {
  loop.push_back(pbs);
}

// Clean up the loop in-place, by extending segments for which the
// adjacent segment is just a continuation of the current segment.
void PixelBdyLoop::clean(const CMicrostructure *ms) {
  std::vector<ICoord>::iterator segend = loop.begin();	 // end of current seg
  ++segend;
  ICoord segdir = *segend - loop.front(); // direction of current seg
  ICRectangle bbox(*loop.begin(), *segend);
  std::vector<ICoord>::iterator next = segend; // next point to examine
  ++next;
  while(next != loop.end()) {
    // segend points to the end point of the current segment.  If the
    // next point extends the segment, just update *segend to be the
    // next point.  If the next point is in a different direction, the
    // old segend is the beginning of a new segment, and segend is
    // incremented to point to the new end point.
    ICoord nextdir = *next - *segend;
    if(nextdir != segdir) {	// Heading off in a new direction
      bbox.swallow(*next);
      ++segend;
      segdir = nextdir;
    }
    *segend = *next;
    ++next;
  }
  // The last retained entry in loop might be redundant if the
  // starting point is in line with it.  If it is redundant, delete it
  // and everything after it.  If it's not redundant, just delete
  // everything after it.
  if(*segend + segdir != loop.front())
    ++segend;
  loop.erase(segend, loop.end());
  
  bounds = new ICRectangle(bbox.lowerleft(), bbox.upperright());
}

bool PixelBdyLoop::closed() const {
  // This is used to check consistency *before* clean() is called.  It
  // won't work afterwards.
  ICoord diff = loop.front() - loop.back();
  return (diff == iUp || diff == iDown || diff == iLeft || diff == iRight);
}

std::ostream &operator<<(std::ostream &os, const PixelBdyLoop &pbl) {
  return os << "PixelBdyLoop(" << pbl.loop << ")";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ClippedPixelBdyLoop::ClippedPixelBdyLoop()
  : PxlBdyLoopBase<Coord, CRectangle>()
{}

ClippedPixelBdyLoop::ClippedPixelBdyLoop(
			 const PxlBdyLoopBase<Coord, CRectangle> *otherloop)
  : PxlBdyLoopBase<Coord, CRectangle>(otherloop->getLoop(), otherloop->bbox())
{
}

ClippedPixelBdyLoop::ClippedPixelBdyLoop(
			 const PxlBdyLoopBase<ICoord, ICRectangle> *otherloop) {
  loop.reserve(otherloop->size());
  for(const ICoord ipt : otherloop->getLoop()) {
    add(ipt);			// converts from ICoord to Coord
  }
}

ClippedPixelBdyLoop::ClippedPixelBdyLoop(const ClippedPixelBdyLoop &other)
  : PxlBdyLoopBase<Coord, CRectangle>(other)
{
}

ClippedPixelBdyLoop::ClippedPixelBdyLoop(ClippedPixelBdyLoop &&other)
  : PxlBdyLoopBase<Coord, CRectangle>(std::move(other))
{}

ClippedPixelBdyLoop &ClippedPixelBdyLoop::operator=(
					    const ClippedPixelBdyLoop &other)
{
  this->PxlBdyLoopBase::operator=(other);
  return *this;
}

void ClippedPixelBdyLoop::clear() {
  delete bounds;
  bounds = nullptr;
  loop.clear();
}

void ClippedPixelBdyLoop::add(const Coord &pt) {
  if(!bounds)
    bounds = new CRectangle(pt, pt);
  else
    bounds->swallow(pt);
  loop.push_back(pt);
}

void ClippedPixelBdyLoop::add(const ICoord &pt) {
  add(Coord(pt(0), pt(1)));
}

std::ostream &operator<<(std::ostream &os, const ClippedPixelBdyLoop &pbl) {
  return os << "ClippedPixelBdyLoop(" << pbl.loop << ")";
}
