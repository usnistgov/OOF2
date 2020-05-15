// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "utility.h"
#include <string.h>
#include <assert.h>

namespace OOFCanvas {

  Coord Coord::operator*(double x) const {
    Coord result(*this);
    result *= x;
    return result;
  }

  Coord Coord::operator/(double x) const {
    Coord result(*this);
    result /= x;
    return result;
  }

  Coord Coord::operator+(const Coord &other) const {
    Coord result(*this);
    result += other;
    return result;
  }

  Coord Coord::operator-(const Coord &other) const {
    Coord result(*this);
    result -= other;
    return result;
  }

  Coord Coord::transform(const Cairo::Matrix &mat) const {
    Coord result(*this);
    mat.transform_point(result.x, result.y);
    return result;
  }

  Coord Coord::user_to_device(Cairo::RefPtr<Cairo::Context> ctxt) const {
    Coord result(*this);
    ctxt->user_to_device(result.x, result.y);
    return result;
  }

  Coord Coord::device_to_user(Cairo::RefPtr<Cairo::Context> ctxt) const {
    Coord result(*this);
    ctxt->device_to_user(result.x, result.y);
    return result;
  }
  
  double cross(const Coord &a, const Coord &b) {
    return a.x*b.y - a.y*b.x;
  }

  bool Coord::operator==(const Coord &other) const {
    return x == other.x && y == other.y;
  }

  bool Coord::operator!=(const Coord &other) const {
    return x != other.x || y != other.y;
  }

  std::ostream &operator<<(std::ostream &os, const Coord &p) {
    return os << "(" << p.x << ", " << p.y << ")";
  }
  
