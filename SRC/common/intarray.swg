// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef INTARRAY_SWG
#define INTARRAY_SWG

%module(package="ooflib.SWIG.common") intarray

%include "common/typemaps.swg"
%import "common/coord.swg"

%{
#include "common/intarray.h"
%}

class IntArray {
public:
  IntArray(int, int);
  ~IntArray();
  ICoord size();
};

IntArray makeIntArray(ICoord *iPoint,int);
#endif // INTARRAY_SWG
