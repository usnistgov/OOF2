// -*- C++ -*-
// $RCSfile: cskeleton.h,v $
// $Revision: 1.58 $
// $Author: langer $
// $Date: 2014/12/23 17:13:36 $

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
#if DIM==3
  static const unsigned char zmovable_;
  vtkPoints *points;
  int index_;
#elif DIM==2
  Coord position_;
  Coord lastposition_;
#endif
  TimeStamp lastmoved;
public:
  ~CSkeletonNode();
#if DIM==2
  CSkeletonNode(double x, double y);
  const Coord &position() const { return position_; }
#elif DIM==3
  double lastposition_[3];
  CSkeletonNode(double x, double y, double z, vtkPoints *p, int idx);
  // we should avoid calling this in 3D because it is slower
  // TODO 3D: it is also contributing to memory leaks!
  Coord position() const { double pos[3]; 
    points->GetPoint(index_,pos); Coord cpos(pos[0],pos[1],pos[2]); return cpos; }
  const int index() const {return index_;};
  vtkPoints *getPoints() const {return points;};
#endif
  TimeStamp nodemoved;
//   bool movable_x() const { return mobility & xmovable_; }
//   bool movable_y() const { return mobility & ymovable_; }
  bool movable_x() const {
    return (mobility & xmovable_) && (mobility & unpinned_);
  }
  bool movable_y() const {
    return (mobility & ymovable_) && (mobility & unpinned_);
  }
#if DIM==3
  bool movable_z() const {
    return (mobility & zmovable_) && (mobility & unpinned_);
  }
#endif
  bool pinned() const { return !(mobility & unpinned_); }
  bool movable() const { return movable_x() || movable_y(); }
  void setMobilityX(bool mob);
  void setMobilityY(bool mob);
#if DIM==3
  void setMobilityZ(bool mob);
#endif
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
//   Coord random_position(double, double) const;

  friend long get_globalNodeCount();
};

long get_globalNodeCount();

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class HomogeneityData {
private:
  double homogeneity;
  int dominantpixel;
  double homog_energy;
  // This is the "clone" constructor.
  HomogeneityData(double hom, int cat, double nrg) : homogeneity(hom),
						     dominantpixel(cat),
						     homog_energy(nrg) {}
public:
  HomogeneityData(double hom, int cat);
  HomogeneityData() : homogeneity(0), dominantpixel(0), homog_energy(0) {}
  double get_homogeneity() const { return homogeneity; }
  int get_dominantpixel() const { return dominantpixel; }
  double get_energy() const { return homog_energy; }
  HomogeneityData clone() { return HomogeneityData(this->homogeneity,
						   this->dominantpixel,
						   this->homog_energy); }
};

#if DIM == 3
typedef std::multimap<double, VoxelBdyIntersection> CellEdgeMap;
typedef std::vector<CellEdgeMap> CellEdge;
typedef std::pair<double, VoxelBdyIntersection> CellEdgeDatum;
typedef std::map<int, int> PointMap;
#endif

class CSkeletonElement {
private:
  static long globalElementCount;
protected:
  std::vector<CSkeletonNode*> nodes;
#if DIM == 3
  vtkCell3D *cell;
#endif
  virtual double shapefun(int, const MasterCoord&) const = 0;

  // static topological info
  static int faceEdges[4][3];
  static int faceEdgeDirs[4][3];
  static int edgeFaces[6][2];
  static int nodeFaces[4][3];
  static int nodeEdges[4][3];
  static double nodeEdgeParam[4][3];


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
#if DIM==2
  double cosCornerAngle(int) const;
  double cosCornerAngleSquared(int) const;
  double getRealAngle(int) const;
#elif DIM==3
  virtual double cosCornerAngle(int, int) const = 0;
  virtual double cosCornerAngleSquared(int, int) const = 0;
  virtual double solidCornerAngle(int) const = 0;
  virtual double cosDihedralAngle(int, int) const = 0;
#endif
  Coord frommaster(MasterCoord *mc, int rotation) const; // convert master coord
  Coord center() const;		// average position of nodes
  CRectangle bbox() const;

