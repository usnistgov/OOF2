// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef COORD_H
#define COORD_H

class Coord;
class ICoord;
class Position;

#include <oofconfig.h>
#include <iostream>
using namespace std;

// The Coord and MasterCoord classes used to be both derived from the
// same template, so that they could share the same code but still be
// distinct classes. That doesn't work now that Coord is derived from
// Position, but MasterCoord isn't.  So now the classes have
// separate but equal definitions.

// The Position base class allows simple objects like Coord and
// complex objects like GaussPoint to be passed to the same functions,
// if all they need to know is the position of the object.

class Position {
public:
  virtual ~Position () {}
  virtual Coord position() const = 0;
};

class Coord: public Position {
private:
  double x[2];
public:
  Coord() : x{0.0, 0.0} {}
  Coord(double x0, double x1) { x[0] = x0; x[1] = x1; }
  // TODO: Remove operator().  Use operator[] instead.
  inline double operator()(int i) const { return x[i]; }
  inline double &operator()(int i) { return x[i]; }
  inline double operator[](int i) const {
    assert(i==0 || i==1);
    return x[i];
  }
  inline double &operator[](int i) {
    assert(i==0 || i==1);
    return x[i];
  }
  inline Coord &operator+=(const Coord &c) {
    x[0]+=c[0];
    x[1]+=c[1];
    return *this;
  }
  inline Coord &operator-=(const Coord &c) {
    x[0]-=c[0];
    x[1]-=c[1];
    return *this;
  }
  Coord &operator*=(double f) {
    x[0]*=f;
    x[1]*=f;
    return *this; }
  Coord &operator/=(double f) {
    x[0]/=f;
    x[1]/=f;
    return *this;
  }
  Coord &operator+=(const ICoord&);
  Coord &operator-=(const ICoord&);
  virtual ~Coord() {}
  virtual Coord position() const { return *this; }
};


inline bool operator<(const Coord &a, const Coord &b) {
  if(a[0] < b[0]) return true;
  if(a[0] > b[0]) return false;
  if(a[1] < b[1]) return true;
  return false;
}

std::ostream &operator<<(std::ostream&, const Coord&);
std::istream &operator>>(std::istream&, Coord&);

inline Coord operator+(const Coord &a, const Coord &b) {
  Coord result(a);
  result += b;
  return result;
}

inline Coord operator-(const Coord &a, const Coord &b) {
  Coord result(a);
  result -= b;
  return result;
}

inline Coord operator*(const Coord &a, double x) {
  Coord b(a);
  b *= x;
  return b;
}

inline Coord operator*(double x, const Coord &a) {
  Coord b(a);
  b *= x;
  return b;
}

template <class COORD1, class COORD2>
inline double cross(const COORD1 &c1, const COORD2 &c2)
{
  // return c1.x*c2.y - c1.y*c2.x;
  return c1[0]*c2[1] - c1[1]*c2[0];
}

inline bool operator==(const Coord &a, const Coord &b) {
  return a[0] == b[0] && a[1] == b[1];
}

inline bool operator!=(const Coord &a, const Coord &b) {
  return a[0] != b[0] || a[1] != b[1];
}

inline double dot(const Coord &c1, const Coord &c2) {
  return c1[0]*c2[0] + c1[1]*c2[1];
}

inline double operator%(const Coord &c1, const Coord &c2)
{
  return(cross(c1,c2));
}

inline double norm2(const Coord &c) {
  return dot(c, c);
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Integer coordinates

class ICoord {
protected:
  int x[DIM];
public:
  virtual ~ICoord() {}
  ICoord(int x0, int x1) { x[0] = x0; x[1] = x1; }
  ICoord() { x[0] = 0; x[1] = 0; }
  // TODO: Remove operator().  Use operator[] instead.
  inline int operator()(int i) const { return x[i]; }
  inline int &operator()(int i) { return x[i]; }
  inline int operator[](int i) const { return x[i]; }
  inline int &operator[](int i) { return x[i]; }
  ICoord &operator+=(const ICoord &c) {
    x[0] += c[0];
    x[1] += c[1];
    return *this;
  }
  ICoord &operator-=(const ICoord &c) {
    x[0] -= c[0];
    x[1] -= c[1];
    return *this;
  }
  ICoord &operator*=(int y) {
    x[0] *= y;
    x[1] *= y;
    return *this;
  }
  friend bool operator==(const ICoord&, const ICoord&);
  friend bool operator!=(const ICoord&, const ICoord&);
};

std::ostream &operator<<(std::ostream&, const ICoord&);
std::istream &operator>>(std::istream&, ICoord&);

inline ICoord operator+(const ICoord &a, const ICoord &b) {
  ICoord result(a);
  result += b;
  return result;
}

inline ICoord operator-(const ICoord &a, const ICoord &b) {
  ICoord result(a);
  result -= b;
  return result;
}

inline Coord operator+(const Coord &a, const ICoord &b) {
  Coord result(a);
  result += b;
  return result;
}

inline Coord operator-(const Coord &a, const ICoord &b) {
  Coord result(a);
  result -= b;
  return result;
}

inline Coord operator+(const ICoord &b, const Coord &a) {
  Coord result(a);
  result += b;
  return result;
}

inline Coord operator-(const ICoord &a, const Coord &b) {
  Coord result(a(0), a(1));
  result -= b;
  return result;
}

inline ICoord operator*(const ICoord &a, int x) {
  ICoord b(a);
  b *= x;
  return b;
}

inline Coord operator*(const ICoord &a, double x) {
  Coord b(a(0), a(1));
  b *= x;
  return b;
}

inline bool operator==(const ICoord &a, const ICoord &b) {
  return a[0] == b[0] && a[1] == b[1];
}

inline bool operator!=(const ICoord &a, const ICoord &b) {
  return a[0] != b[0] || a[1] != b[1];
}

inline bool operator!=(const ICoord &a, const Coord &b) {
  return a[0] != b[0] || a[1] != b[1];
}

inline int dot(const ICoord &c1, const ICoord &c2) {
  return c1[0]*c2[0] + c1[1]*c2[1];
}

inline double dot(const Coord &c1, const ICoord &c2) {
  return c1[0]*c2[0] + c1[1]*c2[1];
}

inline int norm2(const ICoord &c) {
  return dot(c, c);
}

inline bool operator<(const ICoord &a, const ICoord &b) {
  if(a[0] < b[0]) return true;
  if(a[0] > b[0]) return false;
  if(a[1] < b[1]) return true;
  return false;
}

// Convenience function for creating an ICoord from args that might be
// long ints.  Use with care.

template <class TYPE0, class TYPE1>
ICoord iCoordL(const TYPE0 i, const TYPE1 j) {
  assert (i <= std::numeric_limits<int>::max() &&
	  j <= std::numeric_limits<int>::max());
  return ICoord(int(i), int(j));
}

#endif // COORD_H
