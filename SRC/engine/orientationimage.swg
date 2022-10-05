// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ORIENTATIONIMAGE_SWG
#define ORIENTATIONIMAGE_SWG

%module(package="ooflib.SWIG.engine") orientationimage

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/abstractimage.swg"
%import "common/canvasimage.swg"
%import "engine/angle2color.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/ccolor.h"
#include "engine/angle2color.h"
#include "engine/orientationimage.h"
%}

class CMicrostructure;

class OrientationImage : public AbstractImage {
public:
  OrientationImage(CMicrostructure*, Angle2Color*, CColor*, CColor*);
  OOFCanvas::CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);
};

#endif // ORIENTATIONIMAGE_SWG
