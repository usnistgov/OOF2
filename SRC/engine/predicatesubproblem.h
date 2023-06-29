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
template <class PRDCT> class PSPNodeIterator;
template <class PRDCT> class PSPFuncNodeIterator;
template <class PRDCT> class PSPNodeContainer;
template <class PRDCT> class PSPFuncNodeContainer;
template <class PRDCT> class PSPElementContainer;
template <class PRDCT> class PSPInterfaceElementContainer;

template <class PRDCT> class PredicateSubProblemElementIteratorOLD;


#include "engine/csubproblem.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/meshiterator.h"
#include <iostream>
#include <set>

// IndexLT is used as the Comparison operator for std::sets of
// pointers to Nodes, FuncNodes, and Elements.  It's not strictly
// necessary, but if it's not used, then the sets are ordered by the
// values of the *pointers* , which may not be reproducible from run
// to run, which might hinder testing and debugging.  Using IndexLT
// guarantees that iterators over the sets will return the same
// ordering each time.

template<class OBJ>
struct IndexLT {
  bool operator()(const OBJ* n1, const OBJ* n2) const {
    return n1->index() < n2->index();
  }
};

typedef std::set<Node*, IndexLT<Node>> NodeSet;
typedef std::set<FuncNode*, IndexLT<FuncNode>> FuncNodeSet;
typedef std::set<Element*, IndexLT<Element>> ElementSet;
typedef std::set<InterfaceElement*, IndexLT<InterfaceElement>> EdgementSet;

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
  mutable ElementSet *elements_;
  mutable EdgementSet *edgements_;
  NodeSet &nodes() const;
  FuncNodeSet &funcnodes() const;
  ElementSet &elements() const;
  EdgementSet &edgements() const;
public:
  PredicateSubProblem(const PRDCT &p)
    : predicate(p),
      nodes_(nullptr),
      funcnodes_(nullptr),
      elements_(nullptr),
      edgements_(nullptr)
  {}
  virtual ~PredicateSubProblem();
  virtual void redefined();
  virtual ElementIteratorOLD element_iterator_OLD() const;
  // node_iterator and funcnode_iterator need to return pointers to
  // base class MeshNodeContainer objects, because virtual methods in
  // the containers are needed to return different types of iterators.
  // So the containers need to be wrapped by ContainerP the same way
  // that the iterators are wrapped by IterP.
  virtual VContainer<Node>* c_node_iterator() const;
  virtual VContainer<FuncNode>* c_funcnode_iterator() const;
  virtual VContainer<Element>* c_element_iterator() const;
  virtual VContainer<InterfaceElement>* c_interface_element_iterator() const;
  friend class PSPNodeContainer<PRDCT>;
  friend class PSPFuncNodeContainer<PRDCT>;
  friend class PSPElementContainer<PRDCT>;
  friend class PSPInterfaceElementContainer<PRDCT>;

  int nnodes() const { return nodes().size(); }
  int nfuncnodes() const { return funcnodes().size(); }
  int nelements() const { return elements().size(); }
  int nedgements() const { return edgements().size(); }
  
  virtual bool contains(const Element*) const;
  virtual bool containsNode(const Node*) const;

  friend class PredicateSubProblemElementIteratorOLD<PRDCT>;
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
  nodes_ = nullptr;
  funcnodes_ = nullptr;
  elements_ = nullptr;
}

template <class PRDCT>
NodeSet &PredicateSubProblem<PRDCT>::nodes() const {
  if(nodes_ == nullptr) {
    nodes_ = new NodeSet;
    for(Element *element : element_iterator()) {
      for(ElementNodeIterator n(element->node_iterator()); !n.end(); ++n) {
	nodes_->insert(n.node());
      }
    }
  }
  return *nodes_;
}

template <class PRDCT>
FuncNodeSet &PredicateSubProblem<PRDCT>::funcnodes() const {
  if(funcnodes_ == nullptr) {
    funcnodes_ = new FuncNodeSet;
    for(Element *element : element_iterator()) {
      for(CleverPtr<ElementFuncNodeIterator> n(element->funcnode_iterator());
	  !n->end(); ++*n)
	{
	  funcnodes_->insert(n->funcnode());
	}
    }
  }
  return *funcnodes_;
}

template <class PRDCT>
ElementSet &PredicateSubProblem<PRDCT>::elements() const {
  if(elements_ == nullptr) {
    elements_ = new ElementSet;
    for(Element *element : mesh->element_iterator()) {
      if(this->predicate(mesh, element))
	elements_->insert(element);
    }
  }
  return *elements_;
}

