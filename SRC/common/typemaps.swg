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

// TODO PYTHON3: Swig's -builtin doesn't work because it's not
// compatible with the %exception typemap.  If there's ever a fix for
// that, go through all the swigged classes and use python slots
// whereever possible.

// TODO: Change the xxxxxVec* "in" typemaps so that they accept any
// Python iterator, not just lists and tuples.

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

%{
#define SWIG_FILE_WITH_INIT
#include <oofconfig.h>
#include "common/cdebug.h"
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

// Swig macros for adding __repr__s to C++ classes.

// ADD_REPR(class, func) adds a __repr__ to the swigged class.  The
// new __repr__ will call the given C++ class method, which must
// return a new std::string*.  The func must be swigged if using
// -builtin, and declared with %newobject.  ADD_REPR must appear
// *before* the class declaration in the swig file.

// If not using -builtin, ADD_REPR can appear after the declaration
// and the function does not need to be swigged.

// ADD_REPR_GENERIC uses the tostring template (from
// common/tostring.h, not std::to_string) instead of a class method,
// so it's useful as long as the class has defines operator<<.  It
// should come before the class declaration in the swig file if the
// swig file hasn't already #included common/tostring.h.
// TODO PYTHON3? Implement it for -builtin.

// Note that it's not sufficient to add a __repr__ to a base class and
// hope to have it used for the derived classes.  Swig will override
// the base class __repr__ with a generic uninformative __repr__ in
// the derived classes unless a __repr__ is explicitly created for
// them.

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
     return new std::string(tostring(*self));
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
// same as CLASS.  The typedef is not generated automatically here
// just in case NewCLASS is already defined.

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

// Typemaps for strings and vectors of strings.

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
		    "in '$symname', expected a callable python object");
    SWIG_fail;
  }
  $1 = $input;
 }

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// std::vector<double> <--> [double]

// The "in" typemaps use a const vector. C++ will only see a copy of
// the python data, so it can't change it and shouldn't try.

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
// to a std::vector of doubles.

// TODO: If copying the data uses too much memory, converting to a C++
// iterator might be useful.  The C++ iterator would have to keep a
// reference to the Python iterator and call PyIter_Next.  It would be
// slow.

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

// Convert a std::vector<double>& to a list of doubles.  Conversion to
// a python iterator is not recommended unless there are memory
// constraints, because iterating would require a lot of swig API
// calls.

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
// to a std::vector of ints.

// TODO? Converting to a C++ iterator might be useful.  The C++
// iterator would have to keep a reference to the Python iterator and
// call PyIter_Next.  An advantage would be that no vector would need
// to be made.

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

// Because MAKE_LISTVEC_TYPEMAPS adds typedefs to C++ code, it should
// be invoked in the swig file in which the typemap is used, not where
// the TYPE is defined (if it's a different file).  The file where the
// TYPE is defined should be %imported into the file where it's used,
// and the %import will ignore the C++ code containing the typedefs.

// It is possible to add a typemap that doesn't actually create a
// Python list, but instead swigs the C++ vector's iterators.  This
// was tried, but it was much slower than copying vector to a list,
// since it requires swig calls for every list item.  But if memory is
// an issue, that would be good approach.  To do that, swig the
// vector, exposing only its begin and end methods, which return
// iterators. The iterators need operator++, operator!=, and operator*
// defined in python and renamed "increment", "dereference", and
// __ne__.  Then monkeypatch an __iter__ method on the swigged vector
// that looks like this:
//   def _vector___iter__(self):
//      here = self.begin()
//      end = self.end()
//      while here != end:
//         yield here.dereference()
//         here.increment()
// The current code does *not* do this.

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

//==||==\\==||=//==||==\\==||==//==||==\\==||==//==||==\\==||==//

// OOF's global exception typemap, for taking exceptions out of C++
// and throwing the corresponding exceptions in Python.  See the
// comment in threadstate.C about threading_enabled.

%exception {
  // %exception typemap
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

#endif // COMMONTYPEMAPS_SWG

