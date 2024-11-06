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
double deriv_eps = 1e-8;

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

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// A property is computable if all fields that it uses are defined.

// TODO: currently_computable() and find_computable() aren't used.
// Apparently they were intended to cache the result of
// is_computable().  Is there any need to do that?  The functions
// should probably be deleted.

bool Property::is_computable(const CSubProblem *subproblem) const {
  for(std::vector<Field*>::size_type i=0; i<fields_reqd.size(); i++) {
    if(!subproblem->is_defined_field(*fields_reqd[i])) {
      return false;
    }
  }
  return true;
}

bool Property::currently_computable(const CSubProblem *subproblem) const {
  SubProblemFlagCache::const_iterator where = computability.find(subproblem);
  if(where != computability.end())
    return (*where).second;
  return false;
}

void Property::find_computable(const CSubProblem *subproblem) {
  computability[subproblem] = is_computable(subproblem);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


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
  recurse = false;
  
  if(nlsolver->needsResidual()) {
    // TODO TIMEDERIV: Check how nonlinear solvers use the residual.
    // Is it really just the static part of the flux?  What would
    // happen with a nonlinear flux with a linear viscoelastic part?
    static_flux_value(mesh, element, flux, pt, time, fluxdata);
  }

  // Reset 'recurse' before exiting, in case flux_matrix or
  // static_flux_value is called elsewhere.
  recurse = false;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Private utility function that computes the flux matrix by
// numerically differentiating the flux with respect to a single Field
// component.

DoubleVec &FluxProperty::fluxDeriv(const FEMesh *mesh, const Element *element,
				   const ElementFuncNodeIterator &node,
				   const Flux *flux, const MasterPosition &pt,
				   double time,
				   const Field *field, const IndexP &fieldcomp,
				   // This are passed in to avoid
				   // repeated allocation.
				   SmallSystem &fluxDataLo, // workspace
				   SmallSystem &fluxDataHi  // workspace
			      )
  const
{
  fluxDataLo.fluxVector().zero();
  fluxDataHi.fluxVector().zero();
  DegreeOfFreedom *dof = (*field)(node, fieldcomp.integer());
  double oldValue = dof->value(mesh);

  // Scale eps by original value for robustness
  double eps = max(min_eps, fabs(oldValue)*deriv_eps);

  double upValue = oldValue + eps;
  double dnValue = oldValue - eps;

  // First compute the flux at the smaller field value, sigma(u-eps)
  dof->setValue(mesh, dnValue);
  static_flux_value(mesh, element, flux, pt, time, &fluxDataLo);
  DoubleVec &fluxVecLo = fluxDataLo.fluxVector();

  // Now compute the flux at the higher field value, sigma(u+eps)
  dof->setValue(mesh, upValue);
  static_flux_value(mesh, element, flux, pt, time, &fluxDataHi);
  DoubleVec &fluxVecHi= fluxDataHi.fluxVector();

  // std::cerr << "FluxProperty::fluxDeriv: field=" << *field << " flux=" << *flux << std::endl;
  // std::cerr << "FluxProperty::fluxDeriv: oldValue=" << oldValue << std::endl;
  // std::cerr << "FluxProperty::fluxDeriv: fluxVecLo=" << fluxVecLo << std::endl;
  // std::cerr << "FluxProperty::fluxDeriv: fluxVecHi=" << fluxVecHi << std::endl;

  // Reset to original value
  dof->setValue(mesh, oldValue);

  // Compute the numerical derivative: (fluxVecHi - fluxVecLow)/2*eps
  fluxVecHi -= fluxVecLo;
  fluxVecHi /= (upValue - dnValue);
  return fluxVecHi;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The base class version of flux_matrix() computes the matrix by
// numerically differentiating the flux with respect to the fields.
// The flux is obtained from flux_value(), which must be defined in
// the derived class.


void FluxProperty::flux_matrix(const FEMesh *mesh, const Element *element,
			       const ElementFuncNodeIterator &node,
			       const Flux *flux, const MasterPosition &pt,
			       double time, SmallSystem *fluxdata)
  const
{
  // The default version of flux_matrix() (this method) assumes that
  // static_flux_value() has been defined, and numerically
  // differentiates it.  The default version of static_flux_value()
  // assumes that flux_matrix() has been defined, and multiplies it by
  // the DoF values.  If neither is defined, which is possible if the
  // Property only contributes to the flux offset, we therefore have
  // to avoid an infinite loop, which is done with the recurse flag.

  // The flux sigma is a function of the field phi, field gradient
  // dphi, and their time derivatives phi_t and dphi_t.  The various
  // parts of the modulus can be found by differentiating the flux
  // with respect to the field and its derivatives.  The flux matrix
  // is the modulus times the gradient of the shape function.

  // TODO: This is an expensive no-op to perform if neither
  // flux_matrix() or static_flux_value() is redefined in the derived
  // class.  Similarly, FluxProperty::flux_offset() is expensive.  Can
  // the base class have null versions that are redefined in mix-in
  // classes, one mix-in each to provide the default versions of
  // static_flux_value(), flux_matrix(), and flux_offset()?  Maybe the
  // base class methods should be pure virtual, and there should be
  // mix-ins that provide the null methods and other mix-ins that
  // provided the old default methods.

  // std::cerr << "FluxProperty::flux_matrix: node=" << *node.node()
  // 	    <<  " pt=" << pt << std::endl;
  std::cerr << "-------------" << std::endl;
     

#ifdef HAVE_OPENMP
  bool& recurse = recurse_flags[omp_get_thread_num()];
#endif

  if(recurse) {
    return;
  }
  recurse = true;

  int nrows = fluxdata->nrows();
  int ncols = fluxdata->ncols();
  DoubleVec fluxVecLo(nrows);
  DoubleVec fluxVecHi(nrows);
  SmallSystem fluxDataLo(nrows, ncols);
  SmallSystem fluxDataHi(nrows, ncols);

  // Get the current subproblem, to check if the fields are active.
  CSubProblem *subproblem = mesh->getCurrentSubProblem();
  if(!subproblem)
    throw ErrProgrammingError("Current subproblem not defined",
			      __FILE__, __LINE__);

  // TODO OPT: Give FieldEqnList an iterator, and iterate over
  // Node::fieldset instead of looping over all fields and checking
  // Node::hasField().  Also, the PropertyRegistration knows which
  // Fields are relevant.  Can we get that data from Python?  Fields
  // that are defined and active but not relevant won't make a
  // contribution, so should be skipped.

  double shapefn = node.shapefunction(pt);
  const MasterCoord mpt = pt.mastercoord(); // debugging

  for(CompoundField *field : CompoundField::allcompoundfields()) {

    if(node.hasField(*field) && field->is_active(subproblem)) {

      // The flux matrix is
      //   K_{ik\nu} = Modulus_{ijk} {\partial N_\nu / \partial x_j}
      //      i = flux component
      //      k = field component
      //     nu = node or shapefunction index
      // The Modulus is the derivative of the stress wrt the field
      // gradient component, not wrt the field component.

      // Loop over field components
      for(IndexP fieldcomp : *field->components(IN_PLANE)) {
	// fluxDeriv computes the numerical derivative of the flux
	// with respect to one field component.
	DoubleVec &deriv = fluxDeriv(mesh, element, node, flux, pt, time,
				     field, fieldcomp, fluxDataLo, fluxDataHi);

	
	// Assign the derivative value to flux_matrix
	for(IndexP fluxcomp : *flux->components(ALL_INDICES)) {

	  std::cerr << "flux_matrix:"
		    << " el=" << element->get_index()
		    << " mpt=(" << mpt(0) << "," << mpt(1) << ")"
		    << " " << *field << " " << *node.node()
		    << " ij=" << *fluxcomp.fieldindex()
		    << " k=" << *fieldcomp.fieldindex()
		    << " mtx el=" << deriv[fluxcomp.integer()]
		    << std::endl;
	  
	  fluxdata->stiffness_matrix_element(fluxcomp, field, fieldcomp, node)
	    += deriv[fluxcomp.integer()];
	  ///// TODO:  CHECK THIS
	  // The shape function derivative term cancels a factor of
	  // one over the derivative that comes from converting the
	  // derivative wrt the field into a derivative wrt the field
	  // gradient.
	  
	}
      } // loop over field components
    } // end if(node.hasfield())

    // For the out-of-plane part of the field, the flux matrix is the
    // derivative wrt to the field, not the field gradient, since the
    // field is really the z-derivative of the field.  This means that
    // the shape function term isn't cancelled, as it is for the
    // in-plane contribution.  Because the field is already a
    // derivative, multiply by the shape function, not its derivative.
    
    Field *oop = field->out_of_plane();
    if(node.hasField(*oop) && oop->is_active(subproblem)) {
      for(IndexP fluxcomp : *flux->components(ALL_INDICES)) {
	for(IndexP fieldcomp : *oop->components(ALL_INDICES)) {
	  DoubleVec &deriv = fluxDeriv(mesh, element, node, flux, pt, time,
				       oop, fieldcomp, fluxDataLo, fluxDataHi);
	  // std::cerr << "FluxProperty::flux_matrix: "
	  // 	  << "k=" << *fieldcomp.fieldindex()
	  // 	  << " oop deriv= " << deriv << std::endl;
	  std::cerr << "flux_matrix:"
		    << " el=" << element->get_index()
		    << " mpt=(" << mpt(0) << "," << mpt(1) << ")"
		    << " " << *oop << " " << *node.node()
		    << " ij=" << *fluxcomp.fieldindex()
		    << " k=" << *fieldcomp.fieldindex()
		    << " sf=" << shapefn
		    << " modulus=" << deriv[fluxcomp.integer()]
		    << std::endl;

	  // Factor of shapefn needs to be deleted here in order to
	  // get agreement with Elasticity::flux_matrix.  WTF?
	  fluxdata->stiffness_matrix_element(fluxcomp, oop, fieldcomp, node)
	    += deriv[fluxcomp.integer()]; // * shapefn;
	}
      }
    }

    // Same for the time-derivative part of the Field.
    Field *tdf = field->time_derivative();
    // std::cerr << "FluxProperty::flux_matrix: " << *tdf
    // 	      << " hasField=" << node.hasField(*tdf)
    // 	      << " active=" << tdf->is_active(subproblem)
    // 	      << std::endl;
    if(node.hasField(*tdf) && field->is_active(subproblem)) {
      for(IndexP fieldcomp : *tdf->components(ALL_INDICES)) {
	DoubleVec &deriv = fluxDeriv(mesh, element, node, flux, pt, time,
				     tdf, fieldcomp, fluxDataLo, fluxDataHi);
	// std::cerr << "FluxProperty::flux_matrix:     " << fieldcomp
	// 	  << " deriv=" << deriv << std::endl;
	for(IndexP fluxcomp : *flux->components(ALL_INDICES)) {
	  // Index is determined by field, not tdf.
	  // std::cerr << "FluxProperty::flux_matrix: setting damping_matrix_element: " << fluxcomp << " " << *field << " " << fieldcomp << " " << deriv[fluxcomp.integer()] << std::endl;
	  fluxdata->damping_matrix_element(fluxcomp, field, fieldcomp, node)
	    += deriv[fluxcomp.integer()];
	}
      }
    }

    // Same for the time derivative of the out-of-plane part of the Field.
    Field *ooptdf = field->out_of_plane_time_derivative();
    if(node.hasField(*ooptdf) && ooptdf->is_active(subproblem)) {
      for(IndexP fieldcomp : *ooptdf->components(ALL_INDICES)) {
	DoubleVec &deriv = fluxDeriv(mesh, element, node, flux, pt, time,
				     ooptdf, fieldcomp, fluxDataLo, fluxDataHi);
	for(IndexP fluxcomp : *flux->components(ALL_INDICES)) {
	  // Index is determined by field, not tdf.
	  fluxdata->damping_matrix_element(fluxcomp, oop, fieldcomp, node)
	    += deriv[fluxcomp.integer()];
	}
      }
    }
    
  } // loop over all compound fields
} // end of 'FluxProperty::flux_matrix'

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Compute the offset.  This is the flux when all fields are zero.
// TODO: Don't do this for Properties that won't have an offset.  Do
// we need different mix-in base classes for Properties with and
// without offsets?

void FluxProperty::flux_offset(const FEMesh *mesh,
			       const Element *element,
			       const Flux *flux,
			       const MasterPosition &pt,
			       double time, SmallSystem *fluxdata)
  const
{
#ifdef HAVE_OPENMP
  bool& recurse = recurse_flags[omp_get_thread_num()];
#endif
  if(recurse)
    return;
  recurse = true;

  int nrows = fluxdata->nrows();
  int ncols = fluxdata->ncols();
  SmallSystem fluxData0(nrows, ncols);
  CSubProblem *subproblem = mesh->getCurrentSubProblem();
  
  // First, save the old Field values and set the Fields to zero.
  std::vector<double> oldvals;
  for(std::vector<Field*>::size_type fi=0; fi<Field::all().size(); fi++) {
    Field *field = &(*Field::all()[fi]);
    for(CleverPtr<ElementFuncNodeIterator> node(element->funcnode_iterator());
	!node->end(); ++*node) {
      if(node->hasField(*field) && field->is_active(subproblem)) {
	for(IndexP fieldcomp : *field->components(ALL_INDICES)) {
	  DegreeOfFreedom *dof = (*field)(*node, fieldcomp.integer());
	  oldvals.push_back(dof->value(mesh));
	  dof->setValue(mesh, 0.0);
	}
      }
    }
  }

  // Compute the Flux.

  // The default static_flux_value will call flux_offset (ie, this
  // function), but it's a mistake not to override either
  // static_flux_value or flux_offset.  Elasticity defines both
  // flux_matrix and static_flux_value, but not flux_offset.
  static_flux_value(mesh, element, flux, pt, time, &fluxData0);
  // Store the flux as the offset in fluxdata
  fluxdata->offsetVector() += fluxData0.fluxVector();
  // Restore Field values
  int i = 0;
  for(std::vector<Field*>::size_type fi=0; fi<Field::all().size(); fi++) {
    Field *field = &(*Field::all()[fi]);
    for(CleverPtr<ElementFuncNodeIterator> node(element->funcnode_iterator());
	!node->end(); ++*node) {
      if(node->hasField(*field) && field->is_active(subproblem)) {
	for(IndexP fieldcomp : *field->components(ALL_INDICES)) {
	  DegreeOfFreedom *dof = (*field)(*node, fieldcomp.integer());
	  dof->setValue(mesh, oldvals[i++]);
	}
      }
    }
  }
} 

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The default computation for the flux
//
//    flux = flux_matrix*field + flux_matrix'*field_t + flux_offset
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

  std::cerr << "FluxProperty::static_flux_value calling flux_matrix "
	    << "element=" << element->get_index() << std::endl;

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

  // TODO: Check to see if localdofs includes time derivatives.  If it
  // doesn't, then compute dU/dt by inverting C?  Do we have enough
  // information to do that?  It should be done only once for the
  // whole Mesh, if possible.

  // What if dU/dt is in localdofs for some nodes but not others?

  // Don't worry about Property::flux_matrix() trying to numerically
  // differentiate this function.  If flux_matrix() isn't redefined in
  // the subclass, then static_flux_value() must be redefined, so this
  // version of static_flux_value() won't be used.

  
  // If localdofs includes time derivative fields we can do this:
  fluxdata->fluxVector() += localFluxData.cMatrix*localdofs;

} // FluxProperty::static_flux_value

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

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
  static_flux_value(mesh, element, flux, pt, time, fluxdata);
  recurse = false;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

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

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void EqnProperty::force_deriv_matrix(const FEMesh *mesh, const Element *element,
				     const Equation *eqn,
				     const ElementFuncNodeIterator &node,
				     const MasterPosition &pt, double time,
				     SmallSystem *eqndata)  const
{
  int nrows = eqndata->nrows();
  int ncols = eqndata->ncols();
  DoubleVec forceVec0(nrows), forceVec1(nrows);
  SmallSystem eqndata0(nrows, ncols);
  SmallSystem eqndata1(nrows, ncols);

  // Get the current subproblem, to check if the fields are active
  CSubProblem *subproblem = mesh->getCurrentSubProblem();
  if(!subproblem)
    throw ErrProgrammingError("Current subproblem not defined",
			      __FILE__, __LINE__);

  // Loop over all the fields (that the node might have)
  for(std::vector<Field*>::size_type fi=0; fi<Field::all().size(); fi++) {
    Field *field = &(*Field::all()[fi]);
    if(node.hasField(*field) && field->is_active(subproblem)) {
      // Loop over field components
      for(IndexP fieldcomp : *field->components(ALL_INDICES)) {
	DegreeOfFreedom *dof = (*field)(node, fieldcomp.integer());
	double oldValue = dof->value(mesh);

	// Scale eps by original value for robustness
	double eps = max(min_eps, fabs(oldValue) * deriv_eps);
	double upValue = oldValue + eps;
	double dnValue = oldValue - eps;

	// First compute forceVec0 = f(u-eps)
	dof->setValue(mesh, dnValue);
	force_value(mesh, element, eqn, pt, time, &eqndata0);
	forceVec0 = eqndata0.forceVector();

	// Now compute forceVec1 = f(u+eps)
	dof->setValue(mesh, upValue);
	force_value(mesh, element, eqn, pt, time, &eqndata1);
	forceVec1 = eqndata1.forceVector();
	dof->setValue(mesh, oldValue);

	// Compute the numerical derivative: (f1 - f0) / (2*eps)
	forceVec1 -= forceVec0;
	forceVec1 /= (upValue - dnValue);

	// Assign the derivative value to force_deriv_matrix
	for(IndexP eqncomp : *eqn->components())
	  eqndata->force_deriv_matrix_element(eqncomp, field, fieldcomp, node)
	    += forceVec1[ eqncomp.integer() ];

	eqndata0.forceVector().zero();
	eqndata1.forceVector().zero();
      } // loop over field components
    } // end if (node.hasfield())
  } // loop over all fields

} // end of force_deriv_matrix

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const Property &prop) {
  return os << "Property(" << prop.name() << ")";
}

