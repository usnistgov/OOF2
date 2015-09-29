// -*- C++ -*-
// $RCSfile: sincos.C,v $
// $Revision: 1.4 $
// $Author: reida $
// $Date: 2013/11/21 15:53:19 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
#include "common/sincos.h"

#include <math.h>

// Calclulage sin and cos together.  Used to be clever, using an 
// algorithm from Numerical Recipes, but this was slower on some systems,
// and the "finite()" operator was not portable.


void sincos(const double angle, double &sine, double &cosine) {
    sine = sin(angle);
    cosine = cos(angle);
}

//void sincos(const double angle, double &sine, double &cosine) {
//  double tn = tan(0.5*angle);
//  if(!finite(tn)) {
//    sine = sin(angle);
//    cosine = cos(angle);
//    return;
//  }
//  double tntn = 1./(1 + tn*tn);
//  cosine = (1 - tn*tn)*tntn;
//  sine = 2*tn*tntn;
//}
//
