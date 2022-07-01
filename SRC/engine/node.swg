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

%module node
%include "engine/typemaps.swg"
%import "common/coord.swg"
%import "engine/field.swg"
%import "engine/pointdata.swg"
%pragma(python) code="from ooflib.SWIG.engine.pointdata import PointDataPtr"

%{
#include "engine/node.h"
%}

class Node
{
public:
  int index();

  Coord position();

  %new const string *ctor();
  const string &classname();
  // int ndof();
  // int neqn();

  %new StringVec *fieldNames();

  %addmethods {
    double __getitem__(int i) {
      return self->position()(i);
    }
  }
};

class FuncNode : public Node, public PointData {
public:
  Coord displaced_position(FEMesh*);
};

%pythoncode "engine/node.spy"

#endif // NODE_SWG
