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

%module(package="ooflib.SWIG.engine") material

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%include "common/canvasimage.swg"
%import "common/abstractimage.swg"
%import "common/coord.swg"
%import "common/pixelattribute.swg"
%import "common/timestamp.swg"
#endif // NOSECONDIMPORTS

%{
#include "common/ccolor.h"
#include "common/coord.h"
#include "common/pixelgroup.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/material.h"
#include "engine/property.h"
typedef std::string MaterialType;
%}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// get the getMaterial python function

%define GET_GETMATERIAL()
  static PyObject *getMaterial = 0;
  if(!getMaterial) {
    PyObject *module = PyImport_ImportModule("ooflib.engine.materialmanager");
    getMaterial = PyObject_GetAttrString(module, "getMaterial");
    Py_XDECREF(module);
    if(!getMaterial) {
      PyErr_SetString(PyExc_RuntimeError,
		      "in '$symname', could not find 'getMaterial'");
      SWIG_fail;
    }
    Py_XINCREF(getMaterial);
  }
%enddef

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// When a Material* is returned from C++ to Python, the swigged
// Material that's returned isn't the same Python object as the
// Material that was created initially.  This typemap uses the
// Material's name and the MaterialManager to fetch the original
// Material object.

%typemap(out) Material* {
    // typemap(out) Material*
  GET_GETMATERIAL();
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
  GET_GETMATERIAL();
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
  GET_GETMATERIAL();
  $result = PySet_New(NULL);
  for(auto i=$1->begin(); i!=$1->end(); ++i) {
    PyObject *matl = PyObject_CallFunction(getMaterial, "(s)",
					   (*i)->name().c_str());
    // The return value of PyObject_CallFunction is NULL on failure...
    if(!matl)
      SWIG_fail;
    // ... but the return value of PySet_Add is 0 on *success*.
    int status = PySet_Add($result, matl);
    if(status != 0) {
      SWIG_fail;
    }
  }
}

%typemap(newfree) MaterialSet* {
  // typemap(newfree) MaterialSet*
  delete $1;
}

// TODO PYTHON3: Should this be in property.swg?  Would that drag too
// much other stuff into this file?
PYTHONEXPORTABLE(Property);
   
// Convert a std::string& to a MaterialType Enum
// TODO PYTHON3: We should have generic Enum <--> const std::string& typemaps.
%typemap(out) MaterialType {
  // typemap(out) MaterialType
  FETCH_CLASS(ooflib.engine.materialtype, MaterialType)
  $result = PyObject_CallFunction(MaterialTypeClass, "(s)", $1.c_str());
}

%typemap(in) const std::string &MaterialType (std::string mt)
{
  // typemap(in) const std::string &MaterialType
  PyObject *smt = PyObject_CallMethod($input, "string", NULL);
  PyObject *ustr = PyUnicode_AsEncodedString(smt, "UTF-8", "replace");
  mt.assign(PyBytes_AsString(ustr));
  $1 = &mt;
  Py_XDECREF(ustr);
  Py_XDECREF(smt);
}

class CMicrostructure;
class LinearizedSystem;
class PixelSet;
class Property;

class Material {
public:
  //Interface branch
  Material(const std::string& , const std::string &MaterialType);
  ~Material();
  const std::string &name();
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

  // The IC
  void assignToPixels(CMicrostructure*, std::vector<ICoord> *iPointList);
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
  CanvasImage *makeCanvasImage(Coord *Point, Coord *Point);
};

%pythoncode "engine/material.spy"

#endif // MATERIAL_SWG
