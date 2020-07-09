// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/IO/GUI/rubberband.h"
#include "common/IO/GUI/gfxbrushstyle.h"

// Definitions of RubberBand subclass(es) that aren't defined in
// OOFCANVAS for some reason.

// The BrushRubberBand draws a curve along the centerline of the brush
// stroke and also outlines the brush.

BrushRubberBand::BrushRubberBand(GfxBrushStyle *brush) :
  style(brush)
{}

void BrushRubberBand::start(OOFCanvas::CanvasLayer *lyr, double x, double y) {
  RubberBand::start(lyr, x, y);
  trail.emplace_back(x, y);
}

void BrushRubberBand::draw(double x, double y) {
  double lineWidth = 1;
  double dashLength = 7;
  RubberBand::draw(x, y);
  trail.emplace_back(x, y);
  layer->clear();
  style->draw(layer, currentPt); // outline of the brush

  // TODO: Can we reuse the previous CanvasCurve?
  OOFCanvas::CanvasCurve *curve = new OOFCanvas::CanvasCurve(trail);
  curve->setLineColor(OOFCanvas::white);
  curve->setLineWidth(lineWidth);
  curve->setLineWidthInPixels();
  curve->setDashLengthInPixels();
  curve->setDashColor(OOFCanvas::black);
  curve->setDash(std::vector<double>{dashLength}, 0);
  layer->addItem(curve);
}
