// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/coord.h"
#include "common/oofswigruntime.h"
#include "common/pythonlock.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/outputval.h"
#include "engine/pypropertywrapper.h"
#include "engine/smallsystem.h"

//=\\=//=\\=//

// Create a new swigged object from a pointer of the given type.
// Don't include the "*" in the type, it's added automatically.

#define NEWSWIGPTR(ptr, type) SWIG_NewPointerObj(SWIG_as_voidptr(ptr), SWIG_Python_TypeQuery(type "*"), 0)

//=\\=//=\\=//

PyPropertyMethods::PyPropertyMethods(PyObject *referent)
  : referent_(referent)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_INCREF(referent_);
}

PyPropertyMethods::~PyPropertyMethods() {
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_DECREF(referent_);
}

//=\\=//=\\=//

void PyPropertyMethods::py_precompute(Property *prop, FEMesh *mesh) {
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "precompute")) {
    // The function isn't defined in the derived class.  Call the
    // base class method instead.
    PyErr_Clear();
    prop->Property::precompute(mesh);
  }
  else {
    PyObject *method = PyUnicode_FromString("precompute");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *result = PyObject_CallMethodObjArgs(
				    referent_, method, meshp, NULL);
    Py_XDECREF(meshp);
    if(result==NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyPropertyMethods::py_cross_reference(Property *prop, Material *mat) {
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, (char*) "cross_reference")) {
    prop->Property::cross_reference(mat);
  }
  else {
    PyObject *method = PyUnicode_FromString("cross_reference");
    PyObject *matp = NEWSWIGPTR(mat, "Material");
    PyObject *result = PyObject_CallMethodObjArgs(referent_, method, matp,
						  NULL);
    Py_XDECREF(method);
    Py_XDECREF(matp);
    if(result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyPropertyMethods::py_begin_element(Property *prop, const CSubProblem *m,
					 const Element *el)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "begin_element")) {
    prop->Property::begin_element(m, el);
  }
  else {
    PyObject *method = PyUnicode_FromString("begin_element");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *subp = NEWSWIGPTR(m, "CSubProblem");
    PyObject *result = PyObject_CallMethodObjArgs(referent_, method, subp, elp,
						  NULL);
    Py_XDECREF(method);
    Py_XDECREF(elp);
    Py_XDECREF(subp);
    if(result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

void PyPropertyMethods::py_end_element(Property *prop, const CSubProblem *m,
				       const Element *el)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "end_element")) {
    prop->Property::end_element(m, el);
  }
  else {
    PyObject *method = PyUnicode_FromString("end_element");
    PyObject *subp = NEWSWIGPTR(m, "CSubProblem");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *result = PyObject_CallMethodObjArgs(referent_, method, subp, elp,
						  NULL);
    Py_XDECREF(method);
    Py_XDECREF(subp);
    Py_XDECREF(elp);
    if(result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyFluxProperty::begin_point(const FEMesh *m, const Element *el,
				 const Flux *flx, const MasterPosition &mpos) 
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "begin_point")) {
    this->FluxProperty::begin_point(m, el, flx, mpos);
  }
  else {
    PyObject *method = PyUnicode_FromString("begin_point");
    PyObject *meshp = NEWSWIGPTR(m, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *flxp = NEWSWIGPTR(flx, "Flux");
    PyObject *mpp = NEWSWIGPTR(&mpos, "MasterPosition");
    PyObject *result = PyObject_CallMethodObjArgs(referent_, method,
						  meshp, elp, flxp, mpp, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(flxp);
    Py_XDECREF(mpp);
    if(result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

void PyFluxProperty::end_point(const FEMesh *m, const Element *el,
			       const Flux *flx, const MasterPosition &mpos) 
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "end_point")) {
    this->FluxProperty::end_point(m, el, flx, mpos);
  }
  else {
    PyObject *method = PyUnicode_FromString("end_point");
    PyObject *meshp = NEWSWIGPTR(m, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *flxp = NEWSWIGPTR(flx, "Flux");
    PyObject *mpp = NEWSWIGPTR(&mpos, "MasterPosition");
    PyObject *result = PyObject_CallMethodObjArgs(referent_, method,
						  meshp, elp, flxp, mpp, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(flxp);
    Py_XDECREF(mpp);
    if(result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyPropertyMethods::py_post_process(const Property *prop, CSubProblem *m,
					const Element *el)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "post_process")) {
    prop->Property::post_process(m, el);
  }
  else {
    PyObject *method = PyUnicode_FromString("post_process");
    PyObject *subp = NEWSWIGPTR(m, "CSubProblem");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *result = PyObject_CallMethodObjArgs(referent_, method, subp, elp,
						  NULL);
    Py_XDECREF(subp);
    Py_XDECREF(elp);
    Py_XDECREF(method);
    if(result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

// The PyPropertyMethods::py_output function is a bit different than
// the others, because it uses the returned value.  The C++ and Python
// signatures are different: in C++ a pointer to an OutputVal is
// passed in and the OutputVal is changed by the derived class
// function, which returns void.  In Python, the OutputVal is
// returned.

void PyPropertyMethods::py_output(Property *prop,
				  FEMesh *mesh, const Element *el,
				  const PropertyOutput *propout,
				  const MasterPosition &pos,
				  OutputVal *oval)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "output")) {
    prop->Property::output(mesh, el, propout, pos, oval);
  }
  else {
    PyObject *method = PyUnicode_FromString("output");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *propp = NEWSWIGPTR(propout, "PropertyOutput");
    PyObject *posp = NEWSWIGPTR(&pos, "MasterPosition");

    PyObject *result = PyObject_CallMethodObjArgs(referent_, method,
						  meshp, elp, propp, posp,
						  NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(propp);
    Py_XDECREF(posp);
    if(result == NULL)
      pythonErrorRelay();

    if(result != Py_None) {	// TODO PYTHON3: Do we need this check?
      // Convert result to a C++ object
      OutputVal *cresult;
      if(!SWIG_IsOK(SWIG_ConvertPtr(result, (void**) &cresult,
				    ((SwigPyObject*) result)->ty, 0)))
	{
	  throw ErrProgrammingError(
			    "Python output() does not return an OutputVal",
			    __FILE__, __LINE__);
	}
      *oval = *cresult;
    }
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

bool PyPropertyMethods::py_constant_in_space(const Property *prop) const {
  bool c_result;
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "constant_in_space")) {
    throw ErrUserError("constant_in_space method is missing from Property "
		       + prop->name());
  }
  // TODO: Use PyObject_CallMethodNoArgs in Python 3.9 and later
  PyObject *method = PyUnicode_FromString("constant_in_space");
  PyObject *result = PyObject_CallMethodObjArgs(referent_, method, NULL);
						
  Py_XDECREF(method);
  if(result == NULL) {
    pythonErrorRelay();
  }
  c_result = PyObject_IsTrue(result);
  Py_XDECREF(result);
  return c_result;
}

//=\\=//=\\=//

bool PyPropertyMethods::is_symmetric_K(const Property *prop,
				       const CSubProblem *subp)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "is_symmetric_K")) {
    return prop->Property::is_symmetric_K(subp);
  }
  PyObject *method = PyUnicode_FromString("is_symmetric_K");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *result = PyObject_CallMethodObjArgs(referent_, method,
						subpp, NULL);
  Py_XDECREF(method);
  Py_XDECREF(subpp);
  if(result == NULL) {
    pythonErrorRelay();
  }
  bool c_result = PyObject_IsTrue(result);
  Py_XDECREF(result);
  return c_result;
}

bool PyPropertyMethods::is_symmetric_C(const Property *prop,
				       const CSubProblem *subp)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, (char*) "is_symmetric_C")) {
    return prop->Property::is_symmetric_C(subp);
  }
  PyObject *method = PyUnicode_FromString("is_symmetric_C");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *result = PyObject_CallMethodObjArgs(referent_, method, subpp,
						NULL);
  Py_XDECREF(method);
  Py_XDECREF(subpp);
  if(result == NULL) {
    pythonErrorRelay();
  }
  bool c_result = PyObject_IsTrue(result);
  Py_XDECREF(result);
  return c_result;
}

