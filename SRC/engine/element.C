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
#include "common/cmicrostructure.h"
#include "common/doublevec.h"
#include "common/ooferror.h"
#include "common/printvec.h"
#include "common/pythonlock.h"
#include "common/pyutils.h"
#include "common/tostring.h"
#include "common/trace.h"
#include "engine/cnonlinearsolver.h"
#include "engine/cskeleton.h"
#include "engine/csubproblem.h"
#include "engine/edge.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/flux.h"
#include "engine/linearizedsystem.h"
#include "engine/masterelement.h"
#include "engine/material.h"
#include "engine/nodalequation.h"
#include "engine/node.h"
#include "engine/ooferror.h"
#include "engine/outputval.h"
#include "engine/shapefunction.h"
#include <string>
#include <vector>

// ElementData constructors.
ElementData::ElementData(const std::string &nm)
  : name_(nm)
{}

Element::Element(PyObject *skelel, CSkeletonElement *cskelel,
		 const MasterElement &me,
		 const std::vector<Node*> *nl, const Material *mat)
  : master(me),
    nodelist(*nl),
    matl(mat),
    exterior_edges(nullptr),
    skeleton_element(skelel),
    cskeleton_element(cskelel)
{

//   Trace("Element::Element " + me.name());
//   int nn = me.nnodes();
//   for(int i=0; i<nn; i++) {
//     nodelist[i] = (*nl)[i];
//   }
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_XINCREF(skeleton_element);
}

Element::~Element() {
  for(unsigned int i=0; i<edgeset.size(); i++)
    delete edgeset[i];
  delete exterior_edges;
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_XDECREF(skeleton_element);
}

