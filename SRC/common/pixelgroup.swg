// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PIXELGROUP_SWG
#define PIXELGROUP_SWG

%module pixelgroup
%include "common/typemaps.swg"

%{
#include "common/pixelgroup.h"
#include "common/cmicrostructure.h"
#include "common/ooferror.h"
%}
%import "common/cmicrostructure.swg"
%import "common/pixelattribute.swg"

 //%pragma(python) code="from ooflib.SWIG.common.pixelattribute import PxlAttributeRegistrationPtr"

%nodefaultctor PixelSet;

class PixelSet {
public:
  ~PixelSet();
  int id();
  bool is_defunct();
  void set_defunct();
  void add(ICoordVec *iPointList);
  void addWithoutCheck(ICoordVec *iPointList);
  void remove(ICoordVec *iPointList);
  %newobject clone;
  PixelSet *clone();
  void clear();
  ICoordVec *members();
};

%extend PixelSet {
  int __len__() {
    return self->len();
  }
  const ICoord __getitem__(int i) {
    if(i < 0 || i >= self->len()) {
      throw ErrBadIndex(i, __FILE__, __LINE__);
    }
    return (*self)[i];
  }
 };

class PixelGroup : public PixelSet {
public:
  PixelGroup(char *name, ICoord *iPoint, CMicrostructure *microstructure);
  ~PixelGroup();
  void rename(char*);
  bool is_meshable();
  void set_meshable(bool);
  const string &name();
};

%newobject pixelGroupNames;
StringVec *pixelGroupNames(CMicrostructure*, ICoord *iPoint);

class PixelGroupAttributeRegistration : public PxlAttributeRegistration {
public:
  PixelGroupAttributeRegistration();
  ~PixelGroupAttributeRegistration();
};

%pythoncode "pixelgroup.spy"

#endif // PIXELGROUP_SWG
