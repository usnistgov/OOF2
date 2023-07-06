// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef FEMESH_SWG
#define FEMESH_SWG

%module(package="ooflib.SWIG.engine") femesh

%include "common/typemaps.swg"
%import "common/cmicrostructure.swg"
%import "common/lock.swg"
%import "common/timestamp.swg"
%import "engine/element.swg"
%import "engine/field.swg"
%import "engine/node.swg"
%import "engine/material.swg"
%import "engine/meshiterator.swg"

%{
#include "engine/csubproblem.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/material.h"
#include "engine/meshiterator.h"
#include "engine/nodalequation.h"
#include "engine/node.h"
#include "engine/flux.h"	// SWIGBUG
// typedef VContainer<Node> VContainerNode;
// typedef VContainer<FuncNode> VContainerFuncNode;
// typedef VContainer<Element> VContainerElement;
// typedef VContainer<InterfaceElement> VContainerInterfaceElement;

typedef std::vector<FuncNode*> FuncNodeVector;
%}

%typemap(out) DoubleIteratorFuncNodeNode* {
  unsigned int size1 = $1->vec1.size();
  unsigned int size2 = $1->vec2.size();
  $result = PyList_New((Py_ssize_t) (size1 + size2));
  for(unsigned int i=0; i<size1; i++) {
    PyObject *tmp = $1->vec1[i]->pythonObject(false);
    PyList_SET_ITEM($result, (Py_ssize_t) i, tmp);
  }
  for(unsigned int i=0; i<size2; i++) {
    PyObject *tmp = $1->vec2[i]->pythonObject(false);
    PyList_SET_ITEM($result, (Py_ssize_t)(size1 + 1), tmp);
  }
};

MAKE_LISTVEC_TYPEMAPS(FuncNode);
MAKE_LISTVEC_TYPEMAPS(Element);

class FEMesh {
public:
  FEMesh(CMicrostructure*);
  ~FEMesh();

  void refreshMaterials(PyObject *skeletoncontext);
  void refreshInterfaceMaterials(PyObject *skeletoncontext);
  void addMaterial(Material*);
  void removeMaterial(Material*);
  %newobject getAllMaterials;
  MaterialSet *getAllMaterials();

  Node *newMapNode(Coord&);
  FuncNode *newFuncNode(Coord&);
#ifdef HAVE_MPI
  FuncNode *newFuncNode_shares(Coord&,const std::vector<int>*,const std::vector<int>*,int);
#endif
  Node *getNode(int i);
  FuncNode *getFuncNode(int);
  Node *closestNode(double x, double y);
  void reserveFuncNodes(int);
  void reserveMapNodes(int);

  void addElement(Element*);
  Element *getElement(int i);
  void reserveElements(int);

  int nelements();
  int nnodes();

  void addInterfaceElement(InterfaceElement*);
  int nedgements();
  void renameInterfaceElements(char* oldname, char* newname);

  bool in_plane(Field&);
  void set_in_plane(Field&, bool);

  // %rename(node_iterator) c_node_iterator;
  // %rename(funcnode_iterator) c_funcnode_iterator;
  // %rename(element_iterator) c_element_iterator;
  // %rename(interface_element_iterator) c_interface_element_iterator;
  // VContainerNode* c_node_iterator();
  // VContainerFuncNode* c_funcnode_iterator();
  // VContainerElement* c_element_iterator();
  // VContainerInterfaceElement* c_interface_element_iterator();

  // The FuncNodeRefVec typemap, created by MAKE_LISTVEC_TYPEMAPS,
  // copies a C++ vector of FuncNode pointers into a Python list,
  // without using PythonExportable and without taking ownership of
  // the objects.
  FuncNodeRefVec& funcnode_iterator();
  ElementRefVec& element_iterator();
  InterfaceElementRefVec& interface_element_iterator();
  // TODO: Typemap for DoubleIterator that converts both vectors into
  // a single list.
  %newobject node_iterator;
  DoubleIteratorFuncNodeNode* node_iterator();
  
  void iterator_test_NEW();
  void iterator_test_OLD();
  void iterator_test_double();

  void set_rwlock(RWLock *rw);
  RWLock * get_rwlock();

  void setCurrentTime(double);
  double getCurrentTime();

  void setCurrentSubProblem(CSubProblem*);
  void clearCurrentSubProblem();
  // CSubProblem *getCurrentSubProblem();

  double get_dofvalue(int);
  void dumpDoFs(char*);		// for debugging

  %newobject getFieldSetByID;
  std::vector<std::string> *getFieldSetByID(int);
};				// class FEMesh

long get_globalFEMeshCount();

%pythoncode "engine/femesh.spy"

#endif // FEMESH_SWG
