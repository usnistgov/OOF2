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
#include "common/tostring.h"
#include "engine/ooferror.h"
#include <iostream>

ErrNoSuchProperty::ErrNoSuchProperty(const std::string &mat,
				     const std::string &prop)
  : ErrUserErrorBase<ErrNoSuchProperty>(
         "Material \"" + mat + "\" has no property of type \"" + prop + "\"."),
    material(mat),
    propname(prop)
{} 

ErrConvergenceFailure::ErrConvergenceFailure(const std::string &op, int n)
  : ErrUserErrorBase<ErrConvergenceFailure>(
	    op + " failed to converge in " + to_string(n) + " steps"),
      operation(op), nsteps(n)
{}

ErrTimeStepTooSmall::ErrTimeStepTooSmall(double timestep)
  : ErrUserErrorBase<ErrTimeStepTooSmall>(
		     "Timestep " + to_string(timestep) + " is too small."
					  ),
    timestep(timestep)
{}

ErrBadMaterial::ErrBadMaterial(const std::string &name)
  : ErrUserErrorBase<ErrBadMaterial>(
		     "Material \"" + name + "\" is badly formed."),
    name(name)
{}

const std::string &ErrNoSuchField::classname() const {
  static std::string s("ErrNoSuchField");
  return s;
}

const std::string &ErrDuplicateField::classname() const {
  static std::string s("ErrDuplicateField");
  return s;
}

const std::string &ErrNoSuchProperty::classname() const {
  static std::string s("ErrNoSuchProperty");
  return s;
}

const std::string &ErrPropertyMissing::classname() const {
  static std::string s("ErrPropertyMissing");
  return s;
}

const std::string &ErrRedundantProperty::classname() const {
  static std::string s("ErrRedundantProperty");
  return s;
}

const std::string &ErrBadMaterial::classname() const {
  static std::string s("ErrBadMaterial");
  return s;
}

const std::string &ErrConvergenceFailure::classname() const {
  static std::string s("ErrConvergenceFailure");
  return s;
}

const std::string &ErrTimeStepTooSmall::classname() const {
  static std::string s("ErrTimeStepTooSmall");
  return s;
}

const std::string &ErrInvalidDestination::classname() const {
  static std::string s("ErrInvalidDestination");
  return s;
}
