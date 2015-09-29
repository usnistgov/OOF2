// -*- C++ -*-
// $RCSfile: pixelsetboundary.h,v $
// $Revision: 1.27 $
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

#ifndef PIXELSETBOUNDARY_H
#define PIXELSETBOUNDARY_H

#include <map>
#include <set>
#include <vector>

#include "common/coord.h"
#include "common/geometry.h"

class CMicrostructure;

// Special classes for keeping track of the boundaries of pixel sets.

class PixelSetBoundary;


// Special utility class for pixel boundary intersections, so we can
// keep track of "incoming" versus "outgoing" intersections.  Incoming
// and outgoing are intended to be used with respect to elements --
// entry==true means that the pixel boundary enters the element at
// this intersection, and entry==false means that it exits the element
// at this intersection.
class PixelBdyIntersection {
private:
  // The node-index and fraction values are specific to a particular
  // skeleton element, and are filled in by the cskeleton element.
  // The node index is an integer indicating which node is at the
  // start of the element boundary on which the intersection occurs,
  // and the "fraction" number is the square of the distance from the
  // start of this element boundary to the location of the
  // intersection.
  int node_index;
  double fraction; 
public:
  Coord location;
  bool entry;

  PixelBdyIntersection(Coord &loc, bool ntry) 
    : node_index(0), fraction(0), location(loc), entry(ntry) {} 
  PixelBdyIntersection() : node_index(0), fraction(0), 
			   location(Coord(0.0,0.0)), entry(false) {}
  void set_element_data(int ni, double f) {
    node_index = ni;
    fraction = f;
  }
  int get_element_node_index() const { return node_index; }
  double get_element_fraction() const { return fraction; }
};

std::ostream &operator<<(std::ostream&, const PixelBdyIntersection&);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class PixelBdyLoop {
private:
  std::vector<ICoord> loop;
  CRectangle *bounds;		// computed by clean
  const PixelSetBoundary *pixelSetBdy;
public:
  PixelBdyLoop(const PixelSetBoundary *psb)
    : bounds(0), pixelSetBdy(psb)
  {}
  ~PixelBdyLoop();
  void add_point(const ICoord&);
  void clean(const CMicrostructure*);
  bool closed() const;
  const CRectangle &bbox() const { return *bounds; }
  unsigned int size() const { return loop.size(); }
  const std::vector<ICoord> &segments() const { return loop; }

  int find_one_intersection(unsigned int, const Coord *const pts, int npts,
			    bool, PixelBdyIntersection &pbi) const;
  bool find_no_intersection(unsigned int, const Coord* const, int,
			    const Coord&) const;

  // The following methods return information about a given segment in
  // the loop.  Their values could be cached when the loop is cleaned,
  // if recomputing them is too slow.  They're used a lot in the
  // homogeneity calculation.
  ICoord icoord(unsigned int) const;
  ICoord next_icoord(unsigned int) const;
  Coord coord(unsigned int) const;
  Coord next_coord(unsigned int) const;
  bool horizontal(unsigned int) const;
  bool decreasing(unsigned int) const;
  
  friend std::ostream& operator<<(std::ostream&, const PixelBdyLoop&);
  friend class PixelSetBoundary; // for debugging
};

std::ostream& operator<<(std::ostream&, const PixelBdyLoop&);
typedef std::set<ICoord> SegSet;
typedef std::multimap<ICoord, ICoord> CoordMap; // start point, direction

// Pixel set boundary knows its microstructure.  The way this works
// is, you create it with a microstructure, then put in all the pixels
// in the pixel set for which you want this to be the boundary, then
// call the "find_boundary" method, which finds all the loops and
// assigns them to the "loopset" member.
class PixelSetBoundary {
private:
  SegSet segmentsLR;		// segments going from left to right
  SegSet segmentsRL;		// ... right to left
  SegSet segmentsUD;		// ... up to down
  SegSet segmentsDU;		// ... down to up
  std::vector<PixelBdyLoop*> loopset;
  PixelBdyLoop *find_loop(CoordMap&);
  const CMicrostructure* microstructure;
public:
  PixelSetBoundary(const CMicrostructure*);
  ~PixelSetBoundary();
  void add_pixel(const ICoord&);
  void find_boundary();
  const std::vector<PixelBdyLoop*> &get_loops() const { return loopset; }

  friend std::ostream& operator<<(std::ostream &, const PixelSetBoundary&);
  friend class PixelBdyLoop;
};


// For debugging....
std::ostream& operator<<(std::ostream &, const PixelSetBoundary &);


#endif // PIXELSETBOUNDARY_H
