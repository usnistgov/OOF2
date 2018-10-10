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

// Set of perturbation directions for moving nodes.  This is a set of
// nonhorizontal, nonvertical unit vectors which are candidate
// directions for perturbing nodes when searching for intersections
// with pixel-boundary segments.  The exclusion of the i=0 case is
// deliberate.  Nodes are perturbed so that they won't lie directly on
// top of pixel boundaries, which complicates the intersection finding
// code.

// This should be prime, and greater than one more than the number of
// sides of the most-sided possible element.
#define NODE_PERTURB_DIRECTIONS 7


// node_perturbations() returns a Coord* instead of a
// std::vector<Coord> because it's just a little bit faster.  It's
// used in a context (in categoryAreas()) where speed is important.

static const Coord* node_perturbations() {
  static Coord *perturbation_list = 0;
  if(!perturbation_list) {
    // This shows up as a memory leak in valgrind.  It's not, really.
    perturbation_list = new Coord[NODE_PERTURB_DIRECTIONS-1];
    double delta = 2.0*M_PI/((double) NODE_PERTURB_DIRECTIONS);
    for(int i=1; i<NODE_PERTURB_DIRECTIONS; i++) {
      double angle = i*delta;
      perturbation_list[i-1] = Coord(cos(angle), sin(angle));
    }
  }
  return perturbation_list;
}

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

// CategoryArea calculation, and related infrastructure.

typedef std::multimap<double, PixelBdyIntersection> ElEdgeMap;
typedef std::vector<ElEdgeMap> ElEdge;
typedef std::pair<double, PixelBdyIntersection> ElEdgeDatum;


typedef std::multimap<Coord, PixelBdyIntersection> CoordIsec;
typedef std::pair<Coord, PixelBdyIntersection> CoordIsecDatum;

// Utility function for deleting an intersection from one of the
// ordered lists of intersections.  Intersections have sufficient data
// to locate themselves in these lists.
void delete_isec(const PixelBdyIntersection &pbi,
		 ElEdge &eledge) {
  int ni = pbi.get_element_node_index();
  double fr = pbi.get_element_fraction();
  
  int count = eledge[ni].count(fr);
  if (count==1) {
    eledge[ni].erase(fr);
  }
  else {
    ElEdgeMap::iterator emi = eledge[ni].lower_bound(fr);
    for(int i=0; i<count; ++emi, ++i) {
      if (((*emi).second.location==pbi.location) && 
	  ((*emi).second.entry==pbi.entry) ) {
	eledge[ni].erase(emi);
	break;
      }
    }
  }
}

//================

// Another utility function, this one for checking whether a point is
// interior or exterior to the element, using the perturbation-hint to
// resolve ambiguous cases.  If the cross-product of any element
// segment with the candidate point minus the start of the segment is
// negative, it means the point is exterior to that segment.  A point
// is exterior to the element if it is exterior to any segment.

