// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef CSKELETON_H
#define CSKELETON_H

class CSkeleton;
class CSkeletonElement;
class CSkeletonNode;

#include "common/boolarray.h"
#include "common/coord.h"
#include "common/timestamp.h"
#include "common/pixelsetboundary.h"
#include "common/cachedvalue.h"
#include <vector>
#include <iostream>

class CMicrostructure;
class DoubleVec;
class MasterCoord;
class TwoMatrix;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class CSkeletonNode {
private:
  static long globalNodeCount;
  unsigned char mobility;
  static const unsigned char unpinned_;
  static const unsigned char xmovable_;
  static const unsigned char ymovable_;
  Coord position_;
  Coord lastposition_;
  TimeStamp lastmoved;
public:
  ~CSkeletonNode();
  CSkeletonNode(double x, double y);
  const Coord &position() const { return position_; }
  TimeStamp nodemoved;
  bool movable_x() const {
    return (mobility & xmovable_) && (mobility & unpinned_);
  }
  bool movable_y() const {
    return (mobility & ymovable_) && (mobility & unpinned_);
  }
  bool pinned() const { return !(mobility & unpinned_); }
  bool movable() const { return movable_x() || movable_y(); }
  void setMobilityX(bool mob);
  void setMobilityY(bool mob);
  void setPinned(bool pin);
  void copyMobility(const CSkeletonNode *other) {
    mobility = other->mobility;
  }
  bool canMergeWith(const CSkeletonNode*) const;
  bool moveTo(const Coord *pos); // takes pointer so that SWIG typemap can work
  bool canMoveTo(const Coord *pos) const;
  void unconstrainedMoveTo(const Coord *pos);
  bool moveBy(const Coord *shift);
  void moveBack();

  friend long get_globalNodeCount();
};

long get_globalNodeCount();

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

#define UNKNOWN_CATEGORY -1

class HomogeneityData {
private:
  double homogeneity;
  int dominantpixel;
  double homog_energy;
  // This is the "clone" constructor.
  HomogeneityData(double hom, int cat, double nrg)
    : homogeneity(hom), dominantpixel(cat), homog_energy(nrg)
  {}
public:
  HomogeneityData(double hom, int cat);
  HomogeneityData()
    : homogeneity(0), dominantpixel(UNKNOWN_CATEGORY), homog_energy(0)
  {}
  double get_homogeneity() const { return homogeneity; }
  int get_dominantpixel() const { return dominantpixel; }
  double get_energy() const { return homog_energy; }
  HomogeneityData clone() { return HomogeneityData(this->homogeneity,
						   this->dominantpixel,
						   this->homog_energy); }
};


class CSkeletonElement {
private:
  static long globalElementCount;
protected:
  std::vector<CSkeletonNode*> nodes;
  virtual double shapefun(int, const MasterCoord&) const = 0;

public:
  CSkeletonElement(int n);
  virtual ~CSkeletonElement();
  int nnodes() const { return nodes.size(); }
  void replaceNode(int which, CSkeletonNode *replacement);
  std::vector<Coord> *perimeter() const; // list of node positions
  double perimeterLength() const;
  double perimeterSquared() const;
  double edgeLength(int) const;
  double edgeLengthSquared(int) const;

  double cosCornerAngle(int) const;
  double cosCornerAngleSquared(int) const;
  double getRealAngle(int) const;
  Coord frommaster(MasterCoord *mc, int rotation) const; // convert master coord
  Coord center() const;		// average position of nodes
  CRectangle bbox() const;
  Coord size() const;
  virtual bool interior(const Coord*) const = 0; // is the given point inside?
private:
  HomogeneityData c_homogeneity(const CMicrostructure&, bool) const; //see below
  mutable CachedValue<HomogeneityData> homogeneityData;	// see below
public:
  virtual double area() const = 0;
  virtual bool illegal() const = 0;
  virtual const std::vector<ICoord> *underlying_pixels(const CMicrostructure&)
    const = 0;
  DoubleVec categoryAreas(const CMicrostructure&, bool) const;

  // Homogeneity and dominant pixel information is cached so that it
  // isn't calculated more often than necessary.
  // findHomogeneityAndDominantPixel checks to see if it's necessary
  // to recompute the data, and calls c_homogeneity, which actually
  // computes it.  It shouldn't be necessary to call either one of
  // them explicitly, except to get things started during Skeleton
  // construction.
  void findHomogeneityAndDominantPixel(const CMicrostructure&, bool) const;
  // homogeneity(), dominantPixel(), and energyHomogeneity() are the
  // programmer friendly API.  They recompute values only if necessary.
  double homogeneity(const CMicrostructure&, bool) const;
  int dominantPixel(const CMicrostructure&) const;
  double energyHomogeneity(const CMicrostructure&) const;
  // revertHomogeneity returns the cached values to their previous
  // state, saved at the last call to homogeneityData.set_value().
  void revertHomogeneity();
  void copyHomogeneity(const CSkeletonElement&);
  // getHomogeneityData and setHomogeneityData are used by provisional
  // elements to avoid having to recompute values when a provisional
  // skeleton modification is accepted.
  HomogeneityData getHomogeneityData() const;
  void setHomogeneityData(const HomogeneityData&);
  // setHomogeneous() is called during skeleton construction when it's
  // known a priori that an element is homogeneous.  The argument is
  // the dominant pixel category.
  void setHomogeneous(int);

  virtual double energyShape() const = 0;

  friend long get_globalElementCount();

  friend std::ostream &operator<<(std::ostream&, const CSkeletonElement&);
};

class CSkeletonTriangle : public CSkeletonElement {
protected:
  virtual double shapefun(int, const MasterCoord&) const;
public:
  CSkeletonTriangle(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  virtual bool illegal() const;
  virtual bool interior(const Coord*) const;
  virtual double area() const;
  virtual const std::vector<ICoord> *underlying_pixels(const CMicrostructure&)
    const;
  virtual double energyShape() const;
};

class CSkeletonQuad : public CSkeletonElement {
protected:
  virtual double shapefun(int, const MasterCoord&) const;
public:
  CSkeletonQuad(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  virtual bool illegal() const;
  virtual bool interior(const Coord*) const;
  virtual double area() const;
  virtual const std::vector<ICoord> *underlying_pixels(const CMicrostructure&)
    const;
  virtual double energyShape() const;
};

std::ostream &operator<<(std::ostream&, const CSkeletonElement&);

long get_globalElementCount();

#endif // CSKELETON_H

