// -*- C++ -*-


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov.
 */

// heat conductivity

#include <oofconfig.h>

#include "common/coord.h"
#include "common/doublevec.h"
#include "engine/IO/propertyoutput.h"
#include "engine/celectricfield.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/equation.h"
#include "engine/field.h"
#include "engine/fieldindex.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/nodalequation.h"
#include "engine/ooferror.h"
#include "engine/properties/orientation/orientation.h"
#include "engine/properties/permittivity/permittivity.h"

DielectricPermittivity::DielectricPermittivity(PyObject *registry,
				   const std::string &nm)
  : FluxProperty(nm, registry)
{
  voltage = dynamic_cast<ScalarField*>(Field::getField("Voltage"));
  total_polarization = dynamic_cast<VectorFlux*>
    (Flux::getFlux("Total_Polarization"));
}

int DielectricPermittivity::integration_order(const CSubProblem *mesh,
					      const Element *el) const
{
  if(voltage->in_plane(mesh))
    return el->dshapefun_degree();
  return el->shapefun_degree();
}

void DielectricPermittivity::flux_matrix(const FEMesh *mesh,
					 const Element *el,
					 const ElementFuncNodeIterator &j,
					 const Flux *flux,
					 const MasterPosition &pt,
					 double time,
					 SmallSystem *fluxdata)
  const
{
  // The polarization flux matrix M_{ij} multiplies the vector of
  // nodal voltages to give the vector polarization J at point pt.
  // M_{ij} = epsilon_{ik} grad_k N_j
  // J_i = M_{ij} T_j
  // where N_j is the shapefunction at node j.

  if(*flux != *total_polarization) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  double sf = j.shapefunction(pt);
  double dsf0 = j.dshapefunction(0, pt);
  double dsf1 = j.dshapefunction(1, pt);
#if DIM==3
  double dsf2 = j.dshapefunction(2, pt);
#endif

  SymmMatrix3 permit = permittivityTensor(mesh, el, pt);

  // Loop over flux components.  Loop over all components, even if
  // the flux is in-plane, because the out-of-plane components of
  // the flux matrix are used to construct the constraint equation.
  for(IndexP i : flux->components(ALL_INDICES)) {
    // in-plane voltage gradient contributions
    fluxdata->stiffness_matrix_element(i, voltage, j) -=
      permit(i.integer(), 0) * dsf0 +
      permit(i.integer(), 1) * dsf1;
    // out-of-plane voltage gradient contribution
    if(!voltage->in_plane(mesh)) {
      fluxdata->stiffness_matrix_element(i, voltage->out_of_plane(), j)
	-= permit(i.integer(), 2) * sf;
    }
  }
}


