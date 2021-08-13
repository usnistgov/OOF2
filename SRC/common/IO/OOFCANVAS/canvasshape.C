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
    lineWidthInPixels = false;
    line = true;
    modified();
  }

  void CanvasShape::setLineWidthInPixels(double w) {
    lineWidth = w;
    lineWidthInPixels = true;
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

  double CanvasShape::lineWidthInUserUnits(const OffScreenCanvas *canvas) const
  {
    if(lineWidthInPixels) {
      return canvas->pixel2user(lineWidth);
    }
    return lineWidth;
  }

  std::vector<double> CanvasShape::dashLengthInUserUnits(
				 Cairo::RefPtr<Cairo::Context> ctxt)
    const
  {
    if(!dashLengthInPixels)
      return dash;
    std::vector<double> newdash(dash);
    double dummy=0;
    for(unsigned int i=0; i<dash.size(); i++)
      ctxt->device_to_user_distance(newdash[i], dummy);
    return newdash;
  }

  void CanvasShape::setLineColor(const Color &color) {
    lineColor = color;
    line = true;
  }

  void CanvasShape::setDash(const std::vector<double> &d, int offset) {
    dash = d;
    dashOffset = offset;
    dashLengthInPixels = false;
  }
  
  void CanvasShape::setDash(const std::vector<double> *d, int offset) {
    setDash(*d, offset);
  }

  void CanvasShape::setDash(double d) {
    dash = std::vector<double>({d});
    dashOffset = 0;
    dashLengthInPixels = false;
  }
  
  void CanvasShape::setDashInPixels(const std::vector<double> &d, int offset) {
    dash = d;
    dashOffset = offset;
    dashLengthInPixels = true;
  }

  void CanvasShape::unsetDashes() {
    dash.clear();
  }

  void CanvasShape::setDashInPixels(const std::vector<double> *d, int offset) {
    setDashInPixels(*d, offset);
  }

  void CanvasShape::setDashInPixels(double d) {
    dash = std::vector<double>({d});
    dashOffset = 0;
    dashLengthInPixels = true;
  }

  void CanvasShape::setDashColor(const Color &clr) {
    dashColor = clr;
    dashColorSet = true;
  }

  void CanvasShape::stroke(Cairo::RefPtr<Cairo::Context> ctxt) const {
    ctxt->set_line_width(lineWidthInUserUnits(ctxt));
    ctxt->set_line_cap(lineCap);
    ctxt->set_line_join(lineJoin);
    if(dash.empty()) {
      // No dashes
      lineColor.set(ctxt);
      ctxt->stroke();
    }
    else if(!dashColorSet) {
      // line is dashed with gaps between dashes.
      lineColor.set(ctxt);
      ctxt->set_dash(dashLengthInUserUnits(ctxt), dashOffset);
      ctxt->stroke();
    }
    else {
      // gaps between dashes are filled with the dashColor
      dashColor.set(ctxt);
      ctxt->stroke_preserve();
      lineColor.set(ctxt);
      ctxt->set_dash(dashLengthInUserUnits(ctxt), dashOffset);
      ctxt->stroke();
    }
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

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
      stroke(ctxt);
    }
    else if(line) {
      stroke(ctxt);
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
