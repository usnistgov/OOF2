// -*- C++ -*-

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#ifndef CNONLINEARSOLVER_SWG
#define CNONLINEARSOLVER_SWG

%module(package="ooflib.SWIG.engine") cnonlinearsolver

#ifndef NOSECONDIMPORTS
#define NOSECONDIMPORTS
%include "common/typemaps.swg"
%import "common/timestamp.swg"
#endif // NOSECONDIMPORTS

%{
#include "engine/cnonlinearsolver.h"
%}

class CNonlinearSolver {
public:
  CNonlinearSolver(bool);
  bool nonlinear(); 
  void requireJacobian(bool);
  bool needsJacobian();
  const TimeStamp &jacobianRequirementChanged();
  void requireResidual(bool);
  bool needsResidual();
  const TimeStamp &residualRequirementChanged();
};

#endif // CNONLINEARSOLVER_SWG

