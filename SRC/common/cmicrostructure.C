// -*- C++ -*-
// $RCSfile: cmicrostructure.C,v $
// $Revision: 1.90 $
// $Author: langer $
// $Date: 2014/12/31 01:32:22 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include <algorithm>
#include <assert.h>
#include <iomanip>
#include <iostream>
#include <map>
#include <math.h>		// for sqrt()
#include <stdlib.h>		// for abs()
#include <vector>

#include "common/cmicrostructure.h"
#include "common/coord.h"
#include "common/geometry.h"
#include "common/lock.h"
#include "common/printvec.h"
#include "common/pixelattribute.h"
#include "common/pixelsetboundary.h"

using namespace std;

// TODO: Are groups_attributes_lock and category_lock still required?
// Shouldn't the locks in the Who class be sufficient?

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

long CMicrostructure::globalMicrostructureCount = 0; // used for code testing
static SLock globalMicrostructureCountLock;

long get_globalMicrostructureCount() {
  return CMicrostructure::globalMicrostructureCount;
}

CMicrostructure::CMicrostructure(const std::string &name,
				 const ICoord *isz, const Coord *sz) 
  : pxlsize_(*isz),
    size_(*sz),
    attributeMap(nAttributes()),
    attributeGlobalData(nAttributes()),
    categorized(false),
    ncategories(0),
    name_(name)
{
    globalMicrostructureCountLock.acquire();
    ++globalMicrostructureCount;
    globalMicrostructureCountLock.release();
#if DIM == 2
  delta_ = Coord((*sz)(0)/(*isz)(0), (*sz)(1)/(*isz)(1));
  categorymap = Array<int>((*isz)(0), (*isz)(1));
#elif DIM == 3
  delta_ = Coord((*sz)(0)/(*isz)(0), (*sz)(1)/(*isz)(1), (*sz)(2)/(*isz)(2));
  categorymap = Array<int>((*isz)(0), (*isz)(1), (*isz)(2));
#endif
  // Initialize pixel attribute maps.  Lock probably not actually
  // required -- who would contend for data during construction? --
  // but certainly harmless, and maybe safe.
  // std::cerr << "Acquire." << std::endl;
  // category_lock.acquire();
  for(std::vector<Array<PixelAttribute*> >::size_type i=0; i<attributeMap.size(); i++) {
    Array<PixelAttribute*> &map = attributeMap[i];
    const PxlAttributeRegistration *pareg =
      PxlAttributeRegistration::getRegistration(i);
    attributeGlobalData[i] = pareg->createAttributeGlobalData(this);
    map.resize(pxlsize_);
    for(Array<PixelAttribute*>::iterator j=map.begin(); j!=map.end(); ++j) {
      map[j] = pareg->createAttribute(j.coord());
    }
  }
}

CMicrostructure::~CMicrostructure() {
  destroy();
  globalMicrostructureCountLock.acquire();
  --globalMicrostructureCount;
  globalMicrostructureCountLock.release();
}

// This routine, and the constructor, could lock the
// groups_attributes_lock for writing, but it's probably not required.
void CMicrostructure::destroy() {
  for(PixelGroupDict::iterator i=pixelgroups.begin(); i!=pixelgroups.end(); ++i)
    delete (*i).second;
  pixelgroups.clear();
//   for(std::vector<PixelGroup*>::size_type i=0; i<pixelgroups.size(); i++) 
//     delete pixelgroups[i];
//   pixelgroups.resize(0);

  for(std::vector<PixelSetBoundary*>::iterator i=categoryBdys.begin();
      i!=categoryBdys.end(); ++i)
    delete *i;
  categoryBdys.clear();

  for(std::vector<Array<PixelAttribute*> >::size_type i=0;
      i<attributeMap.size(); i++) {
    Array<PixelAttribute*> &map = attributeMap[i];
    for(Array<PixelAttribute*>::iterator j=map.begin(); j!=map.end(); ++j)
      delete *j;
  }
  attributeMap.resize(0);
  for(std::vector<PixelAttributeGlobalData*>::size_type i=0;
      i<attributeGlobalData.size(); i++)
    delete attributeGlobalData[i];
  attributeGlobalData.resize(0);
}

Array<PixelAttribute*> &CMicrostructure::getAttributeMap(int which) const {
  groups_attributes_lock.read_acquire();
#ifdef DEBUG
  assert(which >= 0);
  assert(which < int(attributeMap.size()) );
#endif
  Array<PixelAttribute*> &res = attributeMap[which];
  groups_attributes_lock.read_release();
  return res;
}

PixelAttributeGlobalData *CMicrostructure::getAttributeGlobalData(int which)
  const 
{
  return attributeGlobalData[which];
}

TimeStamp &CMicrostructure::getTimeStamp() {
  return timestamp;
}

const TimeStamp &CMicrostructure::getTimeStamp() const {
  return timestamp;
}

int CMicrostructure::nGroups() const {
  groups_attributes_lock.read_acquire();
  int res = pixelgroups.size();
  groups_attributes_lock.read_release();
  return res;
}

// Convert a Coord in the physical space to pixel coordinates (without
// rounding to the nearest integer).
Coord CMicrostructure::physical2Pixel(const Coord &pt) const {
#if DIM == 2
  return Coord(pt(0)/delta_(0), pt(1)/delta_(1));
#elif DIM == 3
  return Coord(pt(0)/delta_(0), pt(1)/delta_(1), pt(2)/delta_(2));
#endif
}

// Return the physical space coordinates of the lower-left corner of a
// pixel.
Coord CMicrostructure::pixel2Physical(const ICoord &pxl) const {
#if DIM == 2
  return Coord(pxl(0)*delta_(0), pxl(1)*delta_(1));
#elif DIM == 3
  return Coord(pxl(0)*delta_(0), pxl(1)*delta_(1), pxl(2)*delta_(2));
#endif
}

// Return the physical space coordinates of a given non-integer
// coordinate in pixel space.
Coord CMicrostructure::pixel2Physical(const Coord &pt) const {
#if DIM == 2
  return Coord(pt(0)*delta_(0), pt(1)*delta_(1));
#elif DIM == 3
  return Coord(pt(0)*delta_(0), pt(1)*delta_(1), pt(2)*delta_(2));
#endif
}

// Return the coordinates of the pixel that contains the given point.
ICoord CMicrostructure::pixelFromPoint(const Coord &pt) const {
  Coord p = physical2Pixel(pt);
  int xx = (int) floor(p(0));
  int yy = (int) floor(p(1));
  if(xx >= pxlsize_(0))
    --xx;
  if(xx < 0.0)			// round-off can make xx==-1.
    xx = 0.0;
  if(yy >= pxlsize_(1))
    --yy;
  if(yy < 0.0)
    yy = 0.0;
#if DIM == 2
  return ICoord(xx, yy);
#elif DIM == 3
  int zz = (int) floor(p(2));
  if(zz >= pxlsize_(2))
    --zz;
  if(zz < 0.0)
    zz = 0.0;
  return ICoord(xx, yy, zz);
#endif
}

