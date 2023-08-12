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
// without causing an import loop.  It should *not* be included in
// swig_sources in CMakeLists.txt.

// Python exceptions must be derived from Exception, so swigged C++
// exception classes can't be raised or caught by Python.  However, we
// want to be able to throw exceptions in one language and catch them
// in the other.  So when a C++ excepton is swigged, it's passed to
// WRAP_OOFERROR_CLASS, which creates a new Python class derived from
// Exception and containing a reference to a C++ exception.  The new
// class uses __getattr__ to mimic all of the attributes of the C++
// exception.
//
// WRAP_OOFERROR_CLASS also defines a typemap that converts the Python
// exception to a C++ exception.

// When Python calls a swigged C++ function that raises an exception,
// the exception is caught by the %exception code in typemaps.swg.
// All OOF C++ xceptions are derived from ErrError, a PythonExportable
// class defined in ooferror.h The %exception code catches the
// exception and passes it to the static ErrError::pyconverter
// function, which is a *Python* function that raises the Python
// version of the C++ exception.  (pyconverter is initialized by
// calling pyErrorCallback at startup time.)

// When C++ calls a Python function that raises an exception, the
// Python function will return NULL.  C++ must then call
// pythonErrorRelay() (declared in ooferror.h).  pythonErrorRelay will
// raise the C++ version of the exception, if the exception is the
// Python version of something in the ErrError class hierarchy.  The
// exception can then be handled by C++.  If the exception is some
// other kind of Python exception, pythonErrorRelay will raise a
// PythonError, which should be ignored by the C++ code.  It will be
// caught by the swig %exception code, which will then return to
// Python without changing the exception state, effectively passing
// the Python exception from Python through C++ and back to Python.

%pythoncode %{
   from ooflib.common import ooferrorwrappers
%}

%define WRAP_OOFERROR_CLASS(ERR)

%pythoncode %{
    
  class Py##ERR(ooferrorwrappers.PyOOFError):
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
  ooferrorwrappers.pyErrorWrappers[ERR] = Py##ERR
%}

%typemap(in) Py##ERR* {
  // typemap(in) Py##ERR * via WRAP_OOFERROR_CLASS for ERR
  PyObject *cexcept = PyObject_GetAttrString($input, "cexcept");
  int res = SWIG_ConvertPtr(cexcept, &$1, $1_descriptor, 0);
  if(!SWIG_IsOK(res)) {
    PyErr_SetString(PyExc_TypeError,
		    "in method '$symname', expecting a ERR in self.cexcept");
    SWIG_fail;
  }
}

ADD_REPR(ERR, summary);

%enddef // WRAP_OOFERROR_CLASS

#endif // OOFERRORWRAPPERS_SWG