const std::string *Element::repr() const {
  std::string *rep =  new std::string(master.name());
  for(int i=0; i<nnodes(); i++)
    *rep += " " + tostring(*nodelist[i]);
  return rep;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Index stuff.

void Element::set_index(int i) {
  index_=i;
}

int Element::get_index() const {
  return index_;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

int Element::nnodes() const { return master.nnodes(); }
int Element::nmapnodes() const { return master.nmapnodes(); }
int Element::nfuncnodes() const { return master.nfuncnodes(); }
int Element::ncorners() const { return master.ncorners(); }
int Element::nexteriorfuncnodes() const { return master.nexteriorfuncnodes(); }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// refreshMaterial() is called when Materials have been reassigned in
// a Microstructure after the FEMesh has been created.  The Elements
// need to ask their SkeletonElements for the new Material.  It's not
// sufficient to get the Material from the SkeletonElement's dominant
// pixel, because a material might have been assigned to an element
// group.

void Element::refreshMaterial(PyObject *skeletoncontext) {
  PYTHON_THREAD_BEGIN_BLOCK;
  // It would be nice to call SkeletonElement.material() here, but
  // something goes wrong in swig when we try that when using python 3.11.
  PyObject *method = PyUnicode_FromString("materialName");
  PyObject *pymatname = PyObject_CallMethodObjArgs(skeleton_element,
						   method,
						   skeletoncontext, NULL);
  if(!pymatname) {
    pythonErrorRelay();
  }
  if(pymatname == Py_None) {
    matl = nullptr;
  }
  else {
    std::string matname = pyStringAsString(pymatname);
    matl = getMaterialByName(matname);
  }
  Py_XDECREF(method);
  Py_XDECREF(pymatname);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Actually construct the linear system object.  Called from
// CSubProblem::make_linear_system.

void Element::make_linear_system(const CSubProblem *const subproblem,
				 double time,
				 const CNonlinearSolver *nlsolver,
				 LinearizedSystem &system) const
{
  std::vector<int> dofmap = localDoFmap();

  const Material *mat = material();
  if(mat) {
    mat->begin_element(subproblem, this);
    // TODO OPT?: iorder could be precomputed or cached, but do some
    // careful profiling before changing anything.  Preliminary tests
    // indicate that the time spent computing iorder is negligible.
    int iorder = mat->integrationOrder(subproblem, this);

    // TODO OPT MAYBE: Use different integration orders for different
    // equations and properties.  That might make precomputations
    // difficult.
    for(GaussPoint gpt : integrator(iorder)) {
      mat->make_linear_system( subproblem, this, gpt, dofmap, time,
			       nlsolver, system );
    }    
    mat->end_element(subproblem, this);
  }
}



// The InterfaceElement's make_linear_system does two passes, one
// for the left side and one for the right side.  Sidedness is
// manifested in the behavior of the funcnode iterator.  Do this only
// if you have a material -- otherwise, your nodes are not split.
void InterfaceElement::make_linear_system(const CSubProblem *const subproblem,
					  double time,
					  const CNonlinearSolver *nlsolver,
					  LinearizedSystem &system) const
{
  std::vector<int> dofmap = localDoFmap();
  const Material *mat = material();
  
  if(mat) {
    // std::cerr << "Inside InterfaceElement::make_linear_system with a material." << std::endl;
    mat->begin_element(subproblem,this);
    int iorder = mat->integrationOrder(subproblem,this);

    current_side = LEFT;
    // std::cerr << "InterfaceElement::make_linear_system, left-side gp loop." << std::endl;
    for(GaussPoint gpt : integrator(iorder)) {
      mat->make_linear_system( subproblem, this, gpt, dofmap, time,
			       nlsolver, system );
    }    

    current_side = RIGHT;
    // std::cerr << "InterfaceElement::make_linear_system, right-side gp loop." << std::endl;
    for(GaussPoint gpt : integrator(iorder)) {
      mat->make_linear_system( subproblem, this, gpt, dofmap, time,
			       nlsolver, system );
    }
   
    current_side = LEFT;  // Return stateful objects to their initial state..

    mat->end_element(subproblem,this);
  }
}
					  

// Post-processing, which is after equilibration.
void Element::post_process(CSubProblem *subproblem) const {
  const Material *mat = material();
  if(mat) {
    mat->post_process(subproblem, this);
  }
}

// void Element::begin_material_computation(FEMesh *mesh) const {
//   const Material *mat = material();
//   if(mat)
//     mat->begin_element(mesh, this);
// }

// void Element::end_material_computation(FEMesh *mesh) const {
//   const Material *mat = material();
//   if(mat)
//     mat->end_element(mesh, this);
// }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

int Element::appendData(ElementData *x) const {
  el_data.push_back(x);
  return el_data.size()-1;
}

void Element::setData(int i, ElementData *x) const {
  el_data[i]=x;
}

ElementData *Element::getData(int i) const {
  return el_data[i];
}


// This call does retrieval-by-name, and so should be used
// as infrequently as can be managed.
ElementData *Element::getDataByName(const std::string &name) const {
  int i=getIndexByName(name);
  if (i>=0)
    return getData(i);
  else
    return 0;
}

// Overwrites the data indexed under the indicated name, appends
// it, whichever.
void Element::setDataByName(ElementData *x) const {
  int i=getIndexByName(x->name());
  if (i>=0)
    // NB Does this overwrite have implications for reference counts
    // of the referred-to Python data?
    setData(i,x);
  else
    appendData(x);
}


// Retrieval by name should be done infrequently, to avoid the search.
int Element::getIndexByName(const std::string &searchname) const {
  for(std::vector<ElementData*>::size_type i=0; i<el_data.size(); i++) {
    if (el_data[i]->name() == searchname) {
      return i;
    }
  }
  // Not found -- this is permissible, return something.
  return -1;
}



// Deletion functions do not remove the pointed-to object, they just
// remove the ElementData* from the element object's local array.
void Element::delData(int i) const {
  std::vector<ElementData*>::iterator it = el_data.begin();
  it += i;
  el_data.erase(it);
}

void Element::delDataByName(const std::string &name) const {
  std::vector<ElementData*>::iterator it = el_data.begin();
  int i=getIndexByName(name);
  it += i;
  el_data.erase(it);
}

void Element::clearData() const {
  el_data.clear();
}



//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ElementNodeIterator Element::node_iterator() const {
  return ElementNodeIterator(*this);
}

ElementMapNodeIterator Element::mapnode_iterator() const {
  return ElementMapNodeIterator(*this);
}

// This returns a pointer, so that the caller can get either an
// ElementFuncNodeIterator or an InterfaceElementFuncNodeIterator with
// appropriate sidedness, according to context.  This uglifies some of
// the loops.  TODO LATER: Making a templated clever pointer container
// with deletion-on-scope-exit semantics might help to re-prettify
// them.
ElementFuncNodeIterator *Element::funcnode_iterator() const {
  return new ElementFuncNodeIterator(*this);
}

ElementCornerNodeIterator Element::cornernode_iterator() const {
  return ElementCornerNodeIterator(*this);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// conversion between real coordinates and master element coordinates

Coord Element::from_master(const MasterPosition &mc) const {
  Coord p(0., 0.);
  for(ElementMapNodeIterator n=mapnode_iterator(); !n.end(); ++n) {
    p += n.shapefunction(mc) * n.node()->position();
  }
  return p;
}

static const double tolerancesq = 1.e-10; // should be settable by user
static const int maxiter = 100;	// should also be settable by user

MasterCoord Element::to_master(const Coord &x) const {
  // Use Newton's method to solve from_master(xi) - x = 0 for xi.
  // xi -> xi + J^-1 * (x - from_master(xi))
  MasterCoord xi(0, 0);
  Coord dx = x - from_master(xi);
  int iter = 0;
  do {				// Newton iteration
    double jac[DIM][DIM]; // use simple matrix repr. for 2x2
    for(SpaceIndex i=0; i<DIM; ++i)
      for(SpaceIndex j=0; j<DIM; ++j)
	jac[i][j] = jacobian(i, j, xi);

    double dj = jac[0][0]*jac[1][1] - jac[0][1]*jac[1][0];
    dj = 1./dj;
    // xi --> xi + J^-1*(x - from_master(xi))
    xi(0) += ( jac[1][1]*dx(0) - jac[0][1]*dx(1))*dj;
    xi(1) += (-jac[1][0]*dx(0) + jac[0][0]*dx(1))*dj;
    dx = x - from_master(xi);	// reevaluate rhs
  } while((norm2(dx) > tolerancesq) && (++iter < maxiter));
  return xi;
}

// Superconvergent patch recovery
int Element::nSCpoints() const {
  return master.nSCpoints();
}

const MasterCoord &Element::getMasterSCpoint(int i) const {
  return master.getSCpoint(i);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double Element::Jdmasterdx(SpaceIndex i, SpaceIndex j, const GaussPoint &g)
  const
{
  //         | J11  -J01 |
  //  J^-1 = |           | / |J|
  //         |-J10   J00 |

  double sum = 0;
  if(i == j) {
    int ii = 1 - i;
    for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni) {
      sum += (ni.node()->position())(ii) * ni.masterderiv(ii, g);
    }
  }
  else {			// i != j
    for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni)
      sum -= (ni.node()->position())(i) * ni.masterderiv(j, g);
  }
  return sum;

}

double Element::Jdmasterdx(SpaceIndex i, SpaceIndex j, const MasterCoord &mc)
  const
{
  double sum = 0;
  if(i == j) {
    int ii = 1 - i;
    for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni)
      sum += (ni.node()->position())(ii) * ni.masterderiv(ii, mc);
  }
  else {			// i != j
    for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni)
      sum -= (ni.node()->position())(i) * ni.masterderiv(j, mc);
  }
  return sum;
}


