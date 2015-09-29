// -*- C++ -*-
// $RCSfile: typemaps.swg,v $
// $Revision: 1.53 $
// $Author: lck $
// $Date: 2014/06/25 19:38:09 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// GENERIC TYPEMAPS

// In these comments, "[x]" means a Python list of objects of type x

// DON'T ADD TYPEMAPS TO THIS FILE WITHOUT ADDING THEM TO THIS LIST
// Unnamed typemaps defined in this file:

// in           NodeVec*        [Node] -> std::vector<Node*>*
// in		MasterCoordVec* [MasterCoord] -> std::vector<MasterCoord*>*
// in		PyObjectVec*	[anything] -> std::vector<PyObject*>*
// in		SpaceIndex*	SpaceComponent -> SpaceIndex
// out          GaussPointVec*  std::vector<GaussPoint*> -> [GaussPoint]
// newfree      GaussPointVec*  deletes vector
// out		MasterCoordVec* std::vector<MasterCoord*> -> [MasterCoord]
// newfree      MasterCoordVec* deletes vector
// out		FluxVec*	std::vector<Flux*> -> [Flux derived class obj]
// out		SymmMatrix3StarVec* std::vector<SymmMatrix3*> -> [SymmMatrix3]
// out		Flux*		Flux* -> Flux derived class obj
// out		EdgeVec*	std::vector<Edge*> -> [Edge]
// out		OutputValueVec* std::vector<OutputValue>* -> [OutputVal]
// out		DOUBLELIST*	DOUBLELIST* -> [double]
// newfree      DOUBLELIST*
// out		CompoundFieldVec* std::vector<CompoundField*>* ->[CompoundField]
// out          Material*       returns original Material, not newly wrapped Ptr
// out          MaterialVec*    std::vector<Material*> -> [original Material]
// newfree      MaterialVec*    deletes std::vector
// out          MaterialSet*    std::set<Material*> -> set(original Material)
// newfree      MaterialSet*    deletes std::set

// Named typemaps:
// in		MasterCoord *Point	Point->MasterCoord

// Obsolete typemaps, commented out below:
// out		VecVec*		std::vector<std::vector<double>*> -> [[Float]]
// newfree      VecVec*         deletes vector
// out		DoubleStarVec*  std::vector<const double*> -> [Float]

#ifndef ENGINETYPEMAPS_SWG
#define ENGINETYPEMAPS_SWG

%include "common/typemaps.swg"


// Typemap for converting a std::vector<GaussPoint*> to a Python list
// of GaussPointPtr objects.  Python takes ownership of the objects.

%{
#include "engine/gausspoint.h"
typedef std::vector<GaussPoint*> GaussPointVec;
%}

%typemap(python,out) GaussPointVec* {
  // typemap(python,out) GaussPointVec*
  static PyObject *gaussPointClass = 0;
  static PyObject *pyOne;
  if(!gaussPointClass) {
    PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.gausspoint");
    gaussPointClass = PyObject_GetAttrString(module, "GaussPointPtr");
    Py_XDECREF(module);
    if(!gaussPointClass) return 0;
    pyOne = PyInt_FromLong(1);
  }
  GaussPointVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  char _ptemp[128];
  for(std::vector<GaussPoint*>::size_type i=0; i<sz; i++) {
    // Create wrapped swig object.
    SWIG_MakePtr(_ptemp, (char*)(*$source)[i], "_GaussPoint_p");
    PyObject *swigthis = Py_BuildValue("(s)", _ptemp);
    PyObject *gp = PyObject_CallObject(gaussPointClass, swigthis);
    Py_XDECREF(swigthis);
    // Take ownership
    PyObject_SetAttrString(gp, "thisown", pyOne);
    // Put it in the list.
    PyList_SET_ITEM($target, (Py_ssize_t) i, gp); // Steals reference.
  }
}

%typemap(python,newfree) GaussPointVec* {
  // typemap(python,newfree) GaussPointVec*
  delete $source;
}


