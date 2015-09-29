// -*- C++ -*-
// $RCSfile: orientmapdata.swg,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2012/02/28 18:39:46 $

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
%{
#include "orientationmap/orientmapdata.h"
%}

%pragma(python) include="orientmapdata.spy"
%extern "common/abstractimage.swg"
%extern "common/coord.swg"
%extern "common/IO/stringimage.swg"
%extern "engine/angle2color.swg"
%extern "common/corientation.swg"
%extern "image/oofimage.swg"
%pragma(python) code="from ooflib.SWIG.common.abstractimage import AbstractImagePtr"
%pragma(python) code="from ooflib.SWIG.common.coord import CoordPtr"
%pragma(python) code="from ooflib.SWIG.common.coord import ICoordPtr"
%pragma(python) code="from ooflib.SWIG.common.corientation import COrientABGPtr"
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
  void fillstringimage(StringImage*) const;
};

void registerOrientMap(char*, OrientMap*);
void removeOrientMap(char*);

#endif // ORIENTMAPDATA_SWG
