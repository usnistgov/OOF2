// -*- C++ -*-
// $RCSfile: pixelsetboundary.C,v $
// $Revision: 1.39 $
// $Author: langer $
// $Date: 2014/12/31 01:32:23 $


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


// Not as stupid as it looks -- this routine helps resolve the "zero
// or two intersections" case by giving a definitive yes-or-no to the
// question of whether or not there are zero intersections between
// this pixel boundary segment and the element defined by the
// passed-in point list (pts).  The strategy is: if both endpoints of
// this pixel boundary segment are exterior to the same element
// segment, then no intersection is possible (because the element is
// known to be convex); failing that, the endpoints of the pixel
// boundary segment must terminate in different sectors, so if all of
// the element-corner coordinates are on the same side of the pixel
// boundary segment, then an intersection is impossible; failing
// *that*, an intersection (actually, two) is required.  The caller
// promises that both end-points of the pixel boundary segment are
// exterior to the passed-in element (using an interiority test which
// takes the same cross-products as this routine), and we assume
// convexity of the element.

// pts is passed as an array and a size, instead of a std::vector, for
// efficiency.  (TODO: Does that really make a difference?)

bool PixelBdyLoop::find_no_intersection(unsigned int seg,
					const Coord* const pts, int npts,
					const Coord &perturb)
  const
{
  const Coord start = coord(seg);
  const Coord end = next_coord(seg);
    
  // loop over sides of the element 
  for(int i1=0; i1<npts; ++i1) {
    int i2 = (i1+1)%npts;
    // This is the same arithmetic as the CSkeletonElement::interior
    // function -- this is important for avoiding roundoff-related
    // screwups.
    const Coord eside = pts[i2] - pts[i1];
    double start_cross = eside % (start - pts[i1]);
    double end_cross = eside % (end - pts[i1]);

    // Easy case -- if they're both negative for this segment, then
    // there are no intersections, we're done.
    if ( (start_cross < 0) && (end_cross < 0) ) 
      return true;

    // In the boundary case, check against perturbations.
    double delta = perturb % eside;
    bool start_ok = (start_cross < 0) || ( (start_cross==0) && (delta < 0) );
    bool end_ok = (end_cross < 0) || ( (end_cross==0) && (delta < 0) );
    if (start_ok && end_ok)
      return true;
  } // end loop over sides of the element

  // If we made it this far, then the endpoints must be exterior in
  // different "sectors".  In this case, we can still rule out
  // intersections if all of the element nodes are on the same side of
  // the pixel boundary segment.  Find out which side the first one is
  // on.  If any of the others are on a different side, return false,
  // indicating that intersections are required.

  double initial_res = (pts[0] - start) % (end - start);
  double delta = perturb % (end - start);
  if (initial_res == 0)
    initial_res = delta;

  for(int i1=1; i1<npts; ++i1) {
    double new_res = (pts[i1] - start) % (end - start);
    if ( initial_res*new_res < 0)
      return false; // Intersection required.
    if ( (new_res==0) && (initial_res*delta < 0) )
      return false;
  }
  // If we didn't succeed in the first block, or fail in the second
  // block, then there are no intersections.

  return true;
}
				      




// Quick intersection-finding routine, used when you have topological
// information about what's going on.  Specifically, you know that
// it's geometrically required that the pixel boundary segment must
// intersect the passed-in set of coordinates exactly once, you know
// whether it enters or exits, and the only real question is where
// this occurs.  The return value is an integer indicating on which
// element segment the intersection occurred.

