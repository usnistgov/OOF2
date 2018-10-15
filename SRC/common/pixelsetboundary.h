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
class PixelSetSubBoundary;

#include <map>
#include <set>
#include <vector>

#include "common/coord.h"
#include "common/geometry.h"

class CMicrostructure;

// Special classes for keeping track of the boundaries of pixel sets.

typedef std::pair<Coord, Coord> Line;
typedef std::set<ICoord> SegSet;
typedef std::multimap<ICoord, ICoord> CoordMap; // start point, direction
typedef std::vector<Line> LineList;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

template <class VTYPE, class CTYPE>
class PixelBdyLoop_ {
private:
  std::vector<CTYPE> loop;
  CRectangle_<VTYPE, CTYPE> *bounds;
public:
  PixelBdyLoop_() : bounds(nullptr) {}
  ~PixelBdyLoop_() { delete bounds; }
};

class PixelBdyLoop {
private:
  std::vector<ICoord> loop;
  ICRectangle *bounds;		// computed by clean, in physical coords
public:
  PixelBdyLoop();
  ~PixelBdyLoop();
  void add_point(const ICoord&);
  void clean(const CMicrostructure*);
  bool closed() const;
  const ICRectangle &bbox() const { return *bounds; }
  unsigned int size() const { return loop.size(); }
  // const std::vector<ICoord> &segments() const { return loop; }
  // ICoord operator[](unsigned int k) const { return loop[k]; }

  // clip() returns a set of new loops that include the points to the
  // left of the line (not just the segment) going from line.first to
  // line.second, which are Coords.  Usually called by clippedArea().
  std::vector<ClippedPixelBdyLoop*> clip(const Line&) const;

  // clippedArea returns the area of the polygon formed by clipping
  // with all of the given lines.
  double clippedArea(const LineList&) const;

  double areaInPixelUnits() const;

   friend std::ostream& operator<<(std::ostream&, const PixelBdyLoop&);
  friend class PixelSetBoundary; // for debugging
};

// ClippedPixelBdyLoop is like PixelBdyLoop, except that it uses floating
// point coordinates and is only constructed by clipping a PixelBdyLoop.
class ClippedPixelBdyLoop {
private:
  std::vector<Coord> loop;
  CRectangle *bounds;
public:
  ClippedPixelBdyLoop();
  ClippedPixelBdyLoop(const PixelBdyLoop*);
  ClippedPixelBdyLoop(ClippedPixelBdyLoop&&); // Move constructor
  ~ClippedPixelBdyLoop();
  const CRectangle &bbox() const { return *bounds; }
  Coord operator[](unsigned int k) const { return loop[k]; }
  std::vector<ClippedPixelBdyLoop*> clip(const Line&);
  double areaInPixelUnits() const;
  unsigned int size() const { return loop.size(); }
  void add(const Coord&);
  void add(const ICoord&);
  void clear();
  friend std::ostream& operator<<(std::ostream&, const ClippedPixelBdyLoop&);
};

std::ostream& operator<<(std::ostream&, const PixelBdyLoop&);
std::ostream& operator<<(std::ostream&, const ClippedPixelBdyLoop&);

class PixelSetSubBoundary {
private:
  SegSet segmentsLR;		// segments going from left to right
  SegSet segmentsRL;		// ... right to left
  SegSet segmentsUD;		// ... up to down
  SegSet segmentsDU;		// ... down to up
  std::vector<PixelBdyLoop*> loopset;
  PixelBdyLoop *find_loop(CoordMap&);
  void find_boundary(const CMicrostructure*);
  double clippedArea(const LineList&) const;
public:
  ~PixelSetSubBoundary();
  void add_pixel(const ICoord&);
  // const std::vector<PixelBdyLoop*> &get_loops() const { return loopset; }

  friend std::ostream& operator<<(std::ostream &, const PixelSetBoundary&);
  friend class PixelBdyLoop;
  friend class PixelSetBoundary;
};

// Pixel set boundary knows its microstructure.  The way this works
// is, you create it with a microstructure, then put in all the pixels
// in the pixel set for which you want this to be the boundary, then
// call the "find_boundary" method, which finds all the loops and
// assigns them to the "loopset" member.

class PixelSetBoundary {
private:
  std::vector<PixelSetSubBoundary> subBdys;
  const CMicrostructure *microstructure;
  const int nbinsx, nbinsy;
public:
  PixelSetBoundary(const CMicrostructure*, int nbinsx, int nbinsy);
  void add_pixel(const ICoord&);
  void find_boundary();

  double clippedArea(const LineList&) const;
  double area() const;
};


// For debugging....
std::ostream& operator<<(std::ostream &, const PixelSetBoundary &);


#endif // PIXELSETBOUNDARY_H
