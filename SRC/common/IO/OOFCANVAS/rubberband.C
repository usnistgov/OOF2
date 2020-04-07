// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include "canvascircle.h"
#include "canvasrectangle.h"
#include "canvassegment.h"
#include "rubberband.h"
#include "utility.h"
#include <math.h>
#include <vector>

namespace OOFCanvas {

  RubberBand::RubberBand()
    : active_(false),
      lineWidth(1),
      color(black)
  {}

  RubberBand::~RubberBand() {}

  void RubberBand::start(CanvasLayer *lyr, double x, double y) {
    layer = lyr;
    startPt = Coord(x, y);
    currentPt = startPt;
    active_ = true;
  }

  void RubberBand::draw(double x, double y) {
    currentPt = Coord(x, y);
  }

  void RubberBand::stop() {
    layer->clear();
    active_ = false;
  }

  void RectangleRubberBand::draw(double x, double y) {
    RubberBand::draw(x, y);
    CanvasRectangle *rect = new CanvasRectangle(startPt, currentPt);
    rect->setLineWidthInPixels();
    rect->setLineWidth(lineWidth);
    rect->setLineColor(color);
    layer->clear();
    layer->addItem(rect);
  }

  void CircleRubberBand::draw(double x, double y) {
    RubberBand::draw(x, y);
    double r = sqrt((currentPt - startPt).norm2());
    CanvasCircle *circle = new CanvasCircle(startPt, r);
    circle->setLineWidthInPixels();
    circle->setLineWidth(lineWidth);
    circle->setLineColor(color);
    CanvasSegment *seg = new CanvasSegment(startPt, currentPt);
    seg->setLineWidthInPixels();
    seg->setLineWidth(lineWidth/2.);
    seg->setLineColor(color);
    layer->clear();
    layer->addItem(circle);
    layer->addItem(seg);
  }

  void EllipseRubberBand::draw(double x, double y) {
    RubberBand::draw(x, y);
    CanvasRectangle *rect = new CanvasRectangle(startPt, currentPt);
    rect->setLineWidthInPixels();
    rect->setLineWidth(0.5*lineWidth);
    rect->setLineColor(color);

    CanvasEllipse *ellipse = new CanvasEllipse(0.5*(currentPt+startPt),
					       0.5*(currentPt-startPt),
					       0.0 /* angle */ );

    // TODO: Allow the ellipse to be rotated.  This would require a
    // more complicated API.
    
    ellipse->setLineWidthInPixels();
    ellipse->setLineWidth(lineWidth);
    ellipse->setLineColor(color);

    layer->clear();
    layer->addItem(rect);
    layer->addItem(ellipse);
  }
  
};				// namespace OOFCanvas