bool CMicrostructure::contains(const ICoord &ip) const {
  if ((ip(0)>=0 && ip(0)<pxlsize_(0)) && (ip(1)>=0 && ip(1)<pxlsize_(1)))
    return true;
  return false;
}

PixelGroup *CMicrostructure::findGroup(const std::string &name) const {
  // Get an existing group.  Don't create one if it doesn't already exist.
  groups_attributes_lock.read_acquire();
  PixelGroup *res = 0;

  PixelGroupDict::const_iterator i = pixelgroups.find(name);
  if(i != pixelgroups.end())
    res = (*i).second;

//   for(std::vector<PixelGroup*>::size_type i=0; i<pixelgroups.size(); i++) {
//     if(pixelgroups[i]->name() == name) {
//       res = pixelgroups[i];
//       break;
//     }
//   }
  groups_attributes_lock.read_release();
  return res;
}


PixelGroup *CMicrostructure::getGroup(const std::string &name,
				      bool *newness) {
  // Get an existing group, or create one if necessary.  Set the "newness"
  // pointer according to whether or not a new group is created.
  *newness = false;
  // findGroup independently handles the groups_attributes_lock.
  PixelGroup *grp = findGroup(name);
  if(grp) return grp;
  groups_attributes_lock.write_acquire();
  PixelGroup *newgrp = new PixelGroup(name, &pxlsize_, this);
//   pixelgroups.push_back(newgrp);
  pixelgroups.insert(PixelGroupDict::value_type(name, newgrp));
  ++timestamp;
  *newness = true;
  groups_attributes_lock.write_release();
  return newgrp;
}

void CMicrostructure::removeGroup(const std::string &name) {
  // Remove a group from the list of pixel groups, and mark it as
  // defunct.  Defunct groups will be removed from the groupmap later.
  category_lock.acquire();
  groups_attributes_lock.read_acquire();
  
  PixelGroupDict::iterator i = pixelgroups.find(name);
  if(i != pixelgroups.end()) {
    PixelGroup *grp = (*i).second;
    pixelgroups.erase(i);
    grp->set_defunct();
    defunctgroups.push_back(grp);
    categorized = false;
    ++timestamp;
  }
  groups_attributes_lock.read_release();
  category_lock.release();
}

void CMicrostructure::removeAllGroups() {
  category_lock.acquire();
  groups_attributes_lock.read_acquire();
  for(PixelGroupDict::iterator i=pixelgroups.begin(); i!=pixelgroups.end(); ++i)
    {
      PixelGroup *grp = (*i).second;
      grp->set_defunct();
      defunctgroups.push_back(grp);
    }
  pixelgroups.clear();
  categorized = false;
  ++timestamp;
  groups_attributes_lock.read_release();
  category_lock.release();
}

std::vector<std::string> *CMicrostructure::groupNames() const {
  std::vector<std::string> *roster = new std::vector<std::string>;
  groups_attributes_lock.read_acquire();
  for(PixelGroupDict::const_iterator i=pixelgroups.begin();
      i!=pixelgroups.end(); ++i)
    {
      roster->push_back((*i).first);
    }
//   for(std::vector<PixelGroup*>::size_type i=0; i<pixelgroups.size(); ++i)
//     roster->push_back(pixelgroups[i]->name());
  groups_attributes_lock.read_release();
  return roster;
}

void CMicrostructure::renameGroupC(const std::string &oldname,
				   const std::string &newname)
{
  PixelGroup *grp = findGroup(oldname);
  grp->rename(newname);
  pixelgroups.erase(oldname);
  pixelgroups.insert(PixelGroupDict::value_type(newname, grp));
}

// Comparison function for PixelAttribute vectors, used when mapping
// attributes to categories.

static bool ltAttributes(const std::vector<PixelAttribute*> &pavec0,
			 const std::vector<PixelAttribute*> &pavec1)
{
  int n0 = pavec0.size();
  int n1 = pavec1.size();
  int n = n0;
  if(n1 < n0) n = n1;
  for(int i=0; i<n; i++) {
    if(*pavec0[i] < *pavec1[i]) return true;
    if(*pavec1[i] < *pavec0[i]) return false;
  }
  if(n0 < n1) return true;
  return false;
}

// A CatMap is an STL map between vectors of PixelAttributes and
// categories.  This is not the same as CMicrostructure::categorymap,
// which is an array of categories (ie, a map from 2D space to
// categories).

typedef std::map<const std::vector<PixelAttribute*>, int,
		 bool (*)(const std::vector<PixelAttribute*>&,
			  const std::vector<PixelAttribute*>&) > CatMap;

// This function should only be run with the category_lock acquired.
// It is the caller's responsibility to do this -- all callers are
// within the CMicrostructure class, because this function (and the
// lock) is private.
void CMicrostructure::categorize() const {
  groups_attributes_lock.read_acquire();
  CatMap catmap(ltAttributes);	// maps lists of groups to categories
  representativePixels.resize(0);
  for(std::vector<PixelSetBoundary*>::iterator p=categoryBdys.begin();
      p!=categoryBdys.end(); ++p)
    delete *p;
  categoryBdys.clear();

  ncategories = 0;
  int nattrs = attributeMap.size();
  // loop over pixels in the microstructure
  for(Array<int>::iterator i=categorymap.begin(); i!=categorymap.end(); ++i) {

    // TODO: Instead of adding all pixels to the PixelSetBoundary and
    // searching for the edges later, this should check the categories
    // of the neighboring pixels and only add the boundary segments,
    // like the 3D code does.
    
    // construct a list of the attributes of this pixel
    std::vector<PixelAttribute*> attrs(nattrs);
    const ICoord &where = i.coord();
    for(int j=0; j<nattrs; j++)
      attrs[j] = attributeMap[j][where];
    // See if this list of attributes has been seen already
    CatMap::iterator cat = catmap.find(attrs);
    if(cat == catmap.end()) {	// category not found
      catmap[attrs] = ncategories;
      categorymap[i] = ncategories;
      // representativePixels.push_back(i.coord());
      representativePixels.push_back(where);

      PixelSetBoundary *psb = new PixelSetBoundary(this);
      psb->add_pixel(where);
      categoryBdys.push_back(psb);

      ncategories++;
    }
    else {
      categorymap[i] = (*cat).second; // assign previously found category
      categoryBdys[ (*cat).second ]->add_pixel(where);
    }
  }

  // It may not be obvious to the casual reader, but at this point the
  // defunct pixel groups have been removed from the GroupLists, and
  // so the groups can actually be deleted.  What has happened is that
  // the search for categories has called operator<() on pairs of
  // PixelAttributes.  GroupList is a PixelAttribute.  GroupList's
  // operator<() calls GroupList.members(), which sorts the list and
  // removes the defunct groups from it.  PixelGroups are the only
  // PixelAttribute that is specifically stored in the Microstructure,
  // so they get special treatment here.

  if(defunctgroups.size() > 0) {
    for(std::vector<PixelGroup*>::size_type i=0; i<defunctgroups.size(); ++i)
      delete defunctgroups[i];
    defunctgroups.resize(0);
  }

  // Find the boundaries.
  for(std::vector<PixelSetBoundary*>::iterator i = categoryBdys.begin();
      i!=categoryBdys.end(); ++i ) {
    (*i)->find_boundary();
  }
 categorized = true;
 groups_attributes_lock.read_release();
} // end CMicrostructure::categorize()

