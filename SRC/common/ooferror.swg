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

%module(package="ooflib.SWIG.common") ooferror

%include "common/typemaps.swg"
%include "common/ooferrorwrappers.swg"

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

class ErrProgrammingError : public ErrError {
public:
  ErrProgrammingError(const std::string &msg, const std::string &file, int l);
  const std::string &filename();
  int lineno();
  ~ErrProgrammingError();
};
WRAP_OOFERROR_CLASS(ErrProgrammingError);
ADD_REPR(ErrProgrammingError, summary);

class ErrPyProgrammingError : public ErrError {
public:
  ErrPyProgrammingError(std::string&, std::string&, int);
  ~ErrPyProgrammingError();
};
WRAP_OOFERROR_CLASS(ErrPyProgrammingError);
ADD_REPR(ErrPyProgrammingError, summary);

%pythoncode %{
  # Monkeypatch the __init__ so that line number and file
  # are inserted automatically.
  oldinit = PyErrPyProgrammingError.__init__
  def PyErrPyProgrammingError_init(self, msg):
    stack = traceback.extract_stack()
    (phile, lineno, func, txt) = stack[-2]
    self.oldinit(msg, phile, lineno)
  PyErrPyProgrammingError.__init__ = PyErrPyProgrammingError_init
%}

class ErrResourceShortage : public ErrError {
public:
  ErrResourceShortage(const std::string &m);
  ~ErrResourceShortage();
};
WRAP_OOFERROR_CLASS(ErrResourceShortage);
ADD_REPR(ErrResourceShortage, summary);

class ErrBoundsError : public ErrError {
public:
  ErrBoundsError(const std::string &m);
  ~ErrBoundsError();
};
WRAP_OOFERROR_CLASS(ErrBoundsError);
ADD_REPR(ErrBoundsError, summary);


class ErrBadIndex : public ErrError {
public:
  ErrBadIndex(int, const std::string&, int);
  ~ErrBadIndex();
};
WRAP_OOFERROR_CLASS(ErrBadIndex);
ADD_REPR(ErrBadIndex, summary);


class ErrUserError : public ErrError {
public:
  ErrUserError(const std::string&);
  ~ErrUserError();
};
WRAP_OOFERROR_CLASS(ErrUserError);
ADD_REPR(ErrUserError, summary);

class ErrSetupError : public ErrError {
public:
  ErrSetupError(const std::string&);
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

class ErrDataFileError : public ErrError {
public:
  ErrDataFileError(const std::string&);
  ~ErrDataFileError();
};
WRAP_OOFERROR_CLASS(ErrDataFileError);
ADD_REPR(ErrDataFileError, summary);

class ErrWarning : public ErrError {
public:
  ErrWarning(const std::string&);
  ~ErrWarning();
};
WRAP_OOFERROR_CLASS(ErrWarning);
ADD_REPR(ErrWarning, summary);


%pythoncode "common/ooferror.spy"

#endif // OOFERROR_SWG
