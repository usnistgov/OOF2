// -*- C++ -*-
// $RCSfile: compoundsubproblem.swg,v $
// $Revision: 1.6 $
// $Author: langer $
// $Date: 2010/11/15 22:02:44 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef COMPOUNDSUBPROBLEM_SWG
#define COMPOUNDSUBPROBLEM_SWG

%module compoundsubproblem

%include "engine/typemaps.swg"
%extern "engine/csubproblem.swg"
%pragma(python) include="engine/compoundsubproblem.spy"
%pragma(python) code="from ooflib.SWIG.engine.csubproblem import CSubProblemPtr"
%pragma(python) code="from ooflib.SWIG.common.lock import LockPtr"

%{
#include "engine/compoundsubproblem.h"
%}

class CIntersectionSubProblem: public CSubProblem {
public:
  CIntersectionSubProblem(CSubProblem*, CSubProblem*);
  // precomputeLock and precomputeRequired have to be listed here,
  // even though they're swigged in the base class, because swig seems
  // to have a bug.  If data members are swigged in multiple
  // subclasses, when the base class is in another file, then the
  // PyMethodDef list in the swig-generated C++ files lists the wrong
  // class for the set and get methods.
  Lock precomputeLock;
  bool precomputeRequired;
};

class CUnionSubProblem: public CSubProblem {
public:
  CUnionSubProblem(CSubProblem*, CSubProblem*);
  Lock precomputeLock;
  bool precomputeRequired;
};

class CXorSubProblem: public CSubProblem {
public:
  CXorSubProblem(CSubProblem*, CSubProblem*);
  Lock precomputeLock;
  bool precomputeRequired;
};

class CComplementSubProblem: public CSubProblem {
public:
  CComplementSubProblem(CSubProblem*);
  Lock precomputeLock;
  bool precomputeRequired;
};

#endif // COMPOUNDSUBPROBLEM_SWG
