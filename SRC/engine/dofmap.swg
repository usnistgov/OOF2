// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef DOFMAP_SWG
#define DOFMAP_SWG

%module(package="ooflib.SWIG.engine") dofmap

%include "common/typemaps.swg"
%import "common/doublevec.swg"

%{
#include "common/doublevec.h"
#include "common/tostring.h"
#include "engine/dofmap.h"
%}

class DoFMap {
public:
  DoFMap();
  ~DoFMap();
  %newobject extract;
  DoubleVec* extract(DoubleVec&);
  void inject(DoubleVec&, DoubleVec&);
  int range();
  int domain();
};

ADD_REPR_GENERIC(DoFMap);

DoFMap compose(DoFMap&, DoFMap&);
DoFMap concat(DoFMap&, DoFMap&);

#endif // DOFMAP_SWG
