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

%module(package="ooflib.SWIG.engine") element

// Because Element has methods that return these iterators by value
// and they don't have default constructors, we have to make sure that
// swig uses the value wrapper mechanism.  It's supposed to realized
// that automatically, but somehow isn't.  These lines apparently must
// precede the importation of the class definitions.
%feature("valuewrapper") ElementNodeIterator;
%feature("valuewrapper") ElementMapNodeIterator;
%feature("valuewrapper") ElementCornerNodeIterator;

%include "common/typemaps.swg"
%import "common/coord.swg"
%import "engine/csubproblem.swg"
%import "engine/edge.swg"
%import "engine/elementnodeiterator.swg"
%import "engine/femesh.swg"
%import "engine/field.swg"
%import "engine/gausspoint.swg"
%import "engine/indextypes.swg"
%import "engine/mastercoord.swg"
%import "engine/material.swg"
%import "engine/node.swg"
%import "engine/outputval.swg"

%{
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/cskeleton.h"
#include "engine/material.h"
#include "engine/outputval.h"
#include "engine/mastercoord.h"
  #include "engine/flux.h"	// SWIGBUG
%}

PYTHONEXPORTABLE(ElementData);
MAKE_LISTVEC_TYPEMAPS(Edge);
MAKE_LISTVEC_TYPEMAPS(MasterCoord);

class Material;
class ElementNodeIterator;
class ElementMapNodeIterator;
class ElementFuncNodeIterator;
class MasterElement;
class MasterPosition;
class CSkeletonElement;

// Base class for data objects stored in the element.
%nodefaultctor ElementData;
class ElementData {
public:
  const std::string &name();
};

%nodefaultctor Element;

class Element {
public:
  Material *material();
  const MasterElement &masterelement();
  double area();
  BoundaryEdge *getBndyEdge(const FuncNode *, const FuncNode *);
  %newobject perimeter;
  EdgeVec* perimeter();

  GaussPointIntegrator integrator(int);

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
  int get_index() const;
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
  const std::string &name();
  %newobject namelist;
  std::vector<std::string> *namelist();

  void refreshMaterial(PyObject*);

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

%pythoncode %{
def _Element__position(self, coords):
  return list(map(self.from_master, coords))

Element.position = _Element__position
%}

#endif // ELEMENTS_SWG