int PixelBdyLoop::find_one_intersection(
	    unsigned int seg, // index of the starting point of the bdy segment
	    const Coord * const pts, // coords of the polygon corners
	    int npts,		     // number of polygon corners
	    bool entry,		     // is the segment entering the polygon?
	    PixelBdyIntersection &pbi // result
				    )
  const
{
  // Alpha is the fractional distance along an element segment, and
  // beta is the fractional distance along the boundary segment.
  // Round-off error can make it seem as if the intersection is just
  // past the endpoint of one of the segments.  Unless we've found an
  // intersection that clearly is in bounds, we use the one that's
  // least out of bounds.
  int segment = -1;	    // segment number of the best intersection
  double t_pos = 0.0;	    // best position found so far
  double error = std::numeric_limits<double>::max();

  // std::cerr << "find_one_intersection: looking for "
  // 	    << (entry ? "entry" : "exit") << std::endl;

  const Coord segstart = coord(seg);
  const Coord segend = next_coord(seg);
  // std::cerr << "find_one_intersection: seg=" << seg
  // 	    << " segstart=" << segstart
  // 	    << " segend=" << segend << std::endl;
  bool decrseg = decreasing(seg);
  // std::cerr << "find_one_intersection: decreasing=" << decrseg
  // 	    << " horizontal=" << horizontal(seg) << std::endl;
  
  // Transfer the passed-in classification info.
  pbi.entry = entry;

  if (horizontal(seg)) {
    double fp_level = segstart.y;
    for(int i1=0; i1<npts; ++i1) { // loop over polygon edges
      int i2 = (i1 + 1)%npts;

      // Ignore the parallel case.
      if (pts[i1].y == pts[i2].y)
	continue;

      // Also skip segments which are oriented incorrectly for the
      // type of intersection we want.  A horizontal category edge is
      // entering the polygon if the category edge is L->R (!decrseg)
      // and the polygon edge is is going down (!goingup), or if the
      // category edge is R->L (decrseg) and the polygon edge is going
      // up.
      bool goingup = pts[i2].y > pts[i1].y; // polygon edge is going up
      bool seg_entry = (goingup == decrseg);
      if (seg_entry != entry)
	continue;
      
      double alpha = (fp_level - pts[i1].y) / (pts[i2].y - pts[i1].y);
      double x = (1 - alpha)*pts[i1].x + alpha*pts[i2].x;
      double beta = (x - segstart.x)/(segend.x - segstart.x);
      // beta = ((fp_first - pts[i1].x) - (pts[i2].x-pts[i1].x)*alpha)/
      // 	(fp_first-fp_last);
      // If the trial alpha/beta is in-bounds, we're done.
      // TODO: Should these checks use <= and >= ?
      if ((alpha > 0) && (alpha < 1) && (beta > 0) && (beta < 1)) {
	pbi.location = Coord(x, fp_level);
	return i1;
      }
      // Compute how far out of bounds we ended up.
      double new_error = 0.0;
      if (alpha > 1)
	new_error = (alpha-1.0)*(alpha-1.0);
      else if
	(alpha < 0) new_error = alpha*alpha;
      if (beta > 1)
	new_error += (beta-1.0)*(beta-1.0);
      else if (beta < 0)
	new_error += beta*beta;
      
      // If this is the first iteration, or if the new error is
      // smaller than the already-stored error, save the results.
      if (new_error < error) {
	segment = i1;
	t_pos = x;
	error = new_error;
      }
    } // end loop over polygon edges
    
    // If we made it out of the loop, that means none of the element
    // segments were in-bounds.  But the caller insists there must be
    // an intersection, so we'll return our best guess.
    pbi.location = Coord(t_pos, fp_level);
    assert(segment != -1);
    return segment;
  } // end if horizontal
  
  else {
    // Pixel boundary segment is vertical
    double fp_level = segstart.x;
    for(int i1=0; i1 <npts; ++i1) { // loop over polygon edges
      int i2 = (i1 + 1)%npts;
      // Again, ignore the parallel case.
      if (pts[i1].x == pts[i2].x)
	continue;
      // And again, ignore wrongly oriented segments.
      bool goingright = pts[i2].x > pts[i1].x; // polygon edge is going right
      bool seg_entry = (goingright != decrseg);
      if (seg_entry != entry)
	continue;

      double alpha = (fp_level - pts[i1].x)/(pts[i2].x - pts[i1].x);
      double y = (1 - alpha)*pts[i1].y + alpha*pts[i2].y;
      double beta = (y - segstart.y)/(segend.y - segstart.y);
      
      // If we're in-bounds, we're done.
      if ((alpha > 0) && (alpha < 1) && (beta > 0) && (beta < 1)) {
	pbi.location = Coord(fp_level, y);
	return i1;
      }
      double new_error=0.0;
      if (alpha > 1)
	new_error = (alpha-1.0)*(alpha-1.0);
      if (alpha < 0)
	new_error = alpha*alpha;
      if (beta > 1)
	new_error += (beta-1.0)*(beta-1.0);
      if (beta < 0)
	new_error += beta*beta;
      
      if (new_error < error) {
	segment = i1;
	t_pos = y;
	error = new_error;
      }
    }
    // If we made it this far, we were never in-bounds.  Return best-guess.
    pbi.location = Coord(fp_level, t_pos);
    assert(segment != -1);
    return segment;
  } // end if !horizontal
} // end PixelBdyLoop::find_one_intersection
    

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


