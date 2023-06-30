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

/*
  Objects for looping over elements and nodes in FEMeshes and
  CSubProblems.  There are generic interfaces for both.

  The point of this is to provide a uniform interface when iterating
  over the components of a FEMesh, even when the objects being
  returned aren't stored in a simple std::vector or std::set.
  However, it may not be worth the effort...

  The iterators are now real STL-style iterators that can be used like
  this:

    for(Node *node : subproblem->node_iterator()) { ... }

  or
  
    for(auto iter=mesh.node_iterator().begin();
        iter!=mesh.node_iterator().end(); iter++)
	{
           Node *node = *iter;
           ...
        }

  or in Python:
  
     for node in subproblem.nodes():
         ...
  
  FEMesh and all CSubProblem classes need the methods node_iterator(),
  funcnode_iterator(), and element_iterator(). They return a
  VContainerP<Node>, VContainerP<FuncNode>, or VContainerP<Element>.
  "VContainer" is a Virtual container -- it doesn't actually contain
  anything except a pointer to the FEMesh or CSubProblem, but it knows
  how to iterate over the mesh or subproblem and therefore acts like a
  container.  VContainerP<OBJ> wraps a pointer to a VContainer<OBJ>,
  which provides virtual functions that support iteration, namely
  begin(), end(), c_begin(), and c_end().  "VContainerP" is a pointer
  to a virtual container.

  [TODO PYTHON3?  Rename FEMesh::node_iterator(), et al. because the
  functions don't actually return iterators.  Better names might be
  nodes(), funcnodes(), and elements().]

  The VContainer classes define c_begin() and c_end(), which return
  *pointers* to new iterators. They're called by python via swig (the
  "c_" in the name means it's the C++ part of the python iterator.)

  In C++, iteration over a VContainer<OBJ> is done by its begin() and
  end() methods, which return STL compatible forward iterators (more
  or less).  begin() and end() wrap c_begin() and c_end() with an
  IterP<OBJ> object, which just handles deallocation of the pointer.
  Dereferencing an iterator or IterP in C++ produces a pointer to an
  OBJ.
 
  VContainerP<OBJ> does *not* need to be derived from a non-templated
  base class, independent of OBJ.  We always know whether we're
  iterating over Nodes, FuncNodes, or elements, so the template
  argument is always known.

  Different kinds of CSubProblems (and FEMesh) need to return
  different types of VContainers, which will in turn return different
  types of iterators.  The VContainers can be different because
  they're wrapped by VContainerP, which makes virtual function calls
  through the VContainer pointer.  This is necessary because they will
  be used in situations in which the subproblem type isn't known:
     CSubProblem *subp = ...; // base class pointer
     for(auto iter=subp.nodes().begin(); ... )

  TODO PYTHON3:  The VContainer machinery involves a lot of virtual
  functions and dynamic casts, which is why just looping over
  funcnodes is about 4 times faster in C++ if we use unadorned
  std::vector iteration. (See FEMesh::funcnode_iterator_simple().)
  However, the time difference between the two versions in Python is
  negligible.  Since the iterator itself ought to use less time than
  the body of the iteration, it's not clear that it's worth switching
  to the simpler scheme, which would give up a lot of the uniformity
  of the VContainer method.

*/



#ifndef MESHITERATOR_H
#define MESHITERATOR_H

class Element;
class FEMesh;
class FuncNode;
class InterfaceElement;
class Node;

#include <ostream>
#include <vector>

// Base class for all mesh iterators.  OBJ is the type of the contents
// of the container being iterated over: Node, FuncNode, Element, etc.

// This base class is provided so that IterP<> can use ++, !=, and *
// operators.  Unfortunately, it means that those operators defined in
// the derived classes must use generic argument types (eg
// MeshIterator<Node>&) in operator!= instead of specific ones
// (MeshNodeIterator&), which requires a dynamic_cast in the method
// definition.  Returning a generic value from operator++ is less
// bothersome.

// TODO? A lot of the complication here could be eliminated if we
// didn't want the SubProblem iterators to share a common base class
// and interface with the Mesh iterators.  SubProblem iteration can be
// more complicated because a SubProblem's nodes and elements aren't
// necessarily stored in a simple std::vector.

