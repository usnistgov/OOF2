// -*- C++ -*-
// $RCSfile: pixelgroup.swg,v $
// $Revision: 1.29 $
// $Author: langer $
// $Date: 2014/09/27 21:40:26 $

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
%pragma(python) include="pixelgroup.spy"
%extern "common/cmicrostructure.swg"
%extern "common/pixelattribute.swg"

%pragma(python) code="from ooflib.SWIG.common.pixelattribute import PxlAttributeRegistrationPtr"

class PixelSet {
public:
  ~PixelSet();
  int id();
  void resize(ICoord *iPoint);
  bool is_defunct();
  void set_defunct();
  void add(ICoordVec *iPointList);
  void addWithoutCheck(ICoordVec *iPointList);
  void remove(ICoordVec *iPointList);
  %new PixelSet *clone();
  void clear();
  ICoordVec *members();
  %addmethods {
    int __len__() {
      return self->len();
    }
    const ICoord __getitem__(int i) {
      if(i < 0 || i >= self->len()) {
	throw ErrBadIndex(i, __FILE__, __LINE__);
      }
      return (*self)[i];
    }
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

%new StringVec *pixelGroupNames(CMicrostructure*, ICoord *iPoint);

class PixelGroupAttributeRegistration : public PxlAttributeRegistration {
public:
  PixelGroupAttributeRegistration();
  ~PixelGroupAttributeRegistration();
};

#endif // PIXELGROUP_SWG
