// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef BURNCOMMON_SWG
#define BURNCOMMON_SWG

%module autograin
%include "common/typemaps.swg"

%{
#include "common/burn.h"
#include "common/cmicrostructure.h"
%}

%nodefaultctor CPixelDifferentiator2;
%nodefaultctor CPixelDifferentiator3;
class CPixelDifferentiator3 {};
class CPixelDifferentiator2 {};

%pythoncode "common/burn.spy"

#endif // BURNCOMMON_SWG
