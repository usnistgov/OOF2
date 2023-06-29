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

Node *MeshNodeIter::operator*() const {
  return mesh->getNode(index);
}

MeshIterator<Node>* MeshNodeContainer::c_begin() const {
  return new MeshNodeIter(mesh);
}

MeshIterator<Node>* MeshNodeContainer::c_end() const {
  return new MeshNodeIter(mesh, mesh->nnodes());
}

bool MeshNodeIter::operator!=(const MeshIterator<Node> &other) const {
  const MeshNodeIter &o = dynamic_cast<const MeshNodeIter&>(other);
  // TODO PYTHON3: for purposes of looping, comparing the mesh
  // pointers here is unnecessary.  Would it save any time, or does
  // the dynamic cast dominate the inefficiency?
  return o.mesh != mesh || o.index != index;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

FuncNode *MeshFuncNodeIter::operator*() const {
  return mesh->getFuncNode(index);
}

MeshIterator<FuncNode>* MeshFuncNodeContainer::c_begin() const {
  return new MeshFuncNodeIter(mesh);
}

MeshIterator<FuncNode>* MeshFuncNodeContainer::c_end() const {
  return new MeshFuncNodeIter(mesh, mesh->nfuncnodes());
}

bool MeshFuncNodeIter::operator!=(const MeshIterator<FuncNode> &other) const {
  const MeshFuncNodeIter &o = dynamic_cast<const MeshFuncNodeIter&>(other);
  return o.mesh != mesh || o.index != index;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

Element *MeshElementIter::operator*() const {
  return mesh->getElement(index);
}

MeshIterator<Element> *MeshElementContainer::c_begin() const {
  return new MeshElementIter(mesh);
}

MeshIterator<Element> *MeshElementContainer::c_end() const {
  return new MeshElementIter(mesh, mesh->nelements());
}

bool MeshElementIter::operator!=(const MeshIterator<Element> &other) const {
  const MeshElementIter &o = dynamic_cast<const MeshElementIter&>(other);
  return o.mesh != mesh || o.index != index;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

///// OLD BELOW HERE


ElementIteratorOLD::~ElementIteratorOLD() {
  delete base;
}

ElementIteratorOLD::ElementIteratorOLD(const ElementIteratorOLD &other)
  : base(other.base->clone())
{}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

MeshElementIteratorOLD::MeshElementIteratorOLD(const FEMesh * const mesh)
  : mesh(mesh),
    index(0)
{}

void MeshElementIteratorOLD::operator++() {
  if(!end())
    index++;
}

bool MeshElementIteratorOLD::end() const {
  return index == mesh->element.size();
}

Element *MeshElementIteratorOLD::element() const {
  return mesh->element[index];
}

int MeshElementIteratorOLD::size() const {
  return mesh->nelements();
}

int MeshElementIteratorOLD::count() const {
  return index;
}

ElementIteratorBase *MeshElementIteratorOLD::clone() const {
  return new MeshElementIteratorOLD(*this);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//Interface branch

MeshInterfaceElementIteratorOLD::MeshInterfaceElementIteratorOLD(const FEMesh * 
							   const mesh)
  : mesh(mesh),
    index(0)
{}

void MeshInterfaceElementIteratorOLD::operator++() {
  if(!end())
    index++;
}

bool MeshInterfaceElementIteratorOLD::end() const {
  return index == mesh->edgement.size();
}

//TODO: Return InterfaceElement*?
Element *MeshInterfaceElementIteratorOLD::element() const {
  return mesh->edgement[index];
}

int MeshInterfaceElementIteratorOLD::size() const {
  return mesh->nedgements();
}

int MeshInterfaceElementIteratorOLD::count() const {
  return index;
}

ElementIteratorBase *MeshInterfaceElementIteratorOLD::clone() const {
  return new MeshInterfaceElementIteratorOLD(*this);
}

