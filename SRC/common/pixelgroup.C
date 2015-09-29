// -*- C++ -*-
// $RCSfile: pixelgroup.C,v $
// $Revision: 1.48 $
// $Author: langer $
// $Date: 2014/09/12 20:32:17 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include <assert.h>

#include "common/IO/bitoverlay.h"
#include "common/activearea.h"
#include "common/array.h"
#include "common/cmicrostructure.h"
#include "common/pixelattribute.h"
#include "common/pixelgroup.h"
#include "common/tostring.h"
#include "common/trace.h"
#include <algorithm>		// std::sort


// TODO LATER: Would it be more efficient to base PixelGroup on a
// std::set instead of a std::vector? 

//----------- 

const std::string
PixelGroupAttributeRegistration::classname_("PixelGroupAttributeRegistration");
const std::string
PixelGroupAttributeRegistration::modulename_("ooflib.SWIG.common.pixelgroup");

static PixelGroupAttributeRegistration *reg = 0;

PixelGroupAttributeRegistration::PixelGroupAttributeRegistration()
  : PxlAttributeRegistration("PixelGroups")
{
#ifdef DEBUG
  assert( reg==0 );
#endif

  reg = this;
}

// -----------

int PixelSet::ngroups(0);

PixelSet::PixelSet(const ICoord *geometry, CMicrostructure *microstructure)
  : id_(ngroups++),
    defunct_(false),
    weeded(true),
    geometry(*geometry),
    microstructure(microstructure)
{
}
  
PixelGroup::PixelGroup(const std::string &name, const ICoord *geometry,
		       CMicrostructure *microstructure)
  : PixelSet(geometry, microstructure),
    meshable_(true),
    name_(name)
{
}

PixelSet::PixelSet(const PixelSet &other)
  : id_(ngroups++),
    defunct_(other.defunct_),
    weeded(true),
    geometry(other.geometry),
    microstructure(other.microstructure)
{
  addWithoutCheck(other.members());
}

PixelGroup::PixelGroup(const std::string &name, const PixelGroup &other)
  : PixelSet(other),
    meshable_(other.meshable_),
    name_(name)
{
}

PixelSet::~PixelSet() {}

PixelGroup::~PixelGroup() {}

void PixelSet::resize(const ICoord *newgeom) {
  member_lock.acquire();
  if(geometry != *newgeom) {
    geometry = *newgeom;
    // Remove all pixels that don't fit in the new geometry.
    weed();
    int n = len();
    int j = 0;			// new index of accepted pixel
    for(int i=0; i<n; i++) {	// loop over old set of pixels
      ICoord pxl = members_[i];
      if(pxl(0) < geometry(0) && pxl(1) < geometry(1)) { // accept this pixel
	if(j < i)
	  members_[j] = members_[i];
	j++;
      }
    }
    members_.resize(j);
  }
  member_lock.release();
}

void PixelSet::set_defunct() {
  defunct_ = true;
}

void PixelGroup::set_defunct() {
  PixelSet::set_defunct();
  Array<PixelAttribute*> &groupMap = reg->map(microstructure);
  weed();
  for(int i=0; i<len(); i++) {
    GroupList *list = dynamic_cast<GroupList*>(groupMap[members_[i]]);
    list->resort();
  }
}

void PixelSet::add(const std::vector<ICoord> *pixels) {
  member_lock.acquire();
  members_.reserve(members_.size() + pixels->size());
  const ActiveArea *aa = microstructure->getActiveArea();
  for(std::vector<ICoord>::size_type i=0; i<pixels->size(); i++) {
    const ICoord &pxl = (*pixels)[i];
    if(aa->isActive(&pxl)) 
      members_.push_back(pxl);
  }
  weeded = false;
  member_lock.release();
}

void PixelSet::addWithoutCheck(const std::vector<ICoord> *pxls) {
  members_.reserve(members_.size() + pxls->size());
  for(std::vector<ICoord>::const_iterator i=pxls->begin(); i<pxls->end(); ++i)
      members_.push_back(*i);
  weeded = false;
}

