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
#include "canvassegments.h"
#include "rubberband.h"
#include "utility.h"
#include <math.h>
#include <vector>

namespace OOFCanvas {

  RubberBand::RubberBand()
    : active_(false),
      layer(nullptr),
      lineWidth(1),
      color(black),
      dashColor(white),
      dashLength(0),
      coloredDashes(false)
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

  void RubberBand::setDashColor(Color c) {
    dashColor = c;
    coloredDashes = true;
  }

  void RubberBand::doDashes(CanvasShape *shape) {
    if(dashLength > 0) {
      shape->setDashInPixels(dashLength);
      if(coloredDashes)
	shape->setDashColor(dashColor);
    }
  }

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  void LineRubberBand::draw(double x, double y) {
    if(layer != nullptr) {
      RubberBand::draw(x, y);
      CanvasSegment *seg = new CanvasSegment(startPt, currentPt);
      seg->setLineWidthInPixels(lineWidth);
      seg->setLineColor(color);
      doDashes(seg);
      layer->clear();
      layer->addItem(seg);
    }
  }

  void RectangleRubberBand::draw(double x, double y) {
    if(layer != nullptr) {
      RubberBand::draw(x, y);
      CanvasRectangle *rect = new CanvasRectangle(startPt, currentPt);
      rect->setLineWidthInPixels(lineWidth);
      rect->setLineColor(color);
      doDashes(rect);
      layer->clear();
      layer->addItem(rect);
    }
  }

  void CircleRubberBand::draw(double x, double y) {
    if(layer != nullptr) {
      RubberBand::draw(x, y);
      double r = sqrt((currentPt - startPt).norm2());
      CanvasCircle *circle = new CanvasCircle(startPt, r);
      circle->setLineWidthInPixels(lineWidth);
      circle->setLineColor(color);
      CanvasSegment *seg = new CanvasSegment(startPt, currentPt);
      seg->setLineWidthInPixels(lineWidth/2.);
      seg->setLineColor(color);
      doDashes(seg);
      doDashes(circle);
      layer->clear();
      layer->addItem(circle);
      layer->addItem(seg);
    }
  }

  void EllipseRubberBand::draw(double x, double y) {
    if(layer != nullptr) {
      RubberBand::draw(x, y);
      CanvasRectangle *rect = new CanvasRectangle(startPt, currentPt);
      rect->setLineWidthInPixels(0.5*lineWidth);
      rect->setLineColor(color);

      CanvasEllipse *ellipse = new CanvasEllipse(0.5*(currentPt+startPt),
						 0.5*(currentPt-startPt),
						 0.0 /* angle */ );

      // TODO: Allow the ellipse to be rotated.  This would require a
      // more complicated API.
    
      ellipse->setLineWidthInPixels(lineWidth);
      ellipse->setLineColor(color);

      doDashes(ellipse);
      doDashes(rect);

      layer->clear();
      layer->addItem(rect);
      layer->addItem(ellipse);
    }
  }

  SpiderRubberBand::SpiderRubberBand() {
  }

  void SpiderRubberBand::addPoints(const std::vector<Coord> *pts) {
    points.insert(points.end(), pts->begin(), pts->end());
  }

  void SpiderRubberBand::draw(double x, double y) {
    if(layer != nullptr) {
      RubberBand::draw(x, y);
      CanvasSegments *segs = new CanvasSegments();
      segs->setLineWidthInPixels(lineWidth);
      segs->setLineColor(color);
      for(Coord &pt : points) {
	segs->addSegment(currentPt, pt);
      }
      doDashes(segs);
      layer->clear();
      layer->addItem(segs);
    }
  }
  
};				// namespace OOFCanvas
