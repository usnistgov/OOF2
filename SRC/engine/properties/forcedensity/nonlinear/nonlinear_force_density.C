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
#include "common/cleverptr.h"
#include "common/coord.h"
#include "common/ooferror.h"
#include "common/smallmatrix.h"
#include "common/trace.h"
#include "engine/cnonlinearsolver.h"
#include "engine/cstrain.h"
#include "engine/csubproblem.h"
#include "engine/element.h"
#include "engine/elementnodeiterator.h"
#include "engine/equation.h"
#include "engine/femesh.h"
#include "engine/field.h"
#include "engine/flux.h"
#include "engine/material.h"
#include "nonlinear_force_density.h"

// TODO: The NonLinearForceDensityNoDeriv base class was for testing
// the numerical differentation that used to be supported, when users
// didn't want to write the derivative classes.  It's not supported
// any more, because it was too flaky.  The base class should be
// merged into NonlinearForceDensity.

NonlinearForceDensityNoDeriv::NonlinearForceDensityNoDeriv(
						   const std::string &nm,
						   PyObject *reg)
  : EqnProperty(nm,reg)
{
  displacement = dynamic_cast<TwoVectorField*>(Field::getField("Displacement"));
  stress_flux  = dynamic_cast<SymmetricTensorFlux*>(Flux::getFlux("Stress"));
}

void NonlinearForceDensityNoDeriv::precompute(FEMesh*) {
}

int NonlinearForceDensityNoDeriv::integration_order(const CSubProblem*,
						    const Element *el)
  const
{
  return el->shapefun_degree();
}


void NonlinearForceDensityNoDeriv::force_value(
			      const FEMesh *mesh, const Element *element,
			      const Equation *eqn, const MasterPosition &point,
			      double time, void*,
			      SmallSystem *eqndata) const
{
  // first compute the current value of the displacement field at the
  // gauss point
  DoubleVec fieldVal = displacement->values(mesh, element, point);

  // now compute the force density value for the current coordinate x,y,z,
  // time and displacement,
  // the nonlinear force density function returns the corresponding
  // force value in the array 'force',

  Coord coord = element->from_master(point);
  DoubleVec force = nonlin_force_density(coord, time, fieldVal);
  
  eqndata->forceVector() += force;

} // end of 'NonlinearForceDensityNoDeriv::force_value'


void NonlinearForceDensity::force_deriv_matrix(const FEMesh *mesh,
					       const Element *element,
					       const ElementFuncNodeIterator &j,
					       const Equation *eqn,
					       const MasterPosition &point,
					       double time, void*,
					       SmallSystem *eqndata) const
{
  // first compute the current value of the displacement field at the
  // gauss point
  DoubleVec fieldVal = displacement->values(mesh, element, point);

  // now compute the value of the force density derivative function
  // for the current coordinate x,y,z, time and displacement, the
  // nonlinear force density derivative function returns the
  // corresponding force derivative value in the array 'forceDeriv'.

  Coord coord = element->from_master(point);
  SmallMatrix forceDeriv = nonlin_force_density_deriv(coord, time, fieldVal);
  
  for(IndexP eqncomp : *eqn->components()) {
    for (IndexP fieldcomp : *displacement->components(ALL_INDICES)) {
      eqndata->force_deriv_matrix_element(eqncomp, displacement, fieldcomp, j)
	+= forceDeriv(eqncomp, fieldcomp);
    }
  }
} // end of 'NonlinearForceDensity::force_deriv_matrix'


//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//


inline double SQR(double x){ return x*x; }
inline double CUBE(double x){ return x*x*x; }


DoubleVec nonlin_force_density_1(const Coord &pt, double time,
				 const DoubleVec &displacement)
{
  double x = pt[0];
  double y = pt[1];
  double pi = M_PI;
  double m0 = 2.0;
  double n0 = 3.0;
  double m1 = 1.0;
  double n1 = 2.0;

  double uex0 = sin(m0*pi*x) * sin(n0*pi*y);
  double uex1 = sin(m1*pi*x) * sin(n1*pi*y);

  double f0 = (m0*m0 + n0*n0)*pi*pi * uex0 - uex0 + CUBE(uex0);
  double f1 = (m1*m1 + n1*n1)*pi*pi * uex1 - uex1 + CUBE(uex1);

  return {
    displacement[0] - CUBE(displacement[0]) + f0,
    displacement[1] - CUBE(displacement[1]) + f1
  };
  
} 

SmallMatrix nonlin_force_density_deriv_1(const Coord &pt, double time,
					 const DoubleVec &displacement)
{
  SmallMatrix result(2);
  result(0,0) = 1.0 - 3.0 * SQR(displacement[0]);
  result(0,1) = 0.0;

  result(1,0) = 0.0;
  result(1,1) = 1.0 - 3.0 * SQR(displacement[1]);
  return result;
} 


