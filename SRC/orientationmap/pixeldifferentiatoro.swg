// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELDIFFORIENT_SWG
#define PIXELDIFFORIENT_SWG

%module(package="ooflib.SWIG.orientationmap") pixeldifferentiatoro

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/burn.swg"
%import "common/statgroups.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/burn.h"
#include "orientationmap/orientmapdata.h"
#include "orientationmap/pixeldifferentiatoro.h"
%}

class COrientationDifferentiator3 : public CPixelDifferentiator3 {
public:
  COrientationDifferentiator3(OrientMap*, double, double, char*);
};

class COrientationDifferentiator2 : public CPixelDifferentiator2 {
public:
  COrientationDifferentiator2(OrientMap*, double, char*);
};

class OrientationPixelDistFactory : public PixelDistributionFactory {
public:
  OrientationPixelDistFactory(OrientMap*, double, char*);
};

%pythoncode "orientationmap/pixeldifferentiatoro.spy"

#endif // PIXELDIFFORIENT_SWG
