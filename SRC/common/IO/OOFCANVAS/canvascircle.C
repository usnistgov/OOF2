// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "canvas.h"
#include "canvascircle.h"
#include "utility.h"
#include <math.h>

namespace OOFCanvas {

  CanvasCircle::CanvasCircle(const Coord &c, double r)
    : CanvasFillableShape(Rectangle(c-Coord(r,r), c+Coord(r,r))),
      center(c),
      radius(r)
  {}

  CanvasCircle::CanvasCircle(const Coord *c, double r)
    : CanvasFillableShape(Rectangle(*c-Coord(r,r), *c+Coord(r,r))),
      center(*c),
      radius(r)
  {}

  const std::string &CanvasCircle::classname() const {
    static const std::string name("CanvasCircle");
    return name;
  }

  void CanvasCircle::setLineWidth(double w) {
    CanvasShape::setLineWidth(w);
  }

  std::string CanvasCircle::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasCircle &circ) {
    os << "CanvasCircle(" << circ.center << ", " << circ.radius << ")";
    return os;
  }

  bool CanvasCircle::containsPoint(const OffScreenCanvas*, const Coord &pt)
    const
  {
    double d2 = (pt - center).norm2();
    if(fill) {
      return d2 <= radius*radius;
    }
    if(line) {
      double rInner = radius - lineWidth;
      return d2 >= rInner*rInner && d2 <= radius*radius;
    }
    return false;
  }

  void CanvasCircle::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    ctxt->begin_new_sub_path();
    if(fill) {
      ctxt->arc(center.x, center.y, radius, 0, 2*M_PI);
      fillColor.set(ctxt);
      ctxt->fill();
    }
    if(line) {
      double lw = lineWidthInUserUnits(ctxt);
      ctxt->arc(center.x, center.y, radius-0.5*lw, 0, 2*M_PI);
      stroke(ctxt);
    }
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  static Rectangle ellipseBBox(double cx, double cy, double r0, double r1,
			       double angle)
  {
    double ang = M_PI*angle/180.;
    double c = cos(ang);
    double s = sin(ang);
    // Half-widths of the bounding box
    double dx = sqrt(c*c*r0*r0 + s*s*r1*r1);
    double dy = sqrt(c*c*r1*r1 + s*s*r0*r0);
    return Rectangle(cx-dx, cy-dy, cx+dx, cy+dy);
  }

  CanvasEllipse::CanvasEllipse(const Coord &c, const Coord &r,
			       double angle_degrees)
    : CanvasFillableShape(ellipseBBox(c.x, c.y, r.x, r.y, angle_degrees)),
      center(c),
      r0(r.x), r1(r.y),
      angle(M_PI*angle_degrees/180.)
  {}

  CanvasEllipse::CanvasEllipse(const Coord *c, const Coord *r,
			       double angle_degrees)
    : CanvasFillableShape(ellipseBBox(c->x, c->y, r->x, r->y, angle_degrees)),
      center(*c),
      r0(r->x), r1(r->y),
      angle(M_PI*angle_degrees/180.)
  {}

  const std::string &CanvasEllipse::classname() const {
    static const std::string name("CanvasEllipse");
    return name;
  }
  
  void CanvasEllipse::setLineWidth(double w) {
    CanvasShape::setLineWidth(w);
  }

  std::string CanvasEllipse::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasEllipse &ellipse) {
    os << "CanvasEllipse(center=" << ellipse.center << ", r0=" << ellipse.r0
       << ", r1=" << ellipse.r1 << ", angle=" << ellipse.angle*180./M_PI << ")";
    return os;
  }

  bool CanvasEllipse::containsPoint(const OffScreenCanvas*, const Coord &pt)
    const
  {
    Coord p = pt - center;
    double c = cos(angle);
    double s = sin(angle);
    // (x/a)^2 and (y/b)^2 in the rotated coordinate system
    double px = ( p.x*c + p.y*s)/r0;
    double py = (-p.x*s + p.y*c)/r1;
    if(fill) {
      // If filled, we just have to know if the point is inside the
      // ellipse we just calculated.
      return px*px + py*py <= 1.0;
    }
    if(line) {
      // A point is on the unfilled ellipse only if it's on the line.
      // We've already computed the ellipse on the outer edge of the
      // line. 
      if(px*px + py*py > 1.0) // Is the point outside the outer edge?
	return false;
      // Compute the ellipse on the inner edge of the line.
      double rr0 = r0 - lineWidth;
      double rr1 = r1 - lineWidth;
      px = ( p.x*c + p.y*s)/rr0;
      py = (-p.x*s + p.y*c)/rr1;
      return px*px + py*py >= 1.0; // point is outside the inner edge
    }
    return false;
  }

  void CanvasEllipse::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    // Operations are defined in the reverse of the order in which
    // they're applied.  We'll be drawing a circle with radius 1, then
    // scaling it so that it's an ellipse with radii r0 and r1, then
    // rotating it, then translating it to the desired center point.

    // TODO? We could draw a straight line if one of the radii is
    // zero.  We can't ignore the situation and try to draw the
    // ellipse anyway, because Cairo::Context::scale() requires its
    // arguments to be nonzero.
    if(r0 == 0.0 || r1 == 0.0)
      return;

    // The line width has to be computed before rotating because
    // lineWidthInUserUnits uses only the x component of a value
    // returned by Context::device_to_user_distance.
    double lw = lineWidthInUserUnits(ctxt);
    
    ctxt->translate(center.x, center.y);
    ctxt->rotate(angle);

    if(fill) {
      // Do an extra save and restore here so that we don't scale
      // twice if we're both filling and drawing the perimeter.
      ctxt->save();
      ctxt->scale(r0, r1);
      ctxt->begin_new_sub_path();
      ctxt->arc(0.0, 0.0, 1.0, 0.0, 2*M_PI);
      fillColor.set(ctxt);
      ctxt->fill();
      ctxt->restore();
    }
    if(line) {
      // Save and restore the context before stroking the line, so
      // that the line thickness isn't distorted.
      ctxt->save();
      ctxt->scale(r0, r1);
      ctxt->begin_new_sub_path();
      double rr = r0 > r1 ? r0 : r1;
      ctxt->arc(0.0, 0.0, 1.0-0.5*lw/rr, 0.0, 2*M_PI);
      ctxt->restore();
      stroke(ctxt);
    }
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // A CanvasDot is a circle that has a fixed size in device units.
  // Its "bare" bounding box is therefore just a point.

  CanvasDot::CanvasDot(const Coord &c, double r)
    : CanvasFillableShape(Rectangle(c,c)),
      center(c),
      radius(r)
  {}

  CanvasDot::CanvasDot(const Coord *c, double r)
    : CanvasFillableShape(Rectangle(*c, *c)),
      center(*c),
      radius(r)
  {}

  const std::string &CanvasDot::classname() const {
    static const std::string name("CanvasDot");
    return name;
  }

  std::string CanvasDot::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasDot &cdot) {
    os << "CanvasDot(" << cdot.center << ", " << cdot.radius << ")";
    return os;
  }

  bool CanvasDot::containsPoint(const OffScreenCanvas *canvas, const Coord &pt)
    const
  {
    double d2 = (pt - center).norm2();
    double r = canvas->pixel2user(radius);
    double l = line ? canvas->pixel2user(lineWidth) : 0.0;
    if(fill) {
      return d2 <= r*r;
    }
    if(line) {
      double rInner = r - l;
      return d2 >= rInner*rInner && d2 <= r*r;
    }
    return false;
  }

  void CanvasDot::pixelExtents(double &left, double &right,
			       double &up, double &down)
    const
  {
    left = radius;
    right = radius;
    up = radius;
    down = radius;
  }

  void CanvasDot::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    double dummy = 0;
    double r = radius;
    ctxt->device_to_user_distance(r, dummy);
    if(fill) {
      ctxt->begin_new_sub_path();
      ctxt->arc(center.x, center.y, r, 0, 2*M_PI);
      fillColor.set(ctxt);
      ctxt->fill();
    }
    if(line) {
      // A CanvasDot's lineWidth is always in device units.
      double lw = lineWidth;
      ctxt->device_to_user_distance(lw, dummy);
      ctxt->begin_new_sub_path();
      ctxt->arc(center.x, center.y, r-0.5*lw, 0, 2*M_PI);
      stroke(ctxt);
    }
  }

};				// namespace OOFCanvas
