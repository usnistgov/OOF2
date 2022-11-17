// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef TRI6_3_SWIG
#define TRI6_3_SWIG

%module(package="ooflib.SWIG.engine.elements") tri6_3

%include "common/typemaps.swg"
%{
  extern void tri6_3init();
%}
void tri6_3init();

// Tri6_3 (superparametric) elements are not constructed, because
// there's no machinery for placing the shape-controlling side nodes,
// and also no way to draw them properly.  If they're ever used,
// uncomment the following lines:
// %pythoncode %{
//   tri6_3init()
// %}

#endif // TRI6_3_SWIG
