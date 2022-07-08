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

%module pixelgroupsubproblem

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/csubproblem.swg"
#endif // NOSECONDIMPORTS

// %pragma(python) code="from ooflib.SWIG.engine.csubproblem import CSubProblemPtr"
// %pragma(python) code="from ooflib.SWIG.common.lock import LockPtr"

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
