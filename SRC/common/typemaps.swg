// -*- C++ -*-
// $RCSfile: typemaps.swg,v $
// $Revision: 1.80 $
// $Author: langer $
// $Date: 2014/12/31 01:32:23 $

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

// TODO: Change the xxxxxVec* "in" typemaps so that they accept any
// Python iterator, not just lists and tuples.

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// GENERIC TYPEMAPS

// DON'T ADD TYPEMAPS TO THIS FILE WITHOUT ADDING THEM TO THIS LIST

// In these comments, "[x]" means a Python list of objects of type x

// Unnamed typemaps defined in this file:

// in		CColor		Color -> CColor*
// in		CoordVec*	[Coord] -> std::vector<Coord*>*
// in		DoubleList*	[Float] -> std::vector<double>*
// in		IntVec*		[Int] -> std::vector<int>*
// in		ShortVec*	[Int] -> std::vector<unsigned short>*
// in		PyObject *
// in		StringVec*	[Python string]->std::vector<std::string>
// newfree	DoubleList*
// newfree	ICoordVec*	frees std::vector<ICoord>* when tagged by %new
// newfree	IntVec*
// newfree	PointVec*
// newfree	ShortVec*
// newfree	StringVec*
// newfree      string*
// out		CColor		CColor -> RGBColor
// out		Coord		Coord -> Point
// out		Coord&		Coord* -> Point
// out		Coord*		Coord& -> Point
// out		CoordVec*	std::vector<Coord*>* -> [Coord]
// newfree      CoordVec*
// out		DoubleList*	std::vector<double>* -> [Float]
// out		ICoord		ICoord -> iPoint
// out		ICoordVec*	std::vector<ICoord>* -> [iPoint]
// out		IntVec*		std::vector<int>* -> [Int]
// out		ShortVec*	std::vector<unsigned short>* -> [Int]
// out		PointVec*	std::vector<Coord>* -> [Point]
// out          Progress*       Progress* -> derived classes
// out		PyObject*	
// out		StringVec*	std::vector<std::string>->[Python string]
// out		string*		C++ string pointer -> Python string
// out          string&         C++ string reference -> Python string.
// out          string          Forbidden!  It creates memory leaks.

// Named typemaps defined in this file:

// in		PyObject *pythonCallable
// in		PointVec* PointList	[Point] -> std::vector<Coord>*
// in		ICoordVec *iPointList   [iPoint] -> std::vector<ICoord>*	
// in		ICoordVec *iTupleList   [(Int, Int)] -> std::vector<ICoord>*
// in		ICoord *iPoint		iPoint -> ICoord*
// in		Coord *Point		Point -> Coord*
// in		Coord *Sequence		(Float,Float) or [Float,Float] -> Coord*
// in		ICoord *Sequence	(Int,Int) or [Int,Int] -> ICoord*
// in		CharPtrVec *argv		[string] -> std::vector<char*>

// Typemaps are also used to convert C++ base class pointers to Python
// derived types, by the mechanism described in pythonexportable.h.

// out		Node*
// out		Property*
// out          cskel_OutPoint

// Useful typemaps for extracting std::string return values and members.
//typedef char *string;


%{
#include <oofconfig.h>
#include "common/cdebug.h"
#include "common/geometry.h"
#include "common/ooferror.h"
#include "common/pythonlock.h"
#include "common/threadstate.h"
#include <Python.h>	
#include <string>
#include <vector>
typedef std::vector<Coord*> CoordVec;
typedef std::vector<Coord> PointVec;
typedef std::vector<ICoord> ICoordVec;
typedef std::vector<char*> CharPtrVec;
typedef std::vector<double> DoubleList;
typedef std::vector<int> IntVec;
typedef std::vector<std::string> StringVec;
typedef std::vector<unsigned short> ShortVec;
using std::string;
%}




%typemap(python,out) string& {
  // typemap(python, out) string&
  $target = PyString_FromString($source->c_str());
}

