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

  void CanvasSegments::setLineWidth(double w) {
    CanvasShape::setLineWidth(w);
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
    ctxt->set_line_width(lineWidthInUserUnits(ctxt));
    ctxt->set_line_cap(lineCap);
    lineColor.set(ctxt);
    for(const Segment &segment : segments) {
      ctxt->move_to(segment.p0.x, segment.p0.y);
      ctxt->line_to(segment.p1.x, segment.p1.y);
    }
    ctxt->stroke();
  }

  bool CanvasSegments::containsPoint(const OffScreenCanvas *canvas,
				     const Coord &pt) const
  {
    double lw = lineWidthInPixels ?
      lineWidth/canvas->getPixelsPerUnit() : lineWidth;
    double d2max = 0.25*lw*lw;
    for(const Segment &seg : segments) {
      double alpha = 0;		// position along segment
      double distance2 = 0; // distance squared from pt to segment along normal
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
};
