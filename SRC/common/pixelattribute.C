// -*- C++ -*-
// $RCSfile: pixelattribute.C,v $
// $Revision: 1.9 $
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

#include <oofconfig.h>

#include "common/pixelattribute.h"
#include "common/cmicrostructure.h"

std::vector<PxlAttributeRegistration*> &
PxlAttributeRegistration::registrations() {
  static std::vector<PxlAttributeRegistration*> vec;
  return vec;
}

PxlAttributeRegistration::PxlAttributeRegistration(const std::string &name)
  : name_(name)
{
  index_ = nRegistrations();
  registrations().push_back(this);
}

Array<PixelAttribute*> &PxlAttributeRegistration::map(const CMicrostructure *ms)
  const
{
  return ms->getAttributeMap(index_);
}

PixelAttributeGlobalData *
PxlAttributeRegistration::globalData(const CMicrostructure *ms) const {
  return ms->getAttributeGlobalData(index_);
}

int nAttributes() {
  return PxlAttributeRegistration::nRegistrations();
}

const PxlAttributeRegistration *getRegistration(int i) {
  return PxlAttributeRegistration::getRegistration(i);
}

const PxlAttributeRegistration *PxlAttributeRegistration::getRegistration(int i)
{				// static
  return registrations()[i];
}
						   

std::ostream &operator<<(std::ostream &os, const PixelAttribute &pa) {
  pa.print(os);
  return os;
}
