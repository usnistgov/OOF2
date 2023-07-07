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
  return o.index != index;
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
  return o.index != index;
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
  return o.index != index;
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

InterfaceElement *MeshInterfaceElementIter::operator*() const {
  return mesh->edgement[index];
}

MeshIterator<InterfaceElement> *MeshInterfaceElementContainer::c_begin() const {
  return new MeshInterfaceElementIter(mesh);
}

MeshIterator<InterfaceElement> *MeshInterfaceElementContainer::c_end() const {
  return new MeshInterfaceElementIter(mesh, mesh->nedgements());
}

bool MeshInterfaceElementIter::operator!=(
			  const MeshIterator<InterfaceElement> &other)
  const
{
  const MeshInterfaceElementIter &o
    = dynamic_cast<const MeshInterfaceElementIter&>(other);
  return o.index != index;
}
