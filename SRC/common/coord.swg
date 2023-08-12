// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef COORD_SWG
#define COORD_SWG

%module(package="ooflib.SWIG.common") coord

%include "common/typemaps.swg"
%{
#include "common/coord.h"
%}

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

//==||==\\==||==//==||==\\==||==//==||==\\==||==//==||==\\==||==//
//==||===\\=||=//===||===\\=||=//===||===\\=||=//===||===\\=||==//


%nodefaultctor Position;
class Position {};
  
class Coord : public Position {
public:
  Coord(double x1, double x2);
  ~Coord();
};

%extend Coord {
  // This function is 'getitem', not '__getitem__', because
  // __getitem__ is defined in terms of getitem in the .spy file.
  // __getitem__ raises a Python exception if the argument is out of
  // range.
  double getitem(int i) {
    return (*self)(i);
  }
  int __len__() {
    return DIM;
  }
  Coord __mul__(double x) {
    return (*self)*x;
  }
  Coord __rmul__(double x) {
    return (*self)*x;
  }
}

double dot(const Coord *Point, const Coord *Point);

class ICoord {
public:
  ICoord(int x, int y);
};

%extend ICoord {
  int __getitem__(int i) {
    return (*self)(i);
  }
  int __len__() {
    return DIM;
  }
  ICoord __mul__(int x) {
    return (*self)*x;
  }
  ICoord __rmul__(int x) {
    return (*self)*x;
  }
}

MAKE_LISTVEC_TYPEMAPS(Coord);
MAKE_LISTVEC_TYPEMAPS(ICoord);

%pythoncode "common/coord.spy"

#endif // COORD_SWG
