// -*- C++ -*-
// $RCSfile: forcedensity.swg,v $
// $Revision: 1.9 $
// $Author: langer $
// $Date: 2014/09/27 21:41:13 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

%module forcedensity

%{
#include "engine/property/forcedensity/forcedensity.h"
%}
%include "common/typemaps.swg"
%include "engine/propertyhdr.swg"

%pragma(python) include="forcedensity.spy"

class ForceDensity : public Property {
public:
#ifndef DIM_3
  ForceDensity(PyObject *self, char *, double, double);
#else
  ForceDensity(PyObject *self, char *, double, double, double);
#endif
  double fdensity_x();
  double fdensity_y();
#ifdef DIM_3
  double fdensity_z();
#endif
};

