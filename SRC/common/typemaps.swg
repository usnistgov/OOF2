// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef COMMONTYPEMAPS_SWG
#define COMMONTYPEMAPS_SWG

// This file must be %included in every other swig file.

// TODO PYTHON3: This file should contain only generic typemaps and
// typemap-generating macros.  It should *not* contain anything that
// generates code directly (such as %{ ... %} blocks), except for what
// is needed by the %exception typemap.
//
// Move all of the class-specific typemaps into the .swg files that
// define the types.  The swig files that needs those typemaps will
// also need the class definitions, so they can %import the files
// containing the typemaps.  When %importing the files, prevent
// chaining of %imports by using
//   #ifndef NOSECONDIMPORTS
//   #define NOSECONDIMPORTS
//   %import ...
//   #endif
// That will prevent unrelated types from being defined in the
// swig-generated C++ code, which requires unrelated C++ headers to be
// loaded.

// TODO: Change the xxxxxVec* "in" typemaps so that they accept any
// Python iterator, not just lists and tuples.

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// In these comments, "[x]" means a Python list of objects of type x

// GENERIC TYPEMAPS
// TODO PYTHON3: Update these lists

// out:     std::string*   -> PyUnicode
// newfree: std::string*
// out:     std::string&   -> PyUnicode
// out:     std::string    -> PyUnicode  ** do not use, makes extra copy **
// in:      PyUnicode -> std::string&
// in:      PyUnicode -> std::string*
// in:      PyUnicode -> std::string

// in:      RGBAColor (or similar) -> CColor
// out:     CColor -> RGBAColor

// in: [double] -> const std::vector<double>&
// in: [double] -> const std::vector<double>*
// out: std::vector<double>& -> [double]
// out: std::vector<double>* -> [double]
// out: std::vector<double>  -> [double]

// in: [long] -> const std::vector<INT>&     for INT = int, unsigned char
// in: [long] -> const std::vector<INT>*
// out: std::vector<INT>& -> [long]
// out: std::vector<INT>* -> [long]


// out: std::vector<Coord*>* -> [Coord]  (transfers ownership)
// out: CoordRefVec (aka std::vector<Coord*>*) -> [Coord] (no transfer)
// in: [Coord] -> std::vector<Coord*>*
// out: std::vector<ICoord>* -> [iPoint]
// in: [string] -> std::vector<std::string>*
// out: std::vector<std::string>* -> [string]

// Passing objects out as objects rather than pointers or references
// forces them to be copied an extra time, and maybe should be
// avoided.
// out: ICoord -> iPoint
// out: Coord -> Point

// NAMED TYPEMAPS

// in: PyObject *PythonCallable: PyObject* -> PyObject*  no translation
// in: std::vector<double> &iterable: <iterable> -> const std::vector<double>&
// in: std::vector<double> *iterable: <iterable> -> const std::vector<double>*
// in: std::vector<char*> *argv:  [string] -> std::vector<char*>*
// in: std::vector<Coord>* PointList: [Point] -> std::vector<Coord*>
// in: std::vector<ICoord> *iPointList [iPoint] -> std::vector<ICoord>*
// in: Coord *Point:  Point -> Coord
// in: ICoord *iPoint: iPoint -> ICoord
// in: ICoord *Sequence:  PySequence of length 2 -> ICoord
// in: Coord *Sequence:   PySequence of length 2 -> Coord


%{
#define SWIG_FILE_WITH_INIT
#include <oofconfig.h>
#include "common/cdebug.h"
#include "common/geometry.h"
#include "common/ooferror.h"
#include "common/pythonlock.h"
#include "common/pyutils.h"
#include "common/threadstate.h"
#include <string>
#include <vector>
%}

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// FETCH_CLASS imports the class named CLASS from the module named
// MODULE.  It creates a static variable by appending "Class" to the
// given CLASS and stores a pointer to the the PyObject in it.  Don't
// use quotation marks around the arguments when calling FETCH_CLASS.

