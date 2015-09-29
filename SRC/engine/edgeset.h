// -*- C++ -*-
// $RCSfile: edgeset.h,v $
// $Revision: 1.19 $
// $Author: langer $
// $Date: 2012/02/28 18:39:41 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#ifndef EDGESET_H
#define EDGESET_H

#include "common/doublevec.h"
#include "engine/edge.h"
//#include "femesh.h"
#include <vector>

class Node;
class EdgeNodeIterator;
class EdgeSet;
class EdgeSetIterator;
// class BoundaryNodeIterator;
class Edge;
class FEMesh;

// The "EdgeSet" class has all of the information about 
// the geometry of an EdgeBoundary.  
// For integration, it provides gausspoints,
// weights, and the direction of the normal vector.
// It also provides a guaranteed-unique way of getting
// out the FuncNodes of which it is composed.
//
//   Since materials are not directly relevant, it is 
// possible for the element substructure to be hidden by 
// the iterators, but it still has to be somewhere -- the
// "Edge" class refers to edges of particular elements. 
//
class EdgeNodeDistance;

class EdgeSet {
protected:
  FEMesh *mesh;
  std::vector<BoundaryEdge*> edgelist;
public:
 
  // At creation-time, boundaries don't have any edges in them,
  // they have to be populated via addEdge calls.
  EdgeSet(FEMesh *m);
  ~EdgeSet();

  std::vector<const EdgeNodeDistance*> *ndlist();
  int size() const; 

  // The boundary class takes care of adding edges
  // because it needs to detect the directionality 
  // and maintain the integrity of the edge list,
  // which is expected to cross from one element to
  // another at their shared nodes.
  void addEdge_(BoundaryEdge *);

  EdgeSetIterator edge_iterator() const;

  friend class EdgeSetIterator;
  
  // If, some day, we do dynamical re-gridding, boundaries
  // will have to know how to adjust themselves.
};


class EdgeSetIterator {
private:
  const EdgeSet *bdy;
  // TODO OPT: This object is a bit heavy for an iterator.  Does
  // cumulength_ have to be stored here?  Can it be moved to a
  // reference counted class, so that it doesn't have to be copied
  // when the iterator is copied?  Does it matter? 
  DoubleVec cumulength_;
  double length;
  std::vector<BoundaryEdge*>::size_type index_;
public:
  EdgeSetIterator(const EdgeSet *);
  BoundaryEdge* edge() const { return bdy->edgelist[index_]; }
  double traversed_length() const { return cumulength_[index_]; }
  double total_length() const { return length; };
  void operator++() { index_++; }
  bool end() const { return index_==bdy->edgelist.size(); }
};

std::ostream &operator<<(std::ostream&, const EdgeSetIterator&);


// Progress along an EdgeNode is measured not only by nodes, but also
// by cumulative and fractional distance along the edge, as well as
// node index.  These data are encapsulated in this object for
// convenience.
class EdgeNodeDistance {
public:
  const FuncNode *node;
  int index;
  double distance;
  double fraction;
  EdgeNodeDistance(const FuncNode *fn, int i, double d, double f) :
    node(fn), index(i), distance(d), fraction(f) {}
};




#endif

