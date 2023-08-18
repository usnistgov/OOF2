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
#include "element.h"
#include "equation.h"
#include "femesh.h"
#include "nodalequation.h"
#include "node.h"

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Names needed for PythonExportable base class
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

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Representational stuff -- mostly for debugging

// const std::string *Node::repr() const {
//   return new std::string("Node(" + tostring(position()) + ")");
// }

// const std::string *FuncNode::repr() const {
//   return new std::string("FuncNode(" + tostring(position()) + ")");
// }

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
