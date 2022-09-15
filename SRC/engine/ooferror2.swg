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

// This file is called ooferror2.swg instead of ooferror.swg because
// if it were called "ooferror.swg", the swig-generated python code
// would start with "import ooferrorc", which would import
// SWIG/common/ooferrorcmodule, since that one has already been
// loaded.

%module(package="ooflib.SWIG.engine") ooferror2

// When adding Error subclasses here, add them to engine/ooferror.spy
// as well.

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%include "common/ooferrorwrappers.swg"
%import "common/ooferror.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/ooferror.h"
%}

//%pragma(python) code="from ooflib.SWIG.common.ooferror import *"

class ErrNoSuchField : public ErrError {
public:
  ErrNoSuchField(char *m);
  ~ErrNoSuchField();
};
WRAP_OOFERROR_CLASS(ErrNoSuchField);
ADD_REPR(ErrNoSuchField, summary);

class ErrDuplicateField : public ErrError {
public:
  ErrDuplicateField(char*, char*, char*);
  ~ErrDuplicateField();
};
WRAP_OOFERROR_CLASS(ErrDuplicateField);
ADD_REPR(ErrDuplicateField, summary);

class ErrNoSuchProperty : public ErrError {
public:
  ErrNoSuchProperty(char*, char*);
  ~ErrNoSuchProperty();
};
WRAP_OOFERROR_CLASS(ErrNoSuchProperty);
ADD_REPR(ErrNoSuchProperty, summary);

class ErrPropertyMissing : public ErrError {
public:
  ErrPropertyMissing(char*, char*, char*);
  ~ErrPropertyMissing();
};
WRAP_OOFERROR_CLASS(ErrPropertyMissing);
ADD_REPR(ErrPropertyMissing, summary);

class ErrBadMaterial : public ErrError {
public:
  ErrBadMaterial(char*);
  ~ErrBadMaterial();
  const std::string &materialName();
};
WRAP_OOFERROR_CLASS(ErrBadMaterial);
ADD_REPR(ErrBadMaterial, summary);

class ErrRedundantProperty : public ErrError {
public:
  ErrRedundantProperty(char*);
  ~ErrRedundantProperty();
  const std::string &get_tag();
};
WRAP_OOFERROR_CLASS(ErrRedundantProperty);
ADD_REPR(ErrRedundantProperty, summary);

class ErrConvergenceFailure : public ErrError {
public:
  ErrConvergenceFailure(char*, int);
  ~ErrConvergenceFailure();
};
WRAP_OOFERROR_CLASS(ErrConvergenceFailure);
ADD_REPR(ErrConvergenceFailure, summary);

class ErrTimeStepTooSmall : public ErrError {
public:
  ErrTimeStepTooSmall(double);
  ~ErrTimeStepTooSmall();
};
WRAP_OOFERROR_CLASS(ErrTimeStepTooSmall);
ADD_REPR(ErrTimeStepTooSmall, summary);

class ErrInvalidDestination : public ErrError {
public:
  ErrInvalidDestination();
  ~ErrInvalidDestination();
};
WRAP_OOFERROR_CLASS(ErrInvalidDestination);
ADD_REPR(ErrInvalidDestination, summary);

%pythoncode "engine/ooferror2.spy"

#endif // ENGINE_OOFERROR_SWG
