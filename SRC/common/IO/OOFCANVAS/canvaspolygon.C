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
#include "canvaspolygon.h"

namespace OOFCanvas {

  CanvasPolygon::CanvasPolygon(int n) {
    corners.reserve(n);
  }

  const std::string &CanvasPolygon::classname() const {
    static const std::string name("CanvasPolygon");
    return name;
  }

  void CanvasPolygon::addPoint(double x, double y) {
    corners.emplace_back(x, y);
    bbox0.swallow(corners.back());
    bbox = bbox0;
    if(lineWidth > 0)
      bbox.expand(0.5*lineWidth);
    modified();
  }

  void CanvasPolygon::setLineWidth(double w) {
    CanvasShape::setLineWidth(w);
    bbox = bbox0;
    bbox.expand(0.5*w);
    modified();
  }

  void CanvasPolygon::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    if(size() < 2)
      return;
    ctxt->set_line_width(lineWidth);
    ctxt->set_line_cap(lineCap);
    ctxt->set_line_join(lineJoin);
    lineColor.set(ctxt);
    auto iter = corners.begin();
    ctxt->move_to(iter->x, iter->y);
    while(++iter != corners.end()) {
      ctxt->line_to(iter->x, iter->y);
    }
    ctxt->close_path();

    fillAndStroke(ctxt);
  }

  int CanvasPolygon::windingNumber(const Coord &pt) const {
    // Compute the winding number of the polygon around a test point,
    // pt.  It's not necessary to check every segment, just the ones
    // that cross a line that passes through the test point. See
    // http://geomalgorithms.com/a03-_inclusion.html.
    int wn = 0;
    int n = corners.size();
    for(int i=0; i<n; i++) {	// loop over segments
      const Coord &next = corners[(i+1)%n];
      const Coord &prev = corners[i];
      if(prev.y <= pt.y) {
	if(pt.y < next.y) {
	  // An upward crossing of the line y=pt.y
	  if(cross(next-prev, pt-prev) > 0) {
	    // pt is to the left of the segment
	    ++wn;
	  }
	}
      }
      else {			// prev.y > pt.y
	if(next.y <= pt.y ) {
	  // A downward crossing of the line y=pt.y
	  if(cross(next-prev, pt-prev) < 0) {
	    // pt is to the right of the segment
	    --wn;
	  }
	}
      }
    } // end loop over segments
    return wn;
  }

  bool CanvasPolygon::containsPoint(const CanvasBase*, const Coord &pt) const {
    if(fill) {
      if(windingNumber(pt) != 0)
	return true;
      // If a thick perimeter is drawn, the click may be outside the
      // nominal polygon but still on the perimeter line, so we have
      // to do the line check even if the winding number check fails.
    }
    if(line) {
      int n = corners.size();
      double hlw2 = 0.25*lineWidth*lineWidth; // (half line width)^2
      for(int i=0; i<n; i++) {
	const Segment segment(corners[i], corners[(i+1)%n]);
	double alpha = 0;
	double distance2 = 0;
	segment.projection(pt, alpha, distance2);
	if(alpha >= 0.0 && alpha <= 1.0 && distance2 < hlw2)
	  return true;
      }
    }
    return false;
  }

  std::string CanvasPolygon::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasPolygon &poly) {
    os << "CanvasPolygon(";
    if(poly.size() > 0) {
      os << poly.corners[0];
      for(int i=1; i<poly.size(); i++)
	os << ", " << poly.corners[i];
    }
    os << ")";
    return os;
  }

}; // namespace OOFCanvas