// Typemap for converting a std::vector<MasterCoord*> to a List of
// MasterCoords. Python takes over ownership of the MasterCoords.
%{
#include "engine/mastercoord.h"
#include <vector>
  typedef std::vector<MasterCoord*> MasterCoordVec;
%}

%typemap(python,out) MasterCoordVec* {
  // typemap(python,out) MasterCoordVec*
  static PyObject *masterCoordClass = 0;
  static PyObject *pyOne = 0;
  if(!masterCoordClass) {
    PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.elements");
    masterCoordClass = PyObject_GetAttrString(module, "MasterCoordPtr");
    Py_XDECREF(module);
    if(!masterCoordClass) return 0;
    pyOne = PyInt_FromLong(1);
  }
  MasterCoordVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  char _ptemp[128];
  for(std::vector<MasterCoord*>::size_type i=0; i<sz; i++) {
    // Create wrapped swig object
    SWIG_MakePtr(_ptemp, (char*)(*$source)[i], "_MasterCoord_p");
    PyObject *swigthis = Py_BuildValue("(s)", _ptemp);
    PyObject *mc = PyObject_CallObject(masterCoordClass, swigthis);
    Py_XDECREF(swigthis);
    // take ownership
    PyObject_SetAttrString(mc, "thisown", pyOne);
    // put it in the list
    PyList_SET_ITEM($target, (Py_ssize_t) i, mc);
  }
}

%typemap(python, newfree) MasterCoordVec* {
  // typemap(python, newfree) MasterCoordVec*
  delete $source;
}

%typemap(python, in) MasterCoordVec* (MasterCoordVec mcv) {
  // typemap(python, in) MasterCoordVec*
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
		    "Error in MasterCoordVec* typemap.  Python list required.");
    return NULL;
  }
  MasterCoordVec::size_type sz = Py_SAFE_DOWNCAST(PyList_Size($source),
						  Py_ssize_t,
						  MasterCoordVec::size_type);
  mcv.resize(sz);
  for(MasterCoordVec::size_type i=0; i<sz; i++) {
    MasterCoord *mc;
    PyObject *stg = PyObject_GetAttrString(PyList_GET_ITEM($source,
							   (Py_ssize_t) i),
					   "this");
    if(!stg)
      return NULL;
    char *str = PyString_AsString(stg);
    SWIG_GetPtr(str, (void**)&mc, "_MasterCoord_p");
    mcv[i] = mc;
  }
  $target = &mcv;
}

%{
  typedef std::vector<PyObject*> PyObjectVec;
%}

%typemap(python, in) PyObjectVec* (PyObjectVec pov) {
  // typemap(python, in) PyObjectVec*
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
		    "Error in PyObjectVec* typemap.  Python list required.");
    return NULL;
  }
  PyObjectVec::size_type sz = Py_SAFE_DOWNCAST(PyList_Size($source),
					       Py_ssize_t,
					       PyObjectVec::size_type);
  pov.resize(sz);
  for(PyObjectVec::size_type i=0; i<sz; i++) {
    pov[i] = PyList_GET_ITEM($source, (Py_ssize_t) i);
  }
  $target = &pov;
}

// // Typemap for converting a std::vector<std::vector<double>*> to a
// // List of Lists of Floats.
// %{
//   typedef std::vector<std::vector<double>*> VecVec;
// %}

// %typemap(python, out) VecVec* {
//   // typemap(python, out) VecVec*
//   VecVec::size_type sz = $source->size();
//   assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
//   $target = PyList_New((Py_ssize_t) sz);
//   for(std::vector<std::vector<double>*>::size_type i=0; i<sz; i++) {
//     std::vector<double>::size_type dofs = (*$source)[i]->size();
//     PyObject *sublist = PyList_New((Py_ssize_t) dofs);
//     for(std::vector<double>::size_type j=0; j<dofs; j++) {
//       PyList_SET_ITEM(sublist, (Py_ssize_t) j,
// 		      PyFloat_FromDouble( (*(*$source)[i])[j] ) );
//     }
//     PyList_SET_ITEM($target, (Py_ssize_t) i, sublist);
//   }
// }

