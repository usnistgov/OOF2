// -*- C++ -*-
// $RCSfile: masterelement.swg,v $
// $Revision: 1.41 $
// $Author: langer $
// $Date: 2014/09/27 21:40:47 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MASTERELEMENT_SWG
#define MASTERELEMENT_SWG

%include "engine/typemaps.swg"

%pragma(python) include="engine/masterelement.spy"
%extern "engine/element.swg"
%extern "engine/mastercoord.swg"

%{
#include "engine/masterelement.h"
#include "engine/element.h"
#include "common/tostring.h"
typedef std::vector<MasterElement*> MasterElementList;
// typedef std::vector<ContourCellSkeleton*> ContourCellVec;
%}

class ProtoNode {
public:
  int index();
  bool mapping();
  bool func();
  bool corner();
  int nedges();
  int getedge(int i);
  const MasterCoord &mastercoord();
}; 

%typemap(python,out) MasterElementList* {
  MasterElementList::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  char _ptemp[128];
  for(std::vector<MasterElement*>::size_type i=0; i<sz; i++) {
    SWIG_MakePtr(_ptemp, (char *)(*$source)[i], "_MasterElement_p");
    PyList_SET_ITEM($target, (Py_ssize_t) i, Py_BuildValue("s",_ptemp));
  }
}

%typemap(python,newfree) MasterElementList* {
  delete $source;
}

// %typemap(python,out) ContourCellVec* {
//   MasterElementList::size_type sz = $source->size();
//   assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
//   $target = PyList_New((Py_ssize_t) sz);
//   char _ptemp[128];
//   for(std::vector<ContourCellSkeleton*>::size_type i=0; i<sz; i++) {
//     SWIG_MakePtr(_ptemp, (char *)(*$source)[i], "_ContourCellSkeleton_p");
//     PyList_SET_ITEM($target, (Py_ssize_t) i, Py_BuildValue("s",_ptemp));
//   }
// }

// %typemap(python,newfree) ContourCellVec {
//   delete $source;
// }

// In this case, this should *not* be "%new", C++ retains ownership
// of the list, which is static inside the function.
MasterElementList* masterElementList();

class MasterElement {
public:
  int id();
  int nnodes();
  int nmapnodes();
  int nfuncnodes();
  int ninteriorfuncnodes();
  int ninteriormapnodes_only();
  int nexteriormapnodes_only();
  int nsides();
  const string &name();
  const string &description();
  int ncorners();
  double outOfBounds(const MasterCoord&);
#ifndef DIM_3
  // %new ContourCellVec* contourcells(int n);
  bool onBoundary(const MasterCoord&);
  bool onBoundary2(const MasterCoord&, const MasterCoord&);

  InterfaceElement *buildInterfaceElement(PyObject*, PyObject*,
					  int,
					  Material*,
					  NodeVec*, NodeVec*,
					  bool,bool,
					  StringVec*);
#endif
  
  int map_order();
  int fun_order();

  Element *build(PyObject*, Material*, NodeVec*);
  
  %addmethods {
    const ProtoNode *get_protonode(int n) {
      return self->protonode(n);
    }
    %new const string *__repr__() {
      return new std::string(to_string(*self));
    }
  }

  // Superconvergent patch recovery
  int nSCpoints();
  MasterCoord getSCpoint(int);

};

int integration_reduction;

%typemap(python,out) MasterElementList*;
%typemap(python,newfree) MasterElementList*;
// %typemap(python,out) ContourCellVec*;
// %typemap(python,newfree) ContourCellVec*;

#endif // MASTERELEMENT_SWG
