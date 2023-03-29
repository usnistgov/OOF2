// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CMICROSTRUCTURE_H
#define CMICROSTRUCTURE_H

#include <oofconfig.h>

#include <vector>
#include <map>

#include "common/array.h"
#include "common/boolarray.h"
#include "common/coord.h"
#include "common/lock.h"
#include "common/pixelgroup.h"
#include "common/timestamp.h"
//#include "common/pixelsetboundary.h"


class ActiveArea;
class CRectangle;
class PixelAttribute;
class PixelSetBoundary;

// Some operations, such as finding the pixels under an element,
// require marking pixels in the microstructure.  Neither the
// microstructure nor the pixels can keep track of which pixels are
// marked, because there might be concurrent marking threads.  So the
// mark information is kept in a separate MarkInfo object.
class MarkInfo {
private:
  friend class CMicrostructure;
  MarkInfo(const ICoord &size);
  BoolArray markedpixels;
  BoolArray markedregion;	// active subarray of markedpixels
  void mark_site(std::vector<ICoord>&, const ICoord&);
  friend std::ostream &operator<<(std::ostream &os, const MarkInfo &mi) {
    os << mi.markedregion; 
    return os;
  }
};


class TransitionPointIterator {
private:
  const CMicrostructure *MS;
  const std::vector<ICoord> *pixels;
  std::vector<ICoord>::const_iterator pixel;
  Coord p0, p1, currentTransPoint;
  int prevcat, nextcat;
  bool infiniteSlope;
  double slope, invslope, x0, y0; 

public:
  TransitionPointIterator(const CMicrostructure*, const Coord&, const Coord&); 
  TransitionPointIterator(const CMicrostructure*, const Coord&, const Coord&,
			  const std::vector<ICoord>*); 
  ~TransitionPointIterator();
  void begin(); 
  void operator++();
  Coord current() const { return currentTransPoint; }
  bool end() const { return pixel>=pixels->end(); }
  std::size_t numPixels() const { return pixels->size(); }
  int getPrevcat() const { return prevcat; }
  int getNextcat() const { return nextcat; }
  // The first and last points of the segment.
  Coord first() const;
  Coord last() const;
  double getNormDelta() const;
};

class SegmentSection {
public:
  Coord p0, p1;			// end points in pixel units
  int category, stepcategory;
  SegmentSection(const Coord &p0, const Coord &p1, int cat, int stepcat)
    : p0(p0), p1(p1), category(cat), stepcategory(stepcat)
  {}
  double length2() const;	// length squared in pixel units
// #ifdef DEBUG
//   double span(int) const;
// #endif // DEBUG
};

class CMicrostructure {
private:
  ICoord pxlsize_;		// size of microstructure in pixels
  Coord size_;			// physical size of whole microstructure
  Coord delta_;			// physical size of a pixel
  TimeStamp timestamp;

  static long globalMicrostructureCount; // for testing

  // List of pixel groups defined on this microstructure.
  typedef std::map<const std::string, PixelGroup*> PixelGroupDict;
  PixelGroupDict pixelgroups;
  // When groups are removed from the microstructure, they're not
  // deleted right away, because it would take too long to remove them
  // from the attributeMap.  They're put in the defunctgroups list until
  // the next categorization pass.
  mutable std::vector<PixelGroup*> defunctgroups;

  // List of arrays of PixelAttributes.  PixelAttributes allow other
  // modules to assign properties to pixels.  categorize() assigns
  // different categories to pixels with different properties, and the
  // mesh generator attempts to segregate different categories into
  // separate elements.  See comments in pixelattribute.h
  mutable std::vector<Array<PixelAttribute*> > attributeMap;
  std::vector<PixelAttributeGlobalData*> attributeGlobalData;

  // categorymap caches the pixel categories assigned by categorize().
  // It's mutable because CMicrostructure::category() is
  // logically const, but it caches the categories in the categorymap.
  mutable Array<int> categorymap;
  // representativePixels is sort of the inverse of categorymap. Given
  // a category, it tells you one pixel in that category, from which
  // you can determine the actual PixelAttributes of the category.
  mutable std::vector<ICoord> representativePixels;

  // List of the boundaries of the categories.
  mutable std::vector<PixelSetBoundary*> categoryBdys;

  mutable bool categorized;
  mutable unsigned int ncategories;
  void categorize() const;

