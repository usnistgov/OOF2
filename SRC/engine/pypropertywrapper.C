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

void PyPropertyMethods::py_precompute(PyObject *referent, Property *prop,
				      FEMesh *mesh)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "precompute")) {
    // The function isn't defined in the derived class.  Call the
    // base class method instead.
    PyErr_Clear();
    prop->Property::precompute(mesh);
  }
  else {
    PyObject *func = PyObject_GetAttrString(referent, "precompute_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *k_result = PyObject_CallFunctionObjArgs(func, meshp, NULL);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    if(k_result==NULL)
      pythonErrorRelay();
    Py_XDECREF(k_result);
  }
}

//=\\=//=\\=//

void PyPropertyMethods::py_cross_reference(PyObject *referent, Property *prop,
					   Material *mat)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, (char*) "cross_reference")) {
    prop->Property::cross_reference(mat);
  }
  else {
    PyObject *func = PyObject_GetAttrString(referent, "cross_reference_wrap");
    PyObject *matp = NEWSWIGPTR(mat, "Material");
    PyObject *k_result = PyObject_CallFunctionObjArgs(func, matp, NULL);
    Py_XDECREF(func);
    Py_XDECREF(matp);
    if(k_result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(k_result);
  }
}

//=\\=//=\\=//

void PyPropertyMethods::py_begin_element(PyObject *referent, Property *prop,
					 const CSubProblem *m,
					 const Element *el)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "begin_element")) {
    prop->Property::begin_element(m, el);
  }
  else {
    PyObject *func = PyObject_GetAttrString(referent, "begin_element_wrap");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *subp = NEWSWIGPTR(m, "CSubProblem");
    PyObject *k_result = PyObject_CallFunctionObjArgs(func, subp, elp, NULL);
    Py_XDECREF(func);
    Py_XDECREF(elp);
    Py_XDECREF(subp);
    if(k_result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(k_result);
  }
}

void PyPropertyMethods::py_end_element(PyObject *referent, Property *prop,
				       const CSubProblem *m, const Element *el)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "end_element")) {
    prop->Property::end_element(m, el);
  }
  else {
    PyObject *func = PyObject_GetAttrString(referent, "end_element_wrap");
    PyObject *subp = NEWSWIGPTR(m, "CSubProblem");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *k_result = PyObject_CallFunctionObjArgs(func, subp, elp, NULL);
    Py_XDECREF(func);
    Py_XDECREF(subp);
    Py_XDECREF(elp);
    if(k_result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(k_result);
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
    PyObject *func = PyObject_GetAttrString(referent_, "begin_point_wrap");
    PyObject *meshp = NEWSWIGPTR(m, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *flxp = NEWSWIGPTR(flx, "Flux");
    PyObject *mpp = NEWSWIGPTR(&mpos, "MasterPosition");
    PyObject *k_result = PyObject_CallFunctionObjArgs(
				      func, meshp, elp, flxp, mpp, NULL);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(flxp);
    Py_XDECREF(mpp);
    if(k_result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(k_result);
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
    PyObject *func = PyObject_GetAttrString(referent_,
					    (char*) "end_point_wrap");
    PyObject *meshp = NEWSWIGPTR(m, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *flxp = NEWSWIGPTR(flx, "Flux");
    PyObject *mpp = NEWSWIGPTR(&mpos, "MasterPosition");
    PyObject *k_result = PyObject_CallFunctionObjArgs(
				      func, meshp, elp, flxp, mpp, NULL);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(flxp);
    Py_XDECREF(mpp);
    if(k_result==NULL) {
      pythonErrorRelay();
    }
    Py_XDECREF(k_result);
  }
}

//=\\=//=\\=//

void PyPropertyMethods::py_post_process(PyObject *referent,
					const Property *prop,
					CSubProblem *m, const Element *el)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "post_process")) {
    prop->Property::post_process(m, el);
  }
  else {
    PyObject *func = PyObject_GetAttrString(referent,
					    (char*) "post_process_wrap");
    PyObject *subp = NEWSWIGPTR(m, "CSubProblem");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *result = PyObject_CallFunctionObjArgs(func, subp, elp, NULL);
    Py_XDECREF(subp);
    Py_XDECREF(elp);
    Py_XDECREF(func);
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

void PyPropertyMethods::py_output(PyObject *referent, Property *prop,
			       FEMesh *mesh, const Element *el,
			       const PropertyOutput *propout,
			       const MasterPosition &pos,
			       OutputVal *oval)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "output")) {
    prop->Property::output(mesh, el, propout, pos, oval);
  }
  else {
    PyObject *func = PyObject_GetAttrString(referent, "output_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *propp = NEWSWIGPTR(propout, "PropertyOutput");
    PyObject *posp = NEWSWIGPTR(&pos, "MasterPosition");

    PyObject *pyresult = PyObject_CallFunctionObjArgs(
				      func, meshp, elp, propp, posp, NULL);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(propp);
    Py_XDECREF(posp);
    if(pyresult == NULL)
      pythonErrorRelay();

    // Check for None.  PyProperty.output_wrap() returns None if
    // the derived class doesn't define PyProperty.output().
    if(pyresult != Py_None) {
      // Convert result to a C++ object
      OutputVal *cresult;
      if(!SWIG_IsOK(SWIG_ConvertPtr(pyresult, (void**) &cresult,
				    ((SwigPyObject*) pyresult)->ty, 0)))
	{
	  throw ErrProgrammingError(
			    "Python output() does not return an OutputVal",
			    __FILE__, __LINE__);
	}
      *oval = *cresult;
    }
    Py_XDECREF(pyresult);
  }
}

