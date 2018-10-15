// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Simple geometrical objects defined in terms of Coords.

#ifndef GEOMETRY_H
#define GEOMETRY_H

// The geometrical objects defined here are stored in C++, unlike
// those defined in IO/primitives.py, which are stored in Python.  Use
// whichever is more efficient in any given context.

#include <oofconfig.h>
#include "common/coord.h"
#include "common/ooferror.h"
#include <iostream>
#include <vector>

#define min(a,b) ((a) < (b)? (a) : (b))
#define max(a,b) ((a) > (b)? (a) : (b))

// CTYPE is the type of the corner (Coord, ICoord, etc)
// VTYPE is the type of a coordinate (double, int, etc)

template <class VTYPE, class CTYPE>
class CPolygon {
public:
  virtual ~CPolygon() {}
  virtual bool contains(const CTYPE&) const = 0;
  virtual int ncorners() const = 0;
  virtual CTYPE operator[](int) const = 0; // returns a corner
  virtual VTYPE area() const = 0;
};

template <class VTYPE, class CTYPE>
std::ostream &operator<<(std::ostream &os, const CPolygon<VTYPE, CTYPE> &poly) {
  os << "CPolygon:";
  for(int i=0; i<poly.ncorners(); i++)
    os << " " << poly[i];
  return os;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

template <class VTYPE, class CTYPE>
class CRectangle_ : public CPolygon<VTYPE, CTYPE> {
protected:
  CTYPE upright;
  CTYPE lowleft;
  CTYPE size_;
public:
  CRectangle_() {}
  CRectangle_(const CTYPE &a, const CTYPE &b);
  virtual ~CRectangle_() {}
  inline const CTYPE &lowerleft() const { return lowleft; }
  inline const CTYPE &upperright() const { return upright; }
  void swallow(const CTYPE &pt) {
    if(upright(0) < pt(0)) upright(0) = pt(0);
    if(upright(1) < pt(1)) upright(1) = pt(1);
    if(lowleft(0) > pt(0)) lowleft(0) = pt(0);
    if(lowleft(1) > pt(1)) lowleft(1) = pt(1);
  }
  inline VTYPE xmin() const { return lowleft(0); }
  inline VTYPE xmax() const { return upright(0); }
  inline VTYPE ymin() const { return lowleft(1); }
  inline VTYPE ymax() const { return upright(1); }
  inline VTYPE height() const { return upright(1) - lowleft(1); }
  inline VTYPE width() const { return upright(0) - lowleft(0); }
  inline virtual VTYPE area() const { return width()*height(); }
  inline const CTYPE &size() const { return size_; }
  bool contains(const CTYPE &point) const {
    if(point(0) < xmin() || point(0) >= xmax()) return false;
    if(point(1) < ymin() || point(1) >= ymax()) return false;
    return true;
  }
  bool intersects(const CRectangle_<VTYPE, CTYPE> &other) const {
    if(upright(0) < other.lowleft(0)) return false;
    if(upright(1) < other.lowleft(1)) return false;
    if(lowleft(0) > other.upright(0)) return false;
    if(lowleft(1) > other.upright(1)) return false;
    return true;
  }
  virtual int ncorners() const { return 4; }
  virtual CTYPE operator[](int i) const {
    switch(i) {
    case 0:
      return lowleft;
    case 1:
      return CTYPE(upright(0), lowleft(1));
    case 2:
      return upright;
    case 3:
      return CTYPE(lowleft(0), upright(1));
    };
    throw ErrBadIndex(i, __FILE__, __LINE__);
  }
  // 
  void restrict(const CRectangle_<VTYPE, CTYPE> &limits) {
    if(limits.xmin() > lowleft(0))
      lowleft(0) = min(upright(0), limits.xmin());
    if(limits.xmax() < upright(0))
      upright(0) = max(lowleft(0), limits.xmax());
    if(limits.ymin() > lowleft(1))
      lowleft(1) = min(upright(1), limits.ymin());
    if(limits.ymax() < upright(1))
      upright(1) = max(lowleft(1), limits.ymax());
    size_ = upright - lowleft;
  }

  virtual std::ostream &print(std::ostream&) const = 0;

};

template <class VTYPE, class CTYPE>
CRectangle_<VTYPE, CTYPE>::CRectangle_(const CTYPE &a, const CTYPE &b) {
  if(a(0) < b(0)) {
    upright(0) = b(0);
    lowleft(0) = a(0);
  }
  else {
    upright(0) = a(0);
    lowleft(0) = b(0);
  }
  if(a(1) < b(1)) {
    upright(1) = b(1);
    lowleft(1) = a(1);
  }
  else {
    upright(1) = a(1);
    lowleft(1) = b(1);
  }
  size_ = upright - lowleft;
}

class CRectangle: public CRectangle_<double, Coord> {
public:
  CRectangle(const Coord &a, const Coord &b)
    : CRectangle_<double, Coord>(a,b)
  {}
  CRectangle(const ICoord &a, const ICoord &b)
    : CRectangle_<double, Coord>(Coord(a(0), a(1)), Coord(b(0), b(1)))
  {}
  friend std::ostream& operator<<(std::ostream &os, const CRectangle &rect) {
    os << "CRectangle(" << rect.lowleft << ", " << rect.upright << ")";
    return os;
  }
  virtual std::ostream &print(std::ostream &os) const {
    return os << *this;
  }
  void expand(double howmuch) {
    double mid = 0.5*(lowleft(0) + upright(0));
    double size = 0.5*(upright(0) - lowleft(0))*(1 + howmuch);
    lowleft(0) = mid - size;
    upright(0) = mid + size;
    mid = 0.5*(lowleft(1) + upright(1));
    size = 0.5*(upright(1) - lowleft(1))*(1 + howmuch);
    lowleft(1) = mid - size;
    upright(1) = mid + size;
    size_ = upright - lowleft;
  }
};

class ICRectangle : public CRectangle_<int, ICoord> {
public:
  ICRectangle() {}
  ICRectangle(const ICoord &a, const ICoord &b)
    : CRectangle_<int, ICoord>(a,b)
  {}
  friend std::ostream& operator<<(std::ostream &os, const ICRectangle &rect) {
    os << "ICRectangle(" << rect.lowleft << ", " << rect.upright << ")";
    return os;
  }
  virtual std::ostream &print(std::ostream &os) const {
    return os << *this;
  }    
};


#if DIM == 3

template <class VTYPE, class CTYPE>
class CRectangularPrism_  {
protected:
  CTYPE uprightfront;
  CTYPE lowleftback;
public:
  CRectangularPrism_() {}
  CRectangularPrism_(const CTYPE &a, const CTYPE &b);
  virtual ~CRectangularPrism_() {}
	// for compatibility with 2D code, perhaps a more general name
	// should be found for both versions.
  inline const CTYPE &lowerleft() const { return lowleftback; }
  inline const CTYPE &upperright() const { return uprightfront; }
  inline const CTYPE &lowerleftback() const { return lowleftback; }
  inline const CTYPE &upperrightfront() const { return uprightfront; }
  void swallow(const CTYPE &pt) {
    if(uprightfront(0) < pt(0)) uprightfront(0) = pt(0);
    if(uprightfront(1) < pt(1)) uprightfront(1) = pt(1);
    if(uprightfront(2) < pt(2)) uprightfront(2) = pt(2);
    if(lowleftback(0) > pt(0)) lowleftback(0) = pt(0);
    if(lowleftback(1) > pt(1)) lowleftback(1) = pt(1);
    if(lowleftback(2) > pt(2)) lowleftback(2) = pt(2);
  }
  inline VTYPE xmin() const { return lowleftback(0); }
  inline VTYPE xmax() const { return uprightfront(0); }
  inline VTYPE ymin() const { return lowleftback(1); }
  inline VTYPE ymax() const { return uprightfront(1); }
  inline VTYPE zmin() const { return lowleftback(2); }
  inline VTYPE zmax() const { return uprightfront(2); }
  inline VTYPE height() const { return uprightfront(1) - lowleftback(1); }
  inline VTYPE width() const { return uprightfront(0) - lowleftback(0); }
  inline VTYPE depth() const { return uprightfront(2) - lowleftback(2); }
  inline virtual VTYPE volume() const { return width()*height()*depth(); }
  inline CTYPE size() const { return uprightfront - lowleftback; }
  bool contains(const CTYPE &point) const {
    if(point(0) < xmin() || point(0) >= xmax()) return false;
    if(point(1) < ymin() || point(1) >= ymax()) return false;
    if(point(2) < zmin() || point(2) >= zmax()) return false;
    return true;
  }
  bool intersects(const CRectangularPrism_<VTYPE, CTYPE> &other) const {
    if(uprightfront(0) < other.lowleftback(0)) return false;
    if(uprightfront(1) < other.lowleftback(1)) return false;
    if(uprightfront(2) < other.lowleftback(2)) return false;
    if(lowleftback(0) > other.uprightfront(0)) return false;
    if(lowleftback(1) > other.uprightfront(1)) return false;
    if(lowleftback(2) > other.uprightfront(2)) return false;
    return true;
  }
  virtual int ncorners() const { return 8; }
  virtual CTYPE operator[](int i) const {
    switch(i) {
    case 0:
      return lowleftback;
    case 1:
      return CTYPE(uprightfront(0), lowleftback(1), lowleftback(2));
    case 2:
      return CTYPE(uprightfront(0), uprightfront(1), lowleftback(2));
    case 3:
      return CTYPE(lowleftback(0), uprightfront(1), lowleftback(2));
		case 4:
      return uprightfront;
    case 5:
      return CTYPE(lowleftback(0), uprightfront(1), uprightfront(2));
		case 6:
			return CTYPE(lowleftback(0), lowleftback(1), uprightfront(2));
		case 7:
			return CTYPE(uprightfront(0), lowleftback(1), uprightfront(2));
    };
    throw ErrBadIndex(i, __FILE__, __LINE__);
  }
  // 
  void restrict(const CRectangularPrism_<VTYPE, CTYPE> &limits) {
    if(limits.xmin() > lowleftback(0))
      lowleftback(0) = min(uprightfront(0), limits.xmin());
    if(limits.xmax() < uprightfront(0))
      uprightfront(0) = max(lowleftback(0), limits.xmax());
    if(limits.ymin() > lowleftback(1))
      lowleftback(1) = min(uprightfront(1), limits.ymin());
    if(limits.ymax() < uprightfront(1))
      uprightfront(1) = max(lowleftback(1), limits.ymax());
    if(limits.zmin() > lowleftback(2))
      lowleftback(2) = min(uprightfront(2), limits.zmin());
    if(limits.zmax() < uprightfront(2))
      uprightfront(2) = max(lowleftback(2), limits.zmax());
  }

  virtual std::ostream &print(std::ostream&) const = 0;

};

template <class VTYPE, class CTYPE>
CRectangularPrism_<VTYPE, CTYPE>::CRectangularPrism_(const CTYPE &a, const CTYPE &b) {
  if(a(0) < b(0)) {
    uprightfront(0) = b(0);
    lowleftback(0) = a(0);
  }
  else {
    uprightfront(0) = a(0);
    lowleftback(0) = b(0);
  }
  if(a(1) < b(1)) {
    uprightfront(1) = b(1);
    lowleftback(1) = a(1);
  }
  else {
    uprightfront(1) = a(1);
    lowleftback(1) = b(1);
  }
  if(a(2) < b(2)) {
    uprightfront(2) = b(2);
    lowleftback(2) = a(2);
  }
  else {
    uprightfront(2) = a(2);
    lowleftback(2) = b(2);
  }
}

class CRectangularPrism: public CRectangularPrism_<double, Coord> {
public:
  CRectangularPrism(const Coord &a, const Coord &b)
    : CRectangularPrism_<double, Coord>(a,b)
  {}
  friend std::ostream& operator<<(std::ostream &os, const CRectangularPrism &rect) {
    os << "CRectangularPrism(" << rect.lowleftback << ", " << rect.uprightfront << ")";
    return os;
  }
  virtual std::ostream &print(std::ostream &os) const {
    return os << *this;
  }
  void expand(double howmuch) {
    double mid = 0.5*(lowleftback(0) + uprightfront(0));
    double size = 0.5*(uprightfront(0) - lowleftback(0))*(1 + howmuch);
    lowleftback(0) = mid - size;
    uprightfront(0) = mid + size;
    mid = 0.5*(lowleftback(1) + uprightfront(1));
    size = 0.5*(uprightfront(1) - lowleftback(1))*(1 + howmuch);
    lowleftback(1) = mid - size;
    uprightfront(1) = mid + size;
    mid = 0.5*(lowleftback(2) + uprightfront(2));
    size = 0.5*(uprightfront(2) - lowleftback(2))*(1 + howmuch);
    lowleftback(2) = mid - size;
    uprightfront(2) = mid + size;
  }
};

class ICRectangularPrism : public CRectangularPrism_<int, ICoord> {
public:
  ICRectangularPrism() {}
  ICRectangularPrism(const ICoord &a, const ICoord &b)
    : CRectangularPrism_<int, ICoord>(a,b)
  {}
  friend std::ostream& operator<<(std::ostream &os, const ICRectangularPrism &rect) {
    os << "ICRectangularPrism(" << rect.lowleftback << ", " << rect.uprightfront << ")";
    return os;
  }
  virtual std::ostream &print(std::ostream &os) const {
    return os << *this;
  }    
};

#endif //DIM == 3


#undef min
#undef max

#endif
