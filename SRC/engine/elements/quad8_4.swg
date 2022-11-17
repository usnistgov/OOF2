// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef QUAD84_SWIG
#define QUAD84_SWIG

%module(package="ooflib.SWIG.engine.elements") quad8_4

%include "common/typemaps.swg"
%{
  extern void quad8_4init();
%}
void quad8_4init();

// Quad8_4 (superparametric) elements are not constructed, because
// there's no machinery for placing the shape-controlling side nodes,
// and also no way to draw them properly.  If they're ever used,
// uncomment the following lines:
// %pythoncode %{
//   quad8_4init()
// %}

#endif // QUAD8_SWIG