double Element::Jdmasterdx(SpaceIndex i, SpaceIndex j, const Coord &coord)
  const
{
  return Jdmasterdx(i, j, to_master(coord));
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// J(i,j) = d(real_coord i)/d(master_coord j)

double Element::jacobian(SpaceIndex i, SpaceIndex j, const GaussPoint &g) const
{
  double jac = 0.0;
  for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni)
    jac += (ni.node()->position())(i) * ni.masterderiv(j, g);

  return jac;
}

double Element::jacobian(SpaceIndex i, SpaceIndex j, const MasterCoord &mc)
  const
{
  double jac = 0.0;
  for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni)
    jac += (ni.node()->position())(i) * ni.masterderiv(j, mc);
  return jac;
}


// The jacobian is sort of brutally hacked -- we have a 2x2 matrix to
// work with, but we only need one, because we have (x,y) coords as a
// function of a single master-space variable.  So, just use the first
// column.  Also, we over-ride the determinant function, and use it to
// compute the magnitude, but we don't rename it, which is rather
// sleazy.  TODO: De-sleaze this.

double InterfaceElement::jacobian(SpaceIndex i, 
				  SpaceIndex j, const GaussPoint &g) const
{
  double jac = 0.0;

  // std::cerr << "InterfaceElement::jacobian with gpt." << std::endl;

  // For interface elements, only return the (0,0) element, and set
  // the (1,1) element to unity, so that the determinant will be
  // right.
  if (j==0) {
    for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni) { 
      jac += (ni.node()->position())(i)*ni.masterderiv(j,g);
    }
    // std::cerr << "InterfaceElement::jacobian returning " << jac << std::endl;
    return jac;
  }
  else 
    return 0.0;
}