DoubleVec nonlin_force_density_2(const Coord &pt, double time,
			    const DoubleVec &displacement)
{
  double x = pt[0];
  double y = pt[1];
  double pi = M_PI;
  double a0 =  2.0 ;
  double b0 = 3.0;
  double m0 = 2.0;
  double n0 = 3.0;
  double a1 = -4.0;
  double b1 = 5.0;
  double m1 = 1.0;
  double n1 = 2.0;

  double uex0 = (a0*time + b0) * sin(m0*pi*x) * sin(n0*pi*y);
  double uex1 = (a1*time + b1) * sin(m1*pi*x) * sin(n1*pi*y);

  double f0 = (m0*m0 + n0*n0)*pi*pi * uex0 - uex0 + CUBE(uex0);
  double f1 = (m1*m1 + n1*n1)*pi*pi * uex1 - uex1 + CUBE(uex1);

  return {
      displacement[0] - CUBE(displacement[0]) + f0,
      displacement[1] - CUBE(displacement[1]) + f1
  };
} 

SmallMatrix nonlin_force_density_deriv_2(const Coord &pt, double time,
					 const DoubleVec &displacement)
{
  SmallMatrix result(2);
  result(0,0) = 1.0 - 3.0 * SQR(displacement[0]);
  result(0,1) = 0.0;

  result(1,0) = 0.0;
  result(1,1) = 1.0 - 3.0 * SQR(displacement[1]);
  return result;
} 


DoubleVec nonlin_force_density_3(const Coord &pt, double time,
				 const DoubleVec &displacement)
{
  return {
    -4.0 * exp(displacement[0]),
    -5.0 * exp(2.0*displacement[1])
  };
} 

SmallMatrix nonlin_force_density_deriv_3(const Coord &pt, double time,
				  const DoubleVec &displacement)
{
  SmallMatrix result(2);
  result(0,0) = -4.0 * exp(displacement[0]);
  result(0,1) =  0.0;
  result(1,0) =  0.0;
  result(1,1) = -10.0 * exp(2.0*displacement[1]);
  return result;
}


DoubleVec nonlin_force_density_4(const Coord &pt, double time,
				 const DoubleVec &displacement)
{
  return {
    12.0 * exp(-0.25*displacement[0]) - 9.0*exp(-0.5*displacement[0]),
    -4.0 * SQR(displacement[1]) + 8.0 * CUBE(displacement[1])
  };
}

SmallMatrix nonlin_force_density_deriv_4(const Coord &pt, double time,
					 const DoubleVec &displacement)
{
  SmallMatrix result(2);
  result(0,0) = -3.0*exp(-0.25*displacement[0]) + 4.5*exp(-0.5*displacement[0]);
  result(0,1) =  0.0;
  result(1,0) =  0.0;
  result(1,1) = -8.0 * displacement[1] + 24.0 * SQR(displacement[1]);
  return result;
} 

//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//=\\=//

DoubleVec TestNonlinearForceDensity::nonlin_force_density(
	     const Coord &pt, double time, const DoubleVec &displacement)
  const
{
  switch (testNo) {
  case 1:
    return nonlin_force_density_1(pt, time, displacement);
  case 2:
    return nonlin_force_density_2(pt, time, displacement);
  case 3:
    return nonlin_force_density_3(pt, time, displacement);
  case 4:
    return nonlin_force_density_4(pt, time, displacement);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
}


DoubleVec TestNonlinearForceDensityNoDeriv::nonlin_force_density(
	    const Coord &pt, double time, const DoubleVec &displacement)
  const
{
  switch (testNo) {
  case 1:
    return nonlin_force_density_1(pt, time, displacement);
  case 2:
    return nonlin_force_density_2(pt, time, displacement);
  case 3:
    return nonlin_force_density_3(pt, time, displacement);
  case 4:
    return nonlin_force_density_4(pt, time, displacement);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
} 

SmallMatrix TestNonlinearForceDensity::nonlin_force_density_deriv(
		  const Coord &pt, double time, const DoubleVec &displacement)
  const
{
  switch (testNo) {
  case 1:
    return nonlin_force_density_deriv_1(pt, time, displacement);
  case 2:
    return nonlin_force_density_deriv_2(pt, time, displacement);
  case 3:
    return nonlin_force_density_deriv_3(pt, time, displacement);
  case 4:
    return nonlin_force_density_deriv_4(pt, time, displacement);
  }
  throw ErrProgrammingError("Bad test number", __FILE__, __LINE__);
}