  std::ostream &operator<<(std::ostream &os, const ICoord &p) {
    return os << "(" << p.x << ", " << p.y << ")";
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  Coord ICoord::operator*(double a) const {
    return Coord(x*a, y*a);
  }
  
  Coord ICoord::operator/(double a) const {
    return Coord(x/a, y/a);
  }

  ICoord ICoord::operator+(const ICoord &other) const {
    ICoord result(*this);
    result += other;
    return result;
  }

  ICoord ICoord::operator-(const ICoord &other) const {
    ICoord result(*this);
    result -= other;
    return result;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
  
  Rectangle::Rectangle()
    : initialized_(false)
  {}

  Rectangle::Rectangle(double x0, double y0, double x1, double y1) {
    setup(x0, y0, x1, y1);
  }
  
  Rectangle::Rectangle(const Coord &a, const Coord &b) {
    setup(a.x, a.y, b.x, b.y);
  }

  Rectangle::Rectangle(const PangoRectangle &prect) {
    setup(prect.x, prect.y, prect.x+prect.width, prect.y+prect.height);
  }

  Rectangle::Rectangle(const Rectangle &other)
    : pmin(other.pmin),
      pmax(other.pmax),
      initialized_(other.initialized_)
  {}

  void  Rectangle::setup(double x0, double y0, double x1, double y1) {
    if(x0 < x1) {
      pmin.x = x0;
      pmax.x = x1;
    }
    else {
      pmin.x = x1;
      pmax.x = x0;
    }
    if(y0 < y1) {
      pmin.y = y0;
      pmax.y = y1;
    }
    else {
      pmin.y = y1;
      pmax.y = y0;
    }
    initialized_ = true;
  }

  void Rectangle::swallow(const Coord &p) {
    if(initialized_) {
      if(p.x < pmin.x)
	pmin.x = p.x;
      else if(p.x > pmax.x)
	pmax.x = p.x;
      if(p.y < pmin.y)
	pmin.y = p.y;
      else if(p.y > pmax.y)
	pmax.y = p.y;
    }
    else {
      pmin = p;
      pmax = p;
      initialized_ = true;
    }
  }

  void Rectangle::expand(double delta) {
    // Grow by delta in each direction
    if(initialized_) {
      pmin.x -= delta;
      pmin.y -= delta;
      pmax.x += delta;
      pmax.y += delta;
    }
  }

  void Rectangle::shift(const Coord &delta) {
    pmin += delta;
    pmax += delta;
  }

  void Rectangle::scale(double xfactor, double yfactor) {
    pmin.x *= xfactor;
    pmax.x *= xfactor;
    pmin.y *= yfactor;
    pmax.y *= yfactor;
  }

  Coord Rectangle::center() const {
    return 0.5*(pmin + pmax);
  }

  Rectangle Rectangle::user_to_device(Cairo::RefPtr<Cairo::Context> ctxt) const
  {
    return Rectangle(pmin.user_to_device(ctxt), pmax.user_to_device(ctxt));
  }
  
  Rectangle Rectangle::device_to_user(Cairo::RefPtr<Cairo::Context> ctxt) const
  {
    return Rectangle(pmin.device_to_user(ctxt), pmax.device_to_user(ctxt));
  }
  
  const Rectangle &Rectangle::operator=(const Rectangle &other) {
    initialized_ = other.initialized_;
    pmin = other.pmin;
    pmax = other.pmax;
    return *this;
  }

  bool Rectangle::contains(const Coord &pt) const {
    return initialized_ && (pt.x >= pmin.x && pt.x <= pmax.x &&
			    pt.y >= pmin.y && pt.y <= pmax.y);
  }

  bool Rectangle::operator==(const Rectangle &other) const {
    assert(initialized_ && other.initialized_);
    return pmin == other.pmin && pmax == other.pmax;
  }

  bool Rectangle::operator!=(const Rectangle &other) const {
    assert(initialized_ && other.initialized_);
    return pmin != other.pmin || pmax != other.pmax;
  }
   

  std::ostream &operator<<(std::ostream &os, const Rectangle &rect) {
    os << "Rectangle(";
    if(rect.initialized()) 
      os << rect.pmin << ", " << rect.pmax << ")";
    else
      os << "<uninitialized>";
    os << ")";
    return os;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // Given a point, compute the normal distance squared from it to the
  // segment and the position 0<alpha<1 along the segment of the
  // normal to the point.  That is, the normal from the point to the
  // segment intersects the segment at
  // (1-alpha)*seg.p0 + alpha*seg.p1.

  void Segment::projection(const Coord &pt, double &alpha, double &distance2)
    const
  {
    Coord pp = p1 - p0;
    alpha = ((pt - p0) * pp)/pp.norm2();
    distance2 = ((p0 + alpha*pp) - pt).norm2();
  }

  double Segment::angle() const {
    Coord delta = p1 - p0;
    return atan2(delta.y, delta.x);
  }

  Coord Segment::interpolate(double alpha) const {
    return p0 + alpha*(p1 - p0);
  }

  std::ostream &operator<<(std::ostream &os, const Segment &seg) {
    os << "[" << seg.p0 << ", " << seg.p1 << "]";
    return os;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  TMatrix::TMatrix(double a0, double a1, double a2, double a3) {
    a[0] = a0;
    a[1] = a1;
    a[2] = a2;
    a[3] = a3;
  }
  
  TMatrix::TMatrix(const TMatrix &other) {
    memcpy(a, other.a, 4*sizeof(double));
  }
  
  TMatrix &TMatrix::operator*=(const TMatrix &b) {
    double tmp[4];
    memcpy(tmp, a, 4*sizeof(double));
    a[0] = tmp[0]*b.a[0] + tmp[1]*b.a[2]; // 00
    a[1] = tmp[0]*b.a[1] + tmp[1]*b.a[3]; // 01
    a[2] = tmp[2]*b.a[0] + tmp[3]*b.a[2]; // 10
    a[3] = tmp[2]*b.a[2] + tmp[3]*b.a[3]; // 11
    return *this;
  }

  TMatrix &TMatrix::operator*=(double x) {
    a[0] *= x;
    a[1] *= x;
    a[2] *= x;
    a[3] *= x;
    return *this;
  }

  TMatrix TMatrix::operator*(const TMatrix &b) const {
    TMatrix result(*this);
    result *= b;
    return result;
  }

  TMatrix TMatrix::operator*(double x) const {
    TMatrix result(*this);
    result *= x;
    return result;
  }

  TMatrix operator*(double x, const TMatrix &a) {
    return a*x;
  }

  Coord operator*(const TMatrix &m, const Coord &x) {
    return Coord(m.a[0]*x.x + m.a[1]*x.y,
		 m.a[2]*x.x + m.a[3]*x.y);
  }

  Coord axpy(const TMatrix &a, const Coord &x, const Coord &y) {
    return Coord(a.a[0]*x.x + a.a[1]*x.y + y.x,
		 a.a[2]*x.x + a.a[3]*x.y + y.y);
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  void Color::set(Cairo::RefPtr<Cairo::Context> ctxt) const {
    if(alpha == 1.0)
      ctxt->set_source_rgb(red, green, blue);
    else
      ctxt->set_source_rgba(red, green, blue, alpha);
  }

  Color Color::opacity(double newalpha) const {
    return Color(red, green, blue, newalpha);
  }

  const Color black(0.0, 0.0, 0.0);
  const Color gray(0.5, 0.5, 0.5);
  const Color white(1.0, 1.0, 1.0);
  const Color red(1.0, 0.0, 0.0);
  const Color green(0.0, 1.0, 0.0);
  const Color blue(0.0, 0.0, 1.0);
  const Color yellow(1.0, 1.0, 0.0);
  const Color cyan(0.0, 1.0, 1.0);
  const Color magenta(1.0, 0.0, 1.0);

  std::ostream &operator<<(std::ostream &os, const Cairo::Matrix &trans) {
    os << "["
       << trans.xx << ", " << trans.xy << ", "
       << trans.yx << ", " << trans.yy << "; "
       << trans.x0 << ", " << trans.y0 << "]";
    return os;
  }

  bool operator==(const Cairo::Matrix &a, const Cairo::Matrix &b) {
    return (a.xx == b.xx && a.xy == b.xy && a.yx == b.yx && a.yy == b.yy &&
	    a.x0 == b.x0 && a.y0 == b.y0);
  }

  std::ostream &operator<<(std::ostream &os, const std::vector<double> &vec) {
    os << "[";
    bool first = true;
    for(double x : vec) {
      if(!first) os << ", ";
      os << x;
      first = false;
    }
    os << "]";
    return os;
  }

};				// namespace OOFCanvas
		   

