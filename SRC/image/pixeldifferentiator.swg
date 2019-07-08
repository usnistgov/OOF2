// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELDIFFERENTIATORI_SWG
#define PIXELDIFFERENTIATORI_SWG

%module pixeldifferentiator
%include "common/typemaps.swg"

%{
#include "common/cmicrostructure.h"
#include "image/pixeldifferentiator.h"
#include "image/oofimage.h"
%}

%pragma(python) code="from ooflib.SWIG.common.burn import CPixelDifferentiatorPtr"

%pragma(python) include="image/pixeldifferentiator.spy"
%extern "common/burn.swg"

class CColorDifferentiator : public CPixelDifferentiator {
public:
  CColorDifferentiator(OOFImage*, double, double, bool);
};


#endif // PIXELDIFFERENTIATORI_SWG
