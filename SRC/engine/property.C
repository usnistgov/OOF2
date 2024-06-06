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

// smallest step for numerical differentiation
#include <float.h>
static const double min_eps = 16*DBL_EPSILON;

// eps value used for finite difference approx. of numerical derivatives
double deriv_eps = 1e-5;

inline double max(double x, double y)
{
  return (x > y ? x : y);
}

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

void Property::find_computable(const CSubProblem *subproblem) {
  computability[subproblem] = is_computable(subproblem);
}

bool Property::currently_active(const CSubProblem *subproblem) const {
  SubProblemFlagCache::const_iterator where = activity.find(subproblem);
  if(where != activity.end())
    return (*where).second;
  return false;
}

bool Property::currently_computable(const CSubProblem *subproblem) const {
  SubProblemFlagCache::const_iterator where = computability.find(subproblem);
  if(where != computability.end())
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
					   SmallSystem *fluxdata)
  const
{
  // The FluxProperty::static_flux_value() and
  // FluxProperty::flux_matrix() functions will only run if
  // FluxProperty::recurse is false.  Each of those functions sets it
  // to true before calling anything else.  These functions may be
  // overridden by sub-classes which have their own implementations of
  // one or the other (but not both) of these, in which case they will
  // populate the appropriate data structures, ignoring the
  // FluxProperty::recurse datum.  This is also why recurse has to be
  // re-set to false inside the func-node loop.

#ifdef HAVE_OPENMP
  bool& recurse = recurse_flags[omp_get_thread_num()];
#endif
  recurse = false;

  for(CleverPtr<ElementFuncNodeIterator>node(element->funcnode_iterator()); 
      !node->end(); ++*node)
    {
      flux_matrix(mesh, element, *node, flux, pt, time, fluxdata);
      recurse = false;
    }

  flux_offset(mesh, element, flux, pt, time, fluxdata);

  if(nlsolver->needsResidual()) 
    static_flux_value(mesh, element, flux, pt, time, fluxdata);

  // Reset 'recurse' before exiting, in case flux_matrix or
  // static_flux_value is called elsewhere.
  recurse = false;
}

//=\\=//=\\=//=\\=//

// The default version of flux_matrix assumes that static_flux_value
// has been defined, and numerically differentiates it.  The default
// version of static_flux_value assumes that flux_matrix has been
// defined, and multiplies it by the DoF values.  If neither is
// defined, which is possible if the Property only contributes to the
// flux offset, we therefore have to avoid an infinite loop, which is
// done with the recurse flag.  

void FluxProperty::flux_matrix(const FEMesh *mesh, const Element *element,
			       const ElementFuncNodeIterator  &node,
			       const Flux *flux, const MasterPosition &pt,
			       double time, SmallSystem *fluxdata)
  const
{
#ifdef HAVE_OPENMP
  bool& recurse = recurse_flags[omp_get_thread_num()];
#endif

  if(recurse) {
    return;
  }
  recurse = true;

  int nrows = fluxdata->nrows();
  int ncols = fluxdata->ncols();
  DoubleVec fluxVec0(nrows);
  DoubleVec fluxVec1(nrows);
  SmallSystem fluxdata0( nrows, ncols );
  SmallSystem fluxdata1( nrows, ncols );
  CSubProblem *subproblem = mesh->getCurrentSubProblem();

  // Get the current subproblem, to check if the fields are active
  if ( !subproblem )
    throw ErrProgrammingError("Current subproblem not defined",
			      __FILE__, __LINE__);

  // Loop over all the fields (that the node might have)
  for (std::vector<Field*>::size_type fi=0; fi<Field::all().size(); fi++)
  {
    Field *field = &( *Field::all()[fi] );
    if (node.hasField( *field ) && field->is_active( subproblem ))
    {
      // Loop over field components
      for(IndexP fieldcomp : *field->components(ALL_INDICES)) {
	DegreeOfFreedom *dof = (*field)(node, fieldcomp.integer());
	double oldValue = dof->value( mesh );

	// Scale eps by original value for robustness
	double eps = max(min_eps, fabs(oldValue)* deriv_eps); 

	double upValue = oldValue + eps;
	double dnValue = oldValue - eps;

	// First compute fluxVec0 = sigma(u-eps)
	dof->setValue( mesh, dnValue );
	static_flux_value(mesh, element, flux, pt, time, &fluxdata0);
	fluxVec0 = fluxdata0.fluxVector();

	// Now compute fluxVec1 = sigma(u+eps)
	dof->setValue( mesh, upValue );
	static_flux_value(mesh, element, flux, pt, time, &fluxdata1);
	fluxVec1 = fluxdata1.fluxVector();

	// Reset to original value!
	dof->setValue( mesh, oldValue );

	// Compute the numerical derivative: (fluxVec1 - fluxVec0) / 2*eps
	fluxVec1 -= fluxVec0;
	fluxVec1 /= (upValue - dnValue);

	// Assign the derivative value to flux_matrix
	for(IndexP fluxcomp : *flux->components(ALL_INDICES))
	  fluxdata->stiffness_matrix_element( fluxcomp, field, fieldcomp, node )
	    += fluxVec1[ fluxcomp.integer() ];

	  fluxdata0.fluxVector().zero();
	  fluxdata1.fluxVector().zero();
      } // loop over field components
    } // end if (node.hasfield())
  } // loop over all fields

} // end of 'FluxProperty::flux_matrix'

