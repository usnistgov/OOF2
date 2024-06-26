// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef STEPERRORSCALING_SWG
#define STEPERRORSCALING_SWG

%module(package="ooflib.SWIG.engine") steperrorscaling

%include "common/typemaps.swg"
%{
#include "common/doublevec.h"
#include "engine/steperrorscaling.h"
%}

%nodefaultctor StepErrorScaling;

class StepErrorScaling {
public:
  bool globalscaling();
};

%extend StepErrorScaling {
  double __call__(double deltat, DoubleVec &start,
		  DoubleVec &end0, DoubleVec &end1)
  {
    return (*self)(deltat, start, end0, end1);
  }
}

class RelativeErrorScaling : public StepErrorScaling {
public:
  RelativeErrorScaling();
};

class AbsoluteErrorScaling : public StepErrorScaling {
public:
  AbsoluteErrorScaling();
};

class XOverErrorScaling : public StepErrorScaling {
public:
  XOverErrorScaling();
};

class GlobalErrorScaling : public StepErrorScaling {
public:
  GlobalErrorScaling();
};

%pythoncode "engine/steperrorscaling.spy"

#endif // STEPERRORSCALING_SWG
