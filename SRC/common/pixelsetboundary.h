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

#ifndef PIXELSETBOUNDARY_H
#define PIXELSETBOUNDARY_H

class ClippedPixelBdyLoop;
class PixelBdyLoop;
class PixelSetBoundary;
class PSBTile;
class PSBTiling;

#include <map>
#include <set>
#include <vector>

#include "common/coord.h"
#include "common/geometry.h"

class CMicrostructure;

// Classes for keeping track of the boundaries of pixel sets.

typedef std::pair<Coord, Coord> Line;
typedef std::set<ICoord> SegSet;
typedef std::multimap<ICoord, ICoord> CoordMap; // start point, direction
typedef std::vector<Line> LineList;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Base class for pixel boundary loops.

class PBLBase {
public:
  virtual ~PBLBase() {}
  virtual ClippedPixelBdyLoop clip(const Line&) const = 0;
  virtual double areaInPixelUnits() const = 0;
};

template <class CTYPE, class RTYPE>
class PxlBdyLoopBase : public PBLBase {
protected:
  std::vector<CTYPE> loop;
  RTYPE *bounds;
  void pop_back() { loop.pop_back(); }
public:
  PxlBdyLoopBase() : bounds(nullptr) {}
  PxlBdyLoopBase(const std::vector<CTYPE>&, const RTYPE*);
  PxlBdyLoopBase(const PxlBdyLoopBase<CTYPE, RTYPE>&);
  PxlBdyLoopBase(PxlBdyLoopBase<CTYPE, RTYPE>&&);
  PxlBdyLoopBase<CTYPE, RTYPE> &operator=(const PxlBdyLoopBase<CTYPE, RTYPE>&);
  virtual ~PxlBdyLoopBase() { delete bounds; }
  unsigned int size() const { return loop.size(); }
  const RTYPE *bbox() const { return bounds; }
  const std::vector<CTYPE> &getLoop() const { return loop; }
  void reserve(int n) { loop.reserve(n); }
  virtual double areaInPixelUnits() const;
  // clip() returns a new loop that includes the points to the left of
  // the line (not just the segment) going from line.first to
  // line.second, which are Coords.  Usually called by clippedArea().
  // The new loop may contain degenerate or collinear antiparallel
  // segments.
  virtual ClippedPixelBdyLoop clip(const Line&) const;

  friend std::ostream operator<<(std::ostream&,
				 const PxlBdyLoopBase<CTYPE, RTYPE>&);
};

// Pixel Boundary Loops with integer coordinates.

class PixelBdyLoop : public PxlBdyLoopBase<ICoord, ICRectangle> {
public:
  void add_point(const ICoord&);
  void clean(const CMicrostructure*);
  bool closed() const;
  // clippedArea returns the area of the polygon formed by clipping
  // with all of the given lines.  The CRectangle is the polygon's
  // bounding box.
  double clippedArea(const LineList&, const CRectangle&) const;
  friend std::ostream& operator<<(std::ostream&, const PixelBdyLoop&);
  friend class PixelSetBoundary; // for debugging
};

// ClippedPixelBdyLoop is like PixelBdyLoop, except that it uses floating
// point coordinates and is only constructed by clipping a PixelBdyLoop.
class ClippedPixelBdyLoop : public PxlBdyLoopBase<Coord, CRectangle> {
public:
  ClippedPixelBdyLoop();
  ClippedPixelBdyLoop(const PxlBdyLoopBase<ICoord, ICRectangle>*);
  ClippedPixelBdyLoop(const PxlBdyLoopBase<Coord, CRectangle>*);
  ClippedPixelBdyLoop(const ClippedPixelBdyLoop&);
  ClippedPixelBdyLoop(ClippedPixelBdyLoop&&);
  ClippedPixelBdyLoop &operator=(const ClippedPixelBdyLoop&);
  Coord operator[](unsigned int k) const { return loop[k]; }
  void add(const Coord&);
  void add(const ICoord&);
  void clear();
  friend std::ostream& operator<<(std::ostream&, const ClippedPixelBdyLoop&);
};

