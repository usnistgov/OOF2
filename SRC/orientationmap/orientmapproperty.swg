// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ORIENTMAPPROPERTY_SWG
#define ORIENTMAPPROPERTY_SWG

%module(package="ooflib.SWIG.orientationmap") orientmapproperty

%include "common/typemaps.swg"
%import "engine/property.swg"

%{
#include "orientationmap/orientmapproperty.h"
%}

class OrientationMapProp : public Property {
public:
  OrientationMapProp(PyObject *registry, char *name);
};

%pythoncode "orientationmap/orientmapproperty.spy"

#endif // ORIENTMAPPROPERTY_SWG