double InterfaceElement::jacobian(SpaceIndex i, 
				  SpaceIndex j, const MasterCoord &mc)
  const
{
  double jac = 0.0;

  if (j==0) { 
    for(ElementMapNodeIterator ni=mapnode_iterator(); !ni.end(); ++ni) 
      jac += (ni.node()->position())(i)*ni.masterderiv(j,mc);
    return jac;
  }
  else
    return 0.0;
}

double InterfaceElement::det_jacobian(const GaussPoint &g) const {
  double j00 = this->jacobian(0,0,g);
  double j10 = this->jacobian(1,0,g);
  return sqrt(j00*j00+j10*j10);
}

double InterfaceElement::det_jacobian(const MasterCoord &mc) const {
  double j00 = this->jacobian(0,0,mc);
  double j10 = this->jacobian(1,0,mc);
  return sqrt(j00*j00+j10*j10);
}


double Element::det_jacobian(const GaussPoint &g) const {
  return master.mapfunction->det_jacobian(this, g);
}

double Element::det_jacobian(const MasterCoord &mc) const {
  return master.mapfunction->det_jacobian(this, mc);
}

int Element::shapefun_degree() const {
  return master.shapefunction->degree();
}

int Element::dshapefun_degree() const {
  return master.shapefunction->deriv_degree();
}