%define FETCH_CLASS(MODULE, CLASS)
  static PyObject *CLASS##Class = 0;
  if(!CLASS##Class) {
    PyObject *module = PyImport_ImportModule("MODULE");
    CLASS##Class = PyObject_GetAttrString(module, "CLASS");
    Py_XDECREF(module);
    if(!CLASS##Class)
      SWIG_fail;
  }
%enddef // FETCH_CLASS

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// ADD_REPR(class, func) adds a __repr__ to the swigged class.  The
// new __repr__ will call the given C++ class method, which must
// return a new std::string*.  The func must be swigged if using
// -builtin, and declared with %newobject.  ADD_REPR must appear
// *before* the class declaration in the swig file.

// If not using -builtin, ADD_REPR can appear after the declaration
// and the function does not need to be swigged. TODO PYTHON3: Check
// that.

// ADD_REPR_GENERIC uses the to_string template (from
// common/tostring.h, not std::to_string) instead of a class method,
// so it's useful as long as the class has defined operator<<.  It
// should come before the class declaration in the swig file if the
// swig file hasn't already #included common/tostring.h.
// TODO PYTHON3? Implement it for -builtin.

// Note that it's not sufficient to add a __repr__ to a base class.
// Swig will override it with a generic uninformative __repr__ in the
// derived classes unless a __repr__ is explicitly created for them.

#ifdef SWIGPYTHON_BUILTIN
%define ADD_REPR(CLASS, FUNC)
  %feature("python:slot", "tp_repr", functype="reprfunc") CLASS::FUNC
%enddef
%define ADD_STR(CLASS, FUNC)
  %feature("python:slot", "tp_str", functype="reprfunc") CLASS::FUNC
%enddef
  
#else  // not SWIGPYTHON_BUILTIN

%define ADD_REPR(CLASS, FUNC)  
%extend CLASS {
  %newobject __repr__;
    const std::string *__repr__() { // ADD_REPR
      return self->FUNC();
    }
  };
%enddef

%define ADD_REPR_GENERIC(CLASS)
%{
#include "common/tostring.h"
%}
%extend CLASS {
  %newobject __repr__;
   const std::string *__repr__() { // ADD_REPR_GENERIC
     return new std::string(to_string(*self));
   }
};
%enddef

%define ADD_STR(CLASS, FUNC)  
%extend CLASS {
  %newobject __str__;
    const std::string *__str__() { // ADD_STR
      return self->FUNC();
    }
 };
%enddef
#endif	// SWIGPYTHON_BUILTIN


%typemap(newfree) const std::string* {
  // typemap(newfree) const std::string*
  delete $1;
 }

//==||==\\==||=//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// PYTHONEXPORTABLE generates the typemaps to use when a
// PythonExportable object is returned from C++ to Python and needs to
// be turned into a derived class object.  See pythonexportable.h.
// The argument to PYTHONEXPORTABLE is the base class -- ie the class
// derived from PythonExportable.
// If Python should take ownership of the returned object, the
// function being swigged should return NewCLASS* instead of CLASS*,
// and the swig file should include a C++ typedef making NewCLASS the
// same as CLASS.

%define PYTHONEXPORTABLE(CLASS)
%typemap(out) CLASS* {
  // typemap(out) CLASS* (via PYTHONEXPORTABLE)
  if($1) {
    $result = $1->pythonObject(false);
    if(!$result)
      SWIG_fail;
  }
  else {
    Py_INCREF(Py_None);
    $result = Py_None;
  }
 }
%typemap(out) New##CLASS* {
  // typemap(out) New##CLASS* (via PYTHONEXPORTABLE)
  if($1) {
    $result = $1->pythonObject(true);
    if(!$result)
      SWIG_fail;
  }
  else {
    Py_INCREF(Py_None);
    $result = Py_None;
  }
 }
%enddef				// PYTHONEXPORTABLE

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

%typemap(out) std::string* {
  // typemap(out) std::string*
  $result = PyUnicode_FromString($1->c_str());
 }

%typemap(newfree) std::string* {
  // typemap(newfree) std::string*
  delete $1;
}
  
%typemap(out) std::string& {
  // typemap(out) std::string&
  $result = PyUnicode_FromString($1->c_str());
 }

%typemap(out) const std::string& {
  // typemap(out) const std::string&
  $result = PyUnicode_FromString($1->c_str());
 }

%typemap(out, warning="900: This typemap makes an extra copy of its input")
std::string {
  // typemap(out) std::string --- This makes an extra copy!
  // If optimal="1" were specified, then it wouldn't make the extra
  // copy, but that doesn't work with the exception typemap.
  const std::string &str = $1;
  $result = PyUnicode_FromString(str.c_str());
 }

%typemap(in) std::string& (std::string str) {
  // typemap(in) std::string&
  PyObject *ustr = PyUnicode_AsEncodedString($input, "UTF-8", "replace");
  str.assign(PyBytes_AsString(ustr));
  $1 = &str;
  Py_XDECREF(ustr);
}

%typemap(in) std::string* (std::string str) {
  // typemap(in) std::string*
  PyObject *ustr = PyUnicode_AsEncodedString($input, "UTF-8", "replace");
  str.assign(PyBytes_AsString(ustr));
  $1 = &str;
  Py_XDECREF(ustr);
}

