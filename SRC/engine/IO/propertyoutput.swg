// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PROPERTYOUTPUT_SWG
#define PROPERTYOUTPUT_SWG

%module propertyoutput

%include "engine/typemaps.swg"
%extern "engine/properties.swg"
%{
#include "engine/IO/propertyoutput.h"
%}

%typemap(python, out) PropertyOutput* {
  // typemap(python, out) PropertyOutput*
  $target = $source->pythonObject();
}

%typemap(python, out) PropertyOutputInit* {
  // typemap(python, out) PropertyOutputInit*
  $target = $source->pythonObject();
}

%pragma(python) include="engine/IO/propertyoutput.spy"

// PropertyOutput initializers

class PropertyOutputInit {};
class ArithmeticPropertyOutputInit : public PropertyOutputInit {};
class NonArithmeticPropertyOutputInit : public PropertyOutputInit {};

class ScalarPropertyOutputInit : public ArithmeticPropertyOutputInit {
public:
  ScalarPropertyOutputInit();
};

class TwoVectorPropertyOutputInit : public ArithmeticPropertyOutputInit {
public:
  TwoVectorPropertyOutputInit();
};

class ThreeVectorPropertyOutputInit : public ArithmeticPropertyOutputInit {
public:
  ThreeVectorPropertyOutputInit();
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class PropertyOutput {
public:
  ~PropertyOutput();
  const string &name();
  double getFloatParam(char*);
  int getIntParam(char*);
  %new const string *getStringParam(char*);
  %new const string *getEnumParam(char*);
  %new const string *getRegisteredParamName(char*);
};

class ArithmeticPropertyOutput : public PropertyOutput {
public:
  %new ArithmeticOutputValueVec *evaluate(
				  FEMesh*, Element*,
				  ArithmeticPropertyOutputInit*,
				  MasterCoordVec*);
};

class NonArithmeticPropertyOutput : public PropertyOutput {
public:
  %new NonArithmeticOutputValueVec *evaluate(
				  FEMesh*, Element*,
				  NonArithmeticPropertyOutputInit*,
				  MasterCoordVec*);
};

class PropertyOutputRegistration {
public:
  PropertyOutputRegistration(char*, PropertyOutputInit*);
  ~PropertyOutputRegistration();
  const string &name();
  const PropertyOutputInit *initializer();
  %new PropertyOutput *instantiate(PyObject*);
};


#endif
