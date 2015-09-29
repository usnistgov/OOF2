// -*- C++ -*-
// $RCSfile: femesh.swg,v $
// $Revision: 1.93 $
// $Author: reida $
// $Date: 2011/08/11 21:40:35 $

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

%module femesh

%include "engine/typemaps.swg"
%extern "common/cmicrostructure.swg"
%extern "common/lock.swg"
%extern "common/timestamp.swg"
%extern "engine/doublevec.swg"
%extern "engine/element.swg"
%extern "engine/field.swg"
%extern "engine/node.swg"
%extern "engine/meshiterator.swg"

%pragma(python) code="from ooflib.SWIG.engine.field import FieldPtr"
%pragma(python) code="from ooflib.SWIG.common.lock import RWLockPtr"
%pragma(python) code="from ooflib.SWIG.common.lock import LockPtr"
%pragma(python) code="from ooflib.SWIG.engine.meshiterator import NodeIteratorPtr"
%pragma(python) code="from ooflib.SWIG.engine.meshiterator import FuncNodeIteratorPtr"
%pragma(python) code="from ooflib.SWIG.engine.meshiterator import ElementIteratorPtr"

%{
#include "engine/femesh.h"
#include "engine/node.h"
#include "engine/field.h"
#include "engine/nodalequation.h"
#include "engine/meshiterator.h"
#include "engine/csubproblem.h"
%}

%pragma(python) include="femesh.spy"



class FEMesh {
public:
  FEMesh(CMicrostructure*);
  ~FEMesh();


  void refreshMaterials(PyObject *skeletoncontext);
  void refreshInterfaceMaterials(PyObject *skeletoncontext);
  void addMaterial(Material*);
  void removeMaterial(Material*);
  %new MaterialSet *getAllMaterials();

  Node *newMapNode(Coord&);
  FuncNode *newFuncNode(Coord&);
#ifdef HAVE_MPI
  FuncNode *newFuncNode_shares(Coord&,IntVec*,IntVec*,int);
#endif
  Node *getNode(int i);
  FuncNode *getFuncNode(int);
#ifdef DIM_3
  Node *closestNode(double x, double y, double z);
#else
  Node *closestNode(double x, double y);
#endif
  void reserveFuncNodes(int);
  void reserveMapNodes(int);

  void addElement(Element*);
  Element *getElement(int i);
  void reserveElements(int);

  int nelements();
  int nnodes();

  void addInterfaceElement(InterfaceElement*);
  int nedgements();
  ElementIterator edgement_iterator();
  void renameInterfaceElements(char* oldname, char* newname);

  bool in_plane(Field&);
  void set_in_plane(Field&, bool);

  ElementIterator element_iterator();
  NodeIterator node_iterator();
  FuncNodeIterator funcnode_iterator();

  void set_rwlock(RWLock *rw);
  RWLock * get_rwlock();

  void setCurrentTime(double);
  double getCurrentTime();

  void setCurrentSubProblem(CSubProblem*);
  void clearCurrentSubProblem();
  // CSubProblem *getCurrentSubProblem();

  double get_dofvalue(int);
  void dumpDoFs(char*);		// for debugging

  %new StringVec *getFieldSetByID(int);
};				// class FEMesh

long get_globalFEMeshCount();

#endif // FEMESH_SWG
