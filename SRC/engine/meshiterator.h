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

// Objects for looping over elements and nodes in FEMeshes and
// CSubProblems.  There are generic interfaces for both.

// TODO: Can this be simplified by using templates and/or mix-in
// classes?

// TODO PYTHON3: Make these into real STL-style iterators.  

#ifndef MESHITERATOR_H
#define MESHITERATOR_H

class CSubProblem;
class FEMesh;
class Node;
class FuncNode;

#include <ostream>
#include <vector>

template <class ITER, class OBJ>
class IterP {
private:
  ITER *iter;
public:
  IterP(ITER *i) : iter(i) {}
  ~IterP() { delete iter; }
  IterP(IterP &&o) : iter(o.iter) { o.iter = nullptr; }
  IterP(const IterP &o) : iter(o.iter->clone()) {}
  OBJ* operator*() const { return **iter; }
  IterP& operator++() { iter->operator++(); return *this; }
  bool operator!=(const IterP &other) const { return *iter != *other.iter; }
};

// Subclasses of MeshNodeIter determine which nodes are iterated over.
// They are the ITER in the IterP template.  Subclasses must have
// *static* methods begin(FEMesh*) and end(FEMesh*) which return
// instances of the subclass.

class MeshNodeIter {
protected:
  std::vector<Node*>::size_type index;
  const FEMesh* const mesh;
public:
  MeshNodeIter(const FEMesh* const mesh) : mesh(mesh), index(0) {}
  MeshNodeIter(const FEMesh* const mesh, int i) : mesh(mesh), index(i) {}
  virtual ~MeshNodeIter() {}
  virtual MeshNodeIter *clone() const = 0;
  bool operator!=(const MeshNodeIter &) const;
  virtual int size() const = 0;
  virtual MeshNodeIter &operator++() { index++; return *this; }
  Node* operator*() const;
};

class MeshAllNodeIter : public MeshNodeIter {
public:
  MeshAllNodeIter(const FEMesh* const mesh) : MeshNodeIter(mesh) {}
  MeshAllNodeIter(const FEMesh* const mesh, int i) : MeshNodeIter(mesh, i) {}
  virtual MeshAllNodeIter* clone() const {
    return new MeshAllNodeIter(mesh, index);
  }
  virtual int size() const;

  static MeshAllNodeIter* begin(const FEMesh* const mesh);
  static MeshAllNodeIter* end(const FEMesh* const mesh);
};

class MeshFuncNodeIter : public MeshNodeIter {
public:
  MeshFuncNodeIter(const FEMesh* const mesh) : MeshNodeIter(mesh) {}
  MeshFuncNodeIter(const FEMesh* const mesh, int i) : MeshNodeIter(mesh, i) {}
  virtual MeshFuncNodeIter* clone() const {
    return new MeshFuncNodeIter(mesh, index);
  }
  virtual int size() const;

  static MeshFuncNodeIter* begin(const FEMesh* const mesh);
  static MeshFuncNodeIter* end(const FEMesh* const mesh); 
};

// Instances of MeshNodeContainer<> are returned by
// FEMesh::node_iterator, funcnode_iterator, etc.

// TODO PYTHON3: I don't like the name MeshNodeContainer.  It should
// be changed to MeshNodeIterator after the old NodeIterator classes
// are removed.

template <class ITER>
class MeshNodeContainer {
private:
  const FEMesh* const mesh;
public:
  MeshNodeContainer(const FEMesh* const mesh) : mesh(mesh) {}

  // begin() and end() are called from C++ and need to wrap the
  // iterator pointer in IterP, which owns the pointer and will
  // destroy it when it's done.  c_begin and c_end are called from
  // python, and don't wrap the pointer because Python will take care
  // of it.
  ITER* c_begin() const { return ITER::begin(mesh); }
  ITER* c_end() const { return ITER::end(mesh); }
  IterP<ITER, Node> begin() const {
    return IterP<ITER, Node>(ITER::begin(mesh));
  }
  IterP<ITER, Node> end() const {
    return IterP<ITER, Node>(ITER::end(mesh));
  }
};


///// OLD BELOW HERE

// Virtual base class for MeshNodeIterator and various types of
// SubProblemNodeIterator.

