// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CONTOUR_SWG
#define CONTOUR_SWG

%module(package="ooflib.SWIG.engine.IO") contour

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/masterelement.swg"
%import "engine/mastercoord.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/IO/contour.h"
  typedef std::vector<CCurve> CurveVec;
  extern int nContourStates, nCreated, nDeleted; // DEBUGGING
%}

MAKE_LISTVEC_TYPEMAPS(ContourCoord);

%typemap(out) CurveVec* {
  // Convert a vector of CCurves (which are std::deques of
  // MasterCoord*'s) to a list of lists of MasterCoords.
  CurveVec::size_type sz = $source->size();
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<CCurve>::size_type i=0; i<sz; i++) {
    CCurve &curve = (*$1)[i];
    PyObject *coordlist = PyList_New((Py_ssize_t) curve.size());
    PyList_SET_ITEM($result, (Py_ssize_t) i, coordlist);
    for(CCurve::size_type j=0; j<curve.size(); j++) {
      PyObject *tmp = SWIG_NewPointerObj(SWIG_as_voidptr(curve[j]),
					 $descriptor(MasterCoord*), 0);
      PyList_SET_ITEM(coordlist, (Py_ssize_t) j, tmp);
    }
  }
}

%nodefaultctor ContourCoord;

class ContourCoord : public MasterCoord {
public:
  double value;
};

class CContour {
public:
  CContour(double, int);
  ~CContour();
  void compute(ContourCellSet*, MasterElement*, bool);
  CurveVec *getCurves();
  CurveVec *getLoops();
%immutable;
  double value;
%mutable;
};

%nodefaultctor ContourCellSet;

class ContourCellSet {
public:
  ContourCoordRefVec *getCorners();
  void findIntercepts(const std::vector<double>*);
};

ContourCellSet *contourCellCache(MasterElement*, int);
void clearCache();

int nContourStates, nCreated, nDeleted;	// DEBUGGING

%pythoncode "engine/IO/contour.spy"

#endif // CONTOUR_SWG
