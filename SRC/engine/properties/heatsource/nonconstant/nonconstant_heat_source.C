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
#include "nonconstant_heat_source.h"
#include "common/tostring.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/fieldindex.h"
#include "engine/material.h"
#include "engine/properties/orientation/orientation.h"
#include "engine/smallsystem.h"
#include "engine/nodalequation.h"





NonconstantHeatSource::NonconstantHeatSource(const std::string &name,
					     PyObject *reg)
  : EqnProperty(name,reg)
{
    heat_flux = dynamic_cast<VectorFlux*>(Flux::getFlux("Heat_Flux"));
}


int NonconstantHeatSource::integration_order(const CSubProblem *subp,
					     const Element *el) const
{
  return el->shapefun_degree();
}

void NonconstantHeatSource::force_value(const FEMesh *mesh,
					const Element *element,
					const Equation *eqn,
					const MasterPosition &masterpos,
					double time, void*, 
					SmallSystem *eqndata)
  const
{
  Coord coord = element->from_master(masterpos);
  eqndata->force_vector_element(0) -= nonconst_heat_source(coord, time);
}



//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


inline double SQR(double x){ return x*x; }
inline double CUBE(double x){ return x*x*x; }

static double pi = M_PI;
static double pi2 = M_PI*M_PI;


double TestNonconstantHeatSource::nonconst_heat_source_1(
                                  const Coord &pt, double time) const
{
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];

  return -(m*m + n*n) * SQR(pi) * sin(m*pi*x) * sin(n*pi*y);
} 


double TestNonconstantHeatSource::nonconst_heat_source_2(
                                  const Coord &pt, double time) const
{
  
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];

  double source_value  = -(m*m + n*n) * pi2 * sin(m*pi*x) * sin(n*pi*y);
  source_value -= SQR(m*pi* cos(m*pi*x)*sin(n*pi*y))
                  * SQR(m*pi) * sin(m*pi*x) * sin(n*pi*y);
  source_value -= pow(n*pi* sin(m*pi*x)*cos(n*pi*y), 4.0)
                  * SQR(n*pi) * sin(m*pi*x) * sin(n*pi*y) / 10.0;

  return source_value;
}


double TestNonconstantHeatSource::nonconst_heat_source_3(
                                  const Coord &pt, double time) const
{
  double w = -1.5;
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];

  return -(w + (m*m + n*n)*pi2) * exp(w*time) * sin(m*pi*x) * sin(n*pi*y);
}

double TestNonconstantHeatSource::nonconst_heat_source_4(
                                  const Coord &pt, double time) const
{
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];

  // nonlinear flux = -(Ux+Ux^3+Uz/20, Uy+Uy^3+Uz/20, Ux/20+Uy/20+arctan(Uz))
  double Ux =  m*pi * cos(m*pi*x) * sin(n*pi*y);
  double Uy =  n*pi * sin(m*pi*x) * cos(n*pi*y);
  double Uz = -tan((Ux + Uy) / 20.0);

  double Uxx = -m*m*pi2 * sin(m*pi*x) * sin(n*pi*y);
  double Uxy =  m*n*pi2 * cos(m*pi*x) * cos(n*pi*y);
  double Uyx =  Uxy;
  double Uyy = -n*n*pi2 * sin(m*pi*x) * sin(n*pi*y);

  double Uzx = -(1.0 + Uz*Uz) * (Uxx + Uyx) / 20.0;
  double Uzy = -(1.0 + Uz*Uz) * (Uxy + Uyy) / 20.0;

  // source = -div(flux) = -(d(flux0)/dx + d(flux1)/dy)
  return (1.0 + 3.0*Ux*Ux)*Uxx + Uzx/20.0 + (1.0 + 3.0*Uy*Uy)*Uyy + Uzy/20.0;
}


double TestNonconstantHeatSource::nonconst_heat_source_5(
                                  const Coord &pt, double time) const
{
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];
  
  double Ux  = m*pi * cos(m*pi*x) * sin(n*pi*y);
  double Uy  = n*pi * sin(m*pi*x) * cos(n*pi*y);

  double Uxx = -m*m*pi2 * sin(m*pi*x) * sin(n*pi*y);
  double Uyy = -n*n*pi2 * sin(m*pi*x) * sin(n*pi*y);

  return Uxx / (1.0 + SQR(Ux)) + Uyy / (1.0 + SQR(Uy));
}

