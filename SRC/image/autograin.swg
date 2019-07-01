// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef AUTOGRAIN_SWG
#define AUTOGRAIN_SWG

%module autograin
%include "common/typemaps.swg"

%{
#include "common/cmicrostructure.h"
#include "image/autograin.h"
#include "image/oofimage.h"
%}
%pragma(python) include="image/autograin.spy"

class CPixelDifferentiator {};

class CColorDifferentiator : public CPixelDifferentiator {
public:
  CColorDifferentiator(OOFImage*, double, double, bool);
};

const string *autograin(CMicrostructure*, CPixelDifferentiator*,
			bool, char*);

#endif // AUTOGRAIN_SWG