unsigned int CMicrostructure::nCategories() const {
  // std::cerr << "Acquire, nCategories." << std::endl;
  category_lock.acquire();
  if(!categorized)
    categorize();
  unsigned int res = ncategories;
  category_lock.release();
  // std::cerr << "Release." << std::endl;
  return res;
}

int CMicrostructure::category(const ICoord *where) const {
  // std::cerr << "Acquire, category1" << std::endl;
  category_lock.acquire();
  if(!categorized)
    categorize();
  int cat = categorymap[*where];
  category_lock.release();
  // std::cerr << "Release." << std::endl;
  return cat;
}

int CMicrostructure::category(const ICoord &where) const {
  // std::cerr << "Acquire, category2" << std::endl;
  category_lock.acquire();
  if(!categorized)
    categorize();
  int res = categorymap[where];
  category_lock.release();
  // std::cerr << "Release." << std::endl;
  return res;
}

// Special version for finding the category of the pixel under an
// arbitrary point.
int CMicrostructure::category(const Coord &where) const {
  // std::cerr << "Acquire, category3." << std::endl;
  category_lock.acquire();
  if(!categorized) 
    categorize();
  int res = categorymap[pixelFromPoint(where)];
  category_lock.release();
  // std::cerr << "Release." << std::endl;
  return res;
}

int CMicrostructure::category(int x, int y) const {
  // std::cerr << "Acquire, category4" << std::endl;
  category_lock.acquire();
  if(!categorized)
    categorize();
  int res = categorymap[ICoord(x,y)];
  category_lock.release();
  // std::cerr << "Release." << std::endl;
  return res;
}

const ICoord &CMicrostructure::getRepresentativePixel(int category) const {
  // std::cerr << "Acquire, getRepPixel." << std::endl;
  category_lock.acquire();
  if(!categorized)
    categorize();
  ICoord &res = representativePixels[category];
  category_lock.release();
  // std::cerr << "Release." << std::endl;
  return res;
}

const Array<int> *CMicrostructure::getCategoryMap() const {
  // std::cerr << "Acquire, getCategoryMap." << std::endl;
  category_lock.acquire();
  if(!categorized)
    categorize();
  category_lock.release();
  // std::cerr << "Released, getCategoryMap." << std::endl;
  return &categorymap;
}

static bool strictLessThan_Attributes(const std::vector<PixelAttribute*> &p0,
				      const std::vector<PixelAttribute*> &p1)
{
  int n0 = p0.size();
  int n1 = p1.size();
  int n = n0;
  if(n1 < n0) n = n1;
  for(int i=0; i<n; i++) {
    if(p0[i]->strictLessThan(*p1[i])) return true;
    if(p1[i]->strictLessThan(*p0[i])) return false;
  }
  if(n0 < n1) return true;
  return false;
}

// getCategoryMapRO() is a combination of getCategoryMap() and
// categorize().  It doesn't compute representative pixels or category
// boundaries, and it is strictly const -- it doesn't even change any
// mutable data in the CMicrostructure.  It uses
// strictLessThan_Attributes instead of operator< when comparing
// PixelAttributes.  It's used when writing a Microstructure to a file.

const Array<int> *CMicrostructure::getCategoryMapRO() const {
  groups_attributes_lock.read_acquire();
#if DIM == 2
  Array<int> *localmap = new Array<int>(pxlsize_(0), pxlsize_(1));
#elif DIM == 3
  Array<int> *localmap = new Array<int>(pxlsize_(0), pxlsize_(1), pxlsize_(2));
#endif
  CatMap catmap(strictLessThan_Attributes);
  int ncats = 0;
  int nattrs = attributeMap.size();
  // loop over pixels in the microstructure
  for(Array<int>::iterator i=localmap->begin(); i!=localmap->end(); ++i) {
    const ICoord &where = i.coord();
    // construct a list of the attributes of this pixel
    std::vector<PixelAttribute*> attrs(nattrs);
    for(int j=0; j<nattrs; j++)
      attrs[j] = attributeMap[j][where];
    // See if this list of attributes has been seen already
    CatMap::iterator cat = catmap.find(attrs);
    if(cat == catmap.end()) {	// category not found
      catmap[attrs] = ncats;
      *i = ncats;
      ncats++;
    }
    else {
      *i = (*cat).second; // assign previously found category
    }
  }
  groups_attributes_lock.read_release();
  return localmap;
}

