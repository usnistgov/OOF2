// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "canvasshape.h"

namespace OOFCanvas {

  void CanvasShape::setLineWidth(double w) {
    lineWidth = w;
    line = true;
    modified();
  }

  double CanvasShape::lineWidthInUserUnits(Cairo::RefPtr<Cairo::Context> ctxt)
    const
  {
    if(lineWidthInPixels) {
      double dx=1, dy=1;
      ctxt->device_to_user_distance(dx, dy);
      return lineWidth*dx;
    }
    return lineWidth;
  }

  void CanvasShape::setLineColor(const Color &color) {
    lineColor = color;
    line = true;
  }

  void CanvasFillableShape::setFillColor(const Color &color) {
    fillColor = color;
    fill = true;
  }

  void CanvasFillableShape::fillAndStroke(Cairo::RefPtr<Cairo::Context> ctxt)
    const
  {
    if(line && fill) {
      fillColor.set(ctxt);
      ctxt->fill_preserve();
      lineColor.set(ctxt);
      ctxt->stroke();
    }
    else if(line) {
      lineColor.set(ctxt);
      ctxt->stroke();
    }
    else if(fill) {
      fillColor.set(ctxt);
      ctxt->fill();
    }
  }

  // These are for use from python.  See comments in oofcanvas.swg.
  const Cairo::LineCap lineCapButt(Cairo::LineCap::LINE_CAP_BUTT);
  const Cairo::LineCap lineCapRound(Cairo::LineCap::LINE_CAP_ROUND);
  const Cairo::LineCap lineCapSquare(Cairo::LineCap::LINE_CAP_SQUARE);

  const Cairo::LineJoin lineJoinMiter(Cairo::LineJoin::LINE_JOIN_MITER);
  const Cairo::LineJoin lineJoinRound(Cairo::LineJoin::LINE_JOIN_ROUND);
  const Cairo::LineJoin lineJoinBevel(Cairo::LineJoin::LINE_JOIN_BEVEL);  

}; // namespace OOFCanvas