void DielectricPermittivity::output(FEMesh *mesh,
				    const Element *element,
				    const PropertyOutput *output,
				    const MasterPosition &pos,
				    OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Energy") {
    // The parameter is a Python Enum instance.  Extract its name.
    const std::string *etype = output->getEnumParam("etype");
    if(*etype == "Total" || *etype == "Electric") {
      ScalarOutputVal *edata =
	dynamic_cast<ScalarOutputVal*>(data);
      DoubleVec E_field(3, 0.0);
      findElectricField(mesh, element, pos, E_field);
      SymmMatrix3 permit = permittivityTensor(mesh, element, pos);
      DoubleVec D_field = permit*E_field;
      double e = D_field * E_field;
      *edata += 0.5*e;
    }
    delete etype;
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

IsoDielectricPermittivity::IsoDielectricPermittivity(PyObject *reg,
						     const std::string &nm,
						     double epsilon)
  : DielectricPermittivity(reg, nm),
    epsilon_(epsilon)
{
}

void IsoDielectricPermittivity::precompute(FEMesh *mesh) {
  DielectricPermittivity::precompute(mesh);
  permittivitytensor_(0,0) = permittivitytensor_(1,1)
    = permittivitytensor_(2,2) = epsilon_;
}

void IsoDielectricPermittivity::output(FEMesh *mesh,
				       const Element *element,
				       const PropertyOutput *output,
				       const MasterPosition &pos,
				       OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname=="Material Constants:Electric:Dielectric Permittivity epsilon")
    {
      ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
      std::vector<std::string> *idxstrs =
	output->getListOfStringsParam("components");
      for(unsigned int i=0; i<idxstrs->size(); i++) {
	const std::string &idxpair = (*idxstrs)[i];
	if(idxpair[0] == idxpair[1])
	  (*listdata)[i] = epsilon_;
	else
	  (*listdata)[i] = 0;
      }
      delete idxstrs;
    }
  DielectricPermittivity::output(mesh, element, output, pos, data);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

AnisoDielectricPermittivity::AnisoDielectricPermittivity(PyObject *reg,
							 const std::string &nm,
							 SymmMatrix3 *k)
  : DielectricPermittivity(reg,nm),
    epsilon_(*k),
    orientation(0)
{
}

void AnisoDielectricPermittivity::cross_reference(Material *mat) {
  try {
    orientation =
      dynamic_cast<OrientationPropBase*>(mat->fetchProperty("Orientation"));
  }
  catch (ErrNoSuchProperty&) {
    orientation = 0;
    throw;
  }
}

void AnisoDielectricPermittivity::precompute(FEMesh *mesh) {
  DielectricPermittivity::precompute(mesh);
  if(orientation && orientation->constant_in_space())
    permittivitytensor_ = epsilon_.transform(orientation->orientation());
}

const SymmMatrix3
AnisoDielectricPermittivity::permittivityTensor(const FEMesh *mesh,
						const Element *element,
						const MasterPosition &x) const
{
  if(orientation->constant_in_space())
    return permittivitytensor_;
  return epsilon_.transform(orientation->orientation(mesh, element, x));
}

void AnisoDielectricPermittivity::output(FEMesh *mesh,
					 const Element *element,
					 const PropertyOutput *output,
					 const MasterPosition &pos,
					 OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname=="Material Constants:Electric:Dielectric Permittivity epsilon")
    {
      ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
      std::vector<std::string> *idxstrs =
	output->getListOfStringsParam("components");
      const std::string *frame = output->getEnumParam("frame");
      if(*frame == "Lab") {
	precompute(mesh);
	copyOutputVals(permittivityTensor(mesh, element, pos),
		       listdata, *idxstrs);
      }
      else {
	assert(*frame == "Crystal");
	copyOutputVals(epsilon_, listdata, *idxstrs);
      }
      delete idxstrs;
      delete frame;
    }
  DielectricPermittivity::output(mesh, element, output, pos, data);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//
//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

ChargeDensity::ChargeDensity(PyObject *reg,
			       const std::string &name, double q)
  : EqnProperty(name,reg),
    q_(q) {
    total_polarization = dynamic_cast<VectorFlux*>
      (Flux::getFlux("Total_Polarization"));
}

int ChargeDensity::integration_order(const CSubProblem*, const Element*) const {
  return 0;
}

// Adds to the right-hand side of the Coulomb equation, so we want
// force_offset.
void ChargeDensity::force_value(const FEMesh *mesh, const Element *element,
				const  Equation *eqn,
				const MasterPosition &masterpos,
				double time,
				SmallSystem *eqndata) const {

//   if(*flux != *total_polarization) {
//     throw ErrProgrammingError("Unexpected flux.", __FILE__, __LINE__);
//   }

  // In fact, there is only one component, so this is excessive.
//   for(int i=0;i<total_polarization->divergence_dim();i++) {
//     fluxdata->rhs_element(i) -= q_;
//   }
  eqndata->force_vector_element(0) -= q_;
}

void ChargeDensity::output(FEMesh *mesh,
			   const Element *element,
			   const PropertyOutput *output,
			   const MasterPosition &pos,
			   OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Material Constants:Electric:Space Charge") {
    ScalarOutputVal *sdata = dynamic_cast<ScalarOutputVal*>(data);
    *sdata = q_;
  }
}
