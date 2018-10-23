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

#include "common/cmicrostructure.h"
#include "common/doublevec.h"
#include "common/geometry.h"
#include "common/lock.h"
#include "common/pixelsetboundary.h"
#include "common/random.h"
#include "engine/cskeleton.h"
#include "engine/mastercoord.h"
#include "engine/ooferror.h"
#include <algorithm>
#include <iostream>
#include <math.h>

#ifdef DEBUG
#include <assert.h>
#endif

#include <time.h>

#define LEGAL_ELEMENT_AREA_TOLERANCE 1.0e-8
#define COS_SQUARED_TOLERANCE 1.0e-13

const unsigned char CSkeletonNode::xmovable_ = 1;
const unsigned char CSkeletonNode::ymovable_ = 2;
const unsigned char CSkeletonNode::unpinned_ = 4;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

long CSkeletonNode::globalNodeCount = 0; // used for code testing
static SLock globalNodeCountLock;

CSkeletonNode::CSkeletonNode(double x, double y)
  : mobility(xmovable_|ymovable_|unpinned_),
    position_(x, y)
{
  globalNodeCountLock.acquire();
  ++globalNodeCount;
  globalNodeCountLock.release();
}

CSkeletonNode::~CSkeletonNode() {
  globalNodeCountLock.acquire();
  --globalNodeCount;
  globalNodeCountLock.release();
}

void CSkeletonNode::setMobilityX(bool mob) {
  if(mob)
    mobility |= xmovable_;
  else
    mobility &= ~xmovable_;
}

void CSkeletonNode::setMobilityY(bool mob) {
  if(mob)
    mobility |= ymovable_;
  else
    mobility &= ~ymovable_;
}

void CSkeletonNode::setPinned(bool pin) {
  if(pin)
    mobility &= ~unpinned_;
  else
    mobility |= unpinned_;
}

// moveTo and moveBy should not be called directly, except by a
// Skeleton or DeputySkeleton object.  Everyone else should use
// Skeleton.moveNodeTo, etc.

bool CSkeletonNode::moveTo(const Coord *pos) {
  lastmoved = nodemoved;
  lastposition_ = position_;
  position_ = *pos;
  if(!movable_x()) 
    position_.x = lastposition_.x;
  if(!movable_y())
    position_.y = lastposition_.y;
  if(position_ != lastposition_) {
    ++nodemoved;
    return true;
  }
  return false;
};


bool CSkeletonNode::canMoveTo(const Coord *pos) const {
  return ((movable_x() || position_.x == pos->x) &&
	  (movable_y() || position_.y == pos->y));
}


void CSkeletonNode::unconstrainedMoveTo(const Coord *pos) {
  lastmoved = nodemoved;
  lastposition_ = position_;
  position_ = *pos;
  ++nodemoved;
}

bool CSkeletonNode::moveBy(const Coord *shift) {
  lastmoved = nodemoved;
  lastposition_ = position_;
  Coord target = position_ + *shift;
  position_ = target;
  if(!movable_x())
    position_.x = lastposition_.x;
  if(!movable_y())
    position_.y = lastposition_.y;
  if(position_ != lastposition_) {
    ++nodemoved;
    return true;
  }
  return false;
}

void CSkeletonNode::moveBack() {
  nodemoved = lastmoved;
  position_ = lastposition_;
}

// Can this node be moved to and merge with another node?
bool CSkeletonNode::canMergeWith(const CSkeletonNode *other) const {
  bool xmovable = movable_x();
  bool ymovable = movable_y();
  if(!xmovable && !ymovable)
    return false;
  else if(!xmovable && ymovable)
    return position_.x == other->position_.x;
  else if(xmovable && !ymovable)
    return position_.y == other->position_.y;
  return true;
}

long get_globalNodeCount() {
  return CSkeletonNode::globalNodeCount;
}

// Coord CSkeletonNode::random_position(double vx, double vy) const
// {
//   return position_ + Coord(gasdev()*vx, gasdev()*vy);
// }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Is pnt inside the triangle (n0, n1, n2)?

static bool insideTriangle(const Coord &n0, const Coord &n1,
			   const Coord &n2, const Coord &pnt)
{
  Coord r0(n0 - pnt);
  Coord r1(n1 - pnt);
  Coord r2(n2 - pnt);
  return r0%r1 >= 0.0 && r1%r2 >= 0.0 && r2%r0 >= 0.0; // cross products
}