%typemap(in) std::string {
  // typemap(in) std::string
  PyObject *ustr = PyUnicode_AsEncodedString($input, "UTF-8", "replace");
  $1 = PyBytes_AsString(ustr);
  Py_DECREF(ustr);
 }

// Typemaps for std::vectors of std::strings. (Not vectors of
// std::string*s!)

%typemap(out) std::vector<std::string> {
  // typemap(out) std::vector<std::string>
  auto sz = $1.size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<std::string>::size_type i=0; i<sz; i++) {
    PyList_SET_ITEM($result, i, PyUnicode_FromString($1[i].c_str()));
  }
}

%typemap(out) std::vector<std::string>* {
  // typemap(out) std::vector<std::string>
  auto sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<std::string>::size_type i=0; i<sz; i++) {
    PyList_SET_ITEM($result, i, PyUnicode_FromString((*$1)[i].c_str()));
  }
}

%typemap(in) std::vector<std::string>* (std::vector<std::string> svec) {
  // typemap(in) std::vector<std::string>*
  if(!PySequence_Check($input)) {
      PyErr_SetString(PyExc_TypeError,
		      "in method '$symname', expecting a list of strings");
      SWIG_fail;
    }
  int sz = PySequence_Length($input);
  if(sz > 0) {
    svec.resize(sz);
    for(int i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($input, i);
      PyObject *ustr = PyUnicode_AsEncodedString(x, "UTF-8", "replace");
      svec[i] = std::string(PyBytes_AsString(ustr));
      Py_XDECREF(ustr);
      Py_XDECREF(x);
    }
  }
  $1 = &svec;
 }

//==||==\\==||=//==||==\\==||==//==||==\\==||==//==||==\\==||==//


%typemap(newfree) std::vector<std::string>* {
  // typemap(newfree) std::vector<std::string>*
  delete $1;
}  

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

%typemap(in) PyObject *pythonCallable {
  // typemap(in) PyObject *pythonCallable
  if(!PyCallable_Check($input)) {
    std::cerr << "pythonCallable typemap: arg = " << repr_nolock($input)
	      << std::endl;
    PyErr_SetString(PyExc_TypeError,
		    "in '$symname', expected a callback python object");
    SWIG_fail;
  }
  $1 = $input;
 }

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

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

// std::vector<double> <--> [double]

// The "in" typemaps use a const vector. C++ will only see a copy of
// the python data, so it can't change it and shouldn't try.

// TODO: Do we need typemap(in) std::vector<double> (no * or &)?

%typemap(in) const std::vector<double>& (std::vector<double> vec) {
  // typemap(in) std::vector<double>&
  if(!PySequence_Check($input)) {
    PyErr_SetString(PyExc_TypeError,
		    "in '$symname', expected a list of doubles");
    SWIG_fail;
  }
  std::vector<double>::size_type sz = PySequence_Size($input);
  if(sz > 0) {
    vec.resize(sz);
    for(auto i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($input, (Py_ssize_t) i);
      if(PyFloat_Check(x))
	vec[i] = PyFloat_AsDouble(x);
      else if(PyLong_Check(x))
	vec[i] = (double) PyLong_AsLong(x);
      else {
	PyErr_SetString(PyExc_TypeError,
			    "in '$symname', expected a list of doubles");
	SWIG_fail;
      }
      Py_XDECREF(x);
    }
  }
  $1 = &vec;
}

// Because of the way swig converts references to pointers, the same
// typemaps works for both.
%typemap(in) const std::vector<double>* = const std::vector<double>&;


// This converts a Python iterable object, containing ints or floats,
// to a std::vector of doubles.  TODO: Converting to a C++ iterator
// might be useful.  The C++ iterator would have to keep a reference
// to the Python iterator and call PyIter_Next.  An advantage would be
// that no vector would need to be made.

%typemap(in) const std::vector<double> &iterable (std::vector<double> vec) {
  // typemap(int) std::vector<double> &iterable
  PyObject *iter  = PyObject_GetIter($input);
  if(!iter)
    SWIG_fail;
  while(PyObject *item = PyIter_Next(iter)) {
    if(PyFloat_Check(item))
      vec.push_back(PyFloat_AsDouble(item));
    else if(PyLong_Check(item))
      vec.push_back((double) PyLong_AsLong(item));
    else {
      PyErr_SetString(PyExc_TypeError,
		  "in '$symname', expected an iterable container of numbers");
      SWIG_fail;
    }
    Py_DECREF(item);
  }
  $1 = &vec;
 }

%typemap(in) const std::vector<double> *iterable = const std::vector<double> &iterable;

// Convert a std::vector<double>& to a list of doubles.
// TODO: convert a std::vector<double> to a python iterator?

