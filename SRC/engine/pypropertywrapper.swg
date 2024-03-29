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

// Not much has to be done here.  The Python functions which are
// called from the C++ side are defined in pypropertywrapper.spy.
// Authors of extensions should derive new classes from PyFluxProperty
// and/or PyEqnProperty.  The derived classes can define the same
// methods, with the same arguments, as the corresponding C++ classes,
// FluxProperty and EqnProperty.  Almost all methods definitions are
// optional, except for integration_order and constant_in_space, which
// are required.  The default C++ base class method will be used if no
// Python method has been provided.

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
