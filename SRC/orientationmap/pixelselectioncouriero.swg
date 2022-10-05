// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELSELECTIONCOURIERO_SWG
#define PIXELSELECTIONCOURIERO_SWG

%module(package="ooflib.SWIG.orientationmap") pixelselectioncouriero

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/pixelselectioncourier.swg"
%import "engine/corientation.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/corientation.h"
#include "orientationmap/pixelselectioncouriero.h"
%}

class OrientationSelection : public PixelSelectionCourier {
public:
  OrientationSelection(OrientMap*, COrientation*, char*, double);
  ~OrientationSelection();
};

#endif // PIXELSELECTIONCOURIERO_SWG

