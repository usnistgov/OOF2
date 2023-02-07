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

%module(package="ooflib.SWIG.engine.IO") propertyoutput

%include "common/typemaps.swg"
%import "engine/mastercoord.swg"
%import "engine/property.swg"
%import "engine/outputval.swg"

%{
#include "engine/mastercoord.h"
#include "engine/IO/propertyoutput.h"
%}

// %typemap(out) PropertyOutput* {
//   // typemap(out) PropertyOutput*
//   $result = $1->pythonObject();
// }

// %typemap(out) PropertyOutputInit* {
//   // typemap(out) PropertyOutputInit*
//   $result = $1->pythonObject();
// }

// %define PYTHONEXPORTABLEtest(CLASS)
// %typemap(out) CLASS* {
//   // typemap(out) CLASS* (via PYTHONEXPORTABLE)
//   if($1) {
//     $result = $1->pythonObject(false);
//     if(!$result)
//       SWIG_fail;
//   }
//   else {
//     Py_INCREF(Py_None);
//     $result = Py_None;
//   }
//  }
// %typemap(out) New##CLASS* {
//   // typemap(out) NEW##CLASS* (via PYTHONEXPORTABLE)
//   if($1) {
//     $result = $1->pythonObject(true);
//     if(!$result)
//       SWIG_fail;
//   }
//   else {
//     Py_INCREF(Py_None);
//     $result = Py_None;
//   }
//  }
// // %typemap(newfree) CLASS* {
// //   // typemap(newfree) CLASS* (via PYTHONEXPORTABLE)
// //   delete $1;
// //  }
// %enddef


PYTHONEXPORTABLE(PropertyOutput);
PYTHONEXPORTABLE(PropertyOutputInit);
MAKE_LISTVEC_TYPEMAPS(MasterCoord);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// OutputVal initializers

%nodefaultctor PropertyOutputValInit;

class PropertyOutputValInit {
public:
  ~PropertyOutputValInit();
};

class DefaultPropertyOutputValInit : public PropertyOutputValInit {
public:
  DefaultPropertyOutputValInit(OutputVal*);
};

// PropertyOutput initializers

%nodefaultctor PropertyOutputInit;

class PropertyOutputInit {};

class ArithmeticPropertyOutputInit : public PropertyOutputInit {
public:
  ArithmeticPropertyOutputInit();
};

class NonArithmeticPropertyOutputInit : public PropertyOutputInit {
public:
  NonArithmeticPropertyOutputInit();
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

%nodefaultctor PropertyOutput;

class PropertyOutput {
public:
  ~PropertyOutput();
  const std::string &name();
  double getFloatParam(char*);
  int getIntParam(char*);
  void setInitializer(PropertyOutputValInit*);
  %newobject getStringParam;
  const std::string *getStringParam(char*);
  %newobject getEnumParam;
  const std::string *getEnumParam(char*);
  %newobject getRegisteredParamName;
  const std::string *getRegisteredParamName(char*);
  %newobject getListOfStringsParam;
  std::vector<std::string> *getListOfStringsParam(char*);
};

%nodefaultctor ArithmeticPropertyOutput;

class ArithmeticPropertyOutput : public PropertyOutput {
public:
  %newobject evaluate;
  ArithmeticOutputValueVec *evaluate(FEMesh*, Element*, MasterCoordVec*);
};

%nodefaultctor NonArithmeticPropertyOutput;

class NonArithmeticPropertyOutput : public PropertyOutput {
public:
  %newobject evaluate;
  NonArithmeticOutputValueVec *evaluate(FEMesh*, Element*, MasterCoordVec*);
};

class PropertyOutputRegistration {
public:
  PropertyOutputRegistration(char*);
  ~PropertyOutputRegistration();
  const std::string &name();
  %newobject instantiateArithmetic;
  PropertyOutput *instantiateArithmetic(char*, PyObject*);
  %newobject instantiateNonArithmetic;
  PropertyOutput *instantiateNonArithmetic(char*, PyObject*);
};

%pythoncode "engine/IO/propertyoutput.spy"

#endif	// PROPERTYOUTPUT_SWG
