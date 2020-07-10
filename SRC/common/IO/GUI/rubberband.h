// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef RUBBERBAND_H
#define RUBBERBAND_H

#include <oofconfig.h>

#include "common/IO/GUI/OOFCANVAS/rubberband.h"
#include <vector>

class GfxBrushStyle;

class BrushRubberBand : public OOFCanvas::RubberBand {
private:
  GfxBrushStyle *style;
  std::vector<OOFCanvas::Coord> trail;
public:
  BrushRubberBand(GfxBrushStyle*);
  virtual void start(OOFCanvas::CanvasLayer*, double, double);
  virtual void draw(double, double);
};

#endif // RUBBERBAND_H