// %typemap(python, newfree) VecVec* {
//   // typemap(python, newfree) VecVec*
//   for(std::vector<std::vector<double>*>::size_type i=0;i<$source->size();i++) {
//     delete (*$source)[i];
//   }
//   delete $source;
// }

// // Typemap for converting a std::vector<double*> to a List of Floats.
// %{
//   typedef std::vector<const double*> DoubleStarVec;
// %}

// %typemap(python, out) DoubleStarVec* {
//   // typemap(python, out) DoubleStarVec*
//   DoubleStarVec::size_type sz = $source->size();
//   assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
//   $target = PyList_New((Py_ssize_t) sz);
//   for(std::vector<const double*>::size_type i=0; i<sz; i++) {
//     PyList_SET_ITEM($target, (Py_ssize_t) i,
// 		    PyFloat_FromDouble(*(*$source)[i]));
//   }
// }

// %typemap(python, newfree) DoubleStarVec* {
//   // typemap(python, newfree) DoubleStarVec*
//   for(std::vector<const double*>::size_type i=0; i<$source->size(); i++)
//     delete (*$source)[i];
//   delete $source;
// }

%{
#include "engine/symmmatrix.h"
  typedef std::vector<SymmMatrix3*> SymmMatrix3StarVec;
%}

// Convert a vector of SymmMatrix3* objects to a list of
// SymmMatrix3Ptr objects.  The ownership of the swigged objects is
// transferred to Python, so the associated newfree typemap (below)
// doesn't have to delete the members of the vector, unlike the
// DoubleStarVec newfree typemap (above).
%typemap(python, out) SymmMatrix3StarVec* {
  // typemap(python, out) SymmMatrix3StarVec*
  static PyObject *symmMatrix3Class = 0;
  static PyObject *pyOne = 0;
  if(!symmMatrix3Class) {
    PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.symmmatrix");
    symmMatrix3Class = PyObject_GetAttrString(module, "SymmMatrix3Ptr");
    Py_XDECREF(module);
    if(!symmMatrix3Class) return 0;
    pyOne = PyInt_FromLong(1);
  }
  SymmMatrix3StarVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  char _ptemp[128];
  for(std::vector<SymmMatrix3*>::size_type i=0; i<sz; i++) {
    SWIG_MakePtr(_ptemp, (char*)((*$source)[i]), "_SymmMatrix3_p");
    PyObject *swigthis = Py_BuildValue("(s)", _ptemp);
    PyObject *sm3 = PyObject_CallObject(symmMatrix3Class, swigthis);
    Py_XDECREF(swigthis);
     // Set SymmMatrix3Ptr.thisown = 1 to transfer ownership.
     PyObject_SetAttrString(sm3, "thisown", pyOne);

     PyList_SET_ITEM($target, (Py_ssize_t) i, sm3);
  }
}

%typemap(python, newfree) SymmMatrix3StarVec* {
  // typemap(python, newfree), SymmMatrix3StarVec*
  // Don't delete the contents of the vector, because Python owns them
  // and will delete them itself.
  delete $source;
}


%typemap(python, in) MasterCoord *Point (MasterCoord mc) {
  // typemap(python, in) MasterCoord *Point
  PyObject *xobj = PySequence_GetItem($source, 0);
  PyObject *yobj = PySequence_GetItem($source, 1);
#ifdef DIM_3
  PyObject *zobj = PySequence_GetItem($source, 2);
  if(!xobj || !yobj || !zobj) {
    PyErr_SetString(PyExc_TypeError, "Type error in MasterCoord *Point typemap.  Argument must have 0, 1, and 2 components.");
    return NULL;
  }
#else
  if(!xobj || !yobj) {
    PyErr_SetString(PyExc_TypeError, "Type error in MasterCoord *Point typemap.  Argument must have 0 and 1 components.");
    return NULL;
  }
#endif

  mc(0) = PyFloat_AsDouble(xobj);
  mc(1) = PyFloat_AsDouble(yobj);
  Py_XDECREF(xobj);
  Py_XDECREF(yobj);
#ifdef DIM_3
  mc(2) = PyFloat_AsDouble(zobj);
  Py_XDECREF(zobj);
#endif
  $target = &mc;
}



