// -*- C++ -*-
// $RCSfile: newgabor.h,v $
// $Revision: 1.3 $
// $Author: langer $
// $Date: 2014/09/27 21:41:35 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>
/*
Gabor filter. More information on it can be found at image/GRAINBDY/SummerWorkSummary.txt
RG(x,y)=w(x,y)*f(x,y), where:
w(x,y)=exp[-PI*(x'^2/a^2+y'^2/b^2)] and
f(x,y)=cos[2*pi*omega*r*cos(theta-phi).

Definition of given values. Phi is derived in thresholding.C
a: This specifies the width of edges in pixels.
b: This parameter determines the importance of straight lines. A
higher b value reduces amounts of noised added and gives longer
boundaries stronger responses.
numAngles: This determines the number of angles the filter should be
oriented and applied to the image. Lines parallel to the orientation
of the y-axis of the filter have the strongest signals, so a
sufficiently large number of angles to rotate the filter is necessary
to detect lines of all orientations. The suggested number is 4 or 6.
*/
#ifndef NEWGABORY_H
#define NEWGABORY_H

#include "mask.h"
#include "common/doublearray.h"

class NewGB
{
private:
	int a;
	int b;
	double phi;
public:
  NewGB(int a, int b, double phi); 
  DoubleArray apply(DoubleArray curr);
  virtual ~NewGB() {}
};

#endif //NEWGABOR_H
 
