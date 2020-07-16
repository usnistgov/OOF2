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

%module bitoverlay
%include "common/typemaps.swg"

%{
#include "common/IO/bitoverlay.h"
#include "common/IO/OOFCANVAS/canvasimage.h"
typedef OOFCanvas::CanvasImage CanvasImage;
%}
%extern "common/coord.swg"
%extern "common/timestamp.swg"
%extern "common/ccolor.swg"
%extern "common/abstractimage.swg"
%extern "common/IO/OOFCANVAS/oofcanvas.swg"

%pragma(python) code="from ooflib.SWIG.common.timestamp import TimeStampPtr"
%pragma(python) code="from ooflib.SWIG.common.ccolor import CColorPtr"
%pragma(python) code="from ooflib.SWIG.common.abstractimage import AbstractImagePtr"
%pragma(python) code="from ooflib.SWIG.common.IO.OOFCANVAS.oofcanvas import CanvasImagePtr"
   
%pragma(python) include="bitoverlay.spy"

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
  %new CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);
  
  Coord size();
  ICoord sizeInPixels();
  bool empty();
  %new ICoordVec *pixels(int v);	// all pixels whose value==v
  TimeStamp &getTimeStamp();
};

#endif // BITOVERLAY_SWG
