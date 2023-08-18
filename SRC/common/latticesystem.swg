// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef LATTICESYSTEM_SWG
#define LATTICESYSTEM_SWG

%module(package="ooflib.SWIG.common") latticesystem

%include "common/typemaps.swg"

%{
#include "common/latticesystem.h"
%}

class LatticeSymmetry {
};


%typemap(in) SmallMatrix *ThreeByThreeFloats (SmallMatrix mat) {
  // typemap(in) SmallMatrix *ThreeByThreeFloats
  // Convert [[x00, x01, x02],[x10, x11, x12], [x20, x21, x22]] to SmallMatrix
  mat.resize(3, 3);
  for(unsigned int row=0; row<3; row++)  {
    PyObject *pyrow = PyList_GET_ITEM($input, (Py_ssize_t) row);
    for(unsigned int col=0; col<3; col++) {
      PyObject *pyval = PyList_GET_ITEM(pyrow, (Py_ssize_t) col);
      mat(row, col) = PyFloat_AsDouble(pyval);
    }
  }
  $1 = &mat;
}

void addLatticeSymmetryMatrix(char*, SmallMatrix *ThreeByThreeFloats);

%pythoncode "common/latticesystem.spy"

#endif // LATTICESYSTEM_SWG

