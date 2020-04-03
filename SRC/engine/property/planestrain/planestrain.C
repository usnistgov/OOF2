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

#include "engine/IO/propertyoutput.h"
#include "engine/cstrain.h"
#include "engine/element.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/ooferror.h"
#include "engine/property/elasticity/cijkl.h"
#include "engine/property/elasticity/elasticity.h"
#include "engine/property/orientation/orientation.h"
#include "engine/property/planestrain/planestrain.h"
#include "engine/smallsystem.h"

PlaneStrain::PlaneStrain(PyObject *reg,
			 const std::string &nm,
			 double ezz)
  : FluxProperty(nm, reg), ezz_(ezz)
{
  stress_flux = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}

int PlaneStrain::integration_order(const CSubProblem*, const Element*el) const {
  return el->shapefun_degree();
}

void PlaneStrain::cross_reference(Material *mat) {
  try {
    elasticity = dynamic_cast<Elasticity*>(mat->fetchProperty("Elasticity"));
  }
  catch (ErrNoSuchProperty&) {
    elasticity = 0;
    throw;
  }
}


void PlaneStrain::flux_offset(const FEMesh *mesh, const Element *element,
			      const Flux *flux,
			      const MasterPosition &x,
			      double time,
			      SmallSystem *fluxdata)
  const
{
  if(*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux.", __FILE__, __LINE__);
  }
  const Cijkl modulus = elasticity->cijkl(mesh, element, x);
  // Modulus is the rotated cijkl.
  for(SymTensorIterator ij; !ij.end(); ++ij) {
    double &offset_el = fluxdata->offset_vector_element(ij);
    for(SymTensorIterator kl; !kl.end(); ++kl) {
      if(kl.integer()==2) { // Index 2 is voigt-order for the zz component.
	offset_el -= modulus(ij, kl)*ezz_; // Sign gives physical results.
      }
    }
  }
}

void PlaneStrain::output(FEMesh *mesh,
 			 const Element *element,
 			 const PropertyOutput *output,
 			 const MasterPosition &pos,
 			 OutputVal *data)
{
  // Mostly copied from ThermalExpansion::output
  const std::string &outputname = output->name();
  if(outputname == "Strain") {
     const std::string *stype = output->getRegisteredParamName("type");
     SymmMatrix3 *sdata = dynamic_cast<SymmMatrix3*>(data);
     if(*stype == "Elastic")
       (*sdata)(2,2) += ezz_;
     delete stype;
  }
//   if(outputname == "Energy") {
//     // Energy looks strange, because we're doing two of the three
//     // terms in a product of differences.  The full answer is
//     // (1/2)Cijkl(e_ij-e0_ij)(e_kl-e0_kl), with e_ij the strain, and
//     // e0_ij the stress-free strain.  But the elasticity property
//     // independently contributes (1/2)Cijkl.e_ij.e_kl.  The remaining
//     // terms are - Cijkl.e_ij.e0_kl + Cijkl.e0_ij.e0_kl.  In the code
//     // below, "stress" refers to the product Cijkl.e0_ij.
//     const std::string *etype = output->getEnumParam("etype");
//     if(*etype == "Total" || *etype == "Elastic") {
//       ScalarOutputVal *edata = dynamic_cast<ScalarOutputVal*>(data);
//       const Cijkl modulus = elasticity->cijkl(mesh, element, pos);
//       SymmMatrix3 strain;
//       SymmMatrix3 sfs = stressfreestrain(mesh, element, pos);
//       elasticity->geometricStrain(mesh, element, pos, &strain);
//       SymmMatrix3 stress(modulus*sfs);
//       double e = 0;
//       for(int i=0; i<3; i++) {
// 	e += stress(i,i)*(-strain(i,i)+0.5*sfs(i,i));
// 	int j=(i+1)%3;
// 	e += 2*stress(i,j)*(-strain(i,j)+0.5*sfs(i,j));
//       }
//       *edata += e;
//     }
//     delete etype;
//   }
}

