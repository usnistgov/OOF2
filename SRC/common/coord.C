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
#include "coord.h"

Coord &Coord::operator+=(const ICoord &ic) {
  x[0] += ic[0];
  x[1] += ic[1];
  return *this;
}

Coord &Coord::operator-=(const ICoord &ic) {
  x[0] -= ic[0];
  x[1] -= ic[1];
  return *this;
}

std::ostream &operator<<(std::ostream &os, const Coord &coord) {
  os << "(" << coord[0] << ", " << coord[1] << ")";
  return os;
}

std::istream &operator>>(std::istream &is, Coord &coord) {
  char c;
  is >> c;
  if(!is || c != '(') {		// check for initial '('
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord[0];		// read x component
  if(!is) return is;		// check for error
  is >> c;
  if(!is || c != ',') {		// check for ','
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord[1];
  if(!is) return is;
  is >> c;
  if(!is || c != ')') {
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  return is;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const ICoord &coord) {
  os << "(" << coord[0] << ", " << coord[1] << ")";
  return os;
}

std::istream &operator>>(std::istream &is, ICoord &coord) {
  char c;
  is >> c;
  if(!is || c != '(') {		// check for initial '('
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord[0];		// read x component
  if(!is) return is;		// check for error
  is >> c;
  if(!is || c != ',') {		// check for ','
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  is >> coord[1];
  if(!is) return is;
  is >> c;
  if(!is || c != ')') {
    is.clear(std::ios::badbit | is.rdstate());
    return is;
  }
  return is;
}

