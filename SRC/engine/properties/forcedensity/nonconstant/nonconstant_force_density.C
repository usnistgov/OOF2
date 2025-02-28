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

#include "common/coord.h"
#include "nonconstant_force_density.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/equation.h"
#include "engine/indextypes.h"
#include "engine/material.h"
#include "engine/femesh.h"
#include "common/trace.h"
#include "common/ooferror.h"


NonconstantForceDensity::NonconstantForceDensity(const std::string &nm,
						 PyObject *reg)
  : EqnProperty(nm, reg)
{
  displacement = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
  stress_flux  = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}

void NonconstantForceDensity::precompute(FEMesh*) {
}

int NonconstantForceDensity::integration_order(const CSubProblem*,
					       const Element *el)
  const
{
  return el->shapefun_degree();
}

void NonconstantForceDensity::force_value(const FEMesh *mesh,
					  const Element *element,
					  const Equation *eqn,
					  const MasterPosition &masterpos,
					  double time, void*,
					  SmallSystem *eqndata) const
{
  Coord  coord = element->from_master(masterpos);
  const DoubleVec force = nonconst_force_density(coord, time);
  eqndata->forceVector() += force;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

inline double SQR(double x) { return x*x; }
inline double CUBE(double x) { return x*x*x; }


DoubleVec TestNonconstantForceDensity::nonconst_force_density_1(
					      const Coord &pt, double time)
  const
{
  double m0 = 2.0;
  double n0 = 3.0;
  double m1 = 1.0;
  double n1 = 2.0;
  double x = pt[0];
  double y = pt[1];

  return {
    (m0*m0 + n0*n0) * SQR(M_PI) * sin(m0*M_PI*x) * sin(n0*M_PI*y),
    (m1*m1 + n1*n1) * SQR(M_PI) * sin(m1*M_PI*x) * sin(n1*M_PI*y)
  };

}


DoubleVec TestNonconstantForceDensity::nonconst_force_density_2(
                                     const Coord &pt, double time)
  const
{
  double c0 = -0.5;
  double m0 = 2.0;
  double n0 = 3.0;
  double c1 = -1.5;
  double m1 = 1.0;
  double n1 = 2.0;
  double x = pt[0];
  double y = pt[1];

  double soln0 = exp(c0*time) * sin(m0*M_PI*x) * sin(n0*M_PI*y);
  double soln1 = exp(c1*time) * sin(m1*M_PI*x) * sin(n1*M_PI*y);

  return {
    (c0*c0 + (m0*m0 + n0*n0)*M_PI*M_PI) * soln0,
    (c1*c1 + (m1*m1 + n1*n1)*M_PI*M_PI) * soln1
  };

} 


DoubleVec TestNonconstantForceDensity::nonconst_force_density_3(
						const Coord &pt, double time)
  const
{
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];

  // U(x,y) = sin(m*pi*x) * sin(n*pi*y)
  double Ux  =  m*M_PI * cos(m*M_PI*x) * sin(n*M_PI*y);
  double Uxx = -SQR(m*M_PI) * sin(m*M_PI*x) * sin(n*M_PI*y);
  double Uyy = -SQR(n*M_PI) * sin(m*M_PI*x) * sin(n*M_PI*y);
  double Uyx =  m*M_PI*n*M_PI * cos(m*M_PI*x) * cos(n*M_PI*y);

  // V(x,y) = x^2 + y^2
  double Vy  =  2.0*y;
  double Vxx =  2.0;
  double Vyy =  2.0;
  double Vxy =  0.0;

  return {
    -((1.0 + 3.0*Ux*Ux)*Uxx + Uyy + Vxy),
    -(Vxx + (1.0 + 3.0*Vy*Vy)*Vyy + Uyx)
  };
} 


