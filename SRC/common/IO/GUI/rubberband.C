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
// oofcanvas for some reason.

// The BrushRubberBand draws a curve along the centerline of the brush
// stroke and also outlines the brush.

BrushRubberBand::BrushRubberBand(GfxBrushStyle *brush)
  : style(brush),
    trail(nullptr)
{}

void BrushRubberBand::start(OOFCanvas::CanvasLayer *lyr,
			    const OOFCanvas::Coord &pt)
{
  KeyHolder kh(lock);
  RubberBand::start(lyr, pt);
  trail = new OOFCanvas::CanvasCurve();
  trail->addPoint(pt);
  trail->setLineColor(color);
  trail->setLineWidthInPixels(lineWidth);
  doDashes(trail);
  layer->addItem(trail);
  style->start(lyr, startPt);	// adds style's CanvasItem to the layer.
}

void BrushRubberBand::stop() {
  OOFCanvas::RubberBand::stop();
  style->stop();
  trail = nullptr;
}

void BrushRubberBand::update(const OOFCanvas::Coord &pt) {
  KeyHolder kh(lock);
  RubberBand::update(pt);
  trail->addPoint(currentPt);
  style->update(currentPt);
}