%typemap(python,out) string {
  // This typemap should not be used, since swig will use "new string"
  // to copy the output, and won't delete it.

  // typemap(python, out) string
  //$target = PyString_FromString($source->c_str());
  $target = something_that_will_fail_to_compile();
}

%typemap(python, newfree) string* {
  // typemap(python, newfree) string*
  delete $source;
}

// Useful typemap for passing a python callable
%typemap(python,in) PyObject *pythonCallable {
  if(!PyCallable_Check($source)) {
    PyErr_SetString(PyExc_TypeError,"Need a callable object!");
    return NULL;
  }
  $target = $source;
}


// typemap for passing "self" into a PythonExportable/PythonNative
// constructor.  It would seem that this shouldn't be necessary, but
// without it SWIG doesn't do the right thing.
%typemap(python,in) PyObject * {
  // typemap(python, in) PyObject*
  $target = $source;
}

%typemap(python, out) PyObject * {
  // typemap(python, out) PyObject*
  $target = $source;
}

// TODO LATER:  Investigate whether all colors should be SWIG'd CColors.
%typemap(python, in) CColor* (CColor clr) {
  PyObject *red = PyObject_CallMethod($source, (char*)"getRed", NULL);
  PyObject *grn = PyObject_CallMethod($source, (char*)"getGreen", NULL);
  PyObject *blu = PyObject_CallMethod($source, (char*)"getBlue", NULL);
  PyObject *alf = PyObject_CallMethod($source, (char*)"getAlpha", NULL); // alien life form
  clr.setRed(PyFloat_AsDouble(red));
  clr.setGreen(PyFloat_AsDouble(grn));
  clr.setBlue(PyFloat_AsDouble(blu));
  clr.setAlpha(PyFloat_AsDouble(alf));
  Py_XDECREF(red);
  Py_XDECREF(grn);
  Py_XDECREF(blu);
  Py_XDECREF(alf);
  $target = &clr;
}


%typemap(python, out) CColor {
  static PyObject *RGBAColorClass = 0;
  if(!RGBAColorClass) {
    PyObject *module = PyImport_ImportModule("ooflib.common.color");
    RGBAColorClass = PyObject_GetAttrString(module, "RGBAColor");
    Py_XDECREF(module);
    if(!RGBAColorClass) return 0;
  }
  PyObject *rgbaargs = Py_BuildValue("dddd", $source->getRed(),
				    $source->getGreen(),
				    $source->getBlue(),
				    $source->getAlpha());
  delete $source;
  $target = PyObject_CallObject(RGBAColorClass, rgbaargs);
  Py_XDECREF(rgbaargs);
}

%typemap(python,in) DoubleList* (DoubleList vec) {
  if(!PySequence_Check($source)) {
    PyErr_SetString(PyExc_TypeError,"Error in vector<double>* typemap. Expected a sequence of numbers!");
    return 0;
  }
  DoubleList::size_type sz = Py_SAFE_DOWNCAST(PySequence_Size($source),
					     Py_ssize_t, DoubleList::size_type);
  if(sz > 0) {
    vec.resize(sz);
    for(DoubleList::size_type i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($source, (Py_ssize_t) i);
      if(PyFloat_Check(x))
	vec[i] = PyFloat_AsDouble(x);
      else if(PyInt_Check(x))
	vec[i] = (double) PyInt_AsLong(x);
      else {
	PyErr_SetString(PyExc_TypeError, "Error in vector<double>* typemap.  Expected a sequence of numbers.");
	return 0;
      }
      Py_XDECREF(x);
    }
  }
  $target = &vec;
}

%typemap(python, out) DoubleList* {
  // typemap(python, out) DoubleList*
  DoubleList::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(DoubleList::size_type i=0; i<sz; i++)
    PyList_SET_ITEM($target, (Py_ssize_t) i, PyFloat_FromDouble((*$source)[i]));
}

