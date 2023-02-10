// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef COORD_SWG
#define COORD_SWG

%module(package="ooflib.SWIG.common") coord

%include "common/typemaps.swg"
%{
#include "common/coord.h"
%}


%nodefaultctor Position;
class Position {};
  
class Coord : public Position {
public:
  Coord(double x1, double x2);
  ~Coord();
};

%extend Coord {
  // This function is 'getitem', not '__getitem__', because
  // __getitem__ is defined in terms of getitem in the .spy file.
  // __getitem__ raises a Python exception if the argument is out of
  // range.
  double getitem(int i) {
    return (*self)(i);
  }
  int __len__() {
    return DIM;
  }
  Coord __mul__(double x) {
    return (*self)*x;
  }
  Coord __rmul__(double x) {
    return (*self)*x;
  }
}

class ICoord {
public:
  ICoord(int x, int y);
};

%extend ICoord {
  int __getitem__(int i) {
    return (*self)(i);
  }
  int __len__() {
    return DIM;
  }
  ICoord __mul__(int x) {
    return (*self)*x;
  }
  ICoord __rmul__(int x) {
    return (*self)*x;
  }
}

MAKE_LISTVEC_TYPEMAPS(Coord);
MAKE_LISTVEC_TYPEMAPS(ICoord);

%pythoncode "common/coord.spy"

#endif // COORD_SWG