bool PyPropertyMethods::is_symmetric_M(const Property *prop,
				       const CSubProblem *subp)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "is_symmetric_M")) {
    return prop->Property::is_symmetric_M(subp);
  }
  PyObject *method = PyUnicode_FromString("is_symmetric_M");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *result = PyObject_CallMethodObjArgs(referent_, method, subpp, NULL);
  Py_XDECREF(method);
  Py_XDECREF(subpp);
  if(result == NULL) {
    pythonErrorRelay();
  }
  bool c_result = PyObject_IsTrue(result);
  Py_XDECREF(result);
  return c_result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

int PyPhysicalPropertyMethods::py_integration_order(
					    PyObject *referent,
					    const PhysicalProperty *prop,
					    const CSubProblem *subp, 
					    const Element *el)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "integration_order")) {
    throw ErrUserError("integration_order method is missing from Property " 
		       + prop->name());
  }
  PyObject *method = PyUnicode_FromString("integration_order");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *elp = NEWSWIGPTR(el, "Element");
  PyObject *result = PyObject_CallMethodObjArgs(referent, method, subpp, elp,
						NULL);
  Py_XDECREF(method);
  Py_XDECREF(subpp);
  Py_XDECREF(elp);
  if(result==NULL)
    pythonErrorRelay();
  int c_result = PyInt_AsLong(result);
  Py_XDECREF(result);
  return c_result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Note that "regstn" is the registration entry of the property to 