  // The first "interior" function is valid for all elements, and only
  // takes a single argument, but can give ambiguous results for edge
  // cases.  The second one takes an additional perturbation-hint, and
  // will only work (but is quite robust) for convex elements.
  virtual bool interior(const Coord*) const = 0; // is the given point inside?
private:
  bool interior(const Coord&, const Coord&) const; 
  HomogeneityData c_homogeneity(const CMicrostructure&) const; // see below
  mutable CachedValue<HomogeneityData> homogeneityData;	// see below
public:
  virtual double area() const = 0;
#if DIM==3
  virtual double volume() const = 0;
#endif
  virtual bool illegal() const = 0;
  virtual const std::vector<ICoord> *underlying_pixels(const CMicrostructure&)
    const = 0;
#if DIM==2
  const DoubleVec *categoryAreas(const CMicrostructure&) const;
#elif DIM==3
  // helper objects for categoryVolumes
  static vtkCutter *edgeExtractor;
  static vtkMergePoints *locator;
  static vtkCellLocator *cell_locator;
  static vtkGenericCell *generic_cell;

  //int getCategoryAtPoint(double[3], double[3], double, const CMicrostructure &) const;
  //int getCategoryAtPoint(double[3], double, const CMicrostructure &, vtkCellLocator *) const;
  //bool pointsOnElementFace(vtkPoints *points, double maxLength, double tol) const;
  virtual bool faceOnElementFace(double[3], double[3], double maxLength, double tol) const = 0;
  void updateVtkCellPoints() const;
  void addEdgeIntersection(double x[3], double t, int k, CellEdge &elementEdgeData, HullPoints &hullPoints, int *ptIds, double tol, double linetol2, double center[3], int planeidx) const;
  const DoubleVec *categoryVolumes(const CMicrostructure&) const;
  // wrappers for necessary vtkCell functions
  virtual double* getBounds()  const {
    return cell->GetBounds();};
  virtual void getBounds(double bounds[6])  const {
    cell->GetBounds(bounds);};
  virtual int getNumberOfFaces() const = 0;
  virtual int getNumberOfEdges() const = 0;
  virtual int evaluatePosition (double x[3], double *closestPoint, 
				int &subId, double pcoords[3], 
				double &dist2, double *weights) const {
    return cell->EvaluatePosition 
      (x, closestPoint, subId, pcoords, dist2, weights); };
  virtual vtkCell* getFace(int id) const {
    return cell->GetFace(id);};
  virtual vtkCell* getEdge(int id) const {
    return cell->GetEdge(id);};
  virtual int intersectWithLine (double p1[3], double p2[3], double tol, 
				 double &t, double x[3], double pcoords[3], 
				 int &subId) const {
    return cell->IntersectWithLine
      (p1,p2,tol,t,x,pcoords,subId); };
  virtual int getCellType() const = 0;
  virtual void getParametricCenter(double center[3]) const { 
    cell->GetParametricCenter(center); };
  virtual void evaluateLocation(int subId, double pcoords[3], double y[3], double *weights) const {
    cell->EvaluateLocation(subId, pcoords, y, weights); };
  virtual vtkPoints* getPoints() const {
    return cell->GetPoints(); };
  virtual vtkIdList* getPointIds() const {
    return cell->GetPointIds(); };
  virtual void getEdgePoints(int edgeId, int *& pts) const {
    cell->GetEdgePoints(edgeId, pts); };
  // These functions just return the value of a member of a static
  // array, but the size of the array will vary depending on the type.
  virtual int faceEdgeToElementEdge(int faceId, int edgeId) const = 0;
  virtual int faceEdgeToElementEdgeDir(int faceId, int edgeId) const = 0;
  void setIntersectionType(CellEdge&, int, int, double, double, int) const;
  void findOneIntersection(CellEdge&, int, int, double[3], double[3], double[3], int) const;
  bool findTwoIntersections(CellEdge&, vtkCell*, int, int, double[3], double[3], double[3], double[3], double, double) const;
#endif	// DIM==3

  // Homogeneity and dominant pixel information is cached so that it
  // isn't calculated more often than necessary.
  // findHomogeneityAndDominantPixel checks to see if it's necessary
  // to recompute the data, and calls c_homogeneity, which actually
  // computes it.  It shouldn't be necessary to call either one of
  // them explicitly, except to get things started during Skeleton
  // construction.
  void findHomogeneityAndDominantPixel(const CMicrostructure&) const;
  // homogeneity(), dominantPixel(), and energyHomogeneity() are the
  // programmer friendly API.  They recompute values only if necessary.
  double homogeneity(const CMicrostructure&) const;
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

  bool transitionPoint(CMicrostructure&, int, Coord*) const;
  virtual double energyShape() const = 0;

  friend long get_globalElementCount();
};

#if DIM==2
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

#elif DIM==3

double tetrahedraVolume(const Coord  &v0, const Coord &v1, const Coord &v2, const Coord &v3);

