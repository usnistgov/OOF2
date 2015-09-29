// -*- C++ -*-
// $RCSfile: elementnodeiterator.C,v $
// $Revision: 1.19 $
// $Author: lnz5 $
// $Date: 2015/08/19 19:18:29 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/mastercoord.h"
#include "engine/masterelement.h"
#include "engine/ooferror.h"

ElementNodeIterator::ElementNodeIterator(const Element &el)
  : element_(el),
    index_(0),
    startpt(0),
    start(true)
{}

ElementNodeIterator::ElementNodeIterator(const ElementNodeIterator &that)
  : element_(that.element_),
    index_(that.index_),
    startpt(that.startpt),
    start(that.start)
{}

ElementNodeIterator &ElementNodeIterator::operator=(const ElementNodeIterator
						    &that)
{
  if(&element_ != &that.element_)
    throw ErrProgrammingError("attempt to switch iterators in mid stream",
			      __FILE__, __LINE__);
  index_ = that.index_;
  startpt = that.startpt;
  start = that.start;
  return *this;
}

ElementNodeIterator &ElementNodeIterator::operator+=(int n) {
  start = false;
  index_ = (index_ + n) % element_.nnodes();
  return *this;
}

ElementNodeIterator ElementNodeIterator::operator+(int n) const {
  ElementNodeIterator result(*this);
  result += n;
  return result;
}

bool ElementNodeIterator::end() const {
  return !start && (index_ == startpt);
}

void ElementNodeIterator::set_start() {
  startpt = index_;
  start = true;
}

int ElementNodeIterator::mlistindex() const {
  return index_;
}

const ProtoNode *ElementNodeIterator::protonode() const {
  return element_.masterelement().protonode(mlistindex());
}

bool ElementNodeIterator::interior() const {
  return element_.masterelement().protonode(mlistindex())->nedges() == 0;
}