void PixelGroup::add(const std::vector<ICoord> *pixels) {
  extern PixelGroupAttributeRegistration *reg;
  PixelSet::add(pixels);
  // Update grouplists in microstructure
  Array<PixelAttribute*> &groupMap = reg->map(microstructure);
  for(std::vector<ICoord>::const_iterator i=pixels->begin(); i<pixels->end();
      ++i)
    {
      GroupList *list = dynamic_cast<GroupList*>(groupMap[*i]);
      list->add(this);
    }
  microstructure->recategorize();
}

void PixelGroup::addWithoutCheck(const std::vector<ICoord> *pixels) {
  PixelSet::addWithoutCheck(pixels);
  // Update grouplists in microstructure
  Array<PixelAttribute*> &groupMap = reg->map(microstructure);
  for(std::vector<ICoord>::const_iterator i=pixels->begin(); i<pixels->end();
      ++i)
    {
      GroupList *list = dynamic_cast<GroupList*>(groupMap[*i]);
      list->add(this);
    }
  microstructure->recategorize();
}

void PixelSet::add(const ICoord &pixel) {
  if(microstructure->getActiveArea()->isActive(&pixel)) {
    member_lock.acquire();
    members_.push_back(pixel);
    weeded = false;
    member_lock.release();
  }
}

void PixelGroup::add(const ICoord &pixel) {
  PixelSet::add(pixel);
  Array<PixelAttribute*> &groupMap = reg->map(microstructure);
  GroupList *list = dynamic_cast<GroupList*>(groupMap[pixel]);
  list->add(this);
  microstructure->recategorize();
}

void PixelSet::remove(const std::vector<ICoord> *pixels) {
  std::vector<ICoord> rejects(*pixels);	// copy, so we can sort
  weed();			// sort and weed the group
  std::sort(rejects.begin(), rejects.end()); // sort pixels to be rejected
  unsigned int g = 0;			// next group member to consider
  unsigned int r = 0;			// next reject to consider
  unsigned int newsize = 0;
  const ActiveArea *aa = microstructure->getActiveArea();

  while(g < members_.size() && r < rejects.size()) {
    if(r < rejects.size()-1 && rejects[r]==rejects[r+1]) {
      r++;			// skip duplications in reject list
    }
    else if(members_[g] == rejects[r] && aa->isActive(&rejects[r])) {
      g++;			// skip rejects in member list
    }
    else if(members_[g] < rejects[r]) {
      // retain nonrejected members
      if(g > newsize)
	members_[newsize] = members_[g];
      g++;
      newsize++;
    }
    else {
      // go on to next reject
      r++;
    }
  }
  // Include all remaining group members left after we've examined all
  // the rejects.
  while(g < members_.size()) {
    members_[newsize++] = members_[g++];
  }
  members_.resize(newsize);
}

void PixelSet::removeWithoutCheck(const std::vector<ICoord> *pixels) {
  std::vector<ICoord> rejects(*pixels);	// copy, so we can sort
  member_lock.acquire();
  weed();			// sort and weed the group
  std::sort(rejects.begin(), rejects.end()); // sort pixels to be rejected
  unsigned int g = 0;			// next group member to consider
  unsigned int r = 0;			// next reject to consider
  unsigned int newsize = 0;

  while(g < members_.size() && r < rejects.size()) {
    if(r < rejects.size()-1 && rejects[r]==rejects[r+1]) {
      r++;			// skip duplications in reject list
    }
    else if(members_[g] == rejects[r]) {
      g++;			// skip rejects in member list
    }
    else if(members_[g] < rejects[r]) {
      // retain nonrejected members
      if(g > newsize)
	members_[newsize] = members_[g];
      g++;
      newsize++;
    }
    else {
      // go on to next reject
      r++;
    }
  }
  // Include all remaining group members left after we've examined all
  // the rejects.
  while(g < members_.size()) {
    members_[newsize++] = members_[g++];
  }
  members_.resize(newsize);
  member_lock.release();
}