//=\\=//=\\=//

bool PyPropertyMethods::py_constant_in_space(PyObject *referent,
					     const Property *prop) 
  const
{
  bool c_result;
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "constant_in_space")) {
    throw ErrUserError("constant_in_space method is missing from Property "
		       + prop->name());
  }
  PyObject *func = PyObject_GetAttrString(referent, "constant_in_space_wrap");
  // PyObject_CallNoArgs is only available in Python 3.9 and later.
  //  PyObject *k_result = PyObject_CallNoArgs(func);
  PyObject *k_result = PyObject_CallFunctionObjArgs(func, NULL);
  Py_XDECREF(func);
  if(k_result == NULL) {
    pythonErrorRelay();
  }
  c_result = PyObject_IsTrue(k_result);
  Py_XDECREF(k_result);
  return c_result;
}

//=\\=//=\\=//

bool PyPropertyMethods::is_symmetric_K(PyObject *referent, const Property *prop,
				       const CSubProblem *subp)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "is_symmetric_K")) {
    return prop->Property::is_symmetric_K(subp);
  }
  PyObject *func = PyObject_GetAttrString(referent, "is_symmetric_K_wrap");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *k_result = PyObject_CallFunctionObjArgs(func, subpp, NULL);
  Py_XDECREF(func);
  Py_XDECREF(subpp);
  if(k_result == NULL) {
    pythonErrorRelay();
  }
  bool c_result = PyObject_IsTrue(k_result);
  Py_XDECREF(k_result);
  return c_result;
}

bool PyPropertyMethods::is_symmetric_C(PyObject *referent, const Property *prop,
				       const CSubProblem *subp)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, (char*) "is_symmetric_C")) {
    return prop->Property::is_symmetric_C(subp);
  }
  PyObject *func = PyObject_GetAttrString(referent,
					  (char*) "is_symmetric_C_wrap");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *k_result = PyObject_CallFunctionObjArgs(func, subpp, NULL);
  Py_XDECREF(func);
  Py_XDECREF(subpp);
  if(k_result == NULL) {
    pythonErrorRelay();
  }
  bool c_result = PyObject_IsTrue(k_result);
  Py_XDECREF(k_result);
  return c_result;
}