%typemap(python, newfree) DoubleList* {
  // typemap(python, newfree) DoubleList*
  delete $source;
}

%typemap(python, in) IntVec* (IntVec vec) {
  if(!PySequence_Check($source)) {
    PyErr_SetString(PyExc_TypeError, "Type error in vector<int>* typemap. Python sequence of Ints required.");
    return 0;
  }
  IntVec::size_type sz = Py_SAFE_DOWNCAST(PySequence_Length($source),
					  Py_ssize_t, IntVec::size_type);
  if(sz > 0) {
    vec.resize(sz);
    for(IntVec::size_type i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($source, (Py_ssize_t) i);
      vec[i] = PyInt_AsLong(x);
      Py_XDECREF(x);
    }
  }
  $target = &vec;
}

%typemap(python, out) IntVec* {
  // typemap(python, out) IntVec*
  IntVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(IntVec::size_type i=0; i<sz; i++)
    PyList_SET_ITEM($target, (Py_ssize_t) i, PyInt_FromLong((*$source)[i]));
}

%typemap(python, newfree) IntVec* {
  delete $source;
}

%typemap(python, in) ShortVec* (ShortVec vec) {
  if(!PySequence_Check($source)) {
    PyErr_SetString(PyExc_TypeError, "Type error in vector<unsigned char>* typemap.  Python sequence of Ints required.");
    return 0;
  }
  ShortVec::size_type sz = Py_SAFE_DOWNCAST(PySequence_Length($source),
					    Py_ssize_t, ShortVec::size_type);
  if(sz > 0) {
    vec.resize(sz);
    for(ShortVec::size_type i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($source, (Py_ssize_t) i);
      vec[i] = (unsigned short) PyInt_AsLong(x);
      Py_XDECREF(x);
    }
  }
  $target = &vec;
}

%typemap(python, out) ShortVec* {
  // typemap(python, out) ShortVec*
  ShortVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(ShortVec::size_type i=0; i<sz; i++) {
    PyList_SET_ITEM($target, (Py_ssize_t) i, PyInt_FromLong((*$source)[i]));
  }
}

%typemap(python, newfree) ShortVec* {
  delete $source;
}


%typemap(python, in) CharPtrVec *argv (CharPtrVec argh) {
  if(!PySequence_Check($source)) {
    PyErr_SetString(PyExc_TypeError, "Type error in argv typemap.  Expected list of strings.");
    return 0;
  }
  CharPtrVec::size_type sz = 
    Py_SAFE_DOWNCAST(PySequence_Length($source),
		     Py_ssize_t, CharPtrVec::size_type);
  argh.resize(sz);
  for(CharPtrVec::size_type i=0; i<sz; i++) {
    PyObject *str = PySequence_GetItem($source, (Py_ssize_t) i);
    argh[i] = PyString_AsString(str);
    Py_XDECREF(str);
  }
  $target = &argh;
}

// This is an example of the Right Way To Do Copy-Out Typemaps:
// The wrapped function should return a pointer to a vector of 
// pointers to the things being passed out.  Ownership of the
// objects will pass to Python, and the vector itself will be
// freed by the newfree typmap which follows.
// See also the perimeter typemap in element.swg. 

%typemap(python,out) CoordVec* {
  CoordVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <=PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  char _ptemp[128];
  for(std::vector<Coord*>::size_type i=0; i<$source->size();i++) {
    SWIG_MakePtr(_ptemp, (char*)(*$source)[i], "_Coord_p");
    PyList_SET_ITEM($target, (Py_ssize_t) i, Py_BuildValue("s",_ptemp));
  }
}

%typemap(python, newfree) CoordVec* {
  delete $source;
}