int Element::mapfun_degree() const {
  return master.mapfunction->degree();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ArithmeticOutputValue Element::outputField(const FEMesh *mesh,
					   const Field &field,
					   const MasterPosition &pos)
  const
{
  ArithmeticOutputValue val = field.newOutputValue();
  for(CleverPtr<ElementFuncNodeIterator>node(funcnode_iterator()); 
      !node->end(); ++*node) {
    double sfvalue = node->shapefunction(pos);
    val += sfvalue*field.output(mesh, *node);
  }
  return val;
}

std::vector<ArithmeticOutputValue> *
Element::outputFields(const FEMesh *mesh, const Field &field,
		      const std::vector<MasterCoord*> *coords) const
{
  std::vector<ArithmeticOutputValue> *results =
    new std::vector<ArithmeticOutputValue>;
  results->reserve(coords->size());
  for(std::vector<MasterCoord*>::size_type i=0; i<coords->size(); i++) {
    ArithmeticOutputValue val = field.newOutputValue();
    for(CleverPtr<ElementFuncNodeIterator>node(funcnode_iterator()); 
	!node->end(); ++*node) {
      double sfvalue = node->shapefunction(*(*coords)[i]);
      // Field::output returns an appropriate type of 0 if the Field
      // isn't defined on the Node.
      val += sfvalue*field.output(mesh, *node);
    }
    results->push_back(val);
  }
  return results;
}

// std::vector<OutputValue> *
// Element::outputFieldsAnyway(const CSubProblem *mesh, const Field &field,
// 			    const std::vector<MasterCoord*> *coords) const
// {
//   // Return zero if the field isn't defined.  Don't throw an exception.
//   if(mesh->is_defined_field(field))
//     return outputFields(mesh, field, coords);
//   // Field isn't defined.
//   std::vector<OutputValue> *results = new std::vector<OutputValue>;
//   results->reserve(coords->size());
//   for(std::vector<MasterCoord*>::size_type i=0; i<coords->size(); i++) {
//     results->push_back(field.newOutputValue());
//   }
//   return results;
// }

// This version takes a vector of MasterCoords, not MasterCoord*s, and
// is used by Edge::outputFields.
std::vector<ArithmeticOutputValue> *
Element::outputFields(const FEMesh *mesh, const Field &field,
		      const std::vector<MasterCoord> &coords) const
{
  std::vector<ArithmeticOutputValue> *results =
    new std::vector<ArithmeticOutputValue>;
  results->reserve(coords.size());
  for(std::vector<MasterCoord>::size_type i=0; i<coords.size(); i++) {
    ArithmeticOutputValue val = field.newOutputValue();
    for(CleverPtr<ElementFuncNodeIterator>node(funcnode_iterator());
	!node->end(); ++*node) {
      double sfvalue = node->shapefunction(coords[i]);
      // Field::output returns an appropriate type of 0 if the Field
      // isn't defined on the Node.
      val += sfvalue*field.output(mesh, *node);
    }
    results->push_back(val);
  }
  return results;
}

// std::vector<OutputValue> *
// Element::outputFieldsAnyway(const CSubProblem *mesh, const Field &field,
// 		      const std::vector<MasterCoord> &coords) const
// {
//   if(mesh->is_defined_field(field))
//     return outputFields(mesh, field, coords);
//   std::vector<OutputValue> *results = new std::vector<OutputValue>;
//   results->reserve(coords.size());
//   for(std::vector<MasterCoord>::size_type i=0; i<coords.size(); i++) {
//     results->push_back(field.newOutputValue());
//   }
//   return results;
// }

std::vector<ArithmeticOutputValue> *
Element::outputFieldDerivs(const FEMesh *mesh, const Field &field,
			   SpaceIndex *deriv_component,
			   const std::vector<MasterCoord*> *coords) const
{
  std::vector<ArithmeticOutputValue> *results =
    new std::vector<ArithmeticOutputValue>;
  results->reserve(coords->size());
  for(std::vector<MasterCoord*>::size_type i=0; i<coords->size(); i++) {
    ArithmeticOutputValue val = field.newOutputValue();
    for(CleverPtr<ElementFuncNodeIterator> node(funcnode_iterator());
	!node->end(); ++*node) {
      double dsfvalue = node->dshapefunction(*deriv_component, *(*coords)[i]);
      val += dsfvalue*field.output(mesh, *node);
    }
    results->push_back(val);
  }
  return results;
}

ArithmeticOutputValue Element::outputFieldDeriv(
				const FEMesh *mesh,
				const Field &field,
				SpaceIndex *deriv_component,
				const MasterPosition &pos) const
{
  ArithmeticOutputValue val = field.newOutputValue();
  for(CleverPtr<ElementFuncNodeIterator> node(funcnode_iterator());
      !node->end(); ++*node) {
    double dsfvalue = node->dshapefunction(*deriv_component, pos);
    val += dsfvalue*field.output(mesh, *node);
    }
  return val;
}

// OutputValue Element::outputFlux(const FEMesh *mesh, const Flux &flux,
// 				const MasterPosition &pos) const
// {
//   return flux.output( mesh, this, pos );
// }

std::vector<ArithmeticOutputValue> *
Element::outputFluxes(const FEMesh *mesh, const Flux &flux,
		      const std::vector<MasterCoord*> *coords) const
{
  std::vector<ArithmeticOutputValue> *results =
    new std::vector<ArithmeticOutputValue>;
  results->reserve(coords->size());
  for(std::vector<MasterCoord*>::size_type i=0; i<coords->size(); i++)
    results->push_back( flux.output( mesh, this, *(*coords)[i] ) );
  return results;
}



// Create a vector mapping the canonical order of the Element's
// degrees of freedom to the DOF's actual indices.  Almost identical
// code to the routine below.
std::vector<int> Element::localDoFmap() const {
  std::vector<int> dofmap(ndof(),-1);
  for(std::vector<Field*>::size_type fi=0; fi< Field::all().size(); fi++) {
    Field &field = *Field::all()[fi];
    // Field components.
    for(IndexP fcomp : field.components(ALL_INDICES)) {
      // Nodes
      for(CleverPtr<ElementFuncNodeIterator> node(funcnode_iterator());
	  !node->end(); ++*node)
	{
	  if(node->hasField(field)) {
	    DegreeOfFreedom *dof = field(*node, fcomp.integer());
	    dofmap[node->localindex(field, fcomp)] = dof->dofindex();
	  }
	}
    }
  }
  return dofmap;
}




// Fill in a vector of the values of the Element's degrees of freedom,
// in canonical order.  The list is assumed to already be the correct
// size. 

void Element::localDoFs(const FEMesh *mesh, DoubleVec &doflist) const
{
  for(std::vector<Field*>::size_type fi=0; fi<Field::all().size(); fi++) {
    Field &field = *Field::all()[fi];
    // loop over field components
    for(IndexP fcomp : field.components(ALL_INDICES)) {
      // loop over nodes
      for(CleverPtr<ElementFuncNodeIterator> node(funcnode_iterator());
	  !node->end(); ++*node)
	{
	  if(node->hasField(field)) {
	    DegreeOfFreedom *dof = field(*node, fcomp.integer());
// 	    std::cerr << "Element::localDoFs: "
// 		      << field << "[" << fcomp.integer() << "] "
// 		      << node.node()->position() << " "
// 		      << node.localindex(field, fcomp) << std::endl;
	    doflist[node->localindex(field, fcomp)] = dof->value(mesh);
	  }
	}
    }
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The main edge function.

BoundaryEdge *Element::newBndyEdge(const FuncNode *n0, const FuncNode *n1)
  const
{
//   Trace("Element::newBndyEdge " + tostring(*n0) + " " + tostring(*n1));
  // find ElementCornerNodeIterators for each FuncNode
  ElementCornerNodeIterator alpha = cornernode_iterator();
  // It may not be sufficient to compare pointers to Nodes, since the
  // Nodes can have different derived types.  Use
  // operator==(Node&,Node&) and operator!=(Node&,Node&) instead.
  while((*alpha.node() != *n0) && !alpha.end()) {
    ++alpha;
  }
  if(alpha.end()) {
    throw ErrUserError("Element::newBndyEdge: Nodes not corners of element");
  }
  bool forward;
  ElementCornerNodeIterator beta = alpha + 1;
  if(*beta.node() == *n1) {
    // second node is in front of first
    forward = true;
  }
  else {			// second node isn't in front
    beta = alpha + (ncorners() - 1);
    if(*beta.node() != *n1) {
      // it's not behind either
      throw ErrUserError("Element::newBndyEdge: Inconsistent node set");
    }
    forward = false;		// it was behind
  }

  // find out which edge of the masterelement contains alpha and beta
  const MasterEdge *medge = masterelement().masteredge(alpha, beta);

  // put the endpoints and all intermediate FuncNodes in the BoundaryEdge
  BoundaryEdge *ed = new BoundaryEdge(this, medge->func_size());
  ed->add_node(alpha.efuncnode_iterator());

  int increment;
  if(forward)
    increment = 1;
  else
    increment = nexteriorfuncnodes() - 1;

  ElementExteriorNodeIterator middle = alpha.exteriornode_iterator()+increment;
  while(*middle.node() != *beta.node()) {
    ed->add_node(middle);
    middle += increment;
  }
  ed->add_node(beta.efuncnode_iterator());

  return ed;
}

BoundaryEdge *Element::getBndyEdge(const FuncNode *n0, const FuncNode *n1) {
  BoundaryEdge *ed = find_b_edge(n0, n1);
//   Trace("Element::getBndyEdge " + tostring(*n0) + " " + tostring(*n1));
  // find_edge will correctly detect nullness of the edgelist.
  if(ed == nullptr) {
    ed = newBndyEdge(n0, n1);
    if(ed != nullptr) {
      add_b_edge(ed);
      return ed;
    }
    else {
      // Probable cause is that the input nodes are not adjacent
      // corners in the derived element type.
      throw ErrUserError("Element::getBndyEdge: Unable to make edge.");
    }
  }
  return ed; // Otherwise return the non-null result from find_edge.
}

BoundaryEdge *Element::find_b_edge(const FuncNode *n0, const FuncNode *n1) {

  for(unsigned int i=0;i<edgeset.size();i++) {
    if( edgeset[i]->edge_match(n0,n1))
      return edgeset[i];
  }

  return 0;  // If you got all the way to the end, then it wasn't there.
}

void Element::add_b_edge(BoundaryEdge *ed_in) {
  // The edge list is not allocated unless needed, and it needs to be
  // 2x the number of geometric edges, because edges are directed.
  // Edges are simply stored in the order in which they were created,
  // because there aren't very many of them, and the search will be
  // fast.
  if(edgeset.empty())
    edgeset.reserve(2*master.nedges());
  edgeset.push_back(ed_in);
}

std::vector<Edge*> *Element::perimeter() const {
  std::vector<Edge*> *brim = new std::vector<Edge*>(master.nedges());
  for(ElementCornerNodeIterator it=cornernode_iterator(); !it.end(); ++it) {
    (*brim)[it.index()] = new Edge(this,
				   it.mastercoord(), (it+1).mastercoord());
  }
  return brim;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

GaussPointIntegrator Element::integrator(int order) const {
  return GaussPointIntegrator(this, order);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

int Element::ndof() const {
  int n = 0;
  for(CleverPtr<ElementFuncNodeIterator> ni(funcnode_iterator());
      !ni->end(); ++*ni) {
    // int dn = ni.funcnode()->ndof();
    // std::cerr << "DOFs: " << dn << std::endl;
    n += ni->funcnode()->ndof();
  }

  return n;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Generic area calculation, done by integrating 1.

double Element::area() const {
  double a = 0.0;
  for(GaussPoint gpt : integrator(0)) {
    a += gpt.weight();
  }
  return a;
}

MasterCoord Element::center() const {
  return master.center();
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

bool Element::exterior(const MasterCoord &a, const MasterCoord &b) const {
  // Are points a and b on the same exterior edge?
  if(!exterior_edges)
    return 0;
  // Let the master do the actual computation, so as to avoid roundoff errors.
  return master.exterior(a, b, *exterior_edges);
}

void Element::set_exterior(const Node &n0, const Node &n1) {
  if(!exterior_edges)
    exterior_edges = new std::vector<ElementCornerNodeIterator>;
  // find which edge these nodes are on.
  for(ElementCornerNodeIterator it=cornernode_iterator(); !it.end(); ++it) {
    const Node *node0 = it.node();
    const Node *node1 = (it+1).node();
    if((node0==&n0 && node1==&n1) || (node1==&n0 && node0==&n1)) {
      exterior_edges->push_back(it);
//       cerr << "Element::set_exterior it=" << it << endl;
//       cerr << "    n0=" << n0 <<     "    n1=" << n1 << endl;
//       cerr << " node0=" << *node0 << " node1=" << *node1 << endl;
      return;
    }
  }
}

void Element::dump_exterior() const {  // debugging
  if(!exterior_edges) return;
  std::cerr << "Element::dump_exterior " << *this << std::endl;
  for(std::vector<ElementCornerNodeIterator>::size_type i=0;
      i<exterior_edges->size(); i++)
    std::cerr << "   " << (*exterior_edges)[i] << std::endl;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

std::ostream &operator<<(std::ostream &os, const Element &el) {
  os << el.master.name();
  for(ElementCornerNodeIterator it=el.cornernode_iterator(); !it.end(); ++it)
    os << " " << it.node()->position();
  return os;
}

Node* Element::getCornerNode(int i) const
{
  ElementCornerNodeIterator nit = cornernode_iterator();
  return (nit+i).node();
}

//////////////////////////////////////////////////////////////


InterfaceElement::InterfaceElement(PyObject *leftskelel,
				   CSkeletonElement *leftcskelel,
				   PyObject *rightskelel,
				   CSkeletonElement *rightcskelel,
				   int segmentordernumber,
				   const MasterElement &me,
				   const std::vector<Node*> *nlleft, 
				   const std::vector<Node*> *nlright,
				   bool left_inorder,
				   bool right_inorder,
				   const Material *mat,
				   const std::vector<std::string>* 
				   pInterfacenames)
  : Element(leftskelel,leftcskelel,me,nlleft,mat),
    nodelist2(*nlright), 
    left_nodes_in_interface_order(left_inorder),
    right_nodes_in_interface_order(right_inorder),
    skeleton_element2(rightskelel),  // Element base class has "element".
    cskeleton_element2(rightcskelel),
    _segmentordernumber(segmentordernumber),
    _interfacenames(*pInterfacenames),
    current_side(LEFT)
{
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_XINCREF(skeleton_element2);
}

InterfaceElement::~InterfaceElement()
{
  PYTHON_THREAD_BEGIN_BLOCK;
  Py_XDECREF(skeleton_element2);
}


const std::string &InterfaceElement::name() const
{
  //An InterfaceElement is associated with at least one interface or
  //boundary.
  // assert(_interfacenames.size()>0)
  return _interfacenames.back();
}

std::vector<std::string>* InterfaceElement::namelist() const
{
  std::vector<std::string> *ptmp = new std::vector<std::string>(_interfacenames.size());
  //(*ptmp).insert(_interfacenames.begin(),_interfacenames.end());
  (*ptmp).assign(_interfacenames.begin(),_interfacenames.end());
  return ptmp;
}

// Called by FEMesh::refreshMaterials.
void InterfaceElement::refreshInterfaceMaterial(PyObject *skeletoncontext)
{
  //Interface branch -- untested
  PYTHON_THREAD_BEGIN_BLOCK;
  // Call SkeletonContext.getMaterialNameFromInterfaceName(name()) via
  // python API calls.  It will return a string.
  PyObject *pymatname = PyObject_CallMethod(skeletoncontext,
					    "getMaterialNameFromInterfaceName",
					    "s", name().c_str());
  if(!pymatname) {
    pythonErrorRelay();
  }
  if(pymatname == Py_None) {
    setMaterial(nullptr);
  }
  else {
    // Get C++ material name from python object
    std::string matname = pyStringAsString(pymatname);
    // Get C++ material from material name
    const Material *mat = getMaterialByName(matname);
    setMaterial(mat);
  }
  Py_XDECREF(pymatname);

  
  
  // // Call skeleton.getInterfaceMaterial(skeleton_element, segmentordernumber)
  // PyObject *pymat;
  // pymat = PyObject_CallMethod(skeletoncontext, "getInterfaceMaterial",
  // 			      "s", name().c_str());
  // if(!pymat) {
  //   pythonErrorRelay();
  // }
  // if(pymat == Py_None) {
  //   setMaterial(0);
  // }
  // else {
  //   // Extract the C++ Material* from the Python object.
  //   const Material* tmp;
  //   //	  SWIG_GetPtrObj(pymat, (void**)(&tmp), "_Material_p");
  //   SWIG_ConvertPtr(pymat, (void**) &tmp, ((SwigPyObject*) pymat)->ty, 0);
  //   setMaterial(tmp);
  //   Py_XDECREF(pymat);
  // }
}

bool InterfaceElement::isSubProblemInterfaceElement(const CSubProblem* pSubProblem) const
{
  //TODO: Allow the edgement with split-nodes to be
  //located at subproblem or mesh boundaries
//   for(std::vector<Node*>::size_type i=0;
//       i<nnodes();i++)
  for(int i=0;i<nnodes();i++)
    {
      if(pSubProblem->containsNode(get_nodelist()[i])==false)
	{
	  return false;
	}
    }
  for(std::vector<Node*>::size_type i=0;
      i<nodelist2.size();i++)
    {
      if(pSubProblem->containsNode(nodelist2[i])==false)
	{
	  return false;
	}
    }
  return true;
}

void InterfaceElement::rename(const std::string& oldname, 
			      const std::string& newname)
{
  //TODO: Try find() and vector::assign(iter_begin,iter_end)
  for(std::vector<std::string>::size_type i=0;i<_interfacenames.size();i++)
    {
      if(_interfacenames[i]==oldname)
	{
	  _interfacenames[i]=newname;
	  return;
	}
    }
}

// Span retrieval functions.  Return the first and last node on the
// indicated side, in interface order.  If the nodes are not split,
// these two functions will have the same return value.

std::vector<const Node*> InterfaceElement::get_left_span() const {
  std::vector<const Node*> span = std::vector<const Node*>(2);
  if(left_nodes_in_interface_order) {
    span[0] = nodelist.front();
    span[1] = nodelist.back();
  }
  else {
    span[0] = nodelist.back();
    span[1] = nodelist.front();
  }
  return span;
}

std::vector<const Node*> InterfaceElement::get_right_span() const {
  std::vector<const Node*> span = std::vector<const Node*>(2);
 if(right_nodes_in_interface_order) {
    span[0] = nodelist2.front();
    span[1] = nodelist2.back();
  }
  else {
    span[0] = nodelist2.back();
    span[1] = nodelist2.front();
  } 
  return span;
}


ElementFuncNodeIterator *InterfaceElement::funcnode_iterator() const 
{
  return new InterfaceElementFuncNodeIterator(*this);
}


std::ostream &operator<<(std::ostream &os, const InterfaceElement &ed)
{
  os << ed.masterelement().name();
  os << " [";
  for(ElementNodeIterator it=ed.node_iterator(); !it.end(); ++it)
    os << " " << it.node()->position();
  os << " ], [";
  for(std::vector<Node*>::size_type i=0;i<ed.get_rightnodelist().size();i++)
    os << " " << ed.get_rightnodelist()[i]->position();
  os << " ], " << ed._segmentordernumber << ", " << ed.name();
  return os;
}


//////////////////////////////////////////////////////////////////////////

std::string CoordElementData::class_("CoordElementData");
//std::string CoordElementData::module_("ooflib.SWIG.engine.element");