bool PyPropertyMethods::is_symmetric_M(PyObject *referent, const Property *prop,
				       const CSubProblem *subp)
  const
{
  PYTHON_THREAD_BEGIN_BLOCK;
  if(!PyObject_HasAttrString(referent, "is_symmetric_M")) {
    return prop->Property::is_symmetric_M(subp);
  }
  PyObject *func = PyObject_GetAttrString(referent, "is_symmetric_M_wrap");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *k_result = PyObject_CallFunctionObjArgs(func, subpp, NULL);
  Py_XDECREF(func);
  Py_XDECREF(subpp);
  if(k_result == NULL) {
    pythonErrorRelay();
  }
  bool c_result = PyObject_IsTrue(k_result);
  Py_XDECREF(k_result);
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
  PyObject *func = PyObject_GetAttrString(referent, "integration_order_wrap");
  PyObject *subpp = NEWSWIGPTR(subp, "CSubProblem");
  PyObject *elp = NEWSWIGPTR(el, "Element");
  PyObject *k_result = PyObject_CallFunctionObjArgs(func, subpp, elp, NULL);
  Py_XDECREF(func);
  Py_XDECREF(subpp);
  Py_XDECREF(elp);
  if(k_result==NULL)
    pythonErrorRelay();
  int c_result = PyInt_AsLong(k_result);
  Py_XDECREF(k_result);
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
    PyObject *func = PyObject_GetAttrString(referent_, "flux_matrix_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *mpp = NEWSWIGPTR(&gpt, "MasterPosition");
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *result = PyObject_CallFunctionObjArgs(
		    func, meshp, elp, efnip, fluxp, mpp, fluxdatap, NULL);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(efnip);
    Py_XDECREF(fluxp);
    Py_XDECREF(mpp);
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
    PyObject *func = PyObject_GetAttrString(referent_, "flux_value_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *result = PyObject_CallFunctionObjArgs(
			    func, meshp, elp, fluxp, mpp, fluxdatap, NULL);
    Py_XDECREF(func);
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
    PyObject *func = PyObject_GetAttrString(referent_,
					    "static_flux_value_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *result = PyObject_CallFunction(
		    func, "OOOOdO", mpp, elp, fluxp, mpp, time, fluxdatap);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(fluxp);
    Py_XDECREF(mpp);
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
    PyObject *func = PyObject_GetAttrString(referent_, "flux_offset_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(el, "Element");
    PyObject *fluxp = NEWSWIGPTR(flux, "Flux");
    PyObject *fluxdatap = NEWSWIGPTR(fluxdata, "SmallSystem");
    PyObject *mpp = NEWSWIGPTR(&gpt, "MasterPosition");
    PyObject *result = PyObject_CallFunction(func, "OOOOdO",
				     meshp, elp, fluxp, mpp, time, fluxdatap);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(fluxp);
    Py_XDECREF(fluxdatap);
    Py_XDECREF(mpp);
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
    PyObject *func = PyObject_GetAttrString(
			    referent_, "force_deriv_matrix_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallFunction(
	     func, "OOOOOdO", mpp, elp, eqnp, efnip, mpp, time, eqndatap);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(efnip);
    Py_XDECREF(mpp);
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
    PyObject *func = PyObject_GetAttrString(referent_, "force_value_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallFunction(
		     func, "OOOOdO", meshp, elp, eqnp, mpp, time, eqndatap);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(mpp);
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
    PyObject *func = PyObject_GetAttrString(
			    referent_, "first_time_deriv_matrix_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallFunction(
	     func, "OOOOOdO", meshp, elp, eqnp, efnip, mpp, time, eqndatap);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(efnip);
    Py_XDECREF(mpp);
    Py_XDECREF(eqndatap);
    if(result == NULL)
      pythonErrorRelay();
    Py_XDECREF(result);
  }
}

//=\\=//=\\=//

void PyEqnProperty::second_time_deriv_matrix(const FEMesh *mesh,
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
    PyObject *func = PyObject_GetAttrString(
		    referent_, "second_time_deriv_matrix_wrap");
    PyObject *meshp = NEWSWIGPTR(mesh, "FEMesh");
    PyObject *elp = NEWSWIGPTR(element, "Element");
    PyObject *eqnp = NEWSWIGPTR(eqn, "Equation");
    PyObject *efnip = NEWSWIGPTR(&efni, "ElementFuncNodeIterator");
    PyObject *mpp = NEWSWIGPTR(&pt, "MasterPosition");
    PyObject *eqndatap = NEWSWIGPTR(eqndata, "SmallSystem");
    PyObject *result = PyObject_CallFunction(
	     func, "OOOOOdO", meshp, elp, eqnp, efnip, mpp, time, eqndatap);
    Py_XDECREF(func);
    Py_XDECREF(meshp);
    Py_XDECREF(elp);
    Py_XDECREF(eqnp);
    Py_XDECREF(efnip);
    Py_XDECREF(mpp);
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