%typemap(out) std::vector<double>* {
  // typemap(out) std::vector<double>*
  std::vector<double>::size_type sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<double>::size_type i=0; i<sz; i++) {
    PyList_SET_ITEM($result, i, PyFloat_FromDouble((*$1)[i]));
  }
 }

%typemap(out) std::vector<double>& = std::vector<double>*;

%typemap(out) std::vector<double> {
  std::vector<double>::size_type sz = $1.size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<double>::size_type i=0; i<sz; i++) {
    PyList_SET_ITEM($result, i, PyFloat_FromDouble($1[i]));
  }
 }

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// std::vector<int> <--> [long]
// std::vector<unsigned short> <--> [long]

// The "in" typemaps use a const vector. C++ will only see a copy of
// the python data, so it can't change it and shouldn't try.

// TODO: Do we need typemap(in) std::vector<int> (no * or &)?

// Define a swig macro to create the typemaps, so that we can easily
// generate them for different varieties of int.  On the Python side,
// all ints are longs.

%define MAKE_INTVEC_TYPEMAPS(TYPE)

%typemap(in) std::vector<TYPE>& (std::vector<TYPE> vec) {
  // typemap(in) std::vector<TYPE>&  (via MAKE_INTVEC_TYPEMAPS)
  if(!PySequence_Check($input)) {
    PyErr_SetString(PyExc_TypeError,
		    "in '$symname', expected a sequence.");
    SWIG_fail;
  }
  std::vector<TYPE>::size_type sz = PySequence_Size($input);
  if(sz > 0) {
    vec.resize(sz);
    for(auto i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($input, (Py_ssize_t) i);
      if(PyLong_Check(x))
	vec[i] = PyLong_AsLong(x);
      else {
	PyErr_SetString(PyExc_TypeError,
			"in '$symname', expected a TYPE sequence.");
	SWIG_fail;
      }
      Py_XDECREF(x);
    }
  }
  $1 = &vec;
}

%typemap(in) const std::vector<TYPE>* (std::vector<TYPE> vec) {
  // typemap(in) const std::vector<TYPE>* (via MAKE_INTVEC_TYPEMAPS)
  if(!PySequence_Check($input)) {
    PyErr_SetString(PyExc_TypeError, "in '$symname', expected a sequence.");
    SWIG_fail;
  }
  std::vector<TYPE>::size_type sz = PySequence_Size($input);
  vec.resize(sz);
  for(auto i=0; i<sz; i++) {
    PyObject *x = PySequence_GetItem($input, (Py_ssize_t) i);
    if(PyLong_Check(x))
      vec[i] = PyLong_AsLong(x);
    else {
      PyErr_SetString(PyExc_TypeError,
		      "in '$symname', expected a TYPE sequence.");
      SWIG_fail;
    }
    Py_XDECREF(x);
  }
  $1 = &vec;
 }

// This converts a Python iterable object, containing ints,
// to a std::vector of ints.  TODO: Converting to a C++ iterator
// might be useful.  The C++ iterator would have to keep a reference
// to the Python iterator and call PyIter_Next.  An advantage would be
// that no vector would need to be made.

%typemap(in) std::vector<TYPE> &iterable (std::vector<TYPE> vec) {
  // typemap(in) std::vector<TYPE> &iterable (via MAKE_INTVEC_TYPEMAPS)
  PyObject *iter = PyObject_GetIter($input);
  if(!iter)
    SWIG_fail;
  while(PyObject *item = PyIter_Next(iter)) {
     if(PyLong_Check(item))
      vec.push_back((TYPE) PyLong_AsLong(item));
    else {
      PyErr_SetString(PyExc_TypeError,
		  "in '$symname, expected an iterable container of TYPE.");
      SWIG_fail;
    }
    Py_DECREF(item);
  }
  $1 = &vec;
 }

%typemap(in) std::vector<TYPE> &iterable (std::vector<TYPE> vec) {
  // typemap(in) std::vector<TYPE> &iterable (via MAKE_INTVEC_TYPEMAPS)
  PyObject *iter = PyObject_GetIter($input);
  if(!iter)
    SWIG_fail;
  while(PyObject *item = PyIter_Next(iter)) {
     if(PyLong_Check(item))
      vec.push_back((TYPE) PyLong_AsLong(item));
    else {
      PyErr_SetString(PyExc_TypeError,
		  "in '$symname, expected an iterable container of TYPE.");
      SWIG_fail;
    }
    Py_DECREF(item);
  }
  $1 = &vec;
 }
//%typemap(in) const std::vector<TYPE> *iterable = const std::vector<TYPE> &iterable;

// Convert a std::vector<int>& to a list of longs.
// TODO: convert a std::vector<int> to a python iterator?

