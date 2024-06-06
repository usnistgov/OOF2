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
#include "engine/IO/propertyoutput.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/equation.h"
#include "engine/femesh.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/ooferror.h"
#include "engine/properties/elasticity/cijkl.h"
#include "engine/properties/elasticity/elasticity.h"
#include "engine/cstrain.h"
#include "engine/properties/orientation/orientation.h"
#include "engine/smallsystem.h"
#include "thermalexpansion.h"


ThermalExpansion::ThermalExpansion(const std::string &nm, PyObject *reg,
				   double t0)
  : FluxProperty(nm, reg),
    T0(t0)
{
  temperature=dynamic_cast<ScalarField*>(Field::getField("Temperature"));
  stress_flux=dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}


int ThermalExpansion::integration_order(const CSubProblem*,
					const Element *el)
  const
{
  // For the flux_matrix contribution, the integrand has a factor of
  // the shape function derivative for the divergence, AND either a
  // factor of the shape function for the temperature field or a
  // factor of the derivative for the strain.  Use the larger one.
  return el->shapefun_degree() + el->dshapefun_degree();
}


void ThermalExpansion::flux_matrix(const FEMesh *mesh,
				   const Element *element,
				   const ElementFuncNodeIterator &nu,
				   const Flux *flux,
				   const MasterPosition &x,
				   double time,
				   SmallSystem *fluxdata) const
{
  // The stress-free strain is $\epsilon_{kl}^0(T) = \alpha T$
  // where alpha is a symmetric tensor.
  //
  // Our goal is to subtract C_{ijkl}*u_{kl}^0(T) from the stress
  // tensor.
  if(*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux." __FILE__, __LINE__);
  }

  // Assume linear elasticity, for now.  The "elasticity" variable was
  // set by cross_reference().
  const Cijkl modulus = elasticity->cijkl(mesh, element, x);

  double sfval = nu.shapefunction(x);
  // Loop over all tensor components.
  SymmMatrix3 expten = expansiontensor(mesh, element, x);
  for(IndexP ij : *flux->components(ALL_INDICES)) {
    double &mtx_el = fluxdata->stiffness_matrix_element(ij, temperature, nu);
    // Loop over strain tensor components.
    for(SymTensorIndex kl : symTensorIJComponents) {
      double ca = modulus(ij, kl)*expten(kl.row(), kl.col())*sfval;
      if(kl.diagonal()) {
	mtx_el += ca;
      }
      else {
	mtx_el += 2.0*ca;
      }
    }
  }
}

void ThermalExpansion::flux_offset(const FEMesh *mesh,
				   const Element *element,
				   const Flux *flux,
				   const MasterPosition &x,
				   double time,
				   SmallSystem *fluxdata) const {

  if(*flux!=*stress_flux) {
    throw ErrProgrammingError("Unexpected flux.", __FILE__, __LINE__);
  }
  const Cijkl modulus = elasticity->cijkl(mesh, element, x);
  SymmMatrix3 expten = expansiontensor(mesh, element, x);
  for(IndexP ij : *flux->components(ALL_INDICES)) {
    double &offset_el = fluxdata->offset_vector_element(ij); // reference!
    for(SymTensorIndex kl : symTensorIJComponents) {
      if(kl.diagonal()) {
	offset_el -= modulus(ij,kl)*expten[kl]*T0;
      }
      else {
	offset_el -= 2.0*modulus(ij,kl)*expten[kl]*T0;
      }
    }
  }
}

void ThermalExpansion::output(FEMesh *mesh,
			      const Element *element,
			      const PropertyOutput *output,
			      const MasterPosition &pos,
			      OutputVal *data)
{
  const std::string &outputname = output->name();
  
  if(outputname == "Strain") {
    // The parameter is a Python StrainType instance.  Extract its name.
    const std::string *stype = output->getRegisteredParamName("type");
    SymmMatrix3 *sdata = dynamic_cast<SymmMatrix3*>(data);
    // Compute alpha*T with T interpolated to position pos
    double t = temperature->value(mesh, element, pos);
    if(*stype == "Thermal")
      *sdata += expansiontensor(mesh, element, pos)*(t-T0);
    else if(*stype == "Elastic")
      *sdata -= expansiontensor(mesh, element, pos)*(t-T0);
    delete stype;
  } // strain output ends here

  if(outputname == "Energy") {
    // See comment in StressFreeStrain::output.
    const std::string *etype = output->getEnumParam("etype");
    if(*etype == "Total" || *etype == "Elastic") {
      ScalarOutputVal *edata = dynamic_cast<ScalarOutputVal*>(data);
      SymmMatrix3 thermalstrain;
      // 'modulus' is lab reference system stiffness
      const Cijkl modulus = elasticity->cijkl(mesh, element, pos);
      double t = temperature->value(mesh, element, pos);
      thermalstrain = expansiontensor(mesh, element, pos)*(t-T0);
      SymmMatrix3 thermalstress(modulus*thermalstrain);
      SymmMatrix3 strain;
      elasticity->geometricStrain(mesh, element, pos, &strain);
      double e = 0;
      for(SpaceIndex i=0; i<3; i++) {
	e += thermalstress(i,i)*(-strain(i,i) + 0.5*thermalstrain(i,i));
	SpaceIndex j = (i+1)%3;
	e += 2*thermalstress(i,j)*(-strain(i,j) + 0.5*thermalstrain(i,j));
      }
      *edata += e;
    }
    delete etype;
  } // energy output ends here

  if(outputname == "Material Constants:Couplings:Thermal Expansion T0") {
    ScalarOutputVal *sdata = dynamic_cast<ScalarOutputVal*>(data);
    *sdata = T0;
  }
}


