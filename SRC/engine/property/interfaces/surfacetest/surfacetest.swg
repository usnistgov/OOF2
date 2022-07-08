// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef SURFACETEST_SWG
#define SURFACETEST_SWG

%module surfacetest

%{
#include "engine/property/interfaces/surfacetest/surfacetest.h"
%}
%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"

class ForceSurfaceTest : public Property
{
public:
  ForceSurfaceTest(PyObject *self, char *, double);
};


class FluxSurfaceTest : public Property
{
public:
  FluxSurfaceTest(PyObject *self, char*, double);
};

%pythoncode "engine/property/interfaces/surfacetest/surfacetest.spy"

#endif // SURFACETEST_SWG
