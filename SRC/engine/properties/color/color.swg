// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module(package="engine.properties.color") color

%{
#include "engine/properties/color/color.h"
#include "common/ccolor.h"
%}

%include "common/typemaps.swg"
%import "common/ccolor.swg"
%import "engine/property.swg"

class ColorProp : public Property {
public:
  ColorProp(PyObject *self, char *name, CColor *cv);
  CColor color();
};

%pythoncode "engine/properties/color/color.spy"
