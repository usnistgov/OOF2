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

void GfxCircleBrush::draw(OOFCanvas::CanvasLayer *layer,
			  const OOFCanvas::Coord &pt)
  const
{
  double dashLength = 7;
  double lineWidth = 2;
  OOFCanvas::CanvasCircle *circle = new OOFCanvas::CanvasCircle(pt, r);
  circle->setLineWidthInPixels(lineWidth);
  circle->setLineColor(OOFCanvas::white);
  circle->setDashColor(OOFCanvas::black);
  circle->setDashInPixels(dashLength);
  layer->addItem(circle);
}

void GfxSquareBrush::draw(OOFCanvas::CanvasLayer *layer,
			  const OOFCanvas::Coord &pt)
  const
{
  double dashLength = 7;
  double lineWidth = 2;
  OOFCanvas::Coord diag(size, size);

  OOFCanvas::CanvasRectangle *rect =
    new OOFCanvas::CanvasRectangle(pt-diag, pt+diag);
  rect->setLineWidthInPixels(lineWidth);
  rect->setLineColor(OOFCanvas::white);
  rect->setDashColor(OOFCanvas::black);
  rect->setDashInPixels(dashLength);
  layer->addItem(rect);
}
