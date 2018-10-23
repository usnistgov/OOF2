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

class PBLBase {
public:
  virtual ~PBLBase() {}
  virtual ClippedPixelBdyLoop *clip(const Line&) const = 0;
  virtual double areaInPixelUnits() const = 0;
};

template <class CTYPE, class RTYPE>
class PxlBdyLoopBase : public PBLBase {
protected:
  std::vector<CTYPE> loop;
  RTYPE *bounds;
  void pop_back() { loop.pop_back(); }
  // void prepend(PxlBdyLoopBase<CTYPE, RTYPE> &);
public:
  PxlBdyLoopBase() : bounds(nullptr) {}
  PxlBdyLoopBase(const std::vector<CTYPE>&, const RTYPE*);
  virtual ~PxlBdyLoopBase() { delete bounds; }
  unsigned int size() const { return loop.size(); }
  const RTYPE *bbox() const { return bounds; }
  const std::vector<CTYPE> &getLoop() const { return loop; }
  // clippedArea returns the area of the polygon formed by clipping
  // with all of the given lines.
  double clippedArea(const LineList&) const;
  virtual double areaInPixelUnits() const;
  // clip() returns a new loop that includes the points to the left of
  // the line (not just the segment) going from line.first to
  // line.second, which are Coords.  Usually called by clippedArea().
  // The new loop may contain degenerate or collinear antiparallel
  // segments.
  virtual ClippedPixelBdyLoop *clip(const Line&) const;
};

class PixelBdyLoop : public PxlBdyLoopBase<ICoord, ICRectangle> {
public:
  void add_point(const ICoord&);
  void clean(const CMicrostructure*);
  bool closed() const;

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
  // ClippedPixelBdyLoop(ClippedPixelBdyLoop&&); // Move constructor
  Coord operator[](unsigned int k) const { return loop[k]; }
  void add(const Coord&);
  void add(const ICoord&);
  // void prepend(const ClippedPixelBdyLoop*);
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
