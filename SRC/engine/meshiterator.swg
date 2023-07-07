// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MESHITERATOR_SWG
#define MESHITERATOR_SWG

%module(package="ooflib.SWIG.engine") meshiterator

%include "common/typemaps.swg"
%import "engine/element.swg"
%import "engine/node.swg"

%{
#include "engine/element.h"
#include "engine/meshiterator.h"
#include "engine/node.h"
#include "engine/flux.h"	// SWIGBUG

typedef VContainer<Node> VContainerNode;
typedef VContainer<FuncNode> VContainerFuncNode;
typedef VContainer<Element> VContainerElement;
typedef VContainer<InterfaceElement> VContainerInterfaceElement;

typedef std::vector<FuncNode*> FuncNodeVector;
typedef std::vector<FuncNode*>::iterator FuncNodeIterator;
%}

// Constructors for these classes aren't swigged because the objects
// should only be created by calling FEMesh::nodes(), etc.

%nodefaultctor MeshNodeIter;
class MeshNodeIter {
public:
  bool operator!=(const MeshNodeIter&);
};

%extend MeshNodeIter {
  void increment() { ++(*$self); }
  Node* node() { return $self->operator*(); }
};

%nodefaultctor MeshFuncNodeIter;
class MeshFuncNodeIter {
public:
  bool operator!=(const MeshFuncNodeIter&);
};

%extend MeshFuncNodeIter {
  void increment() { ++(*self); }
  FuncNode* node() { return $self->operator*(); }
};

%nodefaultctor MeshElementIter;
class MeshElementIter {
public:
  bool operator!=(const MeshElementIter&);
};

%extend MeshElementIter {
  void increment() { ++(*self); }
  Element *element() { return $self->operator*(); }
};

%nodefaultctor MeshInterfaceElementIter;
class MeshInterfaceElementIter {
public:
  bool operator!=(const MeshInterfaceElementIter&);
};

%extend MeshInterfaceElementIter {
  void increment() { ++(*self); }
  Element *element() { return $self->operator*(); } 
};

// In principle, swig can understand the VContainer template, but I
// couldn't get it to work, so the subtypes are typedefed above and
// swigged individually.

// TODO PYTHON3? There's a lot of repetition here. Can we swig a base
// class?  Currently VContainer<A> and VContainer<B> don't share a
// base class.

%nodefaultctor VContainerNode;
%feature("valuewrapper") VContainerNode;
class VContainerNode {
public:
  int size();
  %newobject c_begin;
  %newobject c_end;
  MeshNodeIter* c_begin();
  MeshNodeIter* c_end();
};

%nodefaultctor VContainerFuncNode;
%feature("valuewrapper") VContainerFuncNode;
class VContainerFuncNode {
public:
  int size();
  %newobject c_begin;
  %newobject c_end;
  MeshFuncNodeIter* c_begin();
  MeshFuncNodeIter* c_end();
};

%nodefaultctor VContainerElement;
%feature("valuewrapper") VContainerElement;
class VContainerElement {
public:
  int size();
  %newobject c_begin;
  %newobject c_end;
  MeshElementIter* c_begin();
  MeshElementIter* c_end();
};

%nodefaultctor VContainerInterfaceElement;
%feature("valuewrapper") VContainerInterfaceElement;
class VContainerInterfaceElement {
public:
  int size();
  %newobject c_begin;
  %newobject c_end;
  MeshElementIter* c_begin();
  MeshElementIter* c_end();
};

%pythoncode "engine/meshiterator.spy"

#endif // MESHITERATOR_SWG
