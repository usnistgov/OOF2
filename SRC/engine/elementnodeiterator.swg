// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ELEMENTNODEITERATOR_SWG
#define ELEMENTNODEITERATOR_SWG

%module elementnodeiterator

%{
#include "engine/elementnodeiterator.h"
%}

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "engine/node.swg"
#endif // NOSECONDIMPORTS

// %pragma(python) code="from ooflib.SWIG.engine.node import *"

%nodefaultctor ElementNodeIterator;
%feature("valuewrapper") ElementNodeIterator;
%feature("valuewrapper") ElementMapNodeIterator;
%feature("valuewrapper") ElementFuncNodeIterator;
%feature("valuewrapper") ElementCornerNodeIterator;
%feature("valuewrapper") ElementExteriorNodeIterator;

class ElementNodeIterator {
public:
   ~ElementNodeIterator();
  bool end();
  Node *node();
  Node *leftnode();
  Node *rightnode();
  void set_start();
};

%extend ElementNodeIterator {
  void increment() {
    ++*self;
  }
  ElementNodeIterator next() {
    return *self + 1;
  }
  ElementNodeIterator __add__(int i) {
    return *self + i;
  }
};

%nodefaultctor ElementShapeFuncIterator;

class ElementShapeFuncIterator : public ElementNodeIterator {
public:
  double shapefunction(MasterPosition&);
  double dshapefunction(int, MasterPosition&);
};

%nodefaultctor ElementMapNodeIterator;

class ElementMapNodeIterator : public ElementShapeFuncIterator {};

%extend ElementMapNodeIterator {
  ElementMapNodeIterator next() {
    return *self + 1;
  }
  ElementMapNodeIterator __add__(int i) {
    return *self + i;
  }
};

%nodefaultctor ElementFuncNodeIterator;

class ElementFuncNodeIterator : public ElementShapeFuncIterator {
public:
  FuncNode *funcnode();
};

%extend ElementFuncNodeIterator {
  ElementFuncNodeIterator next() {
    return *self + 1;
  }
  ElementFuncNodeIterator __add__(int i) {
    return *self + i;
  }
};

%nodefaultctor ElementCornerNodeIterator;

class ElementCornerNodeIterator : public ElementNodeIterator {
public:
  ElementFuncNodeIterator funcnode_iterator();
  ElementExteriorNodeIterator exteriornode_iterator();
};

%extend ElementCornerNodeIterator {
  ElementCornerNodeIterator next() {
    return *self + 1;
  }
  ElementCornerNodeIterator __add__(int i) {
    return *self + i;
  }
};

%nodefaultctor ElementExteriorNodeIterator;

class ElementExteriorNodeIterator : public ElementFuncNodeIterator {};

%extend ElementExteriorNodeIterator {
  ElementExteriorNodeIterator next() {
    return *self + 1;
  }
  ElementExteriorNodeIterator __add__(int i) {
    return *self + 1;
  }
};

%pythoncode "engine/elementnodeiterator.spy"

#endif // ELEMENTNODEITERATOR_SWG
