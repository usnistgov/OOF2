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
%import "common/IO/oofcanvas.swg"

%{
#include "common/IO/GUI/brushrubberband.h"
#include <oofcanvas.h>
// typedef OOFCanvas::Color CanvasColor;
// typedef OOFCanvas::Coord CanvasCoord;
// typedef OOFCanvas::RubberBand CanvasRubberBand;
// using namespace OOFCanvas;
%}

// This is inelegant.  BrushRubberBand has a base class,
// OOFCanvas::RubberBand, which is defined in a different library.
// SWIG doesn't really need to know that, though.  When I tried to
// include the base class info here, SWIG was complaining about an
// unknown module name for the base class.  So the base class is
// omitted here, and the base class functions are listed as if they're
// regular BrushRubberBand methods.  The C++ code will still call the
// correct base class methods.  The problem is that it will break if
// the base class changes.  TODO: Find out how to do this correctly.
//
// /Users/langer/FE/OOF2/SRC/common/IO/GUI/rubberband.swg:28: Warning 401: Base class 'RubberBand' ignored - unknown module name for base. Either import the appropriate module interface file or specify the name of the module in the %import directive.


// Maybe SWIG doesn't know that CanvasColor is the same as
// OOFCanvas::Color, so the arg to setColor is rejected, when called
// from MouseHandler.down in genericselectGUI.py?

class BrushRubberBand {
public:
  BrushRubberBand(GfxBrushStyle *brush);
  ~BrushRubberBand();
  void setLineWidth(double);
  void setColor(const OOFCanvas::Color*);
  void setDashed(bool);
  void setDashLength(double);
  void setDashColor(const OOFCanvas::Color*);
  void update(const OOFCanvas::Coord*);
};

#endif // RUBBERBAND_SWG