%typemap(out) std::vector<TYPE>* {
  // typemap(out) std::vector<TYPE>*  (via MAKE_INTVEC_TYPEMAPS)
  std::vector<TYPE>::size_type sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<TYPE>::size_type i=0; i<sz; i++) {
    PyList_SET_ITEM($result, i, PyLong_FromLong((*$1)[i]));
  }
}

%typemap(newfree) std::vector<TYPE>* {
  // typemap(newfree) std::vector<TYPE>* (via MAKE_INTVEC_TYPEMAPS)
  delete $1;
}

%typemap(out) std::vector<TYPE>& = std::vector<TYPE>*;

%typemap(out) std::vector<TYPE> {
  // typemap(out) std::vector<TYPE>  (via MAKE_INTVEC_TYPEMAPS)
  std::vector<TYPE>::size_type sz = $1.size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<TYPE>::size_type i=0; i<sz; i++) {
    PyList_SET_ITEM($result, i, PyLong_FromLong($1[i]));
  }
}

%enddef // MAKE_INTVEC_TYPEMAPS

MAKE_INTVEC_TYPEMAPS(int)
MAKE_INTVEC_TYPEMAPS(unsigned short)


//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

 // [String] -> std::vector<char*>*

%typemap(in) std::vector<char*> *argv (std::vector<char*> argh,
				       std::vector<PyObject*> ustrs)
{
  // typemap(in) std::vector<char*> *argv
  if(!PySequence_Check($input)) {
    PyErr_SetString(PyExc_TypeError,
		    "in '$symname', expected a list of strings.");
    SWIG_fail;
  }
  std::vector<char*>::size_type sz = PySequence_Size($input);
  argh.resize(sz);
  for(std::vector<char*>::size_type i=0; i<sz; i++) {
    PyObject *str = PySequence_GetItem($input, (Py_ssize_t) i);
    PyObject *ustr = PyUnicode_AsEncodedString(str, "UTF-8", "replace");
    argh[i] = PyBytes_AsString(ustr);
    // argh stores pointers to data that will be deleted as soon as
    // ustr is decreffed.  Store ustr and don't decref it until the
    // called function returns.
    ustrs.push_back(ustr);
    Py_XDECREF(str);
  }
  $1 = &argh;
}

%typemap(freearg) const std::vector<char*> *argv {
  // typemap(freearg) std::vector<char*> *argv
  for(PyObject *ustr: ustrs$argnum)
    Py_XDECREF(ustr);
}

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// std::vector<TYPE*>  <--> [TYPE]

// MAKE_LISTVEC_TYPEMAPS defines unnamed in, out, and newfree typemaps
// for converting between a C++ std::vector* of TYPE*s and a list of
// swigged TYPEs.  It does not copy the objects -- the swigged
// pointers point to the original C++ objects.

// out: TYPEVec *      (transfers ownership of TYPE objects to python)
// out: TYPERefVec *   (does not transfer ownership to python)
// out: TYPESubClassVec * (uses pythonexportable, transfers ownership)
// out: TYPESubClassRefVec * (uses pythonexportable, doesn't transfer ownership)
// in:  TYPEVec*

// If you use std::vector<TYPE*>* as the return type of a function ,
// it will be interpreted as TYPEVec, and Python will take ownership
// of the objects.  You need to explicitly use TYPERefVec* (eg,
// CoordRefVec if TYPE is Coord) as a return type if you don't want
// ownership of the objects to be transferred to Python.


%define MAKE_LISTVEC_TYPEMAPS(TYPE)

%{
  typedef std::vector<TYPE*> TYPE##Vec;
  typedef std::vector<TYPE*> TYPE##RefVec;
  typedef std::vector<TYPE*> TYPE##SubClassVec;
  typedef std::vector<TYPE*> TYPE##SubClassRefVec;
%}

%typemap(out) TYPE##Vec* {
  // typemap(out) TYPE##Vec* via MAKE_LISTVEC_TYPEMAPS for TYPE
  TYPE##Vec::size_type sz = $1->size();
  // assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <=PY_SSIZE_T_MAX);
  $result = PyList_New((Py_ssize_t) sz);
  for(TYPE##Vec::size_type i=0; i<sz; i++) {
    PyObject *tmp = SWIG_NewPointerObj(SWIG_as_voidptr((*$1)[i]),
				       $descriptor(TYPE*),
				       SWIG_POINTER_OWN);
    PyList_SET_ITEM($result, (Py_ssize_t) i, tmp);
  }
}

