// -*- C++ -*-
// $RCSfile: laplacianGauss.C,v $
// $Revision: 1.2 $
// $Author: langer $
// $Date: 2014/09/27 21:41:31 $

/* This software was produced by NIST, an agency of the U.S. government,
 * and by statute is not subject to copyright in the United States.
 * Recipients of this software assume all responsibilities associated
 * with its operation, modification and maintenance. However, to
 * facilitate maintenance we ask that before distributing modified
 * versions of this software, you first contact the authors at
 * oof_manager@nist.gov. 
 */

#include <oofconfig.h>

#include "laplacianGauss.h"

#include <math.h>
#include "mask.h"
#include "common/array.h"
#include "common/doublearray.h"

LaplacianGauss::LaplacianGauss(double stdDev)
  : MASK(9,9)
{
  double c1 = -1/(M_PI*stdDev*stdDev*stdDev*stdDev);
  double c2 = -1/(2*stdDev*stdDev);
  
  for(DoubleArray::iterator i=maskArray.begin();i!=maskArray.end();++i) {
    double  x=i.coord()(0)-4, y=i.coord()(1)-4;
    double temp = (x*x+y*y)*c2;
    maskArray[i]=c1*(1+temp)*exp(temp);
  }
}

