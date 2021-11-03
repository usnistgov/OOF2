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
// a GfxBrushStyle class derived from it here.  The draw() routine
// draws the brush's "rubberband" while the user is moving the mouse.
// The classes defined here must be swigged in gfxbrushstyle.swg, and
// the brushstyle registration must be modified in gfxbrushstyle.spy.

class GfxBrushStyle {
public:
  virtual ~GfxBrushStyle() {}
  virtual void draw(OOFCanvas::CanvasLayer*, const OOFCanvas::Coord&) const = 0;
};

class GfxCircleBrush : public GfxBrushStyle, public CircleBrush {
public:
  GfxCircleBrush(double r) : CircleBrush(r) {}
  virtual void draw(OOFCanvas::CanvasLayer*, const OOFCanvas::Coord&) const;
};

class GfxSquareBrush : public GfxBrushStyle, public SquareBrush {
public:
  GfxSquareBrush(double hs) : SquareBrush(hs) {}
  virtual void draw(OOFCanvas::CanvasLayer*, const OOFCanvas::Coord&) const;
};

#endif // GFXBRUSHSTYLE_H