// This function is used heavily during the homogeneity calculation.
// Rewriting it so that it uses doubles instead of Coords did not
// improve the speed.  (But that was before replacing
// std::vector<Coord> with a simple array...)
bool CSkeletonElement::interior(const Coord &pt, 
				const Coord &perturb) const
{
  int nn = nnodes();
  if(nn==3) {			// Loops unrolled
    Coord pos0 = nodes[0]->position();
    Coord pos1 = nodes[1]->position();
    Coord pos2 = nodes[2]->position();

    Coord edge = pos1 - pos0;
    double cross = edge % (pt - pos0);
    if(cross < 0.0)
      return false;
    if(cross == 0) {
      if(perturb % edge < 0.0)
	return false;
    }
    edge = pos2 - pos1;
    cross = edge % (pt - pos1);
    if(cross < 0.0)
      return false;
    if(cross == 0) {
      if(perturb % edge < 0.0)
	return false;
    }
    edge = pos0 - pos2;
    cross = edge % (pt - pos2);
    if(cross < 0.0)
      return false;
    if(cross == 0) {
      if(perturb % edge < 0.0)
	return false;
    }
    return true;
  }

  else if(nn == 4) {
    Coord pos0 = nodes[0]->position();
    Coord pos1 = nodes[1]->position();
    Coord pos2 = nodes[2]->position();
    Coord pos3 = nodes[3]->position();

    Coord edge = pos1 - pos0;
    double cross = edge % (pt - pos0);
    if(cross < 0.0)
      return false;
    if(cross == 0) {
      if(perturb % edge < 0.0)
	return false;
    }
    edge = pos2 - pos1;
    cross = edge % (pt - pos1);
    if(cross < 0.0)
      return false;
    if(cross == 0) {
      if(perturb % edge < 0.0)
	return false;
    }
    edge = pos3 - pos2;
    cross = edge % (pt - pos2);
    if(cross < 0.0)
      return false;
    if(cross == 0) {
      if(perturb % edge < 0.0)
	return false;
    }
    edge = pos0 - pos3;
    cross = edge % (pt - pos3);
    if(cross < 0.0)
      return false;
    if(cross == 0) {
      if(perturb % edge < 0.0)
	return false;
    }
    return true;
  }

  else {
    // This is the generic case, for nn!=3 and nn!=4, which will
    // probably never occur.  
    Coord *pos = new Coord[nn];
    bool result = true;
    for(int ni=0; ni<nn; ++ni) {
      pos[ni] = nodes[ni]->position();
    }

    for(int ni=0; ni<nn; ++ni) {
      const Coord &posni = pos[ni];
      Coord edge = pos[(ni+1)%nn] - posni;
      double cross = edge % (pt-posni);
      if (cross < 0) {
	result = false;
	break;
      }
      else if (cross==0) {
	if (perturb % edge < 0) {
	  result = false;
	  break;
	}
#ifdef DEBUG
	if (perturb % edge == 0) {
	  std::cerr << "Ambiguous interiority after perturbation!" 
		    << std::endl;
	}
#endif // DEBUG
      }
    }
    delete[] pos;
    return result;
  }
  return 0;
}

//==============

CRectangle CSkeletonElement::bbox() const {
  CRectangle bounds(nodes[0]->position(), nodes[1]->position());
  for(int i=2; i<nnodes(); i++)
    bounds.swallow(nodes[i]->position());
  return bounds;
}

//=============

// Returns a vector of doubles (or a null pointer if the element is so
// badly formed that the areas aren't computable).  Each double in
// this vector is equal to the area of the corresponding
// microstructure category which is within this element.

