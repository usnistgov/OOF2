// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef MATERIAL_SWG
#define MATERIAL_SWG

%module material
%include "common/typemaps.swg"
%import "common/abstractimage.swg"
%import "common/canvasimage.swg"
%import "common/pixelattribute.swg"
%import "common/timestamp.swg"
%import "engine/femesh.swg"

%{
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/material.h"
#include "engine/property.h"
#include "common/pixelgroup.h"
#include "common/ccolor.h"
typedef const std::string MaterialType;
%}

// %pragma(python) code="from ooflib.SWIG.common.abstractimage import AbstractImagePtr"
// %pragma(python) code="from ooflib.SWIG.common.pixelattribute import PxlAttributeRegistrationPtr"
// %pragma(python) code="from ooflib.SWIG.common.timestamp import TimeStampPtr;"

// When a Material* is returned from C++ to Python, the MaterialPtr
// that's returned isn't the same Python object as the Material that
// was created initially.  This typemap uses the Material's name and
// the MaterialManager to fetch the original Material object.

%typemap(out) Material* {
  // typemap(out) Material*
  static PyObject *getMaterial = 0;
  if(!getMaterial) {
    PyObject *module = PyImport_ImportModule("ooflib.engine.materialmanager");
    getMaterial = PyObject_GetAttrString(module, "getMaterial");
    Py_XDECREF(module);
    if(!getMaterial) return 0;
    Py_XINCREF(getMaterial);
  }
  if($1) {
    // call getMaterial()
    $result = PyObject_CallFunction(getMaterial, "(s)", $1->name().c_str());
    // If the material manager can't find the Material, then we're
    // still in the process of building it.  getMaterial will have
    // raised a KeyError, which we clear, and return the unmodified
    // Material object.
    if(!$result) {
      // TODO PYTHON3: Check that there is actually an exception by
      // callding PyErr_Occurred() before PyErr_ExceptionMatches().
      if(PyErr_ExceptionMatches(PyExc_KeyError)) { // we got a KeyError
	PyErr_Clear();
	$result = SWIG_NewPointerObj(SWIG_as_voidptr($1),
				     $descriptor(Material*),
				     0);
      }
      else {			// we got some other error
	$result = 0;
      }
    }
  }
  else {
    Py_INCREF(Py_None);
    $result = Py_None;
  }
}

%{
  typedef std::vector<const Material*> MaterialVec;
%}

%typemap(out) MaterialVec* {
   // typemap(out) MaterialVec*
  static PyObject *getMaterial = 0;
  if(!getMaterial) {
    PyObject *module = PyImport_ImportModule("ooflib.engine.materialmanager");
    getMaterial = PyObject_GetAttrString(module, "getMaterial");
    Py_XDECREF(module);
    if(!getMaterial)
      SWIG_fail;
    Py_XINCREF(getMaterial);
  }
  MaterialVec::size_type sz = $1->size();
  // assert((int)sz >= PY_SSIZE_T_MIN && (int)sz <= PY_SSIZE_T_MAX);
  $result = PyList_New((Py_ssize_t) sz);
  for(std::vector<const Material*>::size_type i=0; i<$1->size(); i++) {
    PyList_SET_ITEM(
       $result, (Py_ssize_t) i,
       PyObject_CallFunction(getMaterial, "(s)", (*$1)[i]->name().c_str()));
  }
}

%typemap(newfree) MaterialVec* {
  // typemap(newfree) MaterialVec*
  delete $1;
}

%{
#include "engine/materialset.h"
#include "engine/material.h"
%}

%typemap(out) MaterialSet* {
   // typemap(out) MaterialSet*
  static PyObject *getMaterial = 0;
  if(!getMaterial) {
    PyObject *module = PyImport_ImportModule("ooflib.engine.materialmanager");
    getMaterial = PyObject_GetAttrString(module, "getMaterial");
    Py_XDECREF(module);
    if(!getMaterial)
      SWIG_fail;
    Py_XINCREF(getMaterial);
  }
  $result = PySet_New(NULL);
  for(auto i=$1->begin(); i!=$1->end(); ++i) {
    PyObject *matl = PyObject_CallFunction(getMaterial, "(s)",
					   (*i)->name().c_str());
    if(!matl)
      SWIG_fail;
    if(!PySet_Add($result, matl))
      SWIG_fail;
  }
}

%typemap(newfree) MaterialSet* {
  // typemap(newfree) MaterialSet*
  delete $1;
}
   
%typemap(out) Property* {
  // typemap(out) Property*
  $result = $1->pythonObject();
  if(!$result)
    SWIG_fail;
}

// Convert a std::string& to a MaterialType Enum
%typemap(out) MaterialType {
  // typemap(out) MaterialType*
  FETCH_CLASS(ooflib.SWIG.engine.material, MaterialType)
  $result = PyObject_CallFunction(MaterialTypeClass, "(s)", $1->c_str());
}

class CMicrostructure;
class LinearizedSystem;
class PixelSet;
class Property;

class Material {
public:
  //Interface branch
  Material(char *name, char* materialtype);
  ~Material();
  const string &name();
  void rename(char *newname);

  //Interface branch
  MaterialType type();

  void add1Property(Property *newprop);
  void remove1Property(Property *oldprop);
  Property *fetchProperty(char *name);
  Property *getProperty(int);
  int nProperties();

  void registerPropertyType(Property *p, char* name);
  void registerFlux(Property*, Flux*);
  void registerEqn(Property*, Equation*);
  void registerOutput(Property*, char*);

  void clear_xref();
  bool self_consistent();
  void set_consistency(bool);
  void cprecompute(CSubProblem*);
  void begin_element(CSubProblem*, Element*);
  void end_element(CSubProblem*, Element*);
  bool contributes_to_flux(Flux*);

  bool cleanAttributes(CMicrostructure*);
  bool replaceAttributes(CMicrostructure*, Material*);

  void assignToPixels(CMicrostructure*, ICoordVec *iPointList);
  void assignToPixelGroup(CMicrostructure*, PixelSet*);
  void assignToAllPixels(CMicrostructure*);
  int nPixelsInMicrostructure(CMicrostructure*);
};

class MaterialAttributeRegistration : public PxlAttributeRegistration {
public:
  MaterialAttributeRegistration();
};

%newobject getMaterials;
MaterialVec *getMaterials(CMicrostructure*);
Material *getMaterialFromCategory(CMicrostructure*, int);
Material *getMaterialFromPoint(CMicrostructure*, ICoord *iPoint);
void removeMaterialFromPixels(CMicrostructure*, PixelSet*);
void removeAllMaterials(CMicrostructure*);
TimeStamp getMaterialTimeStamp(CMicrostructure*);

class MaterialImage : public AbstractImage {
public:
  MaterialImage(CMicrostructure*, CColor*, CColor*);
  %newobject makeCanvasImage;
  CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);
};

%pythoncode "engine/material.spy"

#endif // MATERIAL_SWG
