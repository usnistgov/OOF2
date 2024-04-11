// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef NODE_SWG
#define NODE_SWG

%module(package="ooflib.SWIG.engine") node

%include "common/typemaps.swg"
%import "common/coord.swg"
%import "engine/field.swg"

%{
#include "engine/node.h"
  #include "engine/flux.h"	// SWIGBUG
%}

PYTHONEXPORTABLE(Node);

%nodefaultctor Node;

class Node
{
public:
  int index();

  Coord position();

  %newobject ctor;
  const std::string *ctor();
  const std::string &classname();
  // int ndof();
  // int neqn();

  %newobject fieldNames;
  std::vector<std::string> *fieldNames();
};

%extend Node {
  double __getitem__(int i) {
    return self->position()(i);
  }
};

%nodefaultctor FuncNode;

class FuncNode : public Node {
public:
  Coord displaced_position(FEMesh*);
  bool hasField(const Field&);
  int fieldDefCount(const Field&);
  int fieldSetID();
};

%pythoncode "engine/node.spy"

#endif // NODE_SWG