// Typemap for converting a list of nodes to a standard
// template vector.

%{
#include <vector>
#include "engine/node.h"
  typedef std::vector<Node*> NodeVec;
%}

%typemap(python, in) NodeVec * (NodeVec n) {
  // typemap(python, in) NodeVec*
  if(!PyList_Check($source)) {
    PyErr_SetString(PyExc_TypeError,
		    "Type Error in NodeVec typemap.  Python list required.");
    return NULL;
  }
  NodeVec::size_type sz = Py_SAFE_DOWNCAST(PyList_Size($source),
					   Py_ssize_t,
					   NodeVec::size_type);
  n.resize(sz);
  for(NodeVec::size_type i=0; i<sz; i++) {
    Node *tnode;
    PyObject *stg = PyObject_GetAttrString(PyList_GET_ITEM($source,
							   (Py_ssize_t) i),
					   "this");
    if(!stg)
      return NULL;
    char *str = PyString_AsString(stg);
    SWIG_GetPtr(str, (void **)&tnode, "_CSkeletonNode_p");
    n[i] = tnode;
  }

  $target = &n;
}

%typemap(python, out) Node* {
  // typemap(python, out) Node*
  $target = $source->pythonObject();
  if(!$target)
    return 0;
}


////////////////////////////////

// The CompoundFieldVec* typemap converts a std::vector of
// CompoundField*s to a Python list of CompoundFields.  It does *not*
// use the PythonExportable mechanism because the Field class uses too
// much virtual inheritance for PythonExportable to work properly.
// The typemap instead extracts Field names and calls the Python
// getField function (defined in field.spy).

%{
#include <vector>
#include "engine/field.h"
  typedef std::vector<CompoundField*> CompoundFieldVec;
%}

