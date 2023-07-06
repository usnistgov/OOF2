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
#include "engine/meshiterator.h"
#include "engine/entiremeshsubproblem.h"

CEntireMeshSubProblem::CEntireMeshSubProblem() {}

CEntireMeshSubProblem::~CEntireMeshSubProblem() {}

const DoubleIterator<Node, FuncNode, Node>*
CEntireMeshSubProblem::node_iterator()
  const
{
  return mesh->node_iterator();
}

const std::vector<FuncNode*>& CEntireMeshSubProblem::funcnode_iterator() const {
  return mesh->c_funcnode_iterator();
}

const std::vector<Element*>& CEntireMeshSubProblem::element_iterator() const {
  return mesh->c_element_iterator();
}

const std::vector<InterfaceElement*>&
CEntireMeshSubProblem::c_interface_element_iterator() const {
  return mesh->c_interface_element_iterator();
}

bool CEntireMeshSubProblem::contains(const Element*) const {
  return true;
}

bool CEntireMeshSubProblem::containsNode(const Node*) const {
  return true;
}

MaterialSet *CEntireMeshSubProblem::getMaterials() const {
  return mesh->getAllMaterials();
}
