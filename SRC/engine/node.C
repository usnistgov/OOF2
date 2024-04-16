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
#include "common/tostring.h"
#include "common/trace.h"
#include "engine/element.h"
#include "engine/equation.h"
#include "engine/femesh.h"
#include "engine/freedom.h"
#include "engine/nodalequation.h"
#include "node.h"

// To dump index information about DoFs and eqns, uncomment this line
// and compile in debug mode.
//#define VERBOSE_POINTDATA


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Names needed for PythonExportable base class
const std::string Node::classname_("Node");
const std::string FuncNode::classname_("FuncNode");

Node::Node(int n, const Coord &p)
  : pos(p),
    index_(n)
{}

FuncNode::FuncNode(FEMesh *mesh, int n, const Coord &p)
  : Node(n, p),
    fieldset(mesh),
    equationset(mesh)
{
  // No space is allocated for dofs or nodaleqns here.  It's all done
  // by addField and addEquation.  That means that we're assuming that
  // the FEMesh construction process creates all of the nodes *before*
  // defining any fields or activating any equations.  
  
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

Coord FuncNode::displaced_position(const FEMesh *mesh) const {
  static TwoVectorField *displcmnt = 0;
  if(!displcmnt)
    displcmnt = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
  if(hasField(*displcmnt)) {
    double dx = (*displcmnt)(this, 0)->value(mesh);
    double dy = (*displcmnt)(this, 1)->value(mesh);
    return pos + Coord(dx, dy);
  }
  return pos;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void FuncNode::addField(FEMesh* mesh, const Field &field) {  
  if(fieldset.add(&field, mesh)) {
    // This is the first time we've seen this field -- create and add
    // the DOFs.
    doflist.reserve(doflist.size() + field.ndof());
    for(int i=0;i<field.ndof(); i++) {
      DegreeOfFreedom *dof = mesh->createDoF();
#ifdef VERBOSE_POINTDATA 
#ifdef DEBUG
      std::cerr << "FuncNode::addField: " << field
      		<< " dof=" << dof->dofindex()
      		<< " comp=" << i << " pos=" << position() << std::endl;
#endif // DEBUG
#endif // VERBOSE_POINTDATA
      doflist.push_back(dof);
    }
  }
}

void FuncNode::removeField(FEMesh *mesh, const Field &field) {

  int offset = fieldset.offset(&field);
  
  if (fieldset.remove(&field, mesh)) {
    std::vector<DegreeOfFreedom*>::iterator start = doflist.begin() + offset;
    std::vector<DegreeOfFreedom*>::iterator end = start + field.ndof();
    for(std::vector<DegreeOfFreedom*>::iterator i=start; i< end; ++i) {
      mesh->removeDoF(*i);
    }
    doflist.erase(start,end);
  }
}
    
bool FuncNode::hasField(const Field &field) const {
  return fieldset.contains(&field);
}

int FuncNode::fieldDefCount(const Field & field) const {
  return fieldset.listed(&field);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void FuncNode::addEquation(FEMesh *mesh, const Equation &eqn) {
  if(equationset.add(&eqn, mesh)) {
    // Equation is new to this Node (ie, no other SubProblem has added it)
    eqnlist.reserve(eqnlist.size() + eqn.dim());
    for(int i=0; i<eqn.dim(); i++) {
      NodalEquation *ne = mesh->createNodalEqn();
#ifdef VERBOSE_POINTDATA
#ifdef DEBUG
      std::cerr << "FuncNode::addEquation: " << eqn
      		<< " nodaleqn=" << ne->ndq_index()
      		<< " comp=" << i << " pos=" << position() << std::endl;
#endif // DEBUG
#endif // VERBOSE_POINTDATA
      eqnlist.push_back(ne);
    }
  }
}


void FuncNode::removeEquation(FEMesh *mesh, const Equation &eqn) {
  int offset = equationset.offset(&eqn);
  if(equationset.remove(&eqn, mesh)) {
    std::vector<NodalEquation*>::iterator start = eqnlist.begin() + offset;
    std::vector<NodalEquation*>::iterator end = start + eqn.dim();
    for(std::vector<NodalEquation*>::iterator i=start; i<end; ++i) {
      mesh->removeNodalEqn(*i);
    }
    eqnlist.erase(start, end);
  }
}


bool FuncNode::hasEquation(const Equation &eqn) const {
  return equationset.contains(&eqn);
}



//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Representational stuff -- mostly for debugging

// const std::string *Node::repr() const {
//   return new std::string("Node(" + tostring(position()) + ")");
// }

// const std::string *FuncNode::repr() const {
//   return new std::string("FuncNode(" + tostring(position()) + ")");
// }

std::ostream &operator<<(std::ostream &os, const FuncNode::FieldSet &fset) {
  std::map<int, const Field*> fmap;
  for(int f=0; f<countFields(); f++) {
    Field *field = getFieldByIndex(f);
    if(fset.contains(field)) {
      fmap[fset.offset(field)] = field;
    }
  }
  os << "Offsets and Fields: " << std::endl;
  for(auto &iter : fmap) {
    os << "   " << iter.first << "-" << (iter.first + iter.second->ndof() - 1)
       << "\t " << *iter.second << std::endl;
  }
  return os;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Print a string suitable for use in a Python constructor

const std::string *Node::ctor() const {
  return new std::string("newMapNode(Coord" + tostring(position()) + ")");
}

const std::string *FuncNode::ctor() const {
  return new std::string("newFuncNode(Coord" + tostring(position()) + ")");
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

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
