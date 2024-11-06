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
#include "alt.h"
#include "common/coord.h"
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

CAltElasticityProp::CAltElasticityProp(const std::string &nm,
				       PyObject *registration,
				       const Cijkl &c)
  : FluxProperty(nm, registration),
    c_ijkl(c)
{
  displacement = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
  stress_flux = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}

int CAltElasticityProp::integration_order(const CSubProblem *subp,
					  const Element *el)
  const
{
  if(displacement->in_plane(subp))
    return 2*el->dshapefun_degree();
  return el->shapefun_degree() + el->dshapefun_degree();
}

void CAltElasticityProp::static_flux_value(const FEMesh *mesh,
					   const Element *element,
					   const Flux *flux,
					   const MasterPosition &pt,
					   double time, SmallSystem *fluxdata)
  const
{
  // Unexpected fluxes are bad.
  if (*flux != *stress_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  SymmMatrix3 strain;
  geometricStrain(mesh, element, pt, &strain);
  const Cijkl modulus = cijkl(mesh, element, pt);

  SymmMatrix3 stress = modulus*strain;

  for(SymTensorIndex ij : symTensorIJComponents) {
    int i = ij.row();
    int j = ij.col();
    fluxdata->flux_vector_element(ij) += stress[ij];
      // (modulus( i,j,0,0 ) * strain( 0,0 ) +
      //  modulus( i,j,1,1 ) * strain( 1,1 ) +
      //  modulus( i,j,2,2 ) * strain( 2,2 ) +
      //  2*modulus( i,j,0,1 ) * strain( 0,1 ) +
      //  2*modulus( i,j,0,2 ) * strain( 0,2 ) +
      //  2*modulus( i,j,1,2 ) * strain( 1,2 ));
  }
} // CAltElasticityProp::static_flux_value

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void CAltElasticityProp::geometricStrain(const FEMesh *mesh,
					 const Element *element,
					 const MasterPosition &pos,
					 SymmMatrix3 *strain)
  const
{
  findGeometricStrain(mesh, element, pos, strain, false);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

void CAltElasticityProp::output(FEMesh *mesh,
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
  if(outputname == "Material Constants:Mechanical:Elastic Modulus C") {
    const Cijkl modulus = cijkl(mesh, element, pos);
    ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
    // The PropertyOutput's "components" parameter is a list of pairs
    // of Voigt indices in string form ("11", "62", etc).
    std::vector<std::string> *idxstrs =
      output->getListOfStringsParam("components");
    for(unsigned int i=0; i<idxstrs->size(); i++) { // loop over index pairs
      const std::string &voigtpair = (*idxstrs)[i];
      // Convert from string to int and 1-based indices to 0-based indices
      SymTensorIndex idx0(int(voigtpair[0]-'1'));
      SymTensorIndex idx1(int(voigtpair[1]-'1'));
      // Store the Cijkl component in the PropertyOutput.
      (*listdata)[i] = c_ijkl(idx0, idx1);
    }
    delete idxstrs;
  }

} // CAltElasticityProp::output

