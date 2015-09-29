// -*- C++ -*-
// $RCSfile: nodalequation.C,v $
// $Revision: 1.11 $
// $Author: langer $
// $Date: 2010/09/16 19:24:38 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "nodalequation.h"

#include <iostream>

NodalEquation::NodalEquation(int n) 
  : index_(n)
{
}

std::ostream &operator<<(std::ostream &os, const NodalEquation &neqn) {
  return os << "[" << neqn.ndq_index() << "]";
}
