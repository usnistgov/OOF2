// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ORIENT_BURN_SWG
#define ORIENT_BURN_SWG

%module burn
%include "common/typemaps.swg"
%extern "common/pixelselectioncourier.swg"

%pragma(python) code="from ooflib.SWIG.common.pixelselectioncourier import PixelSelectionCourierPtr"

%{
#include "orientationmap/burn.h"
%}
%pragma(python) include="burn.spy"

class OrientationBurner {
public:
  OrientationBurner(double, double, char*, bool);
};

class OrientBurnSelection : public PixelSelectionCourier {
public:
  OrientBurnSelection(CMicrostructure*, OrientationBurner*, OrientMap*,
		      ICoord *iPoint);
  ~OrientBurnSelection();
};

#endif // ORIENT_BURN_SWG
