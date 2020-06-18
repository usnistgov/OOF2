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
#include "canvassegments.h"
#include <iostream>

namespace OOFCanvas {

  // Use this constructor if you know how many segments you'll be
  // drawing.
  CanvasSegments::CanvasSegments(int n)
    : CanvasShape(Rectangle())
  {
    segments.reserve(n);
  }

  const std::string &CanvasSegments::classname() const {
    static const std::string name("CanvasSegments");
    return name;
  }

  void CanvasSegments::addSegment(double x0, double y0, double x1, double y1) {
    addSegment(Coord(x0, y0), Coord(x1, y1));
  }

  void CanvasSegments::addSegment(const Coord &p0, const Coord &p1) {
    segments.emplace_back(p0, p1);
    bbox.swallow(p0);
    bbox.swallow(p1);
    modified();
  }

  void CanvasSegments::pixelExtents(double &left, double &right,
				    double &up, double &down)
    const
  {
    double halfw = 0.5*lineWidth;
    left = halfw;
    right = halfw;
    up = halfw;
    down = halfw;
  }

  void CanvasSegments::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    for(const Segment &segment : segments) {
      ctxt->move_to(segment.p0.x, segment.p0.y);
      ctxt->line_to(segment.p1.x, segment.p1.y);
    }
    stroke(ctxt);
  }

  bool CanvasSegments::containsPoint(const OffScreenCanvas *canvas,
				     const Coord &pt)
    const
  {
    double lw = lineWidthInPixels ?
      lineWidth/canvas->getPixelsPerUnit() : lineWidth;
    double d2max = 0.25*lw*lw;
    for(const Segment &seg : segments) {
      double alpha = 0;	    // position along segment
      double distance2 = 0; // normal distance squared from pt to segment
      seg.projection(pt, alpha, distance2);
      if(alpha >= 0.0 && alpha <= 1.0 && distance2 < d2max)
	return true;
    }
    return false;
  }

  std::string CanvasSegments::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasSegments &segs) {
    os << "CanvasSegments(";
    if(segs.size() > 0) {
      os << segs.segments[0];
      for(int i=1; i<segs.size(); i++)
	os << ", " << segs.segments[i];
    }
    os << ")";
    return os;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  CanvasCurve::CanvasCurve(int n)
    : CanvasShape(Rectangle())
  {
    points.reserve(n);
  }

  CanvasCurve::CanvasCurve(const std::vector<Coord> &pts)
    : CanvasShape(Rectangle())
  {
    points.reserve(pts.size());
    for(const Coord &pt : pts) {
      points.push_back(pt);
      bbox.swallow(pt);
    }
  }

  const std::string &CanvasCurve::classname() const {
    static const std::string name("CanvasCurve");
    return name;
  }

  void CanvasCurve::addPoint(double x, double y) {
    points.emplace_back(x, y);
    bbox.swallow(points.back());
    modified();
  }

  void CanvasCurve::addPoint(const Coord &pt) {
    points.push_back(pt);
    bbox.swallow(pt);
  }

  void CanvasCurve::addPoints(const std::vector<Coord> &pts) {
    points.insert(points.end(), pts.begin(), pts.end());
    for(const Coord &pt : pts)
      bbox.swallow(pt);
  }

  void CanvasCurve::pixelExtents(double &left, double &right,
				 double &up, double &down)
    const
  {
    double halfw = 0.5*lineWidth;
    left = halfw;
    right = halfw;
    up = halfw;
    down = halfw;
  }

  void CanvasCurve::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    if(points.size() > 1) {
      ctxt->move_to(points[0].x, points[0].y);
      for(unsigned int i=1; i<points.size(); i++)
	ctxt->line_to(points[i].x, points[i].y);
      stroke(ctxt);
    }
  }

  bool CanvasCurve::containsPoint(const OffScreenCanvas *canvas,
				  const Coord &pt)
    const
  {
    if(points.size() < 2)
      return false;
    double lw = lineWidthInPixels ?
      lineWidth/canvas->getPixelsPerUnit() : lineWidth;
    double d2max = 0.25*lw*lw;
    for(unsigned int i=1; i<points.size(); i++) {
      Segment seg(points[i-1], points[i]);
      double alpha = 0;	 // position along segment;
      double distance2;	 // normal distance squared from pt to segment
      seg.projection(pt, alpha, distance2);
      if(alpha >= 0.0 && alpha <= 1.0 && distance2 < d2max)
	return true;
    }
    return false;
  }

  std::string CanvasCurve::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasCurve &curve) {
    os << "CanvasCurve(";
    if(curve.size() > 0) {
      os << curve.points[0];
      for(int i=1; i<curve.size(); i++)
	os << ", " << curve.points[i];
    }
    os << ")";
    return os;
  }

};				// namespace OOFCanvas
