// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef GUITOP_SWG
#define GUITOP_SWG

%module(package="ooflib.SWIG.common") guitop

%include "common/typemaps.swg"
%{
#include "common/guitop.h"
%}

void setMainLoop(bool);
bool getMainLoop();

%pythoncode "common/guitop.spy"

#endif // GUITOP