DoubleVec TestNonconstantForceDensity::nonconst_force_density_4(
						const Coord &pt, double time)
  const
{
  double m = 2.0;
  double n = 3.0;
  double c1=0.05;
  double c2=0.05;
  double x = pt[0];
  double y = pt[1];

  // U(x,y) = c1 * sin(m*pi*x) * sin(n*pi*y)
  double Ux  =  c1 * m*M_PI * cos(m*M_PI*x) * sin(n*M_PI*y);
  double Uy  =  c1 * n*M_PI * sin(m*M_PI*x) * cos(n*M_PI*y);
  double ddU = -c1 * (m*m + n*n)*M_PI*M_PI * sin(m*M_PI*x) * sin(n*M_PI*y);

  // V(x,y) = c2 * (x^2 + y^2)
  double Vx  = c2 * 2.0*x;
  double Vy  = c2 * 2.0*y;
  double ddV = c2 * 4.0;

  return {
    -((1.0 + Ux)*ddU + Vx*ddV),
    -(Uy*ddU + (1.0 + Vy)*ddV)
  };

} 


DoubleVec TestNonconstantForceDensity::nonconst_force_density_5(
						const Coord &pt, double time)
  const
{
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];

  // U0(x,y) = sin(m*pi*x) * sin(n*pi*y),  U1(x,y) = x^2 + y^2, // displacement field
  double U0x  =  m*M_PI * cos(m*M_PI*x) * sin(n*M_PI*y);
  double U0xx = -m*M_PI*m*M_PI * sin(m*M_PI*x) * sin(n*M_PI*y);
  double U0xy =  m*M_PI*n*M_PI * cos(m*M_PI*x) * cos(n*M_PI*y);
  double U0yx =  n*M_PI*m*M_PI * cos(m*M_PI*x) * cos(n*M_PI*y);
  double U0yy = -n*M_PI*n*M_PI * sin(m*M_PI*x) * sin(n*M_PI*y);
  double U1y  =  m*M_PI * sin(n*M_PI*x) * cos(m*M_PI*y);
  double U1xx = -n*M_PI*n*M_PI * sin(n*M_PI*x) * sin(m*M_PI*y);
  double U1xy =  n*M_PI*m*M_PI * cos(n*M_PI*x) * cos(m*M_PI*y);
  double U1yx =  m*M_PI*n*M_PI * cos(n*M_PI*x) * cos(m*M_PI*y);
  double U1yy = -m*M_PI*m*M_PI * sin(n*M_PI*x) * sin(m*M_PI*y);
//   U1y  =  2.0*y;
//   U1xx =  U1yy = 2.0;
//   U1xy =  U1yx = 0.0;

  // V0 = -tan(dU0/dx/20),  V1 = -tan(dU1/dy / 20),
  // V2 = -tan((dU0/dx + dU1/dy) / 20),  // z-derivs of displacement
  double V0x = -(1.0 + SQR(tan(U0x/20.0))) * U0xx / 20.0;
  double V1y = -(1.0 + SQR(tan(U1y/20.0))) * U1yy / 20.0;
  double V2x = -(1.0 + SQR(tan((U0x+U1y)/20.0))) * (U0xx + U1yx) / 20.0;
  double V2y = -(1.0 + SQR(tan((U0x+U1y)/20.0))) * (U0xy + U1yy) / 20.0;
//   V0x = -U0xx / 20.0;
//   V1y = -U1yy / 20.0;
//   V2x = -(U0xx + U1yx) / 20.0;
//   V2y = -(U0xy + U1yy) / 20.0;

  return {
    -((1.0 + 3.0*U0x*U0x)*U0xx + (V0x + V2x)/20.0 + U0yy),
    -(U1xx + (1.0 + 3.0*U1y*U1y)*U1yy + (V1y + V2y)/20.0)
  };

} 

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

DoubleVec TestNonconstantForceDensity::nonconst_force_density(
					      const Coord &pt, double time)
  const
{
  switch (testNo)
  {
    case 1:
      return nonconst_force_density_1(pt, time);
    case 2:
      return nonconst_force_density_2(pt, time);
    case 3:
      return nonconst_force_density_3(pt, time);
    case 4:
      return nonconst_force_density_4(pt, time);
    case 5:
      return nonconst_force_density_5(pt, time);
  }
  return DoubleVec(2, 0.0);

} 

