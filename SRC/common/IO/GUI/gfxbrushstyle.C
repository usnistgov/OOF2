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

#include "gfxbrushstyle.h"

void GfxCircleBrush::start(OOFCanvas::CanvasLayer *layer,
			   const OOFCanvas::Coord &pt)
{
  // TODO GTK3: Get dashlength, linewidth, and colors from parameters
  // in genericSelectGUI.py
  std::cerr << "GfxCircleBrush::start" << std::endl;
  double dashLength = 7;
  double lineWidth = 2;
  circle = new OOFCanvas::CanvasCircle(pt, r);
  std::cerr << "GfxCircleBrush::start: calling setLineWidthInPixels, circle=" << circle << std::endl;
  circle->setLineWidthInPixels(lineWidth);
  std::cerr << "GfxCircleBrush::start: calling setLineColor" << std::endl;
  circle->setLineColor(OOFCanvas::white);
  circle->setDashColor(OOFCanvas::black);
  circle->setDashInPixels(dashLength);
  layer->addItem(circle);
  std::cerr << "GfxCircleBrush::start: done" << std::endl;
}

void GfxCircleBrush::update(const OOFCanvas::Coord &pt) {
  circle->setCenter(pt);
}

void GfxCircleBrush::stop() {
  circle = nullptr;
}

void GfxSquareBrush::start(OOFCanvas::CanvasLayer *layer,
			   const OOFCanvas::Coord &pt)
{
  std::cerr << "GfxSquareBrush::start: " << this << std::endl;

  // TODO GTK3: Get dashlength, linewidth, and colors from parameters
  // in genericSelectGUI.py
  double dashLength = 7;
  double lineWidth = 2;

  OOFCanvas::Coord diag(size, size);
  rectangle = new OOFCanvas::CanvasRectangle(pt-diag, pt+diag);
  rectangle->setLineWidthInPixels(lineWidth);
  rectangle->setLineColor(OOFCanvas::white);
  rectangle->setDashColor(OOFCanvas::black);
  rectangle->setDashInPixels(dashLength);
  layer->addItem(rectangle);
  std::cerr << "GfxSquareBrush::start: done" << std::endl;
}

void GfxSquareBrush::update(const OOFCanvas::Coord &pt) {
  OOFCanvas::Coord diag(size, size);
  rectangle->update(pt-diag, pt+diag);
}

void GfxSquareBrush::stop() {
  rectangle = nullptr;
}
