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

#include "common/pythonlock.h"
#include "common/smallmatrix.h"
#include "common/trace.h"
#include "engine/csubproblem.h"
#include "engine/edge.h"
#include "engine/element.h"
#include "engine/equation.h"
#include "engine/femesh.h"
#include "engine/flux.h"
#include "engine/fluxnormal.h"
#include "engine/indextypes.h"
#include "engine/material.h"
#include "engine/nodalequation.h"
#include "engine/ooferror.h"
#include "engine/outputval.h"
#include "engine/smallsystem.h"
#include "engine/symmmatrix.h"

std::vector<Flux*> &Flux::allfluxes() {
  static std::vector<Flux*> all_fluxes;
  return all_fluxes;
}

Flux *getFluxByIndex(int index) {
  return Flux::allfluxes()[index];
}

int countFluxes() {
  return Flux::allfluxes().size();
}

Flux *Flux::getFlux(const std::string &name) {
  const std::vector<Flux*> &list = allfluxes();
  for(std::vector<Flux*>::size_type i=0; i<list.size(); i++) {
    if(list[i]->name() == name) {
      return list[i];
    }
  }
  throw ErrProgrammingError("Unknown Flux \"" + name + "\"",
			    __FILE__, __LINE__);
}

Flux::Flux(const std::string &nm, int d, int dvdim)
  : name_(nm),
    negate_(false),
    dim(d),
    divdim(dvdim)
{
  index_ = allfluxes().size();
  allfluxes().push_back(this);
}

Flux::Flux(const std::string &nm, int d, int dvdim, bool neg)
  : name_(nm),
    negate_(neg),
    dim(d),
    divdim(dvdim)
{
  index_ = allfluxes().size();
  allfluxes().push_back(this);
}

bool operator==(const Flux &fluxa, const Flux &fluxb) {
  return fluxa.index_ == fluxb.index_;
}

bool operator!=(const Flux &fluxa, const Flux &fluxb) {
  return fluxa.index_ != fluxb.index_;
}

std::ostream &operator<<(std::ostream &os, const Flux &flux) {
  os << "Flux(" << flux.name() << ")";
  return os;
}

void Flux::addEquation(Equation *eqn) {
  // Add eqn to the list of equations in which this flux appears, but
  // first make sure that it's not already in the list.
  for(std::vector<Equation*>::size_type i=0; i<eqnlist.size(); i++) {
    if(eqnlist[i] == eqn) return;
  }
  eqnlist.push_back(eqn);
}