static double triangleArea(const Coord &v0, const Coord &v1, const Coord &v2) {
  return 0.5*(v1 - v0)%(v2 - v0);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

long CSkeletonElement::globalElementCount = 0;
static SLock globalElementCountLock;

long get_globalElementCount() {
  return CSkeletonElement::globalElementCount;
}

CSkeletonElement::~CSkeletonElement() {
  globalElementCountLock.acquire();
  --globalElementCount;
  globalElementCountLock.release();
}


CSkeletonElement::CSkeletonElement(int n)
  :nodes(n)
{
  globalElementCountLock.acquire();
  ++globalElementCount;
  globalElementCountLock.release();
}

void CSkeletonElement::replaceNode(int which, CSkeletonNode *replacement) {
  nodes[which] = replacement;
}

std::vector<Coord> *CSkeletonElement::perimeter() const {
  int n = nnodes();
  std::vector<Coord> *pvec = new std::vector<Coord>(n);
  for(int i=0; i<n; i++)
    (*pvec)[i] = nodes[i]->position();
  return pvec;
}

double CSkeletonElement::perimeterLength() const {
  int n = nnodes();
  double p = 0.0;
  for(int i=0; i<n; i++) {
    int j = (i+1)%n;
    Coord r(nodes[i]->position() - nodes[j]->position());
    p += sqrt(norm2(r));
  }
  return p;
}

double CSkeletonElement::perimeterSquared() const {
  // Note: this isn't actually the perimeter squared, it's the sum of
  // the squares of the lengths of the sides.
  int n = nnodes();
  double p = 0.0;
  for(int i=0; i<n; i++) {
    int j = (i+1)%n;
    Coord r(nodes[i]->position() - nodes[j]->position());
    p += norm2(r);
  }
  return p;
}

double CSkeletonElement::edgeLength(int which) const {
  Coord r(nodes[which]->position() - nodes[(which+1)%nnodes()]->position());
  return sqrt(norm2(r));
}

double CSkeletonElement::edgeLengthSquared(int which) const {
  Coord r(nodes[which]->position() - nodes[(which+1)%nnodes()]->position());
  return norm2(r);
}

double CSkeletonElement::cosCornerAngleSquared(int which) const {
  int n = nnodes();
  Coord p0 = nodes[which]->position();
  Coord side0 = nodes[(which+n-1)%n]->position() - p0;
  Coord side1 = nodes[(which+1)%n]->position() - p0;
  double sdots = dot(side0, side1);
  double cos2 = sdots*sdots/(norm2(side0)*norm2(side1));
  if(cos2 > 1.0)
    return 1.0;
  return cos2;
}

double CSkeletonElement::cosCornerAngle(int which) const {
  int n = nnodes();
  Coord p0 = nodes[which]->position();
  Coord side0 = nodes[(which+n-1)%n]->position() - p0;
  Coord side1 = nodes[(which+1)%n]->position() - p0;
  double cosAngle = dot(side0, side1)/sqrt(norm2(side0)*norm2(side1));
  // Due to a round-off error, this step is needed.
  // (Sometimes cosAngle that should be -1 turns out to be -1.000000001)
  if (cosAngle > 1.0)
    return 1.0;
  else if (cosAngle < -1.0)
    return -1.0;
  else
    return cosAngle;
}

double CSkeletonElement::getRealAngle(int which) const {
  int n = nnodes();
  Coord p0 = nodes[which]->position();
  Coord side0 = nodes[(which+n-1)%n]->position() - p0;
  Coord side1 = nodes[(which+1)%n]->position() - p0;
  return atan2(side1%side0, dot(side1,side0))*180./M_PI;
}

Coord CSkeletonElement::center() const {
  int n = nnodes();
  Coord c = nodes[0]->position();
  for(int i=1; i<n; i++)
    c += nodes[i]->position();
  return (1./n)*c;
}

Coord CSkeletonElement::frommaster(MasterCoord *mc, int rotation) const {
  int n = nnodes();
  Coord result(0., 0.);
  for(int i=0; i<n; i++)
    result += shapefun(i, *mc) * nodes[(i+rotation)%n]->position();
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CRectangle CSkeletonElement::bbox() const {
  CRectangle bounds(nodes[0]->position(), nodes[1]->position());
  for(int i=2; i<nnodes(); i++)
    bounds.swallow(nodes[i]->position());
  return bounds;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Returns a vector of doubles.  Each double in this vector is equal
// to the area (in pixel units) of the corresponding microstructure
// category which is within this element.

DoubleVec CSkeletonElement::categoryAreas(const CMicrostructure &ms) const
{
  // nCategories recomputes categories and boundaries if needed.
  unsigned int ncat = ms.nCategories();
  DoubleVec result(ncat);
  int nn = nodes.size();

  // Get positions of nodes in pixel coordinates.
  Coord element_points[nn];
  for(unsigned int i=0; i<nn; i++)
    element_points[i] = ms.physical2Pixel(nodes[i]->position());
  // Create list of lines that will be used to clip the pixel set boundaries.
  LineList edges(nn);
  std::vector<Coord> npos(nn);	// node positions in pixel coordinates
  for(unsigned int i=0; i<nn; i++)
    npos[i] = ms.physical2Pixel(nodes[i]->position());
  for(unsigned int i=0; i<nn; i++) {
    edges[i] = Line(npos[i], npos[(i+1)%nn]);
  }
  // Get all the pixel set boundaries.
  const std::vector<PixelSetBoundary*> &bdys = ms.getCategoryBdys();
  
  for(int cat=0; cat<ncat; cat++) {
#ifdef DEBUG
    std::cerr << "CSkeletonElement::categoryAreas: category=" << cat << "------"
	      << std::endl;
    std::cerr << "CSkeletonElement::categoryAreas: element=";
    for(const CSkeletonNode *node : nodes)
      std::cerr << " " << node->position();
    std::cerr << std::endl;
#endif // DEBUG
    result[cat] += bdys[cat]->clippedArea(edges);
  }
// #ifdef DEBUG
//   std::cerr << "CSkeletonElement::categoryAreas: result=";
//   for(int cat=0; cat<ncat; cat++) std::cerr << " " << result[cat];
//   std::cerr << std::endl;
// #endif // DEBUG
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double CSkeletonElement::homogeneity(const CMicrostructure &ms) const {
  findHomogeneityAndDominantPixel(ms);
  return homogeneityData.value().get_homogeneity();
}

int CSkeletonElement::dominantPixel(const CMicrostructure &ms) const {
  findHomogeneityAndDominantPixel(ms);
  return homogeneityData.value().get_dominantpixel();
};

double CSkeletonElement::energyHomogeneity(const CMicrostructure &ms) const {
  findHomogeneityAndDominantPixel(ms);
  return homogeneityData.value().get_energy();
};

void CSkeletonElement::copyHomogeneity(const CSkeletonElement &other) {
  homogeneityData.copy(other.homogeneityData);
}

void CSkeletonElement::revertHomogeneity() {
  homogeneityData.revert();
}

HomogeneityData CSkeletonElement::getHomogeneityData() const {
  return homogeneityData.value();
}

void CSkeletonElement::setHomogeneityData(const HomogeneityData &hd) {
  homogeneityData.set_value(hd);
}

void CSkeletonElement::setHomogeneous(int dompxl) {
  HomogeneityData hd(1.0, dompxl);
  homogeneityData.set_value(hd);
}

void CSkeletonElement::findHomogeneityAndDominantPixel(
						       const CMicrostructure &ms)
  const
{
  // Only recompute if the microstructure has changed or nodes have moved
  if(homogeneityData.timestamp() > ms.getTimeStamp()) {
    bool uptodate = true;
    for(int i=0; i<nnodes() && uptodate; i++) {
      if(homogeneityData.timestamp() < nodes[i]->nodemoved) 
	uptodate = false;
    }
    if(uptodate)
      return;
  }
  homogeneityData.set_value(c_homogeneity(ms)); // recompute
}

// Find the homogeneity of the current element.  Element is assumed to
// be legal -- categoryAreas will throw an exception if it isn't.
HomogeneityData CSkeletonElement::c_homogeneity(const CMicrostructure &ms)
  const
{
  if(illegal())
    return HomogeneityData(0, UNKNOWN_CATEGORY);
  const DoubleVec areas(categoryAreas(ms));
  // if(!areas) {
  //   // Element is not illegal, but has parts outside of the
  //   // Microstructure because some *other* element is illegal. 
  //   return HomogeneityData(0, UNKNOWN_CATEGORY);
  // }
  int category = 0;
  double maxarea=0.0;

// #ifdef DEBUG
//   std::cerr << "CSkeletonElement::c_homogeneity: areas=";
//   for(double a : *areas) std::cerr << " " << a;
//   std::cerr << std::endl;
// #endif // DEBUG
  
  for(DoubleVec::size_type i=0; i<areas.size(); ++i) {
    double area = areas[i];
    if(area > maxarea) {
      maxarea = area;
      category = i;
    }
  }

// #ifdef DEBUG
//   std::cerr << "CSkeletonElement::c_homogeneity: maxarea=" << maxarea
// 	    << " total=" << area()
// 	    << std::endl;
// #endif // DEBUG
  double homogeneity = maxarea/area();
  if (homogeneity>1.0) homogeneity=1.0;
  return HomogeneityData(homogeneity, category);
}

// Find the point along edge i where the pixel category in the
// Microstructure changes.  Return true iff there's just one such
// point.
bool CSkeletonElement::transitionPoint(CMicrostructure &microstructure, int i,
				       Coord *point)
  const
{
  return microstructure.transitionPoint(nodes[i]->position(),
					nodes[(i+1)%nnodes()]->position(),
					point);
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CSkeletonQuad::CSkeletonQuad(CSkeletonNode *n0, CSkeletonNode *n1,
			     CSkeletonNode *n2, CSkeletonNode *n3)
  : CSkeletonElement(4)
{
  nodes[0] = n0;
  nodes[1] = n1;
  nodes[2] = n2;
  nodes[3] = n3;
}

double CSkeletonQuad::shapefun(int i, const MasterCoord &mc) const {
  switch(i) {
  case 0:
    return  0.25*(mc(0) - 1.0)*(mc(1) - 1.0);
  case 1:
    return -0.25*(mc(0) + 1.0)*(mc(1) - 1.0);
  case 2:
    return  0.25*(mc(0) + 1.0)*(mc(1) + 1.0);
  case 3:
    return -0.25*(mc(0) - 1.0)*(mc(1) + 1.0);
  }
  throw ErrBadIndex(i, __FILE__, __LINE__);
}

bool CSkeletonQuad::interior(const Coord *point) const {
  //  3________2
  //   |     /|
  //   | L  / |     If a point is inside of either triangle,    
  //   |   /  |     then it is inside the quad.
  //   |  /   |
  //   | / R  |
  //   |/     |
  //   --------
  //   0      1
  Coord p0 = nodes[0]->position();
  Coord p1 = nodes[1]->position();
  Coord p2 = nodes[2]->position();
  Coord p3 = nodes[3]->position();
  double areaL = triangleArea(p0, p2, p3);
  double areaR = triangleArea(p0, p1, p2);
  if(areaR > 0.0 && areaL > 0.0)
    return insideTriangle(p0,p2,p3, *point) || insideTriangle(p0,p1,p2, *point);
  if(areaR < 0.0 && areaL > 0.0)
    // Boomerang shape.  Vertex 1 may lie inside L.  point must lie
    // within L, but not within the inverted R.
    return insideTriangle(p0,p2,p3, *point) && !insideTriangle(p0,p2,p1,*point);
  if(areaR > 0.0 && areaL < 0.0)
    return insideTriangle(p0,p1,p2, *point) && !insideTriangle(p0,p3,p2,*point);
  return false;
}

double CSkeletonQuad::area() const {
  return
    triangleArea(nodes[0]->position(), nodes[2]->position(),
		 nodes[3]->position()) +
    triangleArea(nodes[0]->position(), nodes[1]->position(),
		 nodes[2]->position());
}

bool CSkeletonQuad::illegal() const {
  Coord p0 = nodes[0]->position();
  Coord p1 = nodes[1]->position();
  Coord p2 = nodes[2]->position();
  Coord p3 = nodes[3]->position();

  //   // Using Area() in a thorough way.
  //   double a1 = (p1-p0)%(p3-p0);
  //   double a2 = (p2-p1)%(p0-p1);
  //   double a3 = (p3-p2)%(p1-p2);
  //   double a4 = (p0-p3)%(p2-p3);
  //   if ( (a1<=0) || (a2<=0) || (a3<=0) || (a4<=0) )
  //     return true;
  //   if ( (fabs((a1+a3)/(a2+a4))-1.0) > LEGAL_ELEMENT_AREA_TOLERANCE )
  //     return true;
  //   return false;

  //   // Using Area() only.
  //   return ((p1 - p0) % (p3 - p0) <= 0.0 ||
  // 	  (p2 - p1) % (p0 - p1) <= 0.0 ||
  // 	  (p3 - p2) % (p1 - p2) <= 0.0 ||
  // 	  (p0 - p3) % (p2 - p3) <= 0.0);

  // Using Area() & Cosine().
  return  ( (p1 - p0) % (p3 - p0) <= 0.0 ||
	    (p2 - p1) % (p0 - p1) <= 0.0 ||
	    (p3 - p2) % (p1 - p2) <= 0.0 ||
	    (p0 - p3) % (p2 - p3) <= 0.0 ) ||
    ( cosCornerAngleSquared(0) == 1 ||
      cosCornerAngleSquared(1) == 1 ||
      cosCornerAngleSquared(2) == 1 ||
      cosCornerAngleSquared(3) == 1 );
}

const std::vector<ICoord> *
CSkeletonQuad::underlying_pixels(const CMicrostructure &microstructure) const {
  // Divide the quad into two triangles with positive area, and mark
  // the pixels under them.  This avoids the possibly complicated
  // geometry of quadrilaterals.
  const Coord c0 = nodes[0]->position();
  const Coord c1 = nodes[1]->position();
  const Coord c2 = nodes[2]->position();
  const Coord c3 = nodes[3]->position();
  CRectangle bbox(c0, c2);
  bbox.swallow(c1);
  bbox.swallow(c3);
  MarkInfo *mm = microstructure.beginMarking(bbox);
  if(triangleArea(c0, c1, c2) >= 0.0 &&
     triangleArea(c0, c2, c3) >= 0.0) {
    microstructure.markTriangle(mm, c0, c1, c2);
    microstructure.markTriangle(mm, c0, c2, c3);
  }
  else if(triangleArea(c1, c2, c3) >= 0.0 &&
          triangleArea(c2, c3, c0) >= 0.0) {
    microstructure.markTriangle(mm, c1, c2, c3);
    microstructure.markTriangle(mm, c1, c3, c0);
  }
  std::vector<ICoord> *pxls = microstructure.markedPixels(mm); // new'd vector
  microstructure.endMarking(mm);
  return pxls;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CSkeletonTriangle::CSkeletonTriangle(CSkeletonNode *n0, CSkeletonNode *n1,
				     CSkeletonNode *n2)
  : CSkeletonElement(3)
{
  nodes[0] = n0;
  nodes[1] = n1;
  nodes[2] = n2;
}

double CSkeletonTriangle::shapefun(int i, const MasterCoord &mc) const {
  switch(i) {
  case 0:
    return mc(0);
  case 1:
    return mc(1);
  case 2:
    return 1. - mc(0) - mc(1);
  }
  throw ErrBadIndex(i, __FILE__, __LINE__);
}

bool CSkeletonTriangle::interior(const Coord *point) const {
  return insideTriangle(nodes[0]->position(), nodes[1]->position(),
			nodes[2]->position(), *point);
};

double CSkeletonTriangle::area() const {
  return triangleArea(nodes[0]->position(), nodes[1]->position(),
		      nodes[2]->position());
}

bool CSkeletonTriangle::illegal() const {
  //   // Using Area() basically, but more thoroughly.
  //   const Coord &p1 = nodes[0]->position();
  //   const Coord &p2 = nodes[1]->position();
  //   const Coord &p3 = nodes[2]->position();

  //   double a1 = triangleArea(p1,p2,p3);
  //   if (a1<=0.0)
  //     return true;
  //   double a2 = triangleArea(p2,p3,p1);
  //   if (a2<=0.0)
  //     return true;
  //   double a3 = triangleArea(p3,p1,p2);
  //   if (a3<=0.0)
  //     return true;
    
  //   if (fabs((a1/a2)-1.0) > LEGAL_ELEMENT_AREA_TOLERANCE ||
  //       fabs((a2/a3)-1.0) > LEGAL_ELEMENT_AREA_TOLERANCE ||
  //       fabs((a3/a1)-1.0) > LEGAL_ELEMENT_AREA_TOLERANCE )
  //     return true;

  //   return false;

  // Using Area() & Cosine() only.
  return (area() <= 0.0 ||
	  cosCornerAngleSquared(0) == 1 ||
	  cosCornerAngleSquared(1) == 1 ||
	  cosCornerAngleSquared(2) == 1);
}

const std::vector<ICoord> *
CSkeletonTriangle::underlying_pixels(const CMicrostructure &microstructure)
  const
{
  Coord p0 = nodes[0]->position();
  Coord p1 = nodes[1]->position();
  Coord p2 = nodes[2]->position();
  CRectangle bbox(p0, p1);
  bbox.swallow(p2);
  MarkInfo *mm = microstructure.beginMarking(bbox);
  microstructure.markTriangle(mm, p0, p1, p2);
  std::vector<ICoord> *pxls = microstructure.markedPixels(mm); // new'd vector
  microstructure.endMarking(mm);
  return pxls;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// OLD VERSION USING MAP JACOBIAN

// Shape energy calculation.  The shape energy is (c-1)/c, where c 
// is the ratio of the condition number squared of the jacobian of 
// the ideal->physical space map, to the condition number squared of
// the jacobian of the identity map.  For quads, the maximum condition
// number over all corners of the element is used.
//   The energy is 0 for squares and equilateral triangles, and 1
// for degenerate shapes (ones with 180-degree vertices).

// double CSkeletonTriangle::energyShape() const {
//   Coord a_vec = nodes[1]->position()-nodes[0]->position();
//   Coord b_vec = nodes[2]->position()-nodes[0]->position();

//   double num = norm2(a_vec) + norm2(b_vec) - dot(a_vec, b_vec);
//   double den = cross(a_vec, b_vec);
//   double condtn = num*num/(3.0*den*den);
//   return (condtn-1.0)/condtn;
// }

// double CSkeletonQuad::energyShape() const {
//   double eshape=0.0;
//   for(int i=0;i<4;i++) {
//     Coord a_vec = nodes[(i+1)%4]->position() - nodes[i]->position();
//     Coord b_vec = nodes[(i+3)%4]->position() - nodes[i]->position();
//     double num = norm2(a_vec)+norm2(b_vec);
//     double den = cross(a_vec, b_vec);
//     double condtn = 0.25*num*num/(den*den);
//     double corner_eshape = (condtn-1.0)/condtn;
//     if (corner_eshape > eshape)
//       eshape = corner_eshape;
//   }
//   return pow(eshape, 1.5);
// }

// // Testing new shape energy functions using STANDARD DEVIATION
// double CSkeletonTriangle::energyShape() const {
//   const double pi = acos(-1.0);
//   const double a0 = acos(cosCornerAngle(0))*180.0/pi;
//   const double a1 = acos(cosCornerAngle(1))*180.0/pi;
//   const double a2 = 180.0 - (a0+a1);
//   const double meanA = 60.0;
//   const double normA = 1.4142135623731;
//   const double angleE = sqrt(((meanA-a0)*(meanA-a0)+
// 			      (meanA-a1)*(meanA-a1)+
// 			      (meanA-a2)*(meanA-a2))/3.0)/meanA/normA;

//   const double l0 = edgeLength(0);
//   const double l1 = edgeLength(1);
//   const double l2 = edgeLength(2);
//   const double meanL = (l0+l1+l2)/3.0;
//   const double normL = 0.7071067811866;
//   const double aspectE = sqrt(((meanL-l0)*(meanL-l0)+
// 			       (meanL-l1)*(meanL-l1)+
// 			       (meanL-l2)*(meanL-l2))/3.0)/meanL/normL;

//   if (angleE >= aspectE)
//     return angleE;
//   else
//     return aspectE;
// //   const double beta = 0.5;
// //   return beta*angleE + (1.0-beta)*aspectE;
// }

// double CSkeletonQuad::energyShape() const {
//   const double pi = acos(-1.0);
//   const double a0 = acos(cosCornerAngle(0))*180.0/pi;
//   const double a1 = acos(cosCornerAngle(1))*180.0/pi;
//   const double a2 = acos(cosCornerAngle(2))*180.0/pi;
//   const double a3 = 360.0 - (a0+a1+a2);
//   const double meanA = 90.0;
//   const double angleE = sqrt(((meanA-a0)*(meanA-a0)+
// 			      (meanA-a1)*(meanA-a1)+
// 			      (meanA-a2)*(meanA-a2)+
// 			      (meanA-a3)*(meanA-a3))/4.0)/meanA;

//   const double l0 = edgeLength(0);
//   const double l1 = edgeLength(1);
//   const double l2 = edgeLength(2);
//   const double l3 = edgeLength(3);
//   const double meanL = (l0+l1+l2+l3)/4.0;
//   const double aspectE = sqrt(((meanL-l0)*(meanL-l0)+
// 			      (meanL-l1)*(meanL-l1)+
// 			      (meanL-l2)*(meanL-l2)+
// 			      (meanL-l3)*(meanL-l3))/4.0)/meanL;

//   if (angleE >= aspectE)
//     return angleE;
//   else
//     return aspectE;
// }

// END OF OLD VERSION USING MAP JACOBIAN



// SHAPE ENERGY USING MIN. & MAX. ANGLE and MAX. EDGE RATIO.

// NB dependent max2, max3, max4 (and min) functions removed.

// double CSkeletonTriangle::energyShape() const
// {
//   const double a0 = getRealAngle(0);
//   const double a1 = getRealAngle(1);
//   const double a2 = 180.0 - (a0+a1);
//   const double l0 = edgeLength(0);
//   const double l1 = edgeLength(1);
//   const double l2 = edgeLength(2);

//   const double min_angle_energy = (60.0-min3(a0, a1, a2))/60.0;
//   const double max_angle_energy = (max3(a0, a1, a2)-60.0)/120.0;
//   const double angle_energy = max2(min_angle_energy, max_angle_energy);

//   const double min_length = min3(l0, l1, l2);
//   const double max_length = max3(l0, l1, l2);
//   const double aspect_energy = 1.0 - min_length/max_length;

//   return max2(angle_energy, aspect_energy*aspect_energy);
// }

// double CSkeletonQuad::energyShape() const
// {  
//   const double a0 = getRealAngle(0);
//   const double a1 = getRealAngle(1);
//   const double a2 = getRealAngle(2);
//   const double a3 = 360.0 - (a0+a1+a2);
//   const double l0 = edgeLength(0);
//   const double l1 = edgeLength(1);
//   const double l2 = edgeLength(2);
//   const double l3 = edgeLength(3);

//   const double min_angle_energy = (90.0-min4(a0, a1, a2, a3))/90.0;
//   const double max_angle_energy = (max4(a0, a1, a2, a3)-90.0)/90.0;
//   const double angle_energy = max2(min_angle_energy, max_angle_energy);

//   const double min_length = min4(l0, l1, l2, l3);
//   const double max_length = max4(l0, l1, l2, l3);
//   const double aspect_energy = 1.0 - min_length/max_length;

//   return max2(angle_energy, aspect_energy*aspect_energy);
// }

// SHAPE ENERGY USING TRIANGLE ALTITUDES
// These should be faster to compute.

// double triangleQ(const Coord &n0, const Coord &n1, const Coord &n2) {
//   // The Q of a triangle is the minimum altitude, squared, over the
//   // maximum side, squared.  The altitude from vertex n to side n is
//   // the length of one of the other sides times the sine of the angle
//   // between that side and side n.  That is,
//   //        h  =  side(n+1) cross side(n)/|side(n)|

//   // Sides
//   Coord s0 = n1 - n2;
//   Coord s1 = n2 - n0;
//   Coord s2 = n0 - n1;

//   double c = cross(s0, s1);
//   double ll0 = norm2(s0);
//   if(ll0 == 0.0) return 0.0;
//   double hh0 = c*c/ll0;

//   c = cross(s1, s2);
//   double ll1 = norm2(s1);
//   if(ll1 == 0.0) return 0.0;
//   double hh1 = c*c/ll1;

//   c = cross(s2, s0);
//   double ll2 = norm2(s2);
//   if(ll2 == 0.0) return 0.0;
//   double hh2 = c*c/ll2;

//   return min3(hh0, hh1, hh2)/max3(ll0, ll1, ll2);
// }

// double CSkeletonTriangle::energyShape() const {
//   The factor of 4/3 normalizes Q so that it's 1 for an equilateral
//   triangle.
//   static const double fourthirds = 4./3.;
//   double q = fourthirds*triangleQ(nodes[0]->position(), nodes[1]->position(),
// 				  nodes[2]->position());
//   double e = 1.-q;
//   return e*e*e;
// }

// double CSkeletonQuad::energyShape() const {
//   A quad can be divided into two triangles in two ways.  The Q of a
//   pair of triangles is the *geometric* mean of their individual Qs.
//   We use the geometric mean so that the Q of a pair is 0 if the Q
//   of either member of the pair is zero.  (The triangle Q is
//   normalized so that it's 1 for a right isosceles triangle.)  The Q
//   of the quad is Q of the pair of triangles with the smaller Q.
//   The energy of the quad is 1-Q.

//   double q0 = triangleQ(nodes[1]->position(), nodes[2]->position(),
// 			nodes[3]->position());
//   double q1 = triangleQ(nodes[2]->position(), nodes[3]->position(),
// 			nodes[0]->position());
//   double q2 = triangleQ(nodes[3]->position(), nodes[0]->position(),
// 			nodes[1]->position());
//   double q3 = triangleQ(nodes[0]->position(), nodes[1]->position(),
// 			nodes[2]->position());
//   double q02 = q0*q2;
//   double q13 = q1*q3;
//   double q = 4*sqrt(q02 < q13 ? q02 : q13); factor of 4 is normalization
//   double e = 1.-q;
//   if(e < 0.0) return 0.0;
//   return sqrt(e*e*e);
// }

double CSkeletonTriangle::energyShape() const
{
  // Old OOF way: 4sqrt(3)*AREA/(L0^2 + L1^2 + L2^2),
  // where L0, L1, L2 represent three edges of the triangle.
  // Equilateral triangle: 1
  static const double four_sqrt_three = 4.*sqrt(3.);
  // perimeterSquared actually is the of the squares of the sides.
  double q = four_sqrt_three*area()/perimeterSquared();
  return 1. - q;
}

double paralleloQ(const Coord &n0, const Coord &n1, const Coord &n2)
{
  // For the case of a square, l0=l1, and area2 = 2*l0*l1 = 2*l0*l0.
  // In the same (square) case, the denominator is l0*l0+l1*l1 =
  // 2*l0*l0, so a square of any size returns 1 from this function.  A
  // bit of examination reveals that any deviation from squareness
  // (either because l1 != l2, or because the angle is not 90 degrees)
  // reduces this value, so this is maximal for squares.
  double area2 = 4.*triangleArea(n0, n1, n2);
  double l0 = norm2(Coord(n0 - n1));
  double l1 = norm2(Coord(n1 - n2));
  return area2/(l0 + l1);
}

#define OPPOSITE_NODE_WEIGHT 1.0e-5

double CSkeletonQuad::energyShape() const
{
  // Copied from GiD (http://gid.cimne.upc.es) manual.
  // GiD is a pre- & post process tool developed in Spain.
  // Take the worst of the values computed at four corners.
  // q = 2*AREA/(L0^2 + L1^2),
  // where AREA is area of parallelogram formed with two edges
  // of the corner node and L0 and L2 represent the two edges.
  double q0 = paralleloQ(nodes[3]->position(), nodes[0]->position(),
			 nodes[1]->position());
  double q1 = paralleloQ(nodes[0]->position(), nodes[1]->position(),
			 nodes[2]->position());
  double q2 = paralleloQ(nodes[1]->position(), nodes[2]->position(),
			 nodes[3]->position());
  double q3 = paralleloQ(nodes[2]->position(), nodes[3]->position(),
			 nodes[0]->position());

  double minq = q0;  // Minimum (most-bad) paralleloQ result
  double oppq = q2;  // paralleloQ from node opposite to minimum.
  if (q1<minq) {
    minq = q1; 
    oppq = q3;
  }
  if (q2<minq) {
    minq = q2; 
    oppq = q0;
  }
  if (q3<minq) {
    minq = q3;
    oppq = q1;
  }

  // Return the weighted sum of the worst case seen and the opposite
  // node.  The reason for this is to make sure that any node movement
  // changes the energy, even if it doesn't shift the minimum.  The
  // reason for using a lopsided weight and not just averaging is that
  // we would still like degenerate sub-triangles of quads to give
  // (nearly) the worst energy possible.  Straight averaging would
  // dilute that.
  return 1.0-((1.0-OPPOSITE_NODE_WEIGHT)*minq + OPPOSITE_NODE_WEIGHT*oppq);
  //return 1. - minq;
}


// Homogeneity computations.
// The HomogeneityData constructor is the One True Place where the
// homogeneity energy is computed.
HomogeneityData::HomogeneityData(double hom, int cat) : homogeneity(hom),
							dominantpixel(cat) {
  homog_energy = 1.0-homogeneity;
							}



