// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ARGV_SWG
#define ARGV_SWG

%module(package="ooflib.SWIG.common") argv

%include "common/typemaps.swg"

%{
#include "common/argv.h"
%}

void init_argv(std::vector<char*> *argv);

#endif // ARGV_SWG
