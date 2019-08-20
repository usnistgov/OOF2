// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELSELECTIONCOURIERI_SWG
#define PIXELSELECTIONCOURIERI_SWG

%module pixelselectioncourieri

%include "common/typemaps.swg"
%extern "common/burn.swg"
%extern "common/ccolor.swg"
%extern "common/colordifference.swg"
%extern "common/pixelselectioncourier.swg"
%pragma(python) code="from ooflib.SWIG.common.burn import CPixelDifferentiator3Ptr"
%pragma(python) code="from ooflib.SWIG.common.pixelselectioncourier import PixelSelectionCourierPtr"

%{
#include "image/pixelselectioncourieri.h"
#include "common/ccolor.h"
#include "common/colordifference.h"
#include "common/burn.h"
%}
   
class ColorSelection : public PixelSelectionCourier {
public:
  ColorSelection(CMicrostructure*, OOFImage*, CColor*, ColorDifference*);
  ~ColorSelection();
};

class BurnSelection : public PixelSelectionCourier {
public:
  BurnSelection(CMicrostructure*, CPixelDifferentiator3*, ICoord *iPoint, bool);
  ~BurnSelection();
};

#endif // PIXELSELECTIONCOURIERI_SWG
