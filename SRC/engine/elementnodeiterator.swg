// -*- C++ -*-
// $RCSfile: elementnodeiterator.swg,v $
// $Revision: 1.17 $
// $Author: langer $
// $Date: 2014/09/27 21:40:45 $

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

%{
#include "engine/elementnodeiterator.h"
%}

%include "engine/typemaps.swg"
%pragma(python) include="engine/elementnodeiterator.spy"

%pragma(python) code="from ooflib.SWIG.engine.node import *"
%extern "engine/node.swg"

class ElementNodeIterator {
public:
   ~ElementNodeIterator();
  bool end();
  Node *node();
  Node *leftnode();
  Node *rightnode();
  void set_start();
  %addmethods {
    void increment() {
      ++*self;
    }
    ElementNodeIterator next() {
      return *self + 1;
    }
    ElementNodeIterator __add__(int i) {
      return *self + i;
    }
  }
};

class ElementShapeFuncIterator : public ElementNodeIterator {
public:
  double shapefunction(MasterPosition&);
  double dshapefunction(int, MasterPosition&);
};

class ElementMapNodeIterator : public ElementShapeFuncIterator {
  %addmethods {
    ElementMapNodeIterator next() {
      return *self + 1;
    }
    ElementMapNodeIterator __add__(int i) {
      return *self + i;
    }
  }
};

class ElementFuncNodeIterator : public ElementShapeFuncIterator {
public:
  FuncNode *funcnode();
  %addmethods {
    ElementFuncNodeIterator next() {
      return *self + 1;
    }
    ElementFuncNodeIterator __add__(int i) {
      return *self + i;
    }
  }
};

class ElementCornerNodeIterator : public ElementNodeIterator {
public:
  ElementFuncNodeIterator funcnode_iterator();
  ElementExteriorNodeIterator exteriornode_iterator();
  %addmethods {
    ElementCornerNodeIterator next() {
      return *self + 1;
    }
    ElementCornerNodeIterator __add__(int i) {
      return *self + i;
    }
  }
};

class ElementExteriorNodeIterator : public ElementFuncNodeIterator {
public:
  %addmethods {
    ElementExteriorNodeIterator next() {
      return *self + 1;
    }
    ElementExteriorNodeIterator __add__(int i) {
      return *self + 1;
    }
  }
};

#endif // ELEMENTNODEITERATOR_SWG
