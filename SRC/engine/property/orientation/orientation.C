// -*- C++ -*-
// $RCSfile: orientation.C,v $
// $Revision: 1.25 $
// $Author: langer $
// $Date: 2010/11/08 22:05:19 $


/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/cmicrostructure.h"
#include "common/trace.h"
#include "engine/material.h"
#include "engine/property/orientation/orientation.h"
#include "engine/symmmatrix.h"

OrientationProp::OrientationProp(PyObject *registry, const std::string &nm,
				 const COrientation *orient)
  : OrientationPropBase(registry,nm),
    orient(orient)
{}

OrientationProp::~OrientationProp() {}

const COrientation *OrientationProp::orientation(const FEMesh*, const Element*,
						 const MasterPosition&) const
{
  return orient;
}

const COrientation *OrientationProp::orientation(const CMicrostructure*,
						 const ICoord &) const
{
  return orient;
}

// From the comments in eulerangle.C:
// ... The rotation matrix multiplied by a vector gives the
// coordinates of the vector in a coordinate system that has been
// rotated by the Euler angle.


// SmallMatrix OrientationProp::rotate(const SmallMatrix &A) const {
//   Trace("OrientationProp::rotate");
//   SmallMatrix rot = eulerangle().rotation();
//   return transform(A, rot); // rot.A.(rot-transpose), from mvmult.h
// }

// SymmMatrix3 OrientationProp::rotate(const SymmMatrix3 &A) const {
//   SmallMatrix a(3,3);
//   for(int i=0; i<3; i++)
//     for(int j=0; j<3; j++)
//       a(i,j) = A(i,j);
//   SmallMatrix rotated_a = rotate(a);
//   SymmMatrix3 result;
//   for(int i=0; i<3; i++)
//     for(int j=i; j<3; j++)
//       result(i,j) = rotated_a(i,j);
//   return result;
// }

// VECTOR_D OrientationProp::rotate(const VECTOR_D &x) const {
//   return eulerangle().rotation()*x;
// }
