// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef GAUSSPOINT_SWG
#define GAUSSPOINT_SWG

%module(package="ooflib.SWIG.engine") gausspoint

%{
#include "engine/gausspoint.h"
%}

%include "common/typemaps.swg"
%import "common/coord.swg"
%import "engine/mastercoord.swg"

%nodefaultctor GaussPoint;

ADD_REPR_GENERIC(GaussPoint);

class GaussPoint : public Position, public MasterPosition {
public:
  double weight();
  MasterCoord mastercoord();
  ~GaussPoint();
};

%nodefaultctor GaussPointIterator;
%feature("valuewrapper") GaussPointIterator;
%rename(increment) GaussPointIterator::operator++;
%newobject gausspointptr;

class GaussPointIterator {
public:
  bool operator!=(const GaussPointIterator&) const;
  void operator++();
  GaussPoint *gausspointptr() const;
};

%nodefaultctor GaussPointIntegrator;
%feature("valuewrapper") GaussPointIntegrator;

class GaussPointIntegrator {
public:
  GaussPointIterator begin() const;
  GaussPointIterator end() const;
};

%pythoncode %{
 # See usage note in gausspoint.h
 def _gpt_iter_(self):
    beginp = self.begin()
    endp = self.end()
    while beginp != endp:
       yield beginp.gausspointptr()
       beginp.increment()
 GaussPointIntegrator.__iter__ = _gpt_iter_
%}

#endif // GAUSSPOINT_SWG
