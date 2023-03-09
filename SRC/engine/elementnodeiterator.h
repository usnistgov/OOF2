// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef ELEMENTNODEITERATOR_H
#define ELEMENTNODEITERATOR_H

#include "engine/element.h"
#include "engine/indextypes.h"
#include "node.h"

#include <utility>

class Equation;
class Field;
class GaussPoint;
class MasterCoord;
class MasterPosition;
class FEMesh;
class Position;
class ProtoNode;

// The ElementNodeIterator is used for looping over all Nodes of an
// Element, and is the base class for the specialized iterators, which
// loop over subsets of the Nodes.

// TODO PYTHON3: Make these into real C++ and python iterators?  A
// more natural syntax would be
//
//  for(Node *node : element->nodes()) ...
//  for(FuncNode *node : element->funcnodes()) ...
//  for(ElementNodeIterator i=el->nodes().begin(); i!=el.nodes().end(); ++i) ...
//
// A difficulty with doing this is that the iterators, as currently
// written, wrap around the list of nodes, which would not be
// impossible to implement with STL type iterators, but would be
// somewhat messy.  It looks like this is needed in
// Element::newBndyEdge().

class ElementNodeIterator {	// for looping over all nodes
protected:
  const Element &element_;
  ShapeFunctionIndex index_;	// where we are now
  int startpt;			// where we started from
  bool start;			// are we just starting?

public:
  ElementNodeIterator(const Element &el);
  ElementNodeIterator(const ElementNodeIterator&);
  virtual ~ElementNodeIterator() {}
  ElementNodeIterator &operator=(const ElementNodeIterator&);

  // Go to the node n farther along in the sequence
  virtual ElementNodeIterator &operator+=(int);	// returns *this
  // These two incrementation operators are implemented in terms of operator+=
  ElementNodeIterator &operator++() { return operator+=(1); } // returns *this
  ElementNodeIterator operator+(int) const; // returns new object (not *this)

  virtual bool end() const;	// are we done iterating?
  virtual void set_start();	// pretend we started at the current point

  // various representations of the current point
  const ProtoNode *protonode() const;
  // node() is inline because the Mac profiler suggested it... it helps a bit.
  inline Node *node() const { return element_.nodelist[mlistindex()]; }
  const MasterCoord &mastercoord() const;

  bool interior() const;	// are we at an interior node?

  const Element &element() const { return element_; } // over whom we're looping

  // mlistindex() establishes the correspondence between index of a
  // node in the iterator and the index in the element's and
  // masterelement's nodelists.  By using this virtual function, most
  // of the other functions in the ElementNodeIterator hierarchy need
  // only be defined in the base class.  It returns the index in the
  // master element corresponding to the current index_ in the
  // iterator.
  virtual int mlistindex() const;

  //Cheap way to get the nodes that are 'partnered' with the main
  //interface element nodes Can only be used if the Element really is an
  //InterfaceElement, otherwise, a more sophisticated typecasting mechanism is
  //required.  TODO: Provide a more sophisticated typecasting
  //mechanism.
  inline Node *leftnode() const { 
    return ((InterfaceElement*)&element_)->get_leftnodelist()[mlistindex()]; }
  inline Node *rightnode() const { 
    return ((InterfaceElement*)&element_)->get_rightnodelist()[mlistindex()]; }

  // miscellany
  ShapeFunctionIndex index() const { return index_; }
  virtual void print(std::ostream&) const;
};


// Abstract base class for Iterators which can be used to evaluate
// shape functions.

class ElementShapeFuncIterator : public ElementNodeIterator {
public:
  ElementShapeFuncIterator(const Element &el);
  virtual int mlistindex() const = 0;
  virtual ElementShapeFuncIterator &operator+=(int) = 0;
  // shapefunctions corresponding to this node
  virtual double shapefunction(const MasterPosition&) const = 0;
  // shapefunction derivatives wrt real space coordinates
  virtual double dshapefunction(SpaceIndex, const MasterPosition&) const = 0;
  // shapefunction derivatives wrt master space coordinates
  virtual double masterderiv(SpaceIndex, const MasterPosition&) const = 0;
  virtual void print(std::ostream&) const = 0;
};



