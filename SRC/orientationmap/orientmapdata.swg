// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ORIENTMAPDATA_SWG
#define ORIENTMAPDATA_SWG

%module orientmapdata
%include "common/typemaps.swg"
%include "common/canvasimage.swg"
%{
#include "orientationmap/orientmapdata.h"
%}

%pragma(python) include="orientmapdata.spy"
%extern "common/abstractimage.swg"
%extern "common/coord.swg"
%extern "engine/angle2color.swg"
%extern "engine/corientation.swg"
%extern "image/oofimage.swg"
%pragma(python) code="from ooflib.SWIG.common.abstractimage import AbstractImagePtr"
%pragma(python) code="from ooflib.SWIG.common.coord import CoordPtr"
%pragma(python) code="from ooflib.SWIG.common.coord import ICoordPtr"
%pragma(python) code="from ooflib.SWIG.engine.corientation import COrientABGPtr"
%pragma(python) code="from ooflib.SWIG.image.oofimage import OOFImagePtr"

class OrientMap {
public:
  OrientMap(ICoord *iPoint, Coord *Point);
  ~OrientMap();
  const COrientABG &angle(const ICoord *iPoint);
  const ICoord sizeInPixels();
  const Coord size();
  ICoord pixelFromPoint(Coord *Point);
  bool pixelInBounds(ICoord *iPoint);
  OOFImage *createImage(char *, Angle2Color&);
  void setMicrostructure(CMicrostructure*);
  CMicrostructure *getCMicrostructure();
};

class COrientMapReader {
public:
  COrientMapReader();
  void set_angle(OrientMap &data, const ICoord *iPoint, const COrientation*);
};

class OrientMapImage : public AbstractImage {
public:
  OrientMapImage(OrientMap*, Angle2Color*);
  ~OrientMapImage();
  %newobject makeCanvasImage;
  CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);
};

void registerOrientMap(char*, OrientMap*);
void removeOrientMap(char*);

#endif // ORIENTMAPDATA_SWG