PixelSetBoundary::PixelSetBoundary(const CMicrostructure* ms)
  : microstructure(ms)
{}

PixelSetBoundary::~PixelSetBoundary() {
  for(std::vector<PixelBdyLoop*>::iterator i=loopset.begin(); i<loopset.end();
      ++i)
    delete *i;
}

// Add the boundary segments for this pixel to the map of all pixel
// segments.
void PixelSetBoundary::add_pixel(const ICoord &px) {
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

// find_boundary is called by CMicrostructure::categorize() after it
// has called add_pixel for each pixel in the microstructure.

void PixelSetBoundary::find_boundary() {
  CoordMap cm;
  // The remaining segments are all boundary segments.  Put them in a
  // more convenient map for making connections.  The map key is the
  // starting point of the segment, and the stored value is a pair
  // (DirectedSeg) containing the segment's direction and the pointer
  // to the segment itself.
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

PixelBdyLoop *PixelSetBoundary::find_loop(CoordMap &cm) {
  PixelBdyLoop *loop = new PixelBdyLoop(this);
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

//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//

PixelBdyLoop::~PixelBdyLoop() {
  delete bounds; 
}

void PixelBdyLoop::add_point(const ICoord &pbs) {
  loop.push_back(pbs);
}

ICoord PixelBdyLoop::icoord(unsigned  int k) const {
  assert(k >= 0 && k < loop.size());
  return loop[k];
}

ICoord PixelBdyLoop::next_icoord(unsigned int k) const {
  int kk = k + 1;
  if(kk == loop.size())
    return loop[0];
  return loop[kk];
}

Coord PixelBdyLoop::coord(unsigned int k) const {
  // If this is slow, PixelBdyLoop can cache the CMicrostructure*, or
  // can even precompute a std::vector<Coord> of physical positions.
  return pixelSetBdy->microstructure->pixel2Physical(icoord(k));
};

Coord PixelBdyLoop::next_coord(unsigned int k) const {
  return pixelSetBdy->microstructure->pixel2Physical(next_icoord(k));
}

bool PixelBdyLoop::horizontal(unsigned int k) const {
  return icoord(k)(1) == next_icoord(k)(1);
}

bool PixelBdyLoop::decreasing(unsigned int k) const {
  // A decreasing segment is a horizontal segment that goes right to
  // left or a vertical segment that goes top to bottom.
  ICoord here(icoord(k));
  ICoord next(next_icoord(k));
  return (here(0) == next(0) && here(1) > next(1)) || (here(0) > next(0));
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
  
  bounds = new CRectangle(ms->pixel2Physical(bbox.lowerleft()),
			  ms->pixel2Physical(bbox.upperright()));
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

std::ostream &operator<<(std::ostream &os, const PixelBdyIntersection &pbi) {
  int prec = os.precision();
  os << std::setprecision(20);
  os << "PixelBdyIntersection(" << pbi.location << ", fraction="
     << pbi.get_element_fraction() << ", "
     << (pbi.entry? "entry" : "exit") << ")";
  os << std::setprecision(prec);
  return os;
}