// class CSkeletonBrick : public CSkeletonElement {
// private:
//   static const int edgeIdMap[][4];
//   static const int dirMap[][4];
// protected:
//   virtual double shapefun(int, const MasterCoord&) const;
// public:
//   CSkeletonBrick(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, 
// 								CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
//   virtual bool illegal() const;
//   virtual bool interior(const Coord*) const;
//   virtual double volume() const;
//   virtual double area() const;
//   virtual const std::vector<ICoord> *underlying_pixels(const CMicrostructure&)
//     const;
//   virtual double energyShape() const;
//   virtual bool faceOnElementFace(double[3], double[3], double maxLength, double tol) const;
//   virtual double* getBounds()  const {
//     return (const_cast<CSkeletonBrick*>(this))->GetBounds();};
//   virtual void getBounds(double bounds[6])  const {
//     (const_cast<CSkeletonBrick*>(this))->GetBounds(bounds);};
//   virtual int getNumberOfFaces()  const {return 6;};
//   virtual int getNumberOfEdges()  const {return 12;};	
//   virtual int evaluatePosition (double x[3], double *closestPoint, 
// 				int &subId, double pcoords[3], 
// 				double &dist2, double *weights) const {
//     return (const_cast<CSkeletonBrick*>(this))->EvaluatePosition 
//       (x, closestPoint, subId, pcoords, dist2, weights); };
//   virtual vtkCell* getFace(int id) const {
//     return (const_cast<CSkeletonBrick*>(this))->GetFace(id);};
//   virtual vtkCell* getEdge(int id) const {
//     return (const_cast<CSkeletonBrick*>(this))->GetEdge(id);};
//   virtual int intersectWithLine (double p1[3], double p2[3], double tol, 
// 				 double &t, double x[3], double pcoords[3], 
// 				 int &subId) const {
//     return (const_cast<CSkeletonBrick*>(this))->IntersectWithLine
//       (p1,p2,tol,t,x,pcoords,subId); };
//   virtual int getCellType() const {return VTK_HEXAHEDRON;};
//   virtual void getParametricCenter(double center[3]) const { 
//     (const_cast<CSkeletonBrick*>(this))->GetParametricCenter(center); };
//   virtual void evaluateLocation(int subId, double pcoords[3], double y[3], double *weights) const {
//     (const_cast<CSkeletonBrick*>(this))->EvaluateLocation(subId, pcoords, y, weights); };
//   virtual vtkPoints* getPoints() const {
//     return (const_cast<CSkeletonBrick*>(this))->GetPoints(); };
//   virtual int faceEdge2GlobalEdge(int faceId, int edgeId) const {
//     return edgeIdMap[faceId][edgeId];};
//   virtual int faceEdgeDir2GlobalEdgeDir(int faceId, int edgeId) const {
//     return dirMap[faceId][edgeId];};
// };

class CSkeletonTetra : public CSkeletonElement {
protected:
  virtual double shapefun(int, const MasterCoord&) const;
public:
  CSkeletonTetra(CSkeletonNode*, CSkeletonNode*, CSkeletonNode*, CSkeletonNode*);
  static const int faceToEdgesMap[][3]; 
  static const int faceToEdgeDirMap[][3];
  static const int nodeToOppFaceMap[4];
  virtual double cosCornerAngle(int, int) const;
  virtual double cosCornerAngleSquared(int, int) const;
  virtual double solidCornerAngle(int) const;
  virtual double cosDihedralAngle(int, int) const;
  virtual bool illegal() const;
  virtual bool interior(const Coord*) const;
  virtual double volume() const;
  virtual double area() const;
  virtual const std::vector<ICoord> *underlying_pixels(const CMicrostructure&)
    const;
  virtual double energyShape() const;
  virtual bool faceOnElementFace(double[3], double[3], double maxLength, double tol) const;
  virtual int getNumberOfFaces()  const {return 4;};
  virtual int getNumberOfEdges()  const {return 6;};	
  virtual int getCellType() const {return VTK_TETRA;};
  virtual int faceEdgeToElementEdge(int faceId, int edgeId) const {
   return faceToEdgesMap[faceId][edgeId];};
  virtual int faceEdgeToElementEdgeDir(int faceId, int edgeId) const {
   return faceToEdgeDirMap[faceId][edgeId];};
};

#endif

long get_globalElementCount();

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// class CSkeleton {
// private:
//   std::vector<CSkeletonNode*> nodes;
//   std::vector<CSkeletonElement*> elements;
// public:
//   CSkeleton();
// };


#endif // CSKELETON_H

