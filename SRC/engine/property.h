// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

#ifndef PROPERTY_H
#define PROPERTY_H

// forward declarations
class Property;

#include <oofconfig.h>
#include "common/identification.h" // for ltidobject
#include "common/pythonexportable.h"
#include <string>
#include <vector>
#include <map>

#ifdef HAVE_OPENMP
#include <deque>
#include <omp.h>
#endif

// things defined elsewhere
class CNonlinearSolver;
class CSubProblem;
class DoubleVec;
class EdgeSet;
class Element;
class ElementFuncNodeIterator;
class Equation;
class FEMesh;
class Field;
class Flux;
class IndexP;
class LinearizedSystem;
class MasterPosition;
class Material;
class NewEquation;
class OutputVal;
class PropertyOutput;
class SmallSystem;

// Property objects are universally created from PropertyRegistration
// objects' call methods, from Python.

// Since properties must be visible in Python, they must be SWIG'd,
// and in general should also have a "python part" of the SWIG'd
// interface, conventionally placed in an ".spy" file.  The python
// part of the interface must include registration of the property,
// i.e. the creation of a PropertyRegistration object with appropriate
// data.  The registration code must run at import-time.

// The property registration object must include the name of the
// property, the property's class, module, and a numerical "ordering"
// which is relative to all other property registration objects, and
// controls the presentation of this property in the GUI.  Following
// that, the property should indicate the parameters it requires, the
// fields it uses, and the fluxes to which it contributes.  It should
// indicate what type of property it is, and any outputs to which it
// contributes.

// The property type broadly indicates the role of this property in
// the material, and should be defined such that it only makes sense
// to have one property of each type in a material.  For instance, any
// property dependent on displacement and contributing to stress could
// advertise itself as being of type "Elasticity".  The OOF solver
// will then allow at most one property of type "Elasticity" per
// material.  The types are not predefined, property writers may make
// new types without modifying the engine code -- OOF will simply
// insist that at most one property of each defined type be present in
// each material.


// The EqnProperty and FluxProperty classes are derived from the
// Property class.  The EqnProperty API contains the following
// functions:
//  - force_value
//  - force_deriv_matrix
//  - first_time_deriv_matrix
//  - second_time_deriv_matrix
// The default definitions of the EqnProperty methods are no-ops, but
// some must be redefined for a EqnProperty to be useful.
//
// The FluxProperty API contains
//  - flux_value           (default definition uses flux_matrix and flux_offset)
//  - static_flux_value    (default definition is flux_value)
//  - flux_offset          (default definition is a no-op)
//  - flux_matrix          (default definition is a no-op)
// Either flux_matrix or flux_offset must be defined for a
// FluxProperty to be useful.


class Property: virtual public PythonExportable<Property> {
private:
  const std::string name_;	// name of this instance
  std::string classname_;   // For PythonExportable-ability.
  std::vector<const Field*> fields_reqd; // fields reqd to compute this property
  Property(const Property&);	// prohibited

  // Various subproblem-dependent flags are cached in these maps:
  typedef std::map<const CSubProblem*, bool, ltidobject<CSubProblem>> SubProblemFlagCache;
  SubProblemFlagCache activity;
  SubProblemFlagCache computability;
  SubProblemFlagCache nonlinearity;
public:
  Property(const std::string &nm, PyObject *registration);
  virtual ~Property();

  // As a RegisteredCClass, Property must host a Python "registry"
  // entry, which is a list of Python objects.  This entry is
  // created as class data in the property.spy file.

  // This particular property's registration must also be stored, and
  // be retrievable.
  PyObject *registration_;
  PyObject *registration() const;

  const std::string &name() const { return name_; }
  // The following are required for a base class of PythonExportable.
  virtual const std::string &classname() const { return classname_; }

  // A Property is computable if all the Fields it requires are
  // defined on a Mesh.  A property is active if it is computable and
  // contributes to an active equation or active flux.  Activity and
  // computability are computed during the precomputation steps of
  // stiffness matrix construction and output computation.
  // bool is_active(const CSubProblem*) is in python
  // void find_active(const CSubProblem*) is in python
  void cache_active(const CSubProblem*, bool);
  bool currently_active(const CSubProblem*) const; // returns cached value
  bool is_computable(const CSubProblem*) const;
  // void find_computable(const CSubProblem*);
  // bool currently_computable(const CSubProblem*) const;
  void cache_nonlinearity(const CSubProblem*, bool);
  bool currently_nonlinear(const CSubProblem*) const;

