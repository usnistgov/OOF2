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
#include "canvassegment.h"
#include <iostream>
#include <math.h>

namespace OOFCanvas {

  CanvasSegment::CanvasSegment(double x0, double y0, double x1, double y1)
    : segment(x0, y0, x1, y1),
      bbox0(x0, y0, x1, y1)
  {
  }

  CanvasSegment::CanvasSegment(const Coord &p0, const Coord &p1)
    : segment(p0, p1),
      bbox0(p0, p1)
  {
  }

  const std::string &CanvasSegment::classname() const {
    static const std::string name("CanvasSegment");
    return name;
  }

  void CanvasSegment::setLineWidth(double w) {
    CanvasShape::setLineWidth(w);
    modified();
  }

  const Rectangle &CanvasSegment::findBoundingBox(double ppu) {
    double lw = lineWidthInPixels ? lineWidth/ppu : lineWidth;
    bbox = bbox0;
    bbox.expand(0.5*lw);
    return bbox;
  }

  void CanvasSegment::setDashes(const std::vector<double> &d) {
    dashes = d;
  }

  void CanvasSegment::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    ctxt->set_line_width(lineWidthInUserUnits(ctxt));
    ctxt->set_line_cap(lineCap);
    lineColor.set(ctxt);
    if(!dashes.empty())
      ctxt->set_dash(dashes, 0);
    ctxt->move_to(segment.p0.x, segment.p0.y);
    ctxt->line_to(segment.p1.x, segment.p1.y);
    ctxt->stroke();
  }

  bool CanvasSegment::containsPoint(const OffScreenCanvas *canvas,
				    const Coord &pt) const
  {
    double alpha = 0;
    double distance2 = 0; // distance squared from pt to segment along normal
    double lw = lineWidthInPixels ?
      lineWidth/canvas->getPixelsPerUnit() : lineWidth;
    segment.projection(pt, alpha, distance2);
    return (alpha >= 0.0 && alpha <= 1.0 && distance2 < 0.25*lw*lw);
  }

  std::string CanvasSegment::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasSegment &seg) {
    os << "CanvasSegment(" << seg.segment << ")";
    return os;
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // CanvasArrowheads are meant to be used to decorate CanvasSegments.
  // They're not usable on their own.

  // The position argument passed to the constructor determines where
  // along the segment the tip of the arrow will appear.  A value of 0
  // puts the tip of the arrow on the first point of the segment.  A
  // value of 1 puts it on the second point.  Intermediate values put
  // it somewhere in the middle.

  // The size of the arrowhead is determined by the width and length
  // passed to the constructor.  If setPixelSize() is called, the size
  // is taken to be in pixel units.  Otherwise it's in user units.

  // If setReversed() is called, the arrow will point in the direction
  // of the CanvasSegment's first point.  Otherwise it points toward
  // the second point.

  // Oddities that might not be worth fixing:
  // * If you use position=0
  //   and don't call setReversed(), or position=1 and do call
  //   setReversed(), the tail of the arrow will hang off of the end of
  //   the segment.  This may not be what you want.
  // * The end of the segment isn't trimmed to fit inside the
  //   arrowhead.  If you have a thick line and a sharp arrowhead, it
  //   might look funny.  This might be fixed by creating an arrowhead
  //   shaped mask for the segment, if the mask could be applied only
  //   to the ends of the segment somehow.
  

  CanvasArrowhead::CanvasArrowhead(const CanvasSegment *seg,
				   double pos, double w, double l)
    : segment(seg),
      width(w),	       // width of arrowhead, perpendicular to segment
      length(l),       // length of arrowhead along segment
      position(pos),   // relative position along segment, in the range 0->1.
      pixelScaling(false),
      reversed(false)	    
  {}

  const std::string &CanvasArrowhead::classname() const {
    static const std::string name("CanvasArrowhead");
    return name;
  }

  Coord CanvasArrowhead::location() const {
    return segment->segment.p0 +
      position*(segment->segment.p1 - segment->segment.p0);
  }

  void CanvasArrowhead::drawItem(Cairo::RefPtr<Cairo::Context> ctxt) const {
    Coord loc = location();
    ctxt->translate(loc.x, loc.y);

    // If converting to pixel coordinates, get the size before rotating
    double l = length;
    double w = width;
    if(pixelScaling)
      ctxt->device_to_user_distance(l, w);

    if(reversed)
      l *= -1;
    
    ctxt->rotate(segment->segment.angle());
    ctxt->move_to(0., 0.);
    ctxt->line_to(-l, w/2);
    ctxt->line_to(-l, -w/2);
    ctxt->close_path();
    segment->getLineColor().set(ctxt);
    ctxt->fill();
  }

  Rectangle CanvasArrowhead::findBoundingBox_(double ppu) const {
    // The easiest way to compute the bounding box is to use a Context
    // to transform the coordinates, as in drawItem.  But we don't
    // have a Context when findBoundingBox is called, so create a
    // dummy one.  See CanvasText for a similar treatment.

    auto surface = Cairo::RefPtr<Cairo::ImageSurface>(
		      Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32, 1, 1));
    cairo_t *ct = cairo_create(surface->cobj());
    auto ctxt = Cairo::RefPtr<Cairo::Context>(new Cairo::Context(ct, true));
    ctxt->save();
    ctxt->rotate(segment->segment.angle());
    // Find bounding box in the arrow's coordinates
    double l = reversed ? length : -length;
    double w = width/2.;
    std::vector<Coord> corners({{l, -w}, {0, -w}, {0, w}, {l, w}});
    // convert to device space on the dummy device
    for(Coord &corner : corners)
      ctxt->user_to_device(corner.x, corner.y);
    // convert from device space to the real user coordinates
    ctxt->restore();
    for(Coord &corner : corners)
      ctxt->device_to_user(corner.x, corner.y);
    Rectangle bb = Rectangle(corners[0], corners[1]);
    bb.swallow(corners[2]);
    bb.swallow(corners[3]);
    if(pixelScaling)
      bb.scale(1./ppu, 1./ppu);
    bb.shift(location());
    return bb;
  }

  const Rectangle &CanvasArrowhead::findBoundingBox(double ppu) {
    bbox = findBoundingBox_(ppu);
    return bbox;
  }

  void CanvasArrowhead::pixelExtents(double &left, double &right,
				     double &up, double &down)
    const
  {
    // When ppu=1, the user-space and device-space bounding boxes are
    // the same.
    Rectangle bb(findBoundingBox_(1.0));
    Coord loc(location());
    left = loc.x - bb.xmin();
    right = bb.xmax() - loc.x;
    up = bb.ymax() - loc.y;
    down = loc.y - bb.ymin();
  }

  bool CanvasArrowhead::containsPoint(const OffScreenCanvas*, const Coord &pt)
    const
  {
    return false;
  }

  std::string CanvasArrowhead::print() const {
    return to_string(*this);
  }

  std::ostream &operator<<(std::ostream &os, const CanvasArrowhead &arr) {
    os << "CanvasArrowhead(" << arr.segment->segment
       << ", " << arr.position << ", " << arr.width
       << ", " << arr.length << ")";
    return os;
  }
  
};