template <class OBJ>
class MeshIterator { 
public:
  virtual ~MeshIterator() {}
  virtual MeshIterator<OBJ>& operator++() = 0;
  virtual bool operator!=(const MeshIterator<OBJ>&) const = 0;
  virtual OBJ* operator*() const = 0;
  virtual MeshIterator<OBJ>* clone() const = 0;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Subclasses of MeshNodeIterator determine which nodes are iterated over.

// TODO PYTHON3: Change the names of the base classes now that they're
// used for both Nodes and Elements.

template <class NODE>
class MeshNodeIterBase : public MeshIterator<NODE> {
protected:
  unsigned int index;
  const FEMesh* const mesh;
public:
  MeshNodeIterBase(const FEMesh* const mesh) : mesh(mesh), index(0) {}
  MeshNodeIterBase(const FEMesh* const mesh, unsigned int i)
    : mesh(mesh), index(i)
  {}
  virtual ~MeshNodeIterBase() {}
};

class MeshNodeIter : public MeshNodeIterBase<Node> {
public:
  MeshNodeIter(const FEMesh* const mesh) : MeshNodeIterBase(mesh) {}
  MeshNodeIter(const FEMesh* const mesh, unsigned int i)
    : MeshNodeIterBase(mesh, i)
  {}
  virtual MeshIterator<Node>* clone() const {
    return new MeshNodeIter(mesh, index);
  }
  virtual MeshIterator<Node>& operator++() { index++; return *this; }
  virtual bool operator!=(const MeshIterator<Node>&) const;
  virtual Node* operator*() const;
};

class MeshFuncNodeIter : public MeshNodeIterBase<FuncNode> {
public:
  MeshFuncNodeIter(const FEMesh* const mesh) : MeshNodeIterBase(mesh) {}
  MeshFuncNodeIter(const FEMesh* const mesh, unsigned int i)
    : MeshNodeIterBase(mesh, i)
  {}
  virtual MeshIterator<FuncNode>* clone() const {
    return new MeshFuncNodeIter(mesh, index);
  }
  virtual MeshIterator<FuncNode>& operator++() { index++; return *this; }
  virtual bool operator!=(const MeshIterator<FuncNode>&) const;
  virtual FuncNode* operator*() const;
};

class MeshElementIter : public MeshNodeIterBase<Element> {
public:
  MeshElementIter(const FEMesh* const mesh) : MeshNodeIterBase(mesh) {}
  MeshElementIter(const FEMesh* const mesh, unsigned int i)
    : MeshNodeIterBase(mesh, i)
  {}
  virtual MeshIterator<Element>* clone() const {
    return new MeshElementIter(mesh, index);
  }
  virtual MeshIterator<Element>& operator++() { index++; return *this; }
  virtual bool operator!=(const MeshIterator<Element>&) const;
  virtual Element *operator*() const;
};

class MeshInterfaceElementIter : public MeshNodeIterBase<InterfaceElement> {
public:
  MeshInterfaceElementIter(const FEMesh* const mesh) : MeshNodeIterBase(mesh) {}
  MeshInterfaceElementIter(const FEMesh* const mesh, unsigned int i)
    : MeshNodeIterBase(mesh, i)
  {}
  virtual MeshIterator<InterfaceElement>* clone() const {
    return new MeshInterfaceElementIter(mesh, index);
  }
  virtual MeshIterator<InterfaceElement>& operator++() {
    index++;
    return *this;
  }
  virtual bool operator!=(const MeshIterator<InterfaceElement>&) const;
  virtual InterfaceElement *operator*() const;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Smart-ish wrapper for iterators, so they can be used in for
// statements without worrying about deallocation.  OBJ is Node,
// FuncNode, or Element.

// TODO: Should we just use CleverPtr for this?  CleverPtr won't work
// if a copy constructor is needed.  It also requires dereferencing on
// all method calls, so it's not a drop-in replacement for
// MeshIterator<OBJ>.

template <class OBJ>
class IterP {
private:
  MeshIterator<OBJ> *iter;
public:
  IterP(MeshIterator<OBJ> *i) : iter(i) {}
  ~IterP() { delete iter; }
  IterP(IterP &&o) : iter(o.iter) { o.iter = nullptr; }
  IterP(const IterP &o) : iter(o.iter->clone()) {}
  OBJ* operator*() const { return **iter; }
  IterP<OBJ>& operator++() { iter->operator++(); return *this; }
  bool operator!=(const IterP &other) const { return *iter != *other.iter; }
};


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// VContainers are lightweight objects that have begin() and end()
// methods returning iterators.  They don't actually contain anything,
// but they *act* like containers containing mesh objects, such as
// nodes or elements.  Different types of containers can "contain"
// different subsets of mesh objects by returning different types of
// iterators.

template <class OBJ>
class VContainer {
private:
  unsigned int size_;
public:
  VContainer(unsigned int s) : size_(s) {}
  virtual ~VContainer() {}
  // begin() and end() are called from C++ and return an IterP which
  // wraps an iterator pointer.  IterP owns the pointer and will
  // destroy it when it's done.  c_begin and c_end are called from
  // python, and don't wrap the pointer because Python will take care
  // of it.
  virtual MeshIterator<OBJ>* c_begin() const = 0;
  virtual MeshIterator<OBJ>* c_end() const = 0;
  virtual unsigned int size() const { return size_; }
  IterP<OBJ> begin() const { return IterP<OBJ>(c_begin()); }
  IterP<OBJ> end() const { return IterP<OBJ>(c_end()); }
};

class MeshNodeContainer : public VContainer<Node> {
protected:
  const FEMesh* const mesh;
public:
  MeshNodeContainer(const FEMesh *const mesh, unsigned int size)
    : VContainer<Node>(size), mesh(mesh)
  {}
  virtual MeshIterator<Node>* c_begin() const;
  virtual MeshIterator<Node>* c_end() const;
};

class MeshFuncNodeContainer : public VContainer<FuncNode> {
protected:
  const FEMesh* const mesh;
public:
  MeshFuncNodeContainer(const FEMesh* const mesh, unsigned int size)
    : VContainer<FuncNode>(size),
      mesh(mesh)
  {}
  virtual MeshIterator<FuncNode>* c_begin() const;
  virtual MeshIterator<FuncNode>* c_end() const;
};

class MeshElementContainer : public VContainer<Element> {
protected:
  const FEMesh* const mesh;
public:
  MeshElementContainer(const FEMesh *const mesh, unsigned int size)
    : VContainer<Element>(size), mesh(mesh)
  {}
  virtual MeshIterator<Element>* c_begin() const;
  virtual MeshIterator<Element>* c_end() const;
};

class MeshInterfaceElementContainer : public VContainer<InterfaceElement> {
protected:
  const FEMesh* const mesh;
public:
  MeshInterfaceElementContainer(const FEMesh *const mesh, unsigned int size)
    : VContainer<InterfaceElement>(size), mesh(mesh)
  {}
  virtual MeshIterator<InterfaceElement>* c_begin() const;
  virtual MeshIterator<InterfaceElement>* c_end() const;
};

// Smart-ish wrapper for virtual containers.

template <class OBJ>
class VContainerP {
private:
  VContainerP(const VContainerP<OBJ> &c) = delete;
protected:
  VContainer<OBJ> *container;
public:
  VContainerP(VContainer<OBJ> *cntnr) : container(cntnr) {}
  ~VContainerP() { delete container; }
  VContainerP(VContainerP<OBJ> &&c) : container(c.container) {
    c.container = nullptr;
  }
  
  MeshIterator<OBJ> *c_begin() const { return container->c_begin(); }
  MeshIterator<OBJ> *c_end() const { return container->c_end(); }
  IterP<OBJ> begin() const { return IterP<OBJ>(c_begin()); }
  IterP<OBJ> end() const { return IterP<OBJ>(c_end()); }
  unsigned int size() const { return container->size(); }
};

#endif // MESHITERATOR_H
