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
typedef VContainer<Node> VContainerNode;
typedef VContainer<FuncNode> VContainerFuncNode;
typedef VContainer<Element> VContainerElement;
typedef VContainer<InterfaceElement> VContainerInterfaceElement;

typedef std::vector<FuncNode*> FuncNodeVector;
%}

class FEMesh {
public:
  FEMesh(CMicrostructure*);
  ~FEMesh();

  void refreshMaterials(PyObject *skeletoncontext);
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

  %rename(nodes) c_nodes;
  %rename(funcnodes) c_funcnodes;
  %rename(elements) c_elements;
  %rename(interface_elements) c_interface_elements;
  VContainerNode* c_nodes();
  VContainerFuncNode* c_funcnodes();
  VContainerElement* c_elements();
  VContainerInterfaceElement* c_interface_elements();

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