  // List of fields required to compute this Property
  const std::vector<const Field*> &fields_required() const {
    return fields_reqd;
  }
  // This field is required to compute this Property.  The derived
  // Properties don't call this directly, since they don't necessarily
  // know about compound Fields.  Instead, the Properties call
  // Field::registerProperty(Property*), which calls
  // Property::require_field().  This is done automatically in
  // Property::bookkeeping() (in property.spy), which is called by
  // Material::cross_reference().
  void require_field(const Field&);

  // The remaining virtual functions have default null bodies, so that
  // each Property only has to define the relevant ones:

  // Properties may need to find other properties in the material
  // (using Material::fetchProperty).  This function is called to tell
  // them that it's time to do that. It should throw an exception if
  // it's unsuccessful.
  virtual void cross_reference(Material*) {}

  // compute things that don't depend on Element.  The argument is
  // non-const so that FEMesh::set_property_data can be used.
  // TODO: Some properties redefine a trivial precompute(). Why?  Delete it.
  virtual void precompute(FEMesh*) {}

  virtual bool constant_in_space() const { return true; }

  // These routines allow Properties to precompute and store
  // mesh-specific data.  Since Materials and Properties are shared
  // between Meshes, Properties can't store mesh-specific data
  // themselves.  set_mesh_data stores data in the Mesh, and
  // get_mesh_data retrieves it. clear_mesh_data is a callback, called
  // when the Mesh is being destroyed or the data is being overwritten.
  void set_mesh_data(FEMesh*, void *) const;
  void *get_mesh_data(const FEMesh*) const;
  virtual void clear_mesh_data(FEMesh*, void*) const {}

  // These functions are called when beginning and ending the
  // computations on an Element, allowing Element-dependent
  // precomputation and caching.
  // TODO: Should begin_element return a void* that is passed in to
  // the other methods, like FluxProperty::begin_point?
  virtual void begin_element(const CSubProblem*, const Element*) {}
  virtual void end_element(const CSubProblem*, const Element*) {}

  // This function is called after equilibration, to allow the
  // computation of auxiliary fields which may depend on equilibrium
  // fluxes -- the canonical example is plasticity, where the yield
  // condition is stress-dependent.
  virtual void post_process(CSubProblem *, const Element *) const {}


  // Output function.
  virtual void output(FEMesh*, const Element*, const PropertyOutput*,
		      const MasterPosition&, OutputVal*)
    { return; }

  // TODO?  These belong more naturally in PhysicalProperty, but
  // putting them there breaks the is_symmetric_X methods defined in
  // material.spy.  Those methods loop over all Properties, including
  // AuxiliaryProperties.  One could argue that AuxiliaryProperties
  // *are* symmetric, since they don't actually affect the matrices.
  virtual bool is_symmetric_K(const CSubProblem*) const;
  virtual bool is_symmetric_C(const CSubProblem*) const;
  virtual bool is_symmetric_M(const CSubProblem*) const;

}; // end of Property class definition

std::ostream &operator<<(std::ostream &, const Property&);


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


// class InterfaceProperty: public Property
// {
// public:
//   InterfaceProperty(const std::string &nm, PyObject *registration):
//     Property(nm, registration)
//   {}
//   virtual ~InterfaceProperty() {}
// };


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

class AuxiliaryProperty: public Property {
public:
  AuxiliaryProperty(const std::string &nm, PyObject *registration)
    : Property(nm, registration)
  {}
};

class PhysicalProperty: public Property {
public:
  PhysicalProperty(const std::string &nm, PyObject *registration)
    : Property(nm, registration)
  {}
  // this function returns the polynomial order (in x and y) of the
  // quantity computed by flux_matrix.
  virtual int integration_order(const CSubProblem*, const Element*) const = 0;
};


class FluxProperty: public PhysicalProperty {
public:
  FluxProperty(const std::string &nm, PyObject *registration)
    : PhysicalProperty(nm,registration)
  {}

  // The flux is currently considered to have the following form
  //
  //    flux = K(x,u,Du) Du + sigma_0(x,u,Du) + C Du^dot
  //
  // where u is the field and Du is its gradient, and Du^dot is the
  // time derivative of Du.
  //
  // K(x,u,Du) is the linearization/derivative of the flux
  // with respect to Du and is typically only x-dependent for linear
  // problems. sigma_0(x,u,Du) is the flux offset that captures
  // remaining dependences on u & Du. The following is true by definition
  //
  //    sigma(x,u,Du) = K(x,u,Du) Du + C(x) Du^dot + sigma_0(x,u,Du)
  //

  void make_flux_contributions(const FEMesh*, const Element*,
			       const Flux*,
			       const MasterPosition&, double time,
			       const CNonlinearSolver*,
			       void *, SmallSystem*)
    const;

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
  
