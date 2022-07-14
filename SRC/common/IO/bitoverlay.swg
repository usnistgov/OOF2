// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef BITOVERLAY_SWG
#define BITOVERLAY_SWG

%module(package="ooflib.SWIG.common.IO") bitoverlay

%include "common/typemaps.swg"
%import "common/canvasimage.swg"

%{
#include "common/IO/bitoverlay.h"
#include "oofcanvas/canvasimage.h"
%}
%import "common/coord.swg"
%import "common/timestamp.swg"
%import "common/ccolor.swg"
%import "common/abstractimage.swg"

// %pragma(python) code="from ooflib.SWIG.common.timestamp import TimeStampPtr"
// %pragma(python) code="from ooflib.SWIG.common.ccolor import CColorPtr"
// %pragma(python) code="from ooflib.SWIG.common.abstractimage import AbstractImagePtr"
   
class BitmapOverlay : public AbstractImage {
public:
  BitmapOverlay(Coord *Point, ICoord *iPoint);
  ~BitmapOverlay();
  void resize(Coord *Point, ICoord *iPoint);
  void clear();
  void invert();
  void set(ICoord *iPoint);
  void reset(ICoord *iPoint);
  void toggle(ICoord *iPoint);
  bool get(ICoord *iPoint);
  void copy(BitmapOverlay*);
  bool contains(ICoord *iPoint);
  void setColor(CColor*);
  CColor getBG();
  CColor getFG();
  %newobject makeCanvasImage;
  OOFCanvas::CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);
  
  Coord size();
  ICoord sizeInPixels();
  bool empty();
  %newobject pixels;
  std::vector<ICoord> *pixels(int v);	// all pixels whose value==v
  TimeStamp &getTimeStamp();
};

%pythoncode "common/IO/bitoverlay.spy"

#endif // BITOVERLAY_SWG
