// -*- C++ -*-
// $RCSfile: activearea.C,v $
// $Revision: 1.7 $
// $Author: langer $
// $Date: 2010/03/05 21:56:08 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/activearea.h"


// The one and only nontrivial function in the ActiveArea class itself.
void ActiveArea::add_pixels(std::vector<ICoord> *pxls) {
  bitmap.set(pxls);
  pixset.setFromBitmap(bitmap);
}

ActiveArea::~ActiveArea() {}

ActiveAreasAttributeRegistration *ActiveAreaList::reg=0;


// ActiveArea lists are expected to be small, and keeping them ordered
// is useful for comparisons, so we just do the obvious continuous
// insertion-sort.
void ActiveAreaList::add(const std::string& name) {
  // Maintain sortedness of the list.
  std::list<std::string>::iterator i = areas.begin(); 
  while( i!=areas.end() && (*i) < name) ++i;
  areas.insert(i,name);
}

// Remove benignly does nothing if the name to be removed is not in
// the list.
void ActiveAreaList::remove(const std::string &name) {
  std::list<std::string>::iterator i = areas.begin();
  while( i!=areas.end() && (*i) != name) ++i;
  if (i!=areas.end()) areas.erase(i);
}

// Active areas don't affect microstructure pixel categorization,
// except when saving a Microstructure in a data file.  That means
// that for general purposes, when operator< is used, ActiveAreaLists
// should all be equal to each other.  strictLessThan is used instead
// of operator< when writing data files, so it has to actually compare
// the lists.

bool ActiveAreaList::operator<(const PixelAttribute&) const {
  return false;
}

// An active area list precedes another active area list if it's
// shorter, or if the first unequal component is smaller.
bool ActiveAreaList::strictLessThan(const PixelAttribute &otherbase) const {
  const ActiveAreaList &other = dynamic_cast<const ActiveAreaList&>(otherbase);
  if (areas.size() < other.areas.size()) return true;
  if (other.areas.size() < areas.size()) return false;

  // Warning: Confusing for-loop structure. Iterators are declared
  // outside the loop so that a comma-expression can be used in the
  // "for" statement with the iterators remaining in scope in the body
  // of the loop.  Comma-expresions are lexical scopes, so the
  // "obvious" syntax is, in fact, wrong.
  std::list<std::string>::const_iterator hither,yon;
  for( (hither=areas.begin(),yon=other.areas.begin()); 
       hither!=areas.end(); (++hither,++yon) ) {
    if ((*hither)<(*yon)) return true;
  }
  return false;
}


// This function converts the internal list to a vector, and makes a
// copy, on the assumption that callers will find vectors easier to
// deal with, and may want to molest the data.
std::vector<std::string>* ActiveAreaList::getNames() const {
  std::vector<std::string> *res = new std::vector<std::string>();
  for(std::list<std::string>::const_iterator i = areas.begin();
      i!=areas.end(); ++i) {
    res->push_back(*i);
  }
  return res;
}

void ActiveAreaList::print(std::ostream& o) const {
  o << "ActiveAreaList(";
  std::list<std::string>::const_iterator i;
  int count;
  for(count=areas.size(), i=areas.begin(); i!=areas.end(); --count,++i) {
    o << *i;
    if (count!=1) o << ", ";
  }
}


const std::string ActiveAreasAttributeRegistration::
classname_("ActiveAreasAttributeRegistration");

const std::string ActiveAreasAttributeRegistration::
modulename_("ooflib.SWIG.common.activearea");

ActiveAreasAttributeRegistration::ActiveAreasAttributeRegistration()
  : PxlAttributeRegistration("NamedActiveArea")
{
  ActiveAreaList::reg = this;
}

PixelAttribute *
ActiveAreasAttributeRegistration::createAttribute(const ICoord &c) const {
  return new ActiveAreaList();
}


// Utility functions for IO operations.

ActiveAreaList *areaListFromPixel(const CMicrostructure *ms, 
				  const ICoord *pxl) {
  const Array<PixelAttribute*> &attrMap = ActiveAreaList::reg->map(ms);
  return dynamic_cast<ActiveAreaList*>(attrMap[*pxl]);
}