void PixelGroup::remove(const std::vector<ICoord> *pixels) {
  PixelSet::remove(pixels);
  // Update grouplists in microstructure
  if(microstructure) {
    Array<PixelAttribute*> &groupMap = reg->map(microstructure);
    for(std::vector<ICoord>::const_iterator i=pixels->begin(); i<pixels->end();
	++i) {
      GroupList *list = dynamic_cast<GroupList*>(groupMap[*i]);
      list->remove(this);
    }
    microstructure->recategorize();
  }
}

ICoord PixelSet::pop() {
  member_lock.acquire();
  weed();
  ICoord pxl = members_[members_.size()-1];
  members_.pop_back();
  member_lock.release();
  return pxl;
}

// ICoord PixelGroup::pop() {
//   ICoord pxl = PixelSet::pop();
//   return pxl;
// }

void PixelSet::clear() {
  member_lock.acquire();
  members_.clear();
  weeded = true;
  member_lock.release();
}

void PixelGroup::clear() {
  // Update grouplists in microstructure
  Array<PixelAttribute*> &groupMap = reg->map(microstructure);
  member_lock.acquire();
  for(std::vector<ICoord>::const_iterator i=members_.begin();
      i<members_.end(); ++i)
    {
      GroupList *list = dynamic_cast<GroupList*>(groupMap[*i]);
      list->remove(this);
    }
  member_lock.release();
  microstructure->recategorize();
  PixelSet::clear();
}

void PixelSet::setFromBitmap(const BitmapOverlay &bitmap) {
  // This is used to synchronize the Bitmap and the PixelSet that
  // are stored in a CPixelSelection.  It does *not* check the active
  // area, because it's assumed that the Bitmap is already set
  // correctly.
  const ICoord &bitmapsize = bitmap.sizeInPixels();
  int xmin = bitmapsize(0) < geometry(0) ? bitmapsize(0) : geometry(0);
  int ymin = bitmapsize(1) < geometry(1) ? bitmapsize(1) : geometry(1);
#if DIM == 2
  const Array<bool> sub(bitmap.data.subarray(ICoord(0,0), ICoord(xmin, ymin)));
#elif DIM == 3
  int zmin = bitmapsize(2) < geometry(2) ? bitmapsize(2) : geometry(2);
  const Array<bool> sub(bitmap.data.subarray(ICoord(0,0,0), ICoord(xmin, ymin, zmin)));
#endif
  member_lock.acquire();
  for(Array<bool>::const_iterator i=sub.begin(); i!=sub.end(); ++i)
    if(*i)
      members_.push_back(i.coord());
  weeded = false;
  member_lock.release();
}

// HERE: Commented out for detection...
//void PixelGroup::setFromBitmap(const BitmapOverlay &bitmap) {
//  PixelSet::setFromBitmap(bitmap);
//}

// void PixelSet::copy(const PixelSet *other) {
//   int n = other->len();
//   members_.resize(n);
//   const std::vector<ICoord> &otherpts = *other->members();
//   for(int i=0; i<n; i++)
//     members_[i] = otherpts[i];
// }

int PixelSet::len() const {
  member_lock.acquire();
  weed();
  int res = members_.size();
  member_lock.release();
  return res;
}

// Should be called with the member_lock acquired.
void PixelSet::weed() const {
  if(weeded) return;
  if(!members_.empty()) {
    std::sort(members_.begin(), members_.end());
    std::vector<ICoord>::iterator newend = std::unique(members_.begin(),
						       members_.end());
    members_.erase(newend, members_.end());
   }
  weeded = true;
}



const std::vector<ICoord> *PixelSet::members() const {
  weed();
  return &members_;
}