const DoubleVec * CSkeletonElement::categoryAreas(const CMicrostructure &ms,
						  bool verbose)
  const
{
  // std::cerr << std::endl << "categoryAreas: new Element" << std::endl;

  // nCategories() recomputes categories & boundaries if needed.
  unsigned int ncat = ms.nCategories();
  // std::cerr << "categoryAreas: nCategories=" << n << std::endl;
  DoubleVec *result = new DoubleVec(ncat);
  bool areas_zero = true;
  int nn = nodes.size();

  if(verbose) {
    std::cerr << "categoryAreas: Nodes: " << std::endl;
    for(int di=0; di<nn; ++di) {
      std::cerr << "   " << nodes[di]->position() << std::endl;
    }
  }
    
  // Build up element data for easy passage to intersection-finder.
  //   std::vector<Coord> element_points(nn);
  Coord *element_points = new Coord[nn];
  for(int nj=0; nj<nn; ++nj) {
    element_points[nj] = nodes[nj]->position();
  }

  // For perturbations, select the first one which is not parallel to
  // any element segment.  The set is already guaranteed to be
  // nonhorizontal and nonvertical, so it can't be parallel to the
  // pixel-set boundary.
  Coord element_perturb;
  const Coord *const ptbs = node_perturbations();
  for(int pt=0; pt<NODE_PERTURB_DIRECTIONS-1; ++pt) {
    bool parallel = false;
    for(int el=0;el<nn;++el) {
      Coord v = element_points[(el+1)%nn]-element_points[el];
      if ((ptbs[pt] % v) == 0 ) {
	parallel = true;
	break;
      }
    }
    if (parallel==false) {
      element_perturb = ptbs[pt];
      break;
    }
  }
  assert(element_perturb != Coord(0.0,0.0));
  if(verbose)
    std::cerr << "CSkeletonElement::categoryAreas: element_perturb="
	      << element_perturb << std::endl;

  // Get all the category boundaries.
  const std::vector<PixelSetBoundary*> &bdys = ms.getCategoryBdys();

  assert(bdys.size() == ncat);

  for(std::vector<PixelSetBoundary>::size_type i=0; i<bdys.size(); i++) {

    if(verbose)
      std::cerr << "------" << std::endl
		<< "categoryAreas: Examining a new category, " << i
		<< " rep. pxl " << ms.getRepresentativePixel(i) << std::endl;
    double accum_area = 0.0;
    const std::vector<PixelBdyLoop*> &loops = bdys[i]->get_loops();
   
    // Per-element-segment intersection data.
    PixelBdyIntersection pbi;

    // Store intersection data -- used to figure out what sections
    // of the element boundaries contribute to the area.  Stored a
    // couple of ways -- firstly by element edge, so it can be
    // easily traversed, and secondly indexed by coordinate, so
    // duplicates can be removed.
    ElEdge eledgedata(nn);  // vector of multimap<double, PixelBdyIntersection>
    CoordIsec coordisecs;   // multimap<Coord, PixelBdyIntersection>

    // Loop over all of the boundary loops of this pixel category.
    for(std::vector<PixelBdyLoop*>::const_iterator pbl = loops.begin();
	pbl!=loops.end(); ++pbl)
      {
	const PixelBdyLoop &loop = *(*pbl);
	if(verbose)
	  std::cerr << "categoryAreas: starting loop of size " << loop.size()
		    << std::endl;
	  //std::cerr << "categoryAreas: loop=" << loop << std::endl;

	// Skip this loop if its bounding box doesn't intersect the
	// element's bounding box.
	if(!bbox().intersects(loop.bbox())) {
	  // if(verbose)
	  //   std::cerr << "categoryAreas: no bbox intersection" << std::endl;
	  continue;
	}

	// Find the interiority of the start of the first pixel
	// boundary segment.  End-point interiorities are done on the
	// fly in the k loop.  Start point interiorities for every
	// point after the first are the same as the end point
	// interiority of the previous point.
	bool pbs_start_inside = interior(loop.coord(0), element_perturb);

	int loopsize = loop.size();
	// Loop over points on the boundary loop
	for(unsigned int k=0; k<loopsize; ++k) {
	  const Coord pbs_start = loop.coord(k);
	  const Coord pbs_end = loop.next_coord(k);
	  bool pbs_end_inside = interior(pbs_end, element_perturb);
	  // if(verbose)
	  //   std::cerr << "categoryAreas: pbs_start= " << pbs_start
	  // 	      << " interior=" << pbs_start_inside 
	  // 	      << "    pbs_end  = " << pbs_end
	  // 	      << " interior=" << pbs_end_inside << std::endl;
	  
	  if (pbs_start_inside && pbs_end_inside) {
	    // Pixel boundary segment is wholly interior, add the area.
	    // This is ok because the element is guaranteed to be
	    // convex.
	    // if(verbose)
	    //    std::cerr << "categoryAreas: pbs wholly interior, dA="
	    // 		 << pbs_start % pbs_end << std::endl;
	    accum_area += pbs_start % pbs_end;
	  }
	  // If start and end are hetero-interior, so to speak, then
	  // there's an intersection.  Find it.
	  else if (pbs_start_inside != pbs_end_inside) {
	    int seg = loop.find_one_intersection(k, element_points, nn,
						 pbs_end_inside, pbi);
	    // if(verbose)
	    //    std::cerr << "categoryAreas: one intersection at "
	    // 		 << pbi.location << std::endl;
	      
	    double f = norm2(pbi.location - element_points[seg]);
	    pbi.set_element_data(seg,f);
	    eledgedata[seg].insert(ElEdgeDatum(f, pbi));
	    
	    coordisecs.insert(CoordIsecDatum(pbi.location, pbi));
	      
	    // Accumulate the area of the interior portion.
	    if (pbs_start_inside) {
	      // if(verbose)
	      // 	 std::cerr << "categoryAreas: in->out, dA="
	      // 		   << loop.coord(k) % pbi.location << std::endl;
	      accum_area += pbs_start % pbi.location;
	    }
	    else {
	      // if(verbose)
	      // 	 std::cerr << "categoryAreas: out->in, dA="
	      // 		   << pbi.location % loop.next_coord(k) << std::endl;
	      accum_area += pbi.location % pbs_end;
	    }
	  } // end if bdy segment has exactly one endpoint inside
	  else {
	    assert( !pbs_start_inside && !pbs_end_inside );
	    // The current segment has both endpoints outside the
	    // element.  It must intersect zero or two times.  Find out.
	    
	    bool no_isecs = loop.find_no_intersection(k, element_points, nn,
						      element_perturb);

	  if (!no_isecs) {
	    // if(verbose)
	    //    std::cerr << "categoryAreas: two intersections" << std::endl;
	    // We know there have to be two intersections, find them.
	    PixelBdyIntersection isec0, isec1;

	    // Entry first.
	    int s1 = loop.find_one_intersection(k, element_points, nn,
						true, isec0);
	    // if(verbose)
	    //   std::cerr << "categoryAreas:    isec0=" << isec0.location
	    // 		<< std::endl;
	    double f =  norm2(isec0.location - element_points[s1]);
	    isec0.set_element_data(s1, f);
	    eledgedata[s1].insert(ElEdgeDatum(f, isec0));
	    
	    // Then find the exit.
	    int s2 = loop.find_one_intersection(k, element_points, nn,
						false, isec1);
	    // if(verbose)
	    //    std::cerr << "categoryAreas:    isec1=" << isec1.location
	    // 		 << std::endl;
	    f = norm2(isec1.location - element_points[s2]);
	    isec1.set_element_data(s2, f);
	    eledgedata[s2].insert(ElEdgeDatum(f, isec1));


	    // Measure distance along the segment, for
	    // coincidence-checking and sorting.
	    double d1 = norm2(isec0.location - loop.coord(k));
	    double d2 = norm2(isec1.location - loop.coord(k));

	    // If two intersections coincide, they should annihilate.
	    if (d1==d2) {
	      if (isec0.entry != isec1.entry) {
		// if(verbose)
		//   std::cerr << "categoryAreas:    Annihilation." << std::endl;
		delete_isec(isec0, eledgedata);
		delete_isec(isec1, eledgedata);
	      }
	      else {
		throw ErrProgrammingError(
		  "CategoryAreas: Coincident intersections do not annihilate!",
		  __FILE__, __LINE__);
	      }
	    }
	    // The intersections are not coincident.
	    else {
	      // Order the intersections.  Topologically, the first
	      // one has to be an entry, but if they're very close
	      // together, they could come out in the wrong order by
	      // roundoff.  If this happens, they're within roundoff
	      // of each other, and the area is zero -- delete them.
	      
	      PixelBdyIntersection &one = ( d1 < d2 ? isec0 : isec1 );
	      PixelBdyIntersection &two = ( d1 < d2 ? isec1 : isec0 );
	      
	      // Expected case, first intersection is an entry.  Add
	      // them to the coordisecs structure, and accumulate the
	      // area.
	      if (one.entry) { 
		coordisecs.insert(CoordIsecDatum(one.location, one));
		coordisecs.insert(CoordIsecDatum(two.location, two));
		accum_area += one.location % two.location;
		if(verbose)
		   std::cerr << "categoryAreas:   dA="
			     << one.location % two.location << std::endl;
	      }
	      // Pathological case -- if they're in the topologically
	      // disallowed order, it must be because of roundoff, and
	      // so they must be within roundoff of each other.
	      // Remove them.
	      else {
		if(verbose)
		  std::cerr << "categoryAreas:   wrong order" << std::endl;
		delete_isec(one, eledgedata);
		delete_isec(two, eledgedata);
	      }
	    } // End of non-coincident, two-intersection case.

	  } // End of conditional based on find_no_intersections result.

	} // End of both-endpoints-exterior block.
  
	// Hand off status info in preparation for next pixel bdy segment.
	pbs_start_inside = pbs_end_inside;
      } // End of loop over segments.
    } // End of loop over pixel-boundary loops.  
    

    // // Debugging -- list all intersections.
    // if(verbose) {
    //   std::cerr << "categoryAreas: Pre-annihilation, all intersections: " 
    // 		<< std::endl;
    //   for(int ni = 0; ni<nn; ++ni) {
    // 	for(ElEdgeMap::iterator there = eledgedata[ni].begin();
    // 	    there!=eledgedata[ni].end(); ++there)
    // 	  {
    // 	    std::cerr << "   Intersection: " << (*there).second << std::endl;
    // 	  }
    //   }
    // }

    if(verbose)
      std::cerr << "categoryAreas: after loop over bdy loops, accum_area="
		<< accum_area << std::endl;
    

    // At this point, we have accumulated all the area contributions
    // from the segments which are boundaries of the pixel set, and
    // are interior to the current element.  It remains to traverse
    // the element exterior and add up the contributions from those
    // portions of it which are between an exit intersection and an
    // entry intersection.

    // But first... Check for multiple coincident intersections.
    // These can arise when the corner of an element and the corner of
    // a pixel boundary coincide, and the perturbation resolution is
    // such that the corner point of the pixel boundary set is inside
    // the element, but only by epsilon.  Because each intersection is
    // on a different element-segment/pixel-boundary-segment pair,
    // they don't get picked up earlier.  Coincident intersections
    // cannot be ordered, and so are confusing to the traversal code,
    // so we rationalize them here.

    // Debugging
    if(verbose) {
      std::cerr << "categoryAreas: coordisecs" << std::endl;
      for(CoordIsec::iterator x=coordisecs.begin(); x!=coordisecs.end(); ++x) {
	Coord key = (*x).first;
	std::cerr << "    " << key << " (" << coordisecs.count(key) << ") "
		  << (*x).second << std::endl;
      }
    }

    CoordIsec::iterator x = coordisecs.begin();
    while(x != coordisecs.end()) {
      Coord key = (*x).first;
      int ct = coordisecs.count(key);
      if (ct > 1) {

// #ifdef DEBUG
// 	std::cerr << "Nontrivial coordisec run." << std::endl;
// 	std::cerr << "Coord is " << key << std::endl;
// 	std::cerr << "Count is " << ct << std::endl;
// #endif	// DEBUG

	CoordIsec::iterator w = x;

	// Set x to the start of the next key, for the next
	// iteration of the outer loop.
	x = coordisecs.upper_bound(key);

	// Determine the sign of the resultant intersection.  It may
	// be entry, exit, or zero, if everything cancels out.
	int entries = 0;
	int exits = 0;
	for(CoordIsec::iterator t = w; t!=x; ++t) {
	  ( (*t).second.entry ? entries++ : exits++ );
	}

// #ifdef DEBUG
// 	std::cerr << "Entries: " << entries << ", exits: " << exits
// 		  << std::endl;
// #endif	// DEBUG
	
	if (entries > exits) {
	  // Keep the first entry in the set of coincident points, and
	  // delete the rest.
	  bool got_entry = false;
	  for(CoordIsec::iterator t2 = w; t2!=x; ++t2) {
	    if ((*t2).second.entry && !got_entry)
	      got_entry = true;
	    else 
	      delete_isec((*t2).second, eledgedata);
	  }
	}
	else if (entries < exits) {
	  bool got_exit = false;
	  for(CoordIsec::iterator t2 = w; t2!=x; ++t2) {
	    if (!(*t2).second.entry && !got_exit)
	      got_exit = true;
	    else 
	      delete_isec((*t2).second, eledgedata);
	  }
	}
	else {
	  for(CoordIsec::iterator t2 = w; t2!=x; ++t2)
	    delete_isec((*t2).second, eledgedata);
	}
	
      }	     // end if ct > 1
      else { // Key only occurs once, move on.
	++x;
      }
    } // end search for multiple coincident intersections

    // Also check for multiple intersections where more than one pixel
    // boundary segment intersects an element edge at the same spot.
    // These ought to cancel each other.  If they're left in, the loop
    // below might see them in the wrong order, and get confused about
    // the sequence of entries and exits.

    if(verbose)
      std::cerr << "categoryAreas: starting coincidence check" << std::endl;
    for(int ni=0; ni<nn; ni++) { // loop over edges
      // loop over intersections on this edge
      ElEdgeMap::iterator ii = eledgedata[ni].begin();
      while(ii != eledgedata[ni].end()) {
	double frac = (*ii).first; // parametric position of intersection
	// std::cerr << "categoryAreas: frac=" << frac << std::endl;
	int ninter = eledgedata[ni].count(frac); // # of intersections at frac
	// std::cerr << "categoryAreas: ninter=" << ninter << std::endl;
	if(ninter > 1) {
	  // coincidences detected
	  std::pair<ElEdgeMap::iterator, ElEdgeMap::iterator> range =
	    eledgedata[ni].equal_range(frac);
	  int entries = 0;
	  int exits = 0;
	  for(ElEdgeMap::iterator k=range.first; k!=range.second; ++k) {
	    if((*k).second.entry)
	      entries++;
	    else
	      exits++;
	  }
	  if(entries != exits) {
	    // entries-exits can never be something other than -1, 0,
	    // or 1, because the directions and number of pixel
	    // boundary segments at a point are limited.  This code is
	    // actually more general than it needs to be.
	    bool keep_entry = entries > exits;
	    bool found_one = false;
	    for(ElEdgeMap::iterator j=range.first; j!=range.second; ++j) {
	      if((*j).second.entry == keep_entry && !found_one)
		found_one = true;
	      else
		eledgedata[ni].erase(j);
	    }
	  }
	  else {		// entries == exits
	    eledgedata[ni].erase(range.first, range.second);
	  }
	  ii = range.second;	// go on to next frac
	}			// end if ninter > 1
	else {			// only one intersection at this frac
	  ++ii;
	}
      } // end loop over intersections on this edge
    } // end loop over edges ni
    // std::cerr << "categoryAreas: done with coincidence check" << std::endl;

    // Now traverse the boundary of the element, adding in the area
    // contribution from all the portions that are between an exit and
    // an entry.  "exit" means that the pixel set boundary segment is
    // exiting the element.  (When the pixel set boundary is outside
    // the element, the boundary of the intersection follows the
    // element boundary.)
      
    int icount = 0;
    for(int n=0; n<nn; n++) {	// loop over element edges
      icount += eledgedata[n].size();
    }
    if(verbose)
      std::cerr << "categoryAreas: icount=" << icount << std::endl;
    if (icount > 0) {

      // Debugging -- review all intersections.
      if(verbose) {
	std::cerr << "categoryAreas: All intersections: " << std::endl;
	for(int ni = 0; ni<nn; ++ni) {
	  std::cerr << "   Edge " << ni << std::endl;
	  for(ElEdgeMap::iterator there = eledgedata[ni].begin();
	      there!=eledgedata[ni].end(); ++there)
	    {
	      std::cerr << "       " << (*there).second << " df="
			<< ((*there).second.get_element_fraction() -
			    (*eledgedata[ni].begin()).second.get_element_fraction())
			<< std::endl;
	    }
	}
      }
      
      Coord starting_point;
      Coord last_exit;  // to Brooklyn
      int current_segment = 0;
      bool done=false;
      bool started=false;
      bool outside=false;
      ElEdgeMap::iterator here = eledgedata[0].begin();
      

#ifdef DEBUG
      int et_count = 0;		// infinite loop check
#endif	// DEBUG

      while(!done) {
#ifdef DEBUG
	et_count++;
	assert(et_count < 10000);
#endif	// DEBUG
	if(verbose) {
	  if(here != eledgedata[current_segment].end()) {
	    std::cerr << "categoryAreas: top of loop, here=" << (*here).second
		      << " started=" << started << " outside=" << outside
		      << std::endl;
	  }
	}
	
	// If you've reached the end of a segment, switch to the
	// next segment.  If you're collecting areas, collect from
	// the last exit to the end of the segment, and set
	// last_exit to the beginning of the new segment.
	if (here == eledgedata[current_segment].end() ) {
	  current_segment = (current_segment + 1)%nn;
	  here = eledgedata[current_segment].begin();
	  // std::cerr << "categoryAreas: new segment "
	  // 	    << nodes[current_segment]->position() << " "
	  // 	    << nodes[(current_segment+1)%nn]->position() 
	  // 	    << " here=" << (*here).second
	  // 	    << std::endl;
	  
	  if (started && outside) {
	    // Segment already incremented, end_pt is end of
	    // previous segment, start of new current segment.
	    Coord end_pt = nodes[current_segment]->position();
	    // std::cerr << "categoryAreas: (1) Adding area from " << last_exit
	    // 	      << " to " << end_pt << ",  dA=" << last_exit % end_pt
	    // 	      << std::endl;
	    accum_area += last_exit % end_pt;
	    last_exit = end_pt;
	  }
	} // end if you've reached the end of a segment
	
	// If you've found an exit point, first check if you're
	// already outside.  If so, add the area from the last exit
	// point to this one.  Then, check if it's the initial exit
	// point -- if so, you're done.  Otherwise, update the
	// last_exit and set the "outside" marker to true.  If you
	// haven't started yet, then start, and set the starting
	// point.
	else if (!(*here).second.entry) {
	  if (started && outside) {
	    if(verbose)
	      std::cerr << "categoryAreas: (2) Adding area from " << last_exit
			<< " to " << (*here).second.location
			<< ", dA=" << last_exit % (*here).second.location
			<< std::endl;
	    accum_area += last_exit % (*here).second.location;
	  }
	  if (started && (*here).second.location==starting_point ) {
	    if(verbose)
	       std::cerr << "categoryAreas: back at starting point, done"
			 << std::endl;
	    done = true;
	  }
	  else {
	    if (!started) {
	      started = true;
	      starting_point = (*here).second.location;
	      if(verbose)
		std::cerr << "categoryAreas: starting point = "
			  << starting_point << std::endl;
	    }
	  }
	  outside = true;
	  last_exit = (*here).second.location;
	  ++here;
	} // end if you've found an exit point
	
	// If you've found an entrance point, and you're outside, then
	// add the area from the last exit point to here, and set the
	// outside flag to false.  If you find an entrance point and
	// you're not outside, do nothing.
	else if ((*here).second.entry) {
	  if (started && outside) {
	    if(verbose)
	      std::cerr << "categoryAreas: (3) Adding area from " << last_exit
			<< " to " << (*here).second.location << ", dA="
			<< last_exit % (*here).second.location << std::endl;
	    accum_area += last_exit % (*here).second.location;
	    outside = false;
	  }
	  // else
	  //   std::cerr << "categoryAreas: ignoring entry point" << std::endl;
	  ++here;
	} // end if you've found an entrance point
	
      }	// end while !done
    } // end if icount > 0
    else {
      if(verbose)
	std::cerr << "categoryAreas: no intersections" << std::endl;
      // If there are no intersections, we either need to add all of
      // the element boundary, or none of it.  If the area so far is
      // negative, we need all of it.  Actually, we need 2x it,
      // because the cross-products double-count the area, and this
      // needs to play the same game.
      if (accum_area < 0.0) {
	// This can happen only when the pixel set is annular, and the
	// element lies within the outer loop of the pixel set
	// boundary and encloses the inner loop.  If the element is
	// completely homogeneous, it'll be handled below.
	accum_area += 2.0*area();
      }
    }

    // "accum_area" now contains 2x the contribution of all loops of this
    // category to this element.
    (*result)[i] = 0.5*accum_area;
    if (accum_area != 0.0) {
      areas_zero = false;
    }
    if(verbose)
      std::cerr << "categoryAreas: finished category " << i
		<< " accum_area=" << accum_area << std::endl;

  } // End of loop over categories.

  // If all of the areas are zero, then the element is homogeneous.
  // Figure out which category is the right one by getting the
  // category of the central point.  The central point is used
  // because, for a homogeneous element, round-off will not put it
  // into a different category.  This may end up being slow.
  if (areas_zero) {
    if(verbose)
      std::cerr << "categoryAreas: all areas are zero" << std::endl;
    int cat = ms.category(center());
    (*result)[cat] = area();
  }
    
  // Check that the area of the element is equal to the sum of the
  // areas of the categories.  This check used to raise an exception
  // if it failed.  That made the gui tests fail, which they shouldn't
  // have, because if a Skeleton contains illegal elements, it can
  // also contain legal elements that have nodes outside the
  // Microstructure, which will cause the area sum to be incomplete.
  // So now, if the sum doesn't equal the area, this
  // function returns a null result and doesn't raise an exception.
  bool ok = true;
#ifdef DEBUG
#define CSKELETON_PIXELBDY_AREA_TOL 1.0e-6
  double sum = 0;
  for(unsigned int ct=0; ct<result->size(); ct++) {
    // std::cerr << "categoryAreas: area[" << ct << "]=" << (*result)[ct]
    // 	      << std::endl;
    sum += (*result)[ct];
  }
  double a = area();
  double frac = (sum-a)/a;
  // The areas should be exactly equal, but round-off may make them
  // slightly unequal.  What we're actually looking for here is
  // evidence of some kind of book-keeping error or logic problem in
  // the foregoing intersection computation.  If this occurs, the
  // fractional area is likely to deviate by a large amount.

  ok = fabs(frac) < CSKELETON_PIXELBDY_AREA_TOL;
  if(!ok) {
    std::cerr << "categoryAreas: Error! sum=" << sum << " area=" << area()
	      << " fraction=" << fabs(frac) << std::endl;
  }
  // else
  //   std::cerr << "categoryAreas: consistency check passed." << std::endl;
#endif // DEBUG

  delete[] element_points;
  if(!ok) {
    delete result;
    return 0;
  }

  // Minor hack -- round-off can make some values less than zero.
  // Clamp these to zero.
  for(DoubleVec::size_type ct=0; ct<result->size(); ct++) {
    if ((*result)[ct] < 0)
      (*result)[ct] = 0;
  }
  return result;  // Caller must de-allocate this vector.
} // end of CSkeletonElement::categoryAreas