class ElementMapNodeIterator : public ElementShapeFuncIterator {
public:
  ElementMapNodeIterator(const Element &el);
  ElementMapNodeIterator(const ElementMapNodeIterator&);
  virtual ~ElementMapNodeIterator() {}
  ElementMapNodeIterator &operator=(const ElementMapNodeIterator&);
  virtual ElementMapNodeIterator &operator+=(int);
  ElementMapNodeIterator operator+(int) const;
  virtual int mlistindex() const;
  // shapefunctions corresponding to this node
  virtual double shapefunction(const MasterPosition&) const;
  // shapefunction derivatives wrt real space coordinates
  virtual double dshapefunction(SpaceIndex, const MasterPosition&) const;
  // shapefunction derivatives wrt master space coordinates
  virtual double masterderiv(SpaceIndex, const MasterPosition&) const;
  virtual void print(std::ostream&) const;
};


class ElementFuncNodeIterator : public ElementShapeFuncIterator {
protected:
  int dofsum;			// no. of dofs seen so far
  // The funcnode() member function are called twice within
  // Element::ndof() for each function node of an element. it includes
  // many pointer dereference operations which causes high cache
  // misses rate. As a result, each time when funcnode() is called, we
  // cache the result for reuse.
  // Cache format: index and pointer pair of a function node 
  mutable std::pair<int, FuncNode*> fncache;
public:
  ElementFuncNodeIterator(const Element &el);
  ElementFuncNodeIterator(const ElementFuncNodeIterator&);
  virtual ~ElementFuncNodeIterator() {}
  ElementFuncNodeIterator &operator=(const ElementFuncNodeIterator&);
  virtual ElementFuncNodeIterator &operator+=(int);
  ElementFuncNodeIterator operator+(int) const;
  virtual int mlistindex() const;
  virtual void set_start();
  virtual FuncNode *funcnode() const;
  bool hasField(const Field&) const;
  bool hasEquation(const Equation&) const;
  int localindex(const Field&, const FieldIndex*) const;
  // shapefunctions corresponding to this node
  virtual double shapefunction(const MasterPosition&) const;
  // shapefunction derivatives wrt real space coordinates
  virtual double dshapefunction(SpaceIndex, const MasterPosition&) const;
  // shapefunction derivatives wrt master space coordinates
  virtual double masterderiv(SpaceIndex, const MasterPosition&) const;
  virtual void print(std::ostream&) const;


};

class InterfaceElementFuncNodeIterator : public ElementFuncNodeIterator {
private:
  Sidedness side;
public:
  InterfaceElementFuncNodeIterator(const Element &el);
  InterfaceElementFuncNodeIterator(const InterfaceElementFuncNodeIterator&);
  virtual FuncNode *funcnode() const;

};

// ElementExteriorNodeIterator should really be called
// "ElementExteriorFuncNodeIterator", but the name is too long to
// type.
class ElementExteriorNodeIterator : public ElementFuncNodeIterator {
public:
  ElementExteriorNodeIterator(const Element &el);
  ElementExteriorNodeIterator(const ElementExteriorNodeIterator&);
  virtual ~ElementExteriorNodeIterator() {}
  ElementExteriorNodeIterator& operator=(const ElementExteriorNodeIterator&);
  ElementExteriorNodeIterator operator+(int) const;
  virtual ElementExteriorNodeIterator &operator+=(int);
  virtual int mlistindex() const;
};


class ElementCornerNodeIterator : public ElementNodeIterator {
public:
  ElementCornerNodeIterator(const Element &el);
  ElementCornerNodeIterator(const ElementCornerNodeIterator&);
  virtual ~ElementCornerNodeIterator() {}
  ElementCornerNodeIterator &operator=(const ElementCornerNodeIterator&);
  virtual ElementCornerNodeIterator &operator+=(int);
  virtual int mlistindex() const;
  FuncNode *funcnode() const;
  ElementCornerNodeIterator operator+(int) const;
  ElementFuncNodeIterator funcnode_iterator() const;
  ElementMapNodeIterator mapnode_iterator() const;
  ElementExteriorNodeIterator exteriornode_iterator() const;
  virtual void print(std::ostream&) const;
};

std::ostream &operator<<(std::ostream&, const ElementNodeIterator&);

#endif
