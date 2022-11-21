// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PROGRESS_SWG
#define PROGRESS_SWG

%module(package="ooflib.SWIG.common") progress
%include "common/typemaps.swg"

%{
#include "common/progress.h"
%}

enum ProgressType {
  DEFINITE,
  LOGDEFINITE,
  INDEFINITE
};

// Don't create default constructors for any of the Progress classes.
// They're always created in C++ by the getProgress() function.
%nodefaultctor;

class Progress {
public:
  ~Progress();
  void setProgressBar(PyObject*);
  bool hasProgressBar();
  bool started();
  // See comments in progress.h.
  void finish();
  bool finished();
  void stop();
  bool stopped();
  void setMessage(const std::string&);
  void setFraction(double);
  %newobject message;
  std::string *message();
  const std::string &name();
  int id();
  void acquireThreadLock();
  void releaseThreadLock();
  void disconnectBar(PyObject*);
};

PYTHONEXPORTABLE(Progress);

%extend Progress {
  bool __eq__(Progress *other) {
    return self->id() == other->id();
  }
  int __hash__() {
    return self->id();
  }
};

class DefiniteProgress : public Progress {
 public:
  double getFraction();
};

class LogDefiniteProgress : public DefiniteProgress {
public:
  void setRange(double, double);
};

class IndefiniteProgress : public Progress {
public:
  void pulse();
  unsigned long pulsecount();
};

Progress *getProgress(char*, ProgressType);
Progress *findProgress(char*);
Progress *findProgressByID(int);

#endif // PROGRESS_SWG
