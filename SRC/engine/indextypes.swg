// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef INDEXTYPES_SWG
#define INDEXTYPES_SWG

// Convert any Python Enum type (particularly a SpaceComponent) to a
// SpaceIndex.

// This file doesn't define an interface module. It's just a place to
// store this typemap, which doesn't have a more natural location.

%typemap(in) SpaceIndex* (SpaceIndex idx) {
  // typemap(in) SpaceIndex*
  PyObject *pyindex = PyObject_CallMethod($input, (char*) "index", NULL);
  if(!pyindex)
    SWIG_fail;
  idx = PyLong_AsLong(pyindex);
  Py_XDECREF(pyindex);
  $1 = &idx;
}

#endif // INDEXTYPES_SWG