const MasterCoord &ElementNodeIterator::mastercoord() const {
  return protonode()->mastercoord();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ElementShapeFuncIterator::ElementShapeFuncIterator(const Element &el)
  : ElementNodeIterator(el)
{}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ElementMapNodeIterator::ElementMapNodeIterator(const Element &el)
  : ElementShapeFuncIterator(el)
{}

ElementMapNodeIterator::ElementMapNodeIterator(const
					       ElementMapNodeIterator &that)
  : ElementShapeFuncIterator(that)
{}

ElementMapNodeIterator &
ElementMapNodeIterator::operator=(const ElementMapNodeIterator &that) {
  ElementShapeFuncIterator::operator=(that);
  return *this;
}

int ElementMapNodeIterator::mlistindex() const {
  return element_.masterelement().mapnodes[index_];
}

ElementMapNodeIterator &ElementMapNodeIterator::operator+=(int n) {
  start = false;
  index_ = (index_ + n) % element_.nmapnodes();
  return *this;
}

ElementMapNodeIterator ElementMapNodeIterator::operator+(int n) const {
  ElementMapNodeIterator result(*this);
  result += n;
  return result;
}

double ElementMapNodeIterator::shapefunction(const MasterPosition &pos) const {
  return element_.master.mapfunction->value(index_, pos);
}

double ElementMapNodeIterator::dshapefunction(SpaceIndex i,
					      const MasterPosition &pos) const
{
  return element_.master.mapfunction->realderiv(&element_, index_, i, pos);
}

double ElementMapNodeIterator::masterderiv(SpaceIndex i,
					   const MasterPosition &pos) const
{
  return element_.master.mapfunction->masterderiv(index_, i, pos);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ElementFuncNodeIterator::ElementFuncNodeIterator(const Element &el)
  : ElementShapeFuncIterator(el),
    dofsum(0),
    fncache(index_, NULL)
{}


ElementFuncNodeIterator::ElementFuncNodeIterator(const
						 ElementFuncNodeIterator &that)
  : ElementShapeFuncIterator(that),
    dofsum(that.dofsum),
    fncache(that.fncache)
{}

ElementFuncNodeIterator &
ElementFuncNodeIterator::operator=(const ElementFuncNodeIterator &that) {
  ElementShapeFuncIterator::operator=(that);
  dofsum = that.dofsum;
  fncache = that.fncache;
  return *this;
}

int ElementFuncNodeIterator::mlistindex() const {
  return element_.masterelement().funcnodes[index_];
}

ElementFuncNodeIterator &ElementFuncNodeIterator::operator+=(int n) {
  start = false;

  int nfnodes = element_.nfuncnodes();
  for(int i=0; i<n; i++) {
    // dofsum += node()->ndof();
    dofsum += funcnode()->ndof();
    index_ = (index_ + 1) < nfnodes ? index_ + 1 : 0;
    if(index_ == startpt)	// we've wrapped around
      dofsum = 0;
  }
  return *this;
}

void ElementFuncNodeIterator::set_start() {
  dofsum = 0;
  ElementNodeIterator::set_start();
}

ElementFuncNodeIterator ElementFuncNodeIterator::operator+(int n) const {
  ElementFuncNodeIterator result(*this);
  result += n;
  return result;
}

int ElementFuncNodeIterator::localindex(const Field &field,
					const FieldIndex *component)
  const
{
  return dofsum + field.localindex(funcnode(), *component);
}

bool ElementFuncNodeIterator::hasField(const Field &field) const {
  return funcnode()->hasField(field);
}

bool ElementFuncNodeIterator::hasEquation(const Equation &equation) const {
  return funcnode()->hasEquation(equation);
}

FuncNode *ElementFuncNodeIterator::funcnode() const {
  if (fncache.first != index_ || fncache.second == NULL) {
    // obtain the function node pointer and cache it for reuse
    fncache.first = index_;
    fncache.second = dynamic_cast<FuncNode*>(node());
  }
  return fncache.second;
}

double ElementFuncNodeIterator::shapefunction(const MasterPosition &pos) const {
  return element_.master.shapefunction->value(index_, pos);
}

double ElementFuncNodeIterator::dshapefunction(SpaceIndex i,
					       const MasterPosition &pos) const
{
  return element_.master.shapefunction->realderiv(&element_, index_, i, pos);
}

double ElementFuncNodeIterator::masterderiv(SpaceIndex i,
					    const MasterPosition &mc) const
{
  return element_.master.shapefunction->masterderiv(index_, i, mc);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

InterfaceElementFuncNodeIterator::
InterfaceElementFuncNodeIterator(const Element &el) :
  ElementFuncNodeIterator(el)
{
  side = ((InterfaceElement*)&el)->side();
}

InterfaceElementFuncNodeIterator::
InterfaceElementFuncNodeIterator(const 
				 InterfaceElementFuncNodeIterator &that) :
  ElementFuncNodeIterator(that),side(that.side)
{}
  
FuncNode *InterfaceElementFuncNodeIterator::funcnode() const {
  Node *res;
  if (side==LEFT) {
    res = ((InterfaceElement*)&element_)->get_leftnodelist()[mlistindex()];
  }
  else { // side==RIGHT, obviously...
    res = ((InterfaceElement*)&element_)->get_rightnodelist()[mlistindex()];
  }
  return dynamic_cast<FuncNode*>(res);
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


ElementExteriorNodeIterator::ElementExteriorNodeIterator(const Element &el)
  : ElementFuncNodeIterator(el)
{}

ElementExteriorNodeIterator::ElementExteriorNodeIterator(
				      const ElementExteriorNodeIterator &that)
  :ElementFuncNodeIterator(that)
{}

ElementExteriorNodeIterator&
ElementExteriorNodeIterator::operator=(const ElementExteriorNodeIterator &that) 
{
  ElementFuncNodeIterator::operator=(that);
  return *this;
}

int ElementExteriorNodeIterator::mlistindex() const {
  return element_.masterelement().exteriorfuncnodes[index_];
}

ElementExteriorNodeIterator &ElementExteriorNodeIterator::operator+=(int n) {
  start = false;
  index_ = (index_ + n) % element_.nexteriorfuncnodes();
  return *this;
}

ElementExteriorNodeIterator ElementExteriorNodeIterator::operator+(int n) const
{
  ElementExteriorNodeIterator result(*this);
  result += n;
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ElementCornerNodeIterator::ElementCornerNodeIterator(const Element &el)
  : ElementNodeIterator(el)
{}

ElementCornerNodeIterator::
ElementCornerNodeIterator(const ElementCornerNodeIterator &that)
  : ElementNodeIterator(that)
{}

ElementCornerNodeIterator &
ElementCornerNodeIterator::operator=(const ElementCornerNodeIterator &that) {
  ElementNodeIterator::operator=(that);
  return *this;
}

int ElementCornerNodeIterator::mlistindex() const {
  return element_.masterelement().cornernodes[index_];
}

ElementCornerNodeIterator &ElementCornerNodeIterator::operator+=(int n) {
  start = false;
  index_ = (index_ + n) % element_.ncorners();
  return *this;
}

ElementCornerNodeIterator ElementCornerNodeIterator::operator+(int n) const {
  ElementCornerNodeIterator result(*this);
  result += n;
  return result;
}

ElementFuncNodeIterator ElementCornerNodeIterator::funcnode_iterator() const {
  // create an ElementFuncNodeIterator that starts at the current node
  ElementFuncNodeIterator fni(element_);
  const ProtoNode *pnode = protonode();
  while(fni.protonode() != pnode && !fni.end()) // ugly
    ++fni;
  if(fni.end())
    throw ErrProgrammingError("Unable to convert a cornernode to a funcnode",
			      __FILE__, __LINE__);
  fni.set_start();
  return fni;
}

ElementExteriorNodeIterator ElementCornerNodeIterator::exteriornode_iterator()
  const
{
  ElementExteriorNodeIterator eni(element_);
  const ProtoNode *pnode = protonode();
  while(eni.protonode() != pnode && !eni.end())
    ++eni;
  if(eni.end())
    throw ErrProgrammingError("Unable to convert a cornernode to an exterior node", __FILE__, __LINE__);
  eni.set_start();
  return eni;
}

ElementMapNodeIterator ElementCornerNodeIterator::mapnode_iterator() const {
  ElementMapNodeIterator mni(element_);
  const ProtoNode *pnode = protonode();
  while(mni.protonode() != pnode && !mni.end())
    ++mni;
  if(mni.end())
    throw ErrProgrammingError("Unable to convert a cornernode to a map node",
			      __FILE__, __LINE__);
  mni.set_start();
  return mni;
}

FuncNode *ElementCornerNodeIterator::funcnode() const {
  return dynamic_cast<FuncNode*>(node());
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void ElementNodeIterator::print(std::ostream &os) const {
  os << "ElementNodeIterator(" << index_ << "(" << mlistindex() << "), "
     << *node() << ")";
}

void ElementMapNodeIterator::print(std::ostream &os) const {
  os << "ElementMapNodeIterator(" << index_ << "(" << mlistindex() << "), "
     << *node() << ")";
}

void ElementFuncNodeIterator::print(std::ostream &os) const {
  os << "ElementFuncNodeIterator(" << index_ << "(" << mlistindex() << "), "
     << *node() << ")";
}

void ElementCornerNodeIterator::print(std::ostream &os) const {
  os << "ElementCornerNodeIterator(" << index_ << "(" << mlistindex() << "), "
     << *node() << " " << mastercoord() << ")";
}

std::ostream &operator<<(std::ostream &os, const ElementNodeIterator &eni) {
  eni.print(os);
  return os;
}

