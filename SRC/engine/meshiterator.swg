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
%}

// Constructors for these classes aren't swigged because the objects
// should only be created by calling FEMesh::node_iterator, etc.

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

// OLD BELOW HERE

// The .spy file adds __iter__ and __next__ methods to make these into
// real iterators.

// TODO PYTHON3: Find code that can be simplified because these
// classes are real iterators.

%nodefaultctor NodeIterator;

class NodeIterator {
public:
  ~NodeIterator();
  bool end();
  int size();
  Node *node();
};

%extend NodeIterator {
  void increment() {
    ++(*self);
  }
};

%nodefaultctor FuncNodeIterator;

class FuncNodeIterator {
public:
  ~FuncNodeIterator();
  bool end();
  int size();
  FuncNode *node();
};

%extend FuncNodeIterator {
  void increment() {
    ++(*self);
  }
};

%nodefaultctor ElementIterator;

class ElementIterator {
public:
  ~ElementIterator();
  bool end();
  int size();
  int count();
  Element *element();
};

%extend ElementIterator {
  void increment() {
    ++(*self);
  }
};

%pythoncode "engine/meshiterator.spy"

#endif // MESHITERATOR_SWG
