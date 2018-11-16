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

// Tilings are created at scales that are factors of TILINGFACTOR.
// TILINGFACTOR must be strictly between 0 and 1.
double tilingfactor = 0.5;

// MINTILESCALE is the minumum allowed tile size, in pixel units
int mintilescale = 10;

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

// Utility function used by PSBTiling constructor

static void getTileIndices(int mssize, int ntiles,
			   TileNumbers &tileNumbers,
			   std::vector<unsigned int> &maxes)
{
  // Get the tile number for each pixel, and the max pixel index for
  // each tile.  The x and y directions are done separately.  This
  // routine does one direction at a time.

  // TODO: Cache results.  PSBTiles don't need their own copies of the
  // results, and this routine will be called multiple times with the
  // same mssize and ntiles args.
  unsigned int lasttile = 0;
  double factor = ntiles/(float) mssize;
  // Do this the dumb way by looping over integer pixel coordinates so
  // we don't have to think about what happens if the Microstructure
  // size isn't an integer multiple of the number of tiles.
  for(unsigned int pxl=0; pxl<mssize; pxl++) {
    unsigned int tile = pxl*factor;
    if(tile == ntiles) --tile;
    if(tile > 0 && tile != lasttile) {
      maxes[tile-1] = pxl-1;
    }
    tileNumbers[pxl] = tile;
    lasttile = tile;
  }
  maxes[ntiles-1] = mssize - 1;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

PSBTiling::PSBTiling(const CMicrostructure* ms,
		     unsigned int nx, unsigned int ny)
  : tiles(nx*ny, nullptr),
    microstructure(ms),
    nxtiles(nx), nytiles(ny)
{
  // std::cerr << "PSBTiling::ctor: nx=" << nx << " ny=" << ny << std::endl;
  // A PSBTiling is divided into PSBTiles, which together cover
  // the whole Microstructure.
  ICoord mssize = microstructure->sizeInPixels();
  tiles.reserve(nx*ny);

  // Construct lookup tables that quickly convert pixel coordinates to
  // tile numbers.  At the same time, find the bounding box for each
  // bin. 
  std::vector<unsigned int> maxx(nxtiles, 0);
  std::vector<unsigned int> maxy(nytiles, 0);
  xTileNumbers.resize(mssize[0], 0);
  yTileNumbers.resize(mssize[1], 0);
  getTileIndices(mssize[0], nx, xTileNumbers, maxx);
  getTileIndices(mssize[1], ny, yTileNumbers, maxy);
  
  // Create the tiles. 
  for(unsigned int iy=0; iy<nytiles; iy++) {
    const int ymin = iy == 0 ? 0 : (maxy[iy-1] + 1);
    const int ymax = maxy[iy];
    for(unsigned int ix=0; ix<nxtiles; ix++) {
      const int xmin = ix == 0 ? 0 : (maxx[ix-1] + 1);
      const int xmax = maxx[ix];
      // The argument to the PSBTile constructor is the bounding box
      // of the tile.  A pixel is in the tile if its lower left corner
      // is in the bounding box.
      tiles[tileIndex(ix, iy)] = new PSBTile(ICRectangle(ICoord(xmin, ymin),
							 ICoord(xmax, ymax)));
      // std::cerr << "PSBTiling::ctor:  tile #" << tileIndex(ix, iy)
      // 		<< " " << ix << " " << iy << " " << *tiles[tileIndex(ix, iy)]
      // 		<< std::endl;
    }
  }
}

PSBTiling::~PSBTiling() {
  for(PSBTile *tile : tiles)
    delete tile;
}

unsigned int PSBTiling::tileIndex(unsigned int ix, unsigned int iy) const {
  // When trying to compute the homogeneity of an element that has one
  // or more nodes outside the microstructure, ix or iy can be larger
  // than nxtiles or nytiles.  In that case, the correct thing to do
  // is to truncate them, so that only the part of the element inside
  // the microstructure is used.  Illegal elements with inverted
  // geometries don't make it to this point because
  // CSkeletonElement::c_homogeneity checks for that case.
  if(ix >= nxtiles)
    ix = nxtiles-1;
  if(iy >= nytiles)
    iy = nytiles-1;
  return iy*nxtiles + ix;
}

void PSBTiling::add_pixel(const ICoord &px) {
  // Find which bin the pixel contributes to.
  unsigned int ix = xTileNumbers[px[0]];
  unsigned int iy = yTileNumbers[px[1]];
  // Add to the bin.
  tiles[tileIndex(ix, iy)]->add_pixel(px);
}

void PSBTiling::add_segments(const std::vector<ICoord> &loop) {
  assert(loop.size() >= 4);	// must be a real loop
  unsigned int iprev = loop.size() - 1;
  for(unsigned int i=0; i<loop.size(); i++) {
    // End points of this segment
    ICoord p0 = loop[iprev];
    ICoord p1 = loop[i];
    // Find which direction the segment goes.
    if(p0[0] > p1[0]) {		// segment goes from right to left
      // Add each unit leg of each segment separately.  TODO: Find
      // where segments cross from one tile to another and add longer
      // segments.
      for(unsigned int x=p0[0]; x>p1[0]; x--) {
	// Which tile the segment belongs in is determined by which
	// pixel is responsible for the segment.  This segment goes to
	// the left, so the pixel is below and to the left of the
	// starting point of the segment.
	unsigned int ix = xTileNumbers[x-1];
	unsigned int iy = yTileNumbers[p0[1]-1];
	tiles[tileIndex(ix, iy)]->add_segmentL(ICoord(x, p0[1]));
      }
    }
    else if(p0[0] < p1[0]) {	// left to right
      for(unsigned int x=p0[0]; x<p1[0]; x++) {
	// The pixel is above and to the right of the segment's start.
	unsigned int ix = xTileNumbers[x];
	unsigned int iy = yTileNumbers[p0[1]];
	tiles[tileIndex(ix, iy)]->add_segmentR(ICoord(x, p0[1]));
      }
    }
    else if(p0[1] > p1[1]) {	// up to down
      for(unsigned int y=p0[1]; y>p1[1]; y--) {
	// The pixel is to the right and below the segment's start.
	unsigned int ix = xTileNumbers[p0[0]];
	unsigned int iy = yTileNumbers[y-1];
	tiles[tileIndex(ix, iy)]->add_segmentD(ICoord(p0[0], y));
      }
    }
    else {			// down to up
      assert(p0[1] < p1[1]);
      for(unsigned int y=p0[1]; y<p1[1]; y++) {
	// The pixel is to the left and above the segment's start.
	unsigned int ix = xTileNumbers[p0[0]-1];
	unsigned int iy = yTileNumbers[y];
	tiles[tileIndex(ix, iy)]->add_segmentU(ICoord(p0[0], y));
      }
    }

    iprev = i;
  } // end loop over points i
}

void PSBTiling::add_tile_perimeters(int cat) {
  for(PSBTile *tile : tiles)
    tile->add_perimeter(microstructure, cat);
}

// find_boundary is called by CMicrostructure::categorize() after it
// has called add_pixel for each pixel in the microstructure.

void PSBTiling::find_boundary() {
  for(PSBTile *tile : tiles) {
    tile->find_boundary(microstructure);
  }
}

double PSBTiling::clippedArea(const LineList &lines, const CRectangle &bbox,
			      bool verbose)
  const
{
#ifdef DEBUG
  for(const Line &line : lines)
    assert(line.first != line.second);
#endif // DEBUG
  // Find which PSBTiles to use.
  // Convert element bbox (already in pixel coords) to integers
  unsigned int xmin = int(floor(bbox.lowerleft()[0]));
  unsigned int xmax = int(floor(bbox.upperright()[0]));
  if(xmax >= microstructure->sizeInPixels()[0]) --xmax;
  unsigned int ymin = int(floor(bbox.lowerleft()[1]));
  unsigned int ymax = int(floor(bbox.upperright()[1]));
  if(ymax >= microstructure->sizeInPixels()[1]) --ymax;

#ifdef DEBUG
  if(verbose) {
    std::cerr << "PSBTiling::clippedArea: bbox=" << bbox << std::endl;
    std::cerr << "PSBTiling::clippedArea: x range " << xmin << " " << xmax
	      << " yrange " << ymin << " " << ymax << std::endl;
  }
#endif // DEBUG
  double area = 0.0;
  for(unsigned int iy=yTileNumbers[ymin]; iy<=yTileNumbers[ymax]; iy++) {
    for(unsigned int ix=xTileNumbers[xmin]; ix<=xTileNumbers[xmax]; ix++) {
#ifdef DEBUG
      if(verbose)
	std::cerr << "PSBTiling::clippedArea: using tile " << ix << " " << iy
		  << " " << *tiles[tileIndex(ix, iy)] << std::endl;
#endif // DEBUG
      area += tiles[tileIndex(ix, iy)]->clippedArea(lines, bbox);
    }
  }
  // Convert back to physical units
  Coord pxlsize = microstructure->sizeOfPixels();
  return area * pxlsize[0] * pxlsize[1];
}

PSBTiling *PSBTiling::subdivide(int cat, unsigned int nx, unsigned int ny)
  const
{
  assert(tiles.size() == 1);
  return tiles[0]->subdivide(microstructure, cat, nx, ny);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


std::ostream &operator<<(std::ostream &os, const CoordMap &cm) {
  os << "{";
  for(auto &i : cm)
    os << i.first << ":" << i.second << ", ";
  os << "}";
  return os;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

PSBTile::PSBTile(ICRectangle &&bbox)
  : bounds(std::move(bbox))
{}


PSBTile::~PSBTile() {
  for(std::vector<PixelBdyLoop*>::iterator i=loopset.begin(); i<loopset.end();
      ++i)
    delete *i;
}

std::ostream &operator<<(std::ostream &os, const PSBTile &tile) {
  os << "PSBTile(" << tile.bounds.lowerleft() << ", "
     << tile.bounds.upperright() << ")";
  return os;
}

// Add the boundary segments for this pixel to the map of all pixel
// segments.
void PSBTile::add_pixel(const ICoord &px) {
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

// The add_segmentX routines are called when this tile is being built
// while subdividing a larger tile. There won't be opposing segments,
// so the segments are added to the SegSets without checking.  The
// segmentsXX arrays store the left or bottom endpoints of the
// segments, but the arguments to the add_segmentX routines are the
// starting points of the segments.

void PSBTile::add_segmentL(const ICoord &px) {
  assert(segmentsRL.count(px+iLeft)==0);
  segmentsRL.insert(px+iLeft);
}

void PSBTile::add_segmentR(const ICoord &px) {
  assert(segmentsLR.count(px) == 0);
  segmentsLR.insert(px);
}

void PSBTile::add_segmentU(const ICoord &px) {
  assert(segmentsDU.count(px) == 0);
  segmentsDU.insert(px);
}

void PSBTile::add_segmentD(const ICoord &px) {
  assert(segmentsUD.count(px+iDown) == 0);
  segmentsUD.insert(px+iDown);
}


typedef std::pair<ICoord, ICoord> DirectedSeg; // start point, direction

void PSBTile::find_boundary(const CMicrostructure *microstructure) {
  if(segmentsLR.empty() && segmentsRL.empty() &&
     segmentsUD.empty() && segmentsDU.empty())
    return;
  CoordMap cm;
  // After all calls to add_pixel(), the remaining segments are all
  // boundary segments.  Put them in a more convenient map for making
  // connections.  The map key is the starting point of the segment,
  // and the stored value is a pair (DirectedSeg) containing the
  // segment's direction and the starting point of the segment.
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

PixelBdyLoop *PSBTile::find_loop(CoordMap &cm) {
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

double PSBTile::clippedArea(const LineList &lines, const CRectangle &bbox)
  const
{
  double area = 0.0;
  for(PixelBdyLoop *loop : loopset) {
    area += loop->clippedArea(lines, bbox);
  }
  return area;
}

PSBTiling *PSBTile::subdivide(const CMicrostructure *ms, int cat,
			      unsigned int nx, unsigned int ny)
  const
{
  // Create a new tiling by subdividing this one.  It's assumed that
  // this tile covers the whole Microstructure.
  PSBTiling *newtiling = new PSBTiling(ms, nx, ny);
  // Loop over loops in this tiling and add their segments to the new
  // tiling.
  for(const PixelBdyLoop *loop: loopset) {
    newtiling->add_segments(loop->getLoop());
  }
  // Each new tile may need to add segments along its boundary.
  newtiling->add_tile_perimeters(cat);
  // Consolidate segments into loops.
  newtiling->find_boundary();
  return newtiling;
}

void PSBTile::add_perimeter(const CMicrostructure *ms, int cat) {
  // When subdividing a tiling, edges of the tile that aren't part of
  // loops in the tiling may form parts of loops in the new tiling.
  // Add a segment along the perimeter if the pixels on both sides of
  // the segment are in the Pixel Boundary Set's category.  If only
  // one pixel is in the category or if the segment is on the edge
  // of the entire Microstructure, the segment will already have been
  // included as part of a loop in the original tiling.
  unsigned int ix=0;
  unsigned int iy=0;
 // Bottom edge of bounding box
  iy = bounds.ymin();
  if(iy > 0) {
    // (ix, iy) is the bottom left corner of the pixel that's in the tile.
    // The pixel inside the tile is (ix, iy).
    // The pixel outside the tile is (ix, iy-1).
    for(unsigned int ix=bounds.xmin(); ix<=bounds.xmax(); ix++) {
      if(ms->category(ix, iy-1) == cat && ms->category(ix, iy) == cat)
	add_segmentR(ICoord(ix, iy));
    }
  }
  // Right edge of bounding box
  ix = bounds.xmax() + 1;
  if(ix < ms->sizeInPixels()[0]) {
    // (ix, iy) is the bottom *right* corner of the pixel that's in
    // the tile.
    // The pixel inside the tile is (ix-1, iy).
    // The pixel outside the tile is (ix, iy).
    for(unsigned int iy=bounds.ymin(); iy<=bounds.ymax(); iy++) {
      if(ms->category(ix, iy) == cat && ms->category(ix-1, iy) == cat) {
	add_segmentU(ICoord(ix, iy));
      }
    }
  }
  // Top edge of bounding box
  iy = bounds.ymax() + 1;
  if(iy < ms->sizeInPixels()[1]) {
    // (ix, iy) is the top right corner of the pixel that's in the tile.
    // The pixel inside the tile is (ix-1, iy-1).
    // The pixel outside the tile is (ix-1, iy).
    for(unsigned int ix=bounds.xmax()+1; ix>bounds.xmin(); ix--) {
      if(ms->category(ix-1, iy) == cat && ms->category(ix-1, iy-1) == cat)
	add_segmentL(ICoord(ix, iy));
    }
  }
  // Left edge of bounding box
  ix = bounds.xmin();
  if(ix > 0) {
    // (ix, iy) is the top left corner of the pixel that's in the tile.
    // The pixel outside the tile is (ix-1, iy-1).
    for(unsigned int iy=bounds.ymax()+1; iy>bounds.ymin(); iy--) {
      if(ms->category(ix-1, iy-1) == cat && ms->category(ix, iy-1) == cat)
	add_segmentD(ICoord(ix, iy));
    }
  }
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
} // end PxlBdyLoopBase<>::clip

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

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Stats retained for debugging and optimization
static int maxSubdivisions = 1;
static std::set<int> subDivisions({1});
static int minScale = std::numeric_limits<int>::max();

PixelSetBoundary::PixelSetBoundary(const CMicrostructure *ms)
  : microstructure(ms),
    mssize(ms->sizeInPixels())
{
  // Create the topmost, trivial 1x1, tiling
  scale0 = 0.5*(mssize[0] + mssize[1]);
  minScale = scale0;
  tilings.push_back(new PSBTiling(microstructure, 1, 1));
}

PixelSetBoundary::~PixelSetBoundary() {
  for(PSBTiling *tiling : tilings)
    delete tiling;
}

void PixelSetBoundary::add_pixel(const ICoord &pxl) {
  // All pixels must be added before calling find_boundary, which must
  // be called before nontrivial tilings are created.
  assert(tilings.size() == 1);
  tilings[0]->add_pixel(pxl);
}

void PixelSetBoundary::find_boundary() {
  // find_boundary assembles the individual segments from the pixel
  // edges into loops.  It should only be called on the topmost level
  // of the tiling hierarchy.  Lower levels derive their loops from
  // the top level loops.
  assert(tilings.size() == 1);
  tilings[0]->find_boundary();
}

// Setting fixed_subdivision to something non-zero fixes the number of
// subdivisions on the x and y axes to that value.
int fixed_subdivision = 0;

double PixelSetBoundary::clippedArea(int cat,
				     const LineList &lines,
				     const CRectangle &bbox,
				     bool verbose)
{
  // PixelSetBoundary::clippedArea() decides which PSBTiling to use,
  // and calls the tiling's clippedArea() method.  It may have to
  // create a new tiling, which is why it's not const.
  PSBTiling *tiling = nullptr;
  // bbox is the bounding box of the element whose homogeneity is
  // being computed.  Look for a tiling on the same scale.
  if(fixed_subdivision == 0) {
    double scale = 0.5*(bbox.height() + bbox.width());
    if(scale < mintilescale)
      scale = mintilescale;
    if(scale > scale0)
      scale = scale0;
    int n = floor(log(scale/scale0)/log(tilingfactor));
    assert(n >= 0);
    if(n >= tilings.size())
      tilings.resize(n+1, nullptr);
#ifdef DEBUG
    if(verbose)
      std::cerr << "PixelSetBoundary::clippedArea: tiling size=" << n
		<< std::endl;
#endif // DEBUG
    if(tilings[n] == nullptr) {
      unsigned int nx = floor(pow(tilingfactor, -n));
      if(nx > maxSubdivisions) maxSubdivisions = nx;
      if(scale < minScale) minScale = scale;
      subDivisions.insert(nx);
      tilings[n] = tilings[0]->subdivide(cat, nx, nx); // TODO: make ny!=nx ?
    }
    tiling = tilings[n];
  }
  else if(fixed_subdivision == 1) {
    // The number of subdivisions is fixed, at the trivial value.  The
    // trivial tiling has already been created.
#ifdef DEBUG
    std::cerr << "PixelSetBoundary::clippedArea: using trivial tiling"
	      << std::endl;
#endif // DEBUG
    tiling = tilings[0];
  }
  else {
    // The subdivisions are fixed, at some value other than 1.  Create
    // the tiling if necessary.
    assert(tilings.size() == 1 || tilings.size() == 2);
    if(tilings.size() == 1) {
      // Need to create the fixed_subdivision tiling
      maxSubdivisions = fixed_subdivision;
      minScale = scale0/fixed_subdivision;
      subDivisions.insert(fixed_subdivision);
      tilings.push_back(tilings[0]->subdivide(cat, fixed_subdivision,
					      fixed_subdivision));
    }
    tiling = tilings[1];
#ifdef DEBUG
    std::cerr << "PixelSetBoundary::clippedArea: using fixed tiling "
	      << fixed_subdivision << std::endl;
#endif // DEBUG
  }
  return tiling->clippedArea(lines, bbox, verbose);
}


void printHomogStats() {
  std::cerr << "printHomogStats: "
	    << " #levels=" << subDivisions.size()
	    << " maxSubdivisions=" << maxSubdivisions
	    << " subDivisions=(" << subDivisions << ")"
	    << " minScale=" << minScale
	    << std::endl;
}