//=\\=//=\\=//=\\=//

// The default computation for the static part of the flux
//
//    flux = flux_matrix * field + flux_offset
//
// This is the default computation if the flux property does not
// specify its own definition.

void FluxProperty::static_flux_value(const FEMesh *mesh, const Element *element,
				     const Flux *flux,
				     const MasterPosition &pt,
				     double time, SmallSystem *fluxdata)
  const
{
#ifdef HAVE_OPENMP
  bool& recurse = recurse_flags[omp_get_thread_num()];
#endif

  if(recurse) {
    return;
  }
  recurse = true;

  // retrieve the local coefficients for the field(s) into localdofs.
  DoubleVec localdofs( element->ndof(), 0.0 );
  element->localDoFs( mesh, localdofs );

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
	flux_matrix(mesh, element, *eni, flux, pt, time, &localFluxData);
      }
      catch (ErrNoSuchField &exc) {} // benign
    }
  try {
    flux_offset(mesh, element, flux, pt, time, &localFluxData);
  }
  catch (ErrNoSuchField &exc) {}

  fluxdata->fluxVector() += localFluxData.offsetVector();
  fluxdata->fluxVector() += localFluxData.kMatrix*localdofs;
}

//=\\=//=\\=//=\\=//

// The default flux_value is the static_flux_value.  Properties that
// make non-static contributions to the flux need to redefine this
// function.

void FluxProperty::flux_value(const FEMesh *mesh, const Element *element,
			      const Flux *flux, const MasterPosition &pt,
			      double time, SmallSystem *fluxdata) const
{
#ifdef HAVE_OPENMP
  bool& recurse = recurse_flags[omp_get_thread_num()];
#endif

  recurse = false;
  static_flux_value( mesh, element, flux, pt, time, fluxdata);
  recurse = false;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void EqnProperty::make_equation_contributions(const FEMesh *mesh,
					      const Element *element,
					      const Equation *eqn,
					      const MasterPosition &pt,
					      double time,
					      const CNonlinearSolver *nlsolver,
					      SmallSystem *eqndata)
  const
{
  for(CleverPtr<ElementFuncNodeIterator>node(element->funcnode_iterator()); 
      !node->end(); ++*node)
  {
    first_time_deriv_matrix(mesh, element, eqn, *node, pt, time, eqndata);
    second_time_deriv_matrix(mesh, element, eqn, *node, pt, time, eqndata);
    if(nlsolver->needsJacobian())
      force_deriv_matrix(mesh, element, eqn, *node, pt, time, eqndata);
  }
  force_value(mesh, element, eqn, pt, time, eqndata);
}

//=\\=//=\\=//=\\=//

void EqnProperty::force_deriv_matrix(const FEMesh *mesh, const Element *element,
				     const Equation *eqn,
				     const ElementFuncNodeIterator &node,
				     const MasterPosition &pt, double time,
				     SmallSystem *eqndata)  const
{
  int nrows = eqndata->nrows();
  int ncols = eqndata->ncols();
  DoubleVec forceVec0(nrows), forceVec1(nrows);
  SmallSystem eqndata0( nrows, ncols );
  SmallSystem eqndata1( nrows, ncols );

  // Get the current subproblem, to check if the fields are active
  CSubProblem *subproblem = mesh->getCurrentSubProblem();
  if ( !subproblem )
    throw ErrProgrammingError("Current subproblem not defined",
			      __FILE__, __LINE__);

  // Loop over all the fields (that the node might have)
  for(std::vector<Field*>::size_type fi=0; fi<Field::all().size(); fi++)
  {
    Field *field = &( *Field::all()[fi] );
    if (node.hasField( *field ) && field->is_active( subproblem ))
    {
      // Loop over field components
      for(IndexP fieldcomp : *field->components(ALL_INDICES)) {
	DegreeOfFreedom *dof = (*field)(node, fieldcomp.integer());
	double oldValue = dof->value( mesh );

	// Scale eps by original value for robustness
	double eps = max(min_eps, fabs(oldValue) * deriv_eps);
	double upValue = oldValue + eps;
	double dnValue = oldValue - eps;

	// First compute forceVec0 = f(u-eps)
	dof->setValue( mesh, dnValue );
	force_value(mesh, element, eqn, pt, time, &eqndata0);
	forceVec0 = eqndata0.forceVector();

	// Now compute forceVec1 = f(u+eps)
	dof->setValue( mesh, upValue );
	force_value(mesh, element, eqn, pt, time, &eqndata1);
	forceVec1 = eqndata1.forceVector();
	dof->setValue( mesh, oldValue );

	// Compute the numerical derivative: (f1 - f0) / (2*eps)
	forceVec1 -= forceVec0;
	forceVec1 /= (upValue - dnValue);

	// Assign the derivative value to force_deriv_matrix
	for(IndexP eqncomp : *eqn->components())
	  eqndata->force_deriv_matrix_element( eqncomp, field, fieldcomp, node )
	    += forceVec1[ eqncomp.integer() ];

	eqndata0.forceVector().zero();
	eqndata1.forceVector().zero();
      } // loop over field components
    } // end if (node.hasfield())
  } // loop over all fields

} // end of force_deriv_matrix


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const Property &prop) {
  return os << "Property(" << prop.name() << ")";
}