%typemap(python, out) CompoundFieldVec * {
  // typemap(python, out) CompoundFieldVec*
  static PyObject *getField = 0;
  if(!getField) {
    PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.field");
    getField = PyObject_GetAttrString(module, "getField");
    Py_XDECREF(module);
    if(!getField) return 0;
  }
  CompoundFieldVec::size_type sz = $source->size();
  assert((int) sz >= PY_SSIZE_T_MIN && (int) sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(std::vector<CompoundField*>::size_type i=0; i<sz; i++) {
    PyObject *arg = Py_BuildValue("(s)", (*$source)[i]->name().c_str() );
    PyObject *fldobj = PyObject_CallObject(getField, arg);
    Py_XDECREF(arg);
    arg = Py_BuildValue("O", fldobj);
    PyList_SET_ITEM($target, (Py_ssize_t) i, arg);
  }
}

%typemap(python, newfree) CompoundFieldVec * {
  // typemap(python, newfree) CompoundFieldVec*
  delete $source;
}

////////////////////////////

// Equations and Fluxes are PythonExportable, unlike Fields, so the
// typemap for vectors of them is simpler.

%{
#include <vector>
#include "engine/equation.h"
  typedef std::vector<Equation*> EquationVec;
%}

%typemap(python, out) EquationVec * {
  // typemap(python, out) EquationVec*
  EquationVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(std::vector<Equation*>::size_type i=0; i<sz; i++) {
    // pythonObject() returns a new reference and PyList_SET_ITEM steals it.
    PyObject *eqn = (*$source)[i]->pythonObject();
    if(!eqn)
      return 0;
    PyList_SET_ITEM($target, (Py_ssize_t) i, eqn);
  }
}

%typemap(python, newfree) EquationVec * {
  // typemap(python, newfree) EquationVec*
  delete $source;
}


%{
#include <vector>
#include "engine/flux.h"
  typedef std::vector<Flux*> FluxVec;
%}

%typemap(python, out) Flux* {
  // typemap(python, out) Flux*
  $target = $source->pythonObject();
  if(!$target)
    return 0;
}

%typemap(python, out) FluxVec * {
  // typemap(python, out) FluxVec*
  FluxVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(FluxVec::size_type i=0; i<sz; i++) {
    PyObject *flux = (*$source)[i]->pythonObject();
    if(!flux)
      return 0;
    PyList_SET_ITEM($target, (Py_ssize_t) i, flux);
  }
}

%typemap(python, newfree) FluxVec * {
  // typemap(python, newfree) FluxVec*
  delete $source;
}


%{
#include "engine/edge.h"
  typedef std::vector<Edge*> EdgeVec;
%}

/* Need to take the EdgeVec's out with a copy-out typemap. */
   
%typemap(python,out) EdgeVec* {
  // typemap(python, out) EdgeVec*
  static PyObject *edgeClass = 0;
  static PyObject *pyOne = 0;
  if(!edgeClass) {
    PyObject *module = PyImport_ImportModule("ooflib.SWIG.engine.edge");
    edgeClass = PyObject_GetAttrString(module, "EdgePtr");
    Py_XDECREF(module);
    if(!edgeClass) return 0;
    pyOne = PyInt_FromLong(1);
  }
  EdgeVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  char _ptemp[128];
  for(std::vector<Edge*>::size_type i=0; i<sz; i++) {
    // Create a wrapped swig EdgePtr obejct.
    SWIG_MakePtr(_ptemp, (char*)(*$source)[i], "_Edge_p");
    PyObject *swigthis = Py_BuildValue("(s)", _ptemp);
    PyObject *edge = PyObject_CallObject(edgeClass, swigthis);
    Py_XDECREF(swigthis);
    // Take ownership.
    PyObject_SetAttrString(edge, "thisown", pyOne);
    // Put it in the list.
    PyList_SET_ITEM($target, (Py_ssize_t) i, edge);
  }
}

%typemap(python,newfree) EdgeVec* {
  // typemap(python, newfree) EdgeVec*
  delete $source;
}

// The OutputValueVec typemap converts a std::vector of OutputValues
// to a list of PythonExportable OutputVal subclasses, and hands
// ownership of the objects to Python.

%{
  typedef std::vector<OutputValue> OutputValueVec;
%}

%typemap(python, out) OutputValueVec* {
  // typemap(python, out) OutputValueVec*
  static PyObject *pyOne = 0;
  if(!pyOne) {
    pyOne = PyInt_FromLong(1);
  }
  OutputValueVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(OutputValueVec::size_type i=0; i<sz; i++) {
    // Don't use valuePtr() or valueRef() here, because the OutputVals
    // copied into the Python list will outlive the OutputValues that
    // they're copied from.  valueClone() makes an independent copy.
    PyObject *obj = (*$source)[i].valueClone()->pythonObject();
    if(!obj)
      return 0;
    PyObject_SetAttrString(obj, "thisown", pyOne); // take ownership
    PyList_SET_ITEM($target, (Py_ssize_t) i, obj);
  }
}

%typemap(python, newfree) OutputValueVec* {
  // typemap(python, newfree) OutputValueVec*
  delete $source;
}

// Convert any Python Enum type (particularly a SpaceComponent) to a
// SpaceIndex.

%typemap(python, in) SpaceIndex* (SpaceIndex idx) {
  // typemap(python, in) SpaceIndex*
  PyObject *pyindex = PyObject_CallMethod($source,(char*) "index", 0);
  idx = PyInt_AsLong(pyindex);
  Py_XDECREF(pyindex);
  $target = &idx;
}

//////////

// When a Material* is returned from C++ to Python, the MaterialPtr
// that's returned isn't the same Python object as the Material that
// was created initially.  This typemap uses the Material's name and
// the MaterialManager to fetch the original Material object.

%typemap(python, out) Material* {
  // typemap(python, out) Material*
  static PyObject *getMaterial = 0;
  if(!getMaterial) {
    PyObject *module = PyImport_ImportModule("ooflib.engine.materialmanager");
    getMaterial = PyObject_GetAttrString(module, "getMaterial");
    Py_XDECREF(module);
    if(!getMaterial) return 0;
    Py_XINCREF(getMaterial);
  }
  if($source) {
    PyObject *arglist = Py_BuildValue("(s)", $source->name().c_str());
    $target = PyEval_CallObject(getMaterial, arglist); // call getMaterial()
    Py_XDECREF(arglist);
    // If the material manager can't find the Material, then we're
    // still in the process of building it.  getMaterial will have
    // raised a KeyError, which we clear, and return the unmodified
    // Material object.
    if(!$target) {
      if(PyErr_ExceptionMatches(PyExc_KeyError)) { // we got a KeyError
	PyErr_Clear();
	char _ptemp[128];
	SWIG_MakePtr(_ptemp, (char*) $source, "_Material_p");
	$target = Py_BuildValue("s", _ptemp);
      }
      else {			// we got some other error
	$target = 0;
      }
    }
  }
  else {
    Py_INCREF(Py_None);
    $target = Py_None;
  }
}

%{
  typedef std::vector<const Material*> MaterialVec;
%}

%typemap(python, out) MaterialVec* {
   // typemap(python, out) MaterialVec*
  static PyObject *getMaterial = 0;
  if(!getMaterial) {
    PyObject *module = PyImport_ImportModule("ooflib.engine.materialmanager");
    getMaterial = PyObject_GetAttrString(module, "getMaterial");
    Py_XDECREF(module);
    if(!getMaterial) return 0;
    Py_XINCREF(getMaterial);
  }
  MaterialVec::size_type sz = $source->size();
  assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $target = PyList_New((Py_ssize_t) sz);
  for(std::vector<const Material*>::size_type i=0; i<$source->size(); i++) {
    PyObject *name = Py_BuildValue("(s)", (*$source)[i]->name().c_str());
    PyList_SET_ITEM($target, (Py_ssize_t) i, 
		    PyEval_CallObject(getMaterial, name));
    Py_XDECREF(name);
  }
}

%typemap(python, newfree) MaterialVec* {
  // typemap(python, newfree) MaterialVec*
  delete $source;
}

%{
#include "engine/materialset.h"
#include "engine/material.h"
%}

%typemap(python, out) MaterialSet* {
   // typemap(python, out) MaterialSet*
  static PyObject *getMaterial = 0;
  if(!getMaterial) {
    PyObject *module = PyImport_ImportModule("ooflib.engine.materialmanager");
    getMaterial = PyObject_GetAttrString(module, "getMaterial");
    Py_XDECREF(module);
    if(!getMaterial) return 0;
    Py_XINCREF(getMaterial);
  }
  // Python 2.4 has a set() object but no API for it, so this is
  // written using generic function calls.  If we stop supporting 2.4,
  // then the commented out code should be used instead.
  static PyObject *setType = 0;
  if(!setType) {
    PyObject *module = PyImport_ImportModule("__builtin__");
    setType = PyObject_GetAttrString(module, "set");
    Py_XDECREF(module);
    if(!setType) return 0;
    Py_XINCREF(setType);
  }
  $target = PyObject_CallObject(setType, NULL);
  for(std::set<const Material*, MaterialCompare>::iterator i=$source->begin();
      i!=$source->end(); ++i)
    {
      PyObject *name = Py_BuildValue("(s)", (*i)->name().c_str());
      PyObject *matl = PyEval_CallObject(getMaterial, name);
      Py_XDECREF(name);
      if(!matl) return 0;
      if(!PyObject_CallMethod($target,(char*) "add",(char*) "O", matl))
	return 0;
    }
}

%typemap(python, newfree) MaterialSet* {
  // typemap(python, newfree) MaterialSet*
  delete $source;
}

#endif // ENGINETYPEMAPS_SWG
