// -*- C++ -*-
// $RCSfile: direction.swg,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2012/02/28 22:24:57 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef DIRECTION_SWG
#define DIRECTION_SWG

%module direction

%{
#include "common/direction.h"
%}

%pragma(python) include="direction.spy"

class CDirection {
public:
  ~CDirection();
  double theta();
  double phi();
  CUnitVectorDirection unitVector();
};

class CUnitVectorDirection : public CDirection {
public:
  CUnitVectorDirection(double, double, double);
  double x();
  double y();
  double z();
};

class CAngleDirection : public CDirection {
public:
  CAngleDirection(double, double);
};

#endif // DIRECTION_SWG

