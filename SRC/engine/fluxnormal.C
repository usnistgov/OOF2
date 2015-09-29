// -*- C++ -*-
// $RCSfile: fluxnormal.C,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2011/01/19 16:03:55 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

// Support routines for the generic access method for the FluxNormal
// derived classes.  These are so that you can still query the 
// values even if you're not sure which type you've gotten.

#include "engine/fluxnormal.h"
#include "engine/ooferror.h"


double VectorFluxNormal::operator[](int n) const {
  if(n==0) 
    return val_;
  else
    return 0.0;  // Throw a range error or something.
}

double SymTensorFluxNormal::operator[](int n) const {
  switch(n) {
  case 0: 
    return x;
    break;
  case 1:
    return y;
    break;
  default:
    throw ErrProgrammingError("Bad index for SymTensorFluxNormal", __FILE__, 
			      __LINE__);
  }
}

// n is the boundary frame's x-axis, given in lab-frame coordinates.
// Use this to transform the given x and y, given in boundary-frame
// coordinates, into lab coordinates.
void SymTensorFluxNormal::transform(const Coord &n) {
  double normal_frame_x = x;
  double normal_frame_y = y;
  x=n(0)*normal_frame_x-n(1)*normal_frame_y;
  y=n(0)*normal_frame_y+n(1)*normal_frame_x;
}
