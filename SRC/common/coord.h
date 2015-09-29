// -*- C++ -*-
// $RCSfile: coord.h,v $
// $Revision: 1.28 $
// $Author: langer $
// $Date: 2014/05/29 14:38:03 $

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
public:
	// DIM dependent
  Coord(double x0, double y0) : x(x0), y(y0) {} // For now, leave this so we can compile as we update everything else
#if DIM == 2
  double x, y;
  Coord() : x(0.0), y(0.0) {}
  inline double operator()(int i) const {return (i==0? x : y); }
  inline double &operator()(int i) { return (i==0? x : y); }
  inline Coord &operator+=(const Coord &c) { x+=c.x; y+=c.y; return *this; }
  inline Coord &operator-=(const Coord &c) { x-=c.x; y-=c.y; return *this; }
  Coord &operator*=(double f) { x*=f; y*=f; return *this; }
  Coord &operator/=(double f) { x/=f; y/=f; return *this; }
#elif DIM == 3
  double x, y, z;
  Coord() : x(0.0), y(0.0), z(0.0) {}
  Coord(double x0, double y0, double z0) : x(x0), y(y0), z(z0) {}
  inline double operator()(int i) const {
		switch(i) {
		case 0:
			return x;
		case 1:
			return y;
		default:
			return z;
		}
	}
  inline double &operator()(int i) { 
		switch(i) {
		case 0:
			return x;
		case 1:
			return y;
		default:
			return z;
		}
	}
  inline Coord &operator+=(const Coord &c) { x+=c.x; y+=c.y; z+=c.z; return *this; }
  inline Coord &operator-=(const Coord &c) { x-=c.x; y-=c.y; z-=c.z; return *this; }
  Coord &operator*=(double f) { x*=f; y*=f; z*=f; return *this; }
  Coord &operator/=(double f) { x/=f; y/=f; z/=f; return *this; }
	void writePointer(double pt[3]) { pt[0]=x; pt[1]=y; pt[2]=z; }
#endif

	// DIM independent
  Coord &operator+=(const ICoord&);
  Coord &operator-=(const ICoord&);
  virtual ~Coord() {}
  virtual Coord position() const { return *this; }
};


inline bool operator<(const Coord &a, const Coord &b) {
  if(a.x < b.x) return true;
  if(a.x > b.x) return false;
  if(a.y < b.y) return true;
#if DIM == 3
	if(a.y > b.y) return false;
	if(a.z < b.z) return true;
#endif
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

#if DIM==2

inline double cross(const Coord &c1, const Coord &c2)
{
  return c1.x*c2.y - c1.y*c2.x;
}

inline bool operator==(const Coord &a, const Coord &b) {
  return a.x == b.x && a.y == b.y;
}

inline bool operator!=(const Coord &a, const Coord &b) {
  return a.x != b.x || a.y != b.y;
}

inline double dot(const Coord &c1, const Coord &c2) {
  return c1.x*c2.x + c1.y*c2.y;
}

inline double operator%(const Coord &c1, const Coord &c2)
{
  return(cross(c1,c2));
}

#elif DIM==3

inline double dot(const Coord &c1, const Coord &c2) {
  return c1.x*c2.x + c1.y*c2.y + c1.z*c2.z;
}

inline Coord cross(const Coord &c1, const Coord &c2)
{
	Coord temp((c1.y*c2.z-c1.z*c2.y),
		   (c1.z*c2.x-c1.x*c2.z),
		   (c1.x*c2.y-c1.y*c2.x));
	return temp;
}

inline bool operator==(const Coord &a, const Coord &b) {
  return a.x == b.x && a.y == b.y && a.z == b.z;
}

inline bool operator!=(const Coord &a, const Coord &b) {
  return a.x != b.x || a.y != b.y || a.z != b.z;
}

inline Coord operator%(const Coord &c1, const Coord &c2)
{
  return(cross(c1,c2));
}

#endif

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

  // functions with DIM dependent prototypes
	//#if DIM == 2
	ICoord(int x0, int x1) { x[0] = x0; x[1] = x1; } //Keep available for now
#if DIM==3
	ICoord(int x0, int x1, int x2) { x[0] = x0; x[1] = x1; x[2] = x2; }
#endif

	ICoord() { for(int i=0; i<DIM; i++) x[i]=0; } //x[0] = x[1] = 0; }
  inline int operator()(int i) const { return x[i]; }
  inline int &operator()(int i) { return x[i]; }
  ICoord &operator+=(const ICoord &c) {
		for(int i=0; i<DIM; i++)
			x[i] += c(i);
    return *this;
  }
  ICoord &operator-=(const ICoord &c) {
		for(int i=0; i<DIM; i++)	
			x[i] -= c(i);
    return *this;
  }
  ICoord &operator*=(int y) {
		for(int i=0; i<DIM; i++)	
			x[i] *= y;
    return *this;
  }
  friend bool operator==(const ICoord&, const ICoord&);
  friend bool operator!=(const ICoord&, const ICoord&);
#if DIM==3
	void writePointer(double pt[3]) { pt[0]=(double)x[0]; pt[1]=(double)x[1]; pt[2]=(double)x[2]; }
#endif
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

inline Coord operator-(const ICoord &b, const Coord &a) {
  Coord result(a);
  result -= b;
  return result;
}

inline ICoord operator*(const ICoord &a, int x) {
  ICoord b(a);
  b *= x;
  return b;
}

inline Coord operator*(const ICoord &a, double x) {
#if DIM == 2
  Coord b(a(0), a(1));
#elif DIM == 3
	Coord b(a(0), a(1), a(2));
#endif
  b *= x;
  return b;
}

#if DIM == 2
inline bool operator==(const ICoord &a, const ICoord &b) {
	return a.x[0] == b.x[0] && a.x[1] == b.x[1];
}

inline bool operator!=(const ICoord &a, const ICoord &b) {
	return a.x[0] != b.x[0] || a.x[1] != b.x[1];
}

inline bool operator!=(const ICoord &a, const Coord &b) {
	return a(0) != b.x || a(1) != b.y;
}

#elif DIM == 3
inline bool operator==(const ICoord &a, const ICoord &b) {
	return a.x[0] == b.x[0] && a.x[1] == b.x[1] && a.x[2] == b.x[2];
}

inline bool operator!=(const ICoord &a, const ICoord &b) {
	return a.x[0] != b.x[0] || a.x[1] != b.x[1] || a.x[2] != b.x[2];
}

inline bool operator!=(const ICoord &a, const Coord &b) {
	return a(0) != b.x || a(1) != b.y || a(2) != b.z;
}
#endif

inline int dot(const ICoord &c1, const ICoord &c2) {
	int dotproduct = 0;
	for(int i=0; i<DIM; i++)	
		dotproduct += c1(i)*c2(i);
	return dotproduct;
}

inline double dot(const Coord &c1, const ICoord &c2) {
	double dotproduct = 0;
	for(int i=0; i<DIM; i++)	
		dotproduct += c1(i)*(double)c2(i);
	return dotproduct;
}

inline int norm2(const ICoord &c) {
  return dot(c, c);
}

bool operator<(const ICoord &a, const ICoord &b);



//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//

// Utility segment class -- contains a directed pair of points,
// and can compute the area it sweeps out relative to some
// other point.
class CoordSegment {
private:
  Coord start, end;
public:
  CoordSegment() {}
  CoordSegment(Coord p1, Coord p2) : start(p1), end(p2) {}
  double area(const Coord &) const;
  bool operator<(const CoordSegment &) const;
};






#endif // COORD_H
