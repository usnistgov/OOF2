// -*- C++ -*-
// $RCSfile: surfacetest.swg,v $
// $Revision: 1.4 $
// $Author: langer $
// $Date: 2014/09/27 21:41:19 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

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

%pragma(python) include="surfacetest.spy"
