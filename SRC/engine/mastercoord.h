// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MASTERCOORD_H		/* We also take Discoover and Viisa */
#define MASTERCOORD_H

class MasterCoord;
class MasterPosition;

#include <oofconfig.h>
#include <iostream>
#include <deque>

class Element;
class ShapeFunction;

// The Coord and MasterCoord classes used to be both derived from the
// same template, so that they could share the same code but still be
// distinct classes. That doesn't work now that Coord is derived from
// Position, but MasterCoord isn't.  So now the classes have
// separate but equal definitions.


// The MasterPosition base class allows MasterCoord and GaussPoint to
// be passed to the same functions.

class MasterPosition {
public:
  virtual ~MasterPosition() {}
  virtual MasterCoord mastercoord() const = 0;
  // Shape functions and their derivatives wrt master coordinates are
  // evaluated through these double-dispatch functions.
  virtual double shapefunction(const ShapeFunction&, int) const = 0;
  virtual double mdshapefunction(const ShapeFunction&, int, int) const = 0;
  virtual double dshapefunction(const Element*, const ShapeFunction&, int, int)
    const = 0;
  virtual std::ostream &print(std::ostream&) const = 0;
};

std::ostream &operator<<(std::ostream&, const MasterPosition&);

class MasterCoord : public MasterPosition {
protected:
  double x[2];
public:
  MasterCoord() { x[0] = x[1] = 0; }
  MasterCoord(double x1, double x2) { x[0] = x1; x[1] = x2; }
  MasterCoord(const MasterCoord &c) { x[0] = c.x[0]; x[1] = c.x[1]; }
  virtual MasterCoord mastercoord() const { return *this; }
  double operator[](int i) const { return x[i]; }
  double &operator[](int i) { return x[i]; }
  MasterCoord &operator+=(const MasterCoord &c) {
    x[0] += c[0];
    x[1] += c[1];
    return *this;
  }
  MasterCoord &operator*=(double y) {
    x[0] *= y;
    x[1] *= y;
    return *this;
  }
  virtual double shapefunction(const ShapeFunction&, int) const;
  virtual double mdshapefunction(const ShapeFunction&, int, int) const;
  virtual double dshapefunction(const Element*, const ShapeFunction&, int, int)
    const;
  virtual std::ostream &print(std::ostream&) const;
  friend bool operator==(const MasterCoord&, const MasterCoord&);
};

std::ostream &operator<<(std::ostream&, const MasterCoord&);

std::istream &operator>>(std::istream&, MasterCoord&);

inline MasterCoord operator+(const MasterCoord &a, const MasterCoord &b) {
  MasterCoord result(a);
  result += b;
  return result;
}

inline MasterCoord operator-(const MasterCoord &a, const MasterCoord &b) {
  return MasterCoord(a[0]-b[0], a[1]-b[1]);
}

inline MasterCoord operator*(const MasterCoord &a, double x) {
  MasterCoord b(a);
  b *= x;
  return b;
}

inline MasterCoord operator*(double x, const MasterCoord &a) {
  MasterCoord b(a);
  b *= x;
  return b;
}

inline MasterCoord operator/(const MasterCoord &a, double x) {
  MasterCoord b(a);
  b *= (1/x);
  return b;
}

inline double cross(const MasterCoord &c1, const MasterCoord &c2)
{
  return c1[0]*c2[1] - c1[1]*c2[0];
}

inline double operator%(const MasterCoord &c1, const MasterCoord &c2)
{
  return(cross(c1,c2));
}

inline bool operator==(const MasterCoord &a, const MasterCoord &b) {
  return a.x[0] == b.x[0] && a.x[1] == b.x[1];
}

inline bool operator<(const MasterCoord &a, const MasterCoord &b) {
  return (a[0] < b[0]) || (a[0] == b[0] && a[1] < b[1]);
}

inline double dot(const MasterCoord &c1, const MasterCoord &c2) {
  return c1[0]*c2[0] + c1[1]*c2[1];
}

inline double norm2(const MasterCoord &c) {
  return dot(c, c);
}



// MasterEndPoint marks the ends of contours. 'start' indicates which
// end it is.  The default constructor is never actually used, but
// without it it's not possible to construct a
// std::vector<MasterEndPoint>.

class MasterEndPoint {
public:
  MasterEndPoint(const MasterCoord *mc, bool start) : mc(mc), start(start) {}
  MasterEndPoint() : mc(0), start(false) {}
  double operator[](int i) const { return (*mc)[i]; }
  const MasterCoord *mc;
  bool start;
};

std::ostream &operator<<(std::ostream &os, const MasterEndPoint&);

typedef bool (*MasterEndPointComparator)(const MasterEndPoint&,
					 const MasterEndPoint&);

typedef std::deque<const MasterCoord*> CCurve;

#endif // MASTERCOORD_H