%typemap(out) TYPE##RefVec* {
  // typemap(out) TYPE##RefVec* via MAKE_LISTVEC_TYPEMAPS for TYPE
  TYPE##RefVec::size_type sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(TYPE##RefVec::size_type i=0; i<sz; i++) {
    PyObject *tmp = SWIG_NewPointerObj(SWIG_as_voidptr((*$1)[i]),
				       $descriptor(TYPE*),
				       0); // don't take ownership
    PyList_SET_ITEM($result, (Py_ssize_t) i, tmp);
  }
 }

%typemap(out) TYPE##SubClassVec* {
  // typemap(out) TYPE##SubClassVec* via MAKE_LISTVEC_TYPEMAPS for TYPE
  TYPE##SubClassVec::size_type sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(TYPE##SubClassVec::size_type i=0; i<sz; i++) {
    PyObject *tmp = (*$1)[i]->pythonObject(true); // take ownership
    PyList_SET_ITEM($result, (Py_ssize_t) i, tmp);
  }
 }

%typemap(out) TYPE##SubClassRefVec* {
  // typemap(out) TYPE##SubClassRefVec* via MAKE_LISTVEC_TYPEMAPS for TYPE
  TYPE##SubClassVec::size_type sz = $1->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(TYPE##SubClassVec::size_type i=0; i<sz; i++) {
    PyObject *tmp = (*$1)[i]->pythonObject(false); // don't take ownership
    PyList_SET_ITEM($result, (Py_ssize_t) i, tmp);
  }
 }

%typemap(newfree) TYPE##Vec* {
  // typemap(newfree) TYPE##Vec* via MAKE_LISTVEC_TYPEMAPS for TYPE
  delete $1;
}

%typemap(newfree) TYPE##RefVec* {
  // typemap(newfree) TYPE##RefVec* via MAKE_LISTVEC_TYPEMAPS for TYPE
  delete $1;
}

%typemap(in) TYPE##Vec* (TYPE##Vec v) {
  // typemap(in) TYPE##Vec* via MAKE_LISTVEC_TYPEMAPS for TYPE
  if(!PyList_Check($input)) {
    PyErr_SetString(PyExc_TypeError, "in '$symname', expected a list of TYPE.");
    SWIG_fail;
  }
  TYPE##Vec::size_type sz = PyList_Size($input);
  v.resize(sz);
  for(TYPE##Vec::size_type i=0; i<sz; i++) {
    void *itemptr = 0;
    int res = SWIG_ConvertPtr(PyList_GET_ITEM($input, i), &itemptr,
			      $descriptor(TYPE*), 0);
    if(!SWIG_IsOK(res)) {
      PyErr_SetString(PyExc_TypeError,
		      "in method '$symname', expecting list of TYPEs");
      SWIG_fail;
    }
    v[i] = reinterpret_cast<TYPE*>(itemptr);
  }
    $1 = &v;
 }

%enddef // MAKE_LISTVEC_TYPEMAPS

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// std::vector<Coord>*  <-->  [Point]

%typemap(in) std::vector<Coord> *PointList (std::vector<Coord> v) {
  // typemap(in) std::vector<Coord>*
  if(!PyList_Check($input)) {
    PyErr_SetString(PyExc_TypeError,
		    "in method '$symname', expecting list of Points.");
    SWIG_fail;
  }
  std::vector<Coord>::size_type sz = PyList_Size($input);
  v.resize(sz);
  for(std::vector<Coord>::size_type i=0; i<sz; i++) {
    PyObject *point = PyList_GET_ITEM($input, (Py_ssize_t) i);
    if(!point)
      SWIG_fail;
    PyObject *px = PyObject_GetAttrString(point, "x");
    if(!px)
      SWIG_fail;
    v[i][0] = PyFloat_AsDouble(px);
    Py_XDECREF(px);
    PyObject *py = PyObject_GetAttrString(point, "y");
    if(!py)
      return NULL;
    v[i](1) = PyFloat_AsDouble(py);
    Py_XDECREF(py);
  }
  $1 = &v;
}

%typemap(out) std::vector<Coord>* {
  // typemap(out) std::vector<Coord>*
  std::vector<Coord>::size_type sz = $1->size();
  FETCH_CLASS(ooflib.common.primitives, Point);
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<Coord>::size_type i=0; i<sz; i++) {
    const Coord &c = (*$1)[i];
    PyObject *point = PyObject_CallFunction(PointClass, "dd", c(0), c(1));
    PyList_SET_ITEM($result, (Py_ssize_t) i, point); // Steals reference.
  }
}

%typemap(newfree) std::vector<Coord>* {
  delete $1;
}

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// std::vector<ICoord>*  <-->  [iPoint] 

