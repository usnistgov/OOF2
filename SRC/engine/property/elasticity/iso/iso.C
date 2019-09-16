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
#include "engine/property/elasticity/iso/iso.h"

CIsoElasticityProp::CIsoElasticityProp(PyObject *registration,
				       PyObject *self,
				       const std::string &nm, 
				       const Cijkl &c)
  : PythonNative<Property>(self),
    Elasticity(nm,registration),
    c_ijkl(c)
{
}

void CIsoElasticityProp::output(FEMesh *mesh,
			      const Element *element,
			      const PropertyOutput *output,
			      const MasterPosition &pos,
			      OutputVal *data)
{
  const std::string &outputname = output->name();
  if(outputname == "Elastic Modulus") {
    const Cijkl modulus = cijkl(mesh, element, pos);
    ListOutputVal *listdata = dynamic_cast<ListOutputVal*>(data);
    // The PropertyOutput's "indices" parameter is a list of pairs of voigt
    // indices in string form ("11", "62", etc).

    std::vector<const std::string> idxstrs =
      output->getListOfStringsParam("indices");
    assert(idxstrs.size() <= listdata->size());
    // Extract the desired component of cijkl and store it in the PropertyOutput
    for(unsigned int i=0; i<idxstrs.size(); i++) {
      std::string voigtpair = idxstrs[i];
      SymTensorIndex idx0(int(voigtpair[0]-'0'));
      SymTensorIndex idx1(int(voigtpair[1]-'0'));
      listdata[i] = c_ijkl(idx0, idx1);
    }
  }
  Elasticity::output(mesh, element, output, pos, data);
}
