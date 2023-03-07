// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ENTIREMESHSUBPROBLEM_SWG
#define ENTIREMESHSUBPROBLEM_SWG

%module(package="ooflib.SWIG.engine") entiremeshsubproblem

%include "common/typemaps.swg"
%import "engine/csubproblem.swg"

%{
#include "engine/entiremeshsubproblem.h"
  #include "engine/flux.h"	// SWIGBUG
%}

class CEntireMeshSubProblem : public CSubProblem {
public:
  CEntireMeshSubProblem();
  ~CEntireMeshSubProblem();
};

%pythoncode "engine/entiremeshsubproblem.spy"

#endif // ENTIREMESHSUBPROBLEM_SWG
