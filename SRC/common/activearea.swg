// -*- C++ -*-

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

%module(package="ooflib.SWIG.common") activearea

%include "common/typemaps.swg"
%import "common/cmicrostructure.swg"
%import "common/coord.swg"
%import "common/cpixelselection.swg"
%import "common/pixelattribute.swg"

%{
#include "common/activearea.h"
#include "common/ooferror.h"
%}

class ActiveArea : public CPixelSelection {
public:
  ActiveArea(ICoord *iPoint, Coord *Point, CMicrostructure*);
  ~ActiveArea();
  %newobject clone;
  ActiveArea *clone();
  bool isActive(ICoord *iPoint);
  void override(bool);
  bool getOverride();
  void add_pixels(std::vector<ICoord> *iPointList);
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
  %newobject getNames;
  std::vector<std::string> *getNames() const;
};

ActiveAreaList *areaListFromPixel(CMicrostructure*, ICoord *iPoint);

%pythoncode "common/activearea.spy"

#endif // ACTIVEAREA_SWG
