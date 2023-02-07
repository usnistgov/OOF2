// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELGROUPSUBPROBLEM_SWG
#define PIXELGROUPSUBPROBLEM_SWG

%module(package="ooflib.SWIG.engine") pixelgroupsubproblem

%include "common/typemaps.swg"
%import "engine/csubproblem.swg"

%{
#include "engine/pixelgroupsubproblem.h"
%}

class CPixelGroupSubProblem: public CSubProblem {
public:
  CPixelGroupSubProblem(char*);
  ~CPixelGroupSubProblem();
};

%pythoncode "engine/pixelgroupsubproblem.spy"

#endif // PIXELGROUPSUBPROBLEM_SWG
