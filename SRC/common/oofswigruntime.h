// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Always #include this header file instead of swigruntime.h

// External access to the swig runtime library is provided by
// generating a copy of the swig routines like this:
//   swig -python -external-runtime swigruntime.h
// which will create swigruntime.h.  HOWEVER, that file doesn't
// include any #ifndefs to prevent it from being loaded more than
// once, and at least one #define is missing.  This wrapper addresses
// both of those problems.

// Also, if this is being included inside swig-generated code, all of
// the definitions are already present and nothing needs to be
// imported.  The headers for an external library may already have
// loaded a copy of the runtime.  Checking for SWIG_RUNTIME_VERSION
// takes care of all of those situations.  SWIG_RUNTIME_VERSION is
// defined in swigruntime.h and also defined in all swig-generated C++
// files.

// TODO PYTHON3:  Allow users to switch between swig versions, and
// include either swigruntime-402.h or swigruntime-410.h here.
// BETTER -- generate swigruntime.h via cmake after swig is located.

#include <oofconfig.h>

#ifndef SWIG_RUNTIME_VERSION

#include "common/swigruntime-410.h"
//#include "swigruntime.h"
#define SWIG_as_voidptr(a) const_cast< void * >(static_cast< const void * >(a)) 

#endif 
