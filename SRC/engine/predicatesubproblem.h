// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include <iostream>

#include "common/cleverptr.h"

#ifndef PREDICATESUBPROBLEM_H
#define PREDICATESUBPROBLEM_H

template <class PRDCT> class PredicateSubProblem;
template <class PRDCT> class PredicateSubProblemElementIterator; // OLD
template <class PRDCT> class PSPNodeIteratorOLD;
template <class PRDCT> class PSPNodeIterator;
template <class PRDCT> class PSPFuncNodeIteratorOLD;
template <class PRDCT> class PSPFuncNodeIterator;
template <class PRDCT> class PSPNodeContainer;
template <class PRDCT> class PSPFuncNodeContainer;


#include "engine/csubproblem.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/meshiterator.h"
#include <iostream>
#include <set>

// NodeCompare is used as the Comparison operator for std::sets of
// Node*s and FuncNode*s.  It's not strictly necessary, but if it's
// not used, then the sets are ordered by the values of the Node*
// pointers, which may not be reproducible from run to run, which
// might hinder debugging.  Using NodeCompare guarantees that
// iterators over the sets of Nodes will return the same Node ordering
// each time.

struct NodeCompare {
  bool operator()(const Node* n1, const Node* n2) const {
    return n1->index() < n2->index();
  }
};

typedef std::set<Node*, NodeCompare> NodeSet;
typedef std::set<FuncNode*, NodeCompare> FuncNodeSet;

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Template for SubProblems that are defined in terms of a predicate
// that chooses mesh elements.  The template parameter PRDCT is a
// callable object that takes two arguments, a const FEMesh* and a
// const Element*, and returns true if the Element is included in the
// subproblem.

template <class PRDCT>
class PredicateSubProblem : public CSubProblem {
protected:
  PRDCT predicate; // Not a reference!. PredicateSubProblem has own copy.
private:
  mutable NodeSet *nodes_;
  mutable FuncNodeSet *funcnodes_;
  NodeSet &nodes() const;
  FuncNodeSet &funcnodes() const;
public:
  PredicateSubProblem(const PRDCT &p)
    : predicate(p),
      nodes_(0),
      funcnodes_(0)
  {}
  virtual ~PredicateSubProblem();
  virtual void redefined();
  virtual ElementIterator element_iterator() const;
#ifdef OLDITERATORS
  virtual NodeIterator node_iterator_OLD() const;
  virtual FuncNodeIterator funcnode_iterator_OLD() const;
#endif // OLDITERATORS
  // node_iterator and funcnode_iterator need to return pointers to
  // base class MeshNodeContainer objects, because virtual methods in
  // the containers are needed to return different types of iterators.
  // So the containers need to be wrapped by ContainerP the same way
  // that the iterators are wrapped by IterP.
  virtual VContainer<Node>* c_node_iterator() const;
  virtual VContainer<FuncNode>* c_funcnode_iterator() const;
  friend class PSPNodeContainer<PRDCT>;
  friend class PSPFuncNodeContainer<PRDCT>;

  int nnodes() const { return nodes().size(); }
  int nfuncnodes() const { return funcnodes().size(); }
  
  virtual bool contains(const Element*) const;
  virtual bool containsNode(const Node*) const;

  friend class PredicateSubProblemElementIterator<PRDCT>;

#ifdef OLDITERATORS
  friend class PSPNodeIteratorOLD<PRDCT>;
  friend class PSPFuncNodeIteratorOLD<PRDCT>;
#endif // OLDITERATORS
};

template <class PRDCT>
PredicateSubProblem<PRDCT>::~PredicateSubProblem() {
  if(nodes_) delete nodes_;
  if(funcnodes_) delete funcnodes_;
}

template <class PRDCT>
bool PredicateSubProblem<PRDCT>::contains(const Element *element) const {
  return predicate(mesh, element); // mesh is defined in CSubProblem
}

template <class PRDCT>
bool PredicateSubProblem<PRDCT>::containsNode(const Node *node) const {
  Node *nd = const_cast<Node*>(node);
  NodeSet &nds = nodes();
  NodeSet::iterator i=nds.find(nd);
  return i != nds.end();
}

template <class PRDCT>
void PredicateSubProblem<PRDCT>::redefined() {
  if(nodes_) delete nodes_;
  if(funcnodes_) delete funcnodes_;
  nodes_ = 0;
  funcnodes_ = 0;
}

template <class PRDCT>
NodeSet &PredicateSubProblem<PRDCT>::nodes() const {
  if(nodes_ == 0) {
    nodes_ = new NodeSet;
    for(ElementIterator
	  ei(const_cast<PredicateSubProblem<PRDCT>*>(this)->element_iterator());
	!ei.end(); ++ei)
      {
	for(ElementNodeIterator n(ei.element()->node_iterator()); !n.end(); ++n)
	  {
	    nodes_->insert(n.node());
	  }
      }
  }
  return *nodes_;
}

