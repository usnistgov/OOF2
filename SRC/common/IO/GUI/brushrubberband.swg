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


%module(package="ooflib.SWIG.common.IO.GUI") brushrubberband

%include "common/typemaps.swg"
%import(module="oofcanvas.oofcanvasgui") "common/IO/GUI/oofcanvasgui.swg"

%{
  #include "common/IO/GUI/brushrubberband.h"
  #include <oofcanvas.h>
  typedef OOFCanvas::Color CanvasColor;
  typedef OOFCanvas::Coord CanvasCoord;
  typedef OOFCanvas::RubberBand RubberBand;
%}

class BrushRubberBand : public RubberBand {
public:
  BrushRubberBand(GfxBrushStyle *brush);
  ~BrushRubberBand();
};

#endif // RUBBERBAND_SWG