// which the wrapper refers, not that of the wrapper itself.

// The "PythonNative" parent object holds a pointer to the referent
// Python object, and uses it to answer questions about the type of 
// object and so forth.  Because of this, we probably don't have to 
// do indirection on the repr's.

PyFluxProperty::PyFluxProperty(PyObject *referent, PyObject *regstn,
			       const std::string &name)
  : PythonNative<Property>(referent),
    FluxProperty(name, regstn),
    PyPropertyMethods(referent)
{}

PyFluxProperty::~PyFluxProperty() {}

//=\\=//=\\=//

void PyFluxProperty::flux_matrix(const FEMesh *mesh,
				 const Element *el,
				 const ElementFuncNodeIterator &efni,
				 const Flux *flux,
				 const MasterPosition &gpt,
				 double time,
				 SmallSystem *fluxdata)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "flux_matrix")) {
    this->FluxProperty::flux_matrix(mesh, el, efni, flux, gpt, time, fluxdata);
  }
  else {
    PyObject *method = PyUnicode_FromString("flux_matrix");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *mpp = NEWSWIGPTR(&gpt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *result = PyObject_CallMethodObjArgs(
	  referent_, method,
	  meshp, elp, efnip, fluxp, mpp, timep, fluxdatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(efnip);
    Py_XDECREF(fluxp);
    Py_XDECREF(mpp);
    Py_XDECREF(timep);
    Py_XDECREF(fluxdatap);
    if(result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyFluxProperty::flux_value(const FEMesh *mesh,
				const Element *element,
				const Flux *flux, 
				const MasterPosition &pt,
				double time, 
				SmallSystem *fluxdata)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "flux_value")) {
    this->FluxProperty::flux_value(mesh, element, flux, pt, time, fluxdata);
  }
  else {
    PyObject *method = PyUnicode_FromString("flux_value");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *result = PyObject_CallMethodObjArgs(referent_, method,
						  meshp, elp, fluxp, mpp, timep,
						  fluxdatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(fluxp);
    Py_XDECREF(mpp);
    Py_XDECREF(fluxdatap);
    if(result == NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyFluxProperty::static_flux_value(const FEMesh *mesh,
				       const Element *element,
				       const Flux *flux, 
				       const MasterPosition &pt,
				       double time, 
				       SmallSystem *fluxdata)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "static_flux_value")) {
    this->FluxProperty::static_flux_value(mesh, element, flux, pt, time,
					  fluxdata);
  }
  else {
    PyObject *method = PyUnicode_FromString("static_flux_value");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *result = PyObject_CallMethodObjArgs(
			  referent_, method,
			  mpp, elp, fluxp, mpp, timep, fluxdatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(fluxp);
    Py_XDECREF(mpp);
    Py_XDECREF(timep);
    Py_XDECREF(fluxdatap);
    if(result == NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyFluxProperty::flux_offset(const FEMesh *mesh, const Element *el,
				 const Flux *flux, 
				 const MasterPosition &gpt,
				 double time,
				 SmallSystem *fluxdata) 
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "flux_offset")) {
    this->FluxProperty::flux_offset(mesh, el, flux, gpt, time, fluxdata);
  }
  else {
    PyObject *method = PyUnicode_FromString("flux_offset");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *mpp = NEWSWIGPTR(&gpt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *result = PyObject_CallMethodObjArgs(
			  referent_, method,
			  meshp, elp, fluxp, mpp, timep, fluxdatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(fluxp);
    Py_XDECREF(mpp);
    Py_XDECREF(timep);
    Py_XDECREF(fluxdatap);
    if(result == NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

PyEqnProperty::PyEqnProperty(PyObject *referent, PyObject *regstn,
			     const std::string &name)
  : PythonNative<Property>(referent),
    EqnProperty(name, regstn),
    PyPropertyMethods(referent)
{}

PyEqnProperty::~PyEqnProperty() {}

//=\\=//=\\=//

void PyEqnProperty::force_deriv_matrix(const FEMesh *mesh,
				       const Element *element,
				       const Equation *eqn,
				       const ElementFuncNodeIterator &efni,
				       const MasterPosition &pt,
				       double time,
				       SmallSystem *eqndata)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "force_deriv_matrix")) {
    this->EqnProperty::force_deriv_matrix(mesh, element, eqn, efni, pt, time,
					  eqndata);
  }
  else {
    PyObject *method = PyUnicode_FromString("force_deriv_matrix");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallMethodObjArgs(
		  referent_, method,
		  mpp, elp, eqnp, efnip, mpp, timep, eqndatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(efnip);
    Py_XDECREF(mpp);
    Py_XDECREF(timep);
    Py_XDECREF(eqndatap);
    if(result == NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyEqnProperty::force_value(const FEMesh *mesh,
				const Element *element,
				const Equation *eqn,
				const MasterPosition &pt,
				double time,
				SmallSystem *eqndata)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "force_value")) {
    this->EqnProperty::force_value(mesh, element, eqn, pt, time, eqndata);
  }
  else {
    PyObject *method = PyUnicode_FromString("force_value");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallMethodObjArgs(
			  referent_, method,
			  meshp, elp, eqnp, mpp, timep, eqndatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(mpp);
    Py_XDECREF(timep);
    Py_XDECREF(eqndatap);
    if(result == NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyEqnProperty::first_time_deriv_matrix(const FEMesh *mesh,
					    const Element *element,
					    const Equation *eqn,
					    const ElementFuncNodeIterator &efni,
					    const MasterPosition &pt,
					    double time, SmallSystem *eqndata)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "first_time_deriv_matrix")) {
    this->EqnProperty::first_time_deriv_matrix(mesh, element, eqn, efni, pt,
					       time, eqndata);
  }
  else {
    PyObject *method = PyUnicode_FromString("first_time_deriv_matrix");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallMethodObjArgs(
			  referent_, method,
			  meshp, elp, eqnp, efnip, mpp, timep, eqndatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(efnip);
    Py_XDECREF(mpp);
    Py_XDECREF(timep);
    Py_XDECREF(eqndatap);
    if(result == NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyEqnProperty::second_time_deriv_matrix(
				     const FEMesh *mesh,
				     const Element *element,
				     const Equation *eqn,
				     const ElementFuncNodeIterator &efni,
				     const MasterPosition &pt,
				     double time,
				     SmallSystem *eqndata)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent_, "second_time_deriv_matrix")) {
    this->EqnProperty::second_time_deriv_matrix(mesh, element, eqn, efni, pt,
						time, eqndata);
  }
  else {
    PyObject *method = PyUnicode_FromString("second_time_deriv_matrix");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *timep = PyFloat_FromDouble(time);
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallMethodObjArgs(
			  referent_, method,
			  meshp, elp, eqnp, efnip, mpp, timep, eqndatap, NULL);
    Py_XDECREF(method);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(efnip);
    Py_XDECREF(mpp);
    Py_XDECREF(timep);
    Py_XDECREF(eqndatap);
    if(result == NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::string PyPropertyElementData::classname_("PyPropertyElementData");
// std::string PyPropertyElementData::modulename_(
// 				       "ooflib.SWIG.engine.pypropertywrapper");

PyPropertyElementData::PyPropertyElementData(const std::string & name,
					     PyObject *dat) 
  : ElementData(name), _data(dat) 
{
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_INCREF(_data);
}

// For the particular case of PyObject *'s, simple member 
// retrieval through SWIG doesn't appear to work -- you have to 
// override SWIG's conversion-to-pointer-string to get the actual
// Python object out.  This function has the appropriate typemap
// defined in pypropertywrapper.swg. // TODO PYTHON3: Check this.
PyObject *PyPropertyElementData::data() {
  PYTHON_THREAD_BEGIN_BLOCK;
  // Hacky extra incref.  TODO PYTHON3: Check this too.
  Py_INCREF(_data);
  return _data;
}

PyPropertyElementData::~PyPropertyElementData() {
  PYTHON_THREAD_BEGIN_BLOCK;
  // It's an error if this refcount is already zero -- avoid XDECREF.
  // TODO: Why would it already be zero?
  Py_DECREF(_data);
}

// PyPropertyElementData-handling functions.  Simple wrappers, mostly.
// These are here partially because Element doesn't have a convenient
// SWIG file, and partially because of the need to do the dynamic
// cast.  More direct Python access to the element functions
// is not out of the question.

// int PyProperty::appendElementData(Element *el, 
// 					 PyPropertyElementData *data)
// {
//   return el->appendData(data);
// }

// PyPropertyElementData *PyProperty::getElementData(Element *el, int i)
// {
//   return dynamic_cast<PyPropertyElementData*>(el->getData(i));
// }

// int PyProperty::getElementDataIndex(Element *el, std::string name)
// {
//   std::cerr << "getElementDataIndex" << std::endl;
//   return el->getIndexByName(name);
// }

