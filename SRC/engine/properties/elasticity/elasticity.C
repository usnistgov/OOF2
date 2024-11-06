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
#include "cijkl.h"
#include "common/threadstate.h"
#include "common/coord.h"
#include "common/trace.h"
#include "elasticity.h"
#include "engine/IO/propertyoutput.h"
#include "engine/cstrain.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/indextypes.h"
#include "engine/material.h"
#include "engine/ooferror.h"
#include "engine/smallsystem.h"


Elasticity::Elasticity(const std::string &nm, PyObject *registration)
  : FluxProperty(nm, registration)
{
  displacement = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
  stress_flux = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}

int Elasticity::integration_order(const CSubProblem *subp, const Element *el)
  const
{
  if(displacement->in_plane(subp))
    return 2*el->dshapefun_degree();
  return el->shapefun_degree() + el->dshapefun_degree();
}

// If static_flux_value isn't defined in a derived class, the base
// class version FluxProperty::static_flux_value will produce the same
// result by calling flux_matrix and flux_offset.  It may be less
// efficient though.

void Elasticity::static_flux_value(const FEMesh *mesh, const Element *element,
				   const Flux *flux, const MasterPosition &pt,
				   double time, SmallSystem *fluxdata)
  const
{
  // Unexpected fluxes are bad.
  if (*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  SymmMatrix3 strain;
  geometricStrain(mesh, element, pt, &strain);
  const Cijkl modulus = cijkl( mesh, element, pt );

  for(SymTensorIndex ij : symTensorIJComponents) {
    // TODO OPT: Use modulus(ij,kl) where ij and kl are voigt ints.
    // Unroll the ij loop too.
    int i = ij.row();
    int j = ij.col();
    fluxdata->flux_vector_element( ij ) -=
      (modulus( i,j,0,0 ) * strain( 0,0 ) +
       modulus( i,j,1,1 ) * strain( 1,1 ) +
       modulus( i,j,2,2 ) * strain( 2,2 ) +
       2*modulus( i,j,0,1 ) * strain( 0,1 ) +
       2*modulus( i,j,0,2 ) * strain( 0,2 ) +
       2*modulus( i,j,1,2 ) * strain( 1,2 ));
  }
} // end of 'Elasticity::static_flux_value'

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Elasticity::flux_matrix(const FEMesh *mesh, const Element *element,
			     const ElementFuncNodeIterator &node,
			     const Flux *flux, const MasterPosition &x,
			     double time, SmallSystem *fluxmtx)
  const
{
  // Unexpected fluxes are bad.
  if (*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }
  std::cerr << "-------------" << std::endl;

  double shapeFuncVal = node.shapefunction(x);
  double shapeFuncGrad[] = {node.dshapefunction(0, x),
   			    node.dshapefunction(1, x)};

  const Cijkl modulus = cijkl(mesh, element, x);
  const MasterCoord mpt = x.mastercoord(); // debugging

  for(IndexP ij : *flux->components(ALL_INDICES)) {

    // loop over displacement components for in-plane strain contributions
    for(IndexP ell : *displacement->components(ALL_INDICES)) {

      // loop over k=0,1 is written out explicitly to save a tiny bit of time
      SymTensorIndex ell0(0, ell.integer());
      SymTensorIndex ell1(1, ell.integer());

      for(int k=0; k<2; k++)
	std::cerr << "flux_matrix:"
		  << " el=" << element->get_index()
		  << " mpt=(" << mpt(0) << "," << mpt(1) << ")"
		  << " " << *displacement << " " << *node.node()
		  << " ij=" << *ij.fieldindex()
		  << " k=VectorFieldIndex(" << k << ")"
		  << " mtx el=" << (modulus(*ij,
					     SymTensorIndex(k, ell.integer()))
				     * shapeFuncGrad[k])
		  << std::endl;

      fluxmtx->stiffness_matrix_element(*ij, displacement, ell, node) -=
                                   modulus(*ij, ell0) * shapeFuncGrad[0] +
                                   modulus(*ij, ell1) * shapeFuncGrad[1];
    } // end of loop over ell

    // loop over out-of-plane strains
    if (!displacement->in_plane(mesh)) {
      Field *oop = displacement->out_of_plane();

      for(IndexP kay : *oop->components(ALL_INDICES))
      {
	std::cerr << "flux_matrix:"
		  << " el=" << element->get_index()
		  << " mpt=(" << mpt(0) << "," << mpt(1) << ")"
		  << " " << *oop
		  << " " << *node.node()
		  << " ij=" << *ij.fieldindex()
		  << " k=" << *kay.fieldindex()
		  << " sf=" << shapeFuncVal
		  << " flxumatrx="
		  << -modulus(ij, SymTensorIndex(2, kay.integer()))*shapeFuncVal
		  << std::endl;
	// There are no net factors of 1/2 or 2 here for the
	// off-diagonal terms, dammit.
	fluxmtx->stiffness_matrix_element(ij, oop, kay, node)
	  -= shapeFuncVal * modulus(ij, SymTensorIndex( 2, kay.integer()));
      }
    } // end if
  } // end of loop over ij

} // end of 'Elasticity::flux_matrix'

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Elasticity::geometricStrain(const FEMesh *mesh, const Element *element,
				 const MasterPosition &pos,
				 SymmMatrix3 *strain)
  const
{
  findGeometricStrain(mesh, element, pos, strain, false);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void Elasticity::output(FEMesh *mesh,
			const Element *element,
			const PropertyOutput *output,
			const MasterPosition &pos,
			OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Energy") {
    // The parameter is a Python Enum instance.  Extract its value.
    // The name of the parameter is 'etype', set in outputDefs.py when
    // the ScalarPropertyOutputRegistration for "Energy" was created.
    const std::string *etype = output->getEnumParam("etype");
    if(*etype == "Total" || *etype == "Elastic") {
      ScalarOutputVal *edata = dynamic_cast<ScalarOutputVal*>(data);
      SymmMatrix3 strain;
      const Cijkl modulus = cijkl(mesh, element, pos);
      geometricStrain(mesh, element, pos, &strain);
      SymmMatrix stress(modulus*strain);
      double e = 0;
      for(int i=0; i<3; i++) {
	e += stress(i,i)*strain(i,i);
	int j = (i+1)%3;
	e += 2*stress(i,j)*strain(i,j);
      }
      *edata += 0.5*e;
    }
    delete etype;
  }
} // end of 'Elasticity::output'

