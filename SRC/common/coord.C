// -*- C++ -*-
// $RCSfile: coord.C,v $
// $Revision: 1.13 $
// $Author: langer $
// $Date: 2014/09/27 21:40:19 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "coord.h"

Coord &Coord::operator+=(const ICoord &ic) {
  x += ic(0);
  y += ic(1);
#if DIM == 3
	z += ic(2);
#endif
  return *this;
}

Coord &Coord::operator-=(const ICoord &ic) {
  x -= ic(0);
  y -= ic(1);
#if DIM == 3
	z -= ic(2);
#endif
  return *this;
}

std::ostream &operator<<(std::ostream &os, const Coord &coord) {
  os << "(" << coord.x << ", " << coord.y;
#if DIM == 3
	os << ", " << coord.z;
#endif
	os << ")";
  return os;
}

std::istream &operator>>(std::istream &is, Coord &coord) {
  char c;
  is >> c;
  if(!is || c != '(') {		// check for initial '('
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord.x;		// read x component
  if(!is) return is;		// check for error
  is >> c;
  if(!is || c != ',') {		// check for ','
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord.y;
  if(!is) return is;
  is >> c;
#if DIM == 3
  if(!is || c != ',') {		// check for ','
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord.z;
  if(!is) return is;
  is >> c;	
#endif
  if(!is || c != ')') {
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  return is;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const ICoord &coord) {
  os << "(" << coord(0) << ", " << coord(1);
#if DIM == 3
	os << ", " << coord(2);
#endif
	os << ")";
  return os;
}

std::istream &operator>>(std::istream &is, ICoord &coord) {
  char c;
  is >> c;
  if(!is || c != '(') {		// check for initial '('
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord(0);		// read x component
  if(!is) return is;		// check for error
  is >> c;
  if(!is || c != ',') {		// check for ','
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord(1);
  if(!is) return is;
  is >> c;
#if DIM == 3
  if(!is || c != ',') {		// check for ','
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord(2);
  if(!is) return is;
  is >> c;
#endif
  if(!is || c != ')') {
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  return is;
}

bool operator<(const ICoord &a, const ICoord &b) {
  if(a(0) < b(0)) return true;
  if(a(0) > b(0)) return false;
  if(a(1) < b(1)) return true;
#if DIM == 3
	if(a(1) > b(1)) return false;
	if(a(2) < b(2)) return true;
#endif
  return false;
}


//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//

double CoordSegment::area(const Coord &ctr) const {
  // Avoid constructing new objects...
	// TODO: how will this be used in 3D???
  return (start.x-ctr.x)*(end.y-ctr.y) - (start.y-ctr.y)*(end.x-ctr.x);
}

bool CoordSegment::operator<(const CoordSegment &other) const {
  if (other.start < start) return true;
  if (start < other.start) return false;
  if (other.end < end) return true;
  return false;
}