template <class PRDCT>
FuncNodeSet &PredicateSubProblem<PRDCT>::funcnodes() const {
  if(funcnodes_ == 0) {
    funcnodes_ = new FuncNodeSet;
    for(ElementIterator
	  ei(const_cast<PredicateSubProblem<PRDCT>*>(this)->element_iterator());
	!ei.end(); ++ei)
      {
	for(CleverPtr<ElementFuncNodeIterator> n(ei.element()->
						 funcnode_iterator()); 
	    !n->end(); ++*n)
	  {
	    funcnodes_->insert(n->funcnode());
	  }
      }
  }
  return *funcnodes_;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

template <class PRDCT>
class PredicateSubProblemElementIterator : public ElementIteratorBase {
private:
  const PredicateSubProblem<PRDCT> *subproblem;
  MeshElementIterator iter;
  int count_;
  mutable int size_;
  mutable bool size_computed_;
  bool ok(const FEMesh *mesh, const Element *elem) const {
    return subproblem->predicate(mesh, elem);
  }
public:
  PredicateSubProblemElementIterator(const PredicateSubProblem<PRDCT> *subp);
  PredicateSubProblemElementIterator(
			    const PredicateSubProblemElementIterator<PRDCT>&);
  virtual void operator++();
  virtual bool end() const { return iter.end(); }
  virtual int size() const;
  virtual int count() const { return count_; }
  virtual Element *element() const { return iter.element(); }
  virtual ElementIteratorBase *clone() const {
    return new PredicateSubProblemElementIterator<PRDCT>(*this);
  }
};

template <class PRDCT>
PredicateSubProblemElementIterator<PRDCT>::PredicateSubProblemElementIterator(
			       const PredicateSubProblem<PRDCT> *subp)
  : subproblem(subp),
    iter(subp->mesh),
    count_(0),
    size_(0),
    size_computed_(false)
{
  while(!iter.end() && !ok(subproblem->mesh, iter.element()))
    ++iter;
  if(!iter.end())
    count_++;
}

template <class PRDCT>
PredicateSubProblemElementIterator<PRDCT>::PredicateSubProblemElementIterator(
		      const PredicateSubProblemElementIterator<PRDCT> &other)
  : subproblem(other.subproblem),
    iter(*dynamic_cast<MeshElementIterator*>(other.iter.clone())),
    count_(other.count_),
    size_(other.size_),
    size_computed_(other.size_computed_)
{}

template <class PRDCT>
void PredicateSubProblemElementIterator<PRDCT>::operator++() {
  ++iter;
  while(!iter.end() && !ok(subproblem->mesh, iter.element()))
    ++iter;
  if(!iter.end())
    count_++;
}

template <class PRDCT>
int PredicateSubProblemElementIterator<PRDCT>::size() const {
  if(!size_computed_) {
    size_computed_ = true;
    size_ = 0;
    for(ElementIterator i(subproblem->mesh->element_iterator()); !i.end(); ++i){
      if(ok(subproblem->mesh, i.element()))
	 size_++;
    }
  }
  return size_;
}

template <class PRDCT>
ElementIterator PredicateSubProblem<PRDCT>::element_iterator() const {
  return ElementIterator(new PredicateSubProblemElementIterator<PRDCT>(this));
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Node and FuncNode iterators, returned by c_begin and c_end in
// PSPNodeContainer.

template <class PRDCT, class NODE>
class PSPNodeIter : public MeshIterator<NODE> {
protected:
  const PredicateSubProblem<PRDCT>* const subp;
  typename std::set<NODE*, NodeCompare>::iterator iter;
public:
  PSPNodeIter(const PredicateSubProblem<PRDCT> *const subp,
	      typename std::set<NODE*, NodeCompare>::iterator iter)
    : subp(subp),
      iter(iter)
  {}
  virtual bool operator!=(const MeshIterator<NODE> &o) const {
    const PSPNodeIter<PRDCT, NODE>& other =
      dynamic_cast<const PSPNodeIter<PRDCT, NODE>&>(o);
    return other.iter != iter;
  }
  virtual MeshIterator<NODE>& operator++() { ++iter; return *this; }
  virtual NODE* operator*() const { return *iter; }

  virtual MeshIterator<NODE>* clone() const {
    return new PSPNodeIter<PRDCT, NODE>(*this);
  }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Containers -- objects that can be iterated over.

template <class PRDCT>
class PSPNodeContainer : public VContainer<Node> {
protected:
  const PredicateSubProblem<PRDCT>* const subp;
public:
  PSPNodeContainer(const PredicateSubProblem<PRDCT>* const subp)
    : VContainer<Node>(subp->nnodes()),
      subp(subp)
  {}
  virtual MeshIterator<Node>* c_begin() const {
    return new PSPNodeIter<PRDCT, Node>(this->subp,
					this->subp->nodes().begin());
  }
  virtual MeshIterator<Node>* c_end() const {
    return new PSPNodeIter<PRDCT, Node>(this->subp,
					this->subp->nodes().end());
  }
};

template <class PRDCT>
class PSPFuncNodeContainer : public VContainer<FuncNode> {
protected:
  const PredicateSubProblem<PRDCT>* const subp;
public:
  PSPFuncNodeContainer(const PredicateSubProblem<PRDCT>* const subp)
    : VContainer<FuncNode>(subp->nfuncnodes()),
      subp(subp)
  {}
  virtual MeshIterator<FuncNode>* c_begin() const {
    return new PSPNodeIter<PRDCT, FuncNode>(this->subp,
					    this->subp->funcnodes().begin());
  }
  virtual MeshIterator<FuncNode>* c_end() const {
    return new PSPNodeIter<PRDCT, FuncNode>(this->subp,
					    this->subp->funcnodes().end());
  }
};

//// Subproblem methods that return the containers

template <class PRDCT>
VContainer<Node>* PredicateSubProblem<PRDCT>::c_node_iterator() const
{
  return new PSPNodeContainer<PRDCT>(this);
}
  
template <class PRDCT>
VContainer<FuncNode>* PredicateSubProblem<PRDCT>::c_funcnode_iterator() const
{
  return new PSPFuncNodeContainer<PRDCT>(this);
}

#endif // PREDICATESUBPROBLEM_H
