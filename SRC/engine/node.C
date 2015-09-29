// -*- C++ -*-
// $RCSfile: node.C,v $
// $Revision: 1.44 $
// $Author: langer $
// $Date: 2011/07/14 21:19:31 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/tostring.h"
#include "common/trace.h"
#include "element.h"
#include "equation.h"
#include "femesh.h"
#include "nodalequation.h"
#include "node.h"

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Names needed for PythonExportable base class
const std::string Node::modulename_("ooflib.SWIG.engine.node");
const std::string Node::classname_("Node");
const std::string FuncNode::classname_("FuncNode");

Node::Node(int n, const Coord &p)
  : pos(p),
    index_(n)
{}

FuncNode::FuncNode(FEMesh *mesh, int n, const Coord &p)
  : Node(n, p), PointData(mesh)
{
  // No space is allocated for dofs or nodaleqns here.  It's all done
  // by addField and addEquation.  That means that we're assuming that
  // the FEMesh construction process creates all of the nodes *before*
  // defining any fields or activating any equations.  
  
  // addField and addEquation are in the PointData class, of which
  // nodes are a subclass.
  
#ifdef HAVE_MPI
  //  notShared();
#endif
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Node comparison operator -- the node integer index 
// is the one true arbiter of node equality.

bool operator==(const Node &n1, const Node &n2)
{
  return n1.index() == n2.index();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// void FuncNode::addField(FEMesh *mesh, const Field &field) {
// //   Trace("FuncNode::addField " + field.name() + " " + to_string(index()) 
// // 	+ " Pos: " + to_string(pos));

//   if(fieldset.add(&field, mesh)) {
//     // Field is new to this Node (ie, no other SubProblem has added it)
//     // TODO: Do we have to initialize it here?  How would we know?
//     doflist.reserve(doflist.size() + field.ndof());
//     for(int i=0; i<field.ndof(); i++) {
//       DegreeOfFreedom *dof = mesh->createDoF();
// //       std::cerr << "FuncNode::addField: " << field
// // 		<< " dof=" << dof->dofindex()
// //  		<< " comp=" << i << " pos=" << pos << std::endl;
//       doflist.push_back(dof);
// #ifdef HAVE_MPI
//       if(isShared())
// 	mesh->m_dofnodemap[dof] = this;
// #endif // HAVE_MPI
//     }
//   }
// }

// void FuncNode::removeField(FEMesh *mesh, const Field &field) {
// //    Trace("FuncNode::removeField " + field.name() + " " + to_string(index())
// // 	 + " Pos: " + to_string(pos));

//   // Remove degrees of freedom from doflist, if no SubProblems are
//   // using them anymore.

//   int offset = fieldset.offset(&field);
//   if(fieldset.remove(&field, mesh)) {
//   //    std::cerr << "FuncNode::removeField: removing " << field << " from " << *this << std::endl;
//     // This SubProblem is the only one remaining that was using the Field
//     std::vector<DegreeOfFreedom*>::iterator start = doflist.begin() + offset;
//     std::vector<DegreeOfFreedom*>::iterator end = start + field.ndof();
//     for(std::vector<DegreeOfFreedom*>::iterator i=start; i<end; ++i) {
//       mesh->removeDoF(*i);
// #ifdef HAVE_MPI
//       // No need to check if the key is in the map (but why not check anyway?)
//       if(isShared())
// 	mesh->m_dofnodemap.erase(*i);
// #endif // HAVE_MPI
//     }
//     doflist.erase(start, end);
//   }
// }

// bool FuncNode::hasField(const Field &field) const {
//   return fieldset.contains(&field);
// }

// int FuncNode::fieldDefCount(const Field &field) const {
//   return fieldset.listed(&field);
// }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// void FuncNode::addEquation(FEMesh *mesh, const Equation &eqn) {
// //   Trace("FuncNode::addEquation " + eqn.name() + " " + to_string(index())
// // 	+ " Pos: " + to_string(pos));
//   if(equationset.add(&eqn, mesh)) {
//     // Equation is new to this Node (ie, no other SubProblem has added it)
//     eqnlist.reserve(eqnlist.size() + eqn.dim());
//     for(int i=0; i<eqn.dim(); i++) {
//       NodalEquation *ne = mesh->createNodalEqn();
//       eqnlist.push_back(ne);
// //       std::cerr << "FuncNode::addEquation: " << eqn
// // 		<< " idx=" << ne->ndq_index()
// // 		<< " comp=" << i << " pos=" << pos << std::endl;
// #ifdef HAVE_MPI
//       if(isShared())
// 	mesh->m_eqnnodemap[ne] = this; // TODO MPI: Move to SubProblem?
// #endif // HAVE_MPI
//     }
//   }
// }

// void FuncNode::removeEquation(FEMesh *mesh, const Equation &eqn) {
// //   Trace("FuncNode::removeEquation " + eqn.name() + " " + to_string(index())
// // 	+ " Pos: " + to_string(pos));
//   int offset = equationset.offset(&eqn);
//   if(equationset.remove(&eqn, mesh)) {
//     std::vector<NodalEquation*>::iterator start = eqnlist.begin() + offset;
//     std::vector<NodalEquation*>::iterator end = start + eqn.dim();
//     for(std::vector<NodalEquation*>::iterator i=start; i<end; ++i) {
//       mesh->removeNodalEqn(*i);
// #ifdef HAVE_MPI
//       // No need to check if the key is in the map
//       if(isShared())
// 	mesh->m_eqnnodemap.erase(*i);
// #endif
//     }
//     eqnlist.erase(start, end);
//   }
// }

// bool FuncNode::hasEquation(const Equation &eqn) const {
//   return equationset.contains(&eqn);
// }

//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//

Coord FuncNode::displaced_position(const FEMesh *mesh) const {
#if DIM==2
  static TwoVectorField *displcmnt = 0;
  if(!displcmnt)
    displcmnt = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
#elif DIM==3
  static ThreeVectorField *displcmnt = 0;
  if(!displcmnt)
    displcmnt = dynamic_cast<ThreeVectorField*>(Field::getField("Displacement"));
#endif
  if(hasField(*displcmnt)) {
    double dx = (*displcmnt)(this, 0)->value(mesh);
    double dy = (*displcmnt)(this, 1)->value(mesh);
#if DIM==2
    return pos + Coord(dx, dy);
#elif DIM==3
    double dz = (*displcmnt)(this, 2)->value(mesh);
    return pos + Coord(dx, dy, dz);
#endif
  }
  return pos;
}

//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//

// Representational stuff -- mostly for debugging

// const std::string *Node::repr() const {
//   return new std::string("Node(" + to_string(position()) + ")");
// }

// const std::string *FuncNode::repr() const {
//   return new std::string("FuncNode(" + to_string(position()) + ")");
// }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Print a string suitable for use in a Python constructor

const std::string *Node::ctor() const {
  return new std::string("newMapNode(Coord" + to_string(position()) + ")");
}

const std::string *FuncNode::ctor() const {
  return new std::string("newFuncNode(Coord" + to_string(position()) + ")");
}

//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//-\\-//

std::ostream &operator<<(std::ostream &os, const Node &node) {
  os << "[" << node.index() << "] " << node.pos;
  return os;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::vector<std::string> *Node::fieldNames() const {
  return new std::vector<std::string>;
}

std::vector<std::string> *FuncNode::fieldNames() const {
  std::vector<std::string> *names = new std::vector<std::string>;
  for(int i=0; i<countCompoundFields(); i++) {
    // TODO: There has to be a better way to do this. 
    CompoundField *field = getCompoundFieldByIndex(i);
    if(hasField(*field)) {
      names->push_back(field->name());
    }
  }
  return names;
}
