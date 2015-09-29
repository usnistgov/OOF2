// -*- C++ -*-
// $RCSfile: activearea.swg,v $
// $Revision: 1.10 $
// $Author: langer $
// $Date: 2014/09/27 21:40:16 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ACTIVEAREA_SWG
#define ACTIVEAREA_SWG

%module cactivearea

%{
#include "common/activearea.h"
%}
%include "common/typemaps.swg"
%extern "common/cpixelselection.swg"
%extern "common/pixelattribute.swg"
%pragma(python) code="from ooflib.SWIG.common.cpixelselection import CPixelSelectionPtr"
%pragma(python) code="from ooflib.SWIG.common.pixelattribute import PxlAttributeRegistrationPtr"
%pragma(python) include="activearea.spy"

class ActiveArea : public CPixelSelection {
public:
  ActiveArea(ICoord *iPoint, Coord *Point, CMicrostructure*);
  ~ActiveArea();
  %new ActiveArea *clone();
  bool isActive(ICoord *iPoint);
  void override(bool);
  bool getOverride();
  void add_pixels(ICoordVec *iPointList);
};

class ActiveAreasAttributeRegistration : public PxlAttributeRegistration {
public:
  ActiveAreasAttributeRegistration();
  PixelAttribute *createAttribute(ICoord&);
};

// PixelAttribute is not SWIG'd, so leave it out.
class ActiveAreaList {
public:
  void add(char *);
  void remove(char *);
  StringVec* getNames();
};

ActiveAreaList *areaListFromPixel(CMicrostructure*, ICoord *iPoint);


#endif // ACTIVEAREA_SWG
