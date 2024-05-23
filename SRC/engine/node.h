// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

class Node;

#ifndef NODE_H
#define NODE_H

#include "common/coord.h"
#include "engine/equation.h"
#include "engine/field.h"
#include "engine/fieldeqnlist.h"
#include "engine/freedom.h"
#include "common/pythonexportable.h"
#include <vector>
#include <iostream>

class FEMesh;
class NodalEquation;
class ElementMapNodeIterator;

class Node : public PythonExportable<Node>, public Position {
private:
  static const std::string classname_;
protected:
  Node(int n, const Coord &p);	// only called by FEMesh::newMapNode()
  Node(const Node&);		// prohibited
  Node &operator=(const Node&);	// prohibited

  Coord pos;
  int index_;	// unique for this Node, but not necessarily constant in time.
public:
  int index() const { return index_; }
  
  virtual ~Node() {}
  virtual const std::string &classname() const { return classname_; }
  virtual Coord position() const { return pos; } // get original position

  friend bool operator==(const Node&, const Node&);
  friend bool operator!=(const Node &n0, const Node &n1) { return !(n0==n1); }

  friend std::ostream& operator<<(std::ostream&, const Node&);
  friend class FEMesh;

  // virtual const std::string *repr() const;
  virtual const std::string *ctor() const;

  virtual std::vector<std::string> *fieldNames() const;
};

// Node at which function parameters (degrees of freedom, nodal
// equations) are defined

class FuncNode : public Node {
private:
  static const std::string classname_;
#ifdef HAVE_MPI
  // This may be generalized to include other flags
  //  that require only a bit of storage
  bool _bshare;
#endif
protected:
  FuncNode(FEMesh*, int n, const Coord &p);
                  // only called by FEMesh::newFuncNode()
  friend class FEMesh;
public:
  virtual ~FuncNode() {}
  virtual const std::string &classname() const { return classname_; }

  std::vector<DegreeOfFreedom*> doflist;
  std::vector<NodalEquation*> eqnlist;

  // Used by the regression tests to check solutions.
  Coord displaced_position(const FEMesh*) const;

  int ndof() const { return doflist.size(); }
  int neqn() const { return eqnlist.size(); }

  void addField(FEMesh*, const Field&);
  void removeField(FEMesh*, const Field&);
    bool hasField(const Field&) const;
  // Returns the number of subproblems containing this point for which
  // the passed-in field is defined.
  int fieldDefCount(const Field&) const;

  void addEquation(FEMesh*, const Equation&);
  void removeEquation(FEMesh*, const Equation&);
  bool hasEquation(const Equation&) const;

  typedef FieldEqnList<Field> FieldSet;
  typedef FieldEqnList<Equation> EquationSet;
  FieldSet fieldset;
  EquationSet equationset;

  int fieldSetID() const { return fieldset.id(); }

  virtual const std::string *ctor() const;

  virtual std::vector<std::string> *fieldNames() const;

#ifdef HAVE_MPI
//   void setShared(){ _bshare=true; }
//   void notShared(){ _bshare=false; }
//   bool isShared(){ return _bshare; }
#endif

};				// FuncNode

std::ostream &operator<<(std::ostream&, const FuncNode::FieldSet&);

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Base class for functionals evaluated by Element::interpolate() -- a
// scalar valued function evaluated at a FuncNode.

class FuncNodeFunction {
public:
  virtual ~FuncNodeFunction() {}
  virtual double operator()(const FuncNode*) = 0;
};

#endif