void PixelGroup::set_meshable(bool deshabille) {
  meshable_ = deshabille;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The CMicrostructure keeps an array of GroupList objects, indicating
// to which groups each pixel belongs.  GroupList is a subclass of
// PixelAttribute, and as such is used to categorize pixels.

// GroupList::data is a std::set instead of a std::vector because the
// names are sorted.

void GroupList::add(PixelGroup *group) {
  data.push_back(group);
  sorted = false;
}

void GroupList::remove(PixelGroup *group) {
  sort();
  for(std::vector<PixelGroup*>::iterator i=data.begin(); i<data.end(); ++i) {
    if(*i == group) {
      data.erase(i);
      return;
    }
  }
}

bool GroupList::contains(const PixelGroup *group) const {
  sort();
  for(std::vector<PixelGroup*>::const_iterator i=data.begin(); i<data.end(); ++i)
    {
      if(*i == group)
	return true;
    }
  return false;
}

const std::vector<PixelGroup*> &GroupList::members() const {
  sort();
  return data;
}

void GroupList::sort() const {
  if(sorted) return;
  // remove defunct groups
  std::vector<std::vector<PixelGroup*>::iterator> defunctgroups;
  for(std::vector<PixelGroup*>::iterator i=data.begin(); i<data.end(); ++i) {
    if((*i)->is_defunct())
      defunctgroups.push_back(i);
      // i = data.erase(i);
  }
  for(unsigned int j=0; j<defunctgroups.size(); j++)
    data.erase(defunctgroups[j]);
  // sort the remainder
  std::sort(data.begin(), data.end(), groupsorter);
  // remove duplicates
  std::vector<PixelGroup*>::iterator newend = 
    std::unique(data.begin(), data.end());
  data.erase(newend, data.end());
  sorted = true;
}

bool GroupList::groupsorter(const PixelGroup *a, const PixelGroup *b) {
  return a->name() < b->name();
}

bool GroupList::operator<(const PixelAttribute &other) const {
  // Compare two lists of groups, skipping those that aren't meshable.
  const GroupList &otherlist = dynamic_cast<const GroupList&>(other);
  const std::vector<PixelGroup*> &grps = members();
  const std::vector<PixelGroup*> &othergrps = otherlist.members();
  std::vector<PixelGroup*>::const_iterator i= grps.begin();
  std::vector<PixelGroup*>::const_iterator j = othergrps.begin();
  while(true) {
    while(i != grps.end() && !(*i)->is_meshable())
      ++i;
    while(j != othergrps.end() && !(*j)->is_meshable())
      ++j;
    if(i == grps.end()) {
      if(j != othergrps.end()) {
	return true; // grps contains fewer meshable groups than othergrps
      }
      else {
	return false; 		// grouplists are identical.
      }
    }
    if(j == othergrps.end()) {
      return false; // grps contains more meshable groups than othergrps
    }

    if(*i < *j) {
      return true;
    }
    if(*j < *i) {
      return false;
    }
    // grouplists are identical so far
    ++i;
    ++j;
  }
  throw ErrProgrammingError("Impossible condition in GroupList::operator<",
			    __FILE__, __LINE__);
}

bool GroupList::strictLessThan(const PixelAttribute &other) const {
  const GroupList &otherlist = dynamic_cast<const GroupList&>(other);
  const std::vector<PixelGroup*> &grps = members();
  const std::vector<PixelGroup*> &othergrps = otherlist.members();
  return grps < othergrps;
}

void GroupList::print(std::ostream &os) const {
  const std::vector<PixelGroup*> &grps = members();
  if(grps.size() > 0) {
    os << "Groups(";
    for(std::vector<PixelGroup*>::size_type i=0; i<grps.size(); i++) {
      if(i > 0) os << ", ";
      os << grps[i]->name();
    }
    os << ")";
  }
  else
    os << "[No Groups]";
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::vector<std::string> *pixelGroupNames(const CMicrostructure *microstructure,
					  const ICoord *where)
{
  Array<PixelAttribute*> groupMap = reg->map(microstructure);
  GroupList *list = dynamic_cast<GroupList*>(groupMap[*where]);
  const std::vector<PixelGroup*> &groups = list->members();
  std::vector<std::string> *roster = new std::vector<std::string>;
  roster->reserve(groups.size());
  for(std::vector<PixelGroup*>::size_type i=0; i<groups.size(); i++)
    roster->push_back(groups[i]->name());
  return roster;
}

// Does the given group contain the given pixel?
bool pixelGroupQueryPixel(const CMicrostructure &microstructure,
			  const ICoord &where, const PixelGroup *group)
{
  Array<PixelAttribute*> groupMap = reg->map(&microstructure);
  GroupList *list = dynamic_cast<GroupList*>(groupMap[where]);
  return list->contains(group);
}
