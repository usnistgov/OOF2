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

// TODO PYTHON3: Python exceptions must derive from Exception or
// BaseException.  It's not clear how to to that.  Maybe SWIG4 knows
// how?

%module(package="ooflib.SWIG.common") ooferror

%include "common/typemaps.swg"

%{
#include "common/ooferror.h"
%}

void pyErrorInit(PyObject *pythonCallable);

/* Swigged for automatic synchronization with C++ classes.
   The error-handling scheme involves error objects being created
   in the C++ code, then re-created from Python via the 
   string returned by the pythonequiv method, which must be a 
   call to the constructor in string form, with literal arguments,
   e.g. if the constructor takes a string and two integers, the
   pythonequiv string might look like: "MyError('Doom.', 13, 666)" */
/* NB the pythonequiv method only needs to be visible from C++. */
 

%nodefaultctor ErrError;

class ErrError {
public:
  %newobject summary;
  std::string *summary();
  %newobject details;
  std::string *details();
};

// NOTE: inheritance layout here is different than ooferror.h. 

// Subclasses require individual __repr__s.  If you provide one in the
// base class but don't provide them in the subclasses, SWIG will
// construct default uninformative __repr__s for the subclasses.

/* Args are: Message, filename, line-number. */
class ErrProgrammingError : public ErrError {
public:
  const std::string &filename();
  int lineno();
  ErrProgrammingError(char *, char *, int);
  ~ErrProgrammingError();
};

ADD_REPR(ErrProgrammingError, summary);


class ErrResourceShortage : public ErrError {
public:
  ErrResourceShortage(char *m);
  ~ErrResourceShortage();
};

ADD_REPR(ErrResourceShortage, summary);

class ErrBoundsError : public ErrError {
public:
  ErrBoundsError(char *m);
  ~ErrBoundsError();
};

ADD_REPR(ErrBoundsError, summary);


class ErrBadIndex : public ErrError {
public:
  ErrBadIndex(int, char *, int);
  ~ErrBadIndex();
};

ADD_REPR(ErrBadIndex, summary);


class ErrUserError : public ErrError {
public:
  ErrUserError(char *);
  ~ErrUserError();
};

ADD_REPR(ErrUserError, summary);

class ErrSetupError : public ErrError {
public:
  ErrSetupError(char * m);
  ~ErrSetupError();
};

ADD_REPR(ErrSetupError, summary);

class ErrInterrupted : public ErrError {
public:
  ErrInterrupted();
  ~ErrInterrupted();
};

ADD_REPR(ErrInterrupted, summary);

class ErrNoProgress : public ErrError {
public:
  ErrNoProgress();
  ~ErrNoProgress();
};

ADD_REPR(ErrNoProgress, summary);

%pythoncode "common/ooferror.spy"

#endif // OOFERROR_SWG