  // Redefining each of the following four methods is optional in
  // derived classes, but if the FluxProperty is to have an effect,
  // either flux_matrix or flux_offset must be redefined.  The methods
  // all store their results in the passed-in SmallSystem object.

  // Linearization/derivative of the flux with respect to field and
  // field derivatives.  Used to assemble the stiffness matrix and the
  // Jacobian matrix. 
  virtual void flux_matrix(const FEMesh*, const Element*,
			   const ElementFuncNodeIterator&,
			   const Flux*, const MasterPosition&,
			   double time, void*, SmallSystem*) const
  {}

  // Value of the flux when Du and Du^dot are zero.
  virtual void flux_offset(const FEMesh*, const Element*,
			   const Flux*, const MasterPosition&,
			   double time, void*, SmallSystem*) const
  {}

  // The actual value of the flux at the given element and given
  // point.  The default definition computes the flux from the flux
  // matrix and offset.  Specialized properties can redefine it.
  virtual void flux_value(const FEMesh*, const Element*,
			  const Flux*, const MasterPosition&,
			  double time, void*, SmallSystem*) const;
  

  // The static portion of the flux vector/tensor, equal to flux_value
  // for most cases, but not for viscoelasticity.  The default
  // implementation returns flux_value.
  
  // oof2 assumes that nonlinearities in a FluxProperty only depend on
  // the field and its gradient, not on its time derivative.  The
  // nonlinear solvers need to compute the static part of the flux in
  // order to find the residual at each step.  static_flux_value needs
  // to be redefined in any FluxProperty subclass that is both
  // non-linear and dependent on the time derivative of an active
  // field.
  virtual void static_flux_value(const FEMesh*, const Element*,
				 const Flux*, const MasterPosition&,
				 double time, void*, SmallSystem*) const;

  //=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

  // These functions are called from material.C before and after the
  // flux contributions are requested.  If properties have
  // per-evaluation-point expensive operations they want to perform,
  // they should do them in these functions.  An object allocated and
  // returned by begin_point is passed to all the FluxProperty
  // methods, and can be deallocated by end_point.

  virtual void* begin_point(const FEMesh*, const Element*,
			    const Flux*, const MasterPosition&, double) const
  {
    return nullptr;
  }
  virtual void end_point(const FEMesh*, const Element*,
			 const Flux*, const MasterPosition&, double, void*)
    const
  {}

}; // end of FluxProperty class definition


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


class EqnProperty: public PhysicalProperty {

public:
  EqnProperty(const std::string &nm, PyObject *registration)
    : PhysicalProperty(nm,registration)
  {};

  void make_equation_contributions(const FEMesh*, const Element*,
				   const Equation*,
				   const MasterPosition&,
				   double time,
				   const CNonlinearSolver*,
				   void*,
				   SmallSystem*)
    const;

  // A derived class can optionally redefine any of these functions.
  // It must redefine at least one of them if it is to have any
  // effect.

  // The linearization/derivative of force with respect to field.
  virtual void force_deriv_matrix(const FEMesh*, const Element*,
				  const Equation*,
				  const ElementFuncNodeIterator&,
				  const MasterPosition&,
				  double time,
				  void*, 
				  SmallSystem*) const
  {}

  // The value of the force at a given element and given point.
  virtual void force_value(const FEMesh*, const Element*,
			   const Equation*, const MasterPosition&,
			   double time, void*, SmallSystem*)
    const {}

  // Contributions to the coefficient of the 1st time-deriv of the field.
  // An example of this is heat capacity.
  virtual void first_time_deriv_matrix(const FEMesh*, const Element*,
				       const Equation*,
				       const ElementFuncNodeIterator&,
				       const MasterPosition&,
				       double time,
				       void*,
				       SmallSystem*)
    const {}

  // Contributions to the coefficient of the 2nd time-deriv of the field.
  // An example of this is mass density.
  virtual void second_time_deriv_matrix(const FEMesh*, const Element*,
					const Equation*,
					const ElementFuncNodeIterator&,
					const MasterPosition&,
					double time,
					void*,
					SmallSystem*)
    const {}

  // These functions are called from material.C before and after the
  // equation contributions are requested.  If properties have
  // per-evaluation-point expensive operations they want to perform,
  // they should do them in these functions.
  virtual void* begin_point(const FEMesh*, const Element*,
			   const Equation*, const MasterPosition&,
			   double time) const
  {
    return nullptr;
  }
  virtual void end_point(const FEMesh*, const Element*,
			 const Equation*, const MasterPosition&,
			 double time, void*) const
  {}
  
}; // end of EqnProperty class definition

#endif	// PROPERTY_H
