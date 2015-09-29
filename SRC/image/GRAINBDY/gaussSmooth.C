// -*- C++ -*-
// $RCSfile: gaussSmooth.C,v $
// $Revision: 1.5 $
// $Author: langer $
// $Date: 2014/09/27 21:41:29 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "gaussSmooth.h"

#include <math.h>
#include "mask.h"
#include "common/array.h"
#include "common/doublearray.h"

GaussSmooth::GaussSmooth(double stdDev)
  : MASK(4*int(stdDev)+1,4*int(stdDev)+1)
{
  double constant1=1./(2.*stdDev*stdDev);
  double constant2=constant1/M_PI;
  int M=4*int(stdDev)+1;
  for(DoubleArray::iterator i=maskArray.begin();i!=maskArray.end();++i) {
    double  x=i.coord()(0)-M/2, y=i.coord()(1)-M/2;
    maskArray[i]=constant2*exp(-(x*x+y*y)*constant1);
  }
}
