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

%module cmicrostructure

%{
#include <oofconfig.h>
#include "common/cmicrostructure.h"
#include "common/array.h"
typedef Array<int> ArrayInt;
typedef Array<int> NewArrayInt;
%}

%include "common/typemaps.swg"

%import "common/pixelgroup.swg"
 //%pragma(python) code="from ooflib.SWIG.common.pixelgroup import PixelGroupPtr"

%import "common/timestamp.swg"
 //%pragma(python) code="from ooflib.SWIG.common.timestamp import TimeStampPtr"

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

// %typemap(ignore) bool *newness (bool tmp) {
//   // typemap(ignore) bool *newness
//   $target = &tmp;
// }

%typemap(argout) bool *newness {
  // typemap(argout) bool *newness
  PyObject *res;
  if (*$source) 
    res = Py_True;
  else
    res = Py_False;

  if (!PyList_Check($target)) {
    PyObject *retval = $target;
    $target = PyList_New((Py_ssize_t) 0);
    PyList_Append($target,retval);
    Py_XDECREF(retval);
  }
  PyList_Append($target, res);
}

%import "common/coord.swg"


//For SnapRefine.
 // TODO PYTHON3: Change the name of this typemap
// %typemap(ignore) int *cskel_edgecat (int tmp) {
//   $target = &tmp;
// }

%typemap(argout) int *cskel_edgecat {
  PyObject *res=PyInt_FromLong(*$source);
  if (!PyList_Check($target)) {
    PyObject *retval = $target;
    $target = PyList_New((Py_ssize_t) 0);
    PyList_Append($target,retval);
    Py_XDECREF(retval);
  }
  PyList_Append($target, res);
  Py_XDECREF(res);
}

class CMicrostructure {
public:
  CMicrostructure(char *name, ICoord *Sequence, Coord *Sequence);
  ~CMicrostructure();
  void destroy(); 
  const string &name();
  void rename(char *name);
  TimeStamp &getTimeStamp();
  void setCurrentActiveArea(ActiveArea*);
  int nGroups();
  PixelGroup *getGroup(char *name, 
		       bool *newness); //creates new group if necessary
  PixelGroup *findGroup(char *name); // never creates a new group
  void removeGroup(char *name);
  void removeAllGroups();
  void renameGroupC(char *oldname, char *newname);
  NewStringVec *groupNames() const;
  int nCategories();
  int category(ICoord *iPoint);
  void recategorize();
  bool is_categorized();
  ArrayInt *getCategoryMap();
  NewArrayInt *getCategoryMapRO();
  ICoord getRepresentativePixel(int category);
  bool transitionPointWithPoints(Coord *Point, Coord *Point,
				 Coord *cskel_OutPoint);
//   %extend {
//     Coord transitionPointWithPoints(Coord *Point c0, Coord *Point c1) {
//       Coord *point;
//       self->transitionPointClosest(*c0, *c1, point);
//       return *point;
//     }
//   };
  
  double edgeHomogeneity(Coord Point, Coord Point);
  double edgeHomogeneityCat(Coord Point, Coord Point,
			    int* cskel_edgecat);
  bool transitionPointWithPoints_unbiased(Coord *Point, Coord *Point,
				 Coord *cskel_OutPoint);

};

long get_globalMicrostructureCount();

//For SnapRefine.
%typemap(argout) int *cskel_edgecat {}
// %typemap(ignore) int *cskel_edgecat {}

%pythoncode "common/cmicrostructure.spy"

#endif // CMICROSTRUCTURE_SWG
