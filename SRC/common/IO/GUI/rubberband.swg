// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef RUBBERBAND_SWG
#define RUBBERBAND_SWG

%module(package="ooflib.SWIG.common.IO.GUI") rubberband

%include "common/typemaps.swg"
%import "common/IO/oofcanvas.swg"
%import "common/IO/GUI/oofcanvasgui.swg"

%{
#include "common/IO/GUI/rubberband.h"
  #include <oofcanvas.h>
  typedef OOFCanvas::Color CanvasColor;
  using namespace OOFCanvas;
  //typedef OOFCanvas::RubberBand CanvasRubberBand;
%}

// This typemap converts any Python object with red, green, and blue
// data members to a C++ OOFCanvas::Color.  Here it's used to convert
// a Python OOFCanvas::Color to a C++ OOFCanvas::Color.  This isn't
// necessary if OOF2 and OOFCanvas share the same value of
// SWIG_TYPE_TABLE, which is set (or not) in the top CMakeLists.txt
// file.

// %typemap(in) const CanvasColor& (CanvasColor color) {
//   // typemap(in) OOFCanvas::Color
//   PyObject *red = PyObject_GetAttrString($input, "red");
//   PyObject *green = PyObject_GetAttrString($input, "green");
//   PyObject *blue = PyObject_GetAttrString($input, "blue");
//   color.red = PyFloat_AsDouble(red);
//   color.green = PyFloat_AsDouble(green);
//   color.blue = PyFloat_AsDouble(blue);
//   Py_XDECREF(red);
//   Py_XDECREF(green);
//   Py_XDECREF(blue);
//   $1 = &color;
// }

class BrushRubberBand : public RubberBand {
public:
  BrushRubberBand(GfxBrushStyle *brush);
};

#endif // RUBBERBAND_SWG
