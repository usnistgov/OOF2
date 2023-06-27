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

#include "engine/femesh.h"
#include "engine/element.h"
#include "engine/meshiterator.h"

// int MeshNodeIter::size() const {
//   return mesh->nnodes();
// }

Node *MeshNodeIter::operator*() const {
  return mesh->getNode(index);
}

// int MeshFuncNodeIter::size() const {
//   return mesh->nfuncnodes();
// }

FuncNode *MeshFuncNodeIter::operator*() const {
  return mesh->getFuncNode(index);
}

MeshIterator<Node>* MeshNodeContainer::c_begin() const {
  return new MeshNodeIter(mesh);
}

MeshIterator<Node>* MeshNodeContainer::c_end() const {
  return new MeshNodeIter(mesh, mesh->nnodes());
}

MeshIterator<FuncNode>* MeshFuncNodeContainer::c_begin() const {
  return new MeshFuncNodeIter(mesh);
}

MeshIterator<FuncNode>* MeshFuncNodeContainer::c_end() const {
  return new MeshFuncNodeIter(mesh, mesh->nfuncnodes());
}

bool MeshNodeIter::operator!=(const MeshIterator<Node> &other) const {
  const MeshNodeIter &o = dynamic_cast<const MeshNodeIter&>(other);
  return o.mesh != mesh || o.index != index;
}

bool MeshFuncNodeIter::operator!=(const MeshIterator<FuncNode> &other) const {
  const MeshFuncNodeIter &o = dynamic_cast<const MeshFuncNodeIter&>(other);
  return o.mesh != mesh || o.index != index;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

///// OLD BELOW HERE

#ifdef OLDITERATORS

NodeIterator::NodeIterator(const NodeIterator &other)
  : base(other.base->clone())
{}

NodeIterator::~NodeIterator() {
  delete base;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

MeshNodeIterator::MeshNodeIterator(const FEMesh *const m)
  : mesh(m),
    index(0)
{}

void MeshNodeIterator::operator++() {
  if(int(index) != mesh->nnodes())
    index++;
}

int MeshNodeIterator::size() const {
  return mesh->nnodes();
}

bool MeshNodeIterator::begin() const {
  return index == 0;
}

bool MeshNodeIterator::end() const {
  return int(index) == mesh->nnodes();
}

Node *MeshNodeIterator::node() const {
  return mesh->getNode(index);
}

NodeIteratorBase *MeshNodeIterator::clone() const {
  return new MeshNodeIterator(*this);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

FuncNodeIterator::FuncNodeIterator(const FuncNodeIterator &other)
  : base(other.base->clone())
{}

FuncNodeIterator::~FuncNodeIterator() {
  delete base;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

MeshFuncNodeIterator::MeshFuncNodeIterator(const FEMesh *m)
  : mesh(m),
    index(0)
{}

void MeshFuncNodeIterator::operator++() {
  if(index != mesh->funcnode.size())
    index++;
}

bool MeshFuncNodeIterator::begin() const {
  return index == 0;
}

bool MeshFuncNodeIterator::end() const {
  return index == mesh->funcnode.size();
}

int MeshFuncNodeIterator::size() const {
  return mesh->funcnode.size();
}

FuncNode *MeshFuncNodeIterator::node() const {
  return mesh->funcnode[index];
}

FuncNodeIteratorBase *MeshFuncNodeIterator::clone() const {
  return new MeshFuncNodeIterator(*this);
}

#endif // OLDITERATORS

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ElementIterator::~ElementIterator() {
  delete base;
}

ElementIterator::ElementIterator(const ElementIterator &other)
  : base(other.base->clone())
{}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

MeshElementIterator::MeshElementIterator(const FEMesh * const mesh)
  : mesh(mesh),
    index(0)
{}

void MeshElementIterator::operator++() {
  if(!end())
    index++;
}

bool MeshElementIterator::end() const {
  return index == mesh->element.size();
}

Element *MeshElementIterator::element() const {
  return mesh->element[index];
}

int MeshElementIterator::size() const {
  return mesh->nelements();
}

int MeshElementIterator::count() const {
  return index;
}

ElementIteratorBase *MeshElementIterator::clone() const {
  return new MeshElementIterator(*this);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//Interface branch

MeshInterfaceElementIterator::MeshInterfaceElementIterator(const FEMesh * 
							   const mesh)
  : mesh(mesh),
    index(0)
{}

void MeshInterfaceElementIterator::operator++() {
  if(!end())
    index++;
}

bool MeshInterfaceElementIterator::end() const {
  return index == mesh->edgement.size();
}

//TODO: Return InterfaceElement*?
Element *MeshInterfaceElementIterator::element() const {
  return mesh->edgement[index];
}

int MeshInterfaceElementIterator::size() const {
  return mesh->nedgements();
}

int MeshInterfaceElementIterator::count() const {
  return index;
}

ElementIteratorBase *MeshInterfaceElementIterator::clone() const {
  return new MeshInterfaceElementIterator(*this);
}