// Convert a list of swigged Coords to a std::vector of Coord*s.
// Using a vector of Coord*s instead of Coords eliminates a copy,
// since the Coords already exist in C++, and SWIG has just stored
// pointers to them.
%typemap(python,in) CoordVec* (CoordVec v) {
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError, "Type error in CoordVec* typemap. Python list required.");
    return NULL;
  }
  CoordVec::size_type sz = Py_SAFE_DOWNCAST(PyList_Size($source),
					    Py_ssize_t, CoordVec::size_type);
  v.resize(sz);
  for(CoordVec::size_type i=0; i<sz; i++) {
    PyObject *strobj = PyObject_GetAttrString(PyList_GET_ITEM($source,
							      (Py_ssize_t) i),
					      "this");
    if(!strobj)
      return NULL;
    char *str = PyString_AsString(strobj);
    Py_XDECREF(strobj);
    Coord *c;
    SWIG_GetPtr(str, (void**) &c, "_Coord_p");
    v[i] = c;
  }
  $target = &v;
}

// Convert a list of Python Points to a std::vector of Coords.
%typemap(python, in) PointVec *PointList (PointVec v) {
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
		    "Type error in PointVec typemap.  Python List required.");
    return NULL;
  }
  PointVec::size_type sz = Py_SAFE_DOWNCAST(PyList_Size($source),
					     Py_ssize_t, PointVec::size_type);
  v.resize(sz);
  for(PointVec::size_type i=0; i<sz; i++) {
    PyObject *point = PyList_GET_ITEM($source, (Py_ssize_t) i);
    if(!point)
      return 0;
    PyObject *px = PyObject_GetAttrString(point, "x");
    if(!px)
      return NULL;
    v[i](0) = PyFloat_AsDouble(px);
    Py_XDECREF(px);
    PyObject *py = PyObject_GetAttrString(point, "y");
    if(!py)
      return NULL;
    v[i](1) = PyFloat_AsDouble(py);
    Py_XDECREF(py);
#ifdef DIM_3
    PyObject *pz = PyObject_GetAttrString(point, "z");
    if(!pz)
      return NULL;
    v[i](2) = PyFloat_AsDouble(pz);
    Py_XDECREF(pz);
#endif
  }
  $target = &v;
}

// Convert a std::vector<Coord>* to a Python list of Points.
%typemap(python, out) PointVec* {
  // typemap(python, out) PointVec*
  PointVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz < PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  static PyObject *PointClass = 0;
  if(!PointClass) {
    PyObject *module = PyImport_ImportModule("ooflib.common.primitives");
    PointClass = PyObject_GetAttrString(module, "Point");
    Py_XDECREF(module);
    if(!PointClass) return 0;
  }
  for(PointVec::size_type i=0; i<sz; i++) {
    Coord &c = (*$source)[i];
#ifndef DIM_3
    PyObject *xyargs = Py_BuildValue("dd", c(0), c(1));
#else
    PyObject *xyargs = Py_BuildValue("ddd", c(0), c(1), c(2));
#endif
    PyObject *point = PyObject_CallObject(PointClass, xyargs);
    PyList_SET_ITEM($target, (Py_ssize_t) i, point); // Steals reference.
    Py_XDECREF(xyargs);
  }
}

%typemap(python, newfree) PointVec* {
  delete $source;
}

// Convert a list of Python iPoints to a std::vector of ICoords.
%typemap(python, in) ICoordVec *iPointList (ICoordVec v) {
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
		    "Type error in ICoordVec typemap. Python list required.");
    return NULL;
  }
  ICoordVec::size_type sz = Py_SAFE_DOWNCAST(PyList_Size($source),
					     Py_ssize_t, ICoordVec::size_type);
  v.resize(sz);
  for(ICoordVec::size_type i=0; i<sz; i++) {
    PyObject *ipoint = PyList_GET_ITEM($source, (Py_ssize_t) i);
    if(!ipoint)
      return 0;
    PyObject *px = PyObject_GetAttrString(ipoint, "x");
    if(!px) return NULL;
    v[i](0) = PyInt_AsLong(px);
    Py_XDECREF(px);
    PyObject *py = PyObject_GetAttrString(ipoint, "y");
    if(!py) return NULL;
    v[i](1) = PyInt_AsLong(py);
    Py_XDECREF(py);
#ifdef DIM_3
    PyObject *pz = PyObject_GetAttrString(ipoint, "z");
    if(!pz) return NULL;
    v[i](2) = PyInt_AsLong(pz);
    Py_XDECREF(pz);
#endif
  }
  $target = &v;
}

