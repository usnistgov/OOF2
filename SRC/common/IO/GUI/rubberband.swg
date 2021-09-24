// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef RUBBERBAND_SWG
#define RUBBERBAND_SWG

%module rubberband
%include "common/typemaps.swg"
%{
#include "common/IO/GUI/rubberband.h"
using namespace OOFCanvas;
%}

class RubberBand {
public:
  ~RubberBand();
  void setLineWidth(double);
  void setColor(Color);
  void setDashed(bool);
  void setDashLength(double);
  void setDashColor(Color);
  void draw(double x, double y);
};

%pragma(python) code="from oofcanvas.oofcanvasgui import RubberBandPtr"

class BrushRubberBand : public RubberBand {
public:
  BrushRubberBand(GfxBrushStyle *brush);
};

#endif // RUBBERBAND_SWG
