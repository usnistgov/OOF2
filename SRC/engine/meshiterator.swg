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

%module meshiterator

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/element.swg"
%import "engine/node.swg"
#endif // NOSECONDIMPORTS

// %pragma(python) code="from ooflib.SWIG.engine.element import ElementPtr"
// %pragma(python) code="from ooflib.SWIG.engine.node import NodePtr"
// %pragma(python) code="from ooflib.SWIG.engine.node import FuncNodePtr"

%{
#include "engine/meshiterator.h"
%}

// Constructors for these classes aren't swigged because the objects
// should only be created by calling FEMesh::node_iterator, etc.

// TODO PYTHON3: Make these into real Python iterators.  __next__()
// must return the object being pointed to or raise StopIteration, and
// they must have an __iter__ function that returns self.


%nodefaultctor NodeIterator;

class NodeIterator {
public:
  // NodeIterator();		// DON'T SWIG THE CONSTRUCTOR
  ~NodeIterator();
  bool end();
  int size();
  Node *node();
};

%extend NodeIterator {
  void next() {
    ++(*self);
  }
};

%nodefaultctor FuncNodeIterator;

class FuncNodeIterator {
public:
  // FuncNodeIterator();		// DON'T SWIG THE CONSTRUCTOR
  ~FuncNodeIterator();
  bool end();
  int size();
  FuncNode *node();
};

%extend FuncNodeIterator {
  void next() {
    ++(*self);
  }
};

%nodefaultctor ElementIterator;

class ElementIterator {
public:
  // ElementIterator(); 		// DON'T SWIG THE CONSTRUCTOR
  ~ElementIterator();
  bool end();
  int size();
  int count();
  Element *element();
};

%extend ElementIterator {
  void next() {
    ++(*self);
  }
};

#endif // MESHITERATOR_SWG
