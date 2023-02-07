// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CMICROSTRUCTURE_SWG
#define CMICROSTRUCTURE_SWG

%module(package="ooflib.SWIG.common") cmicrostructure

%{
#include <oofconfig.h>
#include "common/cmicrostructure.h"
#include "common/array.h"
typedef Array<int> ArrayInt;
typedef Array<int> NewArrayInt;
%}

%include "common/typemaps.swg"
%import "common/coord.swg"
%import "common/pixelgroup.swg"
%import "common/timestamp.swg"

%typemap(out) ArrayInt* {
   // typemap(out) ArrayInt*
  int h = $1->height();
  int w = $1->width();
  // assert(h >= PY_SSIZE_T_MIN && h <= PY_SSIZE_T_MAX);
  // assert(w >= PY_SSIZE_T_MIN && w <= PY_SSIZE_T_MAX);
  $result = PyList_New((Py_ssize_t) h);
  for(int j=0; j<h; j++) {
    PyObject *row = PyList_New((Py_ssize_t) w);
    PyList_SET_ITEM($result, (Py_ssize_t) j, row);
    for(int i=0; i<w; i++) {
      PyList_SET_ITEM(row, (Py_ssize_t) i, PyInt_FromLong((*$1)[ICoord(i,j)]));
    }
  }
}

%typemap(out) NewArrayInt* {
   // typemap(out) ArrayInt*
  int h = $1->height();
  int w = $1->width();
  // assert(h >= PY_SSIZE_T_MIN && h <= PY_SSIZE_T_MAX);
  // assert(w >= PY_SSIZE_T_MIN && w <= PY_SSIZE_T_MAX);
  $result = PyList_New((Py_ssize_t) h);
  for(int j=0; j<h; j++) {
    PyObject *row = PyList_New((Py_ssize_t) w);
    PyList_SET_ITEM($result, (Py_ssize_t) j, row);
    for(int i=0; i<w; i++) {
      PyList_SET_ITEM(row, (Py_ssize_t) i, PyInt_FromLong((*$1)[ICoord(i,j)]));
    }
  }
  delete $1;
}

%typemap(in, numinputs=0) bool *bool_argout (bool tmp) {
  // typemap(in, numinputs=0) bool *bool_argout
  $1 = &tmp;
}

%typemap(argout) bool *bool_argout {
  // typemap(argout) bool *bool_argout
  PyObject *newval = (*$1? Py_True : Py_False);

  if (!PyList_Check($result)) {
    // There's already an object in $result, but it's not a list.
    // Change $result to a list containing the pre-existing object.
    PyObject *oldval = $result;
    $result = PyList_New((Py_ssize_t) 0);
    PyList_Append($result, oldval);
    Py_XDECREF(oldval);
  }
  PyList_Append($result, newval);
}

//For SnapRefine.
%typemap(in, numinputs=0) int *int_argout (int tmp) {
  // typemap(in, numinputs=0) int *int_argout
  $1 = &tmp;
}

%typemap(argout) int *int_argout {
  // typemap(argout) int *int_argout
  PyObject *newval = PyLong_FromLong(*$1);
  if (!PyList_Check($result)) {
    PyObject *oldval = $result;
    $result = PyList_New((Py_ssize_t) 0);
    PyList_Append($result ,oldval);
    Py_XDECREF(oldval);
  }
  PyList_Append($result, newval);
  Py_XDECREF(newval);
}

class CMicrostructure {
public:
  CMicrostructure(const std::string &name, ICoord *Sequence, Coord *Sequence);
  ~CMicrostructure();
  void destroy(); 
  const std::string &name();
  void rename(const std::string &name);
  TimeStamp &getTimeStamp();
  void setCurrentActiveArea(ActiveArea*);
  int nGroups();
  PixelGroup *getGroup(const std::string &name, 
		       bool *bool_argout); // creates new group if necessary
  PixelGroup *findGroup(const std::string &name); // never creates a new group
  void removeGroup(char *name);
  void removeAllGroups();
  void renameGroupC(char *oldname, char *newname);
  %newobject groupNames;
  std::vector<std::string> *groupNames() const;
  int nCategories();
  int category(ICoord *iPoint);
  void recategorize();
  bool is_categorized();
  ArrayInt *getCategoryMap();
  NewArrayInt *getCategoryMapRO();
  ICoord getRepresentativePixel(int category);
  bool transitionPointWithPoints(Coord *Point, Coord *Point,
				 Coord *argout_Point);
  double edgeHomogeneity(const Coord &Point, const Coord &Point);
  double edgeHomogeneityCat(const Coord &Point, const Coord &Point,
			    int* int_argout);
  bool transitionPointWithPoints_unbiased(Coord *Point, Coord *Point,
				 Coord *argout_Point);

};

long get_globalMicrostructureCount();

#endif // CMICROSTRUCTURE_SWG