template <class PRDCT>
EdgementSet &PredicateSubProblem<PRDCT>::edgements() const {
  if(edgements_ == nullptr) {
    edgements_ = new EdgementSet;
    for(InterfaceElement *edgement : mesh->interface_element_iterator()) {
      if(edgement->isSubProblemInterfaceElement(this))
	edgements_->insert(edgement);
    }
  }
  return *edgements_;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

template <class PRDCT>
class PredicateSubProblemElementIteratorOLD : public ElementIteratorBase {
private:
  const PredicateSubProblem<PRDCT> *subproblem;
  MeshElementIteratorOLD iter;
  int count_;
  mutable int size_;
  mutable bool size_computed_;
  bool ok(const FEMesh *mesh, const Element *elem) const {
    return subproblem->predicate(mesh, elem);
  }
public:
  PredicateSubProblemElementIteratorOLD(const PredicateSubProblem<PRDCT> *subp);
  PredicateSubProblemElementIteratorOLD(
			    const PredicateSubProblemElementIteratorOLD<PRDCT>&);
  virtual void operator++();
  virtual bool end() const { return iter.end(); }
  virtual int size() const;
  virtual int count() const { return count_; }
  virtual Element *element() const { return iter.element(); }
  virtual ElementIteratorBase *clone() const {
    return new PredicateSubProblemElementIteratorOLD<PRDCT>(*this);
  }
};

template <class PRDCT>
PredicateSubProblemElementIteratorOLD<PRDCT>::PredicateSubProblemElementIteratorOLD(
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
PredicateSubProblemElementIteratorOLD<PRDCT>::PredicateSubProblemElementIteratorOLD(
		      const PredicateSubProblemElementIteratorOLD<PRDCT> &other)
  : subproblem(other.subproblem),
    iter(*dynamic_cast<MeshElementIteratorOLD*>(other.iter.clone())),
    count_(other.count_),
    size_(other.size_),
    size_computed_(other.size_computed_)
{}

template <class PRDCT>
void PredicateSubProblemElementIteratorOLD<PRDCT>::operator++() {
  ++iter;
  while(!iter.end() && !ok(subproblem->mesh, iter.element()))
    ++iter;
  if(!iter.end())
    count_++;
}

template <class PRDCT>
int PredicateSubProblemElementIteratorOLD<PRDCT>::size() const {
  if(!size_computed_) {
    size_computed_ = true;
    size_ = 0;
    for(ElementIteratorOLD i(subproblem->mesh->element_iterator_OLD()); !i.end(); ++i){
      if(ok(subproblem->mesh, i.element()))
	 size_++;
    }
  }
  return size_;
}

template <class PRDCT>
ElementIteratorOLD PredicateSubProblem<PRDCT>::element_iterator_OLD() const {
  return ElementIteratorOLD(new PredicateSubProblemElementIteratorOLD<PRDCT>(this));
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Node and FuncNode iterators, returned by c_begin and c_end in
// PSPNodeContainer.

template <class PRDCT, class NODE>
class PSPNodeIter : public MeshIterator<NODE> {
protected:
  const PredicateSubProblem<PRDCT>* const subp;
  typename std::set<NODE*, IndexLT<NODE>>::iterator iter;
public:
  PSPNodeIter(const PredicateSubProblem<PRDCT> *const subp,
	      typename std::set<NODE*, IndexLT<NODE>>::iterator iter)
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

template <class PRDCT>
class PSPElementContainer : public VContainer<Element> {
protected:
  const PredicateSubProblem<PRDCT>* const subp;
public:
  PSPElementContainer(const PredicateSubProblem<PRDCT>* const subp)
    : VContainer<Element>(subp->nelements()),
      subp(subp)
  {}
  virtual MeshIterator<Element>* c_begin() const {
    return new PSPNodeIter<PRDCT, Element>(this->subp,
					   this->subp->elements().begin());
  }
  virtual MeshIterator<Element>* c_end() const {
    return new PSPNodeIter<PRDCT, Element>(this->subp,
					   this->subp->elements().end());
  }
};

template <class PRDCT>
class PSPInterfaceElementContainer : public VContainer<InterfaceElement> {
protected:
  const PredicateSubProblem<PRDCT>* const subp;
public:
  PSPInterfaceElementContainer(const PredicateSubProblem<PRDCT>* const subp)
    : VContainer<InterfaceElement>(subp->nedgements()),
      subp(subp)
  {}
  virtual MeshIterator<InterfaceElement>* c_begin() const {
    return new PSPNodeIter<PRDCT, InterfaceElement>(
				    this->subp,
				    this->subp->edgements().begin());
  }
  virtual MeshIterator<InterfaceElement>* c_end() const {
    return new PSPNodeIter<PRDCT, InterfaceElement>(
				    this->subp,
				    this->subp->edgements().end());
  }
};

// Subproblem methods that return the containers

template <class PRDCT>
VContainer<Node>* PredicateSubProblem<PRDCT>::c_node_iterator() const {
  return new PSPNodeContainer<PRDCT>(this);
}
  
template <class PRDCT>
VContainer<FuncNode>* PredicateSubProblem<PRDCT>::c_funcnode_iterator() const {
  return new PSPFuncNodeContainer<PRDCT>(this);
}

template <class PRDCT>
VContainer<Element>* PredicateSubProblem<PRDCT>::c_element_iterator() const {
  return new PSPElementContainer<PRDCT>(this);
}

template <class PRDCT>
VContainer<InterfaceElement>*
PredicateSubProblem<PRDCT>::c_interface_element_iterator() const {
  return new PSPInterfaceElementContainer<PRDCT>(this);
}
  

#endif // PREDICATESUBPROBLEM_H
