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
%extern "gfxbrushstyle.swg"
%extern "common/IO/OOFCANVAS/oofcanvas.swg"

%pragma(python) code="from ooflib.SWIG.common.IO.OOFCANVAS.oofcanvas import RubberBandPtr"

class BrushRubberBand : public RubberBand {
public:
  BrushRubberBand(GfxBrushStyle *brush);
};

#endif // RUBBERBAND_SWG