SmallSystem *Flux::initializeSystem(const Element *el) const {
  return new SmallSystem(dim, el->ndof());
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

const std::string &VectorFlux::classname() const {
  static std::string name_("VectorFlux");
  return name_;
}

const std::string &SymmetricTensorFlux::classname() const {
  static std::string name_("SymmetricTensorFlux");
  return name_;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ComponentsP VectorFlux::components(Planarity planarity) const {
  static const VectorFieldComponents allcomps(0, 3);
  static const VectorFieldComponents inplane(0, 2);
  static const VectorFieldComponents outofplane(2, 3);
  if(planarity == ALL_INDICES)
    return ComponentsP(&allcomps);
  if(planarity == IN_PLANE)
    return ComponentsP(&inplane);
  return ComponentsP(&outofplane);
}

ComponentsP VectorFlux::divergenceComponents() const {
  static const ScalarFieldComponents comp;
  return ComponentsP(&comp);
}

ComponentsP VectorFlux::outOfPlaneComponents() const {
  static OutOfPlaneVectorFieldComponents comp(3);
  return ComponentsP(&comp);
}

FieldIndex *VectorFlux::getIndex(const std::string &str) const {
  return new VectorFieldIndex(str[0] - 'x');
}

FieldIndex *VectorFlux::getOutOfPlaneIndex(const std::string &str) const {
  return new OutOfPlaneVectorFieldIndex(str[0] - 'x');
}

FieldIndex *VectorFlux::divergence_getIndex(const std::string&) const {
  return new ScalarFieldIndex();
}

ComponentsP SymmetricTensorFlux::components(Planarity planarity) const {
  static const SymTensorComponents allcomps;
  static const SymTensorInPlaneComponents inplane;
  static const SymTensorOutOfPlaneComponents outofplane;
  if(planarity == ALL_INDICES)
    return ComponentsP(&allcomps);
  if(planarity == IN_PLANE)
    return ComponentsP(&inplane);
  return ComponentsP(&outofplane);
}

ComponentsP SymmetricTensorFlux::divergenceComponents() const {
  // TODO: This just returns the in-plane components.  Is that
  // correct?  It's currently only used in situations in which the
  // in-plane components are desired, but possibly the planarity
  // should be passed as an argument.  It's used in
  // DivergenceEquation::components() and
  // IntegrateBdyFlux::columnNames().
  static const VectorFieldComponents comps(0, 2);
  return ComponentsP(&comps);
}

ComponentsP SymmetricTensorFlux::outOfPlaneComponents() const {
  static const OutOfPlaneSymTensorComponents comps;
  return ComponentsP(&comps);
}

FieldIndex *SymmetricTensorFlux::getIndex(const std::string &str) const {
  return new SymTensorIndex(SymTensorIndex::str2voigt(str));
}

FieldIndex *SymmetricTensorFlux::getOutOfPlaneIndex(const std::string &str)
  const
{
  return new OutOfPlaneSymTensorIndex(SymTensorIndex::str2voigt(str));
}

FieldIndex *SymmetricTensorFlux::divergence_getIndex(const std::string &str)
  const
{
  return new VectorFieldIndex(str[0] - 'x');
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

DoubleVec *Flux::evaluate(const FEMesh *mesh,
			  const Element *el,
			  const MasterPosition &pos) const
{
  DoubleVec *result = new DoubleVec(dim, 0.0);
  if (el->material()!=NULL) {

    if (!el->material()->self_consistent())
      throw ErrBadMaterial(el->material()->name());

    SmallSystem *fluxdata = initializeSystem(el);
    el->material()->find_fluxdata(mesh, el, this, pos, fluxdata);
    *result = fluxdata->fluxVector(); // copy!
    
    delete fluxdata;
  }
  return result;
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

int Flux::eqn_integration_order(const CSubProblem *subp, const Element *el)
  const
{
  int order = 0;
  for(std::vector<Equation*>::size_type i=0; i<eqnlist.size(); ++i) {
    Equation *eqn = eqnlist[i];
    if(subp->is_active_equation(*eqn)) {
      int ord = eqn->integration_order(el);
      if(ord > order)
	order = ord;
    }
  }
  return order;
}

// Flux boundary condition uses the same mechanism as the stiffness
// matrix, only it makes its contribution to the boundary right-hand-side,
// rather than to the global stiffness matrix.
void Flux::boundary_integral(const CSubProblem *subp, LinearizedSystem *ls,
			     const BoundaryEdge *ed,
			     const EdgeGaussPoint &egp,
			     const FluxNormal *flxnormal) const
{
  for(std::vector<Equation*>::size_type i=0; i<eqnlist.size(); i++) {
    Equation *eq = eqnlist[i];
    if(subp->is_active_equation(*eq)) {
      eq->boundary_integral(subp, ls, this, ed, egp, flxnormal);
    }
  }
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


// Contraction maps are used by the Divergence equation to map between
// equation components and flux components.  Since they're only really
// geometry-dependent, they can be precomputed at flux-construction
// time.  The same voigt stuff is already coded into the
// SymTensorIndex object, and in principle it could be re-used instead
// of re-created here, so that if voigt order ever changes, we only
// have to do change it in one place.
std::vector< std::vector<int> >
SymmetricTensorFlux::build_contraction_map()  {

  // This just constructs and returns the voigt index matrix:
  //   0 5 4
  //   5 1 3
  //   4 3 2

  std::vector<int> res0(3,0);
  // This 0 ----------^ is the equation component
  res0[0]=0;  // sigma_00
  res0[1]=5;  // sigma_10
  res0[2]=4;  // sigma_20

  std::vector<int> res1(3,0);
  // This 1 ----------^ is the equation component
  res1[0]=5;  // sigma_01
  res1[1]=1;  // sigma_11
  res1[2]=3;  // sigma_21

  std::vector<int> res2(3,0);
  res2[0]=4;  // sigma_02
  res2[1]=3;  // sigma_12
  res2[2]=2;  // sigma_22

  std::vector< std::vector<int> > res(3);
  res[0]=res0;
  res[1]=res1;
  res[2]=res2;

  return res;
}

std::vector< std::vector<int> > SymmetricTensorFlux::contraction_map_ = \
  SymmetricTensorFlux::build_contraction_map();

std::vector<int> SymmetricTensorFlux::contraction_map(int eqcomp) const {
  return SymmetricTensorFlux::contraction_map_[eqcomp];
}



// This outofplane_map presents the z-column of the tensor in
// Voigt-index order, which means that sigma_zz is first and sigma_xz
// is last.  This appears backwards, but because the rest of the code
// assumes Voigt order, it's the right thing to do here.  This
// ordering makes the conjugacy code's assumption of Voigt ordering
// correct, and allows it to symmetrize the resulting matrix
// correctly.
std::vector<int> SymmetricTensorFlux::build_outofplane_map()  {
  std::vector<int> res(3,0); //
  res[0]=2;  // sigma_22
  res[1]=3;  // sigma_12
  res[2]=4;  // sigma_02
  return res;
}

std::vector<int> SymmetricTensorFlux::outofplane_map_ = \
  SymmetricTensorFlux::build_outofplane_map();

const std::vector<int> &SymmetricTensorFlux::outofplane_map() const {
  return SymmetricTensorFlux::outofplane_map_;
}



std::vector<int> VectorFlux::build_contraction_map() {
 std::vector<int> res(3,0);
  res[0]=0; res[1]=1; res[2]=2;
  return res;
}

std::vector<int> VectorFlux::contraction_map_ = \
  VectorFlux::build_contraction_map();

std::vector<int> VectorFlux::contraction_map(int comp) const {
  return VectorFlux::contraction_map_; // Discard argument.
}



std::vector<int> VectorFlux::build_outofplane_map() {
  std::vector<int> res(1,0); //
  res[0]=2;  // Trivial map, z component.
  return res;
}

std::vector<int> VectorFlux::outofplane_map_ = \
  VectorFlux::build_outofplane_map();

const std::vector<int> &VectorFlux::outofplane_map() const {
  return VectorFlux::outofplane_map_;
}



// Local_boundary function is the analogue of the local_stiffness
// function, except that it's much simpler.  The core assumption here
// is that the components of the equation will match up with
// components of the flux normal in the obvious way, so that the sizes
// will match and the assignment will be straightforward.
void SymmetricTensorFlux::local_boundary(const BoundaryEdge *ed,
					 EdgeNodeIterator& edi,
					 const EdgeGaussPoint &egp,
					 const FluxNormal *flxnormal,
					 DoubleVec& rhs) const {

  const SymTensorFluxNormal *flxn =
    dynamic_cast<const SymTensorFluxNormal*>(flxnormal);
  // Check size of rhs -- has to be 2 for this flux.
  int rhssize = rhs.size();
  if (rhssize == SYMTEN_DIV_DIM) {
    if (flxn->size() == rhssize) { // Simple case, do the obvious.
      double sfvalue = edi.shapefunction(egp);
      rhs[0] = sfvalue * flxn->x;
      rhs[1] = sfvalue * flxn->y;
    }
  }
}


// Evaluate the dot product of the flux with the normal at
// the indicated edge gauss point.
ArithmeticOutputVal *SymmetricTensorFlux::contract(const FEMesh *mesh,
						   const Element *elmt,
						   const EdgeGaussPoint &egpt)
  const
 {
   ArithmeticOutputValue value = output( mesh, elmt, egpt );
   const SymmMatrix3 &valueRef =
     dynamic_cast<const SymmMatrix3&>(value.valueRef());
   Coord normal2 = egpt.normal();
   // Pretend the normal is a 3-vector so that we can dot it with the flux.
   DoubleVec normal3(3, 0.0);
   normal3[0] = normal2(0);
   normal3[1] = normal2(1);
   // Take the dot product.
   DoubleVec resultvec(valueRef*normal3);
   // Convert the result into an OutputVal, dropping the z-component.
   VectorOutputVal *result = new VectorOutputVal(2);
   (*result)[0] = resultvec[0];
   (*result)[1] = resultvec[1];
   return result;
//   DoubleVec *value = evaluate(mesh, elmt, egpt);
//   // voigt order, 00, 11, 22, 12, 02, 01
//   DoubleVec *result = new DoubleVec(divdim, 0.0);
//   Coord normal = egpt.normal();
//   (*result)[0] = (*value)[0]*normal(0) + (*value)[5]*normal(1);
//   (*result)[1] = (*value)[5]*normal(0) + (*value)[1]*normal(1);
//   delete value;  // deleting new'd DoubleVec from "evaluate".
//   return result;
}

FluxNormal *SymmetricTensorFlux::BCCallback(const Coord &pos,
					    double time,
					    const Coord &nrm,
					    const double distance,
					    const double fraction,
					    PyObject *wrapper,
					    const PyObject *pyfunction)
  const {

  Coord cres;

  PYTHON_THREAD_BEGIN_BLOCK;
  PyObject *result = PyObject_CallFunction(wrapper,  "(Oddddddd)",
					   pyfunction, pos(0), pos(1), time,
					   nrm(0), nrm(1), distance, fraction);
  if(result) {
    if(PyTuple_Check(result)) {
      if(PyTuple_Size(result) == (Py_ssize_t) 2) {
	cres(0) = PyFloat_AsDouble(PyTuple_GetItem(result, (Py_ssize_t) 0));
	cres(1) = PyFloat_AsDouble(PyTuple_GetItem(result, (Py_ssize_t) 1));
      }
      else {
	throw
	  ErrSetupError(
		       "SymmetricTensorFlux::BCCallback: Wrong size of tuple.");
      }
    }
    else {
      throw ErrSetupError("SymmetricTensorFlux::BCCallback: Expected a tuple.");
    }
  }
  else {		    // !result.  PyObject_CallFunction failed.
    pythonErrorRelay();
  }
  Py_XDECREF(result);
  return new SymTensorFluxNormal(cres(0),cres(1));
}

ArithmeticOutputValue Flux::output(const FEMesh *mesh, const Element *el,
				   const MasterPosition &pos) const
{
  // std::cerr << "Flux::output: pos=" << pos << " el=" << *el << std::endl;
  DoubleVec *fluxvals = evaluate( mesh, el, pos );
  ArithmeticOutputValue ov = newOutputValue();
  for(IndexP it : components(ALL_INDICES)) 
    ov[it] = (*fluxvals)[it.integer()];
  delete fluxvals;
  // When we started using Eigen's matrix solvers, we learned that we
  // had been constructing *negative* definite matrices for the force
  // balance equation.  The previous CG solver worked with them, but
  // Eigen didn't.  Changing the sign of the force balance equation
  // fixed the problem, but required changing the sign of the Stress.
  // To make this sign change invisible to users, the sign is switched
  // back here and in NeumannBCApp::integrate.
  if(negate_)
    return -1.0*ov;
  return ov;
}

ArithmeticOutputValue SymmetricTensorFlux::newOutputValue() const {
  return ArithmeticOutputValue(new SymmMatrix3());
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ArithmeticOutputValue VectorFlux::newOutputValue() const {
  return ArithmeticOutputValue(new VectorOutputVal(ndof()));
}


// The VectorFlux boundary condition calls the correct wrapper
// for its callback, and assumes the components match up
// trivially, in the absence of indications otherwise from
// the equation.
void VectorFlux::local_boundary(const BoundaryEdge *ed,
				EdgeNodeIterator& edi,
				const EdgeGaussPoint &egp,
				const FluxNormal *flxnormal,
				DoubleVec& rhs) const {
  // Size.
  const VectorFluxNormal *flxn =
    dynamic_cast<const VectorFluxNormal*>(flxnormal);
  int rhssize = rhs.size();
  if (rhssize == VEC_DIV_DIM) {
    if (flxn->size() == rhssize) {
      rhs[0] = edi.shapefunction(egp) * flxn->value();
    }
  }
}


// Evalute the dot product of the flux with the normal at the
// indicated gauss point.
ArithmeticOutputVal *VectorFlux::contract(const FEMesh *mesh,
					  const Element *elmt,
					  const EdgeGaussPoint &egpt)
  const
{
  ArithmeticOutputValue value = output( mesh, elmt, egpt );
  const VectorOutputVal &valueRef =
    dynamic_cast<const VectorOutputVal&>(value.valueRef());
  Coord normal = egpt.normal();
  std::vector<double> normalvec(3);
  normalvec[0] = normal(0);
  normalvec[1] = normal(1);
  normalvec[2] = 0.0;
  return new ScalarOutputVal(valueRef.dot(normalvec));
//   DoubleVec *value = evaluate(mesh, elmt, egpt);
//   Coord normal = egpt.normal();
//   DoubleVec *result = new DoubleVec(divdim, 0.0);
//   (*result)[0] = (*value)[0]*normal(0) + (*value)[1]*normal(1);
//   return result;
}


FluxNormal *VectorFlux::BCCallback(const Coord &pos,
				   double time,
				   const Coord &nrm,
				   const double distance,
				   const double fraction,
				   PyObject *wrapper,
				   const PyObject *pyfunction) const {
  double dres = 0.0;

  PYTHON_THREAD_BEGIN_BLOCK;
  PyObject *result = PyObject_CallFunction(wrapper, "(Oddddddd)",
					   pyfunction, pos(0), pos(1), time,
					   nrm(0), nrm(1), distance, fraction);
  if(result) {
    if(PyTuple_Check(result)) {
      if(PyTuple_Size(result)==1) {
	dres = PyFloat_AsDouble(PyTuple_GET_ITEM(result, (Py_ssize_t) 0));
      }
      else {
	// Only one "release" per possible control-flow path.
	throw
	  ErrSetupError("VectorFlux::BCCallback: Wrong size of tuple.");
      }
    }
    else {
      throw ErrSetupError("VectorFlux::BCCallback: Expected a tuple.");
    }
  }
  else {		    // !result.  PyObject_CallFunction failed.
    pythonErrorRelay();
  }

  Py_XDECREF(result);
  return new VectorFluxNormal(dres);
}
