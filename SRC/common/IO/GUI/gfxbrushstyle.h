// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef GFXBRUSHSTYLE_H
#define GFXBRUSHSTYLE_H

#include <oofconfig.h>

#include "oofcanvas/oofcanvas.h"
#include "common/brushstyle.h"

// Each BrushStyle subclass defined in common/brushstyle.h should have
// a GfxBrushStyle class derived from it here. The start(), stop(),
// and update() methods are the same as in OOFCanvas::RubberBand.  The
// GfxBrushStyle should create CanvasItems in start() and add them to
// the given CanvasLayer, but it should not delete the items.  That is
// done by the CanvasLayer.

// The classes defined here must be swigged in gfxbrushstyle.swg, and
// the brushstyle registration must be modified in gfxbrushstyle.spy.

class GfxBrushStyle {
public:
  virtual ~GfxBrushStyle() {}
  virtual void start(OOFCanvas::CanvasLayer*, const OOFCanvas::Coord&) = 0;
  virtual void update(const OOFCanvas::Coord&) = 0;
  virtual void stop() = 0;
};

class GfxCircleBrush : public GfxBrushStyle, public CircleBrush {
protected:
  OOFCanvas::CanvasCircle *circle;
public:
  GfxCircleBrush(double r) : CircleBrush(r), circle(nullptr) {}
  virtual void start(OOFCanvas::CanvasLayer*, const OOFCanvas::Coord&);
  virtual void update(const OOFCanvas::Coord&);
  virtual void stop();
};

class GfxSquareBrush : public GfxBrushStyle, public SquareBrush {
protected:
  OOFCanvas::CanvasRectangle *rectangle;
public:
  GfxSquareBrush(double hs) : SquareBrush(hs), rectangle(nullptr) {}
  virtual void start(OOFCanvas::CanvasLayer*, const OOFCanvas::Coord&);
  virtual void update(const OOFCanvas::Coord&);
  virtual void stop();
};

#endif // GFXBRUSHSTYLE_H
