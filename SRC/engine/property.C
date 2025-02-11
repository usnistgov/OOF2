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
#include "common/cleverptr.h"
#include "common/doublevec.h"
#include "common/printvec.h"
#include "common/pythonlock.h"
#include "common/pyutils.h"
#include "common/trace.h"
#include "engine/IO/propertyoutput.h"
#include "engine/cnonlinearsolver.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/ooferror.h"
#include "engine/planarity.h"
#include "engine/property.h"
#include "engine/smallsystem.h"

#ifdef HAVE_OPENMP
#include <omp.h>
#endif

// It appears the PyObject* can't be const, because
// PyObject_GetAttrString doesn't take a const argument.

Property::Property(const std::string &nm, PyObject *registration)
  : name_(nm), fields_reqd(0), registration_(registration)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  // registry.classobj.__name__, viewed through C++...
  PyObject *psub = PyObject_GetAttrString(registration, (char*) "subclass");
  classname_ = getPyStringData(psub, "__name__");
  Py_XDECREF(psub);
  Py_INCREF(registration_);
#ifdef DEBUG
  static PyObject *propregclass = nullptr;
  if(!propregclass) {
    PyObject *mod = PyImport_ImportModule("ooflib.engine.propertyregistration");
    assert(mod != nullptr);
    propregclass = PyObject_GetAttrString(mod, "PropertyRegistration");
    assert(propregclass != nullptr);
    Py_XDECREF(mod);
    Py_XINCREF(propregclass);
  }
  assert(PyObject_IsInstance(registration, propregclass));
#endif // DEBUG
}

Property::~Property()
{
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_DECREF(registration_);
}

PyObject *Property::registration() const {
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_INCREF(registration_);
  return registration_;
}

void Property::require_field(const Field &field) {
  for(std::vector<Field*>::size_type i=0; i<fields_reqd.size(); i++)
    if(*fields_reqd[i] == field)
      return;			// don't list a field more than once
  fields_reqd.push_back(&field);
}

// A property is computable if all fields that it uses are defined.

bool Property::is_computable(const CSubProblem *subproblem) const {
  for(std::vector<Field*>::size_type i=0; i<fields_reqd.size(); i++) {
    if(!subproblem->is_defined_field(*fields_reqd[i])) {
      return false;
    }
  }
  return true;
}

// TODO: currently_computable() and find_computable() aren't used.
// Apparently they were intended to cache the result of
// is_computable().  Is there any need to do that?  The functions
// should probably be deleted.

// void Property::find_computable(const CSubProblem *subproblem) {
//   computability[subproblem] = is_computable(subproblem);
// }

// bool Property::currently_computable(const CSubProblem *subproblem) const {
//   SubProblemFlagCache::const_iterator where = computability.find(subproblem);
//   if(where != computability.end())
//     return (*where).second;
//   return false;
// }

// A property is active if it's computable and is used in an active
// Flux or Equation.

// bool Property::is_active(const CSubProblem *subproblem) const {
//   if(!is_computable(subproblem))
//     return false;
//   // Look in the Property's registration to find the fluxes and
//   // equations that it's used in.

// }

void Property::cache_active(const CSubProblem *subproblem, bool active) {
  activity[subproblem] = active;
}

bool Property::currently_active(const CSubProblem *subproblem) const {
  SubProblemFlagCache::const_iterator where = activity.find(subproblem);
  if(where != activity.end())
    return (*where).second;
  return false;
}

void Property::cache_nonlinearity(const CSubProblem *subproblem, bool nonlinear)
{
  nonlinearity[subproblem] = nonlinear;
}