// Convert a std::vector* of ICoords to a List of iPoints.
%typemap(python, out) ICoordVec* {
  // typemap(python, out) ICoordVec*
  ICoordVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  static PyObject *iPointClass = 0;
  if(!iPointClass) {
    PyObject *module = PyImport_ImportModule("ooflib.common.primitives");
    iPointClass = PyObject_GetAttrString(module, "iPoint");
    Py_XDECREF(module);
    if(!iPointClass) return 0;
  }
  for(ICoordVec::size_type i=0; i<sz; i++) {
    ICoord &ic = (*$source)[i];
#ifndef DIM_3
    PyObject *xyargs = Py_BuildValue("ii", ic(0), ic(1));
#else
    PyObject *xyargs = Py_BuildValue("iii", ic(0), ic(1), ic(2));
#endif
    PyObject *ipoint = PyObject_CallObject(iPointClass, xyargs);
    PyList_SET_ITEM($target, (Py_ssize_t) i, ipoint);
    // PyList_SET_ITEM steals a reference. Don't DECREF ipoint!
    Py_XDECREF(xyargs);
  }
}

%typemap(python, in) ICoordVec *iTupleList (ICoordVec v) {
  // typemap(python, in) ICoordVec *iTupleList
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
		    "Type error in ICoordVec typemap.  Python list of tuples required");
    return NULL;
  }
  ICoordVec::size_type sz = Py_SAFE_DOWNCAST(PyList_Size($source),
					     Py_ssize_t, ICoordVec::size_type);
  v.resize(sz);
  for(ICoordVec::size_type i=0; i<sz; i++) {
    PyObject *tuple = PyList_GET_ITEM($source, (Py_ssize_t) i);
    if(!tuple)
      return 0;
    PyObject *px = PyTuple_GET_ITEM(tuple, (Py_ssize_t) 0); // borrowed ref
    PyObject *py = PyTuple_GET_ITEM(tuple, (Py_ssize_t) 1);
    v[i](0) = PyInt_AsLong(px);
    v[i](1) = PyInt_AsLong(py);
#ifdef DIM_3
    PyObject *pz = PyTuple_GET_ITEM(tuple, (Py_ssize_t) 2);
    v[i](2) = PyInt_AsLong(pz);
#endif
  }
  $target = &v;
}

%typemap(python, newfree) ICoordVec* {
  delete $source;
}

%typemap(python, in) StringVec* (StringVec vec) {
  if(!PySequence_Check($source)) {
    PyErr_SetString(PyExc_TypeError, "Type error in vector<string>* typemap. Python sequence of Strings required.");
    return 0;
  }
  int sz = PySequence_Length($source);
  if(sz > 0) {
    vec.resize(sz);
    for(int i=0; i<sz; i++) {
      PyObject *x = PySequence_GetItem($source, i);
	  vec[i] = PyString_AsString(x);
	  Py_XDECREF(x);
	}
  }
  $target = &vec;
}

// Convert a std::vector* of std::strings to a list of Python strings
%typemap(python, out) StringVec* {
  // typemap(python, out) StringVec*
  StringVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(StringVec::size_type i=0; i<sz; i++) {
    PyObject *str = PyString_FromString((*$source)[i].c_str());
    PyList_SET_ITEM($target, (Py_ssize_t) i, str); // Steals reference.
  }
}

%typemap(python, newfree) StringVec *{
  delete $source;
}

// Convert an ICoord (C++) to an iPoint (Python).

