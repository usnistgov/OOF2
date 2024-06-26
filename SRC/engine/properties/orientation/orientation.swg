// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef ORIENTATION_SWG
#define ORIENTATION_SWG

%module(package="ooflib.SWIG.engine.properties.orientation") orientation

%include "common/typemaps.swg"
%import "engine/property.swg"
%import "engine/corientation.swg"

%{
#include "engine/corientation.h"
#include "engine/properties/orientation/orientation.h"
%}


// Typemap for converting a convertible registered Orientation gizmo
// from orientationmatrix.py into a COrientation.  The COrientation is
// already a C++ object, and a pointer to it is stored in the
// Orientation object.

%typemap(in) COrientation * {
  PyObject *py_orient = PyObject_GetAttrString($input,"corient");
  SWIG_ConvertPtr(py_orient, (void**) &$1, $1_descriptor, 0);
}

class OrientationProp : public Property {
public:
  OrientationProp(PyObject *registry, char *name, COrientation *orient);
  const COrientation *orientation();
};

%pythoncode "engine/properties/orientation/orientation.spy"

#endif // ORIENTATION_SWG