std::ostream& operator<<(std::ostream&, const PixelBdyLoop&);
std::ostream& operator<<(std::ostream&, const ClippedPixelBdyLoop&);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// A PixelSetBoundary is a collection of PSBTiles, with each tile
// covering a different part of the image.  The idea is that the
// clipping algorithm will only look at tiles that intersect an
// element's bounding box and won't spend time clipping regions that
// are far from the element.

// TileNumbers[x] is the index of the tile containing pixel x.
typedef std::vector<unsigned int> TileNumbers;


class PSBTile {
private:
  SegSet segmentsLR;		// segments going from left to right
  SegSet segmentsRL;		// ... right to left
  SegSet segmentsUD;		// ... up to down
  SegSet segmentsDU;		// ... down to up
  std::vector<PixelBdyLoop*> loopset;
  PixelBdyLoop *find_loop(CoordMap&);
  void find_boundary(const CMicrostructure*);
  double clippedArea(const LineList&, const CRectangle &bbox) const;
  // A pixel is in the tile if its lower left corner is in the
  // bounding box.
  ICRectangle bounds;
public:
  PSBTile(ICRectangle&&);
  ~PSBTile();
  void set_bounds(ICRectangle bbox) { bounds = bbox; }
  void add_pixel(const ICoord&);
  void add_segmentL(const ICoord &pos);
  void add_segmentR(const ICoord &pos);
  void add_segmentD(const ICoord &pos);
  void add_segmentU(const ICoord &pos);
  void add_perimeter(const CMicrostructure*, int);

  PSBTiling *subdivide(const CMicrostructure*, int cat,
		       unsigned int nx, unsigned int ny) const;

  friend std::ostream& operator<<(std::ostream &, const PSBTile&);
  friend class PSBTiling;
};

class PSBTiling {
private:
  std::vector<PSBTile*> tiles;
  const CMicrostructure *microstructure;
  const unsigned int nxtiles, nytiles;
  TileNumbers xTileNumbers;
  TileNumbers yTileNumbers;
  unsigned int tileIndex(unsigned int, unsigned int) const;
public:
  PSBTiling(const CMicrostructure*, unsigned int nx, unsigned int ny);
  ~PSBTiling();
  void add_pixel(const ICoord&);
  void find_boundary();
  double clippedArea(const LineList&, const CRectangle&, bool) const;
  ICoord size() const { return ICoord(nxtiles, nytiles); }
  double area() const;

  // Used when constructing a tiling from the loops in another tiling.
  PSBTiling *subdivide(int, unsigned int, unsigned int) const;
  void add_segments(const std::vector<ICoord>&);
  void add_tile_perimeters(int);
};

// Pixel set boundary knows its microstructure.  The way this works
// is, you create it with a microstructure, then put in all the pixels
// in the pixel set for which you want this to be the boundary, then
// call the "find_boundary" method, which finds all the loops and
// assigns them to the "loopset" member.

class PixelSetBoundary {
private:
  std::vector<PSBTiling*> tilings;
  const CMicrostructure *microstructure;
  double scale0;      // scale of entire microstructure in pixel units
  ICoord mssize;
public:
  PixelSetBoundary(const CMicrostructure *ms);
  ~PixelSetBoundary();
  void add_pixel(const ICoord&);
  void find_boundary();

  double clippedArea(int, const LineList&, const CRectangle&, bool);
  double area() const;
};

// For setting and testing the hierarchical tiling scheme.
void printHomogStats();
extern double tilingfactor;
extern int mintilescale;
extern int fixed_subdivision;


// For debugging....
std::ostream& operator<<(std::ostream &, const PixelSetBoundary &);
extern int countleft;

#endif // PIXELSETBOUNDARY_H
