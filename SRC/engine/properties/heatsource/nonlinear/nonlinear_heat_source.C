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
#include "common/cleverptr.h"
#include "common/ooferror.h"
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
#include "engine/cnonlinearsolver.h"

#include "nonlinear_heat_source.h"

NonlinearHeatSourceNoDeriv::NonlinearHeatSourceNoDeriv(const std::string &name,
						       PyObject *reg)
  : EqnProperty(name, reg)
{
  temperature = dynamic_cast<ScalarField*>(Field::getField("Temperature"));
  heat_flux   = dynamic_cast<VectorFlux*>(Flux::getFlux("Heat_Flux"));
}

int NonlinearHeatSourceNoDeriv::integration_order(const CSubProblem *,
						  const Element *el)
  const
{
  return el->shapefun_degree();
}


void NonlinearHeatSourceNoDeriv::force_value(const FEMesh *mesh,
					     const Element *element,
					     const Equation *eqn,
					     const MasterPosition &pt,
					     double time, void*,
					     SmallSystem *eqndata) const
{
  double fieldVal = temperature->value(mesh, element, pt);
  Coord coord = element->from_master(pt);
  double sourceVal = nonlin_heat_source(coord, time, fieldVal);
  eqndata->force_vector_element(0) = -sourceVal;

} // NonlinearHeatSourceNoDeriv::force_value

void NonlinearHeatSource::force_deriv_matrix(const FEMesh   *mesh,
					     const Element  *element,
					     const ElementFuncNodeIterator &j,
					     const Equation *eqn,
 					     const MasterPosition &point,
					     double time,
					     void*,
					     SmallSystem *eqndata) const
{
  Coord coord = element->from_master(point);
  double fieldVal = temperature->value(mesh, element, point);
  double funcDerivVal = nonlin_heat_source_deriv_wrt_temperature(
						 coord, time, fieldVal);

  for (IndexP eqncomp : *eqn->components())
    eqndata->force_deriv_matrix_element(eqncomp, temperature, j)
      -= funcDerivVal;

} 

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

inline double SQR(double x){ return x*x; }
inline double CUBE(double x){ return x*x*x; }


double nonlin_heat_source_1(const Coord &pt, double time, double temperature) {
  double source_value;
  double pi = M_PI, uex, f;
  double m = 2.0, n = 3.0;
  double x = pt[0];
  double y = pt[1];

  uex = sin(m*pi*x) * sin(n*pi*y);
  f = -(m*m + n*n)*pi*pi*uex + uex - CUBE(uex);
  source_value = -temperature + CUBE(temperature) + f;

  return source_value;

}


double nonlin_heat_source_deriv_wrt_temperature_1(
			  const Coord &pt, double time, double temperature)
{
  double source_deriv_value = -1.0 + 3.0 * SQR(temperature);
  return source_deriv_value;
}


double nonlin_heat_source_2(const Coord &pt, double time, double temperature) {
  double pi = M_PI, uex, f;
  double w = 1.5, m = 2.0, n = 3.0;
  double x = pt[0];
  double y = pt[1];

  uex = exp(-w*time) * sin(m*pi*x) * sin(n*pi*y);
  f = (w -(m*m + n*n)*pi*pi)*uex + uex - CUBE(uex);
  return -temperature + CUBE(temperature) + f;
}

double nonlin_heat_source_deriv_wrt_temperature_2(
			  const Coord &pt, double time, double temperature)
{
  return -1.0 + 3.0 * SQR(temperature);
}

double nonlin_heat_source_3(const Coord &pt, double time, double temperature)
{
  return 4.0*exp(temperature);
}

double nonlin_heat_source_deriv_wrt_temperature_3(
			  const Coord &pt, double time, double temperature)
{
  return 4.0 * exp(temperature);
}

double nonlin_heat_source_4(const Coord &pt, double time, double temperature)
{
  return 2.0 * CUBE(temperature);
}

double nonlin_heat_source_deriv_wrt_temperature_4(
			  const Coord &pt, double time, double temperature)
{
  return 6.0 * SQR(temperature);
}

double nonlin_heat_source_5(const Coord &pt, double time, double temperature)
{
  return -2.0 + 8.0 * exp(2.0 * temperature);
}

double nonlin_heat_source_deriv_wrt_temperature_5(
			  const Coord &pt, double time, double temperature)
{
  return 16.0 * exp(2.0 * temperature);
}


double TestNonlinearHeatSourceNoDeriv::nonlin_heat_source(
			  const Coord &pt, double time, double temperature)
  const
{
  switch (testNo) {
  case 1:
    return -nonlin_heat_source_1(pt, time, temperature);
  case 2:
    return -nonlin_heat_source_2(pt, time, temperature);
  case 3:
    return -nonlin_heat_source_3(pt, time, temperature);
  case 4:
    return -nonlin_heat_source_4(pt, time, temperature);
  case 5:
    return -nonlin_heat_source_5(pt, time, temperature);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
} 


double TestNonlinearHeatSource::nonlin_heat_source(
		   const Coord &pt, double time, double temperature)
  const
{
  switch (testNo) {
  case 1:
    return -nonlin_heat_source_1(pt, time, temperature);
  case 2:
    return -nonlin_heat_source_2(pt, time, temperature);
  case 3:
    return -nonlin_heat_source_3(pt, time, temperature);
  case 4:
    return -nonlin_heat_source_4(pt, time, temperature);
  case 5:
    return -nonlin_heat_source_5(pt, time, temperature);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
}


double TestNonlinearHeatSource::nonlin_heat_source_deriv_wrt_temperature(
			 const Coord &pt, double time, double temperature)
  const
{
  switch (testNo) {
  case 1:
    return -nonlin_heat_source_deriv_wrt_temperature_1(pt, time, temperature);
  case 2:
    return -nonlin_heat_source_deriv_wrt_temperature_2(pt, time, temperature);
  case 3:
    return -nonlin_heat_source_deriv_wrt_temperature_3(pt, time, temperature);
  case 4:
    return -nonlin_heat_source_deriv_wrt_temperature_4(pt, time, temperature);
  case 5:
    return -nonlin_heat_source_deriv_wrt_temperature_5(pt, time, temperature);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
}
