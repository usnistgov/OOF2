// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef OOFVERSION_SWG
#define OOFVERSION_SWG

%module(package="ooflib.SWIG.common") oofversion

%include "common/typemaps.swg"

%{
  #include <oofconfig.h>
  
  const std::string version() {
    return OOFVERSION;
  }

  int version_major() {
    return OOFVERSION_MAJOR;
  }

  int version_minor() {
    return OOFVERSION_MINOR;
  }

  int version_patch() {
    return OOFVERSION_PATCH;
  }
%}

const std::string version();
int version_major();
int version_minor();
int version_patch();

#endif // OOFVERSION_SWG
