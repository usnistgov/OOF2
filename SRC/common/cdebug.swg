// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CDEBUG_SWG
#define CDEBUG_SWG

%module cdebug

%include "common/typemaps.swg"

%{
#include "common/cdebug.h"
#include "common/pixelsetboundary.h"
  void segfault();
%}
%pragma(python) include="cdebug.spy"

void initDebug(PyObject*);
void segfault(int);
void throwException();
void throwPythonException();
void throwPythonCException();

void spinCycle(int);

int countleft;			// in pixelsetboundary.h

#endif // CDEBUG_SWG
