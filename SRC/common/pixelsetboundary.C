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

// Some geometric utilities

// Is the point, pt, to the left of the line, Line?
template <class COORD>
bool leftside(const COORD &pt, const Line &line) {
  return cross(line.second - line.first, pt - line.first) > 0.0;
}

// Return the intersection point of the segment (a0, a1) and the line
// through (b0, b1).  The intersection is known to exist -- a0 and a1
// are on different sides of the line.

Coord intersection(const Coord &a0, const Coord &a1,
		   const Coord &b0, const Coord &b1)
{
  double denom = cross(a1-a0, b1-b0);
#ifdef DEBUG
  if(denom == 0) {
    std::cerr << "intersection: denom==0! a0=" << a0 << " a1=" << a1
	      << " b0=" << b0 << " b1=" << b1
	      << std::endl;
  }
#endif // DEBUG
  assert(denom != 0); 		// because they're known to intersect
  double alpha = cross(b0-a0, b1-b0)/denom;
  if(alpha < 0.0)
    return a0;
  if(alpha > 1.0)
    return a1;
  return a0 + alpha*(a1-a0);
}

Coord intersection(const ICoord &a0, const ICoord &a1,
		   const Coord &b0, const Coord &b1)
{
  double denom = cross(a1-a0, b1-b0);
  assert(denom != 0); 		// because they're known to intersect
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
  int ix = (px(0)/mssize(0))*nbinsx;
  if(ix >= nbinsx) ix = nbinsx-1;
  int iy = (px(1)/mssize(1))*nbinsy;
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

double PixelSetBoundary::clippedArea(const LineList &lines) const {
#ifdef DEBUG
  for(const Line &line : lines)
    assert(line.first != line.second);
#endif // DEBUG
// #ifdef DEBUG
//   std::cerr << "PixelSetBoundary::clippedArea: lines=";
//   for(const Line &line : lines)
//     std::cerr << " (" << line.first << "," << line.second << ")";
//   std::cerr << std::endl;
// #endif // DEBUG
  
  double area = 0.0;
  for(const PixelSetSubBoundary &subbdy : subBdys) {
    area += subbdy.clippedArea(lines);
  }
  // Convert back to physical units
  Coord pxlsize = microstructure->sizeOfPixels();
  return area * pxlsize.x * pxlsize.y;
}

// ------------

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

double PixelSetSubBoundary::clippedArea(const LineList &lines) const {
  double area = 0.0;
  // std::cerr << "PixelSetSubBoundary::clippedArea: nloops=" << loopset.size()
  // 	    << std::endl;
  for(PixelBdyLoop *loop : loopset) {
    // std::cerr << "PixelSetSubBoundary::clippedArea: loop=" << loop;
    // std::cerr << " " << *loop << std::endl;
    area += loop->clippedArea(lines.begin(), lines.end());
    // std::cerr << "PixelSetSubBoundary::clippedArea: area=" << area << std::endl;
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
double PxlBdyLoopBase<CTYPE, RTYPE>::clippedArea(
				  LineList::const_iterator startlines,
				  LineList::const_iterator endlines)
  const
{
  // If there are no clipping lines, return the area of the loop.  If
  // there are lines, clip with the first one, creating new loops, and
  // call clippedArea() on those loops with the remaining lines.
  // std::cerr << "PxlBdyLoopBase::clippedArea:" << std::endl;
  if(startlines == endlines) {
    // std::cerr << "PxlBdyLoopBase::clippedArea: no lines!" << std::endl;
    return areaInPixelUnits();
  }
  std::vector<ClippedPixelBdyLoop*> newloops = clip(*startlines);
// #ifdef DEBUG
//   std::cerr << "PxlBdyLoopBase::clippedArea: line=(" << startlines->first
// 	    << "," << startlines->second << ")"
// 	    << ": " << newloops.size() << " new loops=" << std::endl;
//   for(const ClippedPixelBdyLoop *loop : newloops)
//     std::cerr << "  new loop " << *loop << std::endl;
// #endif // DEBUG
  double area = 0.0;
  for(ClippedPixelBdyLoop *newloop : newloops) {
    area += newloop->clippedArea(startlines+1, endlines);
    delete newloop;
  }
  // std::cerr << "PxlBdyLoopBase::clippedArea: returning area=" << area
  // 	    << std::endl;
  return area;
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
// #ifdef DEBUG
//   std::cerr << "PxlBdyLoopBase::areaInPixelUnits: loop=";
//   for(const CTYPE &pt : loop) std::cerr << " " << pt;
//   std::cerr << " area=" << 0.5*sum << std::endl;  
// #endif // DEBUG
  return 0.5*sum;
}

template <class CTYPE, class RTYPE>
std::vector<ClippedPixelBdyLoop*> PxlBdyLoopBase<CTYPE, RTYPE>::clip(
						     const Line &line)
  const
{
  assert(line.first != line.second);
  // std::cerr << "PxlBdyLoopBase::clip: line=(" << line.first << ", "
  // 	    << line.second << ")" << std::endl;
  // std::cerr << "PxlBdyLoopBase::clip: bbox=" << *bounds << std::endl;
  // Return the loops formed by clipping by the given line.
  std::vector<ClippedPixelBdyLoop*> newloops;
  // Is the loop's bounding box entirely on one side of the line?
  unsigned int nbbleft = 0;
  for(unsigned int i=0; i<4; i++) {
    if(leftside((*bounds)[i], line))
      nbbleft++;
  }
  // std::cerr << "PxlBdyLoopBase::clip: nbbleft=" << nbbleft << std::endl;
  // If nleft==0, all of the pixels are to the right of the line (or
  // on it), and there's nothing to do.  Return an empty vector of
  // loops.
  if(nbbleft == 4) {
    // All of the pixels are to the left of the line, so they're all
    // retained. Don't do anything other than to convert the
    // PixelBdyLoop to a ClippedPixelBdyLoop.
    // TODO: Figure out a way to avoid copying here.
    newloops.push_back(clone());
  }
  else if(nbbleft != 0) {
    // Actually clip.
    unsigned int n = size();
    std::vector<bool> keep(n, false);
    for(unsigned int i=0; i<n; i++) {
      keep[i] = leftside(loop[i], line);
      // std::cerr << "PxlBdyLoopBase::clip:    " << loop[i]
      // 		<< " keep=" << keep[i] << std::endl;
    }

    unsigned int curpt = 0;
    unsigned int prevpt = n-1;
    ClippedPixelBdyLoop *curloop = nullptr;
    while(curpt < n) {
      // std::cerr << " PxlBdyLoopBase::clip: top of loop, curpt=" << curpt
      // 		<< std::endl;
      if(curloop==nullptr) {
	if(keep[curpt]) {
	  // Start a new loop
	  // std::cerr << "PxlBdyLoopBase::clip: new pixel loop!" << std::endl;
	  curloop = new ClippedPixelBdyLoop();
	  newloops.push_back(curloop);
	  if(!keep[prevpt]) {
	    curloop->add(intersection(loop[prevpt], loop[curpt],
				      line.first, line.second));
	  }
	  curloop->add(loop[curpt]);
	}
      }
      else if(keep[prevpt] && !keep[curpt]) {
	// End the current loop
	// std::cerr << "PxlBdyLoopBase::clip: ending pixel loop" << std::endl;
	curloop->add(intersection(loop[prevpt], loop[curpt],
				  line.first, line.second));
	curloop = nullptr;
      }
      else if(keep[curpt]) {
	// std::cerr << "PxlBdyLoopBase::clip: continuing pixel loop="<< std::endl;
	assert(curloop != nullptr);
	curloop->add(loop[curpt]);
      }
      ++curpt;
      prevpt = curpt-1;
    } // end loop over points in the old loop
    
    // If we get to the end of the list of points in the old loop but
    // haven't ended the current new loop, either the current new loop
    // is part of the first new loop, or the current loop ends on a
    // point between the last and first points on the old loop.
    if(curloop) {
      if(keep[0]) {
	// std::cerr << "PxlBdyLoopBase::clip: closing loop" << std::endl;
	if(newloops[0] != curloop) {
	  newloops[0]->prepend(curloop);
	  delete curloop;
	  curloop = nullptr;
	  newloops.pop_back();
	}
      }
      else {	       // not keeping the first point in the old loop.
	// std::cerr << "PxlBdyLoopBase:: ending last loop" << std::endl;
	curloop->add(intersection(loop.back(), loop.front(),
				  line.first, line.second));
      }
    }
  }
  
  return newloops;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ClippedPixelBdyLoop *PixelBdyLoop::clone() const {
  ClippedPixelBdyLoop *newloop = new ClippedPixelBdyLoop();
  for(const ICoord ipt : loop)
    newloop->add(ipt);
  return newloop;
}

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

ClippedPixelBdyLoop::ClippedPixelBdyLoop(const ClippedPixelBdyLoop *otherloop)
  : PxlBdyLoopBase<Coord, CRectangle>(otherloop->getLoop(), otherloop->bbox())
{
}

ClippedPixelBdyLoop *ClippedPixelBdyLoop::clone() const {
  return new ClippedPixelBdyLoop(this);
}

// ClippedPixelBdyLoop::ClippedPixelBdyLoop(ClippedPixelBdyLoop &&other)
//   : loop(std::move(other.loop))
// {
//   CRectangle *temp = other.bounds;
//   other.bounds = bounds;
//   bounds = temp;
// }

void ClippedPixelBdyLoop::clear() {
  delete bounds;
  bounds = nullptr;
  loop.clear();
}

void ClippedPixelBdyLoop::add(const Coord &pt) {
  // std::cerr << "ClippedPixelBdyLoop::add: pt=" << pt << std::endl;
  if(!bounds)
    bounds = new CRectangle(pt, pt);
  else
    bounds->swallow(pt);
  loop.push_back(pt);
}

void ClippedPixelBdyLoop::add(const ICoord &pt) {
  add(Coord(pt(0), pt(1)));
}

void ClippedPixelBdyLoop::prepend(const ClippedPixelBdyLoop *other) {
  // std::cerr << "ClippedPixelBdyLoop::prepend:  this=" << *this << std::endl;
  // std::cerr << "ClippedPixelBdyLoop::prepend: other=" << *other << std::endl;
  loop.insert(loop.begin(), other->loop.begin(), other->loop.end());
  for(const Coord &pt : other->getLoop())
    bounds->swallow(pt);
  // std::cerr << "ClippedPixelBdyLoop::prepend: after=" << *this << std::endl;
}


std::ostream &operator<<(std::ostream &os, const ClippedPixelBdyLoop &pbl) {
  return os << "ClippedPixelBdyLoop(" << pbl.loop << ")";
}
