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
  ICoordVec *pixels(int v);	// all pixels whose value==v
  TimeStamp &getTimeStamp();
};

// Use the full path to bitoverlay.spy.  When this file is %imported
// by other swig files, this directory may not be in the swig search
// path.  When this file is %imported, nothing is actually included
// from bitoverlay.spy, but swig for some reason (a bug?) still
// complains when it fails to find the file.
%pythoncode "common/IO/bitoverlay.spy"

#endif // BITOVERLAY_SWG