// OBSOLETE.  Not yet removed, because it may be the only caller of
// some of the other routines, and they may need to be removed also.
// const DoubleVec *
// CSkeletonElement::old_categoryAreas(CMicrostructure &ms) const {
//   int ncategories = ms.nCategories();
//   //std::cerr << "before underlying_pixels(ms)" << std::endl;
//   const std::vector<ICoord> *pixels = underlying_pixels(ms);
//   //std::cerr << "after underlying_pixels(ms)" << std::endl;
//   // Find the categories of the underlying pixels, and determine if
//   // they're all the same.  If they are, we can skip the fractional
//   // area calculation.
//   if(pixels->size() == 0)
//     throw ErrProgrammingError("No pixels under element!", __FILE__, __LINE__);
//   std::vector<int> categories(pixels->size());
//   bool uniform = true;
//   categories[0] = ms.category((*pixels)[0]);
//   for(std::vector<int>::size_type i=1; i<categories.size(); i++) {
//     categories[i] = ms.category((*pixels)[i]);
//     uniform = uniform && (categories[i]==categories[i-1]);
//   }

//   DoubleVec *areas = new DoubleVec(ncategories, 0.0);

//   if(uniform) {
//     (*areas)[categories[0]] = area();
//   }
//   else {
//     // Fractional area calculation.
//     Coord pxlsize(ms.sizeOfPixels());
//     for(std::vector<ICoord>::size_type i=0; i<pixels->size(); i++) {
//       int category = categories[i];
//       (*areas)[category] += pixel_intersection(&(*pixels)[i], &pxlsize);
//     }
//   }
//   delete pixels;
  