%typemap(in) std::vector<ICoord> *iPointList (std::vector<ICoord> v) {
  // typemap(in) std::vector<ICoord>* iPointList
  if(!PyList_Check($input)) {
    PyErr_SetString(PyExc_TypeError,
		    "in method '$symname', expecting list of iPoints.");
    SWIG_fail;
  }
  std::vector<ICoord>::size_type sz = PyList_Size($input);
  v.resize(sz);
  for(std::vector<ICoord>::size_type i=0; i<sz; i++) {
    PyObject *point = PyList_GET_ITEM($input, (Py_ssize_t) i);
    if(!point)
      SWIG_fail;
    PyObject *px = PyObject_GetAttrString(point, "x");
    if(!px)
      SWIG_fail;
    v[i][0] = PyLong_AsLong(px);
    Py_XDECREF(px);
    PyObject *py = PyObject_GetAttrString(point, "y");
    if(!py)
      return NULL;
    v[i](1) = PyLong_AsLong(py);
    Py_XDECREF(py);
  }
  $1 = &v;
 }

%typemap(out) std::vector<ICoord>* {
  // typemap(out) std::vector<ICoord>*
  std::vector<ICoord>::size_type sz = $1->size();
  FETCH_CLASS(ooflib.common.primitives, iPoint);
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<ICoord>::size_type i=0; i<sz; i++) {
    const ICoord &c = (*$1)[i];
    PyObject *ipoint = PyObject_CallFunction(iPointClass, "ii", c(0), c(1));
    PyList_SET_ITEM($result, (Py_ssize_t) i, ipoint); // Steals reference.
  }
 }

%typemap(newfree) std::vector<ICoord>* {
  // typemap(newfree) std::vector<ICoord>*
  delete $1;
}

//==||==\\==||=//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// C++ ICoord --> Python iPoint
// C++ Coord  --> Python Point

// TODO: Are these typemaps necessary?  We can handle Coords directly
// in Python, and do so in lots of places in the code.  Including this
// typemap means that we're mixing Coords and Points in a mostly
// uncontrolled fashion.  For example, 2*coord.Coord(1.,2.) returns a
// Point, not a Coord, because this typemap is applied to the result
// of Coord.__rmul__()

// Also, these typemaps make an extra copy of the object they're
// wrapping.  If possible, returning a const reference is preferable.

// Coord and ICoord don't have a swigged default constructor, so swig
// thinks it has to use the SwigValueWrapper mechanism when a function
// returns a Coord or ICoord by value.  The classes *do* have default
// constructors in C++, so we need to tell swig not to use
// SwigValueWrapper.  Using SwigValueWrapper messes up the typemaps.
%feature("novaluewrapper") Coord;
%feature("novaluewrapper") ICoord;

%typemap(out) ICoord {
  // typemap(out) ICoord
  FETCH_CLASS(ooflib.common.primitives, iPoint);
  $result = PyObject_CallFunction(iPointClass, "ii", ($1)(0), ($1)(1));
 }

%typemap(out) Coord {
  // typemap(out) Coord
  FETCH_CLASS(ooflib.common.primitives, Point);
  $result = PyObject_CallFunction(PointClass, "dd", ($1)(0), ($1)(1));
 }

// Python iPoint --> C++ ICoord*
// Python  Point --> C++ Coord*

%typemap(in) ICoord *iPoint (ICoord ic) {
  // typemap(in) ICoord *iPoint
  PyObject *x = PyObject_GetAttrString($input, "x");
  if(!x) {
    PyErr_SetString(PyExc_TypeError, "in '$symname', expected an iPoint.");
    SWIG_fail;
  }
  PyObject *y = PyObject_GetAttrString($input, "y");
  if(!y) {
    PyErr_SetString(PyExc_TypeError, "in '$symname', expected an iPoint.");
    SWIG_fail;
  }
  ic(0) = PyLong_AsLong(x);
  ic(1) = PyLong_AsLong(y);
  Py_XDECREF(x);
  Py_XDECREF(y);
  $1 = &ic;
 }

%typemap(in) Coord *Point (Coord c) {
  // typemap(in) Coord *Point
  PyObject *x = PyObject_GetAttrString($input, "x");
  if(!x) {
    PyErr_SetString(PyExc_TypeError, "in '$symname', expected a Point.");
    SWIG_fail;
  }
  PyObject *y = PyObject_GetAttrString($input, "y");
  if(!y) {
    PyErr_SetString(PyExc_TypeError, "in '$symname', expected a Point.");
    SWIG_fail;
  }
  c(0) = PyFloat_AsDouble(x);
  c(1) = PyFloat_AsDouble(y);
  Py_XDECREF(x);
  Py_XDECREF(y);
  $1 = &c;
 }

