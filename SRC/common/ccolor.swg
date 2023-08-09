// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CCOLOR_SWG
#define CCOLOR_SWG

%module(package="ooflib.SWIG.common") ccolor

%include "common/typemaps.swg"

%{
#include "common/ccolor.h"
%}

// TODO LATER:  Investigate whether all colors should be SWIG'd CColors.

%typemap(in) CColor* (CColor clr) {
  // typemap(in) CColor*  -- converts Python color to C++ CColor
  PyObject *red = PyObject_CallMethod($input, "getRed", NULL);
  PyObject *grn = PyObject_CallMethod($input, "getGreen", NULL);
  PyObject *blu = PyObject_CallMethod($input, "getBlue", NULL);
  PyObject *alf = PyObject_CallMethod($input, "getAlpha", NULL);
  clr.setRed(PyFloat_AsDouble(red));
  clr.setGreen(PyFloat_AsDouble(grn));
  clr.setBlue(PyFloat_AsDouble(blu));
  clr.setAlpha(PyFloat_AsDouble(alf));
  Py_XDECREF(red);
  Py_XDECREF(grn);
  Py_XDECREF(blu);
  Py_XDECREF(alf);
  $1 = &clr;
}

%typemap(out) CColor {
  // typemap(out) CColor -- converts C++ CColor to Python RGBAColor
  FETCH_CLASS(ooflib.common.color, RGBAColor);
  $result = PyObject_CallFunction(RGBAColorClass, "dddd",
				  $1.getRed(), $1.getGreen(),
				  $1.getBlue(), $1.getAlpha());
  
}

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

class CColor {
public:
  double getRed();
  double getGreen();
  double getBlue();
  double getAlpha();
  double getGray();
  double getHue();
  double getSaturation();
  double getValue();

  void setRed(double);
  void setGreen(double);
  void setBlue(double);
  void setAlpha(double);
};

class CGrayColor: public CColor {
public:
  void setGray(double);
};

class CHSVColor: public CColor {
public:
  void setHue(double);
  void setSaturation(double);
  void setValue(double);
};

#endif // CCOLOR_SWG
