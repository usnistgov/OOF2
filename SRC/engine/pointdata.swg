// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef POINTDATA_SWG
#define POINTDATA_SWG

%module(package="ooflib.SWIG.engine") pointdata

%include "common/typemaps.swg"
%import "engine/field.swg"

%{
#include "engine/pointdata.h"
%}

%nodefaultctor PointData;

class PointData {
public:
  bool hasField(const Field&);
  int fieldDefCount(const Field&);
  int fieldSetID();
};

#endif