%typemap(in) const Coord &Point = Coord *Point;

//==||==\\==||=//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// Coord *Sequence: Python 2-tuple --> C++ Coord
// ICoord *Sequence: Python 2-tuple --> C++ ICoord

// TODO: Change the name of the typemaps. "Sequence" is too vague

%typemap(in) Coord *Sequence (Coord c) {
  // typemap(in) Coord *Sequence
  if(!(PySequence_Check($input) && PySequence_Length($input) == 2)) {
    PyErr_SetString(PyExc_TypeError,
		    "in '$symname', expected sequence of length 2.");
    SWIG_fail;
  }
  PyObject *x = PySequence_GetItem($input, (Py_ssize_t) 0);
  PyObject *y = PySequence_GetItem($input, (Py_ssize_t) 1);
  c(0) = PyFloat_AsDouble(x);
  c(1) = PyFloat_AsDouble(y);
  Py_XDECREF(x);
  Py_XDECREF(y);
  $1 = &c;
 }

%typemap(in) ICoord *Sequence (ICoord ic) {
  // typemap(in) Coord *Sequence
  if(!(PySequence_Check($input) && PySequence_Length($input) == 2)) {
    PyErr_SetString(PyExc_TypeError,
		    "in '$symname', expected sequence of length 2.");
    SWIG_fail;
  }
  PyObject *x = PySequence_GetItem($input, (Py_ssize_t) 0);
  PyObject *y = PySequence_GetItem($input, (Py_ssize_t) 1);
  ic(0) = PyLong_AsLong(x);
  ic(1) = PyLong_AsLong(y);
  Py_XDECREF(x);
  Py_XDECREF(y);
  $1 = &ic;
 }

//==||==\\==||=//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// OOF's global exception typemap, for taking exceptions out of C++
// and throwing the corresponding exceptions in Python.  See the
// comment in threadstate.C about threading_enabled.

%exception {
  try {
    installSignals;
    Python_Thread_Allow allow_threads(true);
    //=\\=//
    $action;
    //=\\=//
    allow_threads.end();
  }
  catch (PythonError &p) {
    // In this case, the Python error indicator is already set.  See
    // pythonErrorRelay in ooferror.C.
    restoreSignals;
    SWIG_fail;
  }
  catch (ErrError &e) {
    restoreSignals;
    // pyconverter is common.ooferror.pyErrorCallback.  It raises an
    // Python exception that wraps the C++ exception.  Use
    // pythonObject from PythonExportable so that a derived class
    // object is wrapped, and have Python take ownership of a copy.
    PyObject_CallFunctionObjArgs(e.pyconverter,
				 e.clone()->pythonObject(true),
				 NULL);
    SWIG_fail;
  }
  catch (...) {
    // Caught a C++ exception that wasn't already handled and
    // converted into an ErrError. This means that something is really
    // wrong.
    restoreSignals;
    PyObject_CallFunction(
	  ErrError::pyconverter, "s",
	  "ErrPyProgrammingError('Caught an unexpected C++ exception!')");
    SWIG_fail;
  }
  restoreSignals;
 }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Typemap used by the transitionPoint functions to pass out both its
// status and the transition point, if valid.

// This scheme for handling argout parameters by concatenating tuples
// is from https://www.swig.org/Doc4.0/Python.html#Python_nn61.

%typemap(argout) Coord *argout_Point {
  // typemap(argout) Coord *argout_Point
  // Get the Point class
  FETCH_CLASS(ooflib.common.primitives, Point);
  // Create a Point object from the Coord
  PyObject *point = PyObject_CallFunction(PointClass, "dd",
					  (*$1)(0), (*$1)(1));
  if(!$result || $result == Py_None) {
    // Nothing else is being returned (yet).
    $result = point;
  }
  else {
    // Something else is already being returned.
    if(!PyTuple_Check($result)) {
      // The previously returned object is not a tuple.  Create a
      // tuple and put the old result into it.
      PyObject *other = $result;
      $result = PyTuple_New(1);
      PyTuple_SET_ITEM($result, 0, other); // steals a reference
    }
    // Add the new output to the tuple, by concatenating tuples.
    PyObject *temptuple = PyTuple_New(1);
    PyTuple_SET_ITEM(temptuple, 0, point); // steals a reference
    PyObject *oldresult = $result;
    $result = PySequence_Concat(oldresult, temptuple);
    Py_XDECREF(temptuple);
    Py_XDECREF(oldresult);
  }
 }

%typemap(in, numinputs=0) Coord *argout_Point (Coord tmp) {
  // typemap(in, numinputs=0) Coord *argout_Point
  $1 = &tmp;
 }


#endif // COMMONTYPEMAPS_SWG

