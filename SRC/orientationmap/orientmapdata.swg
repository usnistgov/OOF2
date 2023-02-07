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

%module(package="ooflib.SWIG.orientationmap") orientmapdata

%include "common/typemaps.swg"
%include "common/canvasimage.swg"
%import "common/abstractimage.swg"
%import "common/coord.swg"
%import "engine/angle2color.swg"
%import "engine/corientation.swg"
%import "image/oofimage.swg"

%{
#include "orientationmap/orientmapdata.h"
#include "engine/angle2color.h"
%}

class OrientMap {
public:
  OrientMap(ICoord *iPoint, Coord *Point);
  ~OrientMap();
  const COrientABG &angle(const ICoord *iPoint);
  const ICoord sizeInPixels();
  const Coord size();
  ICoord pixelFromPoint(Coord *Point);
  bool pixelInBounds(ICoord *iPoint);
  %newobject createImage;
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
  CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);
};

void registerOrientMap(char*, OrientMap*);
void removeOrientMap(char*);

%pythoncode "orientationmap/orientmapdata.spy"

#endif // ORIENTMAPDATA_SWG
