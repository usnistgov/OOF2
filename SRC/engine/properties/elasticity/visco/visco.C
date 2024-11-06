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
  stress_flux = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}

int CViscoElasticity::integration_order(const CSubProblem *subp,
					   const Element *el)
  const
{
  if(displacement->in_plane(subp))
    return 2*el->dshapefun_degree();
  return el->shapefun_degree() + el->dshapefun_degree();
}

#ifdef DEFINE_FLUX_MATRIX
void CViscoElasticity::flux_matrix(const FEMesh *mesh,
				   const Element *element,
				   const ElementFuncNodeIterator &nu,
				   const Flux *flux,
				   const MasterPosition &x,
				   double time,
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
    for(IndexP ell : *displacement->components(ALL_INDICES)) {
      // loop over k=0,1 is written out explicitly to save a tiny bit of time
      SymTensorIndex ell0(0, ell.integer());
      SymTensorIndex ell1(1, ell.integer());
      fluxmtx->damping_matrix_element(ij, displacement, ell, nu)
	-= g_ijkl(ij, ell0)*dsf0 + g_ijkl(ij, ell1)*dsf1;
    }

    // loop over out-of-plane strains
    if(!displacement->in_plane(mesh)) {
      Field *oopfield = displacement->out_of_plane();
      for(IndexP ell : *oopfield->components(ALL_INDICES)) {
	double diag_factor = ( ell.integer()==2 ? 1.0 : 0.5);
	fluxmtx->damping_matrix_element(ij, oopfield, ell, nu)
	  -= g_ijkl(ij, SymTensorIndex(2, ell.integer())) * sf * diag_factor;
      }
    }
  }
}
#endif // DEFINE_FLUX_MATRIX




// TODO TIMEDERIV: Does flux_value work now?  No.  It doesn't crash,
// but it's also not called...

// WHAT IS GOING ON?
//
// The default FluxProperty::flux_matrix() numerically differentiates
// static_flux_value(), not flux_value().  That's why defining
// flux_value here isn't doing anything.  flux_value() is called only
// by Material::find_fluxdata() when evaluating a flux output.
//
// Should a property like viscoelasticity, which makes a flux
// contribution with no static part, define flux_value() but not
// static_flux_value()???
//
// What does DivergenceEquation::make_linear_system() do with stress
// components computed here?  They should be used by
// FluxProperty::flux_matrix(), maybe after numerical differentiation.

#ifdef DEFINE_STATIC_FLUX_VALUE
void CViscoElasticity::static_flux_value(const FEMesh *mesh, const Element *element,
				  const Flux *flux, const MasterPosition &pt,
				  double time, SmallSystem *fluxdata)
  const
{
  if(*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  SymmMatrix3 strainrate;
  findGeometricStrainRate(mesh, element, pt, &strainrate, false);

  SymmMatrix3 stress = g_ijkl*strainrate;
  // std::cerr << "CViscoElasticity::static_flux_value: strainrate="
  // 	   << strainrate << " stress=" << stress << std::endl;
  
  for(IndexP ij : *stress.components())
    fluxdata->flux_vector_element(ij) += stress[ij];
}
#endif // DEFINE_STATIC_FLUX_VALUE

void CViscoElasticity::flux_offset(const FEMesh *mesh,
				   const Element *element,
				   const Flux *flux,
				   const MasterPosition &pt,
				   double time, SmallSystem *fluxdata)
  const
{}

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
