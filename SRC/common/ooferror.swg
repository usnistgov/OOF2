// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFERROR_SWG
#define OOFERROR_SWG

// TODO PYTHON3: Change char* args to std::string&, which is what's
// use in the C++ classes.


%module(package="ooflib.SWIG.common") ooferror

%include "common/typemaps.swg"

%{
#include "common/ooferror.h"
%}

void pyErrorInit(PyObject *pythonCallable);

%nodefaultctor ErrError;

class ErrError {
public:
  %newobject summary;
  std::string *summary();
  %newobject details;
  std::string *details();
};

%pythoncode %{
  # Does this work?
  ErrError.__str__ = ErrError.__repr__
%}

// Subclasses require individual __repr__s.  If you provide one in the
// base class but don't provide them in the subclasses, SWIG will
// construct default uninformative __repr__s for the subclasses.

%pythoncode %{
pyErrorWrappers = {}
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

class ErrProgrammingError : public ErrError {
public:
  ErrProgrammingError(char *, char *, int);  // Message, filename, line no.
  const std::string &filename();
  int lineno();
  ~ErrProgrammingError();
};
WRAP_OOFERROR_CLASS(ErrProgrammingError);
ADD_REPR(ErrProgrammingError, summary);


class ErrResourceShortage : public ErrError {
public:
  ErrResourceShortage(char *m);
  ~ErrResourceShortage();
};
WRAP_OOFERROR_CLASS(ErrResourceShortage);
ADD_REPR(ErrResourceShortage, summary);

class ErrBoundsError : public ErrError {
public:
  ErrBoundsError(char *m);
  ~ErrBoundsError();
};
WRAP_OOFERROR_CLASS(ErrBoundsError);
ADD_REPR(ErrBoundsError, summary);


class ErrBadIndex : public ErrError {
public:
  ErrBadIndex(int, char *, int);
  ~ErrBadIndex();
};
WRAP_OOFERROR_CLASS(ErrBadIndex);
ADD_REPR(ErrBadIndex, summary);


class ErrUserError : public ErrError {
public:
  ErrUserError(char *);
  ~ErrUserError();
};
WRAP_OOFERROR_CLASS(ErrUserError);
ADD_REPR(ErrUserError, summary);

class ErrSetupError : public ErrError {
public:
  ErrSetupError(char * m);
  ~ErrSetupError();
};
WRAP_OOFERROR_CLASS(ErrSetupError);
ADD_REPR(ErrSetupError, summary);

class ErrInterrupted : public ErrError {
public:
  ErrInterrupted();
  ~ErrInterrupted();
};
WRAP_OOFERROR_CLASS(ErrInterrupted);
ADD_REPR(ErrInterrupted, summary);

class ErrNoProgress : public ErrError {
public:
  ErrNoProgress();
  ~ErrNoProgress();
};
WRAP_OOFERROR_CLASS(ErrNoProgress);
ADD_REPR(ErrNoProgress, summary);

%pythoncode "common/ooferror.spy"

#endif // OOFERROR_SWG
