// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CPIXELSELECTION_SWG
#define CPIXELSELECTION_SWG

%module(package="ooflib.SWIG.common") cpixelselection

%{
#include "common/cpixelselection.h"
%}

%include "common/typemaps.swg"
%import "common/timestamp.swg"
%import "common/pixelgroup.swg"
%import "common/IO/bitoverlay.swg"
%import "common/coord.swg"

class CPixelSelection {
public:
  CPixelSelection(ICoord *iPoint, Coord *Point, CMicrostructure*);
  ~CPixelSelection();
  %newobject clone;
  CPixelSelection *clone();
  const Coord size();
  const ICoord sizeInPixels();
  bool checkpixel(ICoord *iPoint);

  CMicrostructure *getCMicrostructure();

  void clear();
  void invert();

  void select(PixelSelectionCourier*);
  void unselect(PixelSelectionCourier*);
  void toggle(PixelSelectionCourier*);
  void selectSelected(PixelSelectionCourier*);

  void clearWithoutCheck();
  void invertWithoutCheck();
  void selectWithoutCheck(PixelSelectionCourier*);
  void unselectWithoutCheck(PixelSelectionCourier*);
  void toggleWithoutCheck(PixelSelectionCourier*);

  bool isSelected(ICoord *iPoint);
  void setFromGroup(PixelSet*);
  TimeStamp *getTimeStamp();
  std::vector<ICoord> *members();
  PixelSet *getPixelGroup();
  BitmapOverlay *getBitmap();
  int len();
};

%extend CPixelSelection {
  int __len__() {
    return self->len();
  }
}

%pythoncode "common/cpixelselection.spy"

#endif // CPIXELSELECTION_SWG
