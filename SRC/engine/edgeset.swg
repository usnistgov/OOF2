// -*- C++ -*-
// $RCSfile: edgeset.swg,v $
// $Revision: 1.21 $
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

#ifndef EDGESET_SWG
#define EDGESET_SWG

%module edgeset

%include "engine/typemaps.swg"

%pragma(python) include="engine/edgeset.spy"
%extern "femesh.swg"
%extern "edge.swg"

%{
#include "engine/edgeset.h"
typedef std::vector<const EdgeNodeDistance*> vecdist;
%}

/* This typemap applies to the ndlist() C++ function, which returns a
   vector of const pointers to EdgeNodeDistance objects.  The idea is
   to get this vector into a Python list, and then "let go" of it,
   i.e. remove the c++ reference. In order to work cleanly, "ndlist"
   has to be called by a wrapper method, "nodes", defined in
   edgeset.spy.  See additional comments there. */
%typemap(python,out) vecdist * {
  vecdist::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  char _ptemp[128];
  for(std::vector<const EdgeNodeDistance*>::size_type i=0; i<sz ;i++)
    {
      SWIG_MakePtr(_ptemp, (char *)(*$source)[i], "_EdgeNodeDistance_p");
      PyList_SET_ITEM($target, (Py_ssize_t) i, Py_BuildValue("s",_ptemp));
    }
  delete $source;
}

class EdgeSet {
public:
  EdgeSet(FEMesh *);
  ~EdgeSet();
  void addEdge_(BoundaryEdge *); // Should make the nlistcache stale.
  vecdist* ndlist();
  int size();
  // EdgeSetIterator edge_iterator();
};

class EdgeSetIterator {
public:
  EdgeSetIterator(EdgeSet *);
  BoundaryEdge* edge();
  %addmethods{
    void increment() {
      self->operator++();
    }
  }
  bool end();
}

/* "distance" is how far along an edgeset you are, in lab-frame
   distance units, and "fraction" is how far along the edgeset you are
   in units of the edgeset length. */


class EdgeNodeDistance {
public:
  ~EdgeNodeDistance();
  FuncNode *node;
  int index;
  double distance;
  double fraction;
}

%typemap(python,out) vecdist *;

#endif // EDGESET_SWG
