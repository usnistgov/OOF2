// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ANGLE2COLOR_SWG
#define ANGLE2COLOR_SWG

%module(package="ooflib.SWIG.engine") angle2color

%include "common/typemaps.swg"

%{
#include "engine/angle2color.h"
%}

%nodefaultctor Angle2Color;

class Angle2Color {};

class Bunge2RGB : public Angle2Color {
public:
  Bunge2RGB();
};

class Euler2RGB : public Angle2Color {
public:
  Euler2RGB();
};

class Euler2HSV : public Angle2Color {
public:
  Euler2HSV();
};

class Axis2HSV : public Angle2Color {
public:
  Axis2HSV();
};

%pythoncode "engine/angle2color.spy"

#endif // ANGLE2COLOR_SWG
