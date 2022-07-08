// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef ELEMENTS_SWG
#define ELEMENTS_SWG

%module element
%include "common/typemaps.swg"
%import "common/coord.swg"
%import "engine/csubproblem.swg"
%import "engine/edge.swg"
%import "engine/elementnodeiterator.swg"
%import "engine/femesh.swg"
%import "engine/field.swg"
%import "engine/indextypes.swg"
%import "engine/mastercoord.swg"
%import "engine/material.swg"
%import "engine/outputval.swg"

// %pragma(python) code="from ooflib.SWIG.engine.outputval import OutputValuePtr"
// %pragma(python) code="from ooflib.SWIG.engine.elementnodeiterator import *"
// %pragma(python) code="from ooflib.SWIG.engine.gausspoint import GaussPointPtr"


%{
#include "engine/element.h"
#include "engine/cskeleton.h"
#include "engine/material.h"
%}

// PythonExportable typemap for ElementData*-returning functions.
// Has the extra-special feature of noticing null-pointer returns
// and translating them to "None".

%typemap(out) ElementData* {
  // typemap(out) ElementData*
  if($1 != 0) {
    $result = $source->pythonObject();
    if(!$result)
      SWIG_fail;
  }
  else
    $result = Py_None;
}

class Material;
class ElementNodeIterator;
class ElementMapNodeIterator;
class ElementFuncNodeIterator;
class MasterElement;
class MasterPosition;
class CSkeletonElement;

// Base class for data objects stored in the element.
class ElementData {
public:
  const string &name();
};

MAKE_LISTVEC_TYPEMAPS(GaussPoint);
MAKE_LISTVEC_TYPEMAPS(Edge);

%typemap(newfree) GaussPointVec* {
  delete $1;
 }

class Element {
public:
  Material *material();
  const MasterElement &masterelement();
  double area();
  BoundaryEdge *getBndyEdge(const FuncNode *, const FuncNode *);
  %newobject perimeter;
  EdgeVec* perimeter();

  %newobject integration_points;
  GaussPointVec* integration_points(int);

  MasterCoord center();
  int ncorners();
  ElementNodeIterator node_iterator();
  ElementMapNodeIterator mapnode_iterator();
  ElementFuncNodeIterator *funcnode_iterator();
  ElementCornerNodeIterator cornernode_iterator();
  bool exterior(MasterCoord&, MasterCoord&);
  void set_exterior(Node&, Node&);
  void dump_exterior(); // debugging

  void set_index(int);
  const int get_index() const;
  int shapefun_degree() const;
  int dshapefun_degree() const;
  int mapfun_degree() const;

  // Data retrieval methods.
  int appendData(ElementData *x);
  void setData(int i, ElementData *x);
  void setDataByName(ElementData *x);
  ElementData *getData(int i);
  int getIndexByName(char *name);
  ElementData *getDataByName(char *name);

  //Interface branch
  Node* getCornerNode(int i) const;
  const string &name();
  %newobject namelist;
  StringVec* namelist();

  void refreshMaterial(PyObject *skeletoncontext);

  OutputValue outputField(FEMesh*, Field&, MasterPosition&);
  %newobject outputFields;
  ArithmeticOutputValueVec *outputFields(FEMesh*, Field&, MasterCoordVec*);
  %newobject outputFieldDerivs;
  ArithmeticOutputValueVec *outputFieldDerivs(FEMesh*, Field&, SpaceIndex*,
					      MasterCoordVec*);
  %newobject outputFluxes;
  ArithmeticOutputValueVec *outputFluxes(FEMesh*, Flux&, MasterCoordVec*);

//   void begin_material_computation(FEMesh*);
//   void end_material_computation(FEMesh*);

  Coord from_master(MasterCoord *Point);
  MasterCoord to_master(Coord *Point);
};

ADD_REPR(Element, repr);

%pythoncode "engine/element.spy"

#endif // ELEMENTS_SWG