// TODO: Is this typemap necessary?  See comments below for the
// equivalent Coord typemap.
%typemap(python, out) ICoord {
  // typemap(python, out) ICoord
  static PyObject *iPointClass = 0;
  if(!iPointClass) {
    PyObject *module = PyImport_ImportModule("ooflib.common.primitives");
    iPointClass = PyObject_GetAttrString(module, "iPoint");
    Py_XDECREF(module);
    if(!iPointClass) return 0;
  }
#ifndef DIM_3
  PyObject *xyargs = Py_BuildValue("ii", (*$source)(0), (*$source)(1));
#else
  PyObject *xyargs = Py_BuildValue("iii", (*$source)(0), (*$source)(1), (*$source)(2));
#endif
  delete $source;
  $target = PyObject_CallObject(iPointClass, xyargs);
  Py_XDECREF(xyargs);
}

// Convert a Coord (C++) to a Point (Python).

// TODO: Is this typemap necessary?  We can handle Coords directly
// in Python, and do so in lots of places in the code.  Including this
// typemap means that we're mixing Coords and Points in a mostly
// uncontrolled fashion.  For example, 2*coord.Coord(1.,2.) returns a
// Point, not a Coord, because this typemap is applied to the result
// of Coord.__rmul__()
%typemap(python, out) Coord {
  // typemap(python, out) Coord
  static PyObject *PointClass = 0;
  if(!PointClass) {
    PyObject *module = PyImport_ImportModule("ooflib.common.primitives");
    PointClass = PyObject_GetAttrString(module, "Point");
    Py_XDECREF(module);
    if(!PointClass) return 0;
  }
#ifndef DIM_3
  PyObject *xyargs = Py_BuildValue("dd", (*$source)(0), (*$source)(1));
#else
  PyObject *xyargs = Py_BuildValue("ddd", (*$source)(0), (*$source)(1),
				   (*$source)(2));
#endif
  delete $source;
  $target = PyObject_CallObject(PointClass, xyargs);
  Py_XDECREF(xyargs);
}

// %typemap(python, out) const Coord& {
//   // typemap(python, out) const Coord&
//   static PyObject *PointClass = 0;
//   if(!PointClass) {
//     PyObject *module = PyImport_ImportModule("ooflib.common.primitives");
//     PointClass = PyObject_GetAttrString(module, "Point");
//     Py_XDECREF(module);
//     if(!PointClass) return 0;
//   }
// #ifndef DIM_3
//   PyObject *xyargs = Py_BuildValue("dd", (*$source)(0), (*$source)(1));
// #else
//   PyObject *xyargs = Py_BuildValue("ddd", (*$source)(0), (*$source)(1),
// 				   (*$source)(2));
// #endif
//   $target = PyObject_CallObject(PointClass, xyargs);
//   Py_XDECREF(xyargs);
// }

// %typemap(python, out) const Coord* {
//   // typemap(python, out) const Coord*
//   static PyObject *PointClass = 0;
//   if(!PointClass) {
//     PyObject *module = PyImport_ImportModule("ooflib.common.primitives");
//     PointClass = PyObject_GetAttrString(module, "Point");
//     Py_XDECREF(module);
//     if(!PointClass) return 0;
//   }
// #ifndef DIM_3
//   PyObject *xyargs = Py_BuildValue("dd", (*$source)(0), (*$source)(1));
// #else
//   PyObject *xyargs = Py_BuildValue("ddd", (*$source)(0), (*$source)(1),
// 				   (*$source)(2));
// #endif
//   $target = PyObject_CallObject(PointClass, xyargs);
//   Py_XDECREF(xyargs);
// }

// Convert an iPoint (Python) to an ICoord* (C++)
%typemap(python, in) ICoord *iPoint (ICoord ic) {
  PyObject *xobj = PyObject_GetAttrString($source, "x");
  if(!xobj) return NULL;
  PyObject *yobj = PyObject_GetAttrString($source, "y");
  if(!yobj) return NULL;
#ifdef DIM_3
  PyObject *zobj = PyObject_GetAttrString($source, "z");
  if(!zobj) return NULL;
#endif
  ic(0) = PyInt_AsLong(xobj);
  Py_XDECREF(xobj);
  ic(1) = PyInt_AsLong(yobj);
  Py_XDECREF(yobj);
#ifdef DIM_3
  ic(2) = PyInt_AsLong(zobj);
  Py_XDECREF(zobj);
#endif
  $target = &ic;
}

