// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef TRI3_6_SWIG
#define TRI3_6_SWIG

%module(package="ooflib.SWIG.engine.elements") tri3_6

%include "common/typemaps.swg"
%{
  extern void tri3_6init();
%}
void tri3_6init();

%pythoncode %{
  tri3_6init()
%}

#endif // TRI3_6_SWIG
