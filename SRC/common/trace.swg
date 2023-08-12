// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef TRACE_SWG
#define TRACE_SWG

%module(package="ooflib.SWIG.common") trace

%include "common/typemaps.swg"

#ifdef DEBUG

%{
#include "common/trace.h"
%}

%inline %{
  void trace_enable() {
    Trace_t::enable();
  }

  void trace_disable() {
    Trace_t::disable();
  }
%}

#else // !DEBUG

%pythoncode %{
def trace_enable(): pass
def trace_disable(): pass
%}

#endif // !DEBUG

#endif // TRACE_SWG
