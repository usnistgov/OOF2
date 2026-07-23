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
#include "common/coord.h"
#include "common/doublevec.h"
#include "common/smallmatrix.h"
#include "common/tostring.h"
#include "engine/cnonlinearsolver.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/field.h"
#include "engine/fieldindex.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "engine/nodalequation.h"
#include "engine/properties/heatconductivity/nonlinear/nonlinear_heat_conductivity.h"
#include "engine/properties/orientation/orientation.h"
#include "engine/smallsystem.h"
#include <iostream>
#include <fstream>
#include <string>


NonlinearHeatConductivity::NonlinearHeatConductivity(const std::string &nm,
						     PyObject *reg)
  : FluxProperty(nm, reg)
{
  temperature = dynamic_cast<ScalarField*>(Field::getField("Temperature"));
  heat_flux = dynamic_cast<VectorFlux*>(Flux::getFlux("Heat_Flux"));
}


int NonlinearHeatConductivity::integration_order(const CSubProblem *subp,
						 const Element *el) const
{
  if(temperature->in_plane(subp))
    return el->dshapefun_degree(); 
  return el->shapefun_degree();
}


void NonlinearHeatConductivity::flux_value(const FEMesh *mesh,
					   const Element *element,
					   const Flux *flux,
					   const MasterPosition &pt,
					   double time, void*, 
					   SmallSystem *fluxdata)
  const
{
  // first evaluate the temperature field and the temperature gradient
  double fieldValue = temperature->value(mesh, element, pt);
  DoubleVec fieldGradient = temperature->gradient(mesh, element, pt);

  // evaluate the value of the flux with the given pt, time and
  // temperature field
  Coord coord = element->from_master(pt);
  DoubleVec fluxVector = nonlin_heat_flux(coord, time,
					  fieldValue, fieldGradient);
  // add the heat flux contribution to the small system 'fluxdata',
  // which will later be added to the global div_flux vector
  fluxdata->fluxVector() += fluxVector;
}


void NonlinearHeatConductivity::flux_matrix(const FEMesh *mesh,
					    const Element *element,
					    const ElementFuncNodeIterator &j,
					    const Flux *flux,
					    const MasterPosition &pt,
					    double time,
					    void*,
					    SmallSystem *fluxdata)
  const
{
  // check for unexpected flux, should be heat flux
  if (*flux != *heat_flux) {
    throw ErrProgrammingError("Unexpected flux", __FILE__, __LINE__);
  }

  // first evaluate the temperature field and the temperature gradient

  double fieldValue = temperature->value(mesh, element, pt);
  DoubleVec fieldGradient = temperature->gradient(mesh, element, pt);

  // evaluate the value of the flux derivatives with the given pt,
  // time, temperature etc

  Coord coord = element->from_master(pt);

  // the derivative of the heat flux mapping w.r.t. temperature
  DoubleVec fluxDerivVec =
    nonlin_heat_flux_deriv_wrt_temperature(
				   coord, time, fieldValue, fieldGradient);

  // the derivative of the heat flux mapping w.r.t. temperature gradient
  SmallMatrix fluxDerivMtx =
    nonlin_heat_flux_deriv_wrt_temperature_gradient(
				    coord, time, fieldValue, fieldGradient);

  // evaluate the shape function and its gradient of given node j at given pt
  double shapeFuncVal = j.shapefunction(pt);
  double shapeFuncGrad[] = {j.dshapefunction(0, pt), j.dshapefunction(1, pt)};

  // Loop over flux components.  Loop over all components, even if
  // the flux is in-plane, because the out-of-plane components of
  // the flux matrix are used to construct the constraint equation.
  for(IndexP i : *flux->components(ALL_INDICES)) {
    // in-plane temperature gradient contributions
    fluxdata->stiffness_matrix_element(i, temperature, j)
               += fluxDerivVec[i] * shapeFuncVal +
                  fluxDerivMtx(i, 0) * shapeFuncGrad[0] +
                  fluxDerivMtx(i, 1) * shapeFuncGrad[1];

    if (!temperature->in_plane(mesh))
      fluxdata->stiffness_matrix_element(i, temperature->out_of_plane(), j)
	+= fluxDerivMtx(i, 2) * shapeFuncVal;

  }
} // end of 'NonlinearHeatConductivity::flux_matrix'



//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

inline double SQR(double x){ return x*x; }
inline double CUBE(double x){ return x*x*x; }


DoubleVec nonlin_heat_flux_1(const Coord &pt,
			     double time, double temperature,
			     const DoubleVec &gradtemp)
{
  return {
    -gradtemp[0] - CUBE(gradtemp[0]) / 3.0,
    -gradtemp[1] - pow(gradtemp[1], 5.0)/50.0,
    0.0
  };
}


DoubleVec nonlin_heat_flux_deriv_wrt_temperature_1(
			      const Coord &pt,
			      double time, double temperature,
			      const DoubleVec &gradtemp)
{
  return DoubleVec(3);
}


