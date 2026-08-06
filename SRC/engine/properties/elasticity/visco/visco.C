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
#include "engine/cstrain.h"
#include "engine/properties/elasticity/visco/visco.h"
#include "engine/flux.h"
#include "engine/field.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/smallsystem.h"

CViscoElasticity::CViscoElasticity(const std::string &nm,
				   PyObject *registration, Cijkl &g)
  : FluxProperty(nm,registration),
    g_ijkl(g)
{
  displacement = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
  displacement_t = dynamic_cast<TwoVectorFieldBase*>(
					     displacement->time_derivative());
  stress_flux = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}

int CViscoElasticity::integration_order(const CSubProblem *subp,
					   const Element *el)
  const
{
  if(displacement->in_plane(subp))
    return el->dshapefun_degree();
  return el->shapefun_degree();
}

void CViscoElasticity::flux_matrix(const FEMesh *mesh,
				   const Element *element,
				   const ElementFuncNodeIterator &nu,
				   const Flux *flux,
				   const MasterPosition &x,
				   double time, void*, 
				   SmallSystem *fluxmtx) const
{
  if(*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  double sf = nu.shapefunction(x);
  double dsf0 = nu.dshapefunction(0, x);
  double dsf1 = nu.dshapefunction(1, x);

  for(IndexP ij : *flux->components(ALL_INDICES)) {
    // loop over displacement components for in-plane strain contributions
    for(IndexP ell : *displacement_t->components(ALL_INDICES)) {
      // loop over k=0,1 is written out explicitly to save a tiny bit of time
      SymTensorIndex ell0(0, ell);
      SymTensorIndex ell1(1, ell);
      fluxmtx->damping_matrix_element(ij, displacement_t, ell, nu)
	+= g_ijkl(ij, ell0)*dsf0 + g_ijkl(ij, ell1)*dsf1;
    }

    // loop over out-of-plane strains
    if(!displacement->in_plane(mesh)) {
      Field *oopfield = displacement->out_of_plane_time_derivative();
      for(IndexP ell : *oopfield->components(ALL_INDICES)) {
	double diag_factor = ell.integer()==2 ? 1.0 : 0.5;
	fluxmtx->damping_matrix_element(ij, oopfield, ell, nu)
	  += g_ijkl(ij, SymTensorIndex(2, ell)) * sf * diag_factor;
      }
    }
  }
}

#ifndef GENERIC_FLUX_VALUE
void CViscoElasticity::flux_value(const FEMesh *mesh, const Element *element,
				  const Flux *flux, const MasterPosition &pt,
				  double time, void*, SmallSystem *fluxdata)
  const
{
  if(*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }
  SymmMatrix3 strainrate = findGeometricStrainRate(mesh, element, pt, false);

  SymmMatrix3 stress = g_ijkl*strainrate;
  for(IndexP ij : *stress.components())
    fluxdata->flux_vector_element(ij) += stress[ij];
}
#endif // GENERIC_FLUX_VALUE


void CViscoElasticity::output(FEMesh *mesh,
			      const Element *element,
			      const PropertyOutput *output,
			      const MasterPosition &pos,
			      OutputVal *data)
{
  // This is copied directly from CIsoElasticityProp::output() in
  // engine/properties/elasticity/iso/iso.C.  If we ever implement
  // anisotropic viscosity, copy the output method from aniso/aniso.C.
  const std::string &outputname = output->name();
  if(outputname == "Material Constants:Mechanical:Viscosity") {
    ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
    std::vector<std::string> *idxstrs =
      output->getListOfStringsParam("components");
    for(unsigned int i=0; i<idxstrs->size(); i++) {
      const std::string &voigtpair = (*idxstrs)[i];
      SymTensorIndex idx0(int(voigtpair[0]-'1'));
      SymTensorIndex idx1(int(voigtpair[1]-'1'));
      (*listdata)[i] = g_ijkl(idx0, idx1);
    }
    delete idxstrs;
  }
}
