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

#include "common/doublevec.h"
#include "common/smallmatrix.h"
#include "engine/cstrain.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/mastercoord.h"
#include "engine/symmmatrix.h"


// The following function adds the local geometrical strain at a given
// master position in the given element to the given SymmMatrix3.

void findGeometricStrain(const FEMesh *mesh, const Element *element,
			 const MasterPosition &pos, SymmMatrix3 *strain,
			 bool nonlinear)
{
  SmallMatrix dU(3); // dU(i,j) = du_i/dx_j 
  computeDisplacementGradient(mesh, element, pos, dU);

  // TODO OPT: Earlier versions of this routine had unrolled loops.
  // They could be unrolled again if necessary.

  for(SymTensorIndex ij : symTensorIJComponents) {
    int i = ij.row();
    int j = ij.col();
    (*strain)[ij] += 0.5*(dU(i,j) + dU(j,i));
  }

  if(nonlinear) {
    for(SymTensorIndex ij : symTensorIJComponents) {
      int i = ij.row();
      int j = ij.col();
      (*strain)[ij] += 
	0.5*(dU(0,i)*dU(0,j) + dU(1,i)*dU(1,j) + dU(2,i)*dU(2,j));
    }
  }
} // end of 'findGeometricStrain'


void findGeometricStrainRate(const FEMesh *mesh, const Element *element,
			     const MasterPosition &pos, SymmMatrix3 *straindot,
			     bool nonlinear)
{
  SmallMatrix dU(3); // dU(i,j) = d(du_i/dx_j)/dt
  computeDisplacementGradientRate(mesh, element, pos, dU);
  for(SymTensorIndex ij : symTensorIJComponents) {
    int i = ij.row();
    int j = ij.col();
    (*straindot)[ij] += 0.5 * (dU(i,j) + dU(j,i));
  }
  if(nonlinear) {
    for(SymTensorIndex ij : symTensorIJComponents) {
      int i = ij.row();
      int j = ij.col();
      (*straindot)[ij] +=
	0.5*(dU(0,i)*dU(0,j) + dU(1,i)*dU(1,j) + dU(2,i)*dU(2,j));
    }
  }
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// TODO: Create a non-symmetric 3x3 tensor OutputValue class and
// return it from this function, instead of passing in a SmallMatrix.
// Or just return a SmallMatrix.

// TODO: Using the Output machinery for this feels wrong.  The
// versions of Field::value() that interpolate within a Element would
// be more natural, but perhaps slower.  The Output machinery does all
// the interpolation for all field components at once, whereas
// Field::value would have to be called for each component
// individually.

static void computeFieldGradient(const FEMesh *mesh, const Element *element,
				 const MasterPosition &pt, const Field *field,
				 Field *oop, SmallMatrix &grad)
{

  assert(grad.rows() == 3 && grad.cols() == 3);
  
  for(SpaceIndex j=0; j<DIM; ++j) { // loop over gradient components
    ArithmeticOutputValue oddisp =
      element->outputFieldDeriv(mesh, *field, &j, pt);
    // loop over field components
    for(IndexP i : *field->components(ALL_INDICES)) 
      grad(i.integer(), j) += oddisp[i];
  }

  if(oop) {
    ArithmeticOutputValue oddispz = element->outputField(mesh, *oop, pt);
    for(IndexP i : *oop->components(ALL_INDICES))
      grad(i.integer(), 2) += oddispz[i]; 
  }
}

void computeDisplacementGradient(const FEMesh *mesh, const Element *element,
				 const MasterPosition &pt, SmallMatrix &grad)
{
  // compute the matrix dU(i,j) = d/dx_j (u_i)

  static CompoundField *displacement =
    dynamic_cast<CompoundField*>(Field::getField("Displacement"));

  computeFieldGradient(
       mesh, element, pt, displacement,
       (displacement->in_plane(mesh) ? nullptr : displacement->out_of_plane()),
       grad);
}

void computeDisplacementGradientRate(const FEMesh *mesh,
				     const Element *element,
				     const MasterPosition &pt,
				     SmallMatrix &grad)
{
  static CompoundField *displacement =
    dynamic_cast<CompoundField*>(Field::getField("Displacement"));
  computeFieldGradient(
       mesh, element, pt, displacement->time_derivative(),
       (displacement->in_plane(mesh) ? nullptr :
	displacement->out_of_plane_time_derivative()),
       grad);
}

void computeDisplacement(const FEMesh *mesh, const Element *element,
			 const MasterPosition &pt,
			 DoubleVec &disp)
{
  static CompoundField *displacement =
    dynamic_cast<CompoundField*>(Field::getField("Displacement"));
  assert(disp.size() == 3);
  ArithmeticOutputValue odisp = element->outputField(mesh, *displacement, pt);
  for(IndexP i : *displacement->components(ALL_INDICES))
    disp[i.integer()] += odisp[i];
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// Initialize a PropertyOutput with the geometric strain.

OutputVal *POInitGeometricStrain::operator()(
		       const PropertyOutput *po, const FEMesh *mesh,
		       const Element *element, const MasterCoord &pos)
  const
{
  SymmMatrix3 *strain = new SymmMatrix3();
  // Get the Python parameter that tells which Strain is being
  // computed. It's a RegisteredParameter.
  const std::string *straintype = po->getRegisteredParamName("type");
  if(*straintype == "Geometric" || *straintype == "Elastic") {
    findGeometricStrain(mesh, element, pos, strain, false);
  }
  else if(*straintype == "Nonlinear Geometric") {
    findGeometricStrain(mesh, element, pos, strain, true);
  }
  delete straintype;
  return strain;
};