double TestNonconstantHeatSource::nonconst_heat_source_6(
                                  const Coord &pt, double time) const
{
  double w = -1.5;
  double m = 2.0;
  double n = 3.0;
  double x = pt[0];
  double y = pt[1];

  double Ut  = w * exp(w*time) * sin(m*pi*x) * sin(n*pi*y);
  double Ux  = m*pi * exp(w*time) * cos(m*pi*x) * sin(n*pi*y);
  double Uy  = n*pi * exp(w*time) * sin(m*pi*x) * cos(n*pi*y);

  double Uxx = -m*m*pi2 * exp(w*time) * sin(m*pi*x) * sin(n*pi*y);
  double Uyy = -n*n*pi2 * exp(w*time) * sin(m*pi*x) * sin(n*pi*y);

  return -Ut + Uxx*(1.0 + Ux*Ux) + Uyy*(1.0 + pow(Uy,4.0)/10.0);
}

double TestNonconstantHeatSource::nonconst_heat_source_7(
                                  const Coord &pt, double t) const
{
  double w = 1.5;
  double m = 2.0;
  double n = 3.0;
  double k = 1;
  double x = pt[0];
  double y = pt[1];

  // U = sin(m*pi*x) * sin(n*pi*y) * sin(pi*(k*x - w*t))
  double Ut  = -pi*w * sin(m*pi*x) * sin(n*pi*y) * cos(pi*(k*x-w*t));

  double Ux  = m*pi * cos(m*pi*x) * sin(n*pi*y) * sin(pi*(k*x-w*t)) 
    + k*pi * sin(m*pi*x) * sin(n*pi*y) * cos(pi*(k*x - w*t));
  
  double Uxx = -(m*m + k*k)*pi2 * sin(m*pi*x) * sin(n*pi*y)* sin(n*pi*(x-w*t))
    + 2*m*k*pi2 * cos(m*pi*x) * sin(n*pi*y) * cos(pi*(k*x - w*t));
  
  double Uy  = n*pi * sin(m*pi*x) * cos(n*pi*y) * sin(pi*(k*x - w*t));
  double Uyy = -n*n*pi2 * sin(m*pi*x) * sin(n*pi*y) * sin(pi*(k*x-w*t));

  return -Ut + Uxx*(1.0 + Ux*Ux) + Uyy*(1.0 + pow(Uy,4.0)/10.0);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

#define AA 3

static double f(double x, double t) {
  //  return 0.5*(x-AA*t)*(x-AA*t);
  return exp(AA*t*x);
}

static double dfdx(double x, double t) {
  // return (x-AA*t);
  return AA*t*f(x,t);
}

static double d2fdx2(double x, double t) {
  // return 1;
  return (AA*AA*t*t)*f(x,t);
}

static double dfdt(double x, double t) {
  // return -AA*(x-AA*t);
  return AA*x*f(x,t);
}

double TestNonconstantHeatSource::nonconst_heat_source_8(
				    const Coord &pt, double t)
  const 
{
  // For T = (x^2 - x) (y^2 - y) f(x,t) and the nonlinear
  // conductivity given by
  // TestNonlinearHeatConductivity::nonlin_heat_flux1.
  double x = pt[0];
  double y = pt[1];
  double xx1 = x*x - x;
  double yy1 = y*y - y;
  double fxt = f(x,t);
  // The 100 is the heat capacity in TEST/nonlinear_K_timedep_tests.py.
  double Ut = 100*xx1 * yy1 * dfdt(x,t);
  double Ux = ((2*x-1)*fxt + xx1*dfdx(x,t)) * yy1;
  double Uxx = (2*fxt + 2*(2*x-1)*dfdx(x,t) + xx1*d2fdx2(x,t)) * yy1;
  double Uy = xx1*(2*y-1)*fxt;
  double Uyy = 2*xx1*fxt;

  return -Ut + Uxx*(1.0 + Ux*Ux) + Uyy*(1.0 + pow(Uy,4.0)/10.0);
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

double TestNonconstantHeatSource::nonconst_heat_source(
			       const Coord &pt, double time)
  const
{
  // The minus sign in all of these test functions is necessary
  // because the sign of the Qdot term in the heat equation changed
  // for version 2.1.2.
  switch (testNo) {
  case 1:
    return -nonconst_heat_source_1(pt, time);
  case 2:
    return -nonconst_heat_source_2(pt, time);
  case 3:
    return -nonconst_heat_source_3(pt, time);
  case 4:
    return -nonconst_heat_source_4(pt, time);
  case 5:
    return -nonconst_heat_source_5(pt, time);
  case 6:
    return -nonconst_heat_source_6(pt, time);
  case 7:
    return -nonconst_heat_source_7(pt, time);
  case 8:
    return -nonconst_heat_source_8(pt, time);
  }
  return 0.0;
}
