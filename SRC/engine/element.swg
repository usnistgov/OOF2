// -*- C++ -*-
// $RCSfile: element.swg,v $
// $Revision: 1.24 $
// $Author: reida $
// $Date: 2011/09/01 21:23:38 $


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
%include "engine/typemaps.swg"
%extern "common/coord.swg"
%extern "engine/csubproblem.swg"
%extern "engine/edge.swg"
%extern "engine/femesh.swg"
%extern "engine/field.swg"
%extern "engine/mastercoord.swg"
%extern "engine/outputval.swg"
%pragma(python) code="from ooflib.SWIG.engine.outputval import OutputValuePtr"

%pragma(python) include="element.spy"

%{
#include "engine/element.h"
#include "engine/cskeleton.h"
#include "engine/material.h"
%}

#ifdef DIM_3
%{
#include "vtk-5.0/vtkPythonUtil.h"
#include "vtk-5.0/vtkCell3D.h"
%}
#endif

// VecVec and MasterCoordVec are typedef'd in engine/typemaps.swg
// Likewise GaussPointVec and EdgeVec.


// PythonExportable typemap for ElementData*-returning functions.
// Has the extra-special feature of noticing null-pointer returns
// and translating them to "None".

%typemap(python, out) ElementData* {
  // typemap(python, out) ElementData*
  if ($source != 0) {
    $target = $source->pythonObject();
    if(!$target)
      return 0;
  }
  else
    $target = Py_None;
}

%pragma(python) code="from ooflib.SWIG.engine.elementnodeiterator import *"
%pragma(python) code="from ooflib.SWIG.engine.gausspoint import GaussPointPtr"
%extern "engine/elementnodeiterator.swg"

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

class Element {
public:
  Material *material();
  const MasterElement &masterelement();
  double area();
  BoundaryEdge *getBndyEdge(const FuncNode *, const FuncNode *);
#ifndef DIM_3
  %new EdgeVec* perimeter();
#endif

  %new GaussPointVec* integration_points(int);
  MasterCoord center();
  int ncorners();
  ElementNodeIterator node_iterator();
  ElementMapNodeIterator mapnode_iterator();
  ElementFuncNodeIterator *funcnode_iterator();
  ElementCornerNodeIterator cornernode_iterator();
#ifndef DIM_3
  bool exterior(MasterCoord&, MasterCoord&);
  void set_exterior(Node&, Node&);
  void dump_exterior(); // debugging
#endif

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
  %new StringVec* namelist();

  void refreshMaterial(PyObject *skeletoncontext);

  OutputValue outputField(FEMesh*, Field&, MasterPosition&);
  %new OutputValueVec *outputFields(FEMesh*, Field&, MasterCoordVec*);
  %new OutputValueVec *outputFieldDerivs(FEMesh*, Field&, SpaceIndex*,
					 MasterCoordVec*);
  // OutputValue outputFlux(FEMesh*, Flux&, MasterPosition&);
  %new OutputValueVec *outputFluxes(FEMesh*, Flux&, MasterCoordVec*);

//   void begin_material_computation(FEMesh*);
//   void end_material_computation(FEMesh*);

  Coord from_master(MasterCoord *Point);
  MasterCoord to_master(Coord *Point);

  %addmethods {
#ifdef DIM_3
  // methods needed to access vtk objects so that we can draw the 3D
  // mesh TODO 3D: we should probably be able to eliminate these
  // when meshes use vtk more effectively -- currently only working
  // for linear elements

    int getNumberOfEdges() {
      return self->get_skeleton_element()->getNumberOfEdges();
    }

    PyObject* getEdge(int i) {
      return vtkPythonGetObjectFromPointer( self->get_skeleton_element()->getEdge(i) );
    }

    PyObject* getPointIds() {
      return vtkPythonGetObjectFromPointer( self->get_skeleton_element()->getPointIds() );
    }

    int GetCellType() {
      return self->get_skeleton_element()->getCellType();
    }

    PyObject* GetPoints() {
      return vtkPythonGetObjectFromPointer( self->get_skeleton_element()->getPoints() );
    }
#endif

    %new const string *__repr__() {
      return self->repr();
    }
  } // addmethods
};

%typemap(python,out) EdgeVec*;
%typemap(python,freearg) EdgeVec*;
%typemap(python,out) ElementData*;

#endif // ELEMENTS_SWG
