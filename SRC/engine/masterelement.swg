// -*- C++ -*-

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

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/element.swg"
%import "engine/mastercoord.swg"
%import "engine/material.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/masterelement.h"
#include "engine/element.h"
#include "engine/node.h"
#include "common/tostring.h"
%}

%nodefaultctor ProtoNode;

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

// Create the MasterElementVec typemap and typedef.
MAKE_LISTVEC_TYPEMAPS(MasterElement);
// Create the NodeVec typemap and typedef.
MAKE_LISTVEC_TYPEMAPS(Node);

// Do *not* use %newobject here. C++ retains ownership of the list,
// which is static inside the function.
MasterElementVec* masterElementList();

%nodefaultctor MasterElement;

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
  bool onBoundary(const MasterCoord&);
  bool onBoundary2(const MasterCoord&, const MasterCoord&);

  InterfaceElement *buildInterfaceElement(PyObject*, PyObject*,
					  int,
					  Material*,
					  NodeVec*, NodeVec*,
					  bool,bool,
					  StringVec*);
  int map_order();
  int fun_order();

  Element *build(PyObject*, Material*, NodeVec*);
  
  // Superconvergent patch recovery
  int nSCpoints();
  MasterCoord getSCpoint(int);
};

%extend MasterElement {
  const ProtoNode *get_protonode(int n) {
    return self->protonode(n);
  }
}

ADD_REPR_GENERIC(MasterElement);

int integration_reduction;

%typemap(python,out) MasterElementList*;
%typemap(python,newfree) MasterElementList*;

%pythoncode "engine/masterelement.spy"

#endif // MASTERELEMENT_SWG
