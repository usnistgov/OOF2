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

#include "common/cdebug.h"
#include "common/doublevec.h"
#include "common/smallmatrix.h"
#include "engine/cstrain.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/mastercoord.h"
#include "engine/symmmatrix.h"

DoubleVec findDisplacement(const FEMesh *mesh, const Element *element,
			   const MasterPosition &pt)
{
  static const TwoVectorField *displacement =
    dynamic_cast<const TwoVectorField*>(Field::getField("Displacement"));
  return displacement->values(mesh, element, pt);
}

SmallMatrix findDisplacementGradient(const FEMesh *mesh, const Element *element,
				     const MasterPosition &pt)
{
  // compute the matrix dU(i,j) = d/dx_j (u_i)

  // TODO: This is slightly inefficient, because the repeated calls to
  // Field::value() and Field::gradient() are recomputing identical
  // shape functions.  There could be versions of those functions that
  // operate on non-scalar data.  OTOH, the shape function values are
  // cached and evaluating them should be quick.
  
  static const TwoVectorField *displacement =
    dynamic_cast<const TwoVectorField*>(Field::getField("Displacement"));
  static const ThreeVectorField *displacement_z =
    dynamic_cast<const ThreeVectorField*>(displacement->out_of_plane());
  SmallMatrix result(3, 3);
  try {
    for(int j=0; j<2; j++) { // gradient component
      DoubleVec du = displacement->gradients(mesh, element, pt, j);
      for(int i=0; i<2; i++)	// field component
	result(i, j) = du[i];
    }
    if(!displacement->in_plane(mesh)) {
      DoubleVec uz = displacement_z->values(mesh, element, pt);
      for(int i=0; i<3; i++)
	result(i, 2) = uz[i];
    }
  }
  catch (ErrNoSuchField &exc) {
    // The gradient is 0 if the field isn't defined.
  }
  return result;
}

SmallMatrix findDisplacementGradientRate(const FEMesh *mesh,
					 const Element *element,
					 const MasterPosition &pt)
{
  // compute the matrix dU(i,j) = d/dx_j d(u_i)/dt
  static const TwoVectorField *displacement =
    dynamic_cast<const TwoVectorField*>(Field::getField("Displacement"));
  static const TwoVectorFieldBase *displacement_t =
    dynamic_cast<const TwoVectorFieldBase*>(displacement->time_derivative());
  static const ThreeVectorField *displacement_zt =
    dynamic_cast<const ThreeVectorField*>(
			     displacement->out_of_plane_time_derivative());

  if(displacement_t == nullptr)
    throw ErrProgrammingError("displacement_t is not defined",
			      __FILE__, __LINE__);

  SmallMatrix result(3, 3);
  try {
    for(int j=0; j<2; j++) { // gradient component
      DoubleVec du = displacement_t->gradients(mesh, element, pt, j);
      for(int i=0; i<2; i++)	// field component
	result(i, j) = du[i];
    }
    if(!displacement->in_plane(mesh)) {
      if(displacement_zt == nullptr)
	throw ErrProgrammingError("displacement_zt is not defined",
				  __FILE__, __LINE__);
      DoubleVec uz = displacement_zt->values(mesh, element, pt);
      for(int i=0; i<3; i++)
	result(i, 2) = uz[i];
    }
  }
  catch (ErrNoSuchField &exc) {
    // The gradient is 0 if the field isn't defined.    
  }
  
  return result;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

// The following function adds the local geometrical strain at a given
// master position in the given element to the given SymmMatrix3.

SymmMatrix3 findGeometricStrain(const FEMesh *mesh, const Element *element,
				const MasterPosition &pos, bool nonlinear)
{
  // dU(i,j) = du_i/dx_j 
  SmallMatrix dU(findDisplacementGradient(mesh, element, pos));
  SymmMatrix3 strain;

  // TODO OPT: Earlier versions of this routine had unrolled loops.
  // They could be unrolled again if necessary.
  for(SymTensorIndex ij : symTensorIJComponents) {
    int i = ij.row();
    int j = ij.col();
    strain[ij] = 0.5*(dU(i,j) + dU(j,i));
  }

  if(nonlinear) {
    for(SymTensorIndex ij : symTensorIJComponents) {
      int i = ij.row();
      int j = ij.col();
      strain[ij] += 0.5*(dU(0,i)*dU(0,j) + dU(1,i)*dU(1,j) + dU(2,i)*dU(2,j));
    }
  }
  return strain;
}


SymmMatrix3 findGeometricStrainRate(const FEMesh *mesh, const Element *element,
				    const MasterPosition &pos, 
				    bool nonlinear)
{
  // dU(i,j) = d(du_i/dx_j)/dt
  SymmMatrix3 straindot;
  SmallMatrix dU(findDisplacementGradientRate(mesh, element, pos));
  for(SymTensorIndex ij : symTensorIJComponents) {
    int i = ij.row();
    int j = ij.col();
    straindot[ij] = 0.5 * (dU(i,j) + dU(j,i));
  }
  if(nonlinear) {
    for(SymTensorIndex ij : symTensorIJComponents) {
      int i = ij.row();
      int j = ij.col();
      straindot[ij] = 0.5*(dU(0,i)*dU(0,j) + dU(1,i)*dU(1,j) + dU(2,i)*dU(2,j));
    }
  }
  return straindot;
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
    *strain = findGeometricStrain(mesh, element, pos, false);
  }
  else if(*straintype == "Nonlinear Geometric") {
    *strain = findGeometricStrain(mesh, element, pos, true);
  }
  delete straintype;
  return strain;
};

// Initialize a PropertyOutput with the geometric strain rate.

OutputVal *POInitGeometricStrainRate::operator()(
		       const PropertyOutput *po, const FEMesh *mesh,
		       const Element *element, const MasterCoord &pos)
  const
{
  SymmMatrix3 *strain = new SymmMatrix3();
  // Get the Python parameter that tells which Strain is being
  // computed. It's a RegisteredParameter.
  const std::string *straintype = po->getRegisteredParamName("type");
  if(*straintype == "Geometric" || *straintype == "Elastic") {
    *strain = findGeometricStrainRate(mesh, element, pos, false);
  }
  else if(*straintype == "Nonlinear Geometric") {
    *strain = findGeometricStrainRate(mesh, element, pos, true);
  }
  delete straintype;
  return strain;
};
