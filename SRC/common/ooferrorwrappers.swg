// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFERRORWRAPPERS_SWG
#define OOFERRORWRAPPERS_SWG

// This file doesn't define a module.  It's just a place to put the
// WRAP_OOFERROR_CLASS macro so that it can import pyErrorWrappers
// without causing an import loop.

%pythoncode %{
  from ooflib.common.ooferrorwrappers import pyErrorWrappers
%}

%define WRAP_OOFERROR_CLASS(ERR)

%pythoncode %{
  class Py##ERR(Exception):
    def __init__(self, *args, **kwargs):
      self.cexcept = kwargs.get("cexcept", None)
      if self.cexcept is None:
        self.cexcept = ERR(*args, **kwargs)
    def __getattr__(self, attr):
      return getattr(self.cexcept, attr)
    def __repr__(self):
      return self.cexcept.summary()
    def __str__(self):
      return self.cexcept.summary()
  pyErrorWrappers[ERR] = Py##ERR
%}

%typemap(in) Py##ERR* {
  PyObject *cexcept = PyObject_GetAttrString($input, "cexcept");
  int res = SWIG_ConvertPtr(cexcept, &$1, $1_descriptor, 0);
  if(!SWIG_IsOK(res)) {
    PyErr_SetString(PyExc_TypeError,
		    "in method '$symname', expecting a ERR in self.cexcept");
    SWIG_fail;
  }
}

%enddef // WRAP_OOFERROR_CLASS

#endif // OOFERRORWRAPPERS_SWG