SmallMatrix nonlin_heat_flux_deriv_wrt_temperature_gradient_1(
				       const Coord &pt,
				       double time, double temperature,
				       const DoubleVec &gradtemp)
{
  SmallMatrix heat_flux_deriv(3);
  heat_flux_deriv(0,0) = -1.0 - SQR(gradtemp[0]);
  heat_flux_deriv(1,1) = -1.0 - pow(gradtemp[1], 4.0) / 10.0;
  return heat_flux_deriv;
}


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


DoubleVec nonlin_heat_flux_2(const Coord &pt,
			     double time, double temperature,
			     const DoubleVec &gradtemp)
{
  return {
   -gradtemp[0] - CUBE(gradtemp[0]) -gradtemp[2] / 20.0,
   -gradtemp[1] - CUBE(gradtemp[1]) -gradtemp[2] / 20.0,
   -gradtemp[0]/20.0 - gradtemp[1]/20.0 - atan(gradtemp[2])
  };
}


DoubleVec nonlin_heat_flux_deriv_wrt_temperature_2(
			   const Coord &pt, double time, double temperature,
			   const DoubleVec &gradtemp)
{
  return DoubleVec(3);
} 


SmallMatrix nonlin_heat_flux_deriv_wrt_temperature_gradient_2(
			      const Coord &pt, double time, double temperature,
			      const DoubleVec &gradtemp)
{
  SmallMatrix heat_flux_deriv(3);
  heat_flux_deriv.clear();
  heat_flux_deriv(0,0) = -1.0 - 3.0 * SQR(gradtemp[0]);
  heat_flux_deriv(0,1) =  0.0;
  heat_flux_deriv(0,2) = -1.0 / 20.0;

  heat_flux_deriv(1,0) =  0.0;
  heat_flux_deriv(1,1) = -1.0 - 3.0 * SQR(gradtemp[1]);
  heat_flux_deriv(1,2) = -1.0 / 20.0;

  heat_flux_deriv(2,0) = -1.0 / 20.0;
  heat_flux_deriv(2,1) = -1.0 / 20.0;
  heat_flux_deriv(2,2) = -1.0 / (1.0 + SQR(gradtemp[2]));
  return heat_flux_deriv;
} 


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

DoubleVec nonlin_heat_flux_3(const Coord &pt,
			     double time, double temperature,
			     const DoubleVec &gradtemp)
{
  DoubleVec heat_flux(3);
  heat_flux[0] = -atan(gradtemp[0]);
  heat_flux[1] = -atan(gradtemp[1]);
  heat_flux[2] =  0.0;
  return heat_flux;
} 

DoubleVec nonlin_heat_flux_deriv_wrt_temperature_3(
			   const Coord &pt, double time, double temperature,
			   const DoubleVec &gradtemp)
{
  return DoubleVec(3);
}

SmallMatrix nonlin_heat_flux_deriv_wrt_temperature_gradient_3(
		      const Coord &pt, double time, double temperature,
		      const DoubleVec &gradtemp)
{
  SmallMatrix heat_flux_deriv(3);
  heat_flux_deriv(0,0) = -1.0 / (1.0 + SQR(gradtemp[0]));
  heat_flux_deriv(1,1) = -1.0 / (1.0 + SQR(gradtemp[1]));
  return heat_flux_deriv;
}

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


DoubleVec TestNonlinearHeatConductivity::nonlin_heat_flux(
			     const Coord &pt, double time, double temperature,
			     const DoubleVec &gradtemp)
  const
{
  switch(testNo) {
  case 1:
    return nonlin_heat_flux_1(pt, time, temperature, gradtemp);
  case 2:
    return nonlin_heat_flux_2(pt, time, temperature, gradtemp);
  case 3:
    return nonlin_heat_flux_3(pt, time, temperature, gradtemp);
  }
  return DoubleVec(3);
} 


DoubleVec TestNonlinearHeatConductivity::nonlin_heat_flux_deriv_wrt_temperature(
			const Coord &pt, double time, double temperature,
			const DoubleVec &gradtemp) const
{
  switch(testNo) {
  case 1:
    return nonlin_heat_flux_deriv_wrt_temperature_1(
					    pt, time, temperature, gradtemp);
  case 2:
    return nonlin_heat_flux_deriv_wrt_temperature_2(
					    pt, time, temperature, gradtemp);
  case 3:
    return nonlin_heat_flux_deriv_wrt_temperature_3(
					    pt, time, temperature, gradtemp);
  }
  return DoubleVec(3);
} 

SmallMatrix
TestNonlinearHeatConductivity::nonlin_heat_flux_deriv_wrt_temperature_gradient(
			    const Coord &pt, double time, double temperature,
			    const DoubleVec &gradtemp) const
{
  switch(testNo) {
  case 1:
    return nonlin_heat_flux_deriv_wrt_temperature_gradient_1(
					     pt, time, temperature, gradtemp);
  case 2:
    return nonlin_heat_flux_deriv_wrt_temperature_gradient_2(
					     pt, time, temperature, gradtemp);
  case 3:
    return nonlin_heat_flux_deriv_wrt_temperature_gradient_3(
					     pt, time, temperature, gradtemp);
  }
  return SmallMatrix(3);
} 