bool Property::currently_nonlinear(const CSubProblem *subproblem) const {
  SubProblemFlagCache::const_iterator where = nonlinearity.find(subproblem);
  if(where != nonlinearity.end())
    return (*where).second;
  return false;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The default versions of is_symmetric_* return true because that's
// the correct answer for a Property that doesn't make any
// contribution to a matrix.

bool Property::is_symmetric_K(const CSubProblem*) const {
  return true;
}

bool Property::is_symmetric_C(const CSubProblem*) const {
  return true;
}

bool Property::is_symmetric_M(const CSubProblem*) const {
  return true;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Property::set_mesh_data(FEMesh *mesh, void *ptr) const {
  mesh->set_property_data(this, ptr);
}

void *Property::get_mesh_data(const FEMesh *mesh) const {
  return mesh->get_property_data(this);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void FluxProperty::make_flux_contributions(const FEMesh *mesh,
					   const Element *element,
					   const Flux *flux,
					   const MasterPosition &pt,
					   double time,
					   const CNonlinearSolver *nlsolver,
					   void *localdata,
					   SmallSystem *fluxdata)
  const
{
  for(CleverPtr<ElementFuncNodeIterator>node(element->funcnode_iterator()); 
      !node->end(); ++*node)
    {
      flux_matrix(mesh, element, *node, flux, pt, time, localdata, fluxdata);
    }

  flux_offset(mesh, element, flux, pt, time, localdata, fluxdata);
  
  if(nlsolver->needsResidual()) {
    // TODO TIMEDERIV: Check how nonlinear solvers use the residual.
    // Is it really just the static part of the flux?  What would
    // happen with a nonlinear flux with a linear viscoelastic part?
    flux_value(mesh, element, flux, pt, time, localdata, fluxdata);
  }
}

//=\\=//=\\=//=\\=//

// The default computation for the flux
//
//    flux = flux_matrix*field + flux_matrix'*field_t + flux_offset
//
// This is the default computation if the flux property does not
// specify its own definition.

void FluxProperty::flux_value(const FEMesh *mesh, const Element *element,
			      const Flux *flux, const MasterPosition &pt,
			      double time, void *localdata,
			      SmallSystem *fluxdata)
  const
{
  // retrieve the local coefficients for the field(s) into localdofs.
  DoubleVec localdofs(element->localDoFs(mesh));

  // We want to increment the fluxVector in the passed-in fluxdata
  // object, but we can't use its kMatrix and offsetVector.  Those may
  // already contain values from other Properties.  So here we create
  // a new SmallSystem to use as a local fluxdata, just to compute
  // kMatrix and offsetVector.
  SmallSystem localFluxData(fluxdata->nrows(), fluxdata->ncols());

  for(CleverPtr<ElementFuncNodeIterator>eni(element->funcnode_iterator()); 
      !eni->end(); ++*eni)
    {
      try {
	flux_matrix(mesh, element, *eni, flux, pt, time, localdata,
		    &localFluxData);
      }
      catch (ErrNoSuchField &exc) {} // benign
    }
  try {
    flux_offset(mesh, element, flux, pt, time, localdata, &localFluxData);
  }
  catch (ErrNoSuchField &exc) {}

  fluxdata->fluxVector() += localFluxData.offsetVector();
  fluxdata->fluxVector() += localFluxData.kMatrix*localdofs;

  // If localdofs includes time derivative fields we can do this.  If
  // localdofs doesn't include time derivative fields, then doing this
  // is a no-op. TODO: Skip the call if it's a no-op.
  fluxdata->fluxVector() += localFluxData.cMatrix*localdofs;

} // FluxProperty::flux_value

//=\\=//=\\=//=\\=//

// The default static_flux_value is the flux_value.  Properties that
// make non-static contributions to the flux need to redefine this
// function.

void FluxProperty::static_flux_value(
			     const FEMesh *mesh, const Element *element,
			     const Flux *flux, const MasterPosition &pt,
			     double time, void *localdata,
			     SmallSystem *fluxdata) const
{
  flux_value(mesh, element, flux, pt, time, localdata, fluxdata);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void EqnProperty::make_equation_contributions(const FEMesh *mesh,
					      const Element *element,
					      const Equation *eqn,
					      const MasterPosition &pt,
					      double time,
					      const CNonlinearSolver *nlsolver,
					      void *localdata,
					      SmallSystem *eqndata)
  const
{
  for(CleverPtr<ElementFuncNodeIterator>node(element->funcnode_iterator()); 
      !node->end(); ++*node)
  {
    time_deriv_matrices(mesh, element, *node, eqn, pt, time, localdata,
			eqndata);
    if(nlsolver->needsJacobian())
      force_deriv_matrix(mesh, element, *node, eqn, pt, time, localdata,
			 eqndata);
  }
  force_value(mesh, element, eqn, pt, time, localdata, eqndata);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const Property &prop) {
  return os << "Property(" << prop.name() << ")";
}

