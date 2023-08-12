// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CSKELETON_SWG
#define CSKELETON_SWG

%module(package="ooflib.SWIG.engine") cskeleton

%include "common/typemaps.swg"
%import "common/cmicrostructure.swg"
%import "common/coord.swg"
%import "common/timestamp.swg"
%import "engine/mastercoord.swg"

%{
#include "engine/cskeleton.h"
#include "engine/mastercoord.h"
%}

class CSkeletonNode {
public:
  CSkeletonNode(double, double);
  ~CSkeletonNode();
  Coord position();
  bool movable_x();
  bool movable_y();
  bool movable();
  bool pinned();
  void setMobilityX(bool);
  void setMobilityY(bool);
  void setPinned(bool);
  void copyMobility(CSkeletonNode*);
  bool canMergeWith(CSkeletonNode*);
  bool moveTo(Coord *Point);
  bool canMoveTo(Coord *Point);
  void unconstrainedMoveTo(Coord *Point);
  bool moveBy(Coord *Point);
  void moveBack();
  TimeStamp nodemoved;
};

class HomogeneityData {
public:
  ~HomogeneityData();
};

%nodefaultctor CSkeletonElement;

class CSkeletonElement {
public:
  ~CSkeletonElement();
  int nnodes();
  void replaceNode(int, CSkeletonNode*);
  %newobject perimeter;
  std::vector<Coord> *perimeter();
  double perimeterLength();
  double edgeLength(int);
  double cosCornerAngle(int);
  double getRealAngle(int);
  Coord frommaster(MasterCoord *Point, int);
  Coord center();
  double area();
  Coord size();
  bool illegal();
  bool interior(Coord *Point);
  %newobject underlying_pixels;
  std::vector<ICoord> *underlying_pixels(CMicrostructure&);
  double homogeneity(CMicrostructure&, bool);
  int dominantPixel(CMicrostructure&);
  void copyHomogeneity(CSkeletonElement&);
  double energyHomogeneity(CMicrostructure&);
  void findHomogeneityAndDominantPixel(CMicrostructure&, bool);
  void revertHomogeneity();
  HomogeneityData getHomogeneityData();
  void setHomogeneityData(HomogeneityData&);
  void setHomogeneous(int);
};

class CSkeletonTriangle : public CSkeletonElement {
public:
  CSkeletonTriangle(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  double energyShape();
};

class CSkeletonQuad : public CSkeletonElement {
public:
  CSkeletonQuad(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  ~CSkeletonQuad();
  double energyShape();
};

long get_globalNodeCount();
long get_globalElementCount();

#endif // CSKELETON_SWG
