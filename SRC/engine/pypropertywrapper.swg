// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef PYPROPERTYWRAPPER_SWG
#define PYPROPERTYWRAPPER_SWG

%module(package="ooflib.SWIG.engine") pypropertywrapper

%include "common/typemaps.swg"
%import "engine/element.swg"
%import "engine/property.swg"

%{
#include "engine/pypropertywrapper.h"
  #include "engine/equation.h"	// SWIGBUG
  #include "engine/flux.h"	// SWIGBUG
%}

// Not much has to be done here.  When the C++ code uses a Property
// defined in Python, it calls the methods in pypropertywrapper.C,
// which use the PyObject* passed in to the PyFluxProperty or
// PyEqnProperty constructor to call the Property's Python methods.
// All we need to do here is to swig the constructors and destructors.

class PyFluxProperty : public FluxProperty {
public:
  PyFluxProperty(PyObject*, PyObject*, char *name);
  ~PyFluxProperty();
};

class PyEqnProperty : public EqnProperty {
public:
  PyEqnProperty(PyObject*, PyObject*, char *name);
  ~PyEqnProperty();
};

class PyAuxProperty : public AuxiliaryProperty {
public:
  PyAuxProperty(PyObject*, PyObject*, char*);
  ~PyAuxProperty();
};

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Since PyProperties are spoken to/about from Python, they have
// a simple generic ElementData class with one PyObject* for data.

class PyPropertyElementData : public ElementData {
public:
  PyPropertyElementData(char *name, PyObject *dat);
  // ~PyPropertyElementData();
  PyObject *data();
};

%pythoncode "engine/pypropertywrapper.spy"

#endif // PYPROPERTYWRAPPER_SWG
