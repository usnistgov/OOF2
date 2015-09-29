// -*- C++ -*-
// $RCSfile: edgeset.C,v $
// $Revision: 1.24 $
// $Author: langer $
// $Date: 2014/09/27 21:40:43 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "engine/ooferror.h"
#include "common/tostring.h"
#include "common/trace.h"
#include "edge.h"
#include "edgeset.h"
#include "node.h"
#include <algorithm>
#include <iostream>
#include <list>
#include <stdlib.h>
#include <unistd.h>

EdgeSet::EdgeSet(FEMesh *m)
  : mesh(m),
    edgelist(0)
{
}

EdgeSet::~EdgeSet() {
}

// Add an edge you've gotten from an element.  The edgeset enforces
// contiguousness of the edges, so they have to be added in order.
void EdgeSet::addEdge_(BoundaryEdge *ed_in) {

  if(edgelist.size()==0) {
    edgelist.push_back(ed_in);  // Add to back.
  }
  else {
#if 1
    //Interface branch
    //Adjacent mesh elements may no longer be connected.
    //The sanity check within the #else clause no longer valid.
    edgelist.push_back(ed_in);
#else
    BoundaryEdge *lastedge = edgelist[edgelist.size()-1];
    if ( *(lastedge->endnode()) == *(ed_in->startnode()) ) {
      edgelist.push_back(ed_in);
    }
    else {
      throw ErrProgrammingError("Non-contiguous edges passed to edgeset.",
				__FILE__, __LINE__);
    }
#endif
  }
}



// Build a big list of node pointers, and pass it out.  Let
// the caller (presumed to be a Python routine) iterate over it.
// This is where we fulfill the promise of uniqueness.
std::vector<const EdgeNodeDistance*> *EdgeSet::ndlist() {
  // This object gets deleted by the copy-out typemap in boundary.swg
  std::vector<const EdgeNodeDistance*> *elist = 
    new std::vector<const EdgeNodeDistance*>;

  //  Trace("EdgeSet::ndlist");
  EdgeSetIterator i = EdgeSetIterator(this);
  double edge_length = i.total_length();
  int index = 0;
  for(; !i.end(); ++i) {
    //    Trace("EdgeSet::ndlist edgelist " + to_string(i));
    for( EdgeNodeIterator e=i.edge()->node_iterator(); !e.end(); ++e) {
      // Edgeset is guaranteed contiguous, so we can remove duplicates
      // as we go along here.  Push the node on the list only if it's
      // not already the most recent one.  Pointer comparison is safe
      // here because the nodes are guaranteed to be FuncNodes.
      int listsize = elist->size();
      if ( (listsize==0)  || (*elist)[listsize-1]->node != e.funcnode() ) {
	// NB: This is the undistorted boundary length.
	double distance = i.traversed_length() + 
	  e.fraction()*(i.edge()->lab_length());

	double edgeset_fraction = distance/edge_length;
	elist->push_back(new EdgeNodeDistance( e.funcnode(),
					       index, distance,
					       edgeset_fraction) );
	index++;
      }
    }
  }
  return elist;
}

int EdgeSet::size() const {
  return edgelist.size();
}

EdgeSetIterator EdgeSet::edge_iterator() const {
  return EdgeSetIterator(this);
}

//--\\||//--\\||//--\\||//--\\||//--\\||//--\\||//--\\||//--\\||

// EdgeSetIterators.  We assume that, during the lifetime of the
// EdgeSetIterator, the nodes do not move, so we can reasonably
// compute the proper (lab-space) length of individual edges, and the
// cumulative length of the set.

EdgeSetIterator::EdgeSetIterator(const EdgeSet *b):  
  bdy(b), length(0.0), index_(0) {

  cumulength_.reserve(bdy->edgelist.size());

  // Loop over all the edges in the EdgeSet, and total up their
  // lengths.  At the end, cumulength[i] is the length of all the
  // previous edges up to but not including the edge indexed by i.
  for (std::vector<BoundaryEdge*>::const_iterator i=bdy->edgelist.begin();
       i!=bdy->edgelist.end(); ++i) {
    cumulength_.push_back(length);
    length += (*i)->lab_length();
  }
}

std::ostream &operator<<(std::ostream &os, const EdgeSetIterator &esi) {
  return os << "EdgeSetIterator(" << esi.traversed_length() << ")";
}