bool ThermalExpansion::is_symmetric_K(const CSubProblem* mesh) const {
  Equation *forcebalance = Equation::getEquation("Force_Balance");
  // Thermal expansion makes the force-balance stiffness matrix
  // asymmetric if temperature is an active variable.
  return !(forcebalance->is_active(mesh) &&
	   temperature->is_defined(mesh) &&
	   temperature->is_active(mesh));
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

IsotropicThermalExpansion::IsotropicThermalExpansion(const std::string &name,
						     PyObject *registration,
						     double alpha,
						     double t0)
  : ThermalExpansion(name, registration, t0),
    alpha_(alpha)
{

}

const SymmMatrix3
IsotropicThermalExpansion::expansiontensor(const FEMesh*, const Element*,
					   const MasterPosition&) const
{
  return expansiontensor_;
}

void IsotropicThermalExpansion::cross_reference(Material *mat) {
  // find out which property is the elasticity
  try {
    elasticity = dynamic_cast<Elasticity*>(mat->fetchProperty("Elasticity"));
  }
  catch (ErrNoSuchProperty&) {
    elasticity = 0;
    throw;
  }
}

void IsotropicThermalExpansion::precompute(FEMesh *mesh) {
  ThermalExpansion::precompute(mesh);
  expansiontensor_(0,0) = expansiontensor_(1,1) = expansiontensor_(2,2)
    = alpha_;
}

void IsotropicThermalExpansion::output(FEMesh *mesh,
				       const Element *element,
				       const PropertyOutput *output,
				       const MasterPosition &pos,
				       OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Material Constants:Couplings:Thermal Expansion alpha") {
    ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
    std::vector<std::string> *idxstrs =
      output->getListOfStringsParam("components");
    for(unsigned int i=0; i<idxstrs->size(); i++) {
      const std::string idxpair = (*idxstrs)[i];
      if(idxpair[0] == idxpair[1])
	(*listdata)[i] = alpha_;
      else
	(*listdata)[i] = 0;
    }
    delete idxstrs;
  }
  ThermalExpansion::output(mesh, element, output, pos, data);
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

AnisotropicThermalExpansion::AnisotropicThermalExpansion(const std::string &nm,
							 PyObject *registration,
							 SymmMatrix3 *alpha,
							 double t0)
  : ThermalExpansion(nm, registration, t0),
    alpha_(*alpha),
    orientation(0)
{}

const SymmMatrix3
AnisotropicThermalExpansion::expansiontensor(const FEMesh *mesh,
					     const Element *elem,
					     const MasterPosition &pos) const
{
  if(orientation->constant_in_space())
    return expansiontensor_;
  return alpha_.transform(orientation->orientation(mesh, elem, pos));
}

void AnisotropicThermalExpansion::cross_reference(Material *mat) {
  // find out which property is the elasticity
  try {
    elasticity = dynamic_cast<Elasticity*>(mat->fetchProperty("Elasticity"));
    orientation = dynamic_cast<OrientationPropBase*>
      (mat->fetchProperty("Orientation"));
  }
  catch (ErrNoSuchProperty&) {
    elasticity = 0;
    orientation = 0;
    throw;
  }
}

void AnisotropicThermalExpansion::precompute(FEMesh*) {
  if(orientation && orientation->constant_in_space())
    expansiontensor_ = alpha_.transform(orientation->orientation());
}

void AnisotropicThermalExpansion::output(FEMesh *mesh,
				       const Element *element,
				       const PropertyOutput *output,
				       const MasterPosition &pos,
				       OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Material Constants:Couplings:Thermal Expansion alpha") {
    ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
    std::vector<std::string> *idxstrs =
      output->getListOfStringsParam("components");
    const std::string *frame = output->getEnumParam("frame");
    if(*frame == "Lab") {
      precompute(mesh);
      copyOutputVals(expansiontensor(mesh, element, pos), listdata, *idxstrs);
    }
    else {
      assert(*frame == "Crystal");
      copyOutputVals(alpha_, listdata, *idxstrs);
    }
    delete idxstrs;
    delete frame;
  }
  ThermalExpansion::output(mesh, element, output, pos, data);
}
