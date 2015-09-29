// -*- C++ -*-
// $RCSfile: direction.C,v $
// $Revision: 1.1 $
// $Author: langer $
// $Date: 2012/02/28 18:39:37 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "common/direction.h"
#include "common/ooferror.h"
#include "common/smallmatrix.h"
#include "common/corientation.h"
#include "common/doublevec.h"

#include <math.h>

// CUnitVectorDirection Direction::rotate(const COrientation &orientation) const {
//   return rotate(orientation.rotation());
// }

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

static void normalize(double &x, double &y, double &z) {
  double n2 = x*x + y*y + z*z;
  if(n2 == 0)
    throw ErrUserError("Direction vector has zero magnitude!");
  double n = sqrt(n2);
  x /= n;
  y /= n;
  z /= n;
}

CUnitVectorDirection::CUnitVectorDirection(double x, double y, double z)
  : vec(3)
{
  vec[0] = x;
  vec[1] = y;
  vec[2] = z;
  normalize(vec[0], vec[1], vec[2]);
}

CUnitVectorDirection::CUnitVectorDirection(const DoubleVec *xyz)
  : vec(*xyz)
{
  normalize(vec[0], vec[1], vec[2]);
}

double CUnitVectorDirection::theta() const {
  return acos(vec[2]);
}

double CUnitVectorDirection::phi() const {
  return atan2(vec[1], vec[0]);
}

CAngleDirection CUnitVectorDirection::angles() const {
  return CAngleDirection(theta(), phi());
}

CUnitVectorDirection CUnitVectorDirection::matmult(const SmallMatrix &rmatrix)
const
{
  DoubleVec prod = rmatrix*vec;
  return CUnitVectorDirection(&prod);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CAngleDirection::CAngleDirection(double theta, double phi)
  : theta_(theta),
    phi_(phi)
{}

CUnitVectorDirection CAngleDirection::unitVector() const {
  double rxy = sin(theta_);
  return CUnitVectorDirection(rxy*cos(phi_), rxy*sin(phi_), cos(theta_));
}

CUnitVectorDirection CAngleDirection::matmult(const SmallMatrix &rmatrix) const 
{
  return unitVector().matmult(rmatrix);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

CUnitVectorDirection operator*(const SmallMatrix &mat, const CDirection &v) {
  return v.matmult(mat);
}