//   return areas;
// } // end of old_categoryAreas

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double CSkeletonElement::homogeneity(const CMicrostructure &ms, bool verbose)
  const
{
  findHomogeneityAndDominantPixel(ms, verbose);
  return homogeneityData.value().get_homogeneity();
}

int CSkeletonElement::dominantPixel(const CMicrostructure &ms,
				    bool verbose) const {
  findHomogeneityAndDominantPixel(ms, verbose);
  return homogeneityData.value().get_dominantpixel();
};

double CSkeletonElement::energyHomogeneity(const CMicrostructure &ms) const {
  findHomogeneityAndDominantPixel(ms, /*verbose=*/ false);
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

void CSkeletonElement::findHomogeneityAndDominantPixel(const CMicrostructure &ms,
						       bool verbose)
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
  homogeneityData.set_value(c_homogeneity(ms, verbose)); // recompute
}

// Find the homogeneity of the current element.  Element is assumed to
// be legal -- categoryAreas will throw an exception if it isn't.
HomogeneityData CSkeletonElement::c_homogeneity(const CMicrostructure &ms,
						bool verbose)
  const
{
  if(illegal())
    return HomogeneityData(0, UNKNOWN_CATEGORY);
  const DoubleVec *areas = categoryAreas(ms, verbose);
  if(!areas) {
    // Element is not illegal, but has parts outside of the
    // Microstructure because some *other* element is illegal. 
    return HomogeneityData(0, UNKNOWN_CATEGORY);
  }
  if(verbose) {
    std::cerr << "CSkeletonElement::c_homogeneity: areas=";
    for(double a : *areas)
      std::cerr << " " << a;
    std::cerr << std::endl;
  }
  int category = 0;
  double maxarea=0.0;
  for(DoubleVec::size_type i=0;i<areas->size();++i) {
    double area = (*areas)[i];
    if(area > maxarea) {
      maxarea = area;
      category = i;
    }
  }
  double homogeneity = maxarea/area();
  delete areas;
  if (homogeneity>1.0) homogeneity=1.0;

  if(verbose) {
    std::cerr << "CSkeletonElement::c_homogeneity: nodes=";
    for(CSkeletonNode *n : nodes)
      std::cerr << " " << n->position();
    std::cerr << " homogeneity=" << homogeneity << std::endl;
  }
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