void CMicrostructure::recategorize() {
  // std::cerr << "Acquire, recategorize." << std::endl;
  category_lock.acquire();
  categorized = false;
  ++timestamp;
  category_lock.release();
  // std::cerr << "Release." << std::endl;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Geometry routines for identifying pixels in the microstructure that
// are under segments and elements. 

// Return a list (vector) of pixels underlying a segment.  It's the
// responsibility of the caller to delete the vector.

std::vector<ICoord> *CMicrostructure::segmentPixels(const Coord &c0,
						    const Coord &c1,
						    bool &vertical_horizontal) const
{
  // Coordinates of endpoints in pixel space (real).
  Coord p0(physical2Pixel(c0));
  Coord p1(physical2Pixel(c1));
  // Coordinates of pixels containing the endpoints (integer).  Note
  // that we *don't* use CMicrostructure::pixelFromPoint() here,
  // because we have to treat the pixel boundary cases differently.
#if DIM==2
  ICoord ip0((int) floor(p0(0)), (int) floor(p0(1)));
  ICoord ip1((int) floor(p1(0)), (int) floor(p1(1)));
#elif DIM==3
  ICoord ip0((int) floor(p0(0)), (int) floor(p0(1)), (int) floor(p0(2)));
  ICoord ip1((int) floor(p1(0)), (int) floor(p1(1)), (int) floor(p1(2)));
#endif

  // If an endpoint lies exactly on a pixel boundary, then the correct
  // choice for the pixel "containing" the endpoint depends on which
  // direction the segment is going.  The rule is that some part of
  // the segment must lie within the selected pixel. 
  if(ip0(0) == p0(0) && ip1(0) < ip0(0))
    ip0(0) -= 1;
  if(ip1(0) == p1(0) && ip0(0) < ip1(0))
    ip1(0) -= 1;
  if(ip0(1) == p0(1) && ip1(1) < ip0(1))
    ip0(1) -= 1;
  if(ip1(1) == p1(1) && ip0(1) < ip1(1))
    ip1(1) -= 1;
#if DIM==3
  if(ip0(2) == p0(2) && ip1(2) < ip0(2))
    ip0(2) -= 1;
  if(ip1(2) == p1(2) && ip0(2) < ip1(2))
    ip1(2) -= 1;
#endif

  // Round off error may have put a point out of bounds.  Fix it.
  if(ip0(0) == pxlsize_(0)) ip0(0) -= 1;
  if(ip0(1) == pxlsize_(1)) ip0(1) -= 1;
  if(ip1(0) == pxlsize_(0)) ip1(0) -= 1;
  if(ip1(1) == pxlsize_(1)) ip1(1) -= 1;
  if(ip0(0) < 0) ip0(0) = 0;
  if(ip0(1) < 0) ip0(1) = 0;
  if(ip1(0) < 0) ip1(0) = 0;
  if(ip1(1) < 0) ip1(1) = 0;
#if DIM==3
  if(ip0(2) == pxlsize_(2)) ip0(2) -= 1;
  if(ip1(2) == pxlsize_(2)) ip1(2) -= 1;
  if(ip0(2) < 0) ip0(2) = 0;
  if(ip1(2) < 0) ip1(2) = 0;
#endif

  // For vertical and horizontal segments that exactly lie along
  // the pixel boundaries, we need to pick a right row or column of pixels.
  // For instance,
  //
  //  |    element B  |
  //  |xxxxxxxxxxxxxxx|
  //  b---------------a   segment a-b lies on the pixel boundary
  //  |ooooooooooooooo|
  //  |    element A  |
  //
  //  From element A's point of view, pixels along the segment a-b
  //  should be "ooooo", whereas from element B's p.o.v, corresponding
  //  pixels should be "xxxxx".
  //  Followings will deal with this adjustment.


  vertical_horizontal=false;
#if DIM==2
  // This assumes we are traversing an element in counter clockwise
  // order, which we can only do in 2D.  Here, we are trying to get
  // the pixels that lie on the inside of the element.  We'll have to
  // use different conditions in 3D to figure out which side is the
  // inside. 
  // Horizontal
  if ((p0(1) == p1(1) && p0(1) == ip0(1)) && p0(0) > p1(0)) {
    if(ip0(1) >= 1) ip0(1) -= 1;
    if(ip1(1) >= 1) ip1(1) -= 1;
    vertical_horizontal=true;
  }
  // Vertical 
  if ((p0(0) == p1(0) && p0(0) == ip0(0)) && p0(1) < p1(1)) {
    if(ip0(0) >= 1) ip0(0) -= 1;
    if(ip1(0) >= 1) ip1(0) -= 1;
    vertical_horizontal=true;
  }
#elif DIM==3 
  //TODO 3D: Figure out how what conditions to use to get the inside.
  // We need to pass in information about which direction to perturb
  // in.  This needs to be chosen carefully, using element data such
  // that this direction is not along a plane.
//   // Horizontal
//   if ((p0(1) == p1(1) && p0(1) == ip0(1))) {
//     vertical_horizontal=true;
//   }
//   // Vertical 
//   if ((p0(0) == p1(0) && p0(0) == ip0(0))) {
//     vertical_horizontal=true;
//   }
//   // The other Horizontal
//   if ((p0(2) == p1(2) && p0(2) == ip0(2))) {
//     vertical_horizontal=true;
//   }
#endif

  // For vertical and horizontal segments on skeleton(microstructure)
  // edges, all that matters is that the chosen pixels aren't outside
  // the microstructure.  After the preceding check, the only way that
  // an end pixel can be outside is if the segment lies along the top
  // or right edges.
  int maxx = pxlsize_(0);
  int maxy = pxlsize_(1);
  if(ip0(0) == maxx && ip1(0) == maxx) {
    ip0(0) = maxx - 1;
    ip1(0) = maxx - 1;
  }
  if(ip0(1) == maxy && ip1(1) == maxy) {
    ip0(1) = maxy - 1;
    ip1(1) = maxy - 1;
  }
#if DIM==3
  int maxz = pxlsize_(2);
  if(ip0(2) == maxz && ip1(2) == maxz) {
    ip0(2) = maxz - 1;
    ip1(2) = maxz - 1;
  }
#endif

  ICoord id = ip1 - ip0;	// distance between pixel endpoints

#if DIM==2
  if(id(0) == 0 && id(1) == 0) { // segment is entirely within one pixel
    return new std::vector<ICoord>(1, ip0);
  }
  
  if(id(0) == 0) {	
    // Segment is contained within a single column of pixels.
    int npix = abs(id(1)) + 1;
    std::vector<ICoord> *pixels = new std::vector<ICoord>(npix);
    int x = ip0(0);
    int y0 = (ip0(1) < ip1(1)) ? ip0(1) : ip1(1);
    for(int i=0; i<npix; i++)
      (*pixels)[i] = ICoord(x, y0+i);
    return pixels;
  }
  
  if(id(1) == 0) {	
    // Segment is contained within a single row of pixels.
    int npix = abs(id(0)) + 1;
    std::vector<ICoord> *pixels = new std::vector<ICoord>(npix);
    int y = ip0(1);
    int x0 = (ip0(0) < ip1(0)) ? ip0(0) : ip1(0);
    for(int i=0; i<npix; i++)
      (*pixels)[i] = ICoord(x0+i, y);
    return pixels;
  }

  // segment is diagonal
  if(abs(id(0)) >= abs(id(1))) {
    // x range is bigger than y range, so loop over x.
    // Make sure that p0 is to the left of p1.
    if(ip0(0) > ip1(0)) {
      ICoord itemp(ip1);
      ip1 = ip0;
      ip0 = itemp;
      Coord temp(p1);
      p1 = p0;
      p0 = temp;
    }
    std::vector<ICoord> *pixels = new std::vector<ICoord>;
    pixels->reserve(2*abs(id(0))); // biggest possible size
    double x0 = p0(0);
    double y0 = p0(1);
    double slope = (p1(1) - y0)/(p1(0) - x0);
    pixels->push_back(ip0);
    // Iterate over columns of pixels.  Compute the y intercepts at
    // the boundaries between the columns (ie, integer values of x).
    // Whenever the integer part of the y intercept changes, we need
    // to include an extra pixel (at the new y value) in the previous
    // column.
    int lasty = ip0(1);	// previous integer part of y intercept
    for(int x=ip0(0)+1; x<=ip1(0); ++x) {
      int y = int(floor(y0 + slope*(x-x0)));
      if(y >=0 && y < maxy) {
	if(y != lasty) {
	  pixels->push_back(ICoord(x-1, y));
	}
	pixels->push_back(ICoord(x,y));
      }
      lasty = y;
    }
    // The last pixel may not have been included yet, if there's one
    // more y intercept change to come, so make sure it's included.
    if(pixels->back() != ip1)
      pixels->push_back(ip1);
    return pixels;
  } // abs(id(0)) >= abs(id(1))
  
  // abs(id(1)) > abs(id(0))
  // y range is bigger than x range, so loop over y.
  if(ip0(1) > ip1(1)) {
    ICoord itemp(ip1);
    ip1 = ip0;
    ip0 = itemp;
    Coord temp(p1);
    p1 = p0;
    p0 = temp;
  }
  std::vector<ICoord> *pixels = new std::vector<ICoord>;
  pixels->reserve(2*abs(id(1)));
  double x0 = p0(0);
  double y0 = p0(1);
  double slope = (p1(0) - x0)/(p1(1) - y0); // dx/dy
  pixels->push_back(ip0);
  int lastx = ip0(0);
  // iterate over rows of pixels
  for(int y=ip0(1)+1; y<=ip1(1); ++y) {
    int x = int(floor(x0 + slope*(y-y0)));
    if(x >= 0 && x < maxx) {
      if(x != lastx)
	pixels->push_back(ICoord(x, y-1));
      pixels->push_back(ICoord(x,y));
    }
    lastx = x;
  }
  if(pixels->back() != ip1)
    pixels->push_back(ip1);
  return pixels;

#elif DIM==3

  if(id(0) == 0 && id(1) == 0 && id(2) == 0) { // segment is entirely within one pixel
    return new std::vector<ICoord>(1, ip0);
  }

  ICoord start, increment;
  int npix = 0;
  bool line = false, plane = false;
  int i = -1, j = -1, k = -1;
  if(id(0) == 0 && id(2) == 0) {	
    // Segment is contained within a single y-column of pixels.
    i = 1;
    j = 2;
    k = 0;
    line = true;
  }

  if(id(1) == 0 && id(2) == 0) {	
    // Segment is contained within a single x-row of pixels.
    i = 0;
    j = 1;
    k = 2;
    line = true;
  }

  if(id(0) == 0 && id(1) == 0) {	
    // Segment is contained within a single z-column of pixels.
    i = 2;
    j = 0;
    k = 1;
    line = true;
  }

  if(line) {
    npix = abs(id(i)) + 1;
    start(i) = (ip0(i) < ip1(i)) ? ip0(i) : ip1(i);
    start(j) = ip0(j);
    start(k) = ip0(k);
    increment(i) = 1;
    increment(j) = increment(k) = 0;
    std::vector<ICoord> *pixels = new std::vector<ICoord>(npix);
    for(int i=0; i<npix; i++) 
      (*pixels)[i] = start+increment*i;
    return pixels;
  }

  double slope = 0;
  int x = 0, y = 0, z = 0, lasty = 0;
  double x0 = 0, y0 = 0;

  // swap p0 and p1 if they are not in the right order.  Making a huge
  // if condition so we don't have to repeat these few lines of code
  // 6 times.
  if( ( id(2) == 0 &&
	// z-plane with bigger x-range
	(( abs(id(0)) >= abs(id(1)) && ip0(0) > ip1(0) ) || 
	 // z-plane with bigger y-range
	 ( abs(id(1)) > abs(id(0)) && ip0(1) > ip1(1) )) ) 
      ||
      ( id(1) == 0 &&
	// y-plane with bigger z-range
	(( abs(id(2)) >= abs(id(0)) && ip0(2) > ip1(2) ) || 
	 // y-plane with bigger x-range
	 ( abs(id(0)) > abs(id(2)) && ip0(0) > ip1(0) )) )
      || 
      ( id(0) == 0 &&
	// x-plane with bigger z-range
	(( abs(id(2)) >= abs(id(1)) && ip0(2) > ip1(2) ) || 
	 // x-plane with bigger y-range
	 ( abs(id(1)) > abs(id(2)) && ip0(1) > ip1(1) )) )
      ) {
    ICoord itemp(ip1);
    ip1 = ip0;
    ip0 = itemp;
    Coord temp(p1);
    p1 = p0;
    p0 = temp;
  }

  if(id(2) == 0) {
    // segment is in a z-plane
    k = 2;
    z = ip0(2);
    if(abs(id(0)) >= abs(id(1))) {
      // loop over x
      i = 0;
      j = 1;
    }
    else {
      i = 1;
      j = 0;
    }
    plane = true;
  }
  if(id(1) == 0) {
    // segment is in a y-plane
    k = 1;
    z = ip0(1);
    if(abs(id(2)) >= abs(id(0))) {
      // loop over z
      i = 2;
      j = 0;
    }
    else {
      i = 0;
      j = 2;
    }
    plane = true;
  }
  if(id(0) == 0) {
    // segment is in an x-plane
    k = 0;
    z = ip0(0);
    if(abs(id(2)) >= abs(id(1))) {
      // loop over z
      i = 2;
      j = 1;
    }
    else {
      i = 1;
      j = 2;
    }
    plane = true;
  }
  
  // for simplicity, i and x indicate the coordinate we are looping
  // over, j and y indicate the other varying coord, and k and z refer
  // to the fixed coord.
  if(plane) {
    x0 = p0(i);
    y0 = p0(j);
    slope = (p1(j) - y0)/(p1(i) - x0);    
    std::vector<ICoord> *pixels = new std::vector<ICoord>;
    pixels->reserve(2*abs(id(i))); // biggest possible size
    pixels->push_back(ip0);
    // Iterate over columns of pixels.  Compute the y intercepts at
    // the boundaries between the columns (ie, integer values of x).
    // Whenever the integer part of the y intercept changes, we need
    // to include an extra pixel (at the new y value) in the previous
    // column.
    lasty = ip0(j);	// previous integer part of y intercept
    for(x = ip0(i)+1; x <= ip1(i); ++x) {
      y = int(floor(y0 + slope*(x-x0)));
      if(y >= 0 && y < maxy) {
	if(y != lasty) {
	  ICoord vox1;
	  vox1(i) = x-1;
	  vox1(j) = y;
	  vox1(k) = z;
	  pixels->push_back(vox1);
	}
	ICoord vox2;
	vox2(i) = x;
	vox2(j) = y;
	vox2(k) = z;
	pixels->push_back(vox2);
      }
      lasty = y;
    }    
    // The last pixel may not have been included yet, if there's one
    // more y intercept change to come, so make sure it's included.
    if(pixels->back() != ip1)
      pixels->push_back(ip1);
    return pixels;
  }

  // if we haven't returned by now, then the segment varies in all 3
  // coords. 
  int max = 0;
  for(int c = 0; c < 3; ++c) {
    if(abs(id(c)) > max) {
      max = id(c);
      i = c;
      if(abs(id( (c+1) % 3)) > abs(id( (c+2) % 3))) {
	j = (c+1) % 3;
	k = (c+2) % 3;
      }
      else {
	j = (c+2) % 3;
	k = (c+1) % 3;
      }
    }
  }

  x0 = p0(i);
  y0 = p0(j);
  int z0 = p0(k);
  slope = (p1(j) - y0)/(p1(i) - x0);  
  double slopez = (p1(k) - z0)/(p1(i) - x0);
  std::vector<ICoord> *pixels = new std::vector<ICoord>;
  pixels->reserve(2*abs(id(i))); // biggest possible size
  pixels->push_back(ip0);
  // Iterate over columns of pixels.  Compute the y intercepts at
  // the boundaries between the columns (ie, integer values of x).
  // Whenever the integer part of the y intercept changes, we need
  // to include an extra pixel (at the new y value) in the previous
  // column.
  lasty = ip0(j);	// previous integer part of y intercept
  int lastz = ip0(k);
  for(x = ip0(i)+1; x <= ip1(i); ++x) {
    y = int(floor(y0 + slope*(x-x0)));
    z = int(floor(z0 + slopez*(x-x0)));
    if(y >= 0 && y < maxy) {
      if(y != lasty || z != lastz) {
	ICoord vox1;
	vox1(i) = x-1;
	vox1(j) = y;
	vox1(k) = z;
	pixels->push_back(vox1);
      }
      ICoord vox2;
      vox2(i) = x;
      vox2(j) = y;
      vox2(k) = z;
      pixels->push_back(vox2);
    }
    lasty = y;
    lastz = z;
  }    
  // The last pixel may not have been included yet, if there's one
  // more y intercept change to come, so make sure it's included.
  if(pixels->back() != ip1)
    pixels->push_back(ip1);
  return pixels;
  

  
#endif

}

static const ICoord east(1, 0);
static const ICoord west(-1, 0);
static const ICoord north(0, 1);
static const ICoord south(0, -1);
static const ICoord northeast(1, 1);
static const ICoord northwest(-1, 1);
static const ICoord southeast(1, -1);
static const ICoord southwest(-1, -1);

MarkInfo::MarkInfo(const ICoord &size)
  : markedpixels(size, false)
{
  // Initial setting of markedregion will be overwritten... why is it done?
  markedregion = markedpixels.subarray(ICoord(0,0), markedpixels.size());
}


// Set the bounds of the marking region and clear it.  The
// markedpixels array is an array of booleans, used as an intermediate
// result when marking complicated things like elements.

MarkInfo *CMicrostructure::beginMarking(const CRectangle &bbox) const {
  MarkInfo *mm = new MarkInfo(sizeInPixels());
  ICoord p0 = pixelFromPoint(bbox.lowerleft());
  ICoord p1 = pixelFromPoint(bbox.upperright()) + northeast;
  if(p1(0) >= pxlsize_(0)) p1(0) = pxlsize_(0);
  if(p1(1) >= pxlsize_(1)) p1(1) = pxlsize_(1);
  mm->markedregion = mm->markedpixels.subarray(p0, p1);
  mm->markedregion.clear(false);
  return mm;
}

// Return a vector containing all the marked pixels.  It's the
// responsibility of the caller to delete the vector.

std::vector<ICoord> *CMicrostructure::markedPixels(MarkInfo *mm) const {
  return mm->markedregion.pixels(true); // returns new'd vector
}

// Mark the pixels underlying a segment.

void CMicrostructure::markSegment(MarkInfo *mm, 
				  const Coord &c0, const Coord &c1) const
{
  bool dummy;
  const std::vector<ICoord> *pixels = segmentPixels(c0, c1, dummy);
//   std::cerr << "CMicrostructure::markSegment: c0=" <<  c0 << " c1=" << c1 << std::endl;
  for(std::vector<ICoord>::const_iterator pxl=pixels->begin();
      pxl<pixels->end(); ++pxl)
    {
//       std::cerr << "CMicrostructure::markSegment: pxl=" << *pxl << std::endl;
      mm->markedregion.set(*pxl);
    }
//   std::cerr << "CMicrostructure:markSegment: deleting pixels" << std::endl;
  delete pixels;
//   std::cerr << "CMicrostructure::markSegment: done" << std::endl;
}


// Mark the pixels under a triangle by marking the pixels under its
// edges, then using a burn algorithm to mark the ones inside.

void CMicrostructure::markTriangle(MarkInfo *mm, const Coord &c0,
				   const Coord &c1, const Coord &c2)
  const
{
  markSegment(mm, c0, c1);
  markSegment(mm, c1, c2);
  markSegment(mm, c2, c0);
  // Find an unmarked point at which to start the burn algorithm.  For
  // small or narrow triangles, the center point may lie within a
  // pixel's distance of the edge and be already marked.
  ICoord start = pixelFromPoint(1./3.*(c0 + c1 + c2));
  if(mm->markedregion[start]) {
    // Center is already marked.  Unmarked pixels, if any, will lie
    // near the triangle's shortest edge.  Look for an unmarked pixel
    // by starting at the midpoint of the shortest edge and moving
    // towards the center of the triangle.  This code is really ugly
    // since it hardly seems worthwhile to put c0,c1,c2 in an array
    // and iterate over them.
    int shortest = 0;
    double shortlen = norm2(c1 - c2);
    double dd = norm2(c2 - c0);
    if(dd < shortlen) {
      shortlen = dd;
      shortest = 1;
    }
    dd = norm2(c0 - c1);
    if(dd < shortlen) {
      shortest = 2;
    }
    Coord mid;			// midpoint of shortest side
    Coord r;			// unit vector from center of short
				// side toward the opposite corner.
    switch (shortest) {
    case 0:
      mid = 0.5*(c1 + c2);
      r = c0 - mid;
      break;
    case 1:
      mid = 0.5*(c2 + c0);
      r = c1 - mid;
      break;
    case 2:
      mid = 0.5*(c0 + c1);
      r = c2 - mid;
      break;
    }
    double normr = sqrt(norm2(r));
    double maxdist = normr/3.0;	// no point in moving beyond center
    r = (1./normr)*r;		// unit vector
    double d = 1.0;
    bool ok = false;		// found a starting point yet?
    while(d < maxdist && !ok) {
      start = pixelFromPoint(mid + d*r);
      if(!mm->markedregion[start])
	ok = true;
      d += 1.0;
    }
    if(!ok) return;		// all interior pixels must already be marked
  }
  // Burn algorithm.  If a site is unmarked, the mark_site routine
  // marks it and puts it on the activesites list.  The main loop
  // (here) removes sites from the list and calls mark_site on their
  // neighbors.  Since the edges of the triangle are already marked,
  // they don't become active, and the burn won't spread beyond the
  // edges.
  std::vector<ICoord> activesites; // sites whose neighbors need to be checked
  mm->mark_site(activesites, start); // come on baby, light my fire
  while(activesites.size() > 0) {
    const ICoord here = activesites.back();
    activesites.pop_back();
    mm->mark_site(activesites, here + east);
    mm->mark_site(activesites, here + west);
    mm->mark_site(activesites, here + north);
    mm->mark_site(activesites, here + south);
    mm->mark_site(activesites, here + northeast);
    mm->mark_site(activesites, here + northwest);
    mm->mark_site(activesites, here + southeast);
    mm->mark_site(activesites, here + southwest);
  }
}

void MarkInfo::mark_site(std::vector<ICoord> &activesites,
			     const ICoord &here)
{
  if(markedregion.contains(here) && !markedregion[here]) {
    markedregion.set(here);
    activesites.push_back(here);
  }
}

void CMicrostructure::endMarking(MarkInfo *mm) const {
  delete mm;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Returns Point instead of bool via the cskel_OutPoint typemap.
bool CMicrostructure::transitionPointWithPoints(const Coord *c0,
						const Coord *c1,
						Coord *point) const
{
  TransitionPointIterator tpIterator(this, *c0, *c1);
  return transitionPointClosest(*c0, *c1, tpIterator, point); 
}


// Find the closest transition point in the segment that ranges
// from c0 to c1.  The TransitionPointIterator stores the vector of pixels.
bool CMicrostructure::transitionPointClosest(const Coord &c0, const Coord &c1, 
					     TransitionPointIterator &tpIterator,
					     Coord *result) const
{

  std::vector<Coord> *transitions = new std::vector<Coord>;
  bool found = false;
  for(tpIterator.begin(); !tpIterator.end(); ++tpIterator) {
    found = true;
    transitions->push_back( pixel2Physical(tpIterator.current()) );
  }

  // Now, we need to sort them out to find the closest
  int tsize = transitions->size();
  if( found && tsize>0){ 
    if(tsize == 1)
      *result = Coord((*transitions)[0]);
    else {
      double min, dist;
      int theone = 0;
      min = norm2((*transitions)[0] - c0);
      for(int i=1; i<tsize; i++) {
	dist = norm2((*transitions)[i] - c0);
	if(dist < min) {
	  min = dist;
	  theone = i;
	}
      }
      *result = Coord((*transitions)[theone]);
    }
  }
  delete transitions;
  
  return found;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Find the point on the line joining c0 and c1 at which the pixel
// category changes, and return it in result.  The return value is
// true if there's exactly one transition point.

bool CMicrostructure::transitionPoint(const Coord &c0, const Coord &c1,
				      Coord *result) const
{

  bool found1 = false;
  for(TransitionPointIterator tpIterator(this, c0, c1); 
      !tpIterator.end(); ++tpIterator) {
    *result = pixel2Physical(tpIterator.current());
    if(found1) {   // found too many transitions
      return false;
    }
    else
      found1 = true;
  }
  return found1;

}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double CMicrostructure::edgeHomogeneity(const Coord &c0, const Coord &c1) const
{

  TransitionPointIterator tpIterator(this, c0, c1); 
  // Check to see if all of the pixels have the same category.  If
  // they do, the homogeneity is 1.0.  It's *important* to do this
  // check, because without it roundoff error can give a result that
  // is less than 1.0.  
  if(tpIterator.end())
    return 1.0;

  std::vector<double> lengths(nCategories(), 0.0);
  Coord prevpt = tpIterator.first();
  Coord finalpt = tpIterator.last();
  for( ; !tpIterator.end(); ++tpIterator) {
    lengths[tpIterator.getPrevcat()] += sqrt(norm2(tpIterator.current() - prevpt));
    prevpt = tpIterator.current();
  }
  lengths[tpIterator.getPrevcat()] += sqrt(norm2(finalpt - prevpt));

  double max = 0.0;
  for(std::vector<double>::size_type i=0; i<lengths.size(); i++) {
    if(max < lengths[i])
      max = lengths[i];
  }

  double normdelta = tpIterator.getNormDelta();

  return max/normdelta;
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// For SnapRefine.
// Modified edgeHomogeneity function that returns the dominant pixel category.
// The homogeneity value and dominant pixel category may depend on the order of
// the coordinate parameters i.e. swig'ed edgeHomogeneityCat(c0,c1) not always equal to
// edgeHomogeneity(c1,c0) because segmentPixels is sensitive to the direction
// c0->c1 (see the comments and implementation of segmentPixels).
double CMicrostructure::edgeHomogeneityCat(const Coord &c0, const Coord &c1, int* cat) const
{

  TransitionPointIterator tpIterator(this, c0, c1); 
  // Check to see if all of the pixels have the same category.  If
  // they do, the homogeneity is 1.0.  It's *important* to do this
  // check, because without it roundoff error can give a result that
  // is less than 1.0.  
  if(tpIterator.end()) {
    *cat = tpIterator.getPrevcat();
    return 1.0;
  }

  std::vector<double> lengths(nCategories(), 0.0);
  Coord prevpt = tpIterator.first();
  Coord finalpt = tpIterator.last();
  for( ; !tpIterator.end(); ++tpIterator) {
    lengths[tpIterator.getPrevcat()] += sqrt(norm2(tpIterator.current() - prevpt));
    prevpt = tpIterator.current();
  }
  lengths[tpIterator.getPrevcat()] += sqrt(norm2(finalpt - prevpt));

  double max = 0.0;
  for(std::vector<double>::size_type i=0; i<lengths.size(); i++) {
    if(max < lengths[i]) {
      *cat = i;
      max = lengths[i];
    }
  }

  double normdelta = tpIterator.getNormDelta();

  return max/normdelta;

}


//This version of transitionPointWithPoints looks at the pixels on both
//sides of the directed line segment c0-c1 if the segment is vertical
//or horizontal and lies at a pixel boundary.
bool
CMicrostructure::transitionPointWithPoints_unbiased(const Coord *c0,
						    const Coord *c1,
						    Coord *point) const
{
  Coord cleft,cright;
  bool bleft, bright, bverticalhorizontal;
  
  const std::vector<ICoord> *pixels = segmentPixels(*c0, *c1, bverticalhorizontal);
  TransitionPointIterator tpIterator1(this, *c0, *c1, pixels);
  bleft = transitionPointClosest(*c0, *c1, tpIterator1, &cleft);  
  if(bverticalhorizontal)
    {
      const std::vector<ICoord> *pixelsright = segmentPixels(*c1, *c0, bverticalhorizontal);
      TransitionPointIterator tpIterator2(this, *c0, *c1, pixelsright);
      bright = transitionPointClosest(*c0, *c1, tpIterator2, &cright);
    }
  else
    {
      bright=false;
    }
  if(bleft && bright) {	     //Pick the one closest to the endpoint c0
    if(norm2(*c0-cleft)<norm2(*c0-cright)) {
      *point=cleft;
    }
    else {
      *point=cright;
    }
    return true;
  }
  else if(bright) {
    *point=cright;
    return true;
  }
  else {
    //This may be garbage
    *point=cleft;
    return bleft;
  }
}

TransitionPointIterator::TransitionPointIterator(
			const CMicrostructure *microstructure,
			const Coord &c0, const Coord &c1) 
{
  MS = microstructure;
  bool dummy;
  pixels = MS->segmentPixels(c0,c1,dummy);
  p0 = MS->physical2Pixel(c0);
  p1 = MS->physical2Pixel(c1);
  begin();
}

TransitionPointIterator::TransitionPointIterator(
			const CMicrostructure *microstructure,
			const Coord &c0, const Coord &c1, 
			const std::vector<ICoord> *pxls) 
{
  MS = microstructure;
  pixels = pxls;
  p0 = MS->physical2Pixel(c0);
  p1 = MS->physical2Pixel(c1);
  begin();
}

void TransitionPointIterator::begin()
{
  pixel = pixels->begin();
  cat = MS->category(*pixel);
  prevcat = cat;
  prevpixel = *pixel;
  ++pixel;
  currentTransPoint = Coord(0,0);
  delta = p1-p0;
  //cout << "infiniteSlope? " << infiniteSlope() << endl;
  if(!infiniteSlope()) {
    x0 = p0(0);
    y0 = p0(1);
    slope = delta(1)/delta(0);
    invslope = 1./slope;
#if DIM==3
    z0 = p0(2);
    slopez = delta(2)/delta(0);
    invslopez = 1./slopez;
#endif
  }
#if DIM==3
  else if (delta(1)!=0 && delta(2)!=0){
    y0 = p0(1);
    z0 = p0(2);
    slope = delta(2)/delta(1);
    invslope = 1./slope;
  }
#endif
  found = false;
  // find the first transition point, if there is one
  this->operator++();
}

void TransitionPointIterator::operator++() 
{
  localfound = false;
  prevcat = cat;
  for( ; pixel<pixels->end() && !localfound; ++pixel) {
    cat = MS->category(*pixel);
    if(cat != prevcat) {
      localfound = true;
      found = true;
      if(infiniteSlope()) {
	//cout << "B " << *pixel << cat << " " << prevcat << endl;
#if DIM == 2
	currentTransPoint = Coord(p0(0), (*pixel)(1));
#elif DIM == 3
	if (delta(1) == 0)
	  currentTransPoint = Coord(p0(0), p0(1), (*pixel)(2));
	else if (delta(2) == 0)
	  currentTransPoint = Coord(p0(0), (*pixel)(1), p0(2));
	else {
	  diff = *pixel - prevpixel;
	  if(diff(1) == -1) { // moving down, take bottom edge of last point
	    y = prevpixel(1);
	    z = z0 + (y-y0)*slope;
	  }
	  else if(diff(1) == 1) {	 // moving up, take top edge of last point
	    y = prevpixel(1) + 1.0;
	    z = z0 + (y-y0)*slope;
	  }
	  else if(diff(2) == 1) {	// moving back, take back edge of last point
	    z = prevpixel(2) + 1.0;
	    y = y0 + (z-z0)*invslope;
	  }
	  else if(diff(2) == -1) { // moving left, take left edge of last point
	    z = prevpixel(2);
	    y = y0 + (z-z0)*invslope;
	  }
	  currentTransPoint = Coord(p0(0), y, z);
	}
#endif
	//cout << "C " << currentTransPoint << endl;
      }
      else {
	// cout << "A " <<  *pixel << prevpixel << endl;
	diff = *pixel - prevpixel;
	if(diff(0) == 1) {	// moving right, take right edge of last point
	  x = prevpixel(0) + 1.0;
	  y = y0 + (x-x0)*slope;
#if DIM == 3
	  z = z0 + (x-x0)*slopez;
#endif
	}
	else if(diff(0) == -1) { // moving left, take left edge of last point
	  x = prevpixel(0);
	  y = y0 + (x-x0)*slope;
#if DIM == 3
	  z = z0 + (x-x0)*slopez;
#endif
	}
	else if(diff(1) == -1) { // moving down, take bottom edge of last point
	  y = prevpixel(1);
	  x = x0 + (y-y0)*invslope;
#if DIM == 3
	  z = z0 + (x-x0)*slopez;
#endif
	}
	else if(diff(1) == 1) {	 // moving up, take top edge of last point
	  y = prevpixel(1) + 1.0;
	  x = x0 + (y-y0)*invslope;
#if DIM == 3
	  z = z0 + (x-x0)*slopez;
#endif
	}
#if DIM == 2
	currentTransPoint = Coord(x,y);
#elif DIM == 3
	else if(diff(2) == 1) {  // moving back, take back edge of last point
	  z = prevpixel(2) + 1.0;
	  x = x0 + (z-z0)*invslopez;
	  y = y0 + (x-x0)*slope;
	}
	else {                   // moving forwards, take front edge of last point
	  z = prevpixel(2);
	  x = x0 + (z-z0)*invslopez;
	  y = y0 + (x-x0)*slope;
	}
	currentTransPoint = Coord(x,y,z);
#endif
      }
      //prevcat = cat;
    }
    prevpixel = *pixel;
  }
}


Coord TransitionPointIterator::first() {
  ICoord pix(*pixels->begin());
  if(pix(0) <= p0(0) && pix(0)+1 >= p0(0) &&
     pix(1) <= p0(1) && pix(1)+1 >= p0(1)
#if DIM==3
     && pix(2) <= p0(1) && pix(2)+1 >= p0(2)
#endif
     )
    return p0;
  else 
    return p1;
}	
      
Coord TransitionPointIterator::last() {
  ICoord pix(*pixels->begin());
  if(pix(0) <= p0(0) && pix(0)+1 >= p0(0) &&
     pix(1) <= p0(1) && pix(1)+1 >= p0(1)
#if DIM==3
     && pix(2) <= p0(1) && pix(2)+1 >= p0(2)
#endif
     )
    return p1;
  else 
    return p0;
}  


