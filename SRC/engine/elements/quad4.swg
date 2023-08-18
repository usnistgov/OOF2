// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef QUAD4_SWIG
#define QUAD4_SWIG

%module(package="ooflib.SWIG.engine.elements") quad4

%include "common/typemaps.swg"
%{
  extern void quad4init();
%}
void quad4init();

%pythoncode %{
  quad4init()
%}

#endif // QUAD4_SWIG