// Convert a Point (Python) to a Coord* (C++)
%typemap(python, in) Coord *Point (Coord c) {
  // typemap(python, in) Coord *Point (Coord c)
  PyObject *xobj = PySequence_GetItem($source, 0);
  PyObject *yobj = PySequence_GetItem($source, 1);
#ifdef DIM_3
  PyObject *zobj = PySequence_GetItem($source, 2);
  if(!xobj || !yobj || !zobj) {
    PyErr_SetString(PyExc_TypeError, "Type error in Coord *Point typemap.  Argument must have 0, 1, and 2 components.");
    return NULL;
  }
#else
  if(!xobj || !yobj) {
    PyErr_SetString(PyExc_TypeError, "Type error in Coord *Point typemap.  Argument must have 0 and 1 components.");
    return NULL;
  }
#endif
  c(0) = PyFloat_AsDouble(xobj);
  Py_XDECREF(xobj);
  c(1) = PyFloat_AsDouble(yobj);
  Py_XDECREF(yobj);
#ifdef DIM_3
  c(2) = PyFloat_AsDouble(zobj);
  Py_XDECREF(zobj);
#endif
  $target = &c;
}

%typemap(python, in) Coord *Sequence (Coord c) {
  // typemap(python, in) Coord *Sequence (Coord c)
#ifndef DIM_3
  if(!(PySequence_Check($source) && PySequence_Length($source)==2)) {
    PyErr_SetString(PyExc_TypeError, "Type error in Coord *Sequence typemap.  Expected sequence of length 2.");
    return NULL;
  }
#else
  if(!(PySequence_Check($source) && PySequence_Length($source)==3)) {
    PyErr_SetString(PyExc_TypeError, "Type error in Coord *Sequence typemap.  Expected sequence of length 3.");
    return NULL;
  }
#endif
  PyObject *xobj = PySequence_GetItem($source, (Py_ssize_t) 0);
  c(0) = PyFloat_AsDouble(xobj);
  Py_XDECREF(xobj);
	PyObject *yobj = PySequence_GetItem($source, (Py_ssize_t) 1);
  c(1) = PyFloat_AsDouble(yobj);
	Py_XDECREF(yobj);
#ifdef DIM_3
	PyObject *zobj = PySequence_GetItem($source, (Py_ssize_t) 2);
  c(2) = PyFloat_AsDouble(zobj);
	Py_XDECREF(zobj);
#endif
  $target = &c;
}

