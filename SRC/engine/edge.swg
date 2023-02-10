// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef EDGE_SWG
#define EDGE_SWG

%module(package="ooflib.SWIG.engine") edge

%include "common/typemaps.swg"
%import "common/coord.swg"
%import "engine/field.swg"
%import "engine/node.swg"
%import "engine/element.swg"
%import "engine/mastercoord.swg"
%import "engine/outputval.swg"

%{
#include "engine/edge.h"
#include "engine/outputval.h"
  #include "engine/flux.h"	// SWIGBUG
%}

MAKE_LISTVEC_TYPEMAPS(Coord);

class Edge {
public:
  Edge(const Element *, const FuncNode*, const FuncNode*);
  ~Edge();
  %newobject position_;
  CoordVec* position(const std::vector<double>*);
  %newobject outputFields;
  ArithmeticOutputValueVec *outputFields(const FEMesh*, const Field&,
					 const std::vector<double>*);
  int order();
  MasterCoord startpt();
  MasterCoord endpt();
};

class BoundaryEdge : public Edge  {
public:
  BoundaryEdge(const Element *elin, int n);
  ~BoundaryEdge();
  bool edge_match(const FuncNode *, const FuncNode *);
  Element *element();
  Node *startnode();
  Node *endnode();
};

#endif // EDGE_SWG