class NodeIteratorBase {
public:
  NodeIteratorBase() {}
  virtual ~NodeIteratorBase() {}
  virtual Node *node() const = 0;
  virtual void operator++() = 0;
  virtual bool begin() const = 0;
  virtual bool end() const = 0;
  virtual int size() const = 0;
  virtual NodeIteratorBase *clone() const = 0;
};

class MeshNodeIterator : public NodeIteratorBase {
private:
  const FEMesh *const mesh;
  std::vector<Node*>::size_type index;
public:
  MeshNodeIterator(const FEMesh *const);
  virtual Node *node() const;
  virtual void operator++();
  virtual bool begin() const;
  virtual bool end() const;
  virtual int size() const;
  virtual NodeIteratorBase *clone() const;
};

// NodeIterator is a wrapper class for MeshNodeIterator and the
// various types of SubProblemNodeIterator.

class NodeIterator {
private:
  NodeIteratorBase *base;
public:
  NodeIterator(NodeIteratorBase *base) : base(base) {}
  NodeIterator(const NodeIterator&);
  virtual ~NodeIterator();
  void operator++() { base->operator++(); }
  bool begin() const { return base->begin(); }
  bool end() const { return base->end(); }
  int size() const { return base->size(); }
  Node *node() const { return base->node(); }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class FuncNodeIteratorBase {
public:
  FuncNodeIteratorBase() {}
  virtual ~FuncNodeIteratorBase() {}
  virtual FuncNode *node() const = 0;
  virtual void operator++() = 0;
  virtual bool begin() const = 0;
  virtual bool end() const = 0;
  virtual int count() const = 0;
  virtual int size() const = 0;
  virtual FuncNodeIteratorBase *clone() const = 0;
};

class MeshFuncNodeIterator : public FuncNodeIteratorBase {
private:
  const FEMesh *const mesh;
  std::vector<FuncNode*>::size_type index;
public:
  MeshFuncNodeIterator(const FEMesh * const);
  virtual FuncNode *node() const;
  virtual void operator++();
  virtual bool begin() const;
  virtual bool end() const;
  virtual int count() const { return index; }
  virtual int size() const;
  virtual FuncNodeIteratorBase *clone() const;
};

class FuncNodeIterator {
private:
  FuncNodeIteratorBase *base;
public:
  FuncNodeIterator(FuncNodeIteratorBase *base) : base(base) {}
  FuncNodeIterator(const FuncNodeIterator&);
  ~FuncNodeIterator();
  void operator++() { base->operator++(); }
  bool end() const { return base->end(); }
  int size() const { return base->size(); }
  int count() const { return base->count(); }
  FuncNode *node() const { return base->node(); }
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class ElementIteratorBase {
public:
  virtual ~ElementIteratorBase() {}
  virtual void operator++() = 0;
  virtual bool end() const = 0;
  virtual int size() const = 0;
  virtual int count() const = 0;
  virtual Element *element() const = 0;
  virtual ElementIteratorBase *clone() const = 0;
};

class MeshElementIterator : public ElementIteratorBase {
private:
  const FEMesh * const mesh;
  std::vector<Element*>::size_type index;
public:
  MeshElementIterator(const FEMesh *const);
  virtual ~MeshElementIterator() {}
  virtual void operator++();
  virtual bool end() const;
  virtual int size() const;
  virtual int count() const;
  virtual Element *element() const;
  virtual ElementIteratorBase *clone() const;
};

//Interface branch
class MeshInterfaceElementIterator : public ElementIteratorBase {
private:
  const FEMesh * const mesh;
  std::vector<Element*>::size_type index;
public:
  MeshInterfaceElementIterator(const FEMesh *const);
  virtual ~MeshInterfaceElementIterator() {}
  virtual void operator++();
  virtual bool end() const;
  virtual int size() const;
  virtual int count() const;
  virtual Element *element() const;
  virtual ElementIteratorBase *clone() const;
};

class ElementIterator {
private:
  ElementIteratorBase *base;
public:
  ElementIterator(ElementIteratorBase *base) : base(base) {}
  ~ElementIterator();
  ElementIterator(const ElementIterator&);
  void operator++() { base->operator++(); }
  bool end() const { return base->end(); }
  int size() const { return base->size(); }
  int count() const { return base->count(); } // # of elements already seen
  Element *element() const { return base->element(); }
};


#endif // MESHITERATOR_H