%typemap(python, in) ICoord *Sequence (ICoord ic) {
  // typemap(python, in) ICoord *Sequence (ICoord ic)
#ifndef DIM_3
  if(!(PySequence_Check($source) && PySequence_Length($source)==2)) {
    PyErr_SetString(PyExc_TypeError, "Type error in ICoord *Sequence typemap. Expected sequence of length 2.");
    return NULL;
  }
#else
  if(!(PySequence_Check($source) && PySequence_Length($source)==3)) {
    PyErr_SetString(PyExc_TypeError, "Type error in Coord *Sequence typemap.  Expected sequence of length 3.");
    return NULL;
  }
#endif
  PyObject *xobj = PySequence_GetItem($source, (Py_ssize_t) 0);
  ic(0) = PyInt_AsLong(xobj);
  Py_XDECREF(xobj);
  PyObject *yobj = PySequence_GetItem($source, (Py_ssize_t) 1);
  ic(1) = PyInt_AsLong(yobj);
  Py_XDECREF(yobj);
#ifdef DIM_3
  PyObject *zobj = PySequence_GetItem($source, (Py_ssize_t) 2);
  ic(2) = PyInt_AsLong(zobj);
  Py_XDECREF(zobj);
#endif
  $target = &ic;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// OOF's global exception typemap, for taking exceptions out of C++
// and throwing the corresponding exceptions in Python.  See the
// comment in threadstate.C about threading_enabled.

%except(python) {
  // %except(python)
  PyThreadState *pythread = 0;
  try {
    installSignals;
    if(threading_enabled)
      pythread = PyEval_SaveThread(); // release the Python GIL.
    //=\\=//
    $function;
    //=\\=//
  }
  catch (PythonError &p) {
    // In this case, the Python error indicator is already set.
    if(pythread)		// Check pythread instead of
				// threading_enabled!
				// threading_enabled may have changed.
      PyEval_RestoreThread(pythread); // restore the Python GIL.
    restoreSignals;
    return 0;
  }
  catch (ErrError &e) {
    // Convert a C++ ErrError instance to a Python exception.
    if(pythread)
      PyEval_RestoreThread(pythread);
    restoreSignals;
    PyObject *args = Py_BuildValue("(s)",e.pythonequiv().c_str() );
    PyEval_CallObject((PyObject *)e.pyconverter, args);
    Py_DECREF(args);
    return 0;
  }
  catch (...) {
    // Caught a C++ exception that wasn't already handled and
    // converted into an ErrError. This means that something is really
    // wrong.
    if(pythread)
      PyEval_RestoreThread(pythread);
    restoreSignals;
    PyObject *args = Py_BuildValue(
       "(s)", "ErrPyProgrammingError('Caught an unexpected C++ exception!')");
    PyEval_CallObject((PyObject*) ErrError::pyconverter, args);
    Py_DECREF(args);
    return 0;
  }

  if(pythread)
    PyEval_RestoreThread(pythread); // restore the Python GIL.
  restoreSignals;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


/* Special typemaps used by the transitionPoint function to pass
   out both its status and the transition point, if valid.  To
   prevent confusion with other typemaps, the variables have
   module-specific names. */

%typemap(python, argout) Coord *cskel_OutPoint {
  // Get the Point class
  static PyObject *PointClass = 0;
  if(!PointClass) {
    PyObject *module = PyImport_ImportModule("ooflib.common.primitives");
    PointClass = PyObject_GetAttrString(module, "Point");
    if(!PointClass) return 0;
    Py_XDECREF(module);
  }
  // Create a Point object from the Coord ($source)
#ifndef DIM_3
  PyObject *xyargs = Py_BuildValue("dd", (*$source)(0), (*$source)(1));
#else
  PyObject *xyargs = Py_BuildValue("ddd", (*$source)(0), (*$source)(1), (*$source)(2));
#endif
  PyObject *point = PyObject_CallObject(PointClass, xyargs);
  Py_XDECREF(xyargs);
  if(!$target) {
    // Nothing else is being returned. Just return the Point.
    $target = point;
  }
  else if($target == Py_None) {
    Py_DECREF(Py_None);
    $target = point;
  }
  else {
    // The Point isn't the only thing being returned.  Return a list of stuff.
    if(!PyList_Check($target)) {
      // Other returned values aren't in a list yet.
      PyObject *other = $target;
      $target = PyList_New((Py_ssize_t) 0);
      PyList_Append($target, other);
      Py_XDECREF(other);
    }
    // Append the point to the list.
    PyList_Append($target, point);
    Py_XDECREF(point);
  }
}

%typemap(python, ignore) Coord *cskel_OutPoint (Coord temp) {
  $target = &temp;
}

%typemap(python,out) Progress* {
  // typemap(python, out) Progress*
  if($source) {
    $target = $source->pythonObject();
    if(!$target)
      return 0;
  }
  else {
    Py_INCREF(Py_None);
    $target = Py_None;
  }
 }





#endif // COMMONTYPEMAPS_SWG
