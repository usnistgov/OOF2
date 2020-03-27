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
  {
    segments.reserve(n);
  }

  const std::string &CanvasSegments::classname() const {
    static const std::string name("CanvasSegments");
    return name;
  }

  void CanvasSegments::addSegment(double x0, double y0, double x1, double y1) {
    segments.emplace_back(x0, y0, x1, y1);
    bbox0.swallow(Coord(x0, y0));
    bbox0.swallow(Coord(x1, y1));
    bbox = bbox0;
    modified();
  }

  void CanvasSegments::setLineWidth(double w) {
    CanvasShape::setLineWidth(w);
    modified();
  }

  const Rectangle &CanvasSegments::findBoundingBox(double ppu) {
    double lw = lineWidthInPixels ? lineWidth/ppu : lineWidth;
    bbox = bbox0;
    bbox.expand(0.5*lw);
    return bbox;
  }

  void CanvasSegments::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
// #ifdef DEBUG
//     {
//       double xmin, ymin, xmax, ymax;
//       ctxt->get_clip_extents(xmin, ymin, xmax, ymax);
//       Rectangle clip_extents(xmin, ymin, xmax, ymax);
//       std::cerr << "CanvasSegments::drawItem: clip_extents=" << clip_extents
// 		<< std::endl;
//       for(const Segment & segment : segments) {
// 	if(!clip_extents.contains(segment.p0) ||
// 	   !clip_extents.contains(segment.p1))
// 	  {
// 	    std::cerr << "   Segment " << segment
// 		      << " is not inside clip extents" << std::endl;
// 	  }
//       }
//     }
// #endif // DEBUG
    
    ctxt->set_line_width(lineWidthInUserUnits(ctxt));
    ctxt->set_line_cap(lineCap);
    lineColor.set(ctxt);
    for(const Segment &segment : segments) {
      ctxt->move_to(segment.p0.x, segment.p0.y);
      ctxt->line_to(segment.p1.x, segment.p1.y);
    }
    ctxt->stroke();

// #ifdef DEBUG
//     {
//       static int count = 0;
//       std::string fname = "segments_" + to_string(count++) + ".png";
//       ctxt->get_target()->write_to_png(fname);
//       std::cerr << "CanvasSegments::drawItem: wrote " << fname << std::endl;
//     }
// #endif // DEBUG
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
