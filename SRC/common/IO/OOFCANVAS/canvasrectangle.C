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
#include "canvasrectangle.h"
#include <iostream>

namespace OOFCanvas {
  
  CanvasRectangle::CanvasRectangle(double xmin, double ymin,
				     double xmax, double ymax)
    : xmin(xmin), ymin(ymin),
      xmax(xmax), ymax(ymax),
      bbox0(xmin, ymin, xmax, ymax)
  {
    bbox = bbox0;
  }

  CanvasRectangle::CanvasRectangle(const Coord &p0, const Coord &p1)
    : xmin(p0.x), ymin(p0.y),
      xmax(p1.x), ymax(p1.y),
      bbox0(p0, p1)
  {
    bbox = bbox0;
  }

  const std::string &CanvasRectangle::classname() const {
    static const std::string name("CanvasRectangle");
    return name;
  }

  void CanvasRectangle::setLineWidth(double w) {
    CanvasFillableShape::setLineWidth(w);
  }

  void CanvasRectangle::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    double w = lineWidthInUserUnits(ctxt);
    ctxt->set_line_width(w);
    double halfw = 0.5*w;
    ctxt->set_line_join(lineJoin);
    ctxt->move_to(xmin+halfw, ymin+halfw);
    ctxt->line_to(xmax-halfw, ymin+halfw);
    ctxt->line_to(xmax-halfw, ymax-halfw);
    ctxt->line_to(xmin+halfw, ymax-halfw);
    ctxt->close_path();

    fillAndStroke(ctxt);
  }

  bool CanvasRectangle::containsPoint(const OffScreenCanvas*, const Coord &pt)
    const
  {
    // We already know that the point is within the bounding box, so
    // if the rectangle is filled, the point is on it.
    return fill || (line && (pt.x - bbox.xmin() <= lineWidth ||
			     bbox.xmax() - pt.x <= lineWidth ||
			     pt.y - bbox.ymin() <= lineWidth ||
			     bbox.ymax() - pt.y <= lineWidth));
  }

  std::string CanvasRectangle::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasRectangle &rect) {
    os << "CanvasRectangle(" << Coord(rect.xmin, rect.ymin)
       << ", " << Coord(rect.xmax, rect.ymax) << ")";
    return os;
  }
};				// namespace OOFCanvas
