// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELDIFFORIENT_SWG
#define PIXELDIFFORIENT_SWG

%module pixeldifforient
%include "common/typemaps.swg"

%{
#include "orientationmap/orientmapdata.h"
#include "image/autograin.h"
#include "orientationmap/pixeldifferentiator.h"
%}

%pragma(python) code="from ooflib.SWIG.image.autograin import CPixelDifferentiatorPtr"

%pragma(python) include="orientationmap/pixeldifferentiator.spy"
%extern "image/autograin.swg"
   
class COrientationDifferentiator : public CPixelDifferentiator {
public:
  COrientationDifferentiator(OrientMap*, double, double, char*);
};


#endif // PIXELDIFFORIENT_SWG