  // Lock to protect the sometimes-lengthy categorization process, and
  // functions which query the data it produces.  This lock protects
  // the categoryBdys, categorized, ncategories, categorymap, and
  // defunctgroups members, and should be invoked by any
  // CMicrostructure function that modifies them, including those that
  // might do so indirectly by potentially calling categorize().
  // Categorize itself does not acquire this lock, but all of its
  // callers must.
  mutable SLock category_lock;

  // Second lock, to protect data shared between the categorize()
  // function and other group and attribute modifying functions --
  // categorize reads these data, but others can write them.
  // Specifically, this protects the attributeMap and pixelgroups
  // data members.
  mutable SRWLock groups_attributes_lock;
  
  ActiveArea *activearea;

  std::string name_;
public:
  CMicrostructure(const std::string &name,
		  const ICoord *pxlsize, const Coord *size);
  ~CMicrostructure();
  const std::string &name() const { return name_; }
  void rename(const std::string &name) { name_ = name; }
  void destroy();
  const Coord &size() const { return size_; }
  const ICoord &sizeInPixels() const { return pxlsize_; }
  const Coord &sizeOfPixels() const { return delta_; }
  Coord physical2Pixel(const Coord&) const; // real space to pixel coords
  Coord pixel2Physical(const ICoord&) const;
  Coord pixel2Physical(const Coord&) const;
  ICoord pixelFromPoint(const Coord&) const; // pixel containing the given point
  bool contains(const ICoord&) const;
  TimeStamp &getTimeStamp();
  const TimeStamp &getTimeStamp() const;

  std::vector<ICoord> shuffledPix() const;

  void setCurrentActiveArea(ActiveArea *aa) { activearea = aa; }
  const ActiveArea *getActiveArea() const { return activearea; }

  std::size_t nGroups() const;
  PixelGroup *getGroup(const std::string &name, bool *newness);
  PixelGroup *findGroup(const std::string &name) const;
  void removeGroup(const std::string &name);
  void removeAllGroups();
  void renameGroupC(const std::string &oldname, const std::string &newname);
  std::vector<std::string> *groupNames() const;

  Array<PixelAttribute*> &getAttributeMap(std::size_t attributeID) const;
  PixelAttributeGlobalData *getAttributeGlobalData(std::size_t attributeID)
    const;
  const Array<int> *getCategoryMap() const; // changes mutable private data
  const Array<int> *getCategoryMapRO() const; // changes no data

  unsigned int nCategories() const;
  // Three, no four, no five different versions of this for
  // convenience in calling it...
  int category(const ICoord *where) const;
  int category(const ICoord &where) const;
  int category(int x, int y) const;
  int category(const Coord &where) const; // Arbitrary physical-coord point.
  int category(double x, double y) const { return category(Coord(x,y)); }
  void recategorize();
  const ICoord &getRepresentativePixel(std::size_t category) const;
  bool is_categorized() const { return categorized; }

  const std::vector<PixelSetBoundary*> &getCategoryBdys() const {
    return categoryBdys;
  }

  std::vector<ICoord> *segmentPixels(const Coord&, const Coord&, bool&, bool&)
    const;
  std::vector<SegmentSection*> *getSegmentSections(const Coord*, const Coord*,
						   double) const;
  
  MarkInfo *beginMarking(const CRectangle&) const; // sets active subarray of markedpixels
  void markSegment(MarkInfo*, const Coord&, const Coord&) const;
  void markTriangle(MarkInfo*, const Coord&, const Coord&, const Coord&)
    const;
  std::vector<ICoord> *markedPixels(MarkInfo*) const;
  void endMarking(MarkInfo*) const;

  bool transitionPointWithPoints(const Coord*, const Coord*, Coord*) const;
  bool transitionPointClosest(const Coord&, const Coord&, TransitionPointIterator&,
			      Coord *result) const;
  bool transitionPoint(const Coord&, const Coord&, Coord *result) const;
  double edgeHomogeneity(const Coord&, const Coord&) const;

  double edgeHomogeneityCat(const Coord&, const Coord&, int* cat) const;
  bool transitionPointWithPoints_unbiased(const Coord*, const Coord*, Coord*) const;

  friend long get_globalMicrostructureCount();
};

long get_globalMicrostructureCount();




#endif // CMICROSTRUCTURE_H
