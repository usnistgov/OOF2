// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef EDGESET_SWG
#define EDGESET_SWG

%module edgeset

%include "common/typemaps.swg"

%import "femesh.swg"
%import "edge.swg"

%{
#include "engine/edgeset.h"
typedef std::vector<const EdgeNodeDistance*> vecdist;
%}

MAKE_LISTVEC_TYPEMAPS(EdgeNodeDistance);

class EdgeSet {
public:
  EdgeSet(FEMesh *);
  ~EdgeSet();
  void addEdge_(BoundaryEdge *); // Should make the nlistcache stale.

  NewEdgeNodeDistanceVec *ndlist();
  int size();
  // EdgeSetIterator edge_iterator();
};

class EdgeSetIterator {
public:
  EdgeSetIterator(EdgeSet *);
  BoundaryEdge* edge();
  bool end();
};

%extend EdgeSetIterator {
  void increment() {
    self->operator++();
  }
};

/* "distance" is how far along an edgeset you are, in lab-frame
   distance units, and "fraction" is how far along the edgeset you are
   in units of the edgeset length. */

%nodefaultctor EdgeNodeDistance;

class EdgeNodeDistance {
public:
  ~EdgeNodeDistance();
  FuncNode *node;
  int index;
  double distance;
  double fraction;
};

%pythoncode "engine/edgeset.spy"

#endif // EDGESET_SWG
