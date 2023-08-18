// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ENGINE_OOFERROR_SWG
#define ENGINE_OOFERROR_SWG

%module(package="ooflib.SWIG.engine") ooferror

%include "common/typemaps.swg"
%include "common/ooferrorwrappers.swg"
%import "common/ooferror.swg"

%{
#include "engine/ooferror.h"
%}

class ErrNoSuchField : public ErrError {
public:
  ErrNoSuchField(char *m);
  ~ErrNoSuchField();
};
WRAP_OOFERROR_CLASS(ErrNoSuchField);

class ErrDuplicateField : public ErrError {
public:
  ErrDuplicateField(char*, char*, char*);
  ~ErrDuplicateField();
};
WRAP_OOFERROR_CLASS(ErrDuplicateField);

class ErrNoSuchProperty : public ErrError {
public:
  ErrNoSuchProperty(char*, char*);
  ~ErrNoSuchProperty();
};
WRAP_OOFERROR_CLASS(ErrNoSuchProperty);

class ErrPropertyMissing : public ErrError {
public:
  ErrPropertyMissing(char*, char*, char*);
  ~ErrPropertyMissing();
};
WRAP_OOFERROR_CLASS(ErrPropertyMissing);

class ErrBadMaterial : public ErrError {
public:
  ErrBadMaterial(char*);
  ~ErrBadMaterial();
  const std::string &materialName();
};
WRAP_OOFERROR_CLASS(ErrBadMaterial);

class ErrRedundantProperty : public ErrError {
public:
  ErrRedundantProperty(char*);
  ~ErrRedundantProperty();
  const std::string &get_tag();
};
WRAP_OOFERROR_CLASS(ErrRedundantProperty);

class ErrConvergenceFailure : public ErrError {
public:
  ErrConvergenceFailure(char*, int);
  ~ErrConvergenceFailure();
};
WRAP_OOFERROR_CLASS(ErrConvergenceFailure);

class ErrTimeStepTooSmall : public ErrError {
public:
  ErrTimeStepTooSmall(double);
  ~ErrTimeStepTooSmall();
};
WRAP_OOFERROR_CLASS(ErrTimeStepTooSmall);

class ErrInvalidDestination : public ErrError {
public:
  ErrInvalidDestination();
  ~ErrInvalidDestination();
};
WRAP_OOFERROR_CLASS(ErrInvalidDestination);

%pythoncode "engine/ooferror.spy"

#endif // ENGINE_OOFERROR_SWG
